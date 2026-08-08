# GPBench: in-depth analysis of all six main figures

**Language: English | [中文](figure-analysis.md)**

Paper: Li Z, Yang Y, Lang J, et al. *Evaluating clinical competencies of large language models with a general practice benchmark*. **Nature Communications**. 2026;17:5302. [DOI](https://doi.org/10.1038/s41467-026-71622-6)

## Figure 1 — complete benchmark workflow

![Figure 1 — GPBench workflow](figures/Figure_1.png)

- **What it shows:** three data sources → expert annotation under a competency model → three test sets → LLM responses → automatic or human scoring → domain-level results.
- **Visual grammar:** a clockwise loop, stable blue/orange semantics, dashed stage containers, and one central competency model linking annotation to scoring.
- **Supported claim:** GPBench is a system combining a competency model, three data modalities, and two scoring mechanisms, not merely a question bank.
- **Missing evidence:** sample size, source bias, expert agreement, and external validity are not established by the workflow drawing.
- **Reusable lesson:** let the same clinical framework constrain both annotation and scoring and visibly separate automatic from expert evaluation.

## Figure 2 — every scoring domain and its weight

![Figure 2 — competency hierarchy and weights](figures/Figure_2.png)

- **What it shows:** six primary domains in the inner ring and fourteen secondary competencies outside; primary weights are 10%, 40%, 30%, 10%, 5%, and 5%.
- **Supported claim:** this is a direct Nature Portfolio example of describing all benchmark scoring content in one figure.
- **Boundary:** weights came from Delphi consensus rather than predictive-validity optimization; the figure does not show disagreement or ranking sensitivity.
- **Reusable lesson:** show parent domain, child domain, and weight together only after clinical approval. Hard safety constraints should be non-compensatory gates.
- **Design caution:** rotated labels and wedge area can be hard to read; a hierarchical bar layout may be more precise.

## Figure 3 — MCQ capability profile

![Figure 3 — six-domain radar comparison](figures/Figure_3.png)

- **What it shows:** ten models across six weighted MCQ domains.
- **Strength:** rapid recognition of capability profiles and imbalance.
- **Limitation:** heavy overlap, no uncertainty, and a radial axis beginning at 0.4 visually magnify differences.

## Figure 4 — six open-case result panels

![Figure 4 — domain-level Clinical Case Test Set results](figures/Figure_4.png)

- **What it shows:** diagnosis/differential, complications, emergency recognition, referral, best treatment plan, and health education on a shared 0–100 scale.
- **Strength:** one panel per clinical domain with consistent axes makes cross-domain difficulty easy to inspect.
- **Limitation:** bars omit case distributions, confidence intervals, rater variation, and statistical comparisons.

## Figure 5 — a single bottleneck

![Figure 5 — AI-patient history-taking score](figures/Figure_5.png)

- **What it shows:** one history-taking metric across nine models; DeepSeek-R1 is excluded for instruction-following failure.
- **Supported claim:** all reported models score below 60, highlighting a shared bottleneck.
- **Reusable lesson:** elevate a clinically critical safety endpoint into a standalone figure, but state exclusions and denominators.

## Figure 6 — coverage distribution

![Figure 6 — MCQ counts across competency domains](figures/Figure_6.png)

- **What it shows:** 3,661 questions distributed across six primary and fourteen secondary domains.
- **Supported claim:** benchmark evidence is unevenly distributed; knowledge and diagnosis dominate while some domains are sparse.
- **Boundary:** task count is not clinical importance, difficulty, discrimination, or scoring quality.

## How the six figures form one narrative

| Narrative question | Figure | Role |
|---|---|---|
| How does the benchmark operate? | Figure 1 | Workflow and evaluation loop |
| What is scored? | Figure 2 | Domains, hierarchy, and weights |
| How do models perform on knowledge tasks? | Figure 3 | Capability profile |
| How do they perform on open cases? | Figure 4 | Domain-level outcomes |
| What is the key bottleneck? | Figure 5 | Critical single endpoint |
| Is coverage balanced? | Figure 6 | Sample-distribution audit |

## Evidence boundary
