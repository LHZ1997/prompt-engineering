---
id: model-evaluation
category: ai-development
tags: [evaluation, ai-development, analysis]
author: prompt-engineering-hub
date: 2024-01-15
version: 1.0.0
model_compatibility: [gpt-4, claude-3, gemini-pro]
description: "设计模型评估方案，对比不同模型在特定任务上的表现"
---

# 模型评估方案

## Role
你是一位 AI 评估专家，擅长设计科学的模型对比实验和评估指标体系。

## Context
评估任务：{{task_description}}
候选模型：{{candidate_models}}
评估目标：{{evaluation_goal}}

## Task
请为以上任务设计一套完整的模型评估方案，包括：

1. **评估维度**：准确性、鲁棒性、效率、安全性、成本
2. **测试集设计**：构建或选择测试数据，覆盖典型和边界场景
3. **评估指标**：为每个维度选择合适的量化指标
4. **评估流程**：实验步骤、数据收集方式
5. **结果分析**：如何对比模型、如何解释结果
6. **报告模板**：评估报告的结构

## Constraints
- 测试集应包含 {{test_case_count}} 个测试用例
- 评估指标必须可量化、可复现
- 考虑模型间的公平对比（相同温度参数、相同上下文长度等）
- 标注每次评估的成本估算（如 token 消耗）

## Output Format
### 评估方案概述
（目标、范围、参与模型）

### 测试集设计
| 用例 ID | 类别 | 输入 | 期望输出 | 评估方式 |
|---------|------|------|----------|----------|

### 评估指标体系
| 维度 | 指标 | 权重 | 计算方法 |
|------|------|------|----------|

### 实验流程
1. ...
2. ...

### 评分卡模板
| 模型 | 维度 1 | 维度 2 | ... | 综合得分 |
|------|--------|--------|-----|----------|

### 实施建议
（工具推荐、注意事项）

## Variables
| 变量名 | 类型 | 必填 | 默认值 | 描述 |
|--------|------|------|--------|------|
| `task_description` | string | 是 | - | 评估任务描述 |
| `candidate_models` | array | 是 | - | 候选模型列表 |
| `evaluation_goal` | string | 否 | "选择最优模型" | 评估目标 |
| `test_case_count` | number | 否 | 50 | 测试用例数量 |

## Example
### Input
```
task_description: "中文文本摘要任务"
candidate_models: ["gpt-4", "claude-3", "qwen-max"]
evaluation_goal: "选择在中文摘要任务上综合表现最好的模型"
test_case_count: 30
```

### Output
（包含完整评估方案、测试集设计、指标体系和评分卡模板的方案）
