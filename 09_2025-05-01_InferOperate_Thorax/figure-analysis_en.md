# Lung-surgery AI-3D planning study: figure-by-figure analysis

**Language: [中文](figure-analysis.md) | English**

> Paper: Chen et al. *Artificial intelligence driven 3D reconstruction for enhanced lung surgery planning*. *Nature Communications* 16, 4086 (2025).
>
> DOI: [10.1038/s41467-025-59200-8](https://doi.org/10.1038/s41467-025-59200-8)
>
> Visual format: each image below is a faithful full PDF page view that retains the complete main figure, legend and adjacent article text.
>
> Evidence boundary: the study evaluates thoracic surgeons assisted by AI-3D in simulated preoperative-planning tasks. It does not evaluate autonomous surgical-plan generation or patient outcomes.

## Figure 1: showing the complete clinical-benchmark execution chain

![Figure 1 — MRMC study design (full PDF page view)](figures/page-003.png)

### What the figure shows

Figure 1 starts with 450 consecutively enrolled patients from three centres, then shows random selection of 140 cases, reference construction by three experts, random grouping of ten readers, two crossover assessment phases and a washout of at least 28 days before accuracy, time, confidence and agreement analyses. [Paper: PDF p. 3, Figure 1]

### Why it works as a main benchmark-workflow figure

- It shows how the system is evaluated rather than focusing on the neural-network architecture.
- Patient sources, reference-setting experts and evaluated readers are visually distinct roles, reducing ambiguity about leakage and responsibility.
- The crossover and washout are explicit, so the same-reader, same-case comparison under two conditions is immediately understandable.

### What the figure does not establish

The figure does not identify which segmentation or rendering component caused the observed effect, and it does not establish operative safety or improved patient outcomes. It defines a simulated preoperative-planning evaluation. [Paper: PDF p. 3, Figure 1]

## Figure 2: expanding the primary endpoint across readers, structures and prevalence

![Figure 2 — anatomical-variant identification results (full PDF page view)](figures/page-004.png)

### What the figure shows

- Panel A: case-wise anatomical-identification accuracy with AI-3D assistance versus 2D CT.
- Panel B: results for each of the ten readers, testing whether the aggregate effect is driven by only a few users.
- Panel C: improvement across 39 anatomical structures, with a favourable direction for 35.
- Panel D: correlation between variant prevalence and identification accuracy, with (R^2=0.68).
- Panel E: assistance effects across the prevalence range. [Paper: PDF p. 4, Figure 2]

### Result-story structure

The figure follows a useful progression: overall effect → user consistency → task components → difficulty or prevalence interpretation. The overall panel answers the primary endpoint; reader and structure panels address robustness; prevalence panels explore where changes may be larger. This is more informative than a single mean-accuracy bar chart.

### Conclusion boundary

A favourable direction for 35 of 39 structures shows broad within-study distribution, not guaranteed benefit for every rare variant or external centre. The prevalence analysis is exploratory and does not define a validated clinical indication. [Paper: PDF pp. 4 and 7, Figure 2]

## Figure 3: decomposing mean accuracy into decision-error types

![Figure 3 — procedure selection and error composition (full PDF page view)](figures/page-005.png)

### What the figure shows

Figure 3 first reports an increase in procedure-selection accuracy from 0.77 to 0.85 with an error relative risk of (RR=0.65). It then shows per-reader results, binary lobectomy-versus-segmentectomy decisions and error decomposition into mistaken, insufficient and excessive resection, with relative risks of 0.27, 0.49 and 0.98, respectively. [Paper: PDF p. 5, Figure 3]

### Why this is more useful than one success rate

Aggregate accuracy can hide errors with different clinical consequences. The figure shows stronger effects for mistaken and insufficient resection but almost no improvement for excessive resection. A higher average performance therefore does not imply that every risk decreases.

### Conclusion boundary

Agreement with an expert procedure reference is not evidence of improved patient outcome. The figure also does not weight error categories by the severity of clinical harm. [Paper: PDF pp. 5 and 7, Figure 3]

## Figure 4: separating efficiency, confidence and accuracy

![Figure 4 — planning time and confidence results (full PDF page view)](figures/page-006.png)

### What the figure shows

Figure 4 reports a median reduction of 63 seconds, or 25%, in the reader planning task. It also shows the proportion of assessments with a confidence score of exactly 100 after assistance and relates confidence to anatomical-identification and procedure-selection accuracy. [Paper: PDF p. 6, Figure 4]

### Strength of the visual narrative

Efficiency and confidence remain separate from accuracy. Readers can therefore distinguish whether the workflow is faster, whether users feel more certain and whether decisions are more correct, without treating subjective experience as performance evidence.

### Conclusion boundary

The 63-second difference applies to the reader interpretation task and excludes the AI reconstruction latency of approximately 233.76±75.08 seconds, so it is not a 63-second end-to-end saving. The confidence analysis uses a post-hoc threshold of exactly 100 and does not demonstrate calibration. [Paper: PDF pp. 6–7, Figure 4]

## The complete four-figure result narrative

```text
Figure 1: Is the evaluation workflow credible?
→ Figure 2: Does the primary clinical task improve, and is the effect distributed?
→ Figure 3: Which decision errors change, and which do not?
→ Figure 4: Do efficiency and subjective confidence change as well?
```
