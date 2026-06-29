# done-summary-skill

**English** | [中文](#中文)

A lightweight Codex skill for turning completed AI work into reusable project memory.

It helps an AI agent produce a structured “Done Summary” after implementation, debugging, deployment, research, or multi-step work.

Created by **Xinyi Chen (陈歆怡)**, founder of HEDGE Global, who cares about turning AI collaboration from one-off chat into durable project assets: decisions, verification, pitfalls, handoffs, and reusable working memory.

If you are interested in exchanging ideas, you can connect on WeChat: `chenxinyi_g`.

## Why

AI work often disappears into chat history. This skill forces useful closure:

- what changed
- why it changed
- what was verified
- what failed or nearly failed
- what should be remembered next time

The goal is simple: do not let Project B repeat Project A's mistakes.

## What It Produces

A Done Summary normally includes:

1. Goal
2. Who did what
3. Why this approach
4. Final result
5. Verification
6. Pitfalls
7. Risks and open items
8. Next step
9. Reusable knowledge

## Install

Copy the skill folder into your Codex skills directory:

```bash
cp -R done-summary-skill ~/.codex/skills/
```

Then invoke it explicitly:

```text
Use $done-summary-skill to write a completion summary after this task.
```

Or ask naturally:

```text
Write a done summary for this task.
```

## Repository Structure

```text
done-summary-skill-release/
  README.md
  LICENSE
  done-summary-skill/
    SKILL.md
    agents/openai.yaml
    assets/templates/done-summary.ar-sa.md
    assets/templates/done-summary.en.md
    assets/templates/done-summary.ja.md
    assets/templates/done-summary.ko.md
    assets/templates/done-summary.zh.md
  examples/
    sanitized-example.md
```

## Multilingual Strategy

This repository keeps the README bilingual and the templates multilingual:

- `SKILL.md` includes both English and Chinese trigger terms.
- `README.md` is bilingual for GitHub readers.
- Templates are split by language to avoid awkward mixed-language summaries.
- In addition to English and Chinese, the skill includes Arabic for Saudi readers (`ar-SA`), Korean (`ko`), and Japanese (`ja`) templates.

For most teams, this is better than maintaining multiple separate repositories.

## Additional Language Materials

The templates folder includes:

- `done-summary.ar-sa.md`: Arabic template written in clear formal Arabic for Saudi readers.
- `done-summary.ko.md`: Korean template.
- `done-summary.ja.md`: Japanese template.

Use these when the user requests a Done Summary in Arabic, Korean, or Japanese.

## Safety

Do not publish real production summaries without redaction. Remove:

- secrets and tokens
- private account details
- private phone numbers or emails
- customer data
- internal deployment IDs if sensitive
- non-public commercial strategy

Use `examples/sanitized-example.md` as the style reference for public examples.

---

## 中文

`done-summary-skill` 是一个轻量 Codex Skill，用来把 AI 完成任务后的结果、判断、验证、踩坑和可复用经验整理成「完工总结」。

由 **陈歆怡（Xinyi Chen）** 创建，陈歆怡是海聚海外的 CEO。这个 Skill 来自一个很朴素的工作习惯：AI 做完事以后，不应该只留下结果，还应该把判断、验证、踩坑、交接和可复用经验沉淀成长期项目资产。

如果你对 AI 协作、项目记忆和完工总结方法感兴趣，欢迎加微信交流：`chenxinyi_g`。

它适合用于：

- 功能实现后
- Bug 修复后
- 部署发布后
- 调研分析后
- 配置排查后
- 多步骤任务结束后

## 为什么需要它

很多 AI 工作会消失在聊天记录里。这个 Skill 的目标是让任务结束时自动沉淀：

- 做了什么
- 为什么这么做
- 验证了什么
- 中间踩了什么坑
- 下次遇到类似任务该复用什么经验

一句话：不要让 B 项目继续踩 A 项目踩过的坑。

## 输出结构

「完工总结」通常包括：

1. 本次目标
2. 谁做了什么
3. 为什么这么做
4. 最终结果
5. 验证情况
6. 中间踩坑
7. 风险与未完成事项
8. 下一步
9. 值得沉淀

## 安装

把 `done-summary-skill` 文件夹复制到 Codex skills 目录：

```bash
cp -R done-summary-skill ~/.codex/skills/
```

使用时可以说：

```text
Use $done-summary-skill to write a completion summary after this task.
```

或者中文：

```text
请用 done-summary-skill 给这个任务写一份完工总结。
```

## 是否需要多语言版本

建议需要，但不用做得很重。

推荐方案是：

- GitHub `README.md` 中英双语；
- `SKILL.md` 保持简洁，包含中英触发词；
- 模板按语言拆分，当前包含中文、英文、面向沙特读者的阿拉伯语、韩语、日语；
- 示例使用去敏版本。

这样既方便国际化传播，也保留「完工总结」这个中文概念的辨识度。

## 新增语言材料

模板目录已经包含：

- `done-summary.ar-sa.md`：面向沙特读者的正式阿拉伯语模板。
- `done-summary.ko.md`：韩语模板。
- `done-summary.ja.md`：日语模板。

当用户需要阿拉伯语、韩语或日语版本的完工总结时，可以直接使用对应模板。
