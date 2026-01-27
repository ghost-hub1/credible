import re
from pathlib import Path

ROOT = Path(".").resolve()

# File types to process
EXTENSIONS = {".html", ".htm", ".js", ".json"}

# Match href="/...", src="/...", action="/..."
HTML_ATTR_RE = re.compile(
    r'''(?P<attr>\b(?:href|src|action)=["'])/(?P<path>[^"'>]+)''',
    re.IGNORECASE
)

# Match JSON "url":"/something" BUT NOT regex rules
JSON_URL_RE = re.compile(
    r'''"url"\s*:\s*"/(?!\.\*|\(|\\)([^"]+)"'''
)

def rewrite_file(path: Path):
    original = path.read_text(encoding="utf-8", errors="ignore")
    modified = original

    # HTML attribute rewrite
    modified = HTML_ATTR_RE.sub(
        lambda m: f'{m.group("attr")}./{m.group("path")}',
        modified
    )

    # JSON "url" rewrite (safe)
    modified = JSON_URL_RE.sub(
        lambda m: f'"url":"./{m.group(1)}"',
        modified
    )

    if modified != original:
        path.write_text(modified, encoding="utf-8")
        print(f"[FIXED] {path}")

def main():
    for file in ROOT.rglob("*"):
        if file.suffix.lower() in EXTENSIONS:
            rewrite_file(file)

if __name__ == "__main__":
    main()
