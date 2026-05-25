# Prompt 框架速查表

本文档汇总了常用的 Prompt Engineering 框架，帮助快速选择适合当前任务的提示词结构。

## 框架对比

| 框架 | 组成要素 | 适用场景 | 复杂度 |
|------|----------|----------|--------|
| APE | Action + Purpose + Expectation | 明确行动步骤和期望结果 | 低 |
| TAG | Task + Action + Goal | 快速清晰传达需求 | 低 |
| RTF | Role + Task + Format | 对话问答、智能助手 | 低 |
| CARE | Context + Action + Result + Example | 需要背景信息和示例 | 中 |
| SPAR | Scenario + Problem + Action + Result | 项目管理、问题解决 | 中 |
| SAGE | Situation + Action + Goal + Expectation | 需要全面描述情况 | 中 |
| TRACE | Task + Request + Action + Context + Example | 制定学习计划等 | 中 |
| ROSES | Role + Objective + Scenario + Expected Solution + Steps | 咨询服务、问题解决 | 高 |
| SCOPE | Scenario + Complications + Objective + Plan + Evaluation | 复杂问题解决、战略规划 | 高 |

## 框架详解

### APE 框架

- **Action（行动）**：具体描述用户希望模型执行的操作或任务
- **Purpose（目的）**：阐述执行该行动的目的或意图
- **Expectation（期望）**：明确期望的结果或输出

**适用场景**：营销活动规划、项目管理等需要明确行动步骤和期望结果的业务场景。

**示例**：
```
Action：为新产品撰写一份社交媒体推广文案
Purpose：提高品牌知名度并吸引潜在用户点击
Expectation：生成 3 条不同风格的文案，每条不超过 100 字，包含产品核心卖点
```

---

### TAG 框架

- **Task（任务）**：定义具体任务
- **Action（行动）**：描述需要做什么
- **Goal（目标）**：解释最终目标

**适用场景**：项目管理、任务分配等需要明确任务和目标的场景。

---

### RTF 框架

- **Role（角色）**：指定模型在对话中扮演的角色
- **Task（任务）**：定义具体要完成的任务或问题
- **Format（格式）**：明确用户希望获得的答案或输出的具体形式

**适用场景**：知识问答、智能助手等对话场景。

**示例**：
```
Role：你是一位资深 Python 开发工程师
Task：解释 Python 中的装饰器是什么
Format：用类比+代码示例的方式解释，最后给一个实际应用场景
```

---

### CARE 框架

- **Context（上下文）**：提供与任务相关的背景信息或情境
- **Action（行动）**：具体描述需要执行的操作或任务
- **Result（结果）**：明确期望得到的结果或输出
- **Example（示例）**：提供具体的示例或案例，帮助模型更好地理解任务

**适用场景**：制定健身计划、饮食计划等需要详细背景信息和明确结果的场景。

---

### SPAR 框架

- **Scenario（场景）**：描述背景或情况
- **Problem（问题）**：明确需要解决的问题或挑战
- **Action（行动）**：描述需要采取的行动或措施
- **Result（结果）**：期望得到的结果或输出

**适用场景**：项目管理、问题解决等需要明确场景和问题的场景。

---

### SAGE 框架

- **Situation（情况）**：描述背景或情况
- **Action（行动）**：描述需要采取的行动或措施
- **Goal（目标）**：明确行动的目标或意图
- **Expectation（期望）**：期望得到的结果或输出

**适用场景**：项目管理、问题解决等需要详细描述情况和行动的场景。

---

### TRACE 框架

- **Task（任务）**：定义具体要完成的任务或问题
- **Request（请求）**：明确向模型提出的具体请求或需求
- **Action（行动）**：描述模型需要采取的具体行动或步骤
- **Context（上下文）**：提供与任务相关的背景信息或情境
- **Example（示例）**：给出具体的示例或案例，帮助模型理解任务

**适用场景**：制定学习计划、复杂任务拆解等需要明确任务和上下文的场景。

---

### ROSES 框架

- **Role（角色）**：指定模型在任务中扮演的角色
- **Objective（目标）**：明确任务的目标或意图
- **Scenario（场景）**：提供与任务相关的背景信息或情境
- **Expected Solution（预期解决方案）**：描述期望得到的解决方案或结果
- **Steps（步骤）**：询问实现解决方案所需的具体步骤或操作

**适用场景**：咨询服务、问题解决等需要全面角色和场景描述的场景。

---

### SCOPE 框架

- **Scenario（场景）**：描述情况
- **Complications（并发症/挑战）**：指出在场景中可能遇到的困难、限制或挑战
- **Objective（目标）**：明确在给定场景下需要达成的目标或意图
- **Plan（计划）**：描述为实现目标而制定的具体行动计划或步骤
- **Evaluation（评估）**：说明如何评估计划的成功与否

**适用场景**：复杂问题解决、战略规划或项目管理等需要全面考虑各方面因素的场景。

## 选择建议

| 你的需求 | 推荐框架 |
|----------|----------|
| 快速问答，不需要太多背景 | RTF / TAG |
| 需要模型扮演特定角色 | RTF / ROSES |
| 需要给出示例帮助理解 | CARE / TRACE |
| 复杂问题需要拆解步骤 | TRACE / ROSES / SCOPE |
| 战略规划或项目管理 | SAGE / SPAR / SCOPE |
| 内容生成，需要明确输出 | APE / TAG |

## 组合使用

实际使用中，不必拘泥于单一框架。可以将多个框架的核心要素组合使用：

```
Role（来自 RTF）
Context（来自 CARE）
Task + Action（来自 TAG）
Example（来自 CARE）
Format（来自 RTF）
```

这种组合方式本质上与本项目中 Prompt 文件的标准结构（Role → Context → Task → Constraints → Output Format → Example）是一致的。
