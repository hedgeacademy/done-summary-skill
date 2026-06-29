# GitHub Publishing Guide

This folder is ready to publish as a GitHub repository named:

```text
done-summary-skill
```

## Recommended Visibility

Public is fine if you keep only the sanitized content in this package.

Before publishing, do not add:

- real project completion summaries
- private local paths
- tokens, API keys, or deployment secrets
- customer names, phone numbers, or emails
- internal business strategy

## Publish With GitHub CLI

From this folder:

```bash
cd /path/to/done-summary-skill-release
git init
git add .
git commit -m "Initial release of done-summary-skill"
gh repo create done-summary-skill --public --source=. --remote=origin --push
```

## Publish With GitHub Web UI

1. Create a new GitHub repository named `done-summary-skill`.
2. Do not initialize it with a README, license, or gitignore because this folder already includes them.
3. Upload or push all files from this folder.

## Install After Publishing

Users can install the skill by copying the skill folder:

```bash
cp -R done-summary-skill ~/.codex/skills/
```

Then invoke it with:

```text
Use $done-summary-skill to write a completion summary after this task.
```

## Suggested Repository Description

```text
A bilingual Codex skill for turning completed AI work into reusable project memory.
```

## Suggested Topics

```text
codex
ai-agent
skill
handoff
retrospective
project-memory
completion-summary
```
