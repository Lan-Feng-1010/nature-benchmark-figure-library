# AgentClinic：参考图分析

**语言：中文 | [English](figure-analysis_en.md)**

论文：Schmidgall S, Ziaei R, Harris C, et al. *AgentClinic: a multimodal benchmark for tool-using clinical AI agents*. **npj Digital Medicine**. 2026;9:499. [DOI](https://doi.org/10.1038/s41746-026-02674-7)

![Figure 1——交互式临床 agent 环境与示例轨迹](figures/agentclinic_fig1.png)

- **图的任务：** 左侧给出医生 agent、患者、测量工具和 moderator 的循环；右侧用一次真实对话展示如何问诊、请求影像、形成诊断并由 moderator 与 ground truth 比较。
- **可借鉴：** “抽象架构 + 一例具体轨迹”并排，是介绍 agent benchmark 最直观的方式。
- **边界：** 示例轨迹只说明机制，不代表整体性能或最常见失败。

![Figure 2——医生模型、患者模型和数据源对结果的分层比较](figures/agentclinic_fig2.png)

- **图的任务：** 三组柱图分别改变医生 LLM、患者 LLM和数据集，图底部明确哪一侧模型固定、哪一侧变化。
- **局限：** 柱形排名容易让读者忽略环境模型本身的不确定性。
