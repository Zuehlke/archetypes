# Zuhlke Engineering Archetypes and Learning Pathways
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

## Project Overview
This project aims to help software engineers understand the skills and knowledge required at each stage of their career, from novice to expert. It serves as a roadmap for personal and professional development, enabling individuals to identify areas for growth and track their progress.
This is done by using 'archetypes' that define competencies 'topics' expected at different competency stages, as well as 'learning resources' that guide individuals in acquiring these skills.

### Project Structure
The project is structured into several key components:
-  `src/` - This folder contains definition files that outline the archetypes, topics, and learning resources in Markdown format.
    -  `src/archetypes/` - Contains archetype definitions, which describe the competencies and skills expected at various stages of a software engineer's career.
    -  `src/topics/` - Contains definitions of topics that are relevant to the archetypes, detailing the specific skills, knowledge areas and any learning resources associated with them.
    - `src/assets/` - Contains images and other assets used in the documentation.
- `docs/` - A static website generated from these definitions, providing an accessible and user-friendly interface for exploring the archetypes and learning pathways.

## Contributing
We welcome contributions to the Zühlke Archetypes and Learning Pathways project! Whether you're a seasoned developer or just starting out, your insight and experiences can help shape a more comprehensive and useful resource for everyone.

Please read through the [CONTRIBUTING.md](./CONTRIBUTING.md) file for guidelines on how to contribute effectively. This document covers everything from reporting issues to submitting pull requests, ensuring a smooth and collaborative process.

## Development Setup

This project uses [`just`](https://github.com/casey/just) as a command runner and [`uv`](https://docs.astral.sh/uv/) for Python environment and dependency management.

### Install `just`

```bash
# On macOS (using Homebrew)
brew install just
```

See the [just installation guide](https://github.com/casey/just?tab=readme-ov-file#installation) for more options.

### Install `uv`

```bash
# On macOS (using Homebrew)
brew install uv
```

See the [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/) for more options.

### Install `pre-commit` hooks

```bash
just install
```

The `pre-commit` hook will rebuild the static website before every commit.

## Maintainers

This project is maintained by:

* **Patrick Burls** ([@pburls](https://github.com/pburls))
* **Kevin Denver** ([@kdenver](https://github.com/kevin-denver))

Feel free to reach out to any maintainer if you have questions or need assistance.

## License
This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
