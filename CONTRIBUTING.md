# Contributing to archetypes

First off, thank you for considering contributing to archetypes!
It's people like you that make archetypes such a great resource.
We welcome contributions of all kinds, from fixing typos to adding new learning materials.

This document outlines how to contribute to the project.
Please read it carefully to ensure a smooth and effective contribution process.

## Table of Contents

* [Code of Conduct](#code-of-conduct)
* [How Can I Contribute?](#how-can-i-contribute)
    * [Reporting Bugs or Suggesting Enhancements](#reporting-bugs-or-suggesting-enhancements)
    * [Contributing Content (Learning Materials)](#contributing-content-learning-materials)
    * [Working on Existing Issues](#working-on-existing-issues)
* [Setting Up Your Development Environment](#setting-up-your-development-environment) (Optional - if applicable)
* [Making Changes & Creating Pull Requests](#making-changes--creating-pull-requests)
    * [Forking the Repository](#forking-the-repository)
    * [Creating a Branch](#creating-a-branch)
    * [Committing Your Changes](#committing-your-changes)
    * [Writing Good Commit Messages](#writing-good-commit-messages)
    * [Submitting a Pull Request](#submitting-a-pull-request)
* [Content Guidelines for Learning Materials](#content-guidelines-for-learning-materials)
    * [Topic Relevance](#topic-relevance)
    * [Content Quality](#content-quality)
    * [Formatting](#formatting)
    * [Originality and Citations](#originality-and-citations)
    * [Accessibility](#accessibility)
* [Getting Help](#getting-help)

## Code of Conduct

This project and everyone participating in it is governed by the archetypes Code of Conduct.
By participating, you are expected to uphold this code.
Please report unacceptable behaviour to the SWEX leadership team.

## How Can I Contribute?

### Reporting Bugs or Suggesting Enhancements

If you find a bug in the website or have an idea for an enhancement (including new content areas), please check the [issue tracker](https://github.com/Zuehlke/archetypes/issues) to see if it has already been reported.
If not, please open a new issue.

When reporting a bug, please include:
* A clear and descriptive title.
* What you expected to happen.
* What actually happened.
* Your browser and operating system (if relevant).

When suggesting an enhancement:
* Explain the problem you're trying to solve.
* Describe your proposed solution.
* Explain the benefits this enhancement would bring to users.

### Contributing Content (Learning Materials)

We are excited to receive contributions in the form of learning materials for various skills. This could include:
* Tutorials or how-to guides
* Explanations of concepts
* Collections of useful resources
* Exercises or quizzes
* Case studies

Before starting to write new content, it's a good idea to:
1.  **Check existing content:** Ensure your proposed topic isn't already well-covered.
2.  **Check the issue tracker:** Someone might have already suggested or started working on a similar topic.
3.  **Open an issue (optional but recommended):** Propose your content idea by opening an issue. 
This allows for discussion with maintainers and other contributors, preventing duplicated effort and ensuring your idea aligns with the project's goals. 
Tag it as `content proposal` or similar.

### Working on Existing Issues

You can also contribute by working on existing issues in the issue tracker.
Look for issues tagged with `help wanted` or `good first issue` if you're new.
If you decide to work on an issue, please comment on it to let others know you're taking it on.

## Making Changes & Creating Pull Requests

### Forking the Repository

Click the "Fork" button at the top right of the [main project repository page](https://github.com/Zuehlke/archetypes).
This creates a copy of the repository in your own GitHub account.

### Creating a Branch

Create a descriptive branch name for your changes:
`git checkout -b content/topic-of-learning-material`

Example: `git checkout -b content/introduction-to-python`

### Committing Your Changes

Make your changes to the codebase or add your new content files.
Stage your changes: `git add .` (to add all changes) or `git add path/to/your/file.md` (to add specific files).
Commit your changes: `git commit -m "Your descriptive commit message"`

### Writing Good Commit Messages

* Use the present tense ("Add feature" not "Added feature").
* Use the imperative mood ("Fix bug" not "Fixes bug").
* Limit the first line to 72 characters or less.
* Reference issues and pull requests liberally after the first line.
* Consider using [Conventional Commits](https://www.conventionalcommits.org/) for more structured messages, e.g.:
    * `feat: Add dark mode toggle`
    * `fix: Correct spelling errors in an_article.md`
    * `docs: Update contribution guidelines`
    * `content: Add new tutorial on JavaScript arrays`

### Submitting a Pull Request (PR)

1.  Push your branch to your fork: `git push origin your-branch-name`
2.  Go to the [main project repository](https://github.com/Zuhlke-Internal/archetypes) on GitHub.
3.  You should see a prompt to create a Pull Request from your recently pushed branch. Click it.
4.  Give your PR a clear title and description. Explain the "what" and "why" of your changes. Reference any relevant issues (e.g., "Closes #123").
5.  Ensure your PR targets the `main` (or `master`) branch of the upstream repository.
6.  Submit the PR. Project maintainers will review your changes and may request modifications or provide feedback.

## Content Guidelines for Learning Materials

To ensure consistency and quality, please adhere to the following guidelines when contributing learning materials:

### Topic Relevance

* Content should align with the skills and topics covered by this project.
* If unsure, propose your topic by opening an issue first.

### Content Quality

* **Accuracy:** Ensure all information is factually correct and up-to-date.
* **Clarity:** Write in clear, concise language. Avoid jargon where possible, or explain it if necessary.
* **Completeness:** Cover the topic adequately for the intended audience.
* **Engagement:** Aim to make the material engaging and easy to understand. Use examples, analogies, or visuals where helpful.
* **Structure:** Organize content logically with clear headings and subheadings. Use lists and bullet points for readability.

### Formatting

* **File Format:** Content should typically be submitted in Markdown (`.md`) format.
* **File Naming:** Use lowercase, hyphenated file names (e.g., `my-new-skill-tutorial.md`).
* **Directory Structure:** Place new content files in the appropriate directory (e.g., `src/topics/your-topic.md`). Check existing structure or ask if unsure.
* **Images/Assets:** If your content includes images or other assets:
    * Place them in a relevant assets folder (e.g., `assets/your-topic/your-image.png`).
    * Optimize images for the web (e.g., appropriate size, compression).
    * Ensure you have the rights to use any images. Provide alt text for accessibility.

### Originality and Citations

* All contributed content must be your original work or properly attributed.
* Do not plagiarize. If you use external resources, cite them appropriately.
* If you are referencing code snippets, ensure the license of the original code is compatible with this project and provide attribution.

### Accessibility

* Write with accessibility in mind.
* Use clear and simple language.

## Getting Help

If you have questions or need help with any aspect of contributing, please:
* Open an issue on the [issue tracker](https://github.com/Zuehlke/archetypes/issues) and tag it with `question`.

We're happy to help you get started!

Thank you for contributing!