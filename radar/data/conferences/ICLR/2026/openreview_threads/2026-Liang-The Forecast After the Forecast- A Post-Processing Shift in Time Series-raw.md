# The Forecast After the Forecast: A Post-Processing Shift in Time Series — OpenReview Raw Thread

- Forum: https://openreview.net/forum?id=syfWdclGE1
- PDF: https://openreview.net/pdf?id=syfWdclGE1
- Section: 二、时间序列预测：分布鲁棒、多变量建模与后处理优化
- Zhihu score: 6.0
- Venue status: ICLR 2026 Poster

## Submission metadata
- Authors: Daojun Liang, Qi Li, Yinglong Wang, Jing Chen, Hu Zhang, Xiaoxiao Cui, Qizheng Wang, Shuo Li
- Primary area: learning on time series and dynamical systems
- Keywords: Time Series Forecasting, Post-Processing, Fine-Tuning

## Abstract
Time series forecasting has long been dominated by advances in model architecture, with recent progress driven by deep learning and hybrid statistical techniques. However, as forecasting models approach diminishing returns in accuracy, a critical yet underexplored opportunity emerges: the strategic use of post-processing. In this paper, we address the last-mile gap in time-series forecasting, which is to improve accuracy and uncertainty without retraining or modifying a deployed backbone. We propose $\delta$-Adapter, a lightweight, architecture-agnostic way to boost deployed time series forecasters without retraining. $\delta$-Adapter learns tiny, bounded modules at two interfaces: input nudging (soft edits to covariates) and output residual correction. We provide local descent guarantees, $O(\delta)$ drift bounds, and compositional stability for combined adapters.
Meanwhile, it can act as a feature selector by learning a sparse, horizon-aware mask over inputs to select important features, thereby improving interpretability.
In addition, it can also be used as a distribution calibrator to measure uncertainty. Thus, we introduce a Quantile Calibrator and a Conformal Corrector that together deliver calibrated, personalized intervals with finite-sample coverage.  
Our experiments across diverse backbones and datasets show that $\delta$-Adapter improves accuracy and calibration with negligible compute and no interface changes.

## Reviews
### Reviewer_gci4
- summary: This paper introduces δ-Adapter, a lightweight and model-agnostic post-processing framework to improve deployed time series forecasting models without retraining them. The method learns small, bounded adjustments at two interfaces: "input nudging" to refine covariates and "output residual correction" to adjust predictions. The framework is extended into three applications: a feature selector for interpretability, a quantile calibrator, and a conformal calibrator for reliable uncertainty quantification. Extensive experiments on various models and datasets validate that δ-Adapter effectively boo
- strengths: 1.  **Practicality and Novelty**: The paper addresses the critical real-world problem of updating deployed models in a computationally cheap manner. The δ-Adapter is a practical "plug-and-play" solution compared to costly alternatives like full retraining or fine-tuning.

2.  **Methodological Completeness**: The framework is versatile, being applicable to different backbone forecasting model. It is also comprehensive, addressing crucial aspects like interpretability (feature selection) and relia
- weaknesses: 1.  **Limited Comparison with Alternative Post-Processing Methods:** While the paper positions δ-Adapter as a post-processing technique, the primary comparisons are against fine-tuning or continue-training the backbone model. However, there is a significant body of work on post-processing and test-time adaptation for time series forecasting designed to handle concept or distribution shifts. This includes methods for both batch-training settings (e.g., [SOLID](https://arxiv.org/abs/2310.14838)、[TAFAS](https://arxiv.org/abs/2501.04970)) and online settings (like FSNet and OneNet, mentioned in the paper's related works). An experimental comparison against these direct alternatives is necessary to properly situate the δ-Adapter's advantages; without it, the claims of superiority are not fully convincing.
2.  **Insufficient Motivation:** The motivation presented is not fully developed. The paper's opening question—"Can we keep the strong forecaster intact and learn only a tiny, post-hoc mod
- questions: 1.  **The choice of hyperparameter δ**: In the experiments, δ is set to 0.1 for most datasets but 0.01 for the ETT datasets. Was this value selected empirically, or was there a systematic tuning process (e.g., grid search on a validation set)? Does the optimal value of δ correlate with properties of the backbone model (e.g., complexity) or the dataset (e.g., noise level, degree of concept drift)?

2.  **The online learning setup**: In Figure 2 and Table 6, you demonstrate superior performance under an online training setting. Could you please provide more details on this online experimental setup? Specifically, how is data streamed to the adapter (e.g., sample-by-sample, mini-batches), and how does this setup simulate a real-world scenario where new data arrives continuously?

3.  **The ch
- rating: 4 | confidence: 4

### Reviewer_5yqn
- summary: This paper introduces sigma-Adapter, a lightweight post-processing framework for improving time series forecasting without retraining the backbone model. The approach works by learning small bounded corrections at two interfaces: (1) input nudging (soft edits to covariates) and (2) output residual correction. The authors provide theoretical guarantees for local descent and stability and demonstrate feature selection capabilities through learnable masks, and introduce two distributional correctors (Quantile and Conformal calibrators). The experiments across multiple datasets and backbone models
- strengths: The main strengths of the paper include,
1. The post-processing approach is a well-motivated solution for real-world deployments where retraining large models is costly. The ability to improve frozen forecasters is important and useful problem to tackle. 
2. The paper provides rigorous theoretical analysis for several algorithms: Local descent guarantees (Theorems 2 & 3), Compositional stability for combined adapters (Proposition 3.2) etc.
3. The authors compared against diverse backbones (DistP
- weaknesses: The main weakness of the paper include,

1. The proposed Input/output adapters approach is conceptually similar to existing adapter methods in NLP. The theoretical results (gradient descent, Lipschitz stability) are relatively standard. The main contribution does not appear to be novel as the claims in the paper and looks like an application of the NLP concept to time series.
2. Some important ablation studies such as the impact of adapter architecture (MLP depth, width etc), effect of different sigma values across datasets are missing. 
3. The comparison with other post-processing method (e.g., calibration techniques) and adapter approaches are not presented; The comparison with lightweight fine-tuning methods (e.g., LoRA for time series) across multiple pre-trained models is missing; The LoRA comparison in Figure 8(c) is limited to one model (Sundial) and shows high variance but needs more investigation. 
4. Discussion on fine-tuning/adaptation time across different adapter approache
- questions: 1. Can you compare against other adapter approaches available in time series literature and also compare with adapters used in NLP literature?
2. Can you have thorough discussion on the comparison with LoRA method and investigation on high variance?
3. Can you compare against few other pre-trained models like TabPFN-TS to validate the claims made are generalizable across pre-trained models?
- rating: 6 | confidence: 3

### Reviewer_gkGB
- summary: This paper presents an adapter-based finetuning method for pretrained forecasting models. The paper proposes input and output-based adapters in two forms: additive and multiplicative. The authors provide theoretical results for the stability and improvement under certain conditions with respect to the base model.  Finally, the authors expose how to utilize their adapters as calibration methods for models that only offer fixed-point predictions.
- strengths: - Overall, I think this is a good paper. The presentation is clear and the theory is solid as far as I can tell.
- The presented experiments consistently show the improvement of input and output adapters. 
- Benchmarks look reasonable within popular datasets from the time series literature.
- weaknesses: - Some of the models are relatively old and would not be considered SOTA at the current time (e.g. Autoformer). I would suggest including models like PatchTST, Non-stationary Transformer, TimesNet or TimeMixer.
- Additive vs multiplicative: 
- Reports metrics in Table 2 are  averaged across lenghts. I understand the difficulty of reporting metrics across many horizons, but in my opinion, this makes it harder to interpret the effect over prediction lengths, over which errors may differ significantly.

**Typos and minor comments**
- L132: "Obviously". This can be dropped :) 
- Table 2 Exange (also in the appendix table). caption: "veraged"
- L64: Despite adapter is simplicity
- questions: - L461-463: Could the authors elaborate more on why this type of input/output adapter is desirable over a LoRA style adapter?
- How does additive vs multiplicative updates compare empirically? It seems the experiments mostly focus on additive adapters.
- Why not report results for Ada X+y adapters together (Tables 1 and 2)?
- rating: 8 | confidence: 4

### Reviewer_Fzqc
- summary: The paper proposes **δ-Adapter**, a lightweight and architecture-agnostic framework that improves frozen time-series forecasting models through post-processing rather than retraining. It introduces two modules: **input nudging**, which softly edits covariates before inference, and **output residual correction**, which refines predictions after inference. The method provides theoretical guarantees of local descent, bounded drift, and compositional stability. Additionally, the authors design a **feature-selector adapter** that identifies influential input features and **quantile/conformal calibr
- strengths: The paper’s main strength lies in its original and practical reformulation of time-series improvement as a post-processing problem rather than a model-design or retraining task. This shift in perspective is both creative and highly relevant to real-world forecasting systems, where retraining large backbones is often infeasible. The proposed δ-Adapter is simple yet elegant, introducing bounded input and output modules that deliver measurable gains without altering the base model. Theoretical sect
- weaknesses: While the paper presents a strong theoretical foundation and an appealing practical idea, several areas could be improved to strengthen its impact and clarity.

First, the experimental evaluation, though broad in dataset coverage, lacks comparative depth. The study primarily benchmarks δ-Adapter against frozen and fine-tuned baselines, but it omits comparisons to parameter-efficient adaptation methods such as LoRA, adapters, or residual fine-tuning strategies that have been explored in related forecasting and NLP contexts. Including such baselines would better position δ-Adapter within the broader adaptation literature and clarify its relative advantages.

Second, while the theoretical analysis is thorough, the empirical link to these guarantees remains weak. The paper could provide visual or quantitative evidence of stability, such as loss landscapes or δ–performance trade-offs, to demonstrate how the theory manifests in practice.

Third, the related work section should be expanded to
- questions: 1. **Comparison to Test-Time Adaptation (TTA) Methods**.
   How does δ-Adapter conceptually and empirically differ from recent TTA approaches that also adapt frozen forecasters at inference time (e.g., Kim et al., AAAI 2025; Medeiros et al., 2025; Grover & Etemad, ICML 2025)? Since these methods share similar goals such as robustness to non-stationarity and post-hoc improvement, please clarify what specific challenges δ-Adapter addresses that are not tackled by gradient-based or parameter-efficient TTA methods.

2. **Choice and Sensitivity of δ**.
   The theoretical analysis emphasizes δ as a small trust-region parameter controlling stability. How sensitive are results to δ in practice, and how should it be chosen for new datasets or models? Could adaptive δ-scheduling be beneficial?

3. *
- rating: 6 | confidence: 4

## Author comments / rebuttal
### Reviews and Reviewer-Author Discussion Summary
Dear ACs and Reviewers,

Thank you for your valuable contributions to our work. We declare that **we have complied with all regulations of ICLR 2026**, and **we appreciate the newly assigned AC** taking the time to review our submission.

To assist the AC in this transition, we provide a summary of the reviews, our major revisions, and the resulting positive momentum.

---
**1. Current Status: Positive Trajectory**

   We are grateful that the **`initial reviews were positive`**, recognizing the work's practicality and theoretical rigor. Importantly, during the discussion period, we addressed all major concerns, leading to `improved sentiment and scores`:
-  **Score Increase:** Reviewer **5yqn** raised their score from **6 $\to$ 8** (Refer to Reviewer 5yqn’s reply and the associated time).
-  **Consensus:** The average rating improved from **6 $\to$ 6.5**, with strong support for the paper's novelty and rigorous empirical validation.

---
**2. Key Strengths (Consensus among Reviewers)**
*   **Novelty**:
    *    `Innovative reformulation of time-series improvement as a post-processing task.`

    *    `Addressing critical aspects like interpretability (feature selection) and uncertainty estimation.`
    > All 4 reviewers recognized this point: **gci4: Strength 2; 5yqn: Strength 3; gkGB: Strength 1; and Fzqc: Strength 3**.
*   **Practical & Efficient**: `The method offers a cost-effective, plug-and-play solution, making it highly practical for real-world deployment.`
> All 4 reviewers recognized this point: **gci4: Strength 1; 5yqn: Strength 1;  gkGB: Strength 1; and Fzqc: Strengths 1-2**.
*   **Rigorous Theory**: `Backed by proofs for local descent and compositional/drift stability.`
> All 4 reviewers recognized this point: **gci4: Strength 3; 5yqn: Strength 2; gkGB: Strength 1; and Fzqc: Strength 4**.
*   **Strong Performance**: `Consistent improvements across diverse backbones and benchmarks.`
> All 4 reviewers recognized this point: **gci4: Strength 3; 5yqn: Strength 4; gkGB: Strength 3; and Fzqc: Strength 6**.
- **Clarity**: `The work is well-structured and elegantly reformulated with intuitive explanations and clear figures.`
> Attributed to Reviewers **gkGB: Strength 1 and Fzqc: Strength 5**.

---
**3. Major Concerns & How We Resolved Them**

We implemented substantial changes based on feedback, which satisfied the reviewers:
* **Comparison with SOTA & Baselines** (Addressed: **gci4: W1; 5yqn W3, Q1&3; Fzqc: Q1**)
  * **Action:** Added extensive comparisons with **2 Test-Time**, **2 Fine-Tuning**, and **2 Online Learning** methods across 8 datasets (**Table 2 & 10**).
  * **Result:** Our method consistently outperforms all adaptation baselines, `reducing error by significant margins` (e.g., **~14% reduction** on Exchange).

* **Comparison vs. LoRA/NLP Methods** (Addressed: **5yqn: W1, Q2; gkGB: Q1; Fzqc: Q4**)
  * **Action:** Conducted LoRA-like methods on DistPred and iTransformer backbones (**Fig. 2 & Table 5**).
  * **Result:** While LoR

### Response to Reviewer Fzqc [Part 4]: Supplementary to Q5
**Q5: Practical Deployment Considerations, e.g., training cost, latency overhead, and implementation effort.**

A5-Part 2: **Training cost and latency overhead.**

The $\delta$-Adapter is designed to be extremely lightweight. It is implemented as a 2-layer MLP (specifically, for **Sundial (128M)** and **TabPFN (48M)**, the adapter adds only approx. 1.5M-3M parameters depending on the horizon). Compared to the backbone model, the adapter introduces **less than 2%-6%** additional parameters, validating the lightweight claim.

A4-Part 2: **Training cost and latency overhead** 

We compared the wall-clock time of our method against state-of-the-art test-time adaptation (TTA) methods. As shown in the table below (and Table 6 in the revision), while online adaptation naturally incurs overhead compared to a static offline model (which performs no updates), our proposed method **(Ada-X+Y) is consistently the fastest among all adaptive methods**. When used offline, the additional computational overhead of $\delta$-Adapter is negligible.

*Table 6: Time (S) and memory (MB) of adapters (backbone is TabPFN) and online methods.*
|Offline ~48M||+Ours ~3M|||+SOLID ~0.5M|||+TAFAS ~6M|||+OneNet ~3M|||+FSNet ~2M|||
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Time|Memory|Train|Test|Memory|Train|Test|Memory|Train|Test|Memory|Train|Time|Memory|Train|Time|Memory|
|281|1840|**392**|**395**|1983|511|667|2401|603|861|3468|693|471|1512|621|485|1504|
|307|1848|**386**|**379**|2132|481|624|2423|589|895|3790|681|445|1537|618|472|1531|
|326|1852|**385**|**415**|2622|484|593|2446|583|1152|4186|631|452|1559|599|466|1517|
|351|1856|**369**|**431**|3102|505|398|2501|916|1803|6809|530|465|1567|554|458|1526|

It is worth noting that for some methods in above table, due to reasons such as backprop gradients, the time is related to the number of sample updates, i.e., the longer the prediction length, the fewer the samples, and the shorter the time.

A4-Part 3: Implementation Details

$\delta$-Adapter can be divided into input editing (Ada-X), output correction (Ada-Y), and their composite forms (Ada-X+Y).
The forward pass is:
$$\hat Y=F(X + \delta A_{\theta}^{in}(X)) \qquad (1)$$
$\tilde Y = \hat Y + \delta A_{\theta}^{out}(\hat Y)\qquad(2)$

- - For Ada-X, gradients flow from the loss through the backbone $F$, then through Ada-X (Eq. 2).
- - For Ada-Y, gradients flow from the loss through Ada-Y (Eq. 2), then through the backbone $F$.
-- For Ada-X+Y, Ada-X and Ada-Y are **trained jointly** in an end-to-end manner, not sequentially. We minimize **a single combined loss** $\mathcal{L}$ over the union of parameters $A_{\theta}^{in}$ (Ada-X) and $A_{\theta}^{out}$ (Ada-Y). 
During the backward pass, gradients flow from the loss through Ada-Y (Eq. 2), then through the backbone $F$, and finally to Ada-X (Eq. 1). This ensures that Ada-X learns input perturbations that specifically help the backbone produce features that Ada-Y can best correct.

Experimental Setup:

### Response to Reviewer gci4 [Part 4]
> **Q3: The choice between the Quantile Calibrator (QC) and Conformal Calibrator (CC): The paper proposes two effective uncertainty calibrators, QC and CC. Is there recommendations for us on when to choose one over the other, when faced a new real-world dataset?**

A7: Both modules turn a frozen point forecaster into a calibrated probabilistic predictor, but they are aimed at slightly different desiderata (**updated in Appendix C.7 of the new version**):
- - QC directly learns horizon-wise conditional quantiles as bounded offsets around the point forecast, which produces a smooth quantile function over multiple levels without assumptions about the underlying distribution.
- - CC learns only a heteroscedastic scale function and combines it with normalized-residual conformal prediction on a held-out calibration set, yielding symmetric but input-dependent intervals with finite-sample marginal coverage under exchangeability.

Empirically, both variants achieve strong coverage, but QC tends to produce marginally wider and more conservative bands, while CC attains similar coverage with somewhat tighter intervals (**see Figs. 5, 6 & 11 in the new version**). 
For a new real-world dataset, our recommendation is therefore:
- - If strict coverage guarantees are the main requirement, CC is preferable, since the conformal step provides finite-sample marginal coverage at the target level.
- - If one needs a rich predictive distribution or multiple coverage levels from a single model, QC is more convenient, as it directly returns a full quantile curve while remaining non-parametric w.r.t. the underlying distribution.

We have carefully updated the reply again.
We trust that these clarifications regarding the distinct advantages of our post-hoc approach adequately address the reviewers' concerns, and **we respectfully invite a re-evaluation of the paper in light of these significant improvements.** Many thanks!

### Author comment
We sincerely thank you for your time in re-evaluating our paper and for raising the score. We are glad that our response and revisions have effectively addressed your concerns. Your constructive feedback has significantly helped us strengthen the paper.

### Response to Reviewer gci4 [Part 3]
> **Q1: The choice of hyperparameter $\delta$: In the experiments, $\delta$ is set to 0.1 for most datasets but 0.01 for the ETT datasets. Was this value selected empirically, or was there a systematic tuning process (e.g., grid search on a validation set)? Does the optimal value of $\delta$ correlate with properties of the backbone model (e.g., complexity) or the dataset (e.g., noise level, degree of concept drift)?**

A5-Part 1: **Selection process and robustness**

Yes, $\delta$ is related to the properties of the dataset (e.g., noise level, degree of concept drift). We did not perform an exhaustive grid search for every experiment. Instead, we established a simple, robust heuristic based on the properties of the dataset (the degree of distribution shift and volatility).
- - $\delta = 0.1$ (High Drift): For datasets with severe concept drift or high volatility (e.g., Traffic, Electricity), we set  $\delta = 0.1$ to allow the adapter to correct significant shifts in the data generating process.
- - $\delta = 0.01$ (Low Drift): For datasets with smoother, more stationary patterns (e.g., ETT datasets, which record transformer temperatures), we set $\delta = 0.01$ since these signals are physically constrained and stable. Thus, a smaller $\delta$ prevents the adapter from overfitting to noise.

A5-Part 2: **Correlation with backbone vs. dataset**

For $\delta$-Adapter, we found that the optimal $\delta$ correlates strongly with the dataset but is largely agnostic to the backbone model. Since $\delta$-Adapter learns to correct the residuals, the magnitude of the required correction depends on the nature of the data drift rather than the complexity of the pre-trained forecaster. This is a key advantage, as it allows users to swap backbones without re-tuning $\delta$.

A5-Part 3: **Sensitivity analysis**

We conducted an ablation study to verify this heuristic.  As shown in the tables below, a better value of $\delta=0.1$ might yield better results  (**updated in Appendix C.10 of the new version**).
|+0.1X||x0.1X||x0.2X||+0.1Y||x0.1Y||x0.2Y||+0.1(X&Y)||x0.1(X&Y)||x0.2(X&Y)||
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Val|Test|Val|Test|Val|Test|Val|Test|Val|Test|Val|Test|Val|Test|Val|Test|Val|Test|
|0.418|0.166|0.427|0.168|0.425|0.169|0.421|0.168|0.415|0.165|0.413|0.167|0.413|0.160|0.416|0.162|0.411|0.162|

|$\delta$=|0.01|0.05|0.1|0.2|0.3|
|:-:|:-:|:-:|:-:|:-:|:-:|
|ELC|0.163|0.161|0.160|0.160|0.161|
|Weather | 0.171  | 0.170  | 0.172  |0.177|0.182|
|Traffic|0.443|0.439|0.435|0.432|0.433|

The results below demonstrate two key findings:
- - Heuristic Holds: Datasets like Traffic benefit from higher $\delta$ (0.1 or 0.2), while ELC/Weather are stable around 0.1.
- -  Performance is Robust: The performance sensitivity is low. e.g., on the Weather dataset, the difference between $\delta=0.01$ and $\delta=0.1$ is negligible ($0.001$ MSE). This confirms that $\delta$-Adapter does not require precise, computationally expensi

### Response to Reviewer Fzqc [Part 3]
Q5: Practical Deployment Considerations, e.g., training cost, latency overhead, and implementation effort.

A5-Part 1: The training/test time, parameters and memory are:

||iTransformer||+Ours ~3M||+SOLID ~0.5M||+TAFAS ~6M||OneNet ~3M||FSNet ~2M||
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Length|Time (S)|Memory (MB)|Time|Memory|Time|Memory|Time|Memory|Time|Memory|Time|Memory|
|96|38|460|**167**|1696|554|476|852|2026|444|722|231|704|
|192|43|462|**175**|2402|497|483|865|2270|406|738|192|700|
|336|47|463|**201**|3312|458|486|1104|2648|363|740|194|700|
|720|60|464|**217**|5792|293|502|2142|5672|275|742|163|700|

The above table shows that $\delta$-Adapter is the most time-efficient, it is consistently faster than other methods across all horizons: Taking the offline method as a benchmark, our proposed method **(Ada-X+Y) achieves the fastest speed**. Therefore, $\delta$-Adapter has more deployment advantages due to its simplicity and powerful nature.

We trust that these clarifications regarding the distinct advantages of our post-hoc approach adequately address the reviewers' concerns. Many thanks!

### Response to Reviewer Fzqc [Part 2]
---
- **Q2: Choice and Sensitivity of $\delta$.**

A2-Part 1: **Sensitivity of $\delta$.** Ablation studies of $\delta$ are shown in below. It can be found that when $\delta\approx0.1$, a decent performance can be achieved.
|$\delta$=|0.01|0.05|0.1|0.2|0.3|
|:-:|:-:|:-:|:-:|:-:|:-:|
|ELC|0.163|0.161|0.160|0.160|0.161|
|Weather | 0.171  | 0.170  | 0.172  |0.177|0.182|
|Traffic|0.443|0.439|0.435|0.432|0.433|

A2-Part 2: **Choice of $\delta$.** $\delta$ is related to the properties of the dataset (e.g., noise level, degree of concept drift). In our work, we divided the datasets into two categories: one with severe concept drift ($\delta=0.1$, e.g., Traffic, Weather, etc.) and the other with non-severe concept drift ($\delta=0.01$, e.g., ETT, etc.). For datasets with severe concept drift, setting $\delta=0.1$ is sufficient. As shown in the table below (Page 27, Table 12), a better value of $\delta=0.1$ might yield better results. In our paper, we only reported the two settings ($\delta$=0.1 or 0.01).
|+0.1X||x0.1X||x0.2X||+0.1Y||x0.1Y||x0.2Y||+0.1(X&Y)||x0.1(X&Y)||x0.2(X&Y)||
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Val|Test|Val|Test|Val|Test|Val|Test|Val|Test|Val|Test|Val|Test|Val|Test|Val|Test|
|0.418|0.166|0.427|0.168|0.425|0.169|0.421|0.168|0.415|0.165|0.413|0.167|0.413|0.160|0.416|0.162|0.411|0.162|

A2-Part 3: **Could adaptive $\delta$-scheduling be beneficial?** Adaptive $\delta$-scheduling is definitely beneficial and a very promising direction. However, a systematic study of such policies is orthogonal to our main contributions. We believe it is an interesting extension that could further exploit the $\delta$-Adapter framework.

- **Q3: Theoretical–Empirical Link, e.g., $\delta$ vs. loss curves or visualization of stability bounds.**

A3: Below, we present the performance changes of additive and multiplicative adapters on different datasets over epochs (the blank is due to early stopping). In **Figure 9 (Page 24)** of the new version, we visualize the changes in validation and test losses of $\delta$-Adapter across different datasets.
||Original|1|2|3|4|5|6|7|8|9|10|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|ELC (Add)|0.167|0.161|0.158|0.159|0.159|0.159|0.159|0.159|0.159|0.159|0.159|
|ELC (Mul)|0.167|0.162|0.161|0.160|0.159|0.159|0.159|0.159|0.159|||
|Traffic (Add)|0.463|0.460|0.455|0.453|0.452|0.451|0.451|0.451|0.451|0.451|0.451|
|Traffic (Mul)|0.463|0.459|0.454|0.451|0.449|0.448|0.448|0.448|0.448|0.448||
|Weather (Add)|0.178|0.162|0.161|0.161|0.161|0.161|0.161|0.161|0.161|0.161||
|Weather (Mul)|0.178|0.168|0.166|0.166|0.165|0.165|0.165|0.165|0.165|0.165|0.165|

These experiments show that the loss curve of the $\delta$-Adapter gradually decreases with epochs and has stable and consistent boundaries. Meanwhile, as shown in the table in A2-Part 2, our composite adapter (X&Y) can achieve better performance (Stability Analysis of Section 3), which also proves the robustness of the $\delta$-Adapter and

### Response to Reviewer Fzqc [Part 1]
We would like to sincerely thank Reviewer Fzqc for recognition of our strong theoretical foundation and an appealing practical idea, as well as for providing the insightful review and constructive suggestions. **We have incorporated the weaknesses into the questions block to provide an overall response.** Below are the responses point by point:

- **Q1: Comparison to Test-Time Adaptation (TTA) Methods.**

A1-Part 1: **Differ from recent TTA approaches:** The existing TTA approaches aim to mitigate test-time concept drift via selective layer retraining (SOLID), online linear adapter updates (TAFAS) and its follow-ups PETSA (auxiliary loss) and DynaTTA (dynamic gating), and parallel forecaster combine (ELF), layer-wise adjustment and memory (FSNet), and dynamic model selection (OneNet). These methods are either based on linear adapters, parallel fusion, or overall fine-tuning; and, they do not consider the impact of label leakage ([Liang et al. 2024](https://arxiv.org/abs/2412.00108), [YA Lau et al. 2025](https://openreview.net/pdf?id=I0n3EyogMi)). *$\delta$-Adapter can perform non-linear adaptation on both input and output, with good theoretical guarantees. And it only relies on the most recent sample for fast updates. In addition, it can be used as a feature selector or a corrector.*

A1-Part 2: **Differ from fine-tuning approaches in NLP:** LoRA-style adapters in NLP tend to lead to high performance variance, *since the output range is not fixed (classification task, with probabilities in 0-1), the model tends to exhibit high variance (parameter changes directly affects the outcomes)*, as shown in Figure 8(c).  However, $\delta$-Adapter differs from existing adapters in NLP in the following aspects:
- - $\delta$-Adapter is a post-hoc I/O editor of black-box forecasters. But, NLP adapters (e.g., parameter-efficient fine-tuning in Transformers) are typically inserted inside each layer and trained jointly with full access to the backbone internals.
- - NLP adapters do not modify the I/O data themselves, but rather add additional infos/params to them or calculates auxiliary losses or penalties to achieve domain alignment. In contrast, $\delta$-Adapter places more emphasis on the gains brought to the model by editing or correcting the I/O data itself.

Alternatively, applying $\delta$-Adapter to NLP is also a promising attempt. We have added comparisons in Appendix A of the new version.

A1-Part 3: **Compared the post-processing methods.** For fair comparison, we removed label leakage [Liang et al. 2024](https://arxiv.org/abs/2412.00108) and [YA Lau et al. 2025](https://openreview.net/pdf?id=I0n3EyogMi). Our experiments show that our method achieves the lowest error on every dataset across all backbones (**Tables 2 & 10 in new version**).
||DistPred|+SOLID|+TAFAS|+LoRA|+Ours|iTransformer|+SOLID|+TAFAS|+LoRA|+Ours|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|ELC|0.182|0.182|0.182|0.18|**0.175**|0.19|0.19|0.19|0.186|**0.18**|
|ETTh1|0.461|0.46|0.476

### Response to Reviewer gkGB
We thank the Reviewer gkGB for the positive evaluation and valuable comments. Below are the responses point by point:

- **W1: Some of the models are relatively old.**

A1：We have introduced the mentioned works in the new version and selected the models with SOTA performance among them (PatchTST and TimeMixer) as the backbone to test $\delta$-Adapter (**Page 9 and Table 5 of the new version**). The results are as follows:
||PatchTST||+ Ada-X+Y||+ Ada-X$\times$Y||TimeMixer||+ Ada-X+Y||+ Ada-X$\times$Y||
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
||MSE|MAE|MSE|MAE|MSE|MAE|MSE|MAE|MSE|MAE|MSE|MAE|
|ELC|0.167|0.252|**0.159**|0.245|**0.159**|0.246|0.145|0.243|**0.143**|0.241|**0.143**|0.241|
|Weather|0.178|0.219|**0.161**|0.22|*0.165*|0.224|0.168|0.216|*0.166*|0.214|**0.164**|0.214|
|Traffic|0.463|0.297|*0.451*|0.292|**0.448**|0.29|0.475|0.317|**0.465**|0.307|*0.467*|0.31|

Obviously, after adding the $\delta$-Adapter to PatchTST and TimeMixer, their performance has been significantly improved.

- **W2: The average indicators in Table 2 make it difficult to explain the impact of predicted length.**

A2: Table 2 is the average of Table 9 (new version) over multiple prediction lengths. We have added a link to Table 9 in Table 2 to make it easier to explain the impact on prediction lengths.

- **W3: Typos and minor comments.**

A3: Thanks. We have corrected the mentioned contents.

> **Q1: L461-463: Could the authors elaborate more on why this type of input/output adapter is desirable over a LoRA style adapter?**

A4: LoRA-style adapters tend to lead to high performance variance, as shown in Figure 8(c) of our paper. This phenomenon occurs because LoRA-style adapters are generally used for classification (NLP), where the output range of the model is fixed (probabilities in 0-1), so the model is less likely to collapse. However, when LoRA is applied to regression, *since the output range is not fixed, the model tends to exhibit high variance (parameter changes directly affects the outcomes)*. In such cases, it is necessary to carefully select hyperparameters such as the learning rate to ensure that LoRA is fine-tuned within the original output space, which is not easy.

On the contrary, because $\delta$-Adapter directly limits the editing range of I/O, it is insensitive to the learning rate, and is easy to converge and has low variance, as shown in Fig. 8(b).
In summary, the benefits of the post-processing module include:
- - It is a plug-and-play, model-agnostic lightweight module that can bring significant performance gains;
- - Freezing backbone avoids catastrophic forgetting and robust to overfitting, preserves production hardening and governance;
- - Training a tiny adapter is fast and data-efficient, even with short labeled histories or tight retraining windows;
- - It can be metric-aware, enabling application-aligned calibration without touching backbone.

> **Q2: How does additive vs multiplicative updates compare empirically? It seems 

### Response to Reviewer 5yqn [Part 3]
> **Q3: Can you compare against few other pre-trained models like TabPFN-TS to validate the claims made are generalizable across pre-trained models?**

A7: Yes, we used TabPFN and TimesFM as frozen black-box models to conduct zero-shot testing on various datasets (**in Page 27 of the new version**). For comparison, we corrected the output results of these black-box models by adding Ada-Y. As shown in the table below, it can be found that after adding Ada-Y, the prediction error of the model is significantly reduced, which further proves the effectiveness of the proposed method.

||Traffic|Weather|ELC|Exchange|ETTh1|ETTh2|ETTm1|ETTm2|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|TabPFN|0.367|0.875|0.115|0.129|0.129|0.180|0.037|0.114|
|Ada-Y|**0.342**|**0.552**|**0.089**|**0.096**|**0.095**|**0.171**|**0.034**|**0.103**|
|TimesFM|0.211|0.168|0.084|0.239|0.029|0.135|0.028|0.267|
|Ada-Y|**0.196**|**0.157**|**0.081**|**0.215**|**0.024**|**0.104**|**0.025**|**0.223**|

We hope these responses adequately address your concerns. Thanks.

### Response to Reviewer 5yqn [Part 2]
- **W3: Comparison with other post-processing methods, e.g., calibration techniques and LoRA.**

A3: We compared recent post-processing methods, which aim to mitigate test-time concept drift via selective layer retraining (SOLID), online adapter updates (TAFAS),  auxiliary loss (PETSA), layer-wise adjustment and memory (FSNet), and dynamic model selection (OneNet). However, according to works by [Liang et al. 2024](https://arxiv.org/abs/2412.00108) and [YA Lau et al. 2025](https://openreview.net/pdf?id=I0n3EyogMi), the above methods have used future labels to some extent, causing label leakage in long-term forecasting, where future ground truth is adopted in advance for adaptation. For fair comparison, we removed label leakage (it may cause performance degradation of some adapters):

||DistPred|+SOLID|+TAFAS|+LoRA|+Ours|iTransformer|+SOLID|+TAFAS|+LoRA|+Ours|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|ELC|0.182|0.182|0.182|0.18|**0.175**|0.19|0.19|0.19|0.186|**0.18**|
|ETTh1|0.461|0.46|0.476|0.454|**0.451**|0.454|0.458|0.477|0.448|**0.449**|
|ETTh2|0.39|0.391|0.402|0.385|**0.379**|0.388|0.393|0.448|0.384|**0.377**|
|ETTm1|0.412|0.406|0.411|0.407|**0.396**|0.417|0.414|0.42|0.414|**0.403**|
|ETTm2|0.285|0.285|0.288|0.281|**0.274**|0.3|0.298|0.304|0.293|**0.29**|
|Exange|0.35|0.347|0.363|0.336|**0.297**|0.383|0.376|0.392|0.376|**0.316**|
|Traffic|0.453|0.453|0.455|0.449|**0.44**|0.475|0.475|0.476|0.468|**0.461**|
|Weather|0.256|0.255|0.256|0.251|**0.242**|0.259|0.257|0.259|0.255|**0.244**|

Our experiments show that our method achieves the lowest error on every dataset across all backbones (**Tables 2 & 10 in new version**).

- **W4: Discussion different adapters and comparison against wider range of pretrained models.**

A4: The discussion on $\delta$-Adapter and NLP adapters can be found in **A1**, and the comparison among $\delta$-Adapter and other adapter-based methods on different pre-trained models can be found in **A3** (pre-trained models are DistPred, iTransformer) and **A7** (pre-trained model is TabPFN-TS). The revisions of the paper include the Introduction, Experiments, and Recent work sections. These are also included in the Introduction, Experiments, and Related work sections of the new version PDF.

---

> **Q1: Can you compare against other adapter approaches available in time series literature and also compare with adapters used in NLP literature?**

A5: We compared recent adapter approaches in time series, including SOLID, TAFAS (follow-up methods like PETSA and DynaTTA perform similarly to TAFAS), and LoRA-style methods in NLP, in the above **A3**. It shows that our method achieves the lowest error on every dataset across all backbones (**Tables 2 & 10 in new version**). Furthermore, we discussed the differences between $\delta$-Adapter and the adapters in NLP in **A1**, and emphasized this in the Introduction (Page 1), Experiments (Page 8), and Related work (Page 17) sections of the new version paper.

> **Q2: Can you have t

### Response to Reviewer 5yqn [Part 1]
We would like to sincerely thank Reviewer 5yqn for providing the insightful review and constructive suggestions. Below are the responses point by point:

- **W1: Novelty of the proposed method and theoretical results.**

A1-Part 1: **Novelty of the proposed method.** The proposed $\delta$-Adapter is novel compared to existing methods. The $\delta$-Adapter differs from existing adapters in NLP in the following aspects (**in Pages 1 & 17 of the new version**):
- - $\delta$-Adapter is a post-hoc I/O editor of black-box forecasters. But, NLP adapters (e.g., parameter-efficient fine-tuning in Transformers) are typically inserted inside each layer and trained jointly with full access to the backbone internals.
- - NLP adapters (prompt, prefix, P-tuning, Lora) do not modify the I/O data themselves, but rather add additional infos/params to them or calculates auxiliary losses or penalties to achieve domain alignment. In contrast, $\delta$-Adapter places more emphasis on the gains brought to the model by editing or correcting the I/O data itself.

**The benefits of the post-processing module are**:
- - A plug-and-play, model-agnostic lightweight module that can be used for untouchable black-box models and brings significant performance improvements;
- - Freezing backbone avoids catastrophic forgetting and robust to high variance, preserves production hardening and governance;
- - Fast training/test speeds and high data efficiency are achieved, even with short labeled histories or tight retraining windows;
- - Metric-aware, it enables important feature selection and application-aligned calibration without altering the backbone.

To the best of our knowledge, prior adapter works in NLP do not cover this combination of post-hoc I/O manipulation, feature selection, and calibrated predictive intervals, all within a single unified framework. Alternatively, applying $\delta$-Adapter to NLP is also a promising attempt. We have added comparisons in Appendix A of the new version.

A1-Part 2: **Novelty of the theoretical results.** Our theoretical results (Proposition 3.1, Theorems 2–3, and Proposition 3.2) provide: 1) explicit Lipschitz drift bounds for input edits and their multiplicative variant, 2) per-sample local descent guarantees for both output and input adapters, and 3) a compositional stability result when combining input and output adapters.
Below, we present the performance changes of $\delta$-adapters on different datasets over epochs (the blank is due to early stopping):
||Original|1|2|3|4|5|6|7|8|9|10|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|ELC (Add)|0.167|0.161|0.158|0.159|0.159|0.159|0.159|0.159|0.159|0.159|0.159|
|ELC (Mul)|0.167|0.162|0.161|0.160|0.159|0.159|0.159|0.159|0.159|||
|Traffic (Add)|0.463|0.460|0.455|0.453|0.452|0.451|0.451|0.451|0.451|0.451|0.451|
|Traffic (Mul)|0.463|0.459|0.454|0.451|0.449|0.448|0.448|0.448|0.448|0.448||
|Weather (Add)|0.178|0.162|0.161|0.161|0.161|0.161|0.161|0.161|0.161|0.161||
|Weather (Mul)|0.178|0.1

### Response to Reviewer gci4 [Part 2]
**The benefits of the post-processing module are**:
- - A plug-and-play, model-agnostic lightweight module that can be used for untouchable black-box models and brings significant performance improvements;
- - Freezing backbone avoids catastrophic forgetting and robust to overfitting, preserves production hardening and governance;
- - Fast training/test speeds and high data efficiency are achieved, even with short labeled histories or tight retraining windows;
- - Metric-aware, it enables important feature selection and application-aligned calibration without altering the backbone.

**A2-Part 3: Problem Statement (in Pages 1 & 17).** 
- - **Conditions drift**, which refers to gradual changes in the data-generating process (e.g., seasonal regime shifts, covariate shifts in demand patterns) that occur after the model has been deployed, making full retraining costly;
- - **Low-complexity residual structure** means that residual errors often exhibit simple patterns (e.g., horizon-wise bias, scale miscalibration, calendar offsets) that can be captured by a small function class (tiny MLPs/low-rank heads) rather than requiring a new high-capacity backbone, but the base model fails to absorb them.

We have updated the content of the paper's motivation, including the introduction, recent work, and experimental sections, to make it more clear.

- **W3: Insufficient Detail on Ada-X+Y.**

A3: Ada-X+Y is composed of Ada-X and Ada-Y, and Ada-X and Ada-Y are **trained jointly** in an end-to-end manner, not sequentially. We minimize **a single combined loss** $\mathcal{L}$ over the union of parameters $A_{\theta}^{in}$ (Ada-X) and $A_{\theta}^{out}$ (Ada-Y). The forward pass is:
$$\hat Y=F(X + \delta A_{\theta}^{in}(X)) \qquad (1)$$
$\tilde Y = \hat Y + \delta A_{\theta}^{out}(\hat Y)\qquad(2)$

During the backward pass, gradients flow from the loss through Ada-Y (Eq. 2), then through the backbone $F$, and finally to Ada-X (Eq. 1). This ensures that Ada-X learns input perturbations that specifically help the backbone produce features that Ada-Y can best correct.

Experimental Setup: In our codebase, we instantiate two separate Adam optimizers (learning rate=1E-4) for modular flexibility. However, they are stepped simultaneously after a single backward pass, making the process equivalent to optimizing a joint objective. As derived in **Proposition 3.2**, this joint update rule maintains the $O(\delta)$ drift bounds and descent guarantees, ensuring the two adapters do not destabilize each other (**See Appendix C.4 of the new version**).

- **W4: Scale and Computational Cost.**

A4-Part 1: **Model and it's parameters**
The $\delta$-Adapter is designed to be extremely lightweight. It is implemented as a 2-layer MLP (specifically, for **Sundial (128M)** and **TabPFN (48M)**, the adapter adds only approx. 1.5M-3M parameters depending on the horizon). Compared to the backbone model, the adapter introduces **less than 2%-6%** additional parameters, validating the lightw

### Response to Reviewer gci4 [Part 1]
We extend our sincere gratitude to Reviewer gci4 for their meticulous reading of our paper and for providing insightful reviews and constructive suggestions. Below are the responses point by point:

- **W1: Comparison with Alternative Post-Processing Methods.**

A1: As requested, we have integrated comparisons with batch-training TTA methods (SOLID, TAFAS) and online learning methods (FSNet, OneNet) into the new version (**Tables 2 in Page 7 & 10 in Page 26**).

**Experimental Setup**: To ensure a rigorous comparison, we addressed a critical issue raised in recent literature [Liang et al. 2024](https://arxiv.org/abs/2412.00108) and [YA Lau et al. 2025](https://openreview.net/pdf?id=I0n3EyogMi) regarding Test-Time Label Leakage in long-term forecasting. Standard TTA implementations often assume immediate access to the ground truth of the current prediction window to update the model. However, in realistic long-term forecasting (e.g., horizon $H=96$), the ground truth is not available until $H$ steps later.

Therefore, we evaluated all methods under a strict delayed feedback setting. The TTA and Online methods were only allowed to update their parameters using ground truth data that would be historically available at the inference timestamp, preventing the use of future information.

*Table 1: Comparison with TTA and Online Methods (**Averaged across all lengths; See Table 10 for details**; Metric: MSE)*
||DistPred|+SOLID|+TAFAS|+LoRA|+Ours|iTransformer|+SOLID|+TAFAS|+LoRA|+Ours|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|ELC|0.182|0.182|0.182|0.18|**0.175**|0.19|0.19|0.19|0.186|**0.18**|
|ETTh1|0.461|0.46|0.476|0.454|**0.451**|0.454|0.458|0.477|0.448|**0.449**|
|ETTh2|0.39|0.391|0.402|0.385|**0.379**|0.388|0.393|0.448|0.384|**0.377**|
|ETTm1|0.412|0.406|0.411|0.407|**0.396**|0.417|0.414|0.42|0.414|**0.403**|
|ETTm2|0.285|0.285|0.288|0.281|**0.274**|0.3|0.298|0.304|0.293|**0.29**|
|Exange|0.35|0.347|0.363|0.336|**0.297**|0.383|0.376|0.392|0.376|**0.316**|
|Traffic|0.453|0.453|0.455|0.449|**0.44**|0.475|0.475|0.476|0.468|**0.461**|
|Weather|0.256|0.255|0.256|0.251|**0.242**|0.259|0.257|0.259|0.255|**0.244**|

The results (summarized above) demonstrate the following:
- - **$\delta$-Adapter**: Consistently outperforms the backbones (DistPred, iTransformer) and all adaptation baselines, reducing MSE by significant margins (e.g., ~14% on Exchange).
- - **SOLID & TAFAS**: Under the strict non-leakage setting, these methods show a minor improvement.
- - **FSNet & OneNet**: These online methods struggle significantly. This is likely because they are originally designed for one-step-ahead or short-term variations and suffer from error accumulation when adapted to the delayed feedback loop of long-term forecasting.

It shows that **our method achieves a significant reduction in errors on each dataset across all backbones**, with remarkable performance improvements.

- **W2: Insufficient Motivation.**

A2-Part 1: **Justification of $\delta$-Adapter over A

### The Forecast After the Forecast: A Post-Processing Shift in Time Series


## Meta review / decision
### Paper Decision
Accept (Poster)

## PDF extracted text (first pages)
```text
Published as a conference paper at ICLR 2026
THEFORECASTAFTER THEFORECAST: A POST-
PROCESSINGSHIFT INTIMESERIES
Daojun Liang 1,2 Qi Li 1,2,∗ Yinglong Wang 1,2,∗ Jing Chen 1,2, Hu Zhang 1,2
Xiaoxiao Cui 3 Qizheng Wang 1,2 Shuo Li 4, 5
1 Key Laboratory of Computing Power Network and Information Security, Ministry of Education,
Shandong Computer Science Center (National Supercomputing Center in Jinan),
Qilu University of Technology (Shandong Academy of Sciences), Jinan, 250103, China
2 Shandong Provincial Key Laboratory of Computing Power Internet and Service Computing,
Shandong Fundamental Research Center for Computer Science, Jinan, 250103, China
3 Joint SDU-NTU Centre for Artificial Intelligence Research (C-FAIR), Shandong University
4 Department of Computer and Data Sciences, Case Western Reserve University, Cleveland, USA
5 Department of Biomedical Engineering, Case Western Reserve University, Cleveland, USA
liangdj@sdas.org,{li.qi, wangyinglong}@qlu.edu.cn
{chenj,zhanghu}@sdas.org, cuixiaoxiao711@hotmail.com
574370699@qq.com, shuo.li11@case.edu
ABSTRACT
Time series forecasting has long been dominated by advances in model archi-
tecture, with recent progress driven by deep learning and hybrid statistical tech-
niques. However, as forecasting models approach diminishing returns in accu-
racy, a critical yet underexplored opportunity emerges: the strategic use of post-
processing. In this paper, we address the last-mile gap in time-series forecasting,
which is to improve accuracy and uncertainty without retraining or modifying a
deployed backbone. We proposeδ-Adapter, a lightweight, architecture-agnostic
way to boost deployed time series forecasters without retraining.δ-Adapter learns
tiny, bounded modules at two interfaces: input nudging (soft edits to covariates)
and output residual correction. We provide local descent guarantees,O(δ)drift
bounds, and compositional stability for combined adapters. Meanwhile, it can act
as a feature selector by learning a sparse, horizon-aware mask over inputs to se-
lect important features, thereby improving interpretability. In addition, it can also
be used as a distribution calibrator to measure uncertainty. Thus, we introduce
a Quantile Calibrator and a Conformal Corrector that together deliver calibrated,
personalized intervals with finite-sample coverage. Our experiments across di-
verse backbones and datasets show thatδ-Adapter improves accuracy and calibra-
tion with negligible compute and no interface changes.
1 INTRODUCTION
Time Series Forecasting (TSF) powers decisions across energy Anderson (1976), finance Hyndman
& Athanasopoulos (2018), retail Piccolo (1990), and the sciences Gardner Jr (1985). Despite im-
pressive gains from modern neural forecasters Ekambaram et al. (2024); Hollmann et al. (2025);
Liang (2025); Liu et al. (2025), ranging from temporal convolutions Lea et al. (2016); Wu et al.
(2019; 2022); Li et al. (2023) and Transformers Zhou et al. (2021); Nie et al. (2023); Wang et al.
(2024a); Liu et al. (2023); Ye et al. (2024); Wang et al. (2024a); Liang et al. (2024b) to hybrid
statistical–neural models Liu et al. (2025); Ekambaram et al. (2024), condition drift Baier et al.
(2020); Liang et al. (2025) is still not alleviated. Conventional remedies, e.g., full fine-tuning, archi-
tectural changes, or ensembling, either demand substantial compute, risk destabilizing a hardened
system, or complicate operations. To cope with this, testing-time adaptation (TTA) is introduced
into TSF. The testing-time methods aim to mitigate test-time concept drift via linear adapter updates
∗Corresponding author.
1
Published as a conference paper at ICLR 2026
Kim et al. (2025), dynamic gating Grover & Etemad (2025), parallel forecaster combines Lee et al.
(2025), layer-wise adjustment Pham et al. (2023), and dynamic model selection Wen et al. (2023).
However, these methods rely, to varying degrees, on future labels for online model updates, thereby
introducing label leakage, where future ground-truth labels are unavailable when actually applied,
that causes model performance degradation Liang et al. (2024a); yee Ava Lau et al. (2025). Further-
more, LoRA-style adapters Hu et al. (2022); Pfeiffer et al. (2020); Li & Liang (2021) in NLP tend
to lead to high performance variance, since the output range is not fixed Biderman et al. (2024).
Thus, TSF in real deployments still faces the last-mile gap: 1) Conditions drift Baier et al. (2020),
which refers to gradual changes in the data-generating process (e.g., seasonal regime shifts, covariate
shifts in demand patterns) that occur after the model has been deployed, making full retraining
costly; 2) High performance variance. Existing post-processing techniques are prone to have high
performance variance due to unstable training; 3) Inefficient training/inference. Using complex
modules or frequent updates to absorb low-complexity residuals V ovk et al. (2017; 2018) makes
models suffer from inefficient training/inference. Based on these, we ask a different question:Can
we really keep the strong forecaster intact and learn only a tiny, post-hoc module that makes small
targeted corrections, so accuracy and reliability improve without heavy retraining?
We answer “yes” withδ-Adapter, a lightweight, model-agnostic framework that augments a frozen
forecasterFby learning a tiny adapterAin two minimal placements: input-side nudging (softly
editing covariates before inference) and output-side correction (residual refinement after inference).
Concretely, we instantiate additive or multiplicative forms for both placements, with a small trust-
region parameterδ∈(0,1)that bounds edits for safety and stability. SinceAis a tiny network (e.g.,
shallow MLP or low-rank head) trained whileFremains frozen, it produces consistent gains with
negligible training time and zero changes toF’s inference interface.
Further, a key instantiation of the input adapter is a feature-selector (mask) adapter that learns a
sparse, nearly binary, horizon-aware maskM∈[0,1] L×d and applies it multiplicatively to the
contextX ′ =X⊙M. We trainMend-to-end with sparsity, temporal-smoothness, and budget
regularizers so that the adapter preserves the base model’s inductive biases while exposing the most
consequential inputs for the frozen forecaster. This yields transparent selections, stable training, and
strong empirical gains under tight compute budgets.
Beyond point accuracy,δ-Adapter also upgrades forecast uncertainty without modifyingF. We
present two distributional correctors: 1) a Quantile Calibrator that learns horizon-wise quantile func-
tions as bounded offsets from the point forecast, with a monotonic parameterization and pinball-loss
training augmented by reliability regularization; and 2) a Conformal Calibrator that learns a scale
function for normalized-residual conformal prediction, delivering finite-sample coverage with per-
sonalized, heteroscedastic intervals. Empirically, both calibrators achieve state-of-the-art coverage
quality and produce tight, well-behaved intervals.
Throughδ-Adapter, this “last-mile” adjustment consistently improves forecasting accuracy in our
experiments across diverse backbones and datasets, with negligible training time and no change to
inference interfaces. The main contributions are:
• We formalizeδ-Adapter and instantiate two placements (input nudging and output residual
correction) in additive/multiplicative forms, all drop-in and architecture-agnostic.
• We introduce a learnable, budgeted mask that identifies and preserves the most consequen-
tial inputs, improving transparency and stability.
• We propose quantile and conformal calibrators that deliver calibrated, heteroscedastic un-
certainty with finite-sample coverage guarantees, all while keepingFfrozen.
• Across diverse backbones and benchmarks,δ-Adapter improves accuracy and calibration;
ablations illuminate the roles ofδ, capacity, horizon features, and residual structure.
2 METHODOLOGY
2.1 PROBLEM SETUP
LetD={(X (i), Y (i))}N
i=1 denote training pairs of context windowsX∈R L×d and future tar-
getsY∈R H×m (history lengthL, horizonH,dcovariates,mtarget dimensions). A pre-trained
2
Published as a conference paper at ICLR 2026
Input
Pretrained 
Model
Output
Input
Pretrained 
Model
Output
Post-Processing
+
Input
Pretrained 
Model
OutputOutput
Post-Processing
+
(a) Original Model (b) Input-side Nudging (c) Output-side Correction
Figure 1:δ-Adapter performs input nudging and output correction on the frozen forecaster.
forecasterFmapsXto predictions ˆY=F(X)∈R H×m. We keep all parameters ofFfixed and
introduce a lightweight, learnable adapterAθ with parametersθtrained onD. The adapter composes
withFvia two families of edits:
Input-side nudging: ˜X=X+δ A in
θ (X),(additive input) (1.1)
˜X=X⊙
 
1 +δ A in
θ (X)

,(multiplicative input) (1.2)
Output-side correction: ˜Y=F(X) +δ A out
θ (F(X), X),(additive output) (1.3)
˜Y=F(X)⊙
 
1 +δ A out
θ (F(X), X)

,(multiplicative output) (1.4)
The base risk ofFunder a lossℓis
R(F) =E (X,y)∼D
h
ℓ
  ˜Y , Y
i
.(2)
Here, we consider two adapters, trained by minimizing empirical risk overθwithFfrozen, as shown
in Eq. 1. The key questions are: (i) when does a smallδprovably help; (ii) why do lightweight
adapters suffice; and (iii) How do we chooseδand what is the stability of the adapterA? Now, let’s
answer these questions.
2.2 OUTPUT-SIDE ADAPTERS AS SHRINKAGE RESIDUAL LEARNING
Here, we consider the additive adapter, as shown in Eq. 1.3: ˜Y=F(X) +δA out
θ (F(X), X). With
slight modifications, the relevant analyses and theories also apply to multiplicative adapters.
Letr(X) =Y−F(X)denote the residual process. For squared errorℓ( ˆY , Y) = 1
2 ∥ ˆY−Y∥ 2
2, the
population risk of the output adapter with a fixedFequals
Rout(δ) = 1
2 E
hr(X)−δg(X)
2
2
i
, g(X) :=A out
θ (F(X), X).(3)
Expanding,
Rout(δ) = 1
2 E

∥r∥2
−δE[⟨r, g⟩]| {z }
signal alignment
+ 1
2 δ2E

∥g∥2
.(4)
Proposition 2.1(Small-step improvement).IfE[⟨r, g⟩]>0, then for all
0< δ < 2E[⟨r, g⟩]
E[∥g∥2] ,(5)
we haveR out(δ)<R out(0) = 1
2 E[∥r∥2]. The quadratic inδhas negative derivative at0and a
unique minimizerδ ⋆ = E[⟨r,g⟩]
E[∥g∥2] .
Remark.Improvement hinges on alignment between the learned correctiongand the residualr.
Even whenAis tiny, if residuals have low-complexity structure (calendar offsets, horizon-dependent
bias, scale drift), a smallgcan achieve positive alignment, and a shrunken stepδguarantees risk
reduction. This is exactly the first step of boosting with shrinkage or a stacked residual learner with
a conservative learning rate.
3
Published as a conference paper at ICLR 2026
In practice, we learngfrom finite data with a penaltyΩ(θ)(e.g.,ℓ 2, low rank, sparsity). The
empirical objective
min
θ
1
2
X
i
yi −F(X i)−δg θ(Xi)
2
+λΩ(θ)(6)
yields a shrunken projection of residuals onto the function class ofA. With smallδand a low-
capacityA, we target the dominant residual modes while avoiding variance blow-up.
2.3 INPUT-SIDE ADAPTERS VIA FIRST-ORDER LINEARIZATION
For the input-nudging adapter, as shown in Eq. 1.1: ˜X=X+δA in
θ (X), apply a first-order expansion
ofFaroundX:
F
 
X+δu(X)

≈F(X) +δJ F (X)u(X),(7)
whereu(X) :=A(X, h)andJ F (X)∈R H×d is the Jacobian ofFw.r.t. inputs. Under squared
loss, replacinggbyJ F uin the previous derivation yields
Rin(δ)≈ 1
2 E

∥r∥2
−δE[⟨r, J F u⟩] + 1
2 δ2E

∥JF u∥2
.(8)
In general, forˆyin(X;δ) =F
 
X+δu(X)

,R in(δ) = 1
2 E
hy−ˆyin(X;δ)
2
2
i
, we have
Proposition 2.2(Generalδ-step improvement).IfE[⟨r, J F u⟩]>0, then there existsδ >0such
thatR in(δ)<R in(0)for allδ∈(0, δ]. And, ifFis affine in the near ofX, Prop. 2.1 is also hold.
The proof is given in Appendix B.2. This proposition states that for a differentiable lossℓ,
the loss gradient w.r.t. inputs satisfies∇ xℓ(F(X), y) =J F (X) ⊤∇ˆyℓ. Choosingu(X)≈
−B∇xℓ(F(X), y)for a small, learned preconditionerBrecovers a learned, damped gradient step
in input space; trainingAon data finds such steps implicitly without computingJ ⊤
F at test time.
3 THE STABILITY OFδ-ADAPTER
3.1 PREDICTION STABILITY UNDER BOUNDED INPUT EDITS
Let ˜X=X+δA in
ϕ(X)(additive case). Then, we have
Proposition 3.1(Drift bound).Assume the frozen forecasterFisL F -Lipschitz, the change in pre-
diction is bounded by
∥ ˜Y− ˆY∥ ≤δL F ∥Ain
ϕ(X)∥ ≤δL F
√
Ld.(9)
The proof is given in Appendix B.3. Further, let ˜X=X⊙exp(δA in
ϕ(X)), we have
Corollary 1(Multiplicative input edits).If∥X∥ ∞ ≤B X, then
∥ ˜Y− ˆY∥ ≤δe δLF BX ∥Ain
ϕ(X)∥.(10)
In particular, forδ≤1,∥ ˜Y− ˆY∥=O(δ).
The proof is given in Appendix B.4. Corollary 1 means that smallδyields Lipschitz-stable predic-
tion changes for input adapters.
3.2 LOSS STABILITY AND GUARANTEED LOCAL IMPROVEMENT
Let ˆY=F(X)and consider an output edit ˜Y= ˆY+δdwithd:=A out
ϕ ( ˆY , X), we have
ℓ( ˜Y , y)≤ℓ( ˆY , y) +δ⟨g, d⟩+ β
2 δ2∥d∥2, g:=∇ uℓ(u, y)

u= ˆY .(11)
Ifdaligns with−g, i.e.⟨g, d⟩ ≤ −α∥g∥∥d∥, we get
Theorem 2(Descent for output adapters).If the per-sample prediction lossℓ(·, y)isβ-smooth in
its first argument (e.g., MSE, Huber), for any sample,
ℓ( ˜Y , y)−ℓ( ˆY , y)≤ −δα∥g∥∥d∥+ β
2 δ2∥d∥2.(12)
4
Published as a conference paper at ICLR 2026
Hence, for anyδ∈
 
0, 2α∥g∥
β∥d∥

, the loss strictly decreases. The optimalδ ⋆ = α∥g∥
β∥d∥ yields
ℓ( ˜Y , y)−ℓ( ˆY , y)≤ − α2
2β ∥g∥2.(13)
The proof is given in Appendix B.5.
Remark.With MSE,g= ˆY−y, so the improvement is proportional to the squared residual mag-
nitude. Further, with a bounded adapter family, the trainedA out (minimizing batch loss) producesd
that correlates with−gunless capacity is zero.
Theorem 3(Descent for input adapters).Let ˜X=X+δvwithv:=A in
ϕ(X). AssumeFis
differentiable atXwith JacobianJ F (X). Define the effective prediction steps:=J F (X)v. Then
forδsmall,
ℓ(F( ˜X), y)≤ℓ( ˆY , y) +δ⟨g, s⟩+ β
2 δ2∥d∥2 +O(δ 2).(14)
If⟨g, s⟩ ≤ −α∥g∥∥s∥, there exists ¯δ >0such that∀δ∈(0, ¯δ)the loss strictly decreases. Moreover,
optimizing the quadratic upper bound inδyields the same margin as Theorem 2 up toO(1)terms.
The proof is given in Appendix B.6. Theorems 2 and 3 show that for sufficiently smallδand mild
alignment, both adapter types reduce the loss locally, with explicit improvement margins.
3.3 COMPOSITIONAL STABILITY(INPUT+OUTPUT)
Let the full edit be ˜X=X+δv, ˆY ′ =F( ˜X), then ˜Y= ˆY ′+δd( ˆY ′, X). Under the same conditions
as Prop. 3.1 and Theorems 2 and 3, we have:
Proposition 3.2(Composite drift and loss bound).
∥ ˜Y− ˆY∥ ≤ ∥ ˆY ′ − ˆY∥+δ∥d( ˆY ′, X)∥ ≤δL F ∥v∥+δC d,(15)
so the model drift isO(δ). Further, for the loss,
ℓ( ˜Y , y)≤ℓ( ˆY , y) +δ⟨g, s+d⟩+ β
2 δ2∥s+d∥ 2 +O(δ 2),(16)
The proof is given in Appendix B.7. If the combined steps+daligns with−gby parameter-sharing
or a learned gate, we inherit the same descent guarantee as Theorem 2.
4 IMPLEMENTATION
4.1δ-ADAPTER
δ-Adapter targets structured residuals (bias, scale miscalibration, phase lag) while preservingF’s
inductive biases. We encode this through three principles: 1) Boundedness: Enforce small edits via
δand penalties on∥A θ(·)∥; 2) Low capacity: Use tiny architectures to avoid overfitting and respect
production budgets. 3) Horizon awareness: Allow horizon-specific corrections without destabilizing
temporal coherence. Concretely, we use a tiny MLP as the backbone and impose:
∥Ain
θ (X)∥ ∞ ≤1,∥A out
θ (·)∥∞ ≤1,(17)
via tanh squashing and optional clipping, so thatδis a direct bound on the maximum per-entry
change. For multiplicative edits we ensure positivity where required by applyingexp
 
δAθ(·)

as
an alternative to1 +δA θ. For compositional adapters (input+output), as stated in Prop. 3.2, their
parameters can be optimized in parallel during the training process.
4.2 FEATURESELECTOR
A particularly transparent instantiation of our input adapter is to cast it as a learnable mask (selector)
that selects the parts of the input that are most consequential for the frozen forecasterF. Concretely,
for a context windowX∈R L×d, we parametrize an adapterA θ that outputs a maskM(X;θ)∈
[0,1] L×d,and apply it multiplicatively,
X ′ =X⊙M(X;θ).(18)
5
Published as a conference paper at ICLR 2026
The mask is trained end-to-end while keepingFfixed. Intuitively,Mplays the role of a soft selector:
values near1keep information intact, values near0suppress it. To obtain discrete, human-readable
selections without sacrificing differentiability, we employ relaxed Bernoulli parameterizations. Let
α(X;θ)∈R L×d be adapter logits. We form a Gumbel-Sigmoid (Concrete) relaxation
M(X;θ, τ) =σ
logα(X;θ) +G
τ

,(19)
whereGis i.i.d. Gumbel noise,σ(·)is the logistic function, andτ >0is a temperature annealed
from a high value (smooth masks) to a low value (nearly binary). At inference, we may harden
the mask via a thresholdM hard =1{M >0.5}or keep it soft to avoid distributional brittleness.
As a simpler alternative, we use a straight-through estimator: threshold in the forward pass, back-
propagate through the corresponding sigmoid in the backward pass. Training the mask as a selector
requires explicit structure in the objective. Given predictions ˜Y=F(X⊙M), we minimize
min
θ
Lpred
  ˜Y , Y

| {z }
forecasting error
+λ1 ∥M∥ 1|{z}
sparsity
+λent
P H
 
Mt,j

| {z }
low entropy
+λtv TV(M)| {z }
temporal smoothness
+λbud
 
¯m−κ

+| {z }
budget
,(20)
where¯m= 1
Ld
P
t,j Mt,j is the average keep-rate andκ∈(0,1]is a user-specified budget, which
stabilizes selection under correlations by constraining the feasible keep set, e.g., use at most 10% of
inputs. Theℓ 1 and entropy terms encourage sparse, nearly binary masks; the total-variation penalty
TV(M)promotes temporal contiguity, reflecting the fact that relevant patterns often span short
intervals rather than isolated instants. See the specific expressions of each part in Appendix C.3.
4.3 DISTRIBUTIONCALIBRATOR
Now, we introduce how to use the proposed adapter as a calibrator when the forecasterFis frozen
and produces only fixed-point predictions.
4.3.1 QUANTILECALIBRATOR
If a distributional assumption is undesirable, the adapter can directly output horizon-wise quantiles
as bounded offsets from the point forecast:
qτ,θ(X) = ˆY+εa θ
 
X, ˆY , τ

⊙s θ(X, ˆY),(21)
wherea θ ∈[−1,1] H×m ands θ >0is a learned scale. To ensure monotonicity inτ, we parameterize
qτj+1 ,θ =q τj ,θ + softplus
 
dj,θ(X, ˆY)

, τ 1 < τ 2 <· · ·< τ J ,(22)
whered j,θ is the adapter’s raw increment for the gap between two adjacent quantile levelsτ j and
τj+1. Eq. 22 anchored at a central level (e.g.,τ J/2) via the bounded offset around ˆY. Then, for the
training objective, we replace the point losses with pinball loss and add reliability regularization:
min
θ
1
N
NX
i=1
JX
j=1
ℓτj
 
Y (i), qτj ,θ(X (i))

+λ calCrel(θ) +λ mag∥aθ∥2
2.(23)
whereℓ τ is the pinball loss;C rel can be the same soft-coverage penalty as above, or a PIT-uniformity
term computed by interpolating the predicted quantiles into a differentiable CDF and matching the
PIT distribution toUniform(0,1).
4.3.2 CONFORMALCALIBRATOR
When strict distribution-free guarantees are needed, we combine a learned scale function with con-
formal prediction, i.e., we trainw θ(X, ˆY)>0(small adapter) to predict residual magnitude while
keeping the mean at ˆY:
min
θ
1
N
NX
i=1
Y (i) − ˆY (i)
/wθ
 
X (i), ˆY (i)
+λ∥w θ∥2
2,(24)
6
Published as a conference paper at ICLR 2026
subject to a mild regularizer to keepw θ near 1 on average. Then, we can use conformal scaling on
a held-out calibration setD cal to compute normalized residuals as
r(i) =
Y (i) − ˆY (i)
wθ
 
X (i), ˆY (i) ,(X (i), Y (i))∈ D cal.(25)
Then, the calibrated marginally valid prediction sets can be obtained by
Cα(X) =

y:∥y− ˆY∥ ≤κ αwθ(X, ˆY)
	
,(26)
whereκ α is the empirical(1−α)-quantile of{r (i)}. This yields finite-sample coverage1−αunder
exchangeability. The adapterw θ personalizes interval width whileFremains untouched.
5 EXPERIMENTS
We validate theδ-Adapter method on a variety of widely used datasets, see Appendix C.1. We test its
gains when applied to pre-trained and state-of-the-art (SOTA) models (Section 5.1), its a
```
