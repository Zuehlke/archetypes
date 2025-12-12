# Zuhlke Engineering Archetypes and Learning Pathways
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

> ⚠️ **Note:** This project has been **archived** and migrated to Zühlke's internal GitLab instance. Please visit the new repository at: [https://codehub.zuehlke.com/learning-journey/archetypes](https://codehub.zuehlke.com/learning-journey/archetypes)
>
> The Zühlke Archetypes website is still available to be viewed publicly at: [https://learning-journey.pages.codehub.zuehlke.com/archetypes/](https://learning-journey.pages.codehub.zuehlke.com/archetypes/)

## Project Overview
This project aims to help software engineers understand the skills and knowledge required at each stage of their career, from novice to expert. It serves as a roadmap for personal and professional development, enabling individuals to identify areas for growth and track their progress.
This is done by using 'archetypes' that define competencies 'topics' expected at different competency stages, as well as 'learning resources' that guide individuals in acquiring these skills.

### Project Structure
The project is structured into several key components:
-  `src/` - This folder contains definition files that outline the archetypes, topics, and learning resources in Markdown format.
    -  `src/archetypes/` - Contains archetype definitions, which describe the competencies and skills expected at various stages of a software engineer's career.
    -  `src/topics/` - Contains definitions of topics that are relevant to the archetypes, detailing the specific skills, knowledge areas and any learning resources associated with them.
    - `src/assets/` - Contains images and other assets used in the documentation.
- `_site/` - A static website generated from these definitions using [MkDocs](https://www.mkdocs.org/), providing an accessible and user-friendly interface for exploring the archetypes and learning pathways. *Not to be edited directly or committed to the repository*.

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
* **Fabio Scagliola** ([@fabioscagliola](https://github.com/fabioscagliola))

Feel free to reach out to any maintainer if you have questions or need assistance. You can also contact us via the [Archetypes > General](https://teams.microsoft.com/l/channel/19%3AKP35frVs7vgqGUh8X0iYTMPPWEzy5tqQ41Y6bcF_3oM1%40thread.tacv2/General?groupId=22083902-eb02-4c49-aeb5-04bdf19ddfd4&tenantId=ccce7f5e-a35f-4bc3-8e63-b2215e7d14f9) Teams channel using the @maintainers tag.

## Contributors

We'd like to thank the following individuals for their significant contributions:

* **Kevin Denver** ([@kevin-denver](https://github.com/kevin-denver)) - Set up the initial project and scaffolded the Core Software Engineer archetype
* **Milan Starcevic** ([@MilanStarcevicZuehlke](https://github.com/MilanStarcevicZuehlke)) - Created the FSI Software Engineer archetype and contributed extensive FSI-related topics (banking, insurance, financial crimes, regulations)
* **Milos Bjelcevic** ([@milosbjelceviczuhlke](https://github.com/milosbjelceviczuhlke)) - Contributed to the project structure and design
* **Fabio Scagliola** ([@fabioscagliola](https://github.com/fabioscagliola)) - Contributed to the project structure and design
* **Patrick Burls** ([@pburls](https://github.com/pburls)) - Contributed to the project structure and design

For a complete list of all contributors, see our [GitHub contributors page](https://github.com/Zuehlke/archetypes/graphs/contributors).

## License
This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
