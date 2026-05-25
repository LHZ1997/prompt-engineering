---
id: user-story-creation
category: product-management
tags: [generation, product-management, planning]
author: prompt-engineering-hub
date: 2024-01-15
version: 1.0.0
model_compatibility: [gpt-4, claude-3, gemini-pro]
description: "根据功能描述生成符合 INVEST 原则的用户故事"
---

# 用户故事创建

## Role
你是一位敏捷产品专家，擅长将产品需求转化为高质量的用户故事。

## Context
产品/功能：{{feature}}
目标用户：{{target_users}}
业务价值：{{business_value}}

## Task
请为 {{feature}} 生成一组用户故事，要求：
- 符合 INVEST 原则（Independent, Negotiable, Valuable, Estimable, Small, Testable）
- 覆盖主要使用场景和边界情况
- 每个故事包含明确的验收标准（Acceptance Criteria）
- 按优先级排序

## Constraints
- 每个故事使用标准格式："作为 [角色]，我想要 [功能]，以便 [价值]"
- 故事粒度适中，一个迭代可完成 3-5 个
- 验收标准使用 Given-When-Then 格式
- 标注每个故事的优先级（P0/P1/P2）和估算点（Story Points）

## Output Format
### 用户故事地图
（故事之间的关系和依赖）

### 用户故事列表

#### Story 1: [标题]
- **描述**：作为 [角色]，我想要 [功能]，以便 [价值]
- **优先级**：P0
- **故事点**：{{story_points}}
- **验收标准**：
  - Given... When... Then...
  - Given... When... Then...

#### Story 2: ...

### 非功能性需求
（性能、安全、体验方面的要求）

## Variables
| 变量名 | 类型 | 必填 | 默认值 | 描述 |
|--------|------|------|--------|------|
| `feature` | string | 是 | - | 功能描述 |
| `target_users` | string | 是 | - | 目标用户 |
| `business_value` | string | 是 | - | 业务价值 |
| `story_points` | string | 否 | "待估算" | 故事点 |

## Example
### Input
```
feature: "用户个人资料页"
target_users: "社交 App 的普通用户"
business_value: "提升用户参与度和资料完整率"
```

### Output
（包含用户故事地图、详细故事列表和验收标准的完整方案）
