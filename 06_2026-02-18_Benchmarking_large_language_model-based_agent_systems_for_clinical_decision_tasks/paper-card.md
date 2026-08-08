# Paper Card：Benchmarking large language model-based agent systems for clinical decision tasks

**语言：中文 | [English](paper-card_en.md)**

> Source coverage: Full paper with five figures and two tables
>
> Extraction confidence: High
>
> Locator mode: page-grounded
>
> Primary analytical lens: Clinical evaluation
>
> Secondary analytical lens: Methods / benchmark
>
> Context verification: Official npj Digital Medicine article checked on 2026-08-07
>
> Card completeness: Complete relative to the main paper

## 术语表

| 术语 | 含义 | 边界 |
|---|---|---|
| OpenManus | 基于 Llama-4 的开源通用 agent 框架 | 作者还测试医学 prompt 和工具鼓励变体 |
| Manus | 专有 planner–executor–verifier agent system | 内部实现和模型细节不完全公开 |
| baseline LLM | 不运行 agent workflow 的基础模型 | 与 agent 系统的成本和流程不同 |
| blocked hallucination | 被后处理/安全模块移除的幻觉 | 与真正进入最终诊断的错误分开 |

## 01 基本信息

- [Paper] Yunsong Liu、Zunamys I. Carrero、Xiaofeng Jiang 等；*npj Digital Medicine* 9, 259 (2026)，2026-02-18 发布。[Paper: PDF p. 1]
- [Paper] DOI：[10.1038/s41746-026-02443-6](https://doi.org/10.1038/s41746-026-02443-6)；CC BY 4.0。[Paper: PDF p. 12]
- [Paper] 比较五个 baseline LLM、OpenManus 及其医学变体、以及专有 Manus；覆盖 AgentClinic、MedAgentsBench 与 HLE 文本/多模态任务。[Paper: PDF pp. 1–3]
- [Paper] 代码和非 MIMIC 数据公开；MIMIC-IV 仍需 PhysioNet 申请。[Paper: PDF p. 10]

## 02 一句话总结

[Analysis] 当前通用 agent systems 在多项临床决策 benchmark 上只带来有限准确率改善，却消耗超过 10 倍 token 和超过 2 倍延迟，并仍存在可传播到诊断的幻觉，因此必须同时画最终性能、资源和失败路径。[Paper: PDF pp. 1, 4–8, Figures 2–5]

## 03 研究问题

- [Paper] 通用 agent systems 是否比其 baseline LLM 在临床文本和多模态任务上更准确？[Paper: PDF pp. 1–3]
- [Paper] 医学 prompt、鼓励工具调用和专有架构能否改善结果？[Paper: PDF pp. 3–8]
- [Paper] 准确率增益是否值得 token、时间、路径复杂度和 hallucination 风险？[Paper: PDF pp. 4–8]

## 04 研究背景与发展路线

1. [Paper] 静态医学 QA 已达到较高分，但复杂诊断、对话和多模态任务仍弱。[Paper: PDF pp. 1–2]
2. [Paper] agent 系统通过计划、工具和多步执行被认为可能填补差距。[Paper: PDF p. 2]
3. [Paper] 本研究跨三个 benchmark 家族比较终点表现与过程成本。[Paper: PDF pp. 2–3]
4. [Analysis] 它把“agent 是否更准”改写为“净临床/工程价值是否为正”。

## 05 核心痛点

| 痛点 | 表现 | 证据 |
|---|---|---|
| 增益小且不稳定 | 多数任务仅小幅变化 | [Paper: PDF pp. 3–6, Figures 2–3] |
| 成本陡增 | token >10×、latency >2× | [Paper: PDF pp. 1, 7, Figure 4] |
| 无输出与错误混在准确率中 | null、incorrect、correct 有不同机制 | [Paper: PDF p. 4, Figure 2] |
| 幻觉可被阻断也可传播 | 89.9% 被过滤，但仍有影响诊断者 | [Paper: PDF pp. 1, 8, Figure 5] |

## 06 核心思想

- [Paper] 表层方法：同一批任务上比较 baseline 与 agent 变体，并记录 accuracy、token、time、workflow 和 hallucination。[Paper: PDF p. 3, Figure 1]
- [Paper] 核心洞见：过程复杂度是 agent 评价的一等端点，不是附属工程指标。[Paper: PDF pp. 7–8]
- [Analysis] 可迁移原则：错误发生、被门控捕获、进入最终输出三种状态必须分开。

## 07 方法总览

![Figure 1——系统、数据集和评价端点总览（figure crop）](figures/clinical_agent_fig1.png)

*Figure 1 同时列出被比较系统、三类 benchmark 和四组端点，使读者在看结果前知道研究范围。[Paper: PDF p. 3, Figure 1]*

流程：baseline/agent 配置 → AgentClinic、MedAgentsBench、HLE → text/multimodal 任务 → accuracy/null/error → token/time/workflow → hallucination 发生、阻断和诊断影响。

## 08 核心模块拆解

| 模块 | 功能 | 输入/输出 | 边界 |
|---|---|---|---|
| Baseline LLM | 提供不含 agent loop 的参照 | 题目→答案 | 与 agent 的总调用预算不匹配 |
| OpenManus | 通用计划和工具执行 | 任务→工作流→答案 | 基于 Llama-4 |
| OM_MedAssist | 加医学 assistant prompt | 同上 | prompt 变化与架构效应混合 |
| OM_MedAssist_Tool | 进一步鼓励工具调用 | 同上 | 更多工具不保证更准 |
| Manus | 专有 planner–executor–verifier | 任务→专有 workflow | 复现边界较强 |
| Hallucination filter | 后处理不支持的内容 | 原输出→阻断/保留 | 仍可能漏过有诊断影响的错误 |

[Paper: PDF pp. 2–4, 8]

## 09 必要公式与符号

- [Paper] accuracy 用 Wilson 95% CI；模型总体差异用 Cochran's Q，成对比较用 Holm 校正 McNemar test。[Paper: PDF p. 10]
- [Paper] Table 1 与 Table 2 分别汇总文本和多模态任务的性能与效率。[Paper: PDF pp. 5–6, Tables 1–2]
- 论文核心结论不依赖新的方法学公式。

## 10 实验设计与证据链

| 实验 | 结果 | 支持结论 | 不支持的更强结论 |
|---|---|---|---|
| AgentClinic | agent 系统最高 60.3% MedQA、28.0% MIMIC | 部分配置有有限增益 | 已达到临床诊断水平 |
| MedAgentsBench/HLE text | 最高 30.3% 与 8.6% | 困难任务仍低 | 工具解决知识/推理瓶颈 |
| 多模态 | HLE 15.5%，AgentClinic NEJM 29.2% | 多模态表现仍有限 | agent 已会稳定整合影像 |
| 成本 | >10× token、>2× latency | 增益伴随显著资源代价 | 成本对部署可忽略 |
| hallucination | 89.9% 被 safeguard 过滤，但仍有诊断影响 | 过滤器降低暴露但不消除风险 | 89.9% 等于临床安全率 |

[Paper: PDF pp. 1, 4–8, Figures 2–5]

![Figure 2——正确/无输出/错误及准确率—token 权衡（figure crop）](figures/clinical_agent_fig2.png)

*Figure 2 把 Null 与 Incorrect 分开，并把准确率放到 token 成本坐标中。[Paper: PDF p. 4, Figure 2]*

![Figure 3——HLE 与多模态 benchmark 结果（PDF page view）](figures/page-006.png)

*Figure 3 显示文本和多模态困难任务上 agent 与 baseline 的差距仍小，且绝对准确率偏低。[Paper: PDF p. 6, Figure 3]*

![Figure 4——时间、路径复杂度与工具状态流（figure crop）](figures/clinical_agent_fig4.png)

*Figure 4 从时间、路径长度、节点度和状态流解释 agent 为何更慢、如何调用工具。[Paper: PDF p. 7, Figure 4]*

![Figure 5——幻觉数量、阻断和诊断影响（figure crop）](figures/clinical_agent_fig5.png)

*Figure 5 将错误发生、被阻断和真正影响诊断分开，是安全报告最可复用的结构。[Paper: PDF p. 8, Figure 5]*

## 11 结论的正确解释

- [Paper] benchmark 包括模拟对话、知识问答和困难考试，并非真实临床部署。[Paper: PDF pp. 2–3]
- [Paper] OpenManus 与 Manus 的基础模型、架构和可观察细节不同，不能做纯架构因果归因。[Paper: PDF pp. 2–3]
- [Paper] 过滤掉 hallucination 不等于原始 agent 可靠；同时还应看漏过并影响诊断者。[Paper: PDF p. 8]
- [Analysis] 论文支持“目前净收益有限”，不证明所有未来临床 agent 都不会有效。

## 12 作者明确承认的局限

| 局限 | 表现 | 来源 |
|---|---|---|
| benchmark 与真实临床有差距 | 多数为公开/模拟任务 | [Paper: PDF p. 9] |
| 专有 Manus 可复现性有限 | 内部模型/流程未完全公开 | [Paper: PDF pp. 2, 9] |
| agent 系统快速变化 | 特定版本结果会过时 | [Paper: PDF p. 9] |
| 成本测量依赖平台和实现 | token/延迟不完全可横向泛化 | [Paper: PDF pp. 7, 9] |

## 13 批判性分析

| [Analysis] 观察 | 风险 | 检验 |
|---|---|---|
| baseline 与 agent 使用不同模型/提示/工具 | 效应来源混合 | 同 backbone、同 prompt、同工具、同预算结构消融 |
| hallucination 定义依赖人工/后处理规则 | 漏检与类别漂移 | 双专家盲审和预注册 taxonomy |
| accuracy 成本曲线仍缺临床 utility | 小增益可能不值人工负担 | 将人工监督成本、危害严重度和时间纳入净效益 |

## 14 学到的知识

- Agent-derived knowledge candidate：结果图应包含正确、错误和无输出构成。
- Agent-derived knowledge candidate：把性能—成本散点与最终排名并列。
- Agent-derived knowledge candidate：用状态流表达错误在哪个安全门被捕获。

## 15 与相关研究的连接

[Analysis] 本文可作为同类研究的证据组织和图形设计参考；其任务、数据、评价指标与结论不能直接外推到其他应用领域。

## 16 开放问题

[Analysis] 后续研究仍需在独立数据集上验证论文所述方法，并透明报告不确定性、失败案例与数据分布变化。
