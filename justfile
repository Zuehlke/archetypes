build:
    uv run mkdocs build --clean --strict

serve:
    uv run mkdocs serve

install:
    uv run pre-commit install

fmt:
    uv run pymarkdown scan ./src

validate:
    @echo "🔍 Running full validation…"
    uv run python3 scripts/check_duplicates.py
    uv run python3 scripts/validate_titles.py
    uv run python3 scripts/validate_categories.py
    just build
    @echo "✅ Validation completed!"
