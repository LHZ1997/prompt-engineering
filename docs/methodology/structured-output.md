# Structured Output（结构化输出）

## 核心思想

通过明确的格式规范和约束，引导模型生成可被程序解析、校验和下游处理的标准化输出（如 JSON、XML、Markdown 表格），而非自由文本。

## 适用场景

- API 接口需要结构化数据
- 数据库录入、表单填充
- 多字段信息抽取
- 需要下游自动处理的结果

## 基本模式

### JSON 模式

```
请严格按照以下 JSON Schema 输出结果，不要包含任何额外文本：

{
  "type": "object",
  "properties": {
    "summary": {"type": "string", "description": "内容摘要"},
    "keywords": {"type": "array", "items": {"type": "string"}, "description": "关键词列表"},
    "sentiment": {"type": "string", "enum": ["positive", "negative", "neutral"]}
  },
  "required": ["summary", "keywords", "sentiment"]
}
```

### Markdown 表格模式

```
请将结果以 Markdown 表格形式输出，包含以下列：
| 字段 | 类型 | 说明 |
|------|------|------|
```

## 进阶技巧

### 1. 使用系统提示固定格式

在系统消息中声明：

```
你是一个结构化数据提取助手。所有回复必须是合法的 JSON，不包含 markdown 代码块标记。
```

### 2. 提供输出示例

```
输出示例：
{"name": "张三", "age": 28, "skills": ["Python", "Go"]}
```

### 3. 字段约束说明

对每个字段说明：
- 数据类型
- 取值范围或枚举值
- 是否可为空
- 默认值

### 4. 处理模型不支持 JSON 模式的情况

对于不支持 `response_format: {type: "json_object"}` 的模型：

1. 在 Prompt 中强调 "仅输出 JSON，不要解释"
2. 使用正则表达式从回复中提取 JSON
3. 使用 Retry 机制：解析失败时自动重试并提示 "上次输出不是合法 JSON，请修正"

## 校验与容错

- 始终在后端对模型输出进行 Schema 校验
- 对必填字段缺失的情况设计降级策略
- 记录解析失败案例，用于优化 Prompt
