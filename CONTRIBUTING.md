# Contributing to archetypes

First off, thank you for considering contributing to archetypes!
It's people like you that make archetypes such a great resource.
We welcome contributions of all kinds, from fixing typos to adding new learning materials.

This document outlines how to contribute to the project.
Please read it carefully to ensure a smooth and effective contribution process.

## Table of Contents

* [Code of Conduct](#code-of-conduct)
* [How Can I Contribute?](#how-can-i-contribute)
    * [Understanding the Data Structure](#understanding-the-data-structure)
    * [Reporting Bugs or Suggesting Enhancements](#reporting-bugs-or-suggesting-enhancements)
    * [Contributing Content](#contributing-content)
        * [Adding Learning Materials to Topics](#adding-learning-materials-to-topics)
        * [Creating a New Topic](#creating-a-new-topic)
        * [Contributing to Archetypes](#contributing-to-archetypes)
    * [Working on Existing Issues](#working-on-existing-issues)
* [Making Changes & Creating Pull Requests](#making-changes--creating-pull-requests)
    * [Forking the Repository](#forking-the-repository)
    * [Creating a Branch](#creating-a-branch)
    * [Validating Your Changes](#validating-your-changes)
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

### Understanding the Data Structure

Topics and archetypes use **YAML frontmatter** for structured data (learning resources, skill progressions, metadata). The frontmatter sits at the top of each markdown file and is validated against JSON schemas during build.

**Key concepts:**
* **Frontmatter**: YAML block at file top containing structured data
* **Schemas**: Define valid structure (see `schemas/` directory)
* **Validation**: Build fails if frontmatter doesn't match schema

For full details, see [Data Architecture](docs/data-architecture.md) and [ADR-0001](docs/ADRs/ADR-0001.md).

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

### Contributing Content
We are excited to receive contributions of learning materials, new topics, and archetypes from the community!
There are three main ways you can contribute content:

1. **Learning Materials** - Add resources to existing topics (books, tutorials, courses, etc.)
2. **Topics** - Create new learning areas (e.g., "Version Control Systems", "Test Driven Development")
3. **Archetypes** - Define or update career pathways that organize topics into skill progression stages

**Before starting:**
1. **Search existing content:** Browse `src/topics/` and `src/archetypes/` for similar concepts
2. **Check for overlap:** 
   - Would your contribution substantially duplicate existing content?
   - Could you enhance existing content instead of creating new content?
   - Does your proposed content have a distinct, well-defined scope?
3. **Check the issue tracker:** Someone might already be working on similar content
4. **Open an issue (RECOMMENDED for new topics/archetypes):** Propose your idea to:
   - Discuss scope and boundaries
   - Identify potential overlaps with existing content
   - Get feedback on appropriate granularity

#### Adding Learning Materials to Topics

The most common contribution is adding learning resources to existing topics. Simply edit the topic's frontmatter:

```yaml
---
title: Version Control Systems
learning_resources:
  - type: "external_link"
    title: "Learn Git Branching"
    url: "https://learngitbranching.js.org/"
    description: "Interactive tutorial for learning Git"
  
  # Add your new resource here
  - type: "book"
    title: "Pro Git"
    author: "Scott Chacon"
    url: "https://git-scm.com/book"
    publisher: "Apress"
    year: 2014
    description: "Comprehensive guide to Git"
---
```

**Resource types:** `external_link`, `book`, `course`, `video`, `pdf`, `talk`, `presentation`

**Required fields:** `type`, `title`, `url`

**Optional fields:** `description`, `author`, `publisher`, `year`, `is_internal`, `embed_code`

#### Creating a New Topic

**Topic Scope Guidelines:**
* **Single responsibility:** Each topic should cover one cohesive concept
* **Appropriate granularity:** Not too broad (e.g., "Software Engineering") nor too narrow (e.g., "Git Merge Conflicts")
* **Clear boundaries:** Topic scope should be well-defined and distinct from related topics
* **Use cross-references:** Link related topics rather than duplicating content

**Examples:**
* ✅ Good: "Version Control Systems" (clear scope, covers Git, SVN concepts)
* ✅ Good: "Test Driven Development" (specific practice)
* ❌ Too broad: "Software Development" (covers everything)
* ❌ Too narrow: "How to Write a For Loop in Python" (too specific)
* ❌ Overlapping: Creating both "Git Basics" and "Version Control Systems" when they cover similar ground

**Filename requirements:**
* Use kebab-case: `your-topic-name.md` (lowercase, hyphens only)
* Filename becomes the URL slug
* Pattern: `^[a-z0-9]+(-[a-z0-9]+)*$` (no underscores, special chars, or uppercase)

**Minimal frontmatter template:**
```yaml
---
title: Your Topic Title
---

# Your Topic Title

Your topic content here...
```

**With learning resources:**
```yaml
---
title: Version Control Systems
learning_resources:
  - type: "external_link"
    title: "Learn Git Branching"
    url: "https://learngitbranching.js.org/"
    description: "Interactive tutorial for learning Git"
  
  - type: "book"
    title: "Pro Git"
    author: "Scott Chacon"
    url: "https://git-scm.com/book"
    publisher: "Apress"
    year: 2014
  
  - type: "course"
    title: "Internal Git Workshop"
    url: "https://internal.zuhlke.com/git"
    is_internal: true
    description: "Advanced workshop (Zühlke only)"

cross_references:
  - pair-programming
  - continuous-integration
---

# Version Control Systems

Your content here...

{{ render_learning_resources() }}
```

**Resource types:** `external_link`, `book`, `course`, `video`, `pdf`, `talk`, `presentation`

**Required fields:** `type`, `title`, `url`

Place new topics in `src/topics/your-topic-name.md`.

#### Contributing to Archetypes

Archetypes define career pathways by organizing topics into skill progression stages based on the Dreyfus model.

**To add a topic to an existing archetype**, edit the archetype's frontmatter:

```yaml
---
title: Core Software Engineer
description: Foundation of technical excellence at Zühlke
skill_stages:
  - name: "Novice"
    topics:
      - version-control-systems
      - developer-tooling-basics
      # Add your topic slug here
  
  - name: "Advanced Beginner"
    topics:
      - test-driven-development
      - pair-programming
---
```

**Skill stages:** `Novice`, `Advanced Beginner`, `Competent`, `Proficient`, `Expert`

**Note:** Topics must exist in `src/topics/` before being referenced in archetypes.

Find archetypes in `src/archetypes/`.

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

### Validating Your Changes
Before committing your changes, ensure they are valid and do not break the build:
```bash
just fmt
just build
```

**What gets validated:**
* **Frontmatter schema** - YAML structure must match schemas in `schemas/` directory
* **Broken links** - MkDocs strict mode catches missing pages and broken cross-references
* **Markdown linting** - Ensures consistent formatting

**Common validation errors:**

*Schema validation:*
```
ValidationError: 'title' is a required property
File: src/topics/my-new-topic.md
```
Fix: Add missing required field to frontmatter

*Link validation:*
```
WARNING - Doc file contains a link to 'topics/non-existent.md', but target not found
```
Fix: Create the referenced topic or remove the broken reference

This will format your code and rebuild the static website to ensure everything is up-to-date.

You can also run the local development server to visually inspect your changes:
```bash
just serve
```

### Committing Your Changes

Make your changes to the codebase or add your new content files.
Stage your changes: `git add .` (to add all changes) or `git add path/to/your/file.md` (to add specific files).
Commit your changes: `git commit -m "Your descriptive commit message"`.

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

* **File Format:** Content should be submitted in Markdown (`.md`) format with YAML frontmatter.
* **Frontmatter Requirements:**
    * Topics require at minimum a `title` field
    * Archetypes require `title`, `description`, and `skill_stages`
    * See examples in [Creating a New Topic](#creating-a-new-topic) and [Contributing to Archetypes](#contributing-to-archetypes)
    * Frontmatter is validated against JSON schemas in `schemas/` directory
* **File Naming:** Use kebab-case file names (e.g., `test-driven-development.md`).
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