# GitHub Copilot Instructions

## Project Context
This project defines engineering archetypes and learning pathways for software engineers, outlining competencies and learning resources for career development. The repository is structured to support contributions to these archetypes and topics, which are rendered into a static website using MkDocs.

### Key Components
- **Archetypes (`src/archetypes/`)**: Define the skills and competencies expected at various stages of a software engineer's career.
- **Topics (`src/topics/`)**: Detail specific skills, knowledge areas, and associated learning resources.
- **Assets (`src/assets/`)**: Contain images and other resources used in the documentation.
- **Static Site (`_site/`)**: Generated using MkDocs. Do not edit or commit changes directly to this folder.

## Developer Workflows

### Setting Up the Environment
1. Install `just` (command runner):
   ```bash
   brew install just
   ```
2. Install `uv` (Python environment manager):
   ```bash
   brew install uv
   ```
3. Install pre-commit hooks:
   ```bash
   just install
   ```
   This ensures the static site is rebuilt before every commit.

### Building the Static Site
- Use the `just` command to build the site:
  ```bash
  just build
  ```

### Testing Changes
- Validate your changes locally by running the MkDocs development server:
  ```bash
  just serve
  ```
  Access the site at `http://127.0.0.1:8000/`.

## Contribution Guidelines
- Follow the branch naming convention: `content/<topic-of-learning-material>`.
- Use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages.
- Refer to `CONTRIBUTING.md` for detailed contribution workflows.

## Project-Specific Conventions
- **Markdown Formatting**: Use consistent Markdown syntax for archetypes and topics. Refer to existing files in `src/archetypes/` and `src/topics/` for examples.
- **Learning Resources**: Ensure all topics include actionable learning resources.
- **Static Site Updates**: Do not manually edit `_site/`. Always use the `just build` command to regenerate it.

## External Dependencies
- **MkDocs**: Used for generating the static site. Ensure `mkdocs.yml` is updated for any structural changes.
- **Pre-commit Hooks**: Automatically rebuild the site and enforce formatting standards.

## Examples
- Refer to `src/archetypes/core-software-engineer-archetype.md` for an example of an archetype definition.
- Refer to `src/topics/test-driven-development.md` for an example of a topic definition.

## Maintainers
For questions or assistance, contact:
- **Patrick Burls** ([@pburls](https://github.com/pburls))
- **Kevin Denver** ([@kdenver](https://github.com/kevin-denver))