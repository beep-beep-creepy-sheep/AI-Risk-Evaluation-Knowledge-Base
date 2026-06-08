# Templates & Checklists

## Learning Objectives

After this chapter, you should be able to:

- Use checklists before and after AI-assisted drafting.
- Document prompt changes and output reviews.
- Create repeatable review habits for analyst workflows.
- Keep records without adding unnecessary bureaucracy.

## Safe-Use Preflight Checklist

- Is every example mock or public-style?
- Have private identifiers and confidential facts been removed?
- Does the prompt forbid investment recommendations?
- Does the prompt require uncertainty and assumptions?
- Is human review required before professional use?

## Prompt Design Checklist

- Does the prompt define the role of the output, such as draft, summary, or checklist?
- Does it define allowed sources?
- Does it define disallowed content?
- Does it tell the model what to do when information is missing?
- Does it request a structured output?
- Does it include a review or validation step?

## Output Review Checklist

- Facts are supported by provided context or cited public sources.
- Calculations and formulas have been independently checked.
- The answer avoids definitive advice.
- Limitations are visible.
- The tone is professional and proportionate.
- Prompt version and reviewer notes are recorded.

## Numeric Review Checklist

- Formula is visible.
- Inputs and units are listed.
- Time period is clear.
- Edge cases are considered.
- A simple example or validation row is included.
- Result is checked outside the model.

## Source Review Checklist

- Source names or excerpts are provided.
- Claims are tied to the provided source.
- Unsupported claims are labelled.
- Uncertainty is explicit.
- No private or confidential source material is included.

## Analyst Review Template

```text
Task:
Prompt version:
Input type: mock / public-style
Primary risk category:
Output summary:
Issues found:
Numeric checks completed:
Source checks completed:
Human reviewer:
Decision: accept / revise / reject
Follow-up action:
```

## Prompt Change Log Template

```text
Date:
Prompt name:
Old version:
New version:
Reason for change:
Eval cases added:
Known limitations:
```

## One-Page Workflow Template

```text
1. Define task:
2. Confirm allowed input:
3. Remove sensitive information:
4. Run prompt version:
5. Review output:
6. Check numbers:
7. Check sources:
8. Classify failures:
9. Add regression cases:
10. Update changelog:
```

## Beginner Study Prompt

Use this prompt to practise with the handbook:

```text
I am learning AI risk evaluation. Using only the mock scenario below, help me identify:
1. the safe-use boundary,
2. the likely risk categories,
3. one positive test,
4. one adversarial boundary test,
5. one human review checklist item.

Mock scenario:
{{scenario}}
```
