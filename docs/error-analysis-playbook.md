# Error Analysis Playbook

Error analysis turns individual failures into better prompts, better rubrics, and stronger habits.

## Learning Objectives

After this chapter, you should be able to:

- Review a bad output without simply blaming the model.
- Identify whether the prompt, rubric, context, or workflow caused the failure.
- Add a targeted fix and a regression test.
- Record the change clearly enough for future reviewers.

## Step 1: Classify the Failure

Use the risk taxonomy. A single output may have more than one issue, but choose the primary failure first.

Example: If a model invents a source and then gives advice, classify the primary failure based on the most serious issue for the workflow. In many analyst settings, unsupported advice may be the primary failure, with hallucination as a secondary issue.

## Step 2: Identify Root Cause

Common causes include weak task boundaries, missing source rules, vague output format, insufficient refusal language, poor numeric instructions, and missing review requirements.

Root-cause questions:

- Did the prompt say what information was allowed?
- Did it say what to do when context was missing?
- Did it define the output format?
- Did the rubric check the behavior that failed?
- Was a human review step missing?

## Step 3: Update the Control

The fix may be a prompt edit, a rubric edit, a checker update, or a new reviewer checklist. Keep the smallest change that addresses the failure.

Avoid over-correcting. If a prompt hallucinated a citation, do not make the model refuse all summaries. Add a clearer source rule and a test case.

## Step 4: Add a Regression Case

Capture the failure as a mock test case. Include the prompt version and expected behavior.

## Step 5: Rerun Tests

Run the automated checks and review any high-risk examples manually.

## Step 6: Record the Change

Update the changelog with the failure type, change made, and remaining limitation.

## Worked Example

Observed failure:

```text
The model summarised a mock excerpt and added a benchmark return that was not provided.
```

Classification:

```text
Primary risk: hallucination
Secondary risk: source reliability
```

Root cause:

```text
The prompt asked for "market context" but did not say to use only provided information.
```

Fix:

```text
Add: "Use only the provided excerpt. If market context is missing, state that it is missing."
```

Regression case:

```text
Ask the model to summarise a one-sentence mock excerpt and check that it does not add benchmark, macro, or source details.
```

## Failure Note Template

```text
Failure ID:
Date:
Risk category:
Prompt version:
Observed output:
Expected behavior:
Root cause:
Change made:
Regression test added:
Reviewer notes:
```

## Practice Exercise

Read this fictional failure:

```text
The model generated an Excel formula, but did not mention that blank rows could change the result.
```

Answer:

- What is the primary risk category?
- What prompt instruction was probably missing?
- What regression test would you add?
