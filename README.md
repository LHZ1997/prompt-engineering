# Prompt Engineering Hub

系统化的 Prompt Engineering 知识库与模板库，用于整理、沉淀和复用高质量 Prompt。

## 目录结构

```
.
├── docs/                    # 方法论与文档
│   ├── methodology/         # Prompt Engineering 核心方法论
│   ├── best-practices.md    # 最佳实践
│   ├── naming-convention.md # 命名与分类规范
│   └── evaluation-guide.md  # 效果评估指南
├── templates/               # 可复用模板框架（半抽象）
│   ├── analysis/            # 分析类模板
│   ├── generation/          # 生成类模板
│   ├── reasoning/           # 推理类模板
│   └── conversation/        # 对话类模板
├── prompts/                 # 具体 Prompt 实例（按领域分类）
│   ├── software-development/# 软件开发
│   ├── writing/             # 内容创作
│   ├── data-analysis/       # 数据分析
│   ├── product-management/  # 产品管理
│   └── ai-development/      # AI/LLM 开发
├── examples/                # 实际使用案例（含输入/输出示例）
├── scripts/                 # 辅助工具
│   ├── validate-prompts.py  # Prompt 格式校验
│   ├── render-template.py   # 模板渲染
│   └── generate-metadata.py # 生成全局索引
└── metadata.json            # 全局索引文件
```

## 快速开始

### 直接使用 Prompt

1. 浏览 `prompts/` 目录，按领域找到目标场景
2. 打开对应的 `.md` 文件，复制 Prompt 内容
3. 根据文件中的 `Variables` 部分替换变量后使用

### 使用模板框架

```bash
# 渲染模板并填充变量
python scripts/render-template.py templates/analysis/root-cause-analysis.md --vars vars.json
```

### 贡献新 Prompt

参考 [CONTRIBUTING.md](CONTRIBUTING.md) 了解文件格式规范和贡献流程。

## 文件格式规范

每个 Prompt 文件采用统一结构：

- **YAML Frontmatter**：包含 `id`, `category`, `tags`, `version` 等元数据
- **Role**：定义模型扮演的角色
- **Context**：提供背景上下文
- **Task**：具体任务指令
- **Constraints**：约束条件
- **Output Format**：期望输出格式
- **Variables**：可配置变量说明
- **Example**：输入/输出示例

详细规范见 [docs/naming-convention.md](docs/naming-convention.md)。

## 工具脚本

| 脚本 | 用途 |
|------|------|
| `scripts/validate-prompts.py` | 校验所有 Prompt 文件的元数据完整性和合规性 |
| `scripts/render-template.py` | 将模板中的变量占位符替换为实际值 |
| `scripts/generate-metadata.py` | 扫描全库生成 `metadata.json` 索引 |

## 分类体系

### 一级分类（领域）

- `software-development` — 软件开发
- `writing` — 内容创作
- `data-analysis` — 数据分析
- `product-management` — 产品管理
- `ai-development` — AI/LLM 开发

### 二级标签（能力）

- `code-review`, `generation`, `reasoning`, `analysis`, `translation`, `summarization`

## License

MIT
