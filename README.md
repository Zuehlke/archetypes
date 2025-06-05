# Zuhlke Engineering Archetypes and Learning Pathways
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

## Contributing to the Zühlke Archetypes Project
We welcome contributions to the Zühlke Archetypes and Learning Pathways project! Whether you're a seasoned developer or just starting out, your insight and experiences can help shape a more comprehensive and useful resource for everyone.

Please read through the [CONTRIBUTING.md](./CONTRIBUTING.md) file for guidelines on how to contribute effectively. This document covers everything from reporting issues to submitting pull requests, ensuring a smooth and collaborative process.

## Project Setup

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
