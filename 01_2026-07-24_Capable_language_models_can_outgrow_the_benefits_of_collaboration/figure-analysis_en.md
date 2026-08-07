# Single-agent versus multi-agent scaling: figure analysis

**Language: English | [中文](figure-analysis.md)**

Paper: Kim Y, Gu K, Park C, et al. *Capable language models can outgrow the benefits of collaboration*. **Nature Machine Intelligence**. 2026;8:1157–1172. [DOI](https://doi.org/10.1038/s42256-026-01268-y)

![Figure 2 — matched comparisons of one single-agent and four multi-agent architectures across six benchmarks](figures/agent_scaling_fig2.png)

- **Purpose:** six small multiples preserve the same color order while boxplots show distributions, diamonds show means, and top labels show relative change.
- **Supported message:** multi-agent systems improve some tasks and worsen others; green/red annotations make heterogeneity, not universal gain, immediately visible.
- **Reusable pattern:** preserve layout and scale across benchmark or case strata and report distributions, means, and relative change together.
- **For ImplantAgent:** compare versions/modules across case strata and include absolute differences and confidence intervals; percentages alone can exaggerate change from a low baseline.
- **Boundary:** the figure evaluates LLM collaboration architectures and does not show that adding agents improves implant planning.
