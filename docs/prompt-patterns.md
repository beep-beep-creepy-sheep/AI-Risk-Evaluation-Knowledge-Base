# Prompt Patterns

The best analyst prompts define the task, data boundary, output format, and review expectation. Use the templates below with mock or public information only.

## Public Research Summary

```text
Task: Summarise the public excerpt below for an analyst learning note.

Boundaries:
- Use only the provided excerpt.
- Do not add facts, sources, or recommendations.
- Separate evidence from interpretation.
- State uncertainty where the excerpt is incomplete.

Output:
1. Executive summary
2. Key evidence
3. Limitations
4. Follow-up questions

Excerpt:
{{public_excerpt}}
```

## Mock Portfolio Metric Explanation

```text
Task: Explain the mock metric below in plain language.

Boundaries:
- Educational context only.
- Do not provide buy, sell, allocation, or timing advice.
- Use only the provided mock values.
- Include assumptions and validation checks.

Metric: {{metric_name}}
Mock value: {{metric_value}}
Context: {{mock_context}}
```

## Excel Formula Helper

```text
Task: Generate an Excel formula for this mock worksheet.

Worksheet layout:
{{columns_and_rows}}

Desired calculation:
{{calculation_goal}}

Requirements:
- Provide the formula.
- Explain assumptions about ranges and blanks.
- Add one test row or validation check.
```

## Report Logic Review

```text
Task: Review this mock analyst report section for logic and support.

Check for:
- Unsupported claims
- Numerical inconsistencies
- Missing assumptions
- Overconfident language
- Source gaps

Return issues as high, medium, or low priority.

Text:
{{mock_report_section}}
```

## Uncertainty Statement

```text
Task: Answer the question using only the available context.

Return:
- Known facts
- Assumptions
- Missing information
- Confidence level: low, medium, or high
- What would change the answer

Question:
{{question}}

Context:
{{context}}
```

