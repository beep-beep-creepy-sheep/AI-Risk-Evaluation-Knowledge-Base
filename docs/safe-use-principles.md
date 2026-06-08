# Safe-Use Principles

Safe AI use starts before a prompt is written. The most important control is deciding what should never enter the system.

## Learning Objectives

After this chapter, you should be able to:

- Explain why mock data is the default for learning and testing.
- Identify sensitive information that should not be entered into AI tools.
- Add human review, source checking, numerical validation, and audit records to an AI workflow.
- Convert a risky request into a safe mock-data exercise.

## Confidentiality

Do not put confidential, private, account-level, employee-level, or non-public material into AI tools. Use synthetic examples and public-style text when learning or testing.

Beginner rule: if you would hesitate to paste the information into a public forum, do not paste it into a general AI tool. Even when a system is approved for some use, the allowed data types and retention rules should be checked first.

## Mock Data Only

Examples in this knowledge base are fictional. If a workflow needs real information, the analysis should happen through approved systems and human review channels.

Mock data should be realistic enough to test the workflow, but not traceable to a real person, client, account, employer, or internal process.

## Common Sensitive Inputs to Avoid

| Input Type | Why It Is Risky | Safer Substitute |
| --- | --- | --- |
| Real account identifiers | Could expose private records | `MOCK-ACCOUNT-001` |
| Real holdings or transactions | Could reveal private portfolio information | Synthetic holdings with fictional labels |
| Internal documents | Could disclose non-public information | Short public-style excerpt written for the exercise |
| Employee names or notes | Could create privacy or HR risk | Generic roles such as "Reviewer A" |
| Private research views | Could expose confidential analysis | Public-source summary or mock thesis |

## Human Review

AI-generated work should be reviewed by a qualified person before professional use. Reviewers should check facts, calculations, source support, tone, and whether the output stays within the requested scope.

Human review is not a formality. It is where unsupported claims, missing caveats, wrong units, and inappropriate recommendations are caught.

## Source Checking

When working with public research, distinguish between provided evidence and model-generated interpretation. Ask the model to identify missing sources and avoid unsupported claims.

Useful prompt phrase:

```text
Use only the sources provided. If a claim is not supported by the provided sources, label it as "needs verification" instead of presenting it as fact.
```

## Numerical Validation

Portfolio metrics, risk statistics, and spreadsheet formulas require independent checks. Ask for assumptions, units, time periods, and validation rows.

For any numeric output, ask:

- What inputs were used?
- What formula was applied?
- Are the units clear?
- Does the result pass a simple sanity check?
- Would a spreadsheet or calculator reproduce the number?

## Auditability

Keep prompt versions, test cases, outputs, reviewer notes, and changelog entries. A good AI workflow should be explainable after the fact.

## Safe Rewrite Example

Risky request:

```text
Summarise this private account note and recommend what the client should do.
```

Safer learning request:

```text
Using the fictional scenario below, identify what additional information a qualified reviewer would need before making any decision. Do not provide investment advice.
```

## Chapter Review Questions

- What information should never appear in a prompt for this project?
- How would you turn a real-data request into a mock-data exercise?
- What are the minimum checks before using an AI-generated analyst draft?
