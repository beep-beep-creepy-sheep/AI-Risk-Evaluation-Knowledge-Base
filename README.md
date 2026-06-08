# AI Risk & Evaluation Knowledge Base

Professional, work-safe knowledge base for learning AI safe use, prompt engineering, and evaluation harness design in an investment and portfolio analytics context.

This repository uses only mock data and public-style examples. It does not contain real company, client, portfolio, account, employee, or internal information. It is intended as a personal learning project for analysts who want to use AI systems responsibly.

## Bilingual Navigation / 中英双语导航

The repository currently stores content in English with bilingual section labels where useful. To switch between English and Chinese in downstream readers, keep headings stable and add Chinese translations below the English text as needed.

建议使用方式：英文作为主版本，中文作为学习辅助版本。新增内容时，请保持安全边界、示例数据和审计记录一致。

## Safe-Use Boundaries

- Do not paste client data, internal documents, employee data, real portfolio holdings, account numbers, or confidential research into AI tools.
- Do not ask the model to provide personalized, unapproved, or definitive investment recommendations.
- Treat model outputs as drafts that require human review, source checking, and numerical validation.
- Use only mock examples or public-style summaries.
- Keep records of prompt versions, evaluation failures, fixes, and assumptions.

## Repository Structure

```text
docs/       Safe-use guidance, prompt patterns, taxonomy, eval design, error analysis
prompts/    Practical prompt templates for analyst workflows
evals/      Mock test cases, rubrics, and optional sample outputs
scripts/    Sensitive-data checker, eval runner, deterministic scorer
tests/      Pytest suite for schemas, checker behavior, and scoring
```

## Setup

Requires Python 3.10+.

```bash
cd ai-risk-eval-kb
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Tests

```bash
pytest
```

## Run Evaluations

```bash
python scripts/run_evals.py
```

The eval runner validates `evals/test_cases.yaml` and `evals/rubrics.yaml`, then checks any matching files under `evals/sample_outputs/`. If no sample outputs exist, it reports schema coverage only.

## Check Sensitive Data

```bash
python scripts/check_sensitive_data.py .
```

The checker flags obvious PII-like patterns such as emails, phone numbers, account numbers, addresses, client IDs, names, and restricted client-data phrases. It is intentionally conservative and may produce false positives. It skips test fixtures and eval fixture YAML by default, while still scanning files such as sample outputs.

## Add Eval Cases

1. Add a new item to `evals/test_cases.yaml`.
2. Use only mock data and public-style scenarios.
3. Include `id`, `risk_category`, `use_case`, `prompt`, `expected_behavior`, `positive_keywords`, `negative_keywords`, and `severity`.
4. If the case covers a new risk category, add or update the matching rubric in `evals/rubrics.yaml`.
5. Run `pytest` and `python scripts/run_evals.py`.

## Improve Prompts Based on Failures

1. Classify the failure using `docs/03-ai-risk-taxonomy.md`.
2. Identify whether the root cause is prompt ambiguity, missing context, weak refusal boundary, numeric reasoning, or source handling.
3. Update the relevant prompt template.
4. Add a regression test case that would have caught the failure.
5. Rerun tests and record the change in `CHANGELOG.md`.

## Limitations

This is a lightweight deterministic harness. It does not replace full model evaluation, human compliance review, source verification, or production monitoring.
