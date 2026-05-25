# 贡献指南

感谢你对 Prompt Engineering Hub 的关注！本文档说明如何向本项目贡献新的 Prompt 或改进现有内容。

## 贡献流程

1. **Fork 仓库**（如果是外部贡献者）或创建新分支
2. **按规范编写/修改 Prompt 文件**
3. **本地运行校验脚本**确保格式正确
4. **提交 Pull Request**，等待 CI 校验通过
5. **维护者 Review 后合并**

## 文件格式要求

每个 Prompt 文件必须是一个 Markdown 文件（`.md`），并包含以下结构：

### YAML Frontmatter（必填）

文件顶部必须包含 YAML frontmatter：

```yaml
---
id: unique-prompt-id
category: software-development
tags: [code-review, python, best-practices]
author: your-name
date: 2024-01-15
version: 1.0.0
model_compatibility: [gpt-4, claude-3, gemini-pro]
description: "简短描述该 prompt 的用途和场景"
---
```

字段说明：

| 字段 | 必填 | 说明 |
|------|------|------|
| `id` | 是 | 全局唯一标识符，使用 kebab-case |
| `category` | 是 | 一级分类，必须在预定义列表中 |
| `tags` | 是 | 能力标签数组，至少一个 |
| `author` | 是 | 作者名或 GitHub ID |
| `date` | 是 | 创建日期，格式 `YYYY-MM-DD` |
| `version` | 是 | 语义化版本号 |
| `model_compatibility` | 否 | 测试过的模型列表 |
| `description` | 是 | 一句话描述用途 |

### 正文结构

```markdown
# Prompt 标题

## Role
定义模型应扮演的角色和身份。

## Context
提供必要的背景信息、场景描述或输入数据。

## Task
明确、具体的任务指令。使用祈使句，避免歧义。

## Constraints
列出必须遵守的约束条件（如长度限制、格式要求、禁止事项）。

## Output Format
描述期望的输出格式。可使用 JSON Schema、Markdown 表格或示例说明。

## Variables
| 变量名 | 类型 | 必填 | 默认值 | 描述 |
|--------|------|------|--------|------|
| `var_name` | string | 是 | - | 变量说明 |

## Example
### Input
提供示例输入。

### Output
提供对应示例输出。
```

### 命名规范

- **文件名**：使用 kebab-case，如 `code-review.md`, `blog-outline.md`
- **ID**：与文件名一致（不含扩展名），全局唯一
- **目录名**：使用 kebab-case，与 `category` 字段对应

## 本地校验

提交 PR 前，请在本地运行校验脚本：

```bash
python scripts/validate-prompts.py
```

校验内容包括：
- YAML frontmatter 是否完整
- `id` 是否全局唯一
- `category` 是否在预定义列表中
- `tags` 格式是否合规
- 必填字段是否缺失

## 版本管理

- 修改现有 Prompt 时，更新 `version` 字段
- 遵循语义化版本：
  - `x.y.z+1`：文案微调、示例更新
  - `x.y+1.0`：结构变更、新增变量
  - `x+1.0.0`：重大变更、不兼容旧版本
- 如需保留旧版本，将旧文件移至 `prompts/{category}/archive/`

## 预定义分类与标签

### 一级分类（category）

- `software-development`
- `writing`
- `data-analysis`
- `product-management`
- `ai-development`

### 常用标签（tags）

- `code-review`, `refactoring`, `testing`, `documentation`
- `generation`, `translation`, `summarization`
- `reasoning`, `analysis`, `extraction`
- `roleplay`, `interview`, `simulation`
- `optimization`, `evaluation`

## 模板贡献

向 `templates/` 目录贡献模板时，使用 `{{variable_name}}` 作为变量占位符，并在 `Variables` 章节说明每个占位符的用途。

## 问题与讨论

如有疑问，欢迎通过 Issue 讨论。
