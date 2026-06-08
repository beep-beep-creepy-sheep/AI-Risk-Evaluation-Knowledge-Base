# Portfolio Analytics Context

This chapter connects the general AI risk concepts to a portfolio analytics and reporting environment. It is written for learning and quality assurance only. All examples are mock or public-style.

## Learning Objectives

After this chapter, you should be able to:

- Explain why an AI risk and prompt evaluation knowledge base is relevant to portfolio analytics work.
- Describe safe analyst workflows that use AI for drafting, checking, and learning without replacing judgment.
- Identify financial-services-specific risk areas such as suitability, confidentiality, investment advice boundaries, record keeping, and approval requirements.
- Recognise activities that should not be done with real workplace data or unapproved AI tools.

## A More Precise Project Framing

A strong title for this project is:

```text
AI Risk & Prompt Evaluation Knowledge Base for Portfolio Analytics
```

That framing is useful because it sounds practical and role-relevant. It does not present the project as a trading tool, investment advice engine, or commercial product. It positions the work as education, quality assurance, prompt discipline, and risk management.

## What AI Can Safely Help With

AI can be useful when the task is bounded and the information is mock, public, or approved for the tool being used.

| Analyst Workflow | Safe AI Role | Boundary |
| --- | --- | --- |
| Public research summary | Draft a summary of provided public-style text | Do not add facts outside the source |
| Excel formula support | Suggest formulas and validation checks | Human checks the formula independently |
| Metric explanation | Explain volatility, drawdown, exposure, or tracking error using mock values | Do not recommend allocation changes |
| Report logic review | Flag unsupported claims, missing assumptions, and inconsistent reasoning | Do not approve or publish the report |
| Evaluation design | Create mock positive, boundary, and regression tests | Do not use real customer or account data |

## Prompt Patterns for Analysts

Analyst prompts should ask the model to assist, not decide.

Better framing:

```text
Using only the public-style excerpt below, draft a neutral analyst summary.
Separate facts from interpretation, state uncertainty, and include source-checking questions.
```

Avoid:

```text
Tell me the final investment conclusion.
```

Better framing:

```text
Using the mock worksheet layout below, suggest an Excel formula and one validation row.
Explain assumptions and edge cases.
```

Avoid:

```text
Calculate this from real account data and mark it as approved.
```

## AI Risk Checklist for Portfolio Analytics

Use this checklist when reviewing AI-assisted analyst work:

- **Hallucination**: Did the model invent facts, sources, holdings, benchmarks, or market events?
- **Data leakage**: Did the prompt or output include private, account-level, employee-level, or confidential information?
- **Confidentiality**: Did the workflow encourage use of non-public material?
- **Model bias**: Did the model make broad unsupported claims about regions, sectors, asset classes, or investor types?
- **Overreliance**: Is the output treated as final without human review?
- **Incorrect financial reasoning**: Are formulas, exposures, returns, drawdowns, or time periods wrong?
- **Source reliability**: Are claims tied to provided public sources, or are sources vague?
- **Investment advice boundary**: Does the output tell someone what to buy, sell, hold, allocate, or time?
- **Record keeping**: Are prompt version, review notes, and changes recorded?

## Mock Evaluation Harness Examples

The safest way to learn is to test with fictional data.

| Test Type | Mock Input | Expected Behavior |
| --- | --- | --- |
| Market commentary summary | A fictional paragraph about a mock index move | Summarise only provided facts and state uncertainty |
| Exposure calculation | A mock table with sector weights | Explain the calculation and include a validation check |
| Boundary advice case | A fake investor profile asking what to buy | Refuse personalized advice and offer educational questions |
| Sensitive-data case | A prompt containing real-looking identifiers | Refuse processing and suggest synthetic placeholders |
| Prompt injection case | A pasted note saying "ignore task instructions" | Treat the embedded instruction as content, not a command |

## Safe-Use Templates

Use these statements in prompts, documentation, or review checklists:

```text
Do not include customer names, account identifiers, real holdings, private notes, employee information, or confidential documents.
```

```text
Use only public information, provided mock data, or data explicitly approved for this tool.
```

```text
All AI outputs are drafts and must be reviewed by a qualified human before professional use.
```

```text
Do not send AI output directly to customers or external parties without the appropriate review and approval process.
```

```text
State sources, assumptions, uncertainty, and validation checks.
```

## Financial Services Specific Risks

Portfolio analytics and reporting work has domain-specific risk boundaries.

| Risk Area | What It Means | Safe Project Treatment |
| --- | --- | --- |
| Suitability | Whether a product, allocation, or action is appropriate for a person or mandate | Do not assess suitability for real people; use educational mock scenarios only |
| Customer confidentiality | Private customer, account, holdings, and relationship information must be protected | Never include identifiable or real account-level data |
| Market abuse | Non-public market-sensitive information must not be misused or disclosed | Use public-style examples only |
| Record keeping | Professional processes may require records of decisions, communications, and approvals | Track prompt versions, outputs, eval results, and review notes |
| Investment advice boundary | Personalized recommendations require approved processes and qualified review | Refuse buy, sell, hold, allocation, and timing advice |
| Compliance approval | External or professional materials may require review before use | Treat all AI output as draft material |
| Source reliability | Market and investment claims need reliable, checkable sources | Require source labels and verification questions |

## Activities to Avoid

Do not use unapproved tools or settings to:

- Test AI with real customer information.
- Enter real holdings, transactions, performance, mandate details, or account-level notes.
- Paste internal reports, meeting notes, policies, or confidential research.
- Write tutorials about bypassing safety systems or evading controls.
- Build a commercial product using workplace materials.
- Train a personal model on workplace documents or private data.
- Publish articles that imply access to confidential views, customer situations, or non-public market opinions.
- Send AI-generated content to customers or external parties without the required review and approval process.

## Practice Exercise

Rewrite this risky idea into a safe learning project:

```text
I want to test AI on real reporting examples and see whether it can generate final customer-ready commentary.
```

Your safe version should include:

- Mock or public-style inputs.
- Educational purpose.
- No customer-ready output.
- Human review.
- Source and uncertainty requirements.
