# Nature Benchmark Figure Reference Library

这是一个按论文组织的科研画图参考库，重点保存 Nature Portfolio 及相关高影响力期刊中的：

- benchmark 总工作流图；
- 完整评分域、层级与权重图；
- 主结果与分项结果图；
- 成本、时间、工具使用和流程复杂度图；
- 失败传播、安全或人工评分图；
- 与图一一对应的中文深入分析。

本仓库用于个人科研阅读和图形设计参考。它不为 ImplantAgent 确定任何评分项、权重、阈值、临床终点或结论。

## 推荐阅读顺序

1. [GPBench 完整 Paper Card](01_GPBench_Nature_Communications_2026/paper-card.md)
2. [GPBench 六张主图逐图分析](01_GPBench_Nature_Communications_2026/figure-analysis.md)
3. [肺手术 AI-3D 规划研究 Paper Card](02_Lung_AI3D_Nature_Communications_2025/paper-card.md)
4. 按下面的“可借鉴图形”选择其他论文。

## 论文目录

| 目录 | 论文／期刊 | 保存内容 | 最值得借鉴的图形 |
|---|---|---|---|
| [01 GPBench](01_GPBench_Nature_Communications_2026/) | Li et al., *Nature Communications*, 2026 | 6 张官方主图、完整中文 Paper Card、逐图分析、来源包与审计 | benchmark 工作流、全部评分域与权重、分域小多图、样本分布 |
| [02 Lung AI-3D](02_Lung_AI3D_Nature_Communications_2025/) | Chen et al., *Nature Communications*, 2025 | 4 张主图页面、中文 Paper Card 与审计 | 多读者多病例设计、辅助前后临床规划结果 |
| [03 ClinicalAgentBench](03_ClinicalAgentBench_npj_Digital_Medicine_2026/) | Liu et al., *npj Digital Medicine*, 2026 | 4 张主图及分析 | 准确率—token 权衡、工作流复杂度、幻觉传播 |
| [04 AgentClinic](04_AgentClinic_npj_Digital_Medicine_2026/) | Schmidgall et al., *npj Digital Medicine*, 2026 | 2 张主图及分析 | agent 环境 + 具体轨迹、医生/患者模型因素拆分 |
| [05 BioMedAgent](05_BioMedAgent_Nature_Biomedical_Engineering_2026/) | Bu et al., *Nature Biomedical Engineering*, 2026 | 3 张主图及分析 | 规划—编码—执行回路、逐任务状态、外部 benchmark |
| [06 AFMBench](06_AFMBench_Nature_Communications_2025/) | Mandal et al., *Nature Communications*, 2025 | 3 张主图及分析 | 工具/agent 需求构成、成本效率、任务复杂度分层 |
| [07 Agent Scaling](07_AgentScaling_Nature_Machine_Intelligence_2026/) | Kim et al., *Nature Machine Intelligence*, 2026 | 1 张代表图及分析 | 匹配小多图、箱线分布、相对变化标注 |
| [08 PHIA](08_PHIA_Nature_Communications_2026/) | Merrill et al., *Nature Communications*, 2026 | 2 张主图及分析 | 自动客观指标与人工/专家评分分开呈现 |
| [09 Clinical Trial Scoring](09_ClinicalTrialScoring_Scientific_Reports_2026/) | Mao et al., *Scientific Reports*, 2026 | 1 张评分流程图及分析 | 评分者、0–5 域、汇总与一致性完整评分链 |

## 对手术方案 benchmark 的组合参考

最实用的组合不是照搬一篇论文，而是：

1. 用 GPBench Figure 1 语法画“输入—标注—系统—评分—结果”；
2. 用 GPBench Figure 2 语法画全部评分域，但把不可补偿的安全条件放在门控层；
3. 用 Lung AI-3D 的多读者多病例结构组织临床方案比较；
4. 用 ClinicalAgentBench 的状态图解释自动输出、人工复核和失败传播；
5. 用 PHIA 的点区间图把自动几何指标与专家可接受性分开；
6. 用 AFMBench/Agent Scaling 的小多图按病例复杂度、牙位或版本分层。

## 文件约定

- 每篇论文一个目录。
- `figures/`：论文原始主图或忠实 PDF 页面视图，不保存重绘冒充原图的图片。
- `paper-card.md`：完整中文深读卡片；仅在做过全文精读时提供。
- `figure-analysis.md`：逐图说明画了什么、支持什么、不支持什么、可借鉴点与边界。
- `audit-report.json`：Paper Card 的结构和来源定位审计。
- 新增文献继续沿用此结构。

## 版权与引用

图像版权和许可仍归原作者及出版方所有。每个分析文件都给出论文题名、期刊和 DOI。本仓库不主张对论文原图拥有版权，不应把这些原图直接作为新论文插图重新发表；设计新图时应借鉴信息结构并重新制作自己的原创图形。详见 [SOURCE_AND_USE_NOTICE.md](SOURCE_AND_USE_NOTICE.md)。
