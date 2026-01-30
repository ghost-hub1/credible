import re
from pathlib import Path

ROOT = Path(".").resolve()

EXTENSIONS = {".html", ".htm", ".js", ".json"}

# Reverse HTML attributes: href="./x" → href="/x"
HTML_ATTR_REVERSE = re.compile(
    r'''(?P<attr>\b(?:href|src|action)=["'])\./(?P<path>[^"'>]+)''',
    re.IGNORECASE
)

# Reverse JSON URLs: "url":"./x" → "url":"/x"
JSON_URL_REVERSE = re.compile(
    r'''"url"\s*:\s*"\./([^"]+)"'''
)

def reverse_file(path: Path):
    original = path.read_text(encoding="utf-8", errors="ignore")
    modified = original

    modified = HTML_ATTR_REVERSE.sub(
        lambda m: f'{m.group("attr")}/{m.group("path")}',
        modified
    )

    modified = JSON_URL_REVERSE.sub(
        lambda m: f'"url":"/{m.group(1)}"',
        modified
    )

    if modified != original:
        path.write_text(modified, encoding="utf-8")
        print(f"[REVERSED] {path}")

def main():
    for file in ROOT.rglob("*"):
        if file.suffix.lower() in EXTENSIONS:
            reverse_file(file)

if __name__ == "__main__":
    main()
