# Paper Card：Benchmarking agreement between large language models and published clinical trial conclusions

**语言：中文 | [English](paper-card_en.md)**

> Source coverage: Full paper; methodology figure retained as a PDF page view
>
> Extraction confidence: High for text; mixed for automatic figure inventory
>
> Locator mode: page-grounded
>
> Primary analytical lens: Clinical evaluation
>
> Secondary analytical lens: Resource / benchmark
>
> Context verification: Official Scientific Reports article checked on 2026-08-07
>
> Card completeness: Complete relative to the main paper

## 01 基本信息

- [Paper] Gordon Mao、William Snyder III、Anoop S. Chinthala 等；*Scientific Reports* 16, 15606 (2026)，2026-04-02 发布。[Paper: PDF p. 1]
- [Paper] DOI：[10.1038/s41598-026-45326-2](https://doi.org/10.1038/s41598-026-45326-2)；CC BY-NC-ND 4.0。[Paper: PDF p. 8]
- [Paper] 研究评估 ChatGPT、Gemini、Grok3 和 Claude 对 20 篇 landmark RCT 数值资料的解释。[Paper: PDF pp. 1–2]

## 02 一句话总结

[Analysis] 本研究用两名评分者和五个 0–5 域比较四个平台与已发表 RCT 结论的一致性，但其高分主要反映文本吻合与 rubric 表现，不能证明独立推理、临床安全或前瞻有效性。[Paper: PDF pp. 1–7]

## 03 研究问题

- [Paper] LLM 能否仅根据结构化数值与统计信息，形成与原论文结论一致的解释？[Paper: PDF pp. 1–2]
- [Paper] 不同平台在证据解释、统计理解、临床相关性、局限识别和实际适用性上有何差异？[Paper: PDF pp. 2–3]
- [Analysis] 关键审计问题是“一致性”是否被误写成“原创且正确的临床推理”。

## 04 研究背景与发展路线

1. [Paper] 作者选择 landmark RCT 以减少低质量研究设计带来的混杂。[Paper: PDF pp. 1–2]
2. [Paper] 向四个平台提供标准化数值输入并要求不引用原论文。[Paper: PDF p. 2]
3. [Paper] 两名研究者独立评分五个域，再汇总总分、一致性和可靠性。[Paper: PDF pp. 2–3]
4. [Analysis] 这是“评分链透明化”的有用案例，但不是无污染的推理 benchmark。

## 05 核心痛点

| 痛点 | 表现 | 证据边界 |
|---|---|---|
| 高分可能受训练污染 | landmark trials 很可能已进入训练语料 | [Paper: PDF pp. 1, 6] |
| 人工评分主观 | 仅两名且未对模型身份盲法 | [Paper: PDF p. 6] |
| 一致性不等于正确性 | rubric 以已发表结论为参照 | [Paper: PDF pp. 2, 6] |
| 试验选择偏向“最佳情形” | 清晰、阳性 landmark trials | [Paper: PDF p. 6] |

## 06 核心思想

- [Paper] 表层方法：同一输入模板、五域评分、双评分者与可靠性检查。[Paper: PDF pp. 2–3]
- [Analysis] 核心价值：把“谁评分、评什么、如何汇总、如何核对一致性”画成可审计流程。
- [Analysis] 可迁移原则：临床方案 benchmark 必须将评分者、盲法、锚点、仲裁和一致性统计写进图中。

## 07 方法总览

![Figure 2——从模型回答到五域评分和可靠性分析的完整评分链（PDF page view）](figures/Figure_2_methodology_page.png)

*Figure 2 把 standardized input、四个平台输出、两名独立评分者、五个 0–5 域、均值、25 分总分和 inter-rater reliability 画在同一流程中。[Paper: PDF p. 3, Figure 2]*

流程：20 篇 RCT 数值输入 → 四平台独立生成 → 两名评分者按五域评分 → 每域/总分汇总 → 与论文结论比较 → 检查评分者一致性。

## 08 核心模块拆解

| 模块 | 功能 | 输入/输出 | 风险 |
|---|---|---|---|
| Trial selection | 建立标准题库 | 20 篇 RCT→数值摘要 | landmark/阳性偏倚 |
| Structured prompt | 固定任务要求 | 数值资料→回答 | 无法保证模型不调用记忆 |
| Five-domain rubric | 拆分评价内容 | 回答→5×0–5 | 域定义仍需主观解释 |
| Two raters | 独立评分 | 两套分数→均值 | 未盲法、人数少 |
| Reliability | 检查评分稳定性 | 分数→Cronbach's α | α 不能证明临床有效性 |

[Paper: PDF pp. 2–3]

## 09 必要公式与符号

- [Paper] 每个域 0–5 分，五域总分最高 25 分。[Paper: PDF p. 3, Figure 2]
- [Paper] 两评分者可靠性以 Cronbach's α 报告，α=0.868。[Paper: PDF pp. 1, 4]
- [Analysis] α 衡量评分内部一致性，不是模型输出正确性的置信区间。

## 10 实验设计与证据链

| 端点 | 结果 | 支持结论 | 不支持的结论 |
|---|---|---|---|
| 与发表结论一致 | ChatGPT 100%、Gemini 84%、Grok3 72%、Claude 68% | 四平台在本题集上的吻合程度不同 | ChatGPT 具有无污染独立推理 |
| 主结果识别/建议 | 平台间有差异 | 可比较结构化研究解读 | 可直接支持患者治疗 |
| 五域评分 | ChatGPT/Gemini 在局限与混杂识别较好 | 域级结果比总分更可解释 | 已验证临床安全 |
| 评分可靠性 | α=0.868 | 两评分者分数较一致 | rubric 无偏或可普适迁移 |

[Paper: PDF pp. 1, 3–6]

## 11 结论的正确解释

- [Paper] 论文明确指出训练数据污染可能夸大 concordance。[Paper: PDF pp. 1, 6]
- [Paper] clinical relevance/practical application 高分代表文本连贯与对发表建议的一致，不代表前瞻安全或有效。[Paper: PDF p. 6]
- [Paper] 20 篇试验来自神经外科和心血管干预领域，且偏向清晰阳性结果。[Paper: PDF pp. 1–2, 6]
- [Analysis] 该研究最适合借鉴评分流程图，不适合借用其分数阈值。

## 12 作者明确承认的局限

| 局限 | 具体表现 | 作者建议 | 来源 |
|---|---|---|---|
| 训练污染无法排除 | 模型可能记得论文 | 用更模糊、阴性或新试验验证 | [Paper: PDF p. 6] |
| 评分者少且主观 | 两人、未盲模型身份 | 更大、盲法专家组 | [Paper: PDF p. 6] |
| benchmark 偏最佳情形 | landmark positive trials | 纳入含糊、阴性和方法学较弱研究 | [Paper: PDF p. 6] |
| rubric 惩罚不同于原作者的新结论 | 对发表结论作参照 | 设计容纳独立正确结论的评价 | [Paper: PDF p. 6] |

## 13 批判性分析

| [Analysis] 观察 | 为什么重要 | 如何检验 |
|---|---|---|
| concordance 不是 correctness | 原论文结论本身也可能有限 | 让盲法专家直接评证据—结论有效性 |
| 0–5 域是补偿性总分 | 安全性硬失败可能被其他高分抵消 | 设不可补偿的关键错误门控 |
| 平台是快速变化产品 | 结果依赖 2026 年特定版本 | 保存版本、日期、温度与原始输出 |

## 14 学到的知识

- Agent-derived knowledge candidate：完整评分图要包含评分者数量、独立性、等级锚点、汇总和可靠性。
- Agent-derived knowledge candidate：总分旁必须保留每个域和关键硬失败。
- Agent-derived knowledge candidate：研究结论一致性、专家可接受性和真实结局是不同端点。

## 15 与相关研究的连接

[Analysis] 本文可作为同类研究的证据组织和图形设计参考；其任务、数据、评价指标与结论不能直接外推到其他应用领域。

## 16 开放问题

[Analysis] 后续研究仍需在独立数据集上验证论文所述方法，并透明报告不确定性、失败案例与数据分布变化。
