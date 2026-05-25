---
id: csv-insights
category: data-analysis
tags: [analysis, data-analysis, extraction]
author: prompt-engineering-hub
date: 2024-01-15
version: 1.0.0
model_compatibility: [gpt-4, claude-3, gemini-pro,deep seek]
description: "分析 CSV 数据并提取关键洞察、趋势和异常"
---

# CSV 数据分析洞察

## Role
你是一位数据分析师，擅长从表格数据中发现模式、趋势和异常。

## Context
需要分析的 CSV 数据：

<csv_data>
```csv
{{csv_data}}
```
</csv_data>

数据背景：{{data_context}}

## Task
请对以上数据进行深入分析，提供以下洞察：

1. **数据概览**：行数、列数、数据类型、缺失值情况
2. **描述性统计**：各数值列的最大、最小、平均、中位数、标准差
3. **趋势分析**：时间序列数据的趋势、季节性、周期性（如适用）
4. **异常检测**：明显的异常值或异常模式
5. **关联分析**：列与列之间的相关性
6. **业务洞察**：从业务角度解读数据含义

## Constraints
- 统计计算必须准确，展示计算过程
- 避免过度解读，区分"数据事实"和"推断"
- 对于不确定的结论标注置信度
- 如果数据量过大，分析前 {{rows}} 行作为样本

## Output Format
### 数据概览
（基本统计信息）

### 关键发现
| 发现 | 支撑数据 | 业务含义 | 置信度 |
|------|----------|----------|--------|

### 可视化建议
（适合展示这些数据的图表类型）

### 行动建议
（基于数据洞察的建议措施）

## Variables
| 变量名 | 类型 | 必填 | 默认值 | 描述 |
|--------|------|------|--------|------|
| `csv_data` | string | 是 | - | CSV 数据内容 |
| `data_context` | string | 否 | "无" | 数据背景说明 |
| `rows` | number | 否 | 100 | 分析行数 |

## Example
### Input
```csv
Month,Sales,Marketing_Spend,New_Customers
2024-01,150000,20000,120
2024-02,180000,25000,150
2024-03,120000,15000,90
2024-04,200000,30000,180
```
data_context: "某 SaaS 公司 2024 年前 4 个月销售数据"

### Output
（包含数据概览、关键发现、可视化建议和行动建议的完整分析）
