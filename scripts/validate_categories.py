import yaml
from pathlib import Path
import re

TOPIC_ROOT = Path("src/topics")

# Allowed category folders
ALLOWED_CATEGORIES = {
    "agile",
    "architecture",
    "backend",
    "cloud",
    "data",
    "databases",
    "devops",
    "fundamentals",
    "networking",
    "programming",
    "security",
    "systems",
    "testing",
    "tooling",
}

FRONTMATTER_REGEX = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def load_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None

    match = FRONTMATTER_REGEX.search(text)
    if not match:
        return None

    return yaml.safe_load(match.group(1)) or {}


def main():
    errors = []
    print(f"🔍 Validating categories from folder structure in: {TOPIC_ROOT}")

    existing_files = list(TOPIC_ROOT.rglob("*.md"))

    for file_path in existing_files:
        relative = file_path.relative_to(TOPIC_ROOT)
        parts = relative.parts

        # Check file is inside a category folder
        if len(parts) == 1:
            errors.append(f"❌ File is directly under src/topics/ but must be inside a category: {file_path}")
            continue

        category = parts[0]
        slug = file_path.stem

        # Validate category folder
        if category not in ALLOWED_CATEGORIES:
            errors.append(f"❌ Unknown category folder '{category}' for file {file_path}")
            continue

        # Validate frontmatter category matches folder
        fm = load_frontmatter(file_path)
        if not fm:
            errors.append(f"❌ Missing or invalid frontmatter in {file_path}")
            continue

        fm_category = fm.get("category")
        if fm_category != category:
            errors.append(
                f"❌ Frontmatter category mismatch in {slug}.md "
                f"(frontmatter: '{fm_category}', expected: '{category}')"
            )

    print("\n===== VALIDATION REPORT =====\n")

    if errors:
        for e in errors:
            print(e)
        print(f"\n❌ Validation failed with {len(errors)} errors.\n")
    else:
        print("✅ All category folders and frontmatter values are valid!")

    print("=============================")


if __name__ == "__main__":
    main()
