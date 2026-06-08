# Instructions for Future AI Coding Agents

This repository is a professional, work-safe AI risk and evaluation knowledge base for a personal learning project.

## Non-Negotiable Safety Boundaries

- Use mock data only.
- Do not add real company, employer, client, portfolio, account, employee, or confidential information.
- Do not mention any real employer name in repository content.
- Do not create jailbreak instructions, bypass tactics, or unsafe prompt-injection playbooks.
- Do not provide personalized, definitive, or unapproved investment advice.
- Keep examples professional, compliance-aware, and suitable for analyst education.

## Engineering Expectations

- Keep the VitePress site Markdown-first and easy to maintain.
- English is the root/default language. Simplified Chinese lives under `docs/zh/`.
- Run `npm run docs:build` after documentation or VitePress config changes.
- Run `pytest` after changes.
- Run `python scripts/run_evals.py` when changing eval cases, rubrics, sample outputs, or scoring logic.
- Run `python scripts/check_sensitive_data.py .` before finalizing content changes.
- Document assumptions in README, docs, or changelog when behavior changes.
- Keep dependencies minimal.
- Prefer clear deterministic checks over complex machinery unless the repository owner requests more sophistication.

## Content Expectations

- Preserve safe-use boundaries in every document and prompt.
- Use public-style examples and clearly marked mock data.
- Make uncertainty explicit in templates and expected behaviors.
- Include human review, source checking, auditability, and record-keeping where relevant.
- Record meaningful changes in `CHANGELOG.md`.
- Keep Chinese pages natural and professional rather than literal word-for-word translations.
