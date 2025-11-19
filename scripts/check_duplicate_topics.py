#!/usr/bin/env python3
"""
Duplicate topic detector.

Checks:
- Duplicate slugs
- Duplicate titles
- Similar titles (fuzzy match)
"""

from pathlib import Path
import yaml
import difflib
import re

TOPIC_ROOT = Path(__file__).parent.parent / "src" / "topics"


def extract_frontmatter_and_content(text: str):
    if not text.startswith("---"):
        return None, text

    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text

    frontmatter = yaml.safe_load(parts[1]) or {}
    content = parts[2]
    return frontmatter, content


def extract_h1_title(content: str):
    """Extract '# Title'."""
    m = re.search(r"^#\s+(.+)$", content, flags=re.MULTILINE)
    return m.group(1).strip() if m else None


def load_all_topics():
    topics = []

    for md_file in TOPIC_ROOT.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8")
        frontmatter, content = extract_frontmatter_and_content(text)

        slug = md_file.stem
        title = None

        # Prefer frontmatter title
        if frontmatter and "title" in frontmatter:
            title = frontmatter["title"]
        else:
            # Fallback H1
            title = extract_h1_title(content)

        # Final fallback — derived from slug
        if not title:
            title = slug.replace("-", " ").title()

        topics.append({
            "_slug": slug,
            "_file": md_file.name,
            "title": title
        })

    return topics


def normalize_title(t: str):
    """Convert title to comparable simplified form."""
    if not t:
        return ""

    t = t.lower().strip()
    t = t.replace("(", "").replace(")", "")
    t = t.replace("xp", "").replace("tdd", "")
    t = t.replace("-", " ")
    return " ".join(t.split())


def main():
    print(f"🔍 Checking for duplicate topics in: {TOPIC_ROOT}")

    topics = load_all_topics()
    seen_slugs = {}
    seen_titles = {}
    errors = []

    for t in topics:
        slug = t["_slug"]
        title = t["title"]
        norm_title = normalize_title(title)
        filename = t["_file"]

        # Duplicate slug
        if slug in seen_slugs:
            errors.append(
                f"❌ Duplicate slug '{slug}': {filename} and {seen_slugs[slug]}"
            )
        else:
            seen_slugs[slug] = filename

        # Duplicate title
        if norm_title in seen_titles:
            errors.append(
                f"❌ Duplicate title '{title}': {filename} and {seen_titles[norm_title]}"
            )
        else:
            seen_titles[norm_title] = filename

    # Fuzzy matching
    titles = list(seen_titles.keys())
    for i in range(len(titles)):
        for j in range(i + 1, len(titles)):
            a, b = titles[i], titles[j]
            ratio = difflib.SequenceMatcher(None, a, b).ratio()
            if ratio > 0.80:
                errors.append(
                    f"⚠️ Possible similar topics:\n"
                    f"   - '{a}'\n"
                    f"   - '{b}'\n"
                    f"     similarity={ratio:.2f}"
                )

    print("")

    if errors:
        print("\n".join(errors))
        print(f"\n❌ Found {len(errors)} potential duplicate issues.")
    else:
        print("✅ No duplicates detected!")


if __name__ == "__main__":
    main()
