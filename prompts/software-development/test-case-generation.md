---
id: test-case-generation
category: software-development
tags: [testing, code-generation, software-development]
author: prompt-engineering-hub
date: 2024-01-15
version: 1.0.0
model_compatibility: [gpt-4, claude-3, gemini-pro, deepseek-coder]
description: "根据代码或需求生成全面的测试用例，覆盖正常、边界和异常情况"
---

# 测试用例生成

## Role
你是一位测试专家，擅长设计全面的测试用例，覆盖功能、边界、异常和性能场景。

## Context
需要测试的代码/功能：

<code>
```{{language}}
{{code}}
```
</code>

需求说明：{{requirements}}

## Task
请为以上代码/功能生成全面的测试用例，包括：

1. **单元测试**：针对每个函数/方法
2. **边界测试**：空值、零值、最大值、最小值等
3. **异常测试**：非法输入、异常状态
4. **集成测试**：多个组件交互场景
5. **性能测试**：大数据量、高并发场景（如适用）

## Constraints
- 每个测试用例必须包含：用例 ID、描述、前置条件、输入、预期输出
- 覆盖正向路径和错误路径
- 测试名称应清晰描述测试意图
- 使用 {{test_framework}} 语法

## Output Format
### 测试策略
（总体测试思路和重点）

### 测试用例列表
| 用例 ID | 类型 | 描述 | 输入 | 预期输出 | 优先级 |
|---------|------|------|------|----------|--------|

### 测试代码
```{{language}}
（完整的测试代码）
```

### 覆盖率分析
（预期达到的覆盖率及未覆盖部分的说明）

## Variables
| 变量名 | 类型 | 必填 | 默认值 | 描述 |
|--------|------|------|--------|------|
| `code` | string | 是 | - | 待测试的代码 |
| `language` | string | 否 | auto | 编程语言 |
| `requirements` | string | 否 | "无" | 需求说明 |
| `test_framework` | string | 否 | "pytest" | 测试框架 |

## Example
### Input
```python
def divide(a, b):
    return a / b
```
language: "python"
test_framework: "pytest"

### Output
（包含完整测试用例列表和 pytest 代码的测试套件）
