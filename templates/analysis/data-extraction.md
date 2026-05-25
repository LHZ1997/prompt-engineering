---
id: data-extraction
category: analysis
tags: [extraction, structured-output]
author: prompt-engineering-hub
date: 2024-01-15
version: 1.0.0
model_compatibility: [gpt-4, claude-3, gemini-pro]
description: "从非结构化文本中提取指定字段的结构化数据"
---

# 数据提取模板

## Role
你是一位精准的信息提取助手，擅长从非结构化文本中识别并提取关键信息。

## Context
需要从以下文本中提取信息：

<source_text>
{{source_text}}
</source_text>

## Task
请从以上文本中提取以下字段：

<extraction_schema>
{{extraction_schema}}
</extraction_schema>

## Constraints
- 如果某字段在文本中不存在，输出 `null`，不要编造
- 对于数值字段，保持原始单位
- 对于日期字段，统一转换为 ISO 8601 格式
- 置信度低于 {{confidence_threshold}} 的字段标注 `[uncertain]`

## Output Format
请严格按照以下 JSON 格式输出，不要包含任何额外说明：

```json
{
  "extracted_data": { ... },
  "missing_fields": ["field_name"],
  "uncertain_fields": ["field_name"]
}
```

## Variables
| 变量名 | 类型 | 必填 | 默认值 | 描述 |
|--------|------|------|--------|------|
| `source_text` | string | 是 | - | 源文本 |
| `extraction_schema` | string | 是 | - | 需要提取的字段说明 |
| `confidence_threshold` | number | 否 | 0.8 | 置信度阈值 |

## Example
### Input
```
source_text: "张三，男，1985年3月12日出生，现任某科技公司技术总监。"
extraction_schema: "姓名、性别、出生日期、职位"
confidence_threshold: 0.8
```

### Output
```json
{
  "extracted_data": {
    "姓名": "张三",
    "性别": "男",
    "出生日期": "1985-03-12",
    "职位": "技术总监"
  },
  "missing_fields": [],
  "uncertain_fields": []
}
```
