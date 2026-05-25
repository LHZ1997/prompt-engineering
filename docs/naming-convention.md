# 命名与分类规范

## 文件命名规范

### Prompt 文件

- 使用 **kebab-case**（短横线连接的小写字母）
- 名称应准确描述用途
- 扩展名统一为 `.md`

**示例**：

| 用途 | 正确 | 错误 |
|------|------|------|
| 代码审查 | `code-review.md` | `CodeReview.md`, `code_review.md` |
| 生成测试用例 | `test-case-generation.md` | `testCaseGen.md` |
| 数据提取 | `data-extraction.md` | `dataExtraction.md` |

### 目录命名

- 同样使用 kebab-case
- 目录名与 `category` 字段保持一致

## ID 命名规范

- 每个 Prompt 文件必须有全局唯一的 `id`
- `id` 与文件名一致（不含扩展名）
- 若同一目录下存在变体，使用后缀区分：
  - `code-review-quick.md` → id: `code-review-quick`
  - `code-review-detailed.md` → id: `code-review-detailed`

## 分类体系

### 一级分类（category）

以下分类为预定义值，新增分类需经讨论：

| category | 说明 | 示例 |
|----------|------|------|
| `software-development` | 软件开发 | 代码审查、重构建议、测试生成 |
| `writing` | 内容创作 | 博客大纲、社媒文案、邮件撰写 |
| `data-analysis` | 数据分析 | CSV 洞察、SQL 生成、可视化建议 |
| `product-management` | 产品管理 | PRD 生成、用户故事、竞品分析 |
| `ai-development` | AI/LLM 开发 | Prompt 优化、模型评估、RAG 设计 |
| `business` | 商业应用 | 商业计划书、财务分析、合同审查 |
| `education` | 教育学习 | 课程设计、习题生成、学习规划 |

### 二级标签（tags）

标签用于描述 Prompt 的能力维度，一个 Prompt 可以有多个标签。

**技术能力标签**：

- `code-review` — 代码审查
- `refactoring` — 代码重构
- `testing` — 测试相关
- `documentation` — 文档生成
- `generation` — 内容生成
- `translation` — 翻译
- `summarization` — 摘要总结
- `extraction` — 信息抽取
- `classification` — 分类

**推理能力标签**：

- `reasoning` — 逻辑推理
- `analysis` — 分析
- `planning` — 规划
- `debugging` — 调试排错

**交互能力标签**：

- `roleplay` — 角色扮演
- `conversation` — 对话交互
- `interview` — 面试模拟
- `simulation` — 场景模拟

**领域标签**：

- `python`, `javascript`, `go`, `java` — 编程语言
- `frontend`, `backend`, `devops` — 技术栈
- `sql`, `nosql` — 数据存储

## 模型兼容性标注

`model_compatibility` 字段用于标注已测试的模型：

```yaml
model_compatibility: [gpt-4, claude-3-opus, gemini-pro, deepseek-chat]
```

常见模型标识符：

- `gpt-4`, `gpt-4o`, `gpt-3.5-turbo`
- `claude-3-opus`, `claude-3-sonnet`, `claude-3-haiku`
- `gemini-pro`, `gemini-ultra`
- `deepseek-chat`, `deepseek-coder`
- `qwen-max`, `qwen-plus`
- `llama-3`, `mistral-large`

## 版本号规范

采用语义化版本控制（SemVer）：

```
主版本号.次版本号.修订号
```

- **修订号（Z+1）**：文案微调、示例更新、错别字修复
- **次版本号（Y+1）**：新增变量、结构调整、新增示例
- **主版本号（X+1）**：不兼容的变更、核心逻辑重写

## 日期格式

统一使用 ISO 8601 格式：`YYYY-MM-DD`

**示例**：`2024-01-15`
