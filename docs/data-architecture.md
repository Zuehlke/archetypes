# Data Architecture

This document describes the data model for the Zühlke Archetypes project, which supports career pathway definitions and learning resources.

## Overview

The data architecture defines the structure and relationships between archetypes, skill stages, topics, and learning resources. For context on the decision to move to structured data, see [ADR-0001](./ADRs/ADR-0001.md).

## Entity Model

```mermaid
erDiagram
    ARCHETYPE {
        string title
        string description
        array skill_stages
    }
    
    SKILL_STAGE {
        string name "Novice|Advanced_Beginner|Competent|Proficient|Expert"
        array topic_references "array of topic slugs"
    }
    
    TOPIC {
        string title
        string description
        array learning_resources
        array cross_references "array of topic slugs"
    }
    
    LEARNING_RESOURCE {
        string type "external_link|book|course|video|pdf|talk|presentation"
        string title
        string url
        boolean is_internal
        string description
        string embed_code "for videos/pdfs"
    }
    
    ARCHETYPE ||--o{ SKILL_STAGE : "contains"
    SKILL_STAGE ||--o{ TOPIC : "references"
    TOPIC ||--o{ LEARNING_RESOURCE : "provides"
    TOPIC }o--o{ TOPIC : "cross_references"
```

## Core Entities

### Archetype
Represents a career pathway or role specialization (e.g., "Core Software Engineer").

- **title**: Display name of the archetype
- **description**: Overview explaining the archetype's purpose and scope
- **skill_stages**: Array of Dreyfus model stages containing topics

### Skill Stage
Represents one of the five Dreyfus model stages of skill acquisition:
- Novice
- Advanced Beginner
- Competent
- Proficient
- Expert

Each stage contains references to topics that should be mastered at that level.

### Topic
Detailed learning content for a specific skill or concept (e.g., "Version Control Systems", "Test Driven Development").

- **title**: Display name of the topic
- **description**: Detailed explanation of the concept
- **learning_resources**: Array of learning materials
- **cross_references**: Links to related topics

### Learning Resource
Individual learning materials embedded directly within topics (not normalized as separate entities):

- **external_link**: Web resources and documentation
- **book**: Published books with bibliographic information
- **course**: Internal training courses (marked as internal)
- **video**: YouTube videos and talks (with embed code)
- **pdf**: Presentations and documents (with embed code)

**Important**: Learning resources are stored as arrays within topic files, not as separate referenced entities. This design choice prioritizes simplicity and contextual information over normalization.

## Relationships

1. **Archetype → Skill Stages**: Each archetype defines progression through Dreyfus stages
2. **Skill Stage → Topics**: Each stage references specific topics to master
3. **Topic → Learning Resources**: Topics contain embedded learning materials (not referenced)
4. **Topic → Topic**: Cross-references between related concepts

**Note on Learning Resources**: Unlike other relationships, learning resources are embedded directly within topic files rather than being separate entities. This avoids normalization in favor of simplicity and contextual information.

## Implementation Notes

### Topic References
- Each skill stage contains an array of topic references using **URL slugs**
- Example: `"version-control-systems"` references `/topics/version-control-systems.md`
- Slugs are derived from topic titles: lowercase, spaces → hyphens, special chars removed
- Topic references map directly to file paths and URL structure
- Missing topic pages will result in 404 errors until content is created

### Identifier System
All entities use slug-based identifiers for cross-referencing:
- **Topics**: Use filename slug (e.g., `version-control-systems`)
- **Archetypes**: Use filename slug (e.g., `core-software-engineer`)
- **Learning Resources**: Can optionally have slugs for cross-referencing between topics

### Learning Resource Identification
Learning resources are **embedded directly within topics** rather than being separate referenced entities:

```yaml
# version-control-systems.yaml
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
```

**Rationale:**
- Learning resources are specific to each topic
- No need for separate files or cross-referencing
- Simpler data structure and maintenance
- Resources are contextual to their topic

**Optional Slugs:**
Learning resources can optionally include slugs for advanced use cases (e.g., tracking completion, analytics):
```yaml
learning_resources:
  - slug: "learn-git-branching"  # optional
    type: "external_link"
    title: "Learn Git Branching"
```

### Learning Resource Types
Learning resources are classified by type to enable appropriate rendering:
- **external_link**: Simple web links
- **book**: Include bibliographic information (author, publisher, year)
- **course**: Internal training materials (marked with access restrictions)
- **video**: YouTube videos and talks (include embed codes)
- **pdf**: Presentations and documents (include embed codes)

### Cross-References
Topics can reference related topics using the same slug-based system to create learning pathways and show conceptual relationships.

Example:
```yaml
# extreme-programming-practices.yaml
cross_references:
  - "test-driven-development"
  - "pair-programming"
  - "version-control-systems"
```