# Nature Benchmark Figure Reference Library

**语言：[English](README.md) | 中文**

这是一个按论文组织的科研画图参考库，重点保存 Nature Portfolio 及相关高影响力期刊中的：

- benchmark 总工作流图；
- 完整评分域、层级与权重图；
- 主结果与分项结果图；
- 成本、时间、工具使用和流程复杂度图；
- 失败传播、安全或人工评分图；
- 与图一一对应的中文深入分析。

本仓库用于个人科研阅读和图形设计参考。它不为 ImplantAgent 确定任何评分项、权重、阈值、临床终点或结论。

根目录论文文件夹使用两位导航序号（`01` = 最新），使 GitHub 原生文件夹列表也按最新优先显示；下方论文目录标题不显示这个仅用于排序的前缀。

## 如何使用本库

1. 从下方论文目录开始；目录按出版社正式发表日期倒序排列，最新论文在最前。
2. 根据你要解决的画图问题，使用“最值得借鉴的图形”一栏选择论文。
3. 若论文目录中有 `paper-card.md`，用它查看完整、来源可追溯的深读、关键证据和结论边界。
4. 用 `figure-analysis.md` 查看每张图的工作流、benchmark 或评分设计、结果表达及可迁移的视觉语法分析。
5. 保存的论文原图或忠实 PDF 页面仅用于设计参考；所有科学结论仍须回到所引用的原文核验。

## 论文目录

| 目录 | 论文／期刊 | 保存内容 | 最值得借鉴的图形 |
|---|---|---|---|
| [2026-07-24 — Capable language models can outgrow the benefits of collaboration](01_2026-07-24_Capable_language_models_can_outgrow_the_benefits_of_collaboration/) | Kim et al., *Nature Machine Intelligence*, 2026 | 1 张代表图及分析 | 匹配小多图、箱线分布、相对变化标注 |
| [2026-04-27 — AgentClinic](02_2026-04-27_AgentClinic/) | Schmidgall et al., *npj Digital Medicine*, 2026 | 2 张主图及分析 | agent 环境 + 具体轨迹、医生/患者模型因素拆分 |
| [2026-04-16 — GPBench](03_2026-04-16_GPBench/) | Li et al., *Nature Communications*, 2026 | 6 张官方主图、完整中文 Paper Card、逐图分析、来源包与审计 | benchmark 工作流、全部评分域与权重、分域小多图、样本分布 |
| [2026-04-02 — Benchmarking agreement between large language models and published clinical trial conclusions across four artificial intelligence platforms](04_2026-04-02_Benchmarking_agreement_between_large_language_models_and_published_clinical_trial_conclusions_across_four_artificial_intelligence_platforms/) | Mao et al., *Scientific Reports*, 2026 | 1 张评分流程图及分析 | 评分者、0–5 域、汇总与一致性完整评分链 |
| [2026-03-30 — BioMedAgent](05_2026-03-30_BioMedAgent/) | Bu et al., *Nature Biomedical Engineering*, 2026 | 3 张主图及分析 | 规划—编码—执行回路、逐任务状态、外部 benchmark |
| [2026-02-18 — Benchmarking large language model-based agent systems for clinical decision tasks](06_2026-02-18_Benchmarking_large_language_model-based_agent_systems_for_clinical_decision_tasks/) | Liu et al., *npj Digital Medicine*, 2026 | 4 张主图及分析 | 准确率—token 权衡、工作流复杂度、幻觉传播 |
| [2026-01-12 — PHIA](07_2026-01-12_PHIA/) | Merrill et al., *Nature Communications*, 2026 | 2 张主图及分析 | 自动客观指标与人工/专家评分分开呈现 |
| [2025-10-14 — AFMBench](08_2025-10-14_AFMBench/) | Mandal et al., *Nature Communications*, 2025 | 3 张主图及分析 | 工具/agent 需求构成、成本效率、任务复杂度分层 |
| [2025-05-01 — InferOperate Thorax](09_2025-05-01_InferOperate_Thorax/) | Chen et al., *Nature Communications*, 2025 | 4 张主图页面、中英文 Paper Card、中英文逐图分析、来源包与各自审计 | 多读者多病例设计、辅助前后临床规划结果 |

## 对手术方案 benchmark 的组合参考

最实用的组合不是照搬一篇论文，而是：

1. 用 GPBench Figure 1 语法画“输入—标注—系统—评分—结果”；
2. 用 GPBench Figure 2 语法画全部评分域，但把不可补偿的安全条件放在门控层；
3. 用 InferOperate Thorax 研究的多读者多病例结构组织临床方案比较；
4. 用 Liu 等人临床智能体评测研究的状态图解释自动输出、人工复核和失败传播；
5. 用 PHIA 的点区间图把自动几何指标与专家可接受性分开；
6. 用 AFMBench 和 Kim 等人多智能体协作研究的小多图按病例复杂度、牙位或版本分层。

## 文件约定

- 每篇论文一个目录。
- `README.md` 是默认英文首页；点击语言切换后进入中文版本 `README_CN.md`。
- 目录标题统一为 `YYYY-MM-DD_正式模型或 benchmark 名`；如果论文没有明确命名的单一模型、系统或 benchmark，则使用 `YYYY-MM-DD_原文章名`。日期采用出版社页面的正式 `Published` 日期，不使用接收日期、卷年或入库日期。
- `figures/`：论文原始主图或忠实 PDF 页面视图，不保存重绘冒充原图的图片。
- `paper-card.md`：完整中文深读卡片；仅在做过全文精读时提供。
- `paper-card_en.md`：对应英文深读卡片；仅在已有来源一致性审计时提供。
- `figure-analysis.md`：逐图说明画了什么、支持什么、不支持什么、可借鉴点与边界。
- `figure-analysis_en.md`：对应英文逐图分析。
- `audit-report.json`：Paper Card 的结构和来源定位审计。
- 新增文献继续沿用此结构。

## 版权与引用

图像版权和许可仍归原作者及出版方所有。每个分析文件都给出论文题名、期刊和 DOI。本仓库不主张对论文原图拥有版权，不应把这些原图直接作为新论文插图重新发表；设计新图时应借鉴信息结构并重新制作自己的原创图形。详见 [SOURCE_AND_USE_NOTICE.md](SOURCE_AND_USE_NOTICE.md)。
