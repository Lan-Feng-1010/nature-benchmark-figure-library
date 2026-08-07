# 单 agent 与多 agent scaling：参考图分析

**语言：中文 | [English](figure-analysis_en.md)**

论文：Kim Y, Gu K, Park C, et al. *Capable language models can outgrow the benefits of collaboration*. **Nature Machine Intelligence**. 2026;8:1157–1172. [DOI](https://doi.org/10.1038/s42256-026-01268-y)

![Figure 2——六个 benchmark 上单 agent 与四种多 agent 架构的匹配箱线图](figures/agent_scaling_fig2.png)

- **图的任务：** 六个小面板用相同颜色顺序比较 single-agent 与四种 multi-agent 架构；箱线图呈现分布，菱形呈现均值，顶部百分比直接标注相对变化。
- **可借鉴：** 多个 benchmark/病例组比较时，使用相同布局和尺度；同时给分布、均值和相对变化，不只给一个排名。
- **关键结论语法：** 多 agent 在某些任务改善、另一些任务下降；主图用绿色/红色注释让“异质性而非普遍提升”一眼可见。
- **对 ImplantAgent：** 比较版本或模块时可按病例子群画匹配小多图，并标注相对变化；必须同时报告绝对差异和 CI，避免百分比在低基线下夸大。
- **边界：** 该图比较 LLM 协作架构，不能证明种植规划中增加 agent 一定有效。
