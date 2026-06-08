# 02. Prompt Patterns for Analysts / 分析师提示词模式

Use these patterns with mock data or public information only.

## Summarise Public Research

```text
Task: Summarise the public research excerpt below for an analyst audience.

Boundaries:
- Use only the provided excerpt.
- Do not infer private or non-public information.
- Separate facts, interpretations, and open questions.
- State uncertainty where the excerpt is incomplete.

Output format:
1. Executive summary
2. Key evidence
3. Risks and limitations
4. Questions for human follow-up

Excerpt:
{{public_research_excerpt}}
```

## Explain Portfolio Metrics

```text
Task: Explain the mock portfolio metric below in plain language.

Boundaries:
- This is educational and not investment advice.
- Use only the mock values provided.
- Do not recommend buying, selling, or reallocating assets.
- Flag assumptions and calculation caveats.

Metric:
{{metric_name}}

Mock value:
{{metric_value}}

Context:
{{mock_context}}
```

## Generate Excel Formulas

```text
Task: Generate an Excel formula for the described mock worksheet.

Boundaries:
- Use only the worksheet layout provided.
- Explain assumptions about ranges and missing values.
- Include a simple validation check.
- Do not use external data.

Worksheet layout:
{{columns_and_rows}}

Desired calculation:
{{calculation_goal}}
```

## Check Report Logic

```text
Task: Review the logic of this mock analyst report section.

Boundaries:
- Do not rewrite conclusions as investment recommendations.
- Check consistency, missing assumptions, unsupported claims, and numerical logic.
- Mark each issue as high, medium, or low priority.

Report section:
{{mock_report_section}}
```

## Draft Market Commentary from Provided Public or Mock Information

```text
Task: Draft neutral market commentary using only the information below.

Boundaries:
- Use only provided public or mock information.
- Do not make forward-looking recommendations.
- Avoid certainty beyond the evidence.
- Include a short uncertainty statement.

Information:
{{provided_public_or_mock_information}}
```

## State Uncertainty

```text
Task: Answer the analyst question below and explicitly state uncertainty.

Boundaries:
- Separate known facts from assumptions.
- Identify missing information.
- Provide confidence level: low, medium, or high.
- Explain what would change the answer.

Question:
{{question}}

Available context:
{{context}}
```

