# Paper Card: Evaluating clinical competencies of large language models with a general practice benchmark

**Language: English | [中文](paper-card.md)**

> Source coverage: Full paper with all six main figures and four tables
>
> Extraction confidence: High
>
> Locator mode: page-grounded
>
> Primary analytical lens: Resource / benchmark
>
> Secondary analytical lens: Clinical evaluation
>
> Context verification: Official Nature Communications article checked on 2026-08-07
>
> Card completeness: Complete relative to the main paper

## Terminology Ledger

| Term | Canonical meaning | Boundary |
|---|---|---|
| GPBench | General practice benchmark | Competency model plus three test sets |
| MCQ Test Set | 3,661 multiple-choice items | Primarily closed-form knowledge measurement |
| Clinical Case Test Set | 70 real outpatient records | Open diagnosis/treatment responses |
| AI Patient Test Set | Interactive cases from the same 70 records | Primarily tests history taking within ten turns |

## 01 Basic Information

- [Paper] Zheqing Li, Yiying Yang, Jiping Lang et al.; *Nature Communications* 17, 5302 (2026), published 16 April 2026. [Paper: PDF p. 1]
- [Paper] DOI: [10.1038/s41467-026-71622-6](https://doi.org/10.1038/s41467-026-71622-6); CC BY-NC-ND 4.0. [Paper: PDF p. 12]
- [Paper] Six primary and fourteen secondary competencies; 3,661 MCQs, 70 clinical cases, 70 derived AI-patient cases, and ten LLMs. [Paper: PDF pp. 2, 8–10]
- [Paper] All evaluation tasks were conducted in Chinese. [Paper: PDF p. 2]

## 02 One-Sentence Summary

[Analysis] GPBench uses a Delphi-derived general-practice competency model and three progressively realistic test formats to show that strong MCQ performance does not translate into reliable open-case reasoning or interactive history taking. [Paper: PDF pp. 2–10]

## 03 Research Question

- [Paper] Can a responsibility-driven benchmark distinguish factual medical knowledge from the competencies required in routine general practice? [Paper: PDF pp. 1–2]
- [Paper] How do ten LLMs perform across closed, open, and interactive tasks relative to a small GP reference group? [Paper: PDF pp. 2–6]
- [Analysis] Can the scoring design expose clinically meaningful failure modes rather than only rank models?

## 04 Research Background and Development Path

| Stage | Strength | Limitation | GPBench response |
|---|---|---|---|
| Exam QA | Objective and scalable | Emphasizes recall | MCQ layer retained as baseline |
| Open clinical cases | Exposes diagnostic and treatment omissions | Requires expert rubrics | Clinical Case layer |
| Interactive simulation | Tests active information acquisition | Simulator can add error | AI Patient layer |
| Competency frameworks | Align evaluation with professional duties | Must be operationalized for observable outputs | Six primary, fourteen secondary indicators |

[Paper: PDF pp. 1–3, 8–9]

## 05 Core Pain Points Identified by the Paper

| Pain point | Manifestation | Evidence |
|---|---|---|
| Knowledge–practice mismatch | Good MCQ scores but weaker case reasoning/history taking | [Paper: PDF pp. 4, 7–8] |
| Open outputs resist automatic scoring | Multiple correct elements and clinically important omissions | [Paper: PDF pp. 2, 9] |
| A single score hides failure type | Diagnosis and treatment errors have different safety meaning | [Paper: PDF pp. 5–7, Tables 2–3] |
| Coverage is uneven | MCQ counts vary strongly across competency domains | [Paper: PDF p. 10, Figure 6] |

## 06 Core Idea

- [Paper] Surface method: derive a weighted competency model through expert consensus, construct three test sets, and score each task against that model. [Paper: PDF pp. 2, 8–9]
- [Paper] Core insight: task format changes which clinical capability is observable. [Paper: PDF pp. 4–8]
- [Analysis] General lesson: closed questions, open plans, and interactive information gathering must remain separate endpoints.

## 07 Method Overview

![Figure 1 — GPBench construction and evaluation workflow (official figure)](figures/Figure_1.png)

*Figure 1 closes the loop from source data and competency model to three test sets, model responses, automated/manual grading, and competency-level analysis. [Paper: PDF p. 2, Figure 1]*

Flow: open datasets/expert questions/outpatient records → competency-aligned annotation → MCQ, Clinical Case, and AI Patient tests → LLM responses → automatic accuracy or three-GP rubric scoring → indicator-level reporting. [Paper: PDF pp. 2, 8–9]

## 08 Core Module Breakdown

| Module | Function | Input/output | Evidence/assumption |
|---|---|---|---|
| Competency model | Defines 6 primary and 14 secondary domains and weights | Duties→measurable indicators | Delphi consensus; Figure 2 |
| MCQ Test Set | Scalable knowledge baseline | 3,661 items→accuracy | Five option-order prompts and majority vote |
| Clinical Case Test Set | Open diagnosis/treatment evaluation | 70 records→rubric score | Three-GP manual scoring |
| AI Patient Test Set | History-taking evaluation | 70 cases, ≤10 turns→I2-2 score | Simulator fidelity is assumed |
| Deficiency analysis | Explains score mechanisms | Responses→error categories | Tables 2–3 |

[Paper: PDF pp. 2–9, Table 4]

![Figure 2 — competency indicators and importance weights (official figure)](figures/Figure_2.png)

*Figure 2 is the benchmark-definition figure: it shows exactly what is scored and how domains are weighted, but not rater reliability or score aggregation. [Paper: PDF p. 3, Figure 2]*

## 09 Essential Formulas and Symbols

- [Paper] Primary-domain MCQ scores are weighted combinations of secondary indicators; the weights come from the expert-derived framework. [Paper: PDF pp. 2–3, Figure 2]
- [Paper] Each MCQ is prompted five times with permuted choices and resolved by majority vote; clinical cases are graded once per case. [Paper: PDF p. 9]
- [Paper] Welch's t-test is used for MCQ model comparisons; Wilcoxon rank-sum tests are used for non-normal case-score comparisons. [Paper: PDF p. 9]
- [Paper] Table 1 lists the ten models; Table 4 summarizes content, format, and sample size across test sets. [Paper: PDF pp. 3, 9, Tables 1 and 4]
- [Extraction boundary] The source bundle records Equation 1, Equation 2, Equation 3, Equation 4, and Equation 5, but their automatically extracted text is not reliable enough for verbatim reuse; the statistical procedures above should be checked against the PDF before implementation. [Paper: PDF p. 9]

## 10 Experimental Design and Evidence Chain

| Experiment | Setting | Result | Supported conclusion | Unsupported stronger conclusion |
|---|---|---|---|---|
| MCQ | 3,661 items, 14 indicators | DeepSeek-R1 82.74±1.20; o1-preview 79.16±1.27 | Reasoning models are strong on this Chinese MCQ set | Full general-practice competence |
| Clinical cases | 70 records, manual rubric | DeepSeek-R1 81.80±16.92; only it exceeded 70 on treatment-plan I3-1 | Open cases expose unstable diagnostic/treatment capability | Autonomous clinical readiness |
| AI Patient | Same 70 cases, ≤10 turns | All models <60; o1-preview highest at 55.20±8.01 | Active history taking is a major bottleneck | Equivalent failure in all real consultations |
| GP reference | Six GPs; 200 sampled MCQs and all cases | LLMs generally higher on MCQs, lower on cases | Relative human/model ranking depends on task format | A precise human-equivalence threshold |

[Paper: PDF pp. 3–10, Figures 3–6]

![Figure 3 — MCQ profiles across six primary competencies (official figure)](figures/Figure_3.png)

*Figure 3 provides a multiaxial capability profile, but overlapping polygons and a truncated radial scale limit exact model comparison. [Paper: PDF p. 4, Figure 3]*

![Figure 4 — six Clinical Case competencies (official figure)](figures/Figure_4.png)

*Figure 4 uses matched panels to show that one model can have different strengths across diagnosis, referral, treatment, and education; the bars do not expose case-level dispersion or rater disagreement. [Paper: PDF p. 5, Figure 4]*

![Figure 5 — AI Patient history-taking scores (official figure)](figures/Figure_5.png)

*Figure 5 makes the absolute deficit visible: every included model is below 60, with o1-preview highest at 55.20; DeepSeek-R1 was excluded for instruction-following failure. [Paper: PDF p. 6, Figure 5]*

![Figure 6 — MCQ distribution across competency domains (official figure)](figures/Figure_6.png)

*Figure 6 reveals highly unequal item counts; item count is not the same as clinical importance or measurement quality. [Paper: PDF p. 10, Figure 6]*

- [Paper] Table 2 reports diagnostic-process deficiency proportions; Table 3 reports treatment-recommendation deficiencies. [Paper: PDF pp. 6–7, Tables 2–3]

## 11 Correct Interpretation of the Conclusions

- [Paper] Clinical Case inputs already contain organized records; only the AI Patient condition tests active questioning. [Paper: PDF p. 9]
- [Paper] The human reference comprises six GPs, two per experience stratum, and only 200 MCQs. [Paper: PDF p. 10]
- [Paper] Data are Chinese and the real cases originate from China. [Paper: PDF p. 8]
- [Analysis] GPBench supports the claim that MCQ scores are insufficient; it does not establish that any LLM can practice autonomously.

## 12 Limitations Explicitly Acknowledged by the Authors

| Limitation | Manifestation | Future direction | Source |
|---|---|---|---|
| Language/region | Chinese-only evaluation and local records | Validate across languages and regions | [Paper: PDF p. 8] |
| Case scale | 70 deeply annotated cases | Expand while retaining annotation quality | [Paper: PDF pp. 8–9] |
| Disease coverage | Eight chronic diseases and ten common symptom groups | Broaden clinical coverage | [Paper: PDF pp. 8–9] |
| AI patient fidelity | Simulation may not reproduce real patients | Further validate the simulator | [Paper: PDF p. 9] |

## 13 Critical Analysis

| [Analysis] Observation | Why it matters | Test |
|---|---|---|
| MCQ coverage is highly unequal | Large domains dominate precision and stability | Stratified bootstrap and minimum domain sizes |
| Main case figures show means only | Heterogeneity and rater disagreement are hidden | Add case points, intervals, ICC/weighted κ |
| Human reference is small and asymmetric | “Outperforming physicians” is easy to overstate | Larger paired reader study on identical items |
| AI Patient is both environment and model component | Simulator error can be attributed to the tested model | Human standardized-patient and simulator ablation |

## 14 Knowledge Learned

- Agent-derived knowledge candidate: use a three-level task gradient—closed, open, interactive—and report each separately.
- Agent-derived knowledge candidate: one figure should define the entire benchmark loop; another should define every scoring domain and weight.
- Agent-derived knowledge candidate: pair aggregate scores with failure categories and domain sample sizes.

## 15 Connections to Existing Knowledge

[External] The lung-surgery AI-3D study in this repository supplies a more directly clinical reader-study template: crossed MRMC design, planning accuracy, time, confidence, and agreement. See [Nature Communications](https://doi.org/10.1038/s41467-025-59200-8).

[Analysis] For ImplantAgent, GPBench is most useful for defining a multidomain rubric, while the lung study is more useful for evaluating an actual surgical-planning aid.

## 16 Research Ideas

### Agent-derived research candidate: non-compensatory surgical-plan competency benchmark

- Origin: GPBench's competency hierarchy and uneven domain evidence. [Paper: PDF pp. 3, 10, Figures 2 and 6]
- [Hypothesis] A plan-level profile that separates position, axis, depth, size, anatomic safety, executability, and manual-review reason will predict expert acceptance better than a compensatory total score.
- Delta: introduce hard safety gates that cannot be offset by strengths in other domains.
- Validation: compare domain profiles and total scores against expert accept/reject, correction type, and correction magnitude using patient-level splits and case-level intervals.
- Failure modes: too few experts; rubric weights may not transport; hard gates may be incorrectly specified.
- Innovation status: unverified; clinical consensus and dedicated prior-art search are required.
