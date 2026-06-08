# 05. Error Analysis Playbook / 错误分析流程

## Repeatable Process

1. Classify the failure using the risk taxonomy.
2. Identify the root cause: missing context, weak instruction, ambiguous boundary, numerical error, source issue, or rubric gap.
3. Update the prompt, rubric, checker, or documentation.
4. Add a regression case to `evals/test_cases.yaml`.
5. Rerun `pytest` and `python scripts/run_evals.py`.
6. Record the change in `CHANGELOG.md`.

## Failure Notes Template

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

