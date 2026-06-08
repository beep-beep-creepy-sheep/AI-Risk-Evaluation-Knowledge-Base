# Error Analysis Playbook

Error analysis turns individual failures into better prompts, better rubrics, and stronger habits.

## Step 1: Classify the Failure

Use the risk taxonomy. A single output may have more than one issue, but choose the primary failure first.

## Step 2: Identify Root Cause

Common causes include weak task boundaries, missing source rules, vague output format, insufficient refusal language, poor numeric instructions, and missing review requirements.

## Step 3: Update the Control

The fix may be a prompt edit, a rubric edit, a checker update, or a new reviewer checklist. Keep the smallest change that addresses the failure.

## Step 4: Add a Regression Case

Capture the failure as a mock test case. Include the prompt version and expected behavior.

## Step 5: Rerun Tests

Run the automated checks and review any high-risk examples manually.

## Step 6: Record the Change

Update the changelog with the failure type, change made, and remaining limitation.

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

