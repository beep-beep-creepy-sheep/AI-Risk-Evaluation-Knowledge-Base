# Changelog

## Unreleased

- Added an end-to-end harness workflow chapter in English and Simplified Chinese.
- Added sample mock outputs so the evaluation runner demonstrates scoring behavior, not only schema validation.
- Added pytest coverage that requires sample outputs to pass their paired rubric checks.
- Added GitHub Actions CI for docs build, pytest, eval validation, and sensitive-data scanning.
- Updated README guidance for pull request checks and sample output scoring.

## 0.2.0 - 2026-06-08

- Converted the knowledge base into a bilingual VitePress documentation website.
- Added English root pages and Simplified Chinese pages under `/zh/`.
- Added local search, book-like sidebars, language navigation, and Cloudflare Pages deployment instructions.
- Added Vercel deployment configuration and deployed the site as `ai-risk-eval-kb`.
- Expanded chapters into a beginner-friendly textbook style with learning objectives, examples, review questions, and exercises.
- Preserved the mock evaluation harness and sensitive-data checker alongside the docs site.

## 0.1.0 - 2026-06-08

- Created initial mock-only AI risk and evaluation knowledge base.
- Added safe-use documentation, analyst prompt templates, risk taxonomy, evaluation design guide, and error analysis playbook.
- Added YAML test cases and rubrics across core AI risk categories.
- Added deterministic scoring, sensitive-data checker, eval runner, and pytest coverage.
