# Nature Benchmark Figure Reference Library

**Language: English | [中文](README_CN.md)**

This research-figure reference library is organized by paper. It focuses on examples from Nature Portfolio and related high-impact journals that show:

- end-to-end benchmark workflows;
- complete scoring domains, hierarchies and weights;
- primary and component-level result figures;
- cost, time, tool-use and workflow-complexity figures;
- failure propagation, safety and human-rating figures;
- source-aligned deep analysis of each figure.

The repository is intended for personal research reading and figure-design reference. It does not define any ImplantAgent scoring item, weight, threshold, clinical endpoint or conclusion.

Root paper folders use two-digit navigation ranks (`01` = newest) so GitHub's native folder list is newest first. The paper-directory titles below omit this navigation-only prefix.

## How to use this library

1. Start with the paper directory below. It is ordered by formal publication date, with the newest paper first.
2. Choose a paper according to the figure-design problem you want to solve, using the “Most reusable figure design” column.
3. Open `paper-card.md`, when available, for the complete source-grounded deep reading, key evidence and claim boundaries.
4. Open `figure-analysis.md` for figure-by-figure analysis of workflow, benchmark or scoring design, result presentation and transferable visual grammar.
5. Treat saved source figures or faithful PDF page views as design references. Verify every scientific claim against the cited original article.

## Paper directory

| Directory | Paper / journal | Saved content | Most reusable figure design |
|---|---|---|---|
| [2026-07-24 — Capable language models can outgrow the benefits of collaboration](01_2026-07-24_Capable_language_models_can_outgrow_the_benefits_of_collaboration/) | Kim et al., *Nature Machine Intelligence*, 2026 | One representative figure and Chinese analysis | Matched small multiples, box distributions and annotated relative changes |
| [2026-04-27 — AgentClinic](02_2026-04-27_AgentClinic/) | Schmidgall et al., *npj Digital Medicine*, 2026 | Two main figures and Chinese analysis | Agent environment with concrete trajectories; physician- and patient-model factor decomposition |
| [2026-04-16 — GPBench](03_2026-04-16_GPBench/) | Li et al., *Nature Communications*, 2026 | Six official main figures, complete Chinese Paper Card, figure-by-figure analysis, source bundle and audit | Benchmark workflow, full scoring domains and weights, domain-level small multiples, sample distribution |
| [2026-04-02 — Benchmarking agreement between large language models and published clinical trial conclusions across four artificial intelligence platforms](04_2026-04-02_Benchmarking_agreement_between_large_language_models_and_published_clinical_trial_conclusions_across_four_artificial_intelligence_platforms/) | Mao et al., *Scientific Reports*, 2026 | One scoring-workflow figure and Chinese analysis | A complete chain from raters and 0–5 domains to aggregation and agreement |
| [2026-03-30 — BioMedAgent](05_2026-03-30_BioMedAgent/) | Bu et al., *Nature Biomedical Engineering*, 2026 | Three main figures and Chinese analysis | Planning–coding–execution loop, task-level states and external benchmarks |
| [2026-02-18 — Benchmarking large language model-based agent systems for clinical decision tasks](06_2026-02-18_Benchmarking_large_language_model-based_agent_systems_for_clinical_decision_tasks/) | Liu et al., *npj Digital Medicine*, 2026 | Four main figures and Chinese analysis | Accuracy–token trade-off, workflow complexity and hallucination propagation |
| [2026-01-12 — PHIA](07_2026-01-12_PHIA/) | Merrill et al., *Nature Communications*, 2026 | Two main figures and Chinese analysis | Separate presentation of automatic objective metrics and human/expert ratings |
| [2025-10-14 — AFMBench](08_2025-10-14_AFMBench/) | Mandal et al., *Nature Communications*, 2025 | Three main figures and Chinese analysis | Tool/agent requirement composition, cost efficiency and task-complexity stratification |
| [2025-05-01 — InferOperate Thorax](09_2025-05-01_InferOperate_Thorax/) | Chen et al., *Nature Communications*, 2025 | Four main-figure page views, Chinese and English Paper Cards, bilingual figure analysis, source bundle and separate audits | Multi-reader multi-case design and clinical-planning results before versus after assistance |

## Combined reference for a surgical-planning benchmark

The most useful design combines figure grammars rather than copying one paper:

1. Use GPBench Figure 1 to show “input → annotation → system → scoring → results”.
2. Use GPBench Figure 2 to show all scoring domains, while keeping non-compensable safety requirements in a separate gating layer.
3. Use the InferOperate Thorax study's multi-reader multi-case structure for clinical plan comparisons.
4. Use the state diagrams in Liu et al.'s clinical-agent evaluation to explain automated output, human review and failure propagation.
5. Use PHIA's point-and-interval plots to separate automated geometric metrics from expert acceptability.
6. Use AFMBench and Kim et al.'s multi-agent collaboration small multiples to stratify by case complexity, tooth position or system version.

## File conventions

- One directory per paper.
- `README.md` is the default English landing page; `README_CN.md` is the Chinese version selected through the language switch.
- Name each directory `YYYY-MM-DD_OfficialModelOrBenchmarkName`. If the paper does not explicitly name one principal model, system or benchmark, use `YYYY-MM-DD_OriginalArticleTitle`. Use the publisher's formal `Published` date, not the acceptance date, volume year or repository-addition date.
- `figures/`: original paper figures or faithful PDF page views; never a redrawn image presented as the source figure.
- `paper-card.md`: complete Chinese deep-reading card, available only after a full-paper read.
- `paper-card_en.md`: corresponding English deep-reading card, available only when it has passed source-alignment audit.
- `figure-analysis.md`: explains what each figure shows, supports, does not support, and which design ideas are transferable.
- `figure-analysis_en.md`: corresponding English figure-by-figure analysis.
- `audit-report.json` and `audit-report_en.json`: structure and source-location audits for the corresponding Paper Cards.
- New literature should continue to use this structure.

## Rights and citation

Image rights and licences remain with the original authors and publishers. Each analysis provides the paper title, journal and DOI. This repository does not claim copyright over source figures, and the figures should not be republished directly as new manuscript illustrations. New figures should reuse the information structure while being independently designed. See the [source and use notice](SOURCE_AND_USE_NOTICE.md).
