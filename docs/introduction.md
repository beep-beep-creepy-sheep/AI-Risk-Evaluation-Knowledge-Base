# Introduction

AI tools can help analysts draft notes, summarise public material, explain calculations, and design tests. They can also introduce errors that look polished enough to be trusted too quickly.

This handbook gives you a practical operating model for using AI in a risk-aware way. It focuses on portfolio analytics-style workflows, but every example is mock or public-style. The purpose is education, quality assurance, and repeatable evaluation design.

## Learning Objectives

By the end of this handbook, you should be able to:

- Describe common AI risks in analyst workflows using plain language.
- Write safer prompts that define task boundaries, data boundaries, and review expectations.
- Build simple test cases for hallucination, data leakage, prompt injection, numerical errors, and unsupported recommendations.
- Review model outputs for source quality, assumptions, uncertainty, and auditability.
- Turn failures into prompt changes, regression tests, and changelog entries.

## A Beginner Mental Model

Think of an AI model as a drafting and reasoning assistant, not as a database, calculator, compliance officer, or investment decision-maker. It can help organise work, but it does not know which information is approved, which source is current, or which conclusion is suitable for professional use unless you define those boundaries and review the output.

For a new analyst, the safest workflow is:

1. Start with mock or public-style information.
2. Ask for a structured draft.
3. Require assumptions, uncertainty, and limitations.
4. Check facts and calculations outside the model.
5. Record what changed after review.

## Working Principles

- Keep sensitive information out of prompts and sample files.
- Treat AI output as a draft, not an approval.
- Ask for sources, assumptions, uncertainty, and validation checks.
- Test prompts with ordinary, edge-case, and adversarial scenarios.
- Record prompt versions and changes so improvements are traceable.

## Key Terms

| Term | Plain-English Meaning |
| --- | --- |
| Prompt | The instruction and context given to an AI model. |
| Evaluation | A structured test of whether the model behaves as expected. |
| Test case | A single prompt with expected behavior and pass/fail signals. |
| Rubric | The scoring rules used to judge an output. |
| Regression test | A test added after a failure so the same problem does not return unnoticed. |
| Human review | A qualified person checking facts, calculations, suitability, and risk. |

## Example Learning Path

If you are completely new, read the chapters in this order:

1. **Safe-Use Principles** to learn what must stay outside AI tools.
2. **Prompt Patterns** to learn how to write bounded, useful instructions.
3. **Risk Taxonomy** to learn the vocabulary of AI failures.
4. **Evaluation Design** to turn risks into tests.
5. **Test Case Library** to see mock examples.
6. **Error Analysis** to improve prompts after failures.
7. **Templates & Checklists** to make the workflow repeatable.

## How to Read This Handbook

Start with safe-use principles, then move into prompt patterns. Use the risk taxonomy to classify failures, the evaluation chapter to design tests, and the templates chapter to create repeatable review habits.

## Practice Exercise

Choose one safe task, such as "summarise a public-style research excerpt." Write down:

- What information is allowed.
- What information is not allowed.
- What the output should include.
- What the output must avoid.
- How a reviewer would check it.
