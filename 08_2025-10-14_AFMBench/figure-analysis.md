# AFMBench：参考图分析

**语言：中文 | [English](figure-analysis_en.md)**

论文：Mandal I, Soni J, Zaki M, et al. *Evaluating large language model agents for automation of atomic force microscopy*. **Nature Communications**. 2025;16:9104. [DOI](https://doi.org/10.1038/s41467-025-64105-7)

![Figure 1——多 agent 架构、真实仪器和示例执行轨迹](figures/afmbench_fig1.png)

- **图的任务：** a 画 agent/工具路由；b 展示真实 AFM 装置；c 给出从自然语言任务到工具调用和结果的轨迹。
- **可借鉴：** 对物理或临床工具链，架构示意必须与真实运行环境和一条完整轨迹并列，证明不是纯文本问答。
- **边界：** 单条轨迹只说明可运行，不说明总体成功率。

![Figure 2——benchmark 任务构成和任务重叠](figures/afmbench_fig2.png)

- **图的任务：** 报告单/多工具、单/多 agent、基础/高级操作比例，列出各工具/agent 的题量，并用 Venn 图展示 Documentation、Analysis、Calculation 需求重叠。
- **可借鉴：** 在结果之前公开任务难度和工具需求构成；Venn 图适合 3 个明确集合。
- **局限：** Venn 面积未必严格按比例，类别多于 3 个时不再合适。

![Figure 3——模型结果、效率和任务分层](figures/afmbench_fig3.png)

- **图的任务：** 用任务重叠 Venn、工具调用/步数/token/成功率/延迟和按工具、难度、agent 数量的准确率分层展示结果。
- **可借鉴：** 性能、资源成本和复杂度分层在一张图中闭环；小黑点显示重复试验均值，优于只画单柱。

## 证据边界

AFMBench 是仪器自动化 benchmark，其成功定义、工具风险和任务复杂度不能直接转化为种植规划临床端点。
