#!/usr/bin/env python3
"""
Ensures every topic has:
- A 'title:' in frontmatter
- A valid title (matches slug formatting)
- No missing or invalid titles
"""

from pathlib import Path
import yaml

TOPIC_ROOT = Path(__file__).parent.parent / "src" / "topics"


def slug_to_title(slug: str):
    """Convert 'clean-code-and-refactoring' → 'Clean Code And Refactoring'"""
    words = slug.replace("-", " ").split()
    fixed = []

    for w in words:
        if w.lower() in ["api", "css", "html", "http", "tls", "tcp", "dns", "ip"]:
            fixed.append(w.upper())
        elif w.lower() == "tdd":
            fixed.append("TDD")
        else:
            fixed.append(w.capitalize())

    return " ".join(fixed)


def load_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, None, text

    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, None, text

    fm = yaml.safe_load(parts[1]) or {}
    body = parts[2]
    return fm, body, parts[1]


def main():
    print(f"🔍 Validating titles in: {TOPIC_ROOT}")

    missing = []
    mismatched = []

    for md_file in TOPIC_ROOT.rglob("*.md"):
        fm, body, raw = load_frontmatter(md_file)

        if fm is None:
            continue

        slug = md_file.stem
        expected_title = slug_to_title(slug)

        actual_title = fm.get("title")

        # Missing title
        if not actual_title:
            missing.append((md_file, expected_title))
            continue

        # Title exists but does not match expected title
        if actual_title.strip() != expected_title.strip():
            mismatched.append(
                (md_file, actual_title, expected_title)
            )

    print("")

    if not missing and not mismatched:
        print("✅ All topics have valid titles!")
        return

    if missing:
        print("❌ Missing titles:")
        for f, suggestion in missing:
            print(f" - {f.name} → suggested: '{suggestion}'")

    if mismatched:
        print("\n⚠️ Title mismatch:")
        for f, actual, expected in mismatched:
            print(f" - {f.name}: '{actual}' → expected '{expected}'")

    print("\nRun Step 3b later to automatically fix all titles.")

if __name__ == "__main__":
    main()
