# Evaluation Design

An evaluation is a structured way to ask: "Does this prompt or workflow behave safely and usefully across expected and difficult cases?"

## Define the Use Case

Write down the user, task, allowed inputs, disallowed inputs, desired output, and review expectation.

Example:

```text
Use case: Summarise a public-style research excerpt for an analyst note.
Allowed input: Provided public or mock text.
Disallowed input: Private account details, confidential documents, unpublished research.
Expected output: Summary, evidence, limitations, uncertainty.
```

## Define Expected Behavior

Expected behavior should be specific enough to test. Include what the model should do, what it should refuse, and what it should ask for when context is missing.

## Create Positive Tests

Positive tests confirm useful behavior on ordinary requests: summarising a public excerpt, explaining a mock metric, or creating a spreadsheet formula with caveats.

## Create Adversarial Tests

Adversarial tests check safety boundaries. Examples include requests for hidden instructions, confidential content handling, unsupported recommendations, fake citations, and overconfident numeric claims.

## Create Regression Tests

Every important failure should become a regression test. Keep the test small, label the risk category, and record the prompt version that failed.

## Score Outputs

Start with simple deterministic rubrics: required behaviors, positive indicators, and negative indicators. For higher-risk use, combine automated checks with human review.

## Track Prompt Versions

Use version IDs such as `metric-explainer-v0.3`. Record changed instructions, eval results, known limitations, and reviewer notes.

