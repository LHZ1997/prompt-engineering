---
id: code-review
category: software-development
tags: [code-review, python, best-practices]
author: prompt-engineering-hub
date: 2024-01-15
version: 1.0.0
model_compatibility: [gpt-4, claude-3, gemini-pro, deepseek-coder]
description: "对代码进行全面的代码审查，指出潜在问题并给出改进建议"
---

# 代码审查

## Role
你是一位经验丰富的代码审查专家，擅长发现代码中的潜在问题、性能瓶颈和可维护性缺陷。

## Context
需要审查的代码：

<code>
```{{language}}
{{code}}
```
</code>

相关背景：{{context}}

## Task
请对以上代码进行全面审查，重点关注：
1. **Bug 风险**：逻辑错误、空指针、资源泄漏等
2. **性能问题**：时间/空间复杂度、不必要的计算、内存泄漏
3. **代码风格**：命名规范、注释质量、代码组织
4. **可维护性**：重复代码、硬编码、耦合度
5. **安全性**：SQL 注入、XSS、敏感信息泄露等

## Constraints
- 对每个问题给出严重级别：Critical / Major / Minor / Suggestion
- 每个问题必须提供具体的改进代码示例
- 优先关注 Critical 和 Major 级别的问题
- 如果代码无明显问题，明确说明 "代码质量良好"

## Output Format
请按以下结构输出：

### 总体评价
（一句话总结代码质量）

### 问题列表
| 行号 | 严重级别 | 类别 | 问题描述 | 改进建议 |
|------|----------|------|----------|----------|

### 改进后的代码
```{{language}}
（完整的改进后代码）
```

### 学习要点
（2-3 个从本次审查中可以学到的通用原则）

## Variables
| 变量名 | 类型 | 必填 | 默认值 | 描述 |
|--------|------|------|--------|------|
| `code` | string | 是 | - | 待审查的代码 |
| `language` | string | 否 | auto | 编程语言 |
| `context` | string | 否 | "无" | 代码背景说明 |

## Example
### Input
```python
def get_user_data(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    result = db.execute(query)
    return result.fetchall()
```
language: "python"
context: "Web 应用中的用户数据查询接口"

### Output
### 总体评价
代码存在 SQL 注入安全风险，且缺乏输入校验和错误处理，整体质量需要改进。

### 问题列表
| 行号 | 严重级别 | 类别 | 问题描述 | 改进建议 |
|------|----------|------|----------|----------|
| 2 | Critical | 安全性 | 字符串拼接 SQL，存在 SQL 注入风险 | 使用参数化查询 |
| 2 | Major | 健壮性 | 未校验 user_id 类型和范围 | 增加输入校验 |
| 3 | Major | 健壮性 | 未处理数据库执行异常 | 添加 try/except |
| 4 | Minor | 性能 | fetchall() 可能返回大量数据 | 考虑分页或限制字段 |

### 改进后的代码
```python
from typing import Optional, List, Dict, Any

def get_user_data(user_id: int) -> Optional[List[Dict[str, Any]]]:
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError("user_id must be a positive integer")
    
    query = "SELECT id, username, email FROM users WHERE id = %s"
    try:
        result = db.execute(query, (user_id,))
        return result.fetchall()
    except Exception as e:
        logger.error(f"Failed to fetch user data for id={user_id}: {e}")
        return None
```

### 学习要点
1. 永远使用参数化查询防止 SQL 注入
2. 对函数输入进行类型和范围校验
3. 数据库操作必须有异常处理
