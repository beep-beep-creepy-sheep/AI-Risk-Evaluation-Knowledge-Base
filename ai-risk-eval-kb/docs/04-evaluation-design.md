# 04. Evaluation Design / 评估设计

## Define the Use Case

Describe the workflow, user, input type, expected output, and safety boundaries. Example: "Summarise a public research excerpt for educational review using only provided text."

## Define Expected Behaviour

Write concrete behavior statements. Include what the model should do, what it should refuse, and what it should ask for when context is insufficient.

## Create Adversarial Tests

Include prompts that try to trigger unsafe behavior, such as requests for client data use, unsupported recommendations, hidden instruction following, fake citations, or confidential information.

## Create Positive Tests

Include ordinary safe-use prompts where the model should help: explain a mock metric, draft neutral commentary from provided mock facts, or generate an Excel formula with caveats.

## Create Regression Tests

When a failure occurs, add a test case that represents the failure. Regression cases should be small, clear, and tied to a specific risk category.

## Score Outputs

Use rubrics that combine required behaviors, positive indicators, and negative indicators. Deterministic keyword checks are useful for early development but should be supplemented with human review.

## Track Prompt Versions

Record prompt template changes, eval results, and known limitations. Use `CHANGELOG.md` to preserve a concise history of improvements.

