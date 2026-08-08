# Paper Card: Artificial intelligence driven 3D reconstruction for enhanced lung surgery planning

**Language: [中文](paper-card.md) | English**

> Source coverage: Full paper with all main-text figures and tables, plus the official Supplementary Information
>
> Extraction confidence: High
>
> Locator mode: page-grounded
>
> Primary analytical lens: Clinical evaluation
>
> Secondary analytical lens: Methods and benchmark design
>
> Context verification: Targeted external check of the official Nature Communications article and PubMed record on 5 August 2026
>
> Card completeness: Complete relative to the full article and official Supplementary Information

## Terminology Ledger

| Canonical term | First-use definition | Usage boundary in this card | Decision |
|---|---|---|---|
| AI-3D system | artificial intelligence-driven three-dimensional reconstruction system (AI-3D system) | InferOperate Thorax, which visualizes pulmonary vessels, bronchi and lesions; it is not an autonomous surgical-plan generator | Define once, then use `AI-3D system` |
| MRMC | multi-reader, multi-case (MRMC) study | Ten surgeons evaluated all 140 cases under both conditions | Use `MRMC` after first definition |
| reader | participating thoracic surgeon | One of the ten surgeons who performed the simulated preoperative-planning tasks | Use `reader` when discussing the experimental role |
| expert panel | three senior thoracic surgeons | The group that established and adjudicated the reference standard | Do not conflate with the ten readers |
| reference standard | expert-panel reference used for scoring | Constructed from CT, manual 3D reconstruction, operative videos and surgical records | Prefer over the stronger term `ground truth` |
| anatomical variant identification | identification of planning-relevant pulmonary anatomical structures and variants | The primary clinical task | Keep distinct from segmentation accuracy |
| operation procedure selection | selection of the intended lung-resection procedure | Includes resection extent but is not a complete executable surgical plan | Do not describe as autonomous planning |
| assistance condition | planning with 2D CT and AI-3D support | The evaluated intervention is surgeon plus AI | Use consistently |
| control condition | planning with conventional 2D CT alone | Within-reader comparator | Use consistently |

## 01 Basic Information

- [Paper] Title: *Artificial intelligence driven 3D reconstruction for enhanced lung surgery planning*.
- [Paper] Co-first authors: Xiuyuan Chen, Chenyang Dai, Muyun Peng and Dawei Wang. The corresponding-author group includes Yuming Zhu, Fenglei Yu and Fan Yang. [Paper: PDF p. 1]
- [Paper] Journal and year: *Nature Communications*, 2025, volume 16, article 4086; published on 1 May 2025.
- [Paper] DOI: <https://doi.org/10.1038/s41467-025-59200-8>
- [Paper] Study type: retrospective, three-centre, two-stage, fully crossed MRMC reader study. [Paper: PDF pp. 2–3, Fig. 1]
- [Paper] Population: 140 randomly selected cases from 450 consecutively eligible patients; 62 underwent lobectomy and 78 underwent segmentectomy. Ten thoracic surgeons served as readers. [Paper: PDF pp. 2–3, Table 1 and Fig. 1]
- [Paper] Intervention: preoperative planning with AI-3D assistance. Comparator: planning with conventional 2D CT alone. [Paper: PDF p. 3, Fig. 1]
- [Paper] Primary endpoint: case-wise accuracy of anatomical structure identification. [Paper: PDF pp. 3 and 8]
- [Paper] Field: clinical artificial intelligence, thoracic surgery, surgical planning and medical-image visualization.
- [Paper] Keywords: AI-assisted surgical planning; three-dimensional reconstruction; thoracic surgery; MRMC; human–AI collaboration; clinical benchmark.
- [Paper] Code and data availability: the commercial software is proprietary; source data are supplied for the reported figures, but the complete system is not openly reproducible from the article alone. [Paper: PDF p. 10]
- [Paper] Funding and competing interests: the study was partly funded by Beijing Infervision Technology Co., Ltd.; several authors were company employees. [Paper: PDF p. 10]
- Reading date: 5 August 2026.

## 02 One-Sentence Summary

[Analysis] In a fully crossed MRMC study, the authors tested whether AI-generated three-dimensional pulmonary anatomy improved surgeons' preoperative decisions and found higher anatomical-identification and procedure-selection accuracy with shorter reader planning time, thereby supporting human–AI assistance within the studied setting but not autonomous surgical planning or improved patient outcomes.

## 03 Research Question

### Concrete problem

- [Paper] The primary question was whether AI-3D assistance could improve thoracic surgeons' accuracy in identifying planning-relevant pulmonary anatomical structures during lobectomy and segmentectomy planning. [Paper: PDF pp. 1 and 8]
- [Paper] Secondary questions concerned operation procedure selection, error types, planning time, reader confidence, interobserver agreement and system satisfaction. [Paper: PDF pp. 4–7, Figs. 3–4 and Table 2]

### Why it matters

- [Paper] Complex and distal pulmonary vascular or bronchial variants can be difficult to reconstruct mentally from two-dimensional CT, yet misinterpretation can affect operative preparation and resection decisions. [Paper: PDF pp. 1–2]
- [Paper] Manual 3D reconstruction is time-consuming, which limits its routine use. [Paper: PDF p. 1]

### Why existing evaluation is insufficient

- [Analysis] Segmentation or reconstruction accuracy alone does not establish that the representation improves clinical decision-making.
- [Paper] Prior reports of downstream perioperative benefit were inconsistent, motivating evaluation of the more proximal preoperative-planning task. [Paper: PDF pp. 1–2]

### Precise research question

[Analysis] Can adding an AI-generated 3D anatomical representation to conventional CT improve the accuracy, consistency and efficiency of thoracic surgeons' preoperative planning compared with CT alone?

## 04 Research Background and Development Path

> Context mode: targeted external check. The bibliographic record was externally verified, whereas the field-development narrative below is primarily reconstructed from the paper and is therefore paper-framed.

| Stage | Representative approach | Advantage | Limitation | Position of this paper |
|---|---|---|---|---|
| Conventional planning | Interpretation of 2D CT slices | Widely available and integrated into routine care | Requires mental reconstruction of complex 3D relationships | Used as the control condition |
| Manual 3D reconstruction | Human segmentation and reconstruction | Provides intuitive spatial information | Time-intensive and difficult to scale | Used as one source for the expert reference |
| Automated AI reconstruction | Algorithmic segmentation and rendering | Reduces reconstruction burden and improves accessibility | Technical performance does not by itself prove clinical utility | Provides the AI-3D representation |
| Clinical task evaluation | Reader performance with versus without AI | Tests whether AI changes clinical decisions | Simulated reader studies may not reproduce real workflow or patient outcomes | Core contribution of this article |

1. [Paper] Conventional lung-surgery planning relies primarily on 2D CT, but complex distal structures and anatomical variants are not always intuitively represented. [Paper: PDF p. 1]
2. [Paper] Manual 3D reconstruction may improve spatial understanding but is too time-consuming for widespread routine use. [Paper: PDF p. 1]
3. [Paper] AI can automate reconstruction, but technical reconstruction performance is not equivalent to clinical-planning benefit. [Paper: PDF pp. 1–2]
4. [Paper] Because prior evidence concerning operative time and other downstream outcomes was inconsistent, the authors evaluated a task closer to the intended mechanism: preoperative anatomical interpretation and procedure selection. [Paper: PDF pp. 1–2]
5. [Analysis] The study therefore advances the evidence chain from “Can the model reconstruct anatomy?” to “Does the reconstruction improve clinician performance?”, while remaining one step short of “Does it improve patient outcomes?”.

## 05 Core Pain Points Identified by the Paper

| Pain point | Manifestation | Cause or author explanation | Evidence from the paper |
|---|---|---|---|
| Difficult spatial interpretation | Surgeons may miss or misclassify complex pulmonary structures | 2D slices provide a less intuitive representation of 3D anatomy | [Paper: PDF pp. 1–2] |
| Vulnerability of uncommon variants | Lower-prevalence structures tend to have lower identification accuracy | Limited familiarity and greater anatomical complexity are proposed contributors | [Paper: PDF p. 4, Fig. 2D–E] |
| Limited scalability of manual reconstruction | Manual 3D preparation can take substantial time | Segmentation and model construction require expert labour | [Paper: PDF pp. 1 and 6] |
| Gap between technical and clinical validation | A visually satisfactory reconstruction may not improve a planning decision | Model-level metrics do not directly measure clinician task performance | [Analysis] based on the study design [Paper: PDF p. 3, Fig. 1] |
| Reader and case heterogeneity | Performance varies across surgeons and cases | Clinical benchmarks contain crossed reader, case and interaction effects | [Paper: Supplementary PDF pp. 38–40] |

## 06 Core Idea

### Surface method

[Paper] Generate an AI-derived 3D reconstruction of pulmonary vessels, bronchi and lesions and make it available to surgeons during simulated preoperative planning. [Paper: PDF pp. 3 and 8]

### Core insight

[Paper] Evaluate the incremental clinical value of that representation by having every reader assess every case both with and without AI-3D assistance in a randomized, washed-out crossover design. [Paper: PDF p. 3, Fig. 1; Supplementary PDF pp. 25–41]

### General lesson

[Analysis] For a clinical AI benchmark, the most informative question is often not whether the algorithm reproduces an expert annotation, but whether adding its output changes the quality, consistency and efficiency of a real clinical task. That question requires a human–AI study design distinct from standalone model validation.

## 07 Method Overview

### Input and output

- [Paper] Input to the AI-3D system: chest CT in DICOM format, with eligible images having a slice thickness of no more than 2 mm. [Paper: PDF p. 8]
- [Paper] System output: interactive 3D visualizations of pulmonary vessels, bronchi and lesions. [Paper: PDF p. 8; Supplementary PDF pp. 56–57 and 75–77]
- [Paper] Reader output: identified anatomical structures, selected operation procedure, task time, confidence and system satisfaction. [Paper: PDF pp. 3–7]

### Study flow

```text
450 consecutively eligible patients from three centres
→ random selection of 140 cases
→ independent expert-panel reference construction
→ random allocation of ten readers into two groups
→ phase 1: AI-3D assistance versus 2D CT control
→ washout of at least 28 days
→ phase 2: crossover of the two conditions
→ primary and secondary endpoint analysis
```

![Figure 1 — MRMC study design (full PDF page view)](figures/page-003.png)

### Operational details

1. [Paper] Three centres collected 450 eligible patients.
2. [Paper] A random subset of 140 cases formed the reader-study dataset.
3. [Paper] Three senior surgeons established the reference using CT, manually constructed 3D models, operative video and surgical records. Two experts assessed cases independently and a third adjudicated disagreements. [Paper: PDF p. 3, Fig. 1; Supplementary PDF pp. 25–41]
4. [Paper] Ten readers were randomly divided into two groups of five.
5. [Paper] In phase 1, one group used AI-3D assistance and the other used 2D CT alone; all readers assessed all 140 cases.
6. [Paper] After a washout of at least 28 days, the groups exchanged conditions and reassessed all cases in randomized order. [Paper: PDF p. 3, Fig. 1]

### Main-figure argument map

| Figure or table | Question answered | Role in the evidence chain |
|---|---|---|
| Fig. 1 | How was the benchmark conducted? | Defines cohort flow, reference construction, reader randomization, crossover and washout |
| Fig. 2 | Did AI improve the primary endpoint, and was the effect consistent? | Moves from overall performance to reader-, structure- and prevalence-level analyses |
| Fig. 3 | How did AI change procedure selection and error composition? | Combines overall accuracy, reader consistency, binary decisions and error-type analysis |
| Fig. 4 | Did AI affect efficiency and confidence? | Adds workflow time and reader-reported confidence |
| Table 1 | Who and what were evaluated? | Describes the patient cohort |
| Table 2 | Did readers become more consistent? | Reports interobserver agreement under both conditions |

## 08 Core Module Breakdown

| Module | Function | Why it is needed | Input and output | Supporting evidence | Effect of removal or change |
|---|---|---|---|---|---|
| Bronchial segmentation | Extracts the bronchial tree | Supports airway-variant interpretation | CT patches → bronchial segmentation | [Paper: PDF p. 8] | [Analysis] Not isolated by an ablation; removing it would be expected to reduce bronchial visualization, but the magnitude is unknown |
| Intraparenchymal vessel segmentation | Segments vessels within the lung | Provides planning-relevant vascular anatomy | CT → vascular segmentation via a 2.5D model | [Paper: PDF p. 8] | [Analysis] No component-level clinical ablation is reported |
| Mediastinal vessel segmentation | Segments central vessels | Complements the intrapulmonary vessel model | CT → mediastinal vascular segmentation via a 3D network | [Paper: PDF p. 8] | [Analysis] Its independent contribution is not quantified |
| Region-growing extension | Extends vascular branches towards peripheral regions | Improves distal branch coverage | Initial vascular mask → extended peripheral mask | [Paper: PDF p. 8] | [Analysis] Removal could particularly affect distal branches, but this was not experimentally isolated |
| Surface reconstruction and rendering | Converts segmentations into an interactive 3D representation | Makes spatial relations accessible to the reader | Masks → Marching Cubes mesh → RayCasting/DepthPeeling display | [Paper: PDF p. 8] | [Analysis] The study compares the complete interface, not alternative rendering methods |
| Integrated lesion detection | Displays the target lesion with anatomy | Links lesion location to the planned resection | CT → lesion location within the 3D model | [Paper: Supplementary PDF pp. 56–57 and 75–77] | [Analysis] Lesion masking accounted for some unsatisfactory cases, but no ablation was performed |
| Expert reference construction | Defines the scoring reference | Allows reader answers to be judged consistently | CT, manual 3D models, videos and records → adjudicated reference | [Paper: PDF p. 3, Fig. 1] | A different reference could materially change measured accuracy |
| MRMC crossover protocol | Estimates the effect of adding AI while accounting for readers and cases | Reduces between-reader confounding and supports within-reader comparison | Reader–case assessments under two conditions → comparative endpoints | [Paper: PDF p. 3; Supplementary PDF pp. 25–41] | A parallel design would be more vulnerable to reader-group differences |

[Analysis] The article does not provide a component-removal experiment linking individual segmentation or rendering modules to the clinical endpoints. The supported unit of evaluation is the complete AI-3D assistance package.

## 09 Essential Formulas and Symbols

### 9.1 Case-wise anatomical-identification accuracy

[Paper]

\[
Accuracy_{case}=
\frac{\text{number of planning-relevant structures correctly identified by the reader}}
{\text{total number of planning-relevant structures in the expert reference}}
\]

- Purpose: defines the primary endpoint at the case level.
- Intuition: each case is scored by the proportion of relevant structures correctly identified.
- Boundary: structures are counted rather than weighted by clinical severity.
- Source: [Paper: Supplementary PDF pp. 38–40].

### 9.2 Relative risk of error

[Analysis]

\[
RR_{error}=\frac{1-Accuracy_{AI}}{1-Accuracy_{Control}}
\]

- Purpose: expresses the residual error under AI assistance relative to control.
- Example: accuracies of 0.87 and 0.78 give an approximate error ratio of \(0.13/0.22=0.59\), corresponding to a 41% relative error reduction.
- Interpretation boundary: the relative reduction should be reported together with the absolute accuracy difference to avoid overstating the practical effect.

### 9.3 DBMH MRMC model

[Paper] The primary analysis used the Dorfman–Berbaum–Metz–Hillis (DBMH) framework with jackknife pseudovalues to model method, reader, case and interaction effects: [Paper: Supplementary PDF pp. 38–40]

\[
Y_{ijk}=\mu+\tau_i+R_j+C_k+(\tau R)_{ij}+(RC)_{jk}+(\tau C)_{ik}+(\tau RC)_{ijk}+\epsilon_{n(ijk)}
\]

- \(\mu\): overall mean.
- \(\tau_i\): fixed effect of reading method.
- \(R_j\): reader effect.
- \(C_k\): case effect.
- Interaction terms: method–reader, reader–case, method–case and higher-order interactions.
- Primary superiority hypothesis: \(H_0:\tau_2-\tau_1\leq0\) versus \(H_A:\tau_2-\tau_1>0\), with a superiority margin of zero. [Paper: Supplementary PDF p. 40]

## 10 Experimental Design and Evidence Chain

### 10.1 Population, protocol and analysis set

- [Paper] Setting: three top-tier hospitals in China.
- [Paper] Enrollment: 450 consecutively eligible cases collected from July 2021 to January 2022; 140 randomly selected for the reader study. [Paper: PDF pp. 2 and 8]
- [Paper] Procedures: 62 lobectomies and 78 segmentectomies; all five lobes were represented. [Paper: PDF p. 2, Table 1]
- [Paper] Readers: ten board-certified thoracic surgeons, aged 34–45 years, with 6–19 years of practice. [Paper: PDF pp. 2–3]
- [Paper] Evaluation scale: 140 cases × 10 readers × 2 conditions, corresponding to 2,800 potential case-level planning assessments.
- [Paper] Missing primary entries: 918 of 24,400 anatomical-structure assessments (3.8%) were missing and treated as incorrect in the main analysis; a sensitivity analysis excluding missing answers showed the same direction of effect. [Paper: PDF p. 4]
- [Paper] Primary statistical framework: DBMH MRMC analysis. Additional analyses used continuous-variable tests, regression and Fleiss' kappa as appropriate. [Paper: PDF pp. 8–9; Supplementary PDF pp. 38–41]
- [Paper] Oracle information in the reference: operative videos and surgical records were available to the expert panel but not to readers during prospective planning.

### 10.2 Key numerical results

| Outcome | 2D CT alone | AI-3D assistance | Effect estimate | Source |
|---|---:|---:|---|---|
| Median case-wise anatomical-identification accuracy | 0.78 | 0.87 | Error RR 0.59, 95% CI 0.56–0.63; p<0.01 | [Paper: PDF p. 4, Fig. 2A] |
| Operation procedure selection accuracy | 0.77 | 0.85 | Absolute improvement 0.08, 95% CI 0.04–0.12; error RR 0.65 | [Paper: PDF p. 5, Fig. 3A–B] |
| Lobectomy-versus-segmentectomy classification | Not separately tabulated | Not separately tabulated | Absolute improvement 0.04, 95% CI 0.01–0.07 | [Paper: PDF p. 5, Fig. 3C] |
| Reader planning time | — | — | Median reduction 63 s, 95% CI 42–78; relative reduction 25% | [Paper: PDF p. 6, Fig. 4A–B] |
| Interobserver agreement for anatomical identification | κ=0.33 | κ=0.43 | Increased, although remaining moderate | [Paper: PDF p. 7, Table 2] |
| Interobserver agreement for procedure planning | κ=0.70 | κ=0.76 | Modest increase | [Paper: PDF p. 7, Table 2] |

![Figure 2 — anatomical-variant identification results (full PDF page view)](figures/page-004.png)
*Figure 2 moves from the overall primary endpoint to per-reader consistency, structure-level effects and prevalence-related patterns. It supports a distributed within-study benefit, but the exploratory prevalence analysis does not establish a validated indication for rare variants. [Paper: PDF p. 4, Figure 2]*

![Figure 3 — procedure selection and error composition (full PDF page view)](figures/page-005.png)
*Figure 3 combines overall procedure-selection accuracy with reader consistency, binary resection classification and error-type relative risks. The unequal effects across mistaken, insufficient and excessive resection show why a benchmark should report error composition rather than only one aggregate accuracy value. [Paper: PDF p. 5, Figure 3]*

![Figure 4 — planning time and confidence results (full PDF page view)](figures/page-006.png)
*Figure 4 separates task time from subjective confidence and relates confidence to accuracy. It supports faster reader interpretation and higher reported confidence under AI assistance, but it does not establish end-to-end time savings or calibrated confidence. [Paper: PDF p. 6, Figure 4]*

### 10.3 Experiment-to-claim matrix

| Experiment | Claim tested | Comparison and conditions | Result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|---|
| Primary MRMC analysis | AI-3D improves anatomical identification | Same ten readers and 140 cases under both conditions | 0.87 vs 0.78; error RR 0.59 | AI-3D assistance improved reader performance in this task and population | AI independently identified anatomy or improved surgical safety | [Paper: PDF p. 4, Fig. 2] |
| Missing-answer sensitivity analysis | The primary result is not solely caused by missing responses | Exclusion of unanswered structures | 0.86 vs 0.79; RR 0.64, 95% CI 0.57–0.82 | Direction of benefit was robust to this missing-data treatment | All possible missing-data mechanisms are resolved | [Paper: PDF p. 4] |
| Per-reader and per-structure analysis | Improvement is not driven by a single reader or structure | Ten readers, five lobes and 39 structures | Directionally improved for all ten readers and 35 of 39 structures | Benefit was broadly distributed within the study | Equivalent benefit for all future clinicians and rare variants | [Paper: PDF p. 4, Fig. 2B–C] |
| Procedure-selection analysis | AI affects a clinically relevant planning decision | Same readers and cases under both conditions | Accuracy 0.85 vs 0.77; error RR 0.65 | AI assistance improved agreement with the study reference | The selected procedure improves patient outcomes | [Paper: PDF p. 5, Fig. 3] |
| Error-type analysis | Benefit differs by decision error | Mistaken, insufficient and excessive resection | RR 0.27, 0.49 and 0.98, respectively | AI reduced some error types but not excessive resection | AI uniformly improves all planning errors | [Paper: PDF p. 5, Fig. 3D–E] |
| Corrected-versus-misled analysis | AI can both repair and introduce decisions | Reader decisions before and after AI support | Lobectomy: 68 corrected/19 misled; segmentectomy: 42 corrected/32 misled | Net benefit coexists with human–AI interaction risk | AI advice is harmless whenever overall accuracy increases | [Paper: Supplementary PDF, Fig. S3B] |
| Time analysis | AI reduces reader interpretation time | Within-reader planning time under both conditions | Median reduction 63 s | The AI representation reduced the timed reader task | Total end-to-end workflow was 63 s faster | [Paper: PDF p. 6, Fig. 4] |
| Confidence analysis | AI changes subjective certainty | Post-hoc confidence=100 versus <100 | Confident proportion increased; confidence correlated with accuracy | AI assistance was associated with greater reported confidence | Confidence was calibrated or caused accuracy improvement | [Paper: PDF p. 6, Fig. 4C–E] |

### 10.4 Usability and computation

- [Paper] AI reconstruction required 233.76 ± 75.08 seconds. [Paper: PDF p. 6]
- [Paper] Overall reader satisfaction was 99%. Fourteen of 1,400 evaluations were rated unsatisfactory: six because a lesion masked structures, four because of unsatisfactory distal branches, two because of artery–vein classification errors and two because of unclear display. [Paper: PDF p. 7]
- [Analysis] Satisfaction is a user rating of the complete reconstruction, not an independent technical-accuracy estimate.

## 11 Correct Interpretation of the Conclusions

### What the evidence supports

- [Paper] Within this simulated preoperative-planning study, AI-3D assistance improved surgeons' anatomical-identification and operation-procedure-selection performance and reduced reader planning time.
- [Paper] The direction of primary-endpoint improvement was consistent across all ten readers, all five lobes and most evaluated anatomical structures. [Paper: PDF p. 4]
- [Analysis] The results support the clinical task value of a human-in-the-loop 3D anatomical-assistance system under the studied conditions.

### What the evidence does not support

- [Analysis] It does not show that the AI system independently generated a correct surgical plan; the final judgments came from surgeons.
- [Analysis] It does not establish reduced bleeding, shorter operations, fewer complications or better long-term outcomes.
- [Analysis] The 99% satisfaction rate must not be reported as 99% reconstruction accuracy.
- [Analysis] An operation-procedure-selection accuracy of 0.85 is not equivalent to 85% accuracy for a complete surgical plan.
- [Analysis] The exploratory trends for uncommon variants, low-confidence cases and difficult cases are not confirmed indications for use.
- [Analysis] The timed reader benefit must be separated from the approximately 234-second reconstruction latency when discussing end-to-end efficiency.

### Bounded restatement

[Analysis] The study demonstrates that, among ten experienced thoracic surgeons evaluating 140 selected cases from three Chinese centres, access to the complete AI-3D system improved agreement with a retrospectively constructed expert reference for defined planning tasks; it does not demonstrate autonomous planning, prospective safety or patient-outcome benefit.

## 12 Limitations Explicitly Acknowledged by the Authors

| Limitation | Specific manifestation | Future direction proposed by the authors | Source |
|---|---|---|---|
| Planning improvement is not a patient outcome | Better anatomical identification does not directly establish less bleeding, shorter operations or fewer complications | Prospective studies and randomized trials incorporating perioperative outcomes | [Paper: PDF p. 7] |
| Rare variants were underrepresented | Performance for uncommon variants such as independent upper pulmonary vein or bronchus suis remains uncertain | Build and evaluate a dedicated rare-variant database | [Paper: PDF p. 7] |
| Procedure reference used a simplified margin rule | The rule required a resection margin at least as large as the nodule diameter, whereas ideal margins also depend on pathology and recurrence | Further evaluation incorporating pathological and outcome-related considerations | [Paper: PDF p. 7] |
| Beneficial subgroup analyses were exploratory | Larger effects for uncommon variants and low-confidence cases were not prespecified and may be underpowered | Larger, prespecified confirmatory studies | [Paper: PDF p. 7] |
| MRMC simulation incompletely represents clinical workflow | It may not capture interpretation sequence, workload, teamwork, consequences of error and other real-world dynamics | Future studies closer to real clinical deployment | [Paper: PDF p. 7] |

## 13 Critical Analysis

| [Analysis] Observation | Potential issue or alternative explanation | Why it matters | How to test it | Basis |
|---|---|---|---|---|
| The reference includes operative videos and records | The reference contains post-operative information unavailable during prospective planning | It is a strong anatomical oracle but not an input-matched expert preoperative plan | Build a second reference using only the same preoperative inputs available to readers and compare conclusions | [Paper: PDF p. 3, Fig. 1] |
| The study evaluates the complete assistance package | Clinical benefit cannot be attributed to any specific segmentation or rendering component | System-level success does not identify which module is necessary | Conduct controlled interface or component studies while keeping reader tasks constant | [Paper: PDF p. 8] |
| Entry criteria favour high-quality imaging | CT had to be high quality and ≤2 mm; prior surgery, trauma, poor imaging and trans-lobar invasion were excluded | Transportability to difficult routine scans and more complex patients is uncertain | Perform external validation stratified by acquisition quality and excluded clinical conditions | [Paper: PDF p. 8] |
| All readers were experienced attendings | Effects may differ for trainees, novices or surgeons in lower-volume centres | The result cannot be generalized to all potential users | Prespecify reader-experience strata in an external MRMC study | [Paper: PDF pp. 2–3] |
| The primary accuracy weights structures equally | Missing a critical vessel and missing a low-risk distal branch may have different consequences | An unweighted mean may not reflect clinical harm | Add a blinded, prespecified severity-weighted error analysis | Primary-endpoint definition [Paper: Supplementary PDF pp. 38–40] |
| Fig. 2 cites a Mann–Whitney test while Methods designate DBMH as primary | The hierarchy between the figure-level comparison and the MRMC-adjusted inference is not fully transparent | Ignoring reader–case dependence can yield overconfident inference | Report the DBMH effect estimate, variance components and figure-level descriptive test separately | [Paper: PDF p. 4, Fig. 2; Supplementary PDF pp. 38–40] |
| Sample-size descriptions appear inconsistent | The main text mentions a pilot effect of 0.13 followed by a “conservative effect size of 0.7”, whereas the supplement describes a planned effect of 0.08 | The apparent typo or ambiguity limits reproducibility of the power calculation | Clarify the intended effect size and reproduce the calculation from protocol assumptions | [Paper: PDF p. 8; Supplementary PDF pp. 40–41] |
| Confidence was dichotomized post hoc at exactly 100 | An extreme, non-prespecified threshold may exaggerate a binary contrast | Greater confidence is not equivalent to improved calibration | Analyse the full confidence scale with calibration curves and prespecified thresholds | [Paper: PDF p. 6, Fig. 4] |
| Many secondary and exploratory analyses were reported | Multiplicity may increase false-positive findings | Subgroup trends should remain hypothesis-generating | Prespecify a hierarchical testing strategy in a confirmatory study | [Paper: PDF pp. 4–7] |
| AI both corrected and misled readers | Net accuracy can conceal clinically important harmful transitions | A system with positive average benefit may still introduce severe errors | Report severity-weighted corrected-versus-misled transitions and adverse interaction cases | [Paper: Supplementary PDF, Fig. S3B] |
| Commercial involvement and proprietary implementation | Independent reproducibility and sponsor-independent performance remain uncertain | External validity is essential for clinical deployment claims | Conduct independent, multi-vendor or investigator-led external validation | [Paper: PDF p. 10] |

## 14 Knowledge Learned

### Agent-derived knowledge candidates

#### A. How to draw the main benchmark workflow

- [Analysis] Figure 1 depicts the evaluation workflow rather than the algorithm pipeline. For a benchmark paper, this may be more important than showing every neural-network component.
- [Analysis] The clearest visual backbone is: case pool → random sampling → independent reference → reader randomization → phase 1 → washout → crossover phase 2 → endpoint analysis.
- [Analysis] The figure should make three sources of independence visually explicit: the patient cohort, the reference-setting experts and the evaluated readers.

#### B. How to organize the results figures

- [Analysis] The paper follows a reusable hierarchy: overall effect → individual-reader consistency → task or structure breakdown → error mechanism → efficiency and confidence.
- [Analysis] Reporting absolute differences, relative error risks and 95% confidence intervals together is more informative than presenting p values alone.
- [Analysis] Per-reader plots answer whether the result is driven by a few users; heatmaps and error-type plots answer where and why performance changes.
- [Analysis] Showing a non-improved outcome—excessive resection, RR 0.98—defines the capability boundary and strengthens credibility.

#### C. Transferable study-design concepts

- [Analysis] Fully crossed MRMC studies can isolate the effect of adding an AI tool while modelling both reader and case variability.
- [Analysis] Missing answers should remain visible through conservative main analyses and sensitivity analyses rather than disappearing from the denominator.
- [Analysis] Corrected-versus-misled transitions are clinically more interpretable than net accuracy alone.
- [Analysis] Standalone model validity, clinician-assistance benefit and patient-outcome benefit are separate evidentiary layers.

## 15 Connections to related research

[Analysis] This paper can inform evidence organization and figure design in related research; its tasks, data, metrics and conclusions cannot be transferred directly to other application domains.

## 16 Open questions

[Analysis] Future work should validate the reported method on independent datasets and report uncertainty, failure cases, and distribution shifts transparently.
