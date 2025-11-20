#!/usr/bin/env python3
"""
Add minimal frontmatter to all topic files that don't have it.

Frontmatter added:

---
title: <existing H1 or derived from filename>
learning_resources: []
cross_references: []
---
"""

from pathlib import Path
import re
import yaml

TOPIC_ROOT = Path(__file__).parent.parent / "src" / "topics"

def derive_title_from_filename(filename: str) -> str:
    """Convert 'clean-code-and-refactoring.md' -> 'Clean Code And Refactoring'"""
    name = filename.replace(".md", "")
    words = name.split("-")
    # Capitalise nicely, keep acronyms as-is
    fixed = []
    for w in words:
        if w.upper() in ["API", "CSS", "HTML", "HTTP", "TCP", "IP", "DNS", "TLS"]:
            fixed.append(w.upper())
        else:
            fixed.append(w.capitalize())
    return " ".join(fixed)

def extract_h1_title(content: str) -> str | None:
    """Find '# Title' as the first H1 """
    match = re.search(r"^#\s+(.+)$", content, flags=re.MULTILINE)
    return match.group(1).strip() if match else None

def add_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")

    # If already has frontmatter, skip
    if text.startswith("---"):
        print(f"Skipping (already has frontmatter): {path.name}")
        return

    # Determine title
    h1_title = extract_h1_title(text)
    title = h1_title or derive_title_from_filename(path.name)

    frontmatter = {
        "title": title,
        "learning_resources": [],
        "cross_references": []
    }

    fm_block = "---\n" + yaml.safe_dump(frontmatter, sort_keys=False) + "---\n\n"

    new_text = fm_block + text
    path.write_text(new_text, encoding="utf-8")

    print(f"Added frontmatter -> {path.name}")

def main():
    for md in TOPIC_ROOT.rglob("*.md"):
        add_frontmatter(md)

if __name__ == "__main__":
    main()
