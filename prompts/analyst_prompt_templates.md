# Analyst Prompt Templates

## Public Research Summary

```text
Summarise the following public research excerpt for a portfolio analytics learning note.
Use only the provided text. Do not add facts, sources, or recommendations.
Return: summary, evidence, limitations, and follow-up questions.

Excerpt:
{{excerpt}}
```

## Mock Metric Explanation

```text
Explain {{metric_name}} using the mock values below.
Keep the explanation educational. Do not provide investment advice.
Mention assumptions, units, and validation checks.

Mock data:
{{mock_data}}
```

## Formula Builder

```text
Create an Excel formula for this mock worksheet task.
Provide the formula, a short explanation, and one test row to validate it.

Worksheet layout:
{{layout}}

Task:
{{task}}
```

## Logic Reviewer

```text
Review this mock report section for logic, evidence, and numerical consistency.
Classify issues as high, medium, or low priority.
Do not turn the review into investment advice.

Section:
{{section}}
```

