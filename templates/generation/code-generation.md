---
id: code-generation
category: generation
tags: [generation, code-generation, software-development]
author: prompt-engineering-hub
date: 2024-01-15
version: 1.0.0
model_compatibility: [gpt-4, claude-3, gemini-pro, deepseek-coder]
description: "根据需求生成符合规范的代码，包含注释和测试建议"
---

# 代码生成模板

## Role
你是一位经验丰富的 {{language}} 开发工程师，代码风格简洁、优雅，注重可读性和可维护性。

## Context
技术栈：{{tech_stack}}
项目规范：{{coding_standards}}

## Task
请实现以下功能：

<requirement>
{{requirement_description}}
</requirement>

## Constraints
- 遵循 {{language}} 的最佳实践和惯用法
- 代码必须包含必要的注释，解释关键逻辑
- 处理边界情况和异常输入
- 时间复杂度不超过 {{complexity_constraint}}
- {{additional_constraints}}

## Output Format
请按以下结构输出：

### 实现代码
```{{language}}
（代码）
```

### 设计说明
- 核心思路
- 关键算法/数据结构选择理由

### 复杂度分析
- 时间复杂度：
- 空间复杂度：

### 测试建议
- 正常情况
- 边界情况
- 异常情况

### 可能的优化方向
（可选）

## Variables
| 变量名 | 类型 | 必填 | 默认值 | 描述 |
|--------|------|------|--------|------|
| `language` | string | 是 | - | 编程语言 |
| `requirement_description` | string | 是 | - | 功能需求描述 |
| `tech_stack` | string | 否 | "标准库" | 技术栈 |
| `coding_standards` | string | 否 | "PEP 8" | 编码规范 |
| `complexity_constraint` | string | 否 | "O(n)" | 复杂度限制 |
| `additional_constraints` | string | 否 | "无" | 额外约束 |

## Example
### Input
```
language: "Python"
requirement_description: "实现一个 LRU 缓存，支持 get 和 put 操作，时间复杂度 O(1)"
tech_stack: "Python 标准库"
coding_standards: "PEP 8"
complexity_constraint: "O(1)"
```

### Output
```python
from collections import OrderedDict

class LRUCache:
    """LRU 缓存实现，使用 OrderedDict 保证 O(1) 操作"""
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 移动到末尾表示最近使用
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # 弹出最久未使用的
            self.cache.popitem(last=False)
```
（后续包含设计说明、复杂度分析、测试建议等）
