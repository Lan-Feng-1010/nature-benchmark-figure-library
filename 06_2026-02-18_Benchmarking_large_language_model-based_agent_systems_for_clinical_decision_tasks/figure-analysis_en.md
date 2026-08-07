# Clinical agent benchmark: figure analysis

**Language: English | [中文](figure-analysis.md)**

Paper: Liu Y, Carrero ZI, Jiang X, et al. *Benchmarking large language model-based agent systems for clinical decision tasks*. **npj Digital Medicine**. 2026;9:259. [DOI](https://doi.org/10.1038/s41746-026-02443-6)

![Figure 1 — systems, datasets, and evaluation endpoints](figures/clinical_agent_fig1.png)

- **Purpose:** one figure declares compared baseline/agent systems, three benchmark families, and four endpoint groups: accuracy, token/time, workflow graph, and hallucination.
- **Reusable pattern:** a benchmark overview should declare not only execution but also what final evidence will be reported.
- **Boundary:** the figure defines scope, not endpoint weights, sample size, or clinical effectiveness.

![Figure 2 — correct/null/incorrect composition and accuracy–token trade-off](figures/clinical_agent_fig2.png)

- **Purpose:** stacked bars separate outcome states; uncertainty-aware points show accuracy versus token cost; additional panels show performance profiles.
- **Reusable pattern:** show performance–cost trade-offs and keep Null distinct from Incorrect.
- **Limitation:** packing many chart types into one figure increases reading burden, and radar overlap remains difficult.

![Figure 4 — time, path length, graph complexity, and tool-state flow](figures/clinical_agent_fig4.png)

- **Purpose:** time, path length, mean node degree, and workflow graphs explain why agents are slow and how they act.
- **Reusable pattern:** move beyond final correctness to process. A state flow fits ImplantAgent's automatic output, manual review, rejection, and recovery paths.
- **Limitation:** dense graphs should retain only frequent or safety-critical transitions.

![Figure 5 — hallucination count, type, propagation, and diagnostic impact](figures/clinical_agent_fig5.png)

- **Purpose:** distinguish total hallucinations, blocked hallucinations, and diagnosis-affecting hallucinations, then show propagation to final diagnosis.
- **Reusable pattern:** separate error occurrence from error impact. For ImplantAgent, distinguish geometry anomalies, gate-captured anomalies, and anomalies exposed in recommendations.
- **Boundary:** the paper's hallucination definition is not a dental-geometric failure definition; only the reporting structure transfers.

## Direct lesson for ImplantAgent

Organize the main evidence in four layers: case/task composition → final correctness or acceptability → time/human burden → workflow state and failure propagation. Do not replace these with one composite score.
