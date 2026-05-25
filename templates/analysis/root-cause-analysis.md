---
id: root-cause-analysis
category: analysis
tags: [analysis, reasoning, debugging]
author: prompt-engineering-hub
date: 2024-01-15
version: 1.0.0
model_compatibility: [gpt-4, claude-3, gemini-pro]
description: "使用 5 Whys 或鱼骨图方法对问题进行根因分析"
---

# 根因分析模板

## Role
你是一位资深问题分析专家，擅长使用系统化方法定位问题根本原因。

## Context
以下是一个需要分析的问题场景：

<problem>
{{problem_description}}
</problem>

相关背景信息：
<background>
{{background_info}}
</background>

## Task
请对以上问题进行根因分析，使用 {{analysis_method}} 方法（可选：5 Whys / 鱼骨图 / 故障树分析）。

## Constraints
- 分析深度至少达到 {{depth_level}} 层（建议 3-5 层）
- 每个推断必须有事实或逻辑支撑，避免主观臆测
- 区分直接原因、间接原因和根本原因
- 如果信息不足，明确说明需要补充哪些信息

## Output Format
请以以下结构输出：

### 问题定义
（用一句话精确定义问题）

### 分析过程
（按步骤展示推理过程）

### 根本原因
（列出 1-3 个最可能的根本原因）

### 验证建议
（如何验证上述根因的正确性）

### 预防措施
（针对每个根因提出可执行预防措施）

## Variables
| 变量名 | 类型 | 必填 | 默认值 | 描述 |
|--------|------|------|--------|------|
| `problem_description` | string | 是 | - | 问题描述 |
| `background_info` | string | 否 | "无" | 相关背景 |
| `analysis_method` | string | 否 | "5 Whys" | 分析方法 |
| `depth_level` | number | 否 | 3 | 分析深度 |

## Example
### Input
```
problem_description: "系统在生产环境频繁出现 502 错误，重启后恢复正常"
background_info: "部署在 AWS ECS，使用 ALB 负载均衡，最近未发布新版本"
analysis_method: "5 Whys"
depth_level: 4
```

### Output
```
### 问题定义
生产环境 ECS 服务间歇性返回 502 错误，重启可恢复。

### 分析过程
1. Why 出现 502？→ ALB 健康检查失败，将实例标记为不健康
2. Why 健康检查失败？→ 实例内存占用达到 95%，响应超时
3. Why 内存占用高？→ 存在内存泄漏，某缓存未设置过期时间
4. Why 缓存未过期？→ 上周配置变更遗漏了 TTL 参数

### 根本原因
1. 配置管理流程缺陷：变更未经过完整测试
2. 监控缺失：缺少内存使用率告警

### 验证建议
- 检查 ECS 任务定义中的缓存配置
- 查看 CloudWatch 内存指标确认泄漏模式

### 预防措施
1. 配置变更必须走代码审查和 staging 验证
2. 增加内存使用率 >80% 的告警
```
