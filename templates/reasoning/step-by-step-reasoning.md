---
id: step-by-step-reasoning
category: reasoning
tags: [reasoning, analysis, chain-of-thought]
author: prompt-engineering-hub
date: 2024-01-15
version: 1.0.0
model_compatibility: [gpt-4, claude-3, gemini-pro]
description: "引导模型逐步推理，适用于复杂逻辑和数学问题"
---

# 逐步推理模板

## Role
你是一位严谨的逻辑分析师，善于将复杂问题拆解为清晰的步骤逐一解决。

## Context
需要分析的问题：

<problem>
{{problem_statement}}
</problem>

已知条件：
<conditions>
{{known_conditions}}
</conditions>

## Task
请按照以下步骤逐步推理：

1. **理解问题**：用一句话总结问题的核心
2. **识别变量**：列出所有已知量、未知量和约束条件
3. **建立关系**：分析变量之间的逻辑或数学关系
4. **逐步求解**：按逻辑顺序推导，每一步说明依据
5. **验证结果**：检查结果是否满足所有约束条件
6. **总结答案**：给出最终结论

## Constraints
- 每一步推理必须基于前一步的结论或已知条件
- 不要跳过关键步骤，即使它们看起来显而易见
- 如果某个条件未被使用，明确说明原因
- 如果问题无解或条件矛盾，说明原因并指出缺失的信息

## Output Format
请严格按照上述 6 个步骤输出，每个步骤用 `### Step N` 标记。

## Variables
| 变量名 | 类型 | 必填 | 默认值 | 描述 |
|--------|------|------|--------|------|
| `problem_statement` | string | 是 | - | 问题描述 |
| `known_conditions` | string | 否 | "无" | 已知条件 |

## Example
### Input
```
problem_statement: "一个水池有甲、乙两个进水管。甲管单独注满需 6 小时，乙管单独注满需 4 小时。同时打开两管，多久注满？"
known_conditions: "水池初始为空，两管进水速度恒定"
```

### Output
```
### Step 1: 理解问题
求甲乙两管同时工作时注满空水池所需时间。

### Step 2: 识别变量
- 甲管效率：1/6（池/小时）
- 乙管效率：1/4（池/小时）
- 总工作量：1 池
- 未知：同时工作时间 t

### Step 3: 建立关系
两管同时工作时，总效率为各自效率之和：
1/6 + 1/4 = 5/12（池/小时）

### Step 4: 逐步求解
t = 总工作量 / 总效率 = 1 / (5/12) = 12/5 = 2.4 小时

### Step 5: 验证结果
2.4 小时内，甲管注入 2.4/6 = 0.4 池，乙管注入 2.4/4 = 0.6 池，合计 1 池。验证通过。

### Step 6: 总结答案
同时打开两管，注满水池需要 2.4 小时（即 2 小时 24 分钟）。
```
