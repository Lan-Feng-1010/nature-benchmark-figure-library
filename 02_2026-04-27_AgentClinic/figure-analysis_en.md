# AgentClinic: figure analysis

**Language: English | [中文](figure-analysis.md)**

Paper: Schmidgall S, Ziaei R, Harris C, et al. *AgentClinic: a multimodal benchmark for tool-using clinical AI agents*. **npj Digital Medicine**. 2026;9:499. [DOI](https://doi.org/10.1038/s41746-026-02674-7)

![Figure 1 — interactive clinical-agent environment and example trajectory](figures/agentclinic_fig1.png)

- **Purpose:** the left panel shows the physician agent, patient, measurement tools, and moderator loop; the right panel instantiates it with a real dialogue, imaging request, diagnosis, and ground-truth comparison.
- **Reusable pattern:** place an abstract architecture beside one concrete trajectory so readers can understand both system rules and execution.
- **Boundary:** an example trajectory explains mechanism, not aggregate performance or the most common failure.

![Figure 2 — stratification by physician model, patient model, and data source](figures/agentclinic_fig2.png)

- **Purpose:** three bar-chart groups vary the physician LLM, patient LLM, or dataset while explicitly showing which side remains fixed.
- **Reusable pattern:** factor the agent from the simulated environment; for ImplantAgent, separately fix segmentation, candidate generation, and rule checking so upstream errors are not all assigned to the final planner.
- **Limitation:** rank-like bars can understate uncertainty in the environment model itself.

## Direct lesson for ImplantAgent

Use one case trajectory to show case input → agent action → tool/image request → termination → expert decision, followed by stratified experiments that separate segmentation, candidate generation, geometry checks, and final recommendation.
