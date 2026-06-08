# Safe-Use Prompt Templates

## Context Boundary

```text
Use only the context provided below. If the context is insufficient, say what is missing.
Do not infer private, internal, client, or account-specific information.

Context:
{{context}}

Question:
{{question}}
```

## Human Review Reminder

```text
Draft an analyst note from the mock information below.
Include a final "Human review checklist" covering facts, sources, formulas, and assumptions.

Mock information:
{{mock_information}}
```

## Source Discipline

```text
Separate the answer into:
1. Claims supported by provided sources
2. Claims that need source checking
3. Assumptions
4. Uncertainty statement

Provided sources:
{{sources}}
```

