# Evaluation Design

An evaluation is a structured way to ask: "Does this prompt or workflow behave safely and usefully across expected and difficult cases?"

## Learning Objectives

After this chapter, you should be able to:

- Define a use case clearly enough to test it.
- Write positive, adversarial, and regression test cases.
- Create simple rubrics with required behaviors and failure indicators.
- Interpret failures without overfitting the prompt to one example.

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

Weak expected behavior:

```text
The model should be safe.
```

Stronger expected behavior:

```text
The model should summarise only the provided mock excerpt, avoid unsupported facts, state missing context, and label the output as a draft.
```

## Create Positive Tests

Positive tests confirm useful behavior on ordinary requests: summarising a public excerpt, explaining a mock metric, or creating a spreadsheet formula with caveats.

Positive tests are important because a model that refuses everything is safe but not useful. A good system helps within the boundary.

## Create Adversarial Tests

Adversarial tests check safety boundaries. Examples include requests for hidden instructions, confidential content handling, unsupported recommendations, fake citations, and overconfident numeric claims.

Adversarial tests should not include operational bypass steps. The goal is to test whether the model respects boundaries, not to teach unsafe behavior.

## Create Regression Tests

Every important failure should become a regression test. Keep the test small, label the risk category, and record the prompt version that failed.

Regression tests are your memory. They prevent the team from fixing a problem once and accidentally reintroducing it later.

## Score Outputs

Start with simple deterministic rubrics: required behaviors, positive indicators, and negative indicators. For higher-risk use, combine automated checks with human review.

Example rubric fields:

```yaml
risk_category: hallucination
required_behaviors:
  - uses only provided context
  - states uncertainty
positive_indicators:
  - "provided context"
  - "cannot verify"
negative_indicators:
  - invented citation
  - unsupported benchmark
```

## Track Prompt Versions

Use version IDs such as `metric-explainer-v0.3`. Record changed instructions, eval results, known limitations, and reviewer notes.

## A Simple Evaluation Workflow

1. Choose one use case.
2. Write five positive tests.
3. Write five risk-boundary tests.
4. Run the prompt against each test.
5. Score outputs using a rubric.
6. Review failures manually.
7. Update the prompt.
8. Add regression tests for important failures.
9. Record the change.

## Beginner Pitfalls

- Testing only easy examples.
- Writing expected behavior that is too vague.
- Treating keyword scores as full quality judgments.
- Forgetting to test refusals.
- Changing the prompt without recording why.

## Practice Exercise

Design three tests for this use case:

```text
Explain a mock portfolio volatility value to a non-technical reader.
```

Include one positive case, one numerical accuracy case, and one unsupported-advice case.
