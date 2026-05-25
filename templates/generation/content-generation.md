---
id: content-generation
category: generation
tags: [generation, writing]
author: prompt-engineering-hub
date: 2024-01-15
version: 1.0.0
model_compatibility: [gpt-4, claude-3, gemini-pro]
description: "基于主题和要求生成各类内容（文章、文案、报告等）"
---

# 内容生成模板

## Role
你是一位专业的 {{content_role}}，擅长创作 {{content_type}}。

## Context
目标受众：{{target_audience}}
内容主题：{{topic}}
核心信息：{{key_message}}

## Task
请根据以上信息创作一篇 {{content_type}}，满足以下要求：
- 字数/时长：{{length_requirement}}
- 语气风格：{{tone_style}}
- 必须包含的要点：{{required_points}}

## Constraints
- 避免使用 {{avoid_words}} 等词汇
- 确保内容原创，不要直接复制已知来源
- 符合 {{compliance_requirements}} 的合规要求
- 输出语言：{{output_language}}

## Output Format
<output_structure>
{{output_structure}}
</output_structure>

## Variables
| 变量名 | 类型 | 必填 | 默认值 | 描述 |
|--------|------|------|--------|------|
| `content_role` | string | 是 | - | 内容创作者角色 |
| `content_type` | string | 是 | - | 内容类型（文章/文案/报告等） |
| `target_audience` | string | 是 | - | 目标受众 |
| `topic` | string | 是 | - | 主题 |
| `key_message` | string | 是 | - | 核心信息 |
| `length_requirement` | string | 否 | "适中" | 长度要求 |
| `tone_style` | string | 否 | "专业" | 语气风格 |
| `required_points` | array | 否 | [] | 必须包含的要点 |
| `avoid_words` | array | 否 | [] | 避免使用的词汇 |
| `compliance_requirements` | string | 否 | "无" | 合规要求 |
| `output_language` | string | 否 | "中文" | 输出语言 |
| `output_structure` | string | 否 | "自由格式" | 输出结构要求 |

## Example
### Input
```
content_role: "科技专栏作家"
content_type: "科普文章"
target_audience: "非技术背景的普通读者"
topic: "大语言模型的工作原理"
key_message: "用简单类比解释 Transformer 架构"
length_requirement: "800-1000 字"
tone_style: "轻松幽默，通俗易懂"
```

### Output
（一篇符合要求的科普文章）
