---
name: done-summary-skill
description: Create a Done Summary / 完工总结 after completed AI work. Use when the user asks for a 完工总结, done summary, completion summary, work log, post-task summary, handoff, retrospective, lessons learned, writeback, or wants task results, verification, pitfalls, risks, next steps, and reusable knowledge captured after implementation, debugging, deployment, research, configuration, or multi-step work.
---

# Done Summary Skill / 完工总结 Skill

Use this skill to turn finished work into reusable project memory. Prefer the user's language for headings and prose.

## Core Workflow

1. Confirm the work is actually finished, or clearly state what remains unfinished.
2. Gather evidence from the current turn: files changed, commands run, validation results, links, artifacts, decisions, and blockers.
3. Separate facts from inference. Mark inferred causes as inferred.
4. Write the Done Summary using the compact structure below.
5. Identify what should be written back to project docs, memory, runbooks, or future task instructions.
6. Remove secrets, private contact details, tokens, customer data, and non-public business details before producing a shareable summary.

## Required Sections

For Chinese users, use:

- `本次目标`
- `谁做了什么`
- `为什么这么做`
- `最终结果`
- `验证情况`
- `中间踩坑`
- `风险与未完成事项`
- `下一步`
- `值得沉淀`

For English users, use:

- `Goal`
- `Who Did What`
- `Why This Approach`
- `Final Result`
- `Verification`
- `Pitfalls`
- `Risks And Open Items`
- `Next Step`
- `Reusable Knowledge`

Keep the summary concise. For small tasks, collapse sections into short paragraphs. For medium or larger tasks, keep section headings.

## Writeback Guidance

Recommend writing back when the task revealed durable knowledge such as:

- Real source path, wrapper folder, service name, deployment path, or runtime entrypoint.
- Commands for install, build, test, deploy, smoke checks, rollback, or data refresh.
- Tool failure modes, API changes, model changes, timeout fixes, environment quirks, or authentication issues.
- Data definitions, metric logic, report contracts, missing-data markers, or validation rules.
- User preferences, exact output format, naming convention, compliance wording, or acceptance criteria.
- Reusable debugging paths, known errors, and how to avoid repeating them.

If editing project docs is allowed by the current task, update the relevant file. If not, explicitly suggest where the knowledge should be written.

## Safety Rules

- Do not include secrets, tokens, private keys, full credentials, raw customer data, private phone numbers, or private email addresses.
- Redact local-only or private details when writing a public example.
- Do not claim verification passed unless it was actually run and passed.
- If verification failed, include the failure and the likely cause.
- Do not make marketing claims from weak evidence; keep outcome claims proportional to validation.

## Templates

Use bundled templates when a concrete file is useful:

- Chinese: `assets/templates/done-summary.zh.md`
- English: `assets/templates/done-summary.en.md`

For public GitHub examples, use a sanitized example rather than a real client or production project summary.
