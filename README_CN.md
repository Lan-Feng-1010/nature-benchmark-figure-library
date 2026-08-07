# Nature Benchmark Figure Reference Library

**语言：[English](README.md) | 中文**

这是一个按论文组织的公开科研画图参考库，重点保存 Nature Portfolio 及相关高影响力期刊中的：

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
2. 先用“最核心亮点”判断文章的主要贡献，再按“最值得借鉴的图形”选择与你的画图问题最匹配的论文。
3. 默认打开 `paper-card_en.md` 英文深读；点击卡片顶部语言切换进入中文 `paper-card.md`。
4. 默认打开 `figure-analysis_en.md` 英文逐图分析；点击语言切换进入中文 `figure-analysis.md`。
5. 用 `source_article.pdf` 核对归档原文；若许可不允许公开分发，则打开 `source_article_access.md` 并沿正式 DOI 访问。
6. 保存的论文原图或忠实 PDF 页面仅用于设计参考；所有科学结论仍须回到所引用的原文核验。

## 论文目录

| 目录 | 论文／期刊 | 最核心亮点 | 最值得借鉴的图形 |
|---|---|---|---|
| [2026-07-24 — Capable language models can outgrow the benefits of collaboration](01_2026-07-24_Capable_language_models_can_outgrow_the_benefits_of_collaboration/paper-card_en.md) | Kim et al., *Nature Machine Intelligence*, 2026 | 多智能体协作并非普遍增益；其价值随底座模型能力和任务结构改变。 | 匹配小多图、箱线分布、相对变化标注 |
| [2026-04-27 — AgentClinic](02_2026-04-27_AgentClinic/paper-card_en.md) | Schmidgall et al., *npj Digital Medicine*, 2026 | 用交互式多模态临床环境评价智能体能否主动获取信息并选择合适工具。 | agent 环境 + 具体轨迹、医生/患者模型因素拆分 |
| [2026-04-16 — GPBench](03_2026-04-16_GPBench/paper-card_en.md) | Li et al., *Nature Communications*, 2026 | 用临床专家构建的能力框架统一六个一级域、十四个二级能力与三类互补测试。 | benchmark 工作流、全部评分域与权重、分域小多图、样本分布 |
| [2026-04-02 — Benchmarking agreement between large language models and published clinical trial conclusions across four artificial intelligence platforms](04_2026-04-02_Benchmarking_agreement_between_large_language_models_and_published_clinical_trial_conclusions_across_four_artificial_intelligence_platforms/paper-card_en.md) | Mao et al., *Scientific Reports*, 2026 | 将模型与已发表临床试验结论的一致性转化为透明的五域、双评分者和一致性评价。 | 评分者、0–5 域、汇总与一致性完整评分链 |
| [2026-03-30 — BioMedAgent](05_2026-03-30_BioMedAgent/paper-card_en.md) | Bu et al., *Nature Biomedical Engineering*, 2026 | planner–programmer–executor 多智能体执行工具感知的生物医学分析，并更新工具使用经验。 | 规划—编码—执行回路、逐任务状态、外部 benchmark |
| [2026-02-18 — Benchmarking large language model-based agent systems for clinical decision tasks](06_2026-02-18_Benchmarking_large_language_model-based_agent_systems_for_clinical_decision_tasks/paper-card_en.md) | Liu et al., *npj Digital Medicine*, 2026 | 通用临床智能体仅带来有限增益，却显著增加 token 和耗时，且仍可能传播影响诊断的幻觉。 | 准确率—token 权衡、工作流复杂度、幻觉传播 |
| [2026-01-12 — PHIA](07_2026-01-12_PHIA/paper-card_en.md) | Merrill et al., *Nature Communications*, 2026 | 迭代推理、Python 与网页检索的组合改善个体穿戴数据分析，并允许从代码错误中恢复。 | 自动客观指标与人工/专家评分分开呈现 |
| [2025-10-14 — AFMBench](08_2025-10-14_AFMBench/paper-card_en.md) | Mandal et al., *Nature Communications*, 2025 | 100 个可执行 AFM 任务揭示实验室智能体的知识—执行差距、提示敏感性和指令偏离风险。 | 工具/agent 需求构成、成本效率、任务复杂度分层 |
| [2025-05-01 — InferOperate Thorax](09_2025-05-01_InferOperate_Thorax/paper-card_en.md) | Chen et al., *Nature Communications*, 2025 | 用读者研究比较术前规划辅助前后，评价 AI 驱动三维重建对手术决策的作用。 | 多读者多病例设计、辅助前后临床规划结果 |

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
- `audit-report.json` 与 `audit-report_en.json`：中英文 Paper Card 各自的结构和来源定位审计。
- `source_bundle.json`：来源、图表/公式清单和审计所用溯源记录。
- `source_article.pdf`：仅在论文许可或其他合法依据允许公开分发时保存的原文 PDF。
- `source_article_access.md`：原文不能合法公开分发时的必需替代文件，记录 DOI、正式访问路径和版权边界。
- 新增文献继续沿用此结构。

## 版权与引用

论文与图像的版权和许可仍归原作者及出版方所有。归档 PDF 继续受各篇文章自己的许可约束，本公开仓库不会对其重新许可。每个分析文件都给出论文题名、期刊和 DOI。除非许可允许，不应把论文原图直接作为新论文插图重新发表；设计新图时应借鉴信息结构并重新制作原创图形。详见 [来源与使用声明](SOURCE_AND_USE_NOTICE_CN.md)。
