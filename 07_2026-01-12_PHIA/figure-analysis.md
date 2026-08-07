# PHIA 可穿戴健康 agent：参考图分析

论文：Merrill MA, Paruchuri A, Rezaei N, et al. *Transforming wearable data into personal health insights using large language model agents*. **Nature Communications**. 2026;17:1143. [DOI](https://doi.org/10.1038/s41467-025-67922-y)

![Figure 1——客观题、开放题、合成用户与 agent 循环](figures/phia_fig1.png)

- **图的任务：** 区分用于自动评分的客观题和用于人工评分的开放题，说明合成用户来源、Think–Act–Observe 循环，并给出一条代码+搜索+回答轨迹。
- **可借鉴：** 同一 benchmark 可把自动评分与人工评分任务从源头分开，且展示一条可审计的 agent 过程。
- **边界：** 合成用户和示例轨迹不能替代真实临床验证。

![Figure 7——客观准确率与人工/专家评分结果](figures/phia_fig7.png)

- **图的任务：** a 用横条报告客观数值正确率；b、c 用点估计和区间分别报告 reasoning quality 与 code quality 的多个子维度。
- **可借鉴：** 自动指标和人工评价不要混成一个分数；专家评分应按 relevance、interpretation、logic、avoids harm 等子维度展示，并显示不确定性。
- **对 ImplantAgent：** 自动几何误差、安全距离与专家可接受性/可执行性应分别成图；专家评分建议用点区间图，不只画均值柱。
- **边界：** PHIA 的评分域针对个人健康洞见和代码质量，不是牙科手术方案 rubric。
