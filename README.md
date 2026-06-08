# AI Risk & Evaluation Knowledge Base

A bilingual VitePress documentation website for learning safe AI use, prompt engineering, AI risk testing, and evaluation harness design in analyst workflows.

English is the default language at `/`. Simplified Chinese is available at `/zh/`.

## Live Website

View the deployed handbook here:

[https://ai-risk-eval-kb.vercel.app](https://ai-risk-eval-kb.vercel.app)

## Safety Boundaries

- Use mock data and public-style examples only.
- Do not include real client data, real portfolio holdings, account numbers, employee names, confidential company information, or internal documents.
- Do not mention any real employer.
- Do not provide financial advice or investment recommendations.
- Do not include jailbreak, bypass, or safety-circumvention instructions.
- Frame content as education, quality assurance, safe-use guidance, and risk management.

## Site Structure

```text
docs/
  index.md                         English landing page
  introduction.md                  English handbook chapters
  safe-use-principles.md
  prompt-patterns.md
  risk-taxonomy.md
  evaluation-design.md
  test-case-library.md
  error-analysis-playbook.md
  templates-checklists.md
  zh/                              Simplified Chinese pages
  .vitepress/config.ts             VitePress configuration

evals/                             Mock evaluation fixtures
scripts/                           Python eval and sensitive-data utilities
tests/                             Pytest coverage for the utilities
```

## Local Development

Requires Node.js 18+ and Python 3.10+.

```bash
npm install
npm run docs:dev
```

The local VitePress server will print a URL such as `http://localhost:5173/`.

## Build the Website

```bash
npm run docs:build
npm run docs:preview
```

The static build output is written to:

```text
docs/.vitepress/dist
```

## Cloudflare Pages Deployment

Cloudflare Pages is the recommended deployment path.

Use these settings:

- Project name: `ai-risk-eval-kb`
- Production branch: `main`
- Build command: `npm run docs:build`
- Build output directory: `docs/.vitepress/dist`
- Framework preset: `None` or `VitePress` if available

Typical flow:

1. Push this repository to GitHub.
2. In Cloudflare Pages, choose **Create a project**.
3. Connect the repository.
4. Name the Pages project `ai-risk-eval-kb`.
5. Set the build command and output directory above.
6. Deploy from `main`.

Use a unique Cloudflare Pages project name for each future book or knowledge base. For example, keep this site as `ai-risk-eval-kb`, then use a different project name such as `portfolio-metrics-handbook` for another book. That prevents a later deployment from replacing this site.

## GitHub Pages Alternative

GitHub Pages can also host the generated static site. Configure a workflow that runs `npm install` and `npm run docs:build`, then publishes `docs/.vitepress/dist`. Cloudflare Pages is simpler for this project because the build settings map directly to VitePress.

## Vercel Deployment

This site can also be deployed on Vercel as an independent project named `ai-risk-eval-kb`.

Recommended settings:

- Project name: `ai-risk-eval-kb`
- Build command: `npm run docs:build`
- Output directory: `docs/.vitepress/dist`

The current production deployment is:

```text
https://ai-risk-eval-kb.vercel.app
```

## Run Python Checks

The repository still includes a lightweight mock evaluation harness.

```bash
pip install -r requirements.txt
pytest
python scripts/run_evals.py
python scripts/check_sensitive_data.py .
```

## Add or Improve Content

1. Update the English chapter first.
2. Add a natural Simplified Chinese counterpart under `docs/zh/`.
3. Keep links aligned across languages.
4. Use only mock or public-style examples.
5. Run `npm run docs:build`, `pytest`, and the sensitive-data checker.
6. Record meaningful changes in `CHANGELOG.md`.

## Limitations

The site is an educational handbook and a lightweight evaluation demo. It does not replace professional review, compliance approval, source verification, production monitoring, or qualified investment governance.
