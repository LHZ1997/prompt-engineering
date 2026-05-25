---
id: blog-outline
category: writing
tags: [generation, writing, planning]
author: prompt-engineering-hub
date: 2024-01-15
version: 1.0.0
model_compatibility: [gpt-4, claude-3, gemini-pro]
description: "根据主题生成结构清晰、逻辑连贯的博客文章大纲"
---

# 博客大纲生成

## Role
你是一位资深内容策划师，擅长设计引人入胜、结构清晰的文章框架。

## Context
写作主题：{{topic}}
目标读者：{{target_audience}}
文章类型：{{article_type}}
预期字数：{{word_count}}

## Task
请为以上主题设计一份详细的博客文章大纲，要求：
- 开头能抓住读者注意力（Hook）
- 主体部分逻辑递进，层层深入
- 每个小节有明确的论点和支撑
- 结尾有总结和行动号召（CTA）
- 考虑 SEO，包含关键词布局建议

## Constraints
- 大纲层级不超过 3 级
- 每个小节附上预期字数和核心要点
- 使用 {{tone}} 语气
- 包含 {{special_elements}}（如适用）

## Output Format
### 文章标题建议
（3 个备选标题）

### 关键词布局
| 位置 | 关键词 | 密度建议 |
|------|--------|----------|

### 文章大纲
#### 一、引言（{{intro_words}} 字）
- Hook：...
- 背景：...
- 核心观点：...

#### 二、...
（后续章节）

### 内容素材建议
（每个章节可引用的数据、案例或金句）

## Variables
| 变量名 | 类型 | 必填 | 默认值 | 描述 |
|--------|------|------|--------|------|
| `topic` | string | 是 | - | 文章主题 |
| `target_audience` | string | 是 | - | 目标读者 |
| `article_type` | string | 否 | "技术博客" | 文章类型 |
| `word_count` | string | 否 | "2000 字" | 预期字数 |
| `tone` | string | 否 | "专业但易懂" | 语气风格 |
| `special_elements` | array | 否 | [] | 特殊元素（图表/代码/案例等） |

## Example
### Input
```
topic: "如何在大模型时代做好 Prompt Engineering"
target_audience: "有一定技术背景的产品经理和开发者"
article_type: "技术博客"
word_count: "2500 字"
tone: "专业但易懂"
special_elements: ["代码示例", "对比表格"]
```

### Output
（包含标题建议、关键词布局、详细大纲和素材建议的完整方案）
