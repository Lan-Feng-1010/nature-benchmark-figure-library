# Nature Benchmark Figure Reference Library

**Language: [中文](README.md) | English**

This research-figure reference library is organized by paper. It focuses on examples from Nature Portfolio and related high-impact journals that show:

- end-to-end benchmark workflows;
- complete scoring domains, hierarchies and weights;
- primary and component-level result figures;
- cost, time, tool-use and workflow-complexity figures;
- failure propagation, safety and human-rating figures;
- source-aligned deep analysis of each figure.

The repository is intended for personal research reading and figure-design reference. It does not define any ImplantAgent scoring item, weight, threshold, clinical endpoint or conclusion.

## Recommended reading order

1. [GPBench complete Paper Card — Chinese](01_GPBench_Nature_Communications_2026/paper-card.md)
2. [GPBench analysis of all six main figures — Chinese](01_GPBench_Nature_Communications_2026/figure-analysis.md)
3. Lung-surgery AI-3D planning Paper Card: [English](02_Lung_AI3D_Nature_Communications_2025/paper-card_en.md) | [中文](02_Lung_AI3D_Nature_Communications_2025/paper-card.md)
4. Lung-surgery AI-3D analysis of all four main figures: [English](02_Lung_AI3D_Nature_Communications_2025/figure-analysis_en.md) | [中文](02_Lung_AI3D_Nature_Communications_2025/figure-analysis.md)
5. Select other papers from the “most reusable figure design” column below.

## Paper directory

| Directory | Paper / journal | Saved content | Most reusable figure design |
|---|---|---|---|
| [01 GPBench](01_GPBench_Nature_Communications_2026/) | Li et al., *Nature Communications*, 2026 | Six official main figures, complete Chinese Paper Card, figure-by-figure analysis, source bundle and audit | Benchmark workflow, full scoring domains and weights, domain-level small multiples, sample distribution |
| [02 Lung AI-3D](02_Lung_AI3D_Nature_Communications_2025/) | Chen et al., *Nature Communications*, 2025 | Four main-figure page views, Chinese and English Paper Cards, bilingual figure analysis, source bundle and separate audits | Multi-reader multi-case design and clinical-planning results before versus after assistance |
| [03 ClinicalAgentBench](03_ClinicalAgentBench_npj_Digital_Medicine_2026/) | Liu et al., *npj Digital Medicine*, 2026 | Four main figures and Chinese analysis | Accuracy–token trade-off, workflow complexity and hallucination propagation |
| [04 AgentClinic](04_AgentClinic_npj_Digital_Medicine_2026/) | Schmidgall et al., *npj Digital Medicine*, 2026 | Two main figures and Chinese analysis | Agent environment with concrete trajectories; physician- and patient-model factor decomposition |
| [05 BioMedAgent](05_BioMedAgent_Nature_Biomedical_Engineering_2026/) | Bu et al., *Nature Biomedical Engineering*, 2026 | Three main figures and Chinese analysis | Planning–coding–execution loop, task-level states and external benchmarks |
| [06 AFMBench](06_AFMBench_Nature_Communications_2025/) | Mandal et al., *Nature Communications*, 2025 | Three main figures and Chinese analysis | Tool/agent requirement composition, cost efficiency and task-complexity stratification |
| [07 Agent Scaling](07_AgentScaling_Nature_Machine_Intelligence_2026/) | Kim et al., *Nature Machine Intelligence*, 2026 | One representative figure and Chinese analysis | Matched small multiples, box distributions and annotated relative changes |
| [08 PHIA](08_PHIA_Nature_Communications_2026/) | Merrill et al., *Nature Communications*, 2026 | Two main figures and Chinese analysis | Separate presentation of automatic objective metrics and human/expert ratings |
| [09 Clinical Trial Scoring](09_ClinicalTrialScoring_Scientific_Reports_2026/) | Mao et al., *Scientific Reports*, 2026 | One scoring-workflow figure and Chinese analysis | A complete chain from raters and 0–5 domains to aggregation and agreement |

## Combined reference for a surgical-planning benchmark

The most useful design combines figure grammars rather than copying one paper:

1. Use GPBench Figure 1 to show “input → annotation → system → scoring → results”.
2. Use GPBench Figure 2 to show all scoring domains, while keeping non-compensable safety requirements in a separate gating layer.
3. Use Lung AI-3D's multi-reader multi-case structure for clinical plan comparisons.
4. Use ClinicalAgentBench's state diagrams to explain automated output, human review and failure propagation.
5. Use PHIA's point-and-interval plots to separate automated geometric metrics from expert acceptability.
6. Use AFMBench/Agent Scaling small multiples to stratify by case complexity, tooth position or system version.

## File conventions

- One directory per paper.
- `figures/`: original paper figures or faithful PDF page views; never a redrawn image presented as the source figure.
- `paper-card.md`: complete Chinese deep-reading card, available only after a full-paper read.
- `paper-card_en.md`: corresponding English deep-reading card, available only when it has passed source-alignment audit.
- `figure-analysis.md`: explains what each figure shows, supports, does not support, and which design ideas are transferable.
- `figure-analysis_en.md`: corresponding English figure-by-figure analysis.
- `audit-report.json` and `audit-report_en.json`: structure and source-location audits for the corresponding Paper Cards.
- New literature should continue to use this structure.

## Rights and citation

Image rights and licences remain with the original authors and publishers. Each analysis provides the paper title, journal and DOI. This repository does not claim copyright over source figures, and the figures should not be republished directly as new manuscript illustrations. New figures should reuse the information structure while being independently designed. See [SOURCE_AND_USE_NOTICE.md](SOURCE_AND_USE_NOTICE.md).
