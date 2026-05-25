# 博客大纲示例

## 使用的 Prompt

[prompts/writing/blog-outline.md](../../prompts/writing/blog-outline.md)

## 输入

### 变量

| 变量 | 值 |
|------|-----|
| `topic` | `如何在大模型时代做好 Prompt Engineering` |
| `target_audience` | `有一定技术背景的产品经理和开发者` |
| `article_type` | `技术博客` |
| `word_count` | `2500 字` |
| `tone` | `专业但易懂` |
| `special_elements` | `["代码示例", "对比表格"]` |

## 输出

### 文章标题建议

1. **《Prompt Engineering 完全指南：从入门到精通的实战方法论》**
2. **《大模型时代，如何写出让 AI "听懂" 的 Prompt？》**
3. **《Prompt Engineering 进阶：提升 LLM 输出质量的 8 个核心技巧》**

### 关键词布局

| 位置 | 关键词 | 密度建议 |
|------|--------|----------|
| 标题 | Prompt Engineering | 1 次 |
| 首段 | 大模型、Prompt 优化 | 各 1 次 |
| H2 标题 | Few-Shot、Chain-of-Thought、结构化输出 | 自然融入 |
| 正文 | LLM、提示词工程、AI 应用 | 各 2-3 次 |
| 结尾 | Prompt Engineering 最佳实践 | 1 次 |

### 文章大纲

#### 一、引言（300 字）

- **Hook**：用一个失败的 Prompt 案例引出话题——"为什么同样的模型，别人能得到完美答案，你却得到废话？"
- **背景**：大模型能力飞速提升，但输出质量高度依赖输入质量
- **核心观点**：Prompt Engineering 不是玄学，而是一门可系统学习和实践的技术

#### 二、什么是 Prompt Engineering（250 字）

- 定义：设计和优化输入指令以获得期望输出的工程方法
- 与传统编程的区别：声明式 vs 指令式
- 为什么它很重要：模型能力的"放大器"
- **对比表格**：普通 Prompt vs 优化后 Prompt 的效果差异

#### 三、核心方法论（1200 字）

##### 3.1 角色设定（Persona）
- 原理：激活模型在特定领域的知识模式
- **代码示例**：如何设计有效的 Role 描述
- 注意事项：避免过度虚构，关键约束需在 Task 中重复

##### 3.2 思维链（Chain-of-Thought）
- 原理：显式引导推理步骤
- 适用场景：数学、逻辑、多步骤决策
- **代码示例**：Zero-shot 和 Few-shot CoT 的对比

##### 3.3 少样本学习（Few-Shot）
- 原理：通过示例学习任务模式
- 示例设计原则：代表性、一致性、准确性
- **代码示例**：3 个高质量示例的结构

##### 3.4 结构化输出
- 原理：明确格式约束，减少自由度
- JSON Schema、Markdown 表格的应用
- **代码示例**：强制 JSON 输出的 Prompt 模板

#### 四、Prompt 优化实战技巧（500 字）

- 具体化原则：用量词替代模糊描述
- 分隔符使用：XML 标签、Markdown 代码块
- 约束前置：先告诉模型"不要做什么"
- 迭代优化：测试 → 分析 → 修正 → 回归
- **对比表格**：优化前后的 Prompt 对比

#### 五、常见陷阱与对策（200 字）

- 陷阱 1：指令冲突（同时要求详细和简洁）
- 陷阱 2：示例偏见（覆盖不全面）
- 陷阱 3：过度依赖 Few-Shot（占用上下文）

#### 六、总结与行动号召（50 字）

- 总结：Prompt Engineering 是人与 AI 协作的核心技能
- CTA：从本文的模板开始，迭代你自己的 Prompt 库

### 内容素材建议

| 章节 | 可引用素材 |
|------|-----------|
| 引言 | OpenAI GPT-4 官方文档关于 Prompt 设计的说明 |
| 3.2 | Google Research "Chain-of-Thought Prompting Elicits Reasoning in LLMs" |
| 3.3 | Microsoft 关于 Few-Shot Learning 的最佳实践指南 |
| 4 | 个人或团队的 Prompt 迭代前后对比案例 |
| 5 | 社区中常见的 Prompt 失败案例（如 "Do Anything Now" 攻击） |

### 特殊元素安排

- **代码示例**：共 4 处，分布在 3.1-3.4 节，展示实际可用的 Prompt 模板
- **对比表格**：2 处，分别在第 2 节和第 4 节，直观展示优化效果
