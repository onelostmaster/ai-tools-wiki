#!/usr/bin/env python3
"""Build the static wiki website from data/tools.json.

Usage:
    python3 -I site/build.py [DATA_PATH]

DATA_PATH defaults to data/tools.json at the repo root. Output goes to
site/dist/. Python standard library only.

The allow-list gate runs before anything is written. Any failure prints
every problem to stderr and exits with status 1, so a bad data file is
never published.
"""

import datetime
import hashlib
import html
import json
import os
import re
import shutil
import sys
import unicodedata
from pathlib import Path

SITE_DIR = Path(__file__).resolve().parent
REPO_ROOT = SITE_DIR.parent
DEFAULT_DATA = REPO_ROOT / "data" / "tools.json"
DIST = SITE_DIR / "dist"

TOP_LEVEL_KEYS = {"count", "tools"}
PUBLIC_FIELDS = (
    "Name",
    "Type",
    "Category",
    "Official URL",
    "GitHub repo",
    "Price",
    "Decision",
    "Safety verdict",
    "Safety basis",
    "Safety reason",
    "Safe install",
    "YOLO install",
    "Install notes",
    "Last checked",
)
VERDICTS = {"safe", "caution", "unreviewed", "avoid"}
NO_YOLO_VERDICTS = {"avoid", "unreviewed"}
ALLOWED_YOLO_FOR_NO_YOLO = {"", "Not offered."}
# Links to the private workspace tool. Escaped on purpose: the literal
# domains must not appear in this public repo.
NOTION_LINK = re.compile(
    r"(?<![a-z0-9-])(?:www\.)?notion\.so\b|app\.notion\.com|notion\.site\b", re.I
)
# Dots that browsers treat as a normal dot in a host name.
DOT_LOOKALIKES = str.maketrans({"\u3002": ".", "\uff0e": ".", "\uff61": "."})

CSP = "default-src 'self'"


class GateError(Exception):
    def __init__(self, problems):
        super().__init__("\n".join(problems))
        self.problems = problems


def iter_strings(value, path):
    """Yield (path, string) for every string anywhere inside value."""
    if isinstance(value, str):
        yield path, value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield path + "." + str(key), str(key)
            yield from iter_strings(item, path + "." + str(key))
    elif isinstance(value, list):
        for i, item in enumerate(value):
            yield from iter_strings(item, "%s[%d]" % (path, i))


def gate(data):
    """Return the list of tools if data passes the allow-list gate."""
    problems = []
    if not isinstance(data, dict):
        raise GateError(["top level is not a JSON object"])

    extra = sorted(set(data) - TOP_LEVEL_KEYS)
    if extra:
        problems.append("top-level keys not allowed: %s" % ", ".join(extra))

    tools = data.get("tools")
    if not isinstance(tools, list):
        problems.append("'tools' is missing or not a list")
        tools = []

    if not tools:
        problems.append("'tools' is empty: refusing to publish an empty site")

    count = data.get("count")
    if type(count) is not int:
        problems.append("count is missing or not a whole number: %r" % (count,))
    elif count != len(tools):
        problems.append("count is %d but tools has %d entries" % (count, len(tools)))

    for i, tool in enumerate(tools):
        label = "tools[%d]" % i
        if not isinstance(tool, dict):
            problems.append("%s is not an object" % label)
            continue
        name = tool.get("Name")
        if isinstance(name, str) and name:
            label = "%s (%s)" % (label, name)
        extra_fields = sorted(set(tool) - set(PUBLIC_FIELDS))
        if extra_fields:
            problems.append("%s: fields not allowed: %s" % (label, ", ".join(extra_fields)))
        for field in PUBLIC_FIELDS:
            value = tool.get(field, "")
            if not isinstance(value, str):
                problems.append("%s: field %r is not text" % (label, field))
        verdict = tool.get("Safety verdict", "")
        yolo = tool.get("YOLO install", "")
        if verdict not in VERDICTS:
            problems.append(
                "%s: Safety verdict %r is not one of %s" % (label, verdict, ", ".join(sorted(VERDICTS)))
            )
        if verdict in NO_YOLO_VERDICTS and yolo not in ALLOWED_YOLO_FOR_NO_YOLO:
            problems.append(
                "%s: YOLO install on an %s tool (only empty or 'Not offered.' allowed)" % (label, verdict)
            )

    for path, text in iter_strings(data, "$"):
        normal = unicodedata.normalize("NFKC", text).translate(DOT_LOOKALIKES)
        if NOTION_LINK.search(normal):
            problems.append("%s: contains a link to the private workspace" % path)

    if problems:
        raise GateError(problems)
    return tools


def git_blob_sha(raw):
    """Same id git gives this file's bytes (git hash-object)."""
    header = b"blob %d\0" % len(raw)
    return hashlib.sha1(header + raw).hexdigest()


def slugify(name, used):
    base = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "tool"
    slug, n = base, 2
    while slug in used:
        slug = "%s-%d" % (base, n)
        n += 1
    used.add(slug)
    return slug


def safe_url(text):
    """Return the leading http(s) URL of a value, or of a leading [label](url)
    Markdown link, else ''. Trailing notes such as "@ abc123 (MIT)" are ignored."""
    text = (text or "").strip()
    match = re.match(r"\[[^\]]*\]\((https?://[^)\s]+)\)", text)
    if match:
        text = match.group(1)
    match = re.match(r"https?://[^\s<>\"'()\[\]]+", text)
    return match.group(0) if match else ""


def esc(text):
    return html.escape(text or "", quote=True)


def page(title, body, css_href):
    return (
        "<!doctype html>\n"
        '<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "<title>%s</title>\n"
        '<link rel="stylesheet" href="%s">\n'
        "</head>\n<body>\n%s</body>\n</html>\n" % (esc(title), css_href, body)
    )


def tool_page(tool):
    get = lambda f: tool.get(f, "") or ""
    decision = get("Decision") or "Not decided"
    safe_install = get("Safe install")
    rows = [
        ("Type", get("Type")),
        ("Category", get("Category")),
        ("Price", get("Price")),
        ("Decision", decision),
        ("Safety verdict", get("Safety verdict")),
        ("Safety basis", get("Safety basis")),
        ("Verdict as of", get("Last checked")),
    ]
    dl = "".join("<dt>%s</dt><dd>%s</dd>\n" % (esc(k), esc(v)) for k, v in rows)
    links = []
    for label, field in (("Official site", "Official URL"), ("Source code", "GitHub repo")):
        url = safe_url(get(field))
        if url:
            links.append('<li><a href="%s" rel="noopener noreferrer">%s</a></li>' % (esc(url), esc(label)))
    links_html = "<ul class=\"links\">%s</ul>\n" % "".join(links) if links else ""
    if safe_install:
        install_html = "<pre><code>%s</code></pre>\n" % esc(safe_install)
    else:
        install_html = "<p class=\"empty\">Safe install: not written yet.</p>\n"
    notes = get("Install notes")
    notes_html = ""
    if notes:
        notes_html = (
            "<h2>Install notes</h2>\n<p class=\"warn\">Not fix-reviewed yet.</p>\n"
            "<pre><code>%s</code></pre>\n" % esc(notes)
        )
    body = (
        '<header><a href="../../">All tools</a></header>\n<main>\n'
        "<h1>%s</h1>\n<dl>\n%s</dl>\n%s"
        "<h2>Why this verdict</h2>\n<p>%s</p>\n"
        "<h2>Safe install</h2>\n%s%s"
        "</main>\n"
    ) % (esc(get("Name")), dl, links_html, esc(get("Safety reason")), install_html, notes_html)
    return page(get("Name") + " | AI tools wiki", body, "../../style.css")


def home_page(tools, sample_slug, sample_name):
    safe_written = sum(1 for t in tools if (t.get("Safe install") or "").strip())
    body = (
        "<main>\n<h1>AI tools wiki</h1>\n"
        "<p>%d tools, each with a safety verdict. Safe installs written: %d of %d.</p>\n"
        '<p>Sample tool page: <a href="t/%s/">%s</a></p>\n'
        "</main>\n"
    ) % (len(tools), safe_written, len(tools), esc(sample_slug), esc(sample_name))
    return page("AI tools wiki", body, "style.css")


STYLE = """:root { color-scheme: light dark; --fg: #1a1a1a; --bg: #fdfdfb; --muted: #5a5a5a; --line: #d8d8d2; --warn: #8a4b00; }
@media (prefers-color-scheme: dark) { :root { --fg: #ececea; --bg: #141413; --muted: #a8a8a2; --line: #3a3a36; --warn: #f0b060; } }
* { box-sizing: border-box; }
body { margin: 0; font: 16px/1.55 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; color: var(--fg); background: var(--bg); }
header, main { max-width: 46rem; margin: 0 auto; padding: 1rem; }
h1 { font-size: 1.75rem; line-height: 1.2; overflow-wrap: anywhere; }
h2 { font-size: 1.15rem; margin-top: 2rem; }
dl { display: grid; grid-template-columns: max-content 1fr; gap: .25rem 1rem; }
dt { color: var(--muted); }
dd { margin: 0; overflow-wrap: anywhere; }
pre { overflow-x: auto; padding: .75rem; border: 1px solid var(--line); border-radius: 6px; white-space: pre-wrap; overflow-wrap: anywhere; }
a { color: inherit; }
a:focus-visible { outline: 3px solid currentColor; outline-offset: 2px; }
.empty, .warn { color: var(--warn); }
@media (max-width: 26rem) { dl { grid-template-columns: 1fr; } dd { margin-bottom: .5rem; } }
"""


def build(data_path):
    raw = Path(data_path).read_bytes()
    data = json.loads(raw.decode("utf-8"))
    tools = gate(data)

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    used = set()
    ordered = sorted(tools, key=lambda t: (t.get("Name") or "").lower())
    sample = ordered[0] if ordered else {"Name": ""}
    sample_slug = slugify(sample.get("Name") or "tool", used)
    tool_dir = DIST / "t" / sample_slug
    tool_dir.mkdir(parents=True)
    (tool_dir / "index.html").write_text(tool_page(sample), encoding="utf-8")

    (DIST / "index.html").write_text(home_page(tools, sample_slug, sample.get("Name") or ""), encoding="utf-8")
    (DIST / "style.css").write_text(STYLE, encoding="utf-8")
    (DIST / "_headers").write_text(
        "/*\n"
        "  Content-Security-Policy: %s\n"
        "  X-Content-Type-Options: nosniff\n"
        "  Referrer-Policy: no-referrer\n" % CSP,
        encoding="utf-8",
    )
    build_info = {
        "data_blob_sha": git_blob_sha(raw),
        "build_commit": os.environ.get("CF_PAGES_COMMIT_SHA") or None,
        "build_time": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "tool_count": len(tools),
    }
    (DIST / "build.json").write_text(json.dumps(build_info, indent=2) + "\n", encoding="utf-8")
    return build_info


def main(argv):
    data_path = Path(argv[1]) if len(argv) > 1 else DEFAULT_DATA
    try:
        info = build(data_path)
    except GateError as err:
        print("BUILD GATE FAILED: %d problem(s)" % len(err.problems), file=sys.stderr)
        for problem in err.problems:
            print("  - " + problem, file=sys.stderr)
        return 1
    except (OSError, ValueError) as err:
        print("BUILD FAILED: %s" % err, file=sys.stderr)
        return 1
    print("Built %d tools into %s (data blob %s)" % (info["tool_count"], DIST, info["data_blob_sha"][:12]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
