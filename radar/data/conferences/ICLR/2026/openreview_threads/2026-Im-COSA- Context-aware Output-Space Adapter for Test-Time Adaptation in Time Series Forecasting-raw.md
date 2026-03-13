# COSA: Context-aware Output-Space Adapter for Test-Time Adaptation in Time Series Forecasting — OpenReview Raw Thread

- Forum: https://openreview.net/forum?id=L7Z5wBMPrW
- PDF: https://openreview.net/pdf?id=L7Z5wBMPrW
- Section: 二、时间序列预测：分布鲁棒、多变量建模与后处理优化
- Zhihu score: 6.0
- Venue status: ICLR 2026 Poster

## Submission metadata
- Authors: Jeonghwan Im, Hyuk-Yoon Kwon
- Primary area: learning on time series and dynamical systems
- Keywords: Test-Time Adaptation, Time-Series Forecasting, Non-stationarity, Context-aware Adapter

## Abstract
Deployed time-series forecasters suffer performance degradation under non-stationarity and distribution shifts.
Test-time adaptation (TTA) for time-series forecasting differs from vision TTA because ground truth becomes observable shortly after prediction. 
Existing time-series TTA methods typically employ dual input/output adapters that indirectly modify data distributions, making their effect on the frozen model difficult to analyze. 
We introduce the Context-aware Output-Space Adapter (COSA), a minimal, plug-and-play adapter that directly corrects predictions of a frozen base model.
COSA performs residual correction modulated by gating, utilizing the original prediction and a lightweight context vector that summarizes statistics from recently observed ground truth.
At test time, only the adapter parameters (linear layer and gating) are updated under a leakage-free protocol, using observed ground truth with an adaptive learning rate schedule for faster adaptation.
Across diverse scenarios, COSA demonstrates substantial performance gains versus baselines without TTA (13.91$\sim$17.03\%) and SOTA TTA methods (10.48$\sim$13.05\%), with particularly large improvements at long horizons, while adding a reasonable level of parameters and negligible computational overhead.
The simplicity of COSA makes it architecture-agnostic and deployment-friendly.
Source code: https://github.com/bigbases/COSA_ICLR2026

## Reviews
### Reviewer_8Mzj
- summary: This paper introduces COSA (Context-aware Output-Space Adapter), a Test-Time Adaptation (TTA) framework designed to address the performance degradation of time series forecasting models caused by distribution shifts after deployment. In contrast to existing TTA methods that often employ complex dual input-output adapters, COSA proposes a simpler and more direct strategy that operates solely in the output space. The core mechanism utilizes a lightweight context vector, which summarizes statistics from recently observed ground truth, along with the base model's original prediction. This informat
- strengths: 1.  **Simplicity and Novelty:** The "output-space-only" design is a great innovation. It directly corrects predictions, offering a simpler, more intuitive, and safer alternative to complex dual-adapter methods that indirectly modify data distributions.
2.  **Inference Efficiency:** The method is quite fast, achieving a nearly order-of-magnitude speedup in inference time compared to prior TTA methods. This high efficiency makes it well-suited for practical, low-latency deployment scenarios.
3.  *
- weaknesses: 1. **Unconventional Experimental Settings:** The experimental setup has some questionable aspects: (1) The lookback window of 96 is relatively short. Most contemporary work uses longer history windows, such as 336 or 512. Predicting a long horizon of 720 from a short 96-step history is a somewhat impractical scenario and may weaken the persuasiveness of the method's effectiveness. (2) For multivariate time series, the mainstream approach (even for channel-independent models) is to process all variates concurrently. Splitting multivariate series into univariate ones for individual forecasting is inefficient, especially for widely-used datasets with a large number of variates like Electricity and Traffic.
2. **Missing Comparison with a Key Baseline and Motivation:** The authors motivate their work by claiming that existing TTA methods for time series forecasting use a dual-adapter architecture, and theirs is novel for being output-space-only. However, a recent paper, [SOLID](https://arxi
- questions: 1. **Design of the Context Vector:** The context vector C is constructed by aggregating the K most recent batches, which implicitly assumes temporal locality. However, this assumption may not always hold. For series with strong periodicity, data points from the same phase in previous cycles might be more informative contexts. Conversely, for series with abrupt concept drifts, a context vector based on recent history could provide outdated or even detrimental information. Is a design that relies solely on recent locality optimal, or would it be more robust to consider other relationships such as periodicity?
2. **Clarification on Parameter Efficiency:** Given that COSA has far more parameters than PETSA, could the authors clarify the rationale behind choosing a linear layer with a relativel
- rating: 6 | confidence: 4

### Reviewer_hY4L
- summary: The paper proposes a simple yet effective method to adapt time-series forecasting models under distribution shifts. Instead of dual adapters that modify both inputs and outputs, COSA introduces a single output-space adapter that directly corrects predictions from a frozen base model using a linear residual correction modulated by a learnable gate. The adapter leverages a lightweight context vector summarizing recent ground-truth statistics and updates only its parameters during inference under a leakage-free streaming protocol. COSA achieves consistent accuracy gains across six datasets and mu
- strengths: The paper presents a clear and elegant solution to the problem of test-time adaptation in time-series forecasting through a single output-space adapter, offering originality by simplifying previous dual-adapter frameworks. The methodology is technically sound, with a well-motivated design and a careful leakage-free adaptation protocol. Empirical results are extensive, covering multiple architectures, horizons, and datasets, demonstrating consistent and significant improvements. The paper is well
- weaknesses: The context construction relies on simple aggregation statistics, which may not capture complex temporal dependencies or handle irregular or missing data effectively. The experiments focus mainly on standard LTSF datasets without testing on more challenging non-stationary or real-world drift scenarios. The computational analysis could better clarify the trade-offs between adaptation time and inference latency. Additionally, statistical significance reporting or variance analysis would strengthen the reliability of the reported performance gains.
- questions: 1. Can the authors clarify under which conditions an output-only adapter is sufficient, and when input-side calibration would still be necessary for stable adaptation?

2. How sensitive is COSA to the construction of the context vector? Would richer temporal encodings or normalization statistics improve its robustness and generalization?

3. Could the method be extended to jointly handle multivariate forecasting instead of decomposing into independent univariate tasks?

4. How would COSA perform under partial label availability or delayed target feedback, which are common in real-world streaming scenarios?

5. Would the proposed adaptive learning rate schedule still remain stable when applied to models with much longer adaptation windows or non-periodic datasets?

6. Could you fix the code
- rating: 8 | confidence: 4

### Reviewer_htEG
- summary: This paper, titled “COSA: Context-Aware Output-Space Adapter for Test-Time Adaptation in Time Series Forecasting”, addresses the problem of distribution shifts and non-stationarity that cause performance degradation in deployed time-series forecasting models. The main objective is to develop a lightweight, architecture-agnostic test-time adaptation (TTA) mechanism that can improve model performance post-deployment without retraining the base model.

The proposed method, COSA, is a context-aware output-space adapter that performs direct residual correction on the model’s predictions. It introdu
- strengths: - The paper tackles an important and timely problem—test-time adaptation for time-series forecasting—which has received comparatively less attention than its vision counterparts.
- The proposed output-space-only adapter (COSA) is a conceptually clean and lightweight solution, addressing the design complexity and interpretability challenges of prior dual-adapter approaches.
- The idea of context-aware residual correction, where recent ground-truth statistics inform a gating-based correction, is i
- weaknesses: - Although the paper proposes a simplified, output-space-only adapter, the underlying idea of residual correction or adapter-based adaptation is not fundamentally new. Similar concepts—such as residual adapters, calibration layers, and lightweight correction modules—have appeared in various works.

- While the simplicity of a linear output-space adapter is appealing, it may also limit the method’s expressive power, particularly under nonlinear or abrupt regime shifts.

- The context vector construction relies on fixed aggregation (mean or median) and fixed length K, which might not generalize across datasets with different periodicities or nonstationary characteristics.

- The paper positions the cosine–adaptive learning rate (CALR) as theoretically motivated but does not provide formal derivation or convergence analysis.
- questions: - The context vector $C_t$ is built from recent batch statistics (e.g., means) with fixed length $K$. Could a learned context encoder (e.g., lightweight RNN/SSM/attention) or an adaptive $K$ selected online (error-aware rather than rule-based) improve robustness across different periodicities and drift patterns without eroding the latency advantages? Please discuss the accuracy–overhead trade-off.

- COSA applies a learnable gate $g$ with $\tanh(g)$ to modulate correction. Do you observe interpretable gate trajectories during level shifts, scale drift, and seasonal phase changes (e.g., stronger gating when residuals spike)? Would horizon-specific or channel-specific gating improve control or stability relative to a single scalar gate?

- Experiments decompose multivariate data into per-var
- rating: 4 | confidence: 4

### Reviewer_jjeA
- summary: This paper introduces COSA (Context aware Output-Space Adapter), an adapter-based model that adjust predictions of a frozen base model. COSA achieves this via by learning a gated linear transformation on the original prediction and a context vector of summary statistics of the input. The model was tested on standard time series forecasting benchmarks and showed better performance with faster inference time. In addition, authors showed the utility of different components via an ablation study.
- strengths: - Although the idea is simple and one may argue that it is not novel per se, I think the empirical results show strong adequate performance gain in a much shorter inference time compared to the other baselines. 

- I think authors have done a good job in finding relevant (albeit recent) works.

- Authors have reported hyper-parameters and also provided code. 

The current results support the claims in the paper and look convincing to me and overall I am in favour of acceptance.
- weaknesses: - The input of the gating mechanism and its transformation by parameters g is a bit unclear to me in the formulation and figures. I think authors should elaborate this part similar to other components. 

- Authors conducted experiments on the standard time series benchmarks. I think the message of the paper will be stronger if also test the method on the Monash benchmark [1]. Just to be clear, I do not expect authors to repeat all their experiments on this benchmark.  

- The benefit of the proposed method is only visible in long-term forecasting which one may argue it is expected as in the current setup (including baselines) there is a delay period to observe some ground truth. I think the paper will be stronger if authors highlight the applicability domain of the work i.e., what problems COSA-F (-P) is the most suitable for? 

- Standard error or confidence interval for numerical results and error bars for the bar plots are not reported. Also, it would be nice to have average+se to s
- questions: Can you please comment on the performance of COSA-F (-P) with only a single update (S==1) either verbally and/or empirically?
- rating: 6 | confidence: 3

## Author comments / rebuttal
### Author comment
We sincerely thank you for your positive feedback and for your continued support of our work.

### Author comment
We sincerely appreciate your thoughtful feedback and are glad that our revisions have addressed your concerns. Following your suggestions, we have improved the presentation quality by (1) making caption of Table 3 more detailed to provide better context without requiring reference to the main text, and (2) increasing the font size of axis labels and legends across all figures for improved readability. We believe these changes will significantly enhance the accessibility of our results. Thank you again for your constructive comments and for raising your score.

### Author comment
Thank you for your careful checking and for bringing this to our attention. Additionally, we use a time-ordered 7:1:2 (train:val:test) split for all ETT datasets, and we have explicitly clarified this in Section 4.1. Under this unified split setup, ETTh1/ETTm1 indeed show lower accuracy than in the original papers, whereas ETTh2/ETTm2 actually achieve lower MSE, indicating that the effect is dataset-dependent. Despite these differences in absolute numbers, all TTA methods are evaluated on exactly the same pretrained baselines, so our conclusions about the relative gains of COSA over No TTA and other TTA methods remain valid.

### Author comment
We appreciate your recognition of our rebuttal and are grateful for the opportunity to further address the remaining concern regarding the choice of uncertainty measures. We additionally provide 95% confidence intervals for the main accuracy comparison results in the appendix. We believe this clarifies the distinction between variability and uncertainty and addresses the concern raised in Weakness #4. (**Table 19 in Appendix I**)

### Author comment
### Weakness

The context construction relies on simple aggregation statistics, which may not capture complex temporal dependencies or handle irregular or missing data effectively. The experiments focus mainly on standard LTSF datasets without testing on more challenging non-stationary or real-world drift scenarios. The computational analysis could better clarify the trade-offs between adaptation time and inference latency. Additionally, statistical significance reporting or variance analysis would strengthen the reliability of the reported performance gains.

### Response #7

1. Moivated by Reviewer’s comment, we additionally implement a variant that construct context by selecting top-K context values with importance scores. While this selective variant yields higher accuracy in some cases, the original local-context design performs better overall (**Table 12 in Appendix G.1.2**). 
We further discuss about the results and future directions in **Appendix H**.
    
    
    |  | Proposed | Selective |
    | --- | --- | --- |
    | Avg. MSE | **0.3240** | 0.3270 |
    | Avg. Adaptation Time / Batch (ms) | **80.12 ± 13.58** | 83.64 ± 15.71 |
    | Avg. Inference Time (ms) | **1.25 ± 0.0984** | 1.26  ± 0.1039 |
    | Avg. Parameter | **1,211,287** | 1,317,239 |
2. We conducted additional experiments on the Electricity dataset, which is a large-scale, real-world load monitoring benchmark with on average 33.77× more variates than our main datasets and exhibits **strong nonlinearity** (Avg. $R^2 = 0.0253$). COSA consistently outperforms all baselines, indicating that a linear output-space adapter is still sufficiently expressive for challenging non-stationary scenarios considered in this work **(Table 6 in Appendix F.1)**.
    
    
    |  | No TTA | TAFAS | PETSA | COSA-F | COSA-P |
    | --- | --- | --- | --- | --- | --- |
    | Avg.MSE | 0.2121 | 0.2031 | 0.2023 | 0.2004 | **0.1998** |
3. We clarify that adaptation time and inference latency, although both affected by the number of adapter parameters, arise from different computation paths and should be treated as separate metrics. Adaptation time is dominated by backward passes and repeated adaptation steps, while inference latency is the cost of a single forward pass after adaptation. Empirically, adaptation time is more sensitive to batch size and the number of adaptation steps, whereas inference latency remains small and almost unchanged relative to the backbone (**Figures 4(a), 4(c), and Table 10 in Appendix F.5**).
4. Most of our numerical results focus on prediction accuracy (MSE), whose standard deviations are all below 0.001. For readability, we therefore omit “±” and explicitly note this in the main results. For quantities that exhibit more noticeable variation, such as adaptation time per batch and inference time, we additionally report dispersion (mean ± standard deviation).

### Author comment
### Weakness #4

Standard error or confidence interval for numerical results and error bars for the bar plots are not reported. Also, it would be nice to have average+se to summarize each method/dataset.

### Response #4

Most of our numerical results focus on prediction accuracy (MSE), whose standard deviations across runs are all below 0.001. For readability, we therefore omit “±” and explicitly note this in the main results. For quantities that exhibit more noticeable variation, such as adaptation time per batch and inference time, we additionally report dispersion (mean ± standard deviation).

---

### Weakness #5

The baseline normalization is not clearly defined in Section 4.2.2, overall this section seems a bit disconnected to the rest of the paper.

### Response #5

We added a brief overview of the normalization methods and representative approaches RevIN and DDN in **Appendix G.7**, and clarified the purpose of the comparison in **Section 4.2.2**. This experiment is intended to examine whether COSA acts as a substitute or a complement to existing normalization schemes. Empirically, COSA alone provides more consistent gains than RevIN/DDN, and combining COSA with either normalization yields further improvements. These results indicate that COSA is independent of a particular normalization choice and can be applied compatibly on top of existing normalization methods.

---

### Weakness #6

Looking at the reported results in TAFAS and PETSA paper, there are significant differences with those reported in this paper (Exchange, ETTm2, ETTh2 on iTransformer).

### Response #6

When comparing iTransformer results to those reported in PETSA, we observe noticeable differences in MAE for several cases (ETTh2–720, Exchange Rate–96/720), while our numbers are close to those reported in TAFAS. For ETTh1 and Weather, the reported results are largely consistent across works, suggesting that the discrepancies stem from unreported hyperparameter or seed choices that affect the base model quality in PETSA for specific settings. Importantly, the relative improvement of COSA over its baselines remains consistent across all datasets. Our baselines are reproduced from the officially released code of each method, and to ensure reproducibility, we provide all scripts used in the paper at the following anonymous repository: https://anonymous.4open.science/r/linear-adapter-A720
.

---

### Question #1

Can you please comment on the performance of COSA-F (-P) with only a single update (S==1) either verbally and/or empirically?

### Response #7

The proposed CALR scheduler resets the learning rate at the beginning of each new batch and then adapts it step-wise after the first update within that batch. Therefore, when $S = 1$, CALR is effectively inactive, which is why we initially omitted this setting. We have now added the $S = 1$ results to **Figure 4(a)**. As expected, **S = 1** yields slightly lower accuracy than larger **$S$** values, but achieves the fastest w

### Author comment
We appreciate Reviewer jjeA for their thoughtful and detailed feedbacks. Below we address each weakness and question in turn, and have updated the manuscript and appendix accordingly. Added or revised content is marked in **blue**.

---

### Weakness #1

The input of the gating mechanism and its transformation by parameters g is a bit unclear to me in the formulation and figures. I think authors should elaborate this part similar to other components.

### Response #1

We apologize for the lack of clarity and have revised the paper to better explain the gating mechanism (**Appendix D.1**).

In COSA, the gate is defined as  $gating = \tanh(g) \in [-1, 1]$ with a learnable parameter $g$ and this bounded scalar is multiplied with the linear residual output to modulate the correction strength. If we directly used *g* instead of  $tanh(g)$, small changes in $g$ could cause large, unstable changes in the correction and make the adapter overly sensitive to noisy points. The $tanh$ transform instead keeps the gate bounded and ensures that changes in $g$ are reflected smoothly and gradually. When the residual magnitude spikes, the gate moves toward 0, as shown in **Fig 5 in Appendix D.1** thereby attenuating the residual correction and stabilizing adaptation.

---

### Weakness #2

Authors conducted experiments on the standard time series benchmarks. I think the message of the paper will be stronger if also test the method on the Monash benchmark [1]. Just to be clear, I do not expect authors to repeat all their experiments on this benchmark.

### Response #2

To address this suggestion, we additionally evaluate COSA on the **Electricity** dataset from the Monash benchmark, which has the lowest $R^2$ among the considered datasets and is a large-scale, real-world load-monitoring series with on average 33.77× more variates than our main benchmarks. As summarized in the newly added results table, COSA consistently achieves the highest predictive accuracy across all settings, demonstrating that it remains effective even on highly nonlinear, high-dimensional time series (**Table 6 in Appendix F.1**).

|  | No TTA | TAFAS | PETSA | COSA-F | COSA-P |
| --- | --- | --- | --- | --- | --- |
| Avg.MSE | 0.2121 | 0.2031 | 0.2023 | 0.2004 | **0.1998** |

---

### Weakness #3

The benefit of the proposed method is only visible in long-term forecasting which one may argue it is expected as in the current setup (including baselines) there is a delay period to observe some ground truth. I think the paper will be stronger if authors highlight the applicability domain of the work i.e., what problems COSA-F (-P) is the most suitable for?

### Response #3

1. Although our main setup focuses on long-horizon forecasting, COSA is not specialized only for long-term horizons. To verify this, we conducted additional experiments on shorter forecasting windows and observed that, unlike other Timse-series Forecasting (TSF)-TTA methods, COSA provides consistent and stable improvements e

### Author comment
### Question #4

You describe a cosine–adaptive learning-rate schedule with thresholds motivated by stability. Can you provide formal reasoning or empirical evidence for convergence/safety (e.g., avoidance of error amplification) under short adaptation steps , and comparisons against simpler schedules (fixed/one-cycle/standard AdamW) with statistical significance?

### Response #7

Following the Reviewer htEG’s suggestion, we conducted additional experiments comparing CALR with other PyTorch schedulers: CosineAnnealingLR, ExponentialLR, ReduceLROnPlateau, StepLR, and a fixed learning rate. We excluded One-Cycle because it requires a pre-defined schedule based on a fixed number of steps (and batch size), which is incompatible with PAAS-based dynamic batch sizes and continuously arriving test-time data in our TTA scenario. Across almost all cases, the proposed CALR achieves the best or second-best performance (**Table 16 in Appendix G.4**).

|  | CALR | Cosine | Exp | Fixed | Plataeu | Step |
| --- | --- | --- | --- | --- | --- | --- |
| **Average MSE** | **0.3222** | 0.3380 | 0.3487 | 0.3552 | 0.3418 | 0.3312 |

---

### Question #5

In cases where short-term perturbations revert (e.g., transient scale spikes), how quickly does COSA roll back adaptation?

### Response #8

**Figure 6 in Appendix D.2** visualizes the trajectory of pre-adaptation loss and learning rate for the iTransformer–ETTm1, \(L = 96\) case. When a short-term loss spike occurs, CALR immediately decreases the learning rate to minimize the impact of the perturbation, and once the loss enters a stable decreasing phase, CALR increases the learning rate again to promote rapid re-adaptation. This control mechanism suppresses excessive parameter drift **without requiring any roll-back**, allowing COSA to quickly recover its correction performance after the perturbation. The interaction between learning rate and loss demonstrates that, under non-stationary environments with short-term perturbations, COSA can respond and restore performance in a stable manner.

### Author comment
### Weakness #4

The paper positions the cosine–adaptive learning rate (CALR) as theoretically motivated but does not provide formal derivation or convergence analysis.

### Response #4

We agree that classical convergence analysis is difficult to formalize in non-stationary TSF-TTA, where the data distribution and effective optimum keep shifting over time. Our theoretical focus is therefore on **stability within each short adaptation window**, rather than convergence to a fixed point. In CALR, each step-wise parameter update is **uniformly bounded** due to 1) an upper bound on the learning rate $\eta_{\max}$, 2) gradient clipping, 3) L2 normalization loss term, and the gating factor $gating \in [-1, 1]$. These safeguards structurally prevent uncontrolled error amplification during adaptation. We provide more details in **Appendix A**.

The term “theoretically motivated” in Section 3.5 was intended to emphasize this stability-driven design, not to claim a full convergence proof. To avoid confusion, we have revised the wording to “stability-induced” in the updated manuscript.

---

### Question #2

- COSA applies a learnable gate with to modulate correction. Do you observe interpretable gate trajectories during level shifts, scale drift, and seasonal phase changes (e.g., stronger gating when residuals spike)? Would horizon-specific or channel-specific gating improve control or stability relative to a single scalar gate?

### Response #5

1. We analyzed batch-wise gate values together with the residual magnitude (squared sum of linear residuals). During level shifts and scale drift where residual spikes occur, the gate rapidly moves toward 0, effectively attenuating correction strength. For example, in the iTransformer–ETTm1–96 setting, a spike around the 70–80th batch is immediately followed by the gate shrinking toward 0, which we interpret as COSA suppressing over-correction **(Figure 5 in Appendix D.1)**.
2. We also implemented a horizon-wise vector gating with the same length as the prediction length, aiming for finer modulation when drift affects only specific horizons. However, this variant yielded lower average accuracy than a single scalar gate, likely because the influence of noisy points propagates across all horizon-specific gates over time. In contrast, scalar gating provides a consistent batch-level modulation that limits the impact of such noise. **(Table 18 in Appendix G.6)**

|  | Scalar | Vector |
| --- | --- | --- |
| Avg. MSE | **0.3240** | 0.3287 |
| Avg. Adaptation Time / Batch (ms) | **80.12 ± 13.58** | 96.34±12.48 |
| Avg. Inference Time (ms) | **1.25 ± 0.0984** | 1.89 ± 0.0745 |
| Avg. Parameter | **1,211,287** | 1,211,623 |

---

### Question #3

Experiments decompose multivariate data into per-variable univariate tasks. In settings with strong cross-variable dependence, would COSA benefit from structured (e.g., block-sparse or low-rank shared components) or shared context to capture cross-covariances? What happens to para

### Author comment
We appreciate Reviewer htEG for their detailed, constructive feedbacks. Below we address each weakness and question in turn, and have updated the manuscript and appendix accordingly. Added or revised content is marked in **blue**.

---

### Weakness #1

Although the paper proposes a simplified, output-space-only adapter, the underlying idea of residual correction or adapter-based adaptation is not fundamentally new. Similar concepts—such as residual adapters, calibration layers, and lightweight correction modules—have appeared in various works.

### Response #1

We agree that the general ideas of residual adapters and lightweight correction modules have appeared in other domains. **However,** these works do not address time-series test-time adaptation (TSF-TTA) under non-stationary, continuously drifting distributions. TSF-TTA is particularly challenging because (i) even small errors can be strongly amplified along the horizon due to autocorrelation, and (ii) the type and magnitude of non-stationarity can change at every input, requiring continuous re-tuning of correction strength. Our contribution is to show that a simple output-space linear residual adapter can effectively address these challenges and yields stable, efficient gains across diverse non-stationary scenarios when combined with TSF-TTA–specific design of COSA (CALR, context modeling, and gating), as validated by extensive experiments and ablations.

---

### Weakness #2

While the simplicity of a linear output-space adapter is appealing, it may also limit the method’s expressive power, particularly under nonlinear or abrupt regime shifts.

### Response #2

We conducted additional experiments on the Electricity dataset, which is a large-scale, real-world load monitoring benchmark with on average 33.77× more variates than our main datasets and exhibits **strong nonlinearity** (Avg. $R^2 = 0.0253$). Even under this highly nonlinear and high-dimensional regime, COSA consistently outperforms all baselines, indicating that a linear output-space adapter is still sufficiently expressive for challenging non-stationary scenarios considered in this work **(Table 6 in Appendix F.1)**.

|  | No TTA | TAFAS | PETSA | COSA-F | COSA-P |
| --- | --- | --- | --- | --- | --- |
| Avg.MSE | 0.2121 | 0.2031 | 0.2023 | 0.2004 | **0.1998** |

---

### Weakness #3, Question #1

- The context vector construction relies on fixed aggregation (mean or median) and fixed length K, which might not generalize across datasets with different periodicities or nonstationary characteristics.
- The context vector is built from recent batch statistics (e.g., means) with fixed length . Could a learned context encoder (e.g., lightweight RNN/SSM/attention) or an adaptive selected online (error-aware rather than rule-based) improve robustness across different periodicities and drift patterns without eroding the latency advantages? Please discuss the accuracy–overhead trade-off.

### Response #3

COSA currently uses a very lig

### Author comment
---

### Question #3

Could the method be extended to jointly handle multivariate forecasting instead of decomposing into independent univariate tasks?

### Response #3

COSA can be applied in a model-agnostic manner, as it fundamentally adopts an output-space residual adapter architecture. For fair comparison with prior TSF-TTA baselines (which all decompose multivariate series into per-variable univariate tasks), our main experiments adopt the univariate setting.

Following the reviewer’s suggestion, we additionally implement a multivariate variant that uses cross-variable attention to exchange context across variables and mix shared and variable-specific patterns before applying COSA. This multivariate COSA generally outperforms the univariate version when cross-variable correlations are meaningful, while the Exchange Rate dataset still favors univariate modeling due to its weak inter-variable dependence. The added cross-variable module, however, introduces non-negligible complexity and latency. (**Table 17 in Appendix G.5**)

We provide additional discussion on the future direction in the **Appendix H**.

|  | Proposed (Muiltiple Independent Univariate) | Multivariate |
| --- | --- | --- |
| Avg. MSE | 0.3240 | 0.3071 |
| Avg. Adaptation Time / Batch (ms) | 80.12 ± 13.58 | 186.28 ± 15.36 |
| Avg. Inference Time (ms) | 1.25 ± 0.0984 | 6.35 ± 0.2452 |
| Avg. Parameter | 1,211,287 | 1,212,446 |

---

### Question #4

How would COSA perform under partial label availability or delayed target feedback, which are common in real-world streaming scenarios?

### Response #4

Existing TSF-TTA methods, including COSA, assume that ground-truth labels eventually become available, and our experiments follow this setting. In real deployments, however, labels can be delayed or missing for certain time steps. To handle this, COSA updates its adapter parameters **only when** the corresponding ground-truth becomes available, and simply reuses the last updated correction for unlabeled steps, ensuring a leakage-free protocol (**Section 3.2**). Thus, under partial or delayed feedback, only the adaptation frequency changes, while prediction procedure of COSA remains stable and applicable.

---

### Question #5

Would the proposed adaptive learning rate schedule still remain stable when applied to models with much longer adaptation windows or non-periodic datasets?

### Response #5

CALR remains stable under longer adaptation windows because each step-wise update is uniformly bounded and the learning rate within a window is decayed to 0 by a cosine annealing schedule (**Appendix A**). Even if the number of adaptation steps per batch increases, later-step updates have vanishing impact, so the cumulative parameter change in an adaptation window stays bounded.

Moreover, CALR does not rely on periodicity. It adjusts the learning rate solely based on the local loss behavior within each adaptation window. In additional experiments on forecasting horizons as short as $L \i

### Author comment
We appreciate Reviewer hY4L for their positive and encouraging evaluation of our work. Below we address each weakness and question in turn, and have updated the manuscript and appendix accordingly. Added or revised content is marked in **blue**.

---

### Question #1

Can the authors clarify under which conditions an output-only adapter is sufficient, and when input-side calibration would still be necessary for stable adaptation?

### **Response #1**

We added experiments that combine COSA with the input-side calibration of TAFAS (GCM). On average, using COSA alone yields better accuracy and lower latency, because GCM suppresses fast or irregular but potentially informative distribution shifts and can therefore hurt adaptation.

Output-only residual correction is sufficient when the input distribution is relatively stable and non-stationarity mainly appears as accumulated bias/scale drift in the outputs. In contrast, on datasets with strong input spikes/noise (ETTh1/h2/m2), input-side GCM smooths the inputs, stabilizes the base forecasts, and further improves COSA (**Table 13 in Appendix G.2**). We provide further discussion in **Appendix H**.

|  | COSA-Only | COSA+GCM |
| --- | --- | --- |
| Avg. MSE | 0.3240 | 0.3298 |
| Avg. Adaptation Time / Batch (ms) | 80.12 ± 13.58 | 86.64±12.93 |
| Avg. Inference Time (ms) | 1.2500 ± 0.0984 | 1.38 ± 0.0953 |
| Avg. Parameter | 1,211,287 | 1,276,478 |

---

### Question #2

How sensitive is COSA to the construction of the context vector? Would richer temporal encodings or normalization statistics improve its robustness and generalization?

### Response #2

To assess the sensitivity of COSA to context construction, we extended the analysis of context construction methods by adding encoder-based context vectors that extract temporal embeddings from the observed ground truth, in addition to the original statistic-based designs.

We observed cases where encoder-based context, especially with an attention encoder, improved performance, indicating the potential of richer temporal encodings. However, on average, our original statistic-based context yielded the best overall accuracy. In non-stationary TSF-TTA, the distribution changes rapidly and the number of  adaptation steps is limited, making it difficult to reliably learn high-quality representations. As a result, encoder-based contexts can overfit on specific patterns or fail to track distribution shifts, degrading performance. Implementation details and the results are provided in **Table 12 in Appendix G.1.2, Table 13 in G.1.3** and further discussion in **Appendix H.**

|  | Proposed | Rnn | LSTM | Attention |
| --- | --- | --- | --- | --- |
| Avg. MSE | 0.3240 | 0.3254 | 0.3260 | 0.3278 |
| Avg. Adaptation Time / Batch (ms) | 80.12 ± 13.58 | 126.52 ± 22.88 | 134.29 ± 25.67 | 175.72 ± 16.88 |
| Avg. Inference Time (ms) | 1.2500 ± 0.0984 | 1.6610 ± 0.2315 | 1.7419 ± 0.2778 | 1.9618 ± 0.3183 |
| Avg. Parameter | 1,211,287 | 1,317,239 | 1,466,615 | 1,647,73

### Author comment
### Question #1: Design of the Context Vector

COSA is designed to quickly and stably correct output bias in the local residual correction. In non-stationary TTA settings, the input distribution continuously drifts over time, so relying on distant past information can conflict with the current drift direction and degrade correction performance. For this reason, our original context vector is constructed from recent information only.

Motivated by Reviewer 8Mzj’s question, we additionally implement a variant that construct context by selecting top-K context values with importance scores. While this selective variant yields higher accuracy in some cases, the original local-context design performs better overall (**Table 12 in Appendix G.1.2**). 

We further discuss about the results and future directions in **Appendix H**.

|  | Proposed | Selective |
| --- | --- | --- |
| Avg. MSE | **0.3240** | 0.3270 |
| Avg. Adaptation Time / Batch (ms) | **80.12 ± 13.58** | 83.64 ± 15.71 |
| Avg. Inference Time (ms) | **1.25 ± 0.0984** | 1.26  ± 0.1039 |
| Avg. Parameter | **1,211,287** | 1,317,239 |

---

### Question #2: Parameter Efficiency

To provide sufficient capacity under this constraint, we adopt a full linear layer.

The number parameters of COSA adapter account relatively small compared to the base model. While this is larger than PETSA adapter, it is still smaller than the TAFAS. Despite using more parameters than PETSA, COSA achieves faster inference, more stable behavior, and larger accuracy gains.

Low-rank factorization can, in principle, be applied to COSA as well, but it trades parameter efficiency for reduced expressiveness and a sharper gradient landscape, which can overfit specific drift patterns or destabilize adaptation. As seen in PETSA, such approaches typically require additional architectural changes and auxiliary losses to remain stable. We therefore position COSA as complementary to low-rank designs and highlight parameter-efficient variants of COSA (e.g., via low-rank adapters) as an interesting direction for future work, which we now explicitly discuss in the **Appendix H** of revised paper.

---

### Question #3: Practical Use

COSA-P uses a PAAS strategy that estimates the dominant frequency via Fast Fourier Transform and sets the batch size accordingly, enabling cycle-aligned adaptation on strongly periodic series. However, when no clear dominant frequency is detected within the input window, the batch size defaults to the full window length, which can hurt performance on weakly or very long-periodic data. Empirically, for datasets where periodicity is observable within the window (ETTh1/ETTh2), COSA-P achieves a smaller average batch size than COSA-F (B=48) and thus more frequent corrections, whereas on datasets with weak or long-range periodicity (Exchange Rate, Weather), COSA-F outperforms COSA-P (**Table 7 in Appendix F.2**).

For COSA-F, there is an inherent trade-off between adaptation time and efficiency as batch size 

### Author comment
We thank Reviewer 8Mzj for the thoughtful feedback. Below we address each weakness and question in turn, and have updated the manuscript and appendix accordingly. Added or revised content is marked in **blue**.

---
### Weakness #1: Unconventional Experimental Settings

Our experimental setting was designed based on the experimental settings of major research on long-term time series forecasting tasks. The referenced studies are as follows: 

- Liu, et al. "itransformer: Inverted transformers are effective for time series forecasting." *arXiv* 2023.
- Wang, et al. "Timexer: Empowering transformers for time series forecasting with exogenous variables." NeruIPS2024.
- Zhou, et al. "Fedformer: Frequency enhanced decomposed transformer for long-term series forecasting." PMLR, 2022.
- Zeng, et al. "Are transformers effective for time series forecasting?." AAAI 2023.
- Kim, et al. "Battling the non-stationarity in time series forecasting via test-time adaptation." AAAI 2025.

Additionally, we conducted longer look-back window experiments (192, 336) on 3 representative base models due to time constraints. COSA still achieving the largest performance improvement (**Table 7 in Appendix F.2**).

|  | No TTA | TAFAS | PETSA | COSA-F | COSA-P |
| --- | --- | --- | --- | --- | --- |
| 192 → 192 | 0.2414 | 0.2779 | 0.2757 | **0.2361** | 0.2363 |
| 192 → 336 | 0.2884 | 0.3404 | 0.3346 | **0.2817** | 0.2823 |
| 192 → 720 | 0.4183 | 0.4881 | 0.4833 | 0.4072 | **0.4071** |
| 336 → 720 | 0.3039 | 0.3520 | 0.3423 | **0.2963** | 0.2993 |
| 336 → 720 | 0.4581 | 0.5081 | 0.5057 | **0.4250** | 0.4310 |

---

### Weakness #2: Missing Comparison with SOLID

SOLID fine-tunes the prediction layer of a base forecaster, while other methods keeps the base model frozen. In the revised paper, we clarify this distinction and add a conceptual comparison to COSA. COSA consistently achieves higher accuracy and better efficiency than SOLID (**Table 8 in Appendix F.3**).

|  | **SOLID** | **COSA-F** | **COSA-P** |
| --- | --- | --- | --- |
| **Prediction Accuracy(MSE)** | 0.3545 | **0.3100** | 0.3197 |
| **Wall-Clock Time(Seconds)** | 306.55 ± 2.6183 | 9.73 ± 0.0840 | **7.44 ± 0.0488** |

---

### Weakness #3: Potential Risk of Over-Correction and Instability

COSA aggressively adapts to incoming test-time data with only a few adaptation steps to quickly correct prediction errors. To prevent over-correction, we regularize this process with a learnable gating mechanism and gradient clipping. In addition, the proposed CALR scheduler adjusts the learning rate step-wise within each batch: when the loss spikes, CALR temporarily reduces the learning rate to soften updates; when the loss decreases steadily, CALR increases the learning rate to accelerate adaptation. Consequently, even if a transient noisy/anomalous batch causes a sharp loss increase, CALR immediately lowers the learning rate at the next step and rapidly damps the error amplification from that batch (**Appendix A**).

As a res

### COSA: Context-aware Output-Space Adapter for Test-Time Adaptation in Time Series Forecasting


## Meta review / decision
### Paper Decision
Accept (Poster)

## PDF extracted text (first pages)
```text
Published as a conference paper at ICLR 2026
COSA: C ONTEXT -AWARE OUTPUT -SPACE ADAPTER
FOR TEST-T IME ADAPTATION IN TIME SERIES FORE -
CASTING
Jeonghwan Im
Department of Data Science
Seoul National University of Science and Technology
24520018@seoultech.ac.kr
Hyuk-Yoon Kwon∗
Department of Data Science
Seoul National University of Science and Technology
hyukyoon.kwon@seoultech.ac.kr
ABSTRACT
Deployed time-series forecasters suffer performance degradation under non-
stationarity and distribution shifts. Test-time adaptation (TTA) for time-series
forecasting differs from vision TTA because ground truth becomes observable
shortly after prediction. Existing time-series TTA methods typically employ dual
input/output adapters that indirectly modify data distributions, making their ef-
fect on the frozen model difficult to analyze. We introduce the Context-aware
Output-Space Adapter (COSA), a minimal, plug-and-play adapter that directly
corrects predictions of a frozen base model. COSA performs residual correction
modulated by gating, utilizing the original prediction and a lightweight context
vector that summarizes statistics from recently observed ground truth. At test
time, only the adapter parameters (linear layer and gating) are updated under
a leakage-free protocol, using observed ground truth with an adaptive learning
rate schedule for faster adaptation. Across diverse scenarios, COSA demonstrates
substantial performance gains versus baselines without TTA (13.91 ∼17.03%)
and SOTA TTA methods (10.48∼13.05%), with particularly large improvements
at long horizons, while adding a reasonable level of parameters and negligible
computational overhead. The simplicity of COSA makes it architecture-agnostic
and deployment-friendly. Source code: https://github.com/bigbases/
COSA_ICLR2026
1 I NTRODUCTION
Time-series forecasting serves as the foundation for critical decision-making across diverse do-
mains, including finance (Chen et al., 2023), supply chain management (Aamer et al., 2020), energy
grids (Di Piazza et al., 2021), and predictive maintenance (Makridis et al., 2020). Modern forecast-
ing models, including Transformer-based architectures (Zhou et al., 2021; Liu et al., 2023; 2022),
typically achieve high accuracy. However, they suffer performance degradation in real deployment
settings due to non-stationarity and distribution shifts (Du et al., 2021; Chen et al., 2024a). Time
series exhibit inherent non-stationarity, with changing temporal patterns and statistical characteris-
tics over time, resulting in distributions at training that typically differ from those encountered after
deployment.
To address this challenge, various approaches have been proposed, including online learning, con-
tinual learning, and domain adaptation. Online and continual learning methods adapt by updating
model parameters directly to streaming data (Du et al., 2021; Zhang et al., 2024; Kirkpatrick et al.,
2017; Rolnick et al., 2019; Giannini et al., 2023; Pham et al., 2022), but these approaches incur
additional computational costs, memory requirements, catastrophic forgetting issues, and plasticity.
Furthermore, these methods typically require labeled data or explicit knowledge of task boundaries,
making them unsuitable for scenarios where only unlabeled streaming data is available during de-
ployment. Domain adaptation methods learn robust representations by reducing source–target dis-
∗Corresponding author: hyukyoon.kwon@seoultech.ac.kr
1
Published as a conference paper at ICLR 2026
Figure 1: Overview of COSA operation showing the context-aware gated linear adapter architecture
with input processing, linear transformation, gating mechanism, and output correction for test-time
adaptation.
tribution differences (Wilson et al., 2020; Jin et al., 2022), but they rely on explicit target domain
data and boundary definitions.
Test-time adaptation (TTA) offers an alternative approach that adapts to distribution changes by up-
dating only lightweight modules using unlabeled test streams after deployment. TTA methods have
evolved mainly in the vision domain through batch normalization coefficient optimization and en-
tropy minimization (Wang et al., 2020), self-supervised/contrastive learning combined with pseudo-
labeling (Liang et al., 2021; Chen et al., 2022; Gong et al., 2025), single-sample multi-augmentation-
based adaptation (Zhang et al., 2022), and long-term adaptation stabilization (Wang et al., 2022).
Unlike vision tasks, time-series forecasting has unique characteristics that distinguish it from vision
tasks: 1) it employs normalization methods different from vision tasks to preserve periodicity and
level information, and 2) ground truth becomes sequentially observable after prediction with short
delays, enabling the use of direct losses such as Mean Squared Error (MSE).
Time-series forecasting TTA is a recently evolving topic; to the best of our knowledge, only few
methods (Kim et al., 2025; Medeiros et al., 2025; Grover & Etemad, 2025) have been proposed.
All of them adopted dual-adapter architectures that place calibration modules at both input and
output ends of the base model. They map inputs to domains that the base model can handle more
easily and restore outputs to the original domain, controlling adaptation intensity through gating.
However, these indirect distribution calibration methods involve design complexity and create un-
certainty about the impact of input transformations on internal model representations.
To this end, we propose Context-aware Output-Space Adapter (COSA), which offers a direct output-
space correction approach that operates with minimal computational overhead. Figure 1 presents the
overview of COSA. COSA takes the predictions from a frozen base model and a lightweight context
vector, summarizes recent observation statistics as input, computes residuals through linear correc-
tion, and controls correction strength using gating. At deployment, we freeze the base forecaster
and update only a lightweight output adapter (i.e., linear correction with a learnable gate) under
a leakage-free streaming protocol: after each prediction, adaptation uses only previously revealed
ground truth, never current or future labels. COSA is architecture-agnostic and demonstrates consis-
tent performance improvements over existing state-of-the-art time-series forecasting TTA methods
across various predictors and horizons.
The main contributions of this study are summarized as follows:
1. Architecture-agnostic output adapter. Unlike existing time-series TTA methods that
adopt dual input-output adapters, COSA consists of a single output adapter. COSA oper-
ates independently in the output space, correcting predictions from any base model without
changes to training pipelines or internal parameters. COSA also shows compatibility with
SOTA normalizers, consistently reducing prediction error.
2
Published as a conference paper at ICLR 2026
2. Context-aware linear residual with gating. A linear correction uses the base prediction
and a lightweight context vector that summarizes statistics of recent observed ground truth,
and a learnable gate modulates correction strength.
3. Consistent accuracy gains. Across six benchmarks, four horizons, and six baseline ar-
chitectures, COSA improves test MSE over baselines (13.91 ∼17.03%) and SOTA TTA
methods (10.48∼13.05%), in particular, with the largest gains at longer horizons.
4. Fast, efficient TTA.Adaptive learning rate enables faster convergence of COSA, leading to
higher accuracy within a few adaptation steps. Specifically, COSA enables 88.59∼90.10%
faster inference time against prior SOTA TTA methods.
2 R ELATED WORK
2.1 T IME -SERIES FORECASTING
To handle non-stationarity in time-series forecasting, existing methods typically employ 1) on-
line learning, 2) continual learning, and 3) domain adaptation. Representative online learning,
D3A (Zhang et al., 2024) narrows source–target gaps through z-score monitoring of loss distribu-
tions and Gaussian noise injection, whereas Adarnn (Du et al., 2021) reduces temporal distribution
shifts using temporal distribution characterization and distribution matching. In continual learning,
cPNN (Giannini et al., 2023) grows temporal columns and transfers knowledge via lateral connec-
tions, and FSNet (Pham et al., 2022) separates per-layer adapters for rapid adaptation from asso-
ciative memory for long-term retention to balance plasticity and stability. For domain adaptation,
CoDATS (Wilson et al., 2020) learns domain-invariant features adversarially, and DAF (Jin et al.,
2022) shares attention with domain-invariant queries/keys and domain-specific values. These fami-
lies generally update the base model during training or online operation, differing from TTA, which
adapts lightweight modules on unlabeled test streams while keeping the base model frozen.
2.2 T EST-T IME ADAPTATION
Tent (Wang et al., 2020) optimizes only batch-normalization affine parameters under entropy mini-
mization, and SHOT (Liang et al., 2021) combines information maximization with self-supervised
objectives to transfer source hypotheses to the target. AdaContrast (Chen et al., 2022) constructs
pseudo-labels via contrastive learning with a dynamic memory bank for gradual adaptation, while
MEMO (Zhang et al., 2022) applies multi-augmentation to a single test example to minimize
marginal output entropy, updating all weights. CoTTA (Wang et al., 2022) limits error accumulation
via weight and stochastic restoration, and ACCUP (Gong et al., 2025) integrates adaptive clustering
with pseudo-labeling. However, they are proposed for vision tasks. TTA for time-series forecasting
requires different approaches from those for vision tasks due to its own characteristics.
2.3 T EST-T IME ADAPTATION FOR TIME -SERIES FORECASTING
Time-series forecasting TTA methods typically employ dual adapters that calibrate distributions at
both input and output. TAFAS (Kim et al., 2025) couples a calibration module to map inputs to a
model-friendly domain and restores outputs to the original domain. It uses gating to modulate the
calibration strength and utilizes Periodicity-Aware Adaptive Scheduling (PAAS) to adjust adaptation
frequency using frequency patterns based on inputs. PETSA (Medeiros et al., 2025) factorizes the
calibration module with a low-rank structure and adopts a combined loss for stable adaptation with
fewer parameters. DynaTTA (Grover & Etemad, 2025) adjusts the dynamic learning rate, based on
local distribution shift, global distribution shift, loss z-score. Existing time-series forecasting TTA
methods employ an indirect approach that bidirectionally calibrates distributions at the input and
output sides of the base model. They entailed design complexity due to indirect calibration and
difficulty in predicting the impact of input transformations on internal representations. In contrast,
we aim to utilize a single output-space adapter that directly corrects predictions without requiring
input calibration or bidirectional transformation, resulting in a simpler design and more predictable
adaptation behavior.
3
Published as a conference paper at ICLR 2026
Table 1: Adapter-specific notation. Basic sizes/indices are defined as (W, L, K, B; t, i, k).
Symbol Meaning (shape)
Y(0)
t Base (frozen) L-step prediction at time t (RL).
Ytrue
t True L-step target revealed after t (RL).
Ct Context vector from revealed batch statistics [µt − K, . . . , µt − 1]⊤ (RK).
Xt Input look-back window (RW ).
X(a)
t Adapter input [Y(0)
t ∥ Ct] (RL+K).
Ht Linear residual W X(a)
t + b (RL).
ˆYt Corrected output Y(0)
t + α Ht with α = tanh(g) ∈ [−1, 1] (RL).
W , b, g Adapter weights (RL × (L + K)), bias (RL), and gate parameter (R).
Operators: concatenation [a ∥ b]; ∥ · ∥2 vector norm; ∥ · ∥F Frobenius.
Figure 2: Detailed architecture of COSA illustrating the linear correction layer (weight matrix W
and bias b), learnable gating parameter ( g), and context vector ( C) integration for output-space
correction.
3 COSA:C ONTEXT -AWARE OUTPUT -SPACE ADAPTER
3.1 N OTATION AND PROBLEM FORMULATION
Table 1 shows the symbols necessary for COSA and their meanings.
This study targets univariate time-series forecasting, following the existing SOTA time-series fore-
casting TTA methods (Kim et al., 2025; Medeiros et al., 2025; Grover & Etemad, 2025). For mul-
tivariate time-series inputs, we decompose them into per-variable univariate forecasting tasks and
perform the task iteratively for each variable. At time t, base model generates L-step original pre-
dictions Y(0)
t ∈ RL from input Xt ∈ RW , where W denotes the input look-back window length.
COSA generates corrected predictions ˆYt ∈ RL from input X(a)
t ∈ RL+K, where K denotes the
length of the context vector. After making predictions, the ground truth for that interval becomes se-
quentially observable following a short delay. Like other TTA approaches, we keep the base model
completely frozen and perform only adapter adaptation at test time. Adaptation is performed by col-
lecting the most recent B prediction, ground truth pairs (batch index i ∈ { 1, . . . , B} and context
index k ∈ {1, . . . , K}).
3.2 O VERALL ARCHITECTURE
Figure 2 illustrates the overall operation of COSA. COSA consists of a single output adapter that
directly corrects the predictions. The key components are: 1) a linear layer composed of weight
matrix W and bias variable b that computes correction values H, 2) learnable gating g that controls
correction strength, and 3) a context vector C that summarizes and stores recent trend information.
We choose a single linear layer for two key reasons: 1) Efficiency: Linear operations provide lower
latency and higher throughput compared to nonlinear modules, making them suitable for fast adapta-
tion. We confirmed that a single-layer adapter shows 34.95% faster wall-clock time on average than
a 2-layer MLP adapter. 2) Simplicity-Performance balance: As reported in LTSF-Linear (Zeng
4
Published as a conference paper at ICLR 2026
et al., 2023), a linear layer sufficiently performs well in time-series forecasting, despite its simplic-
ity. We also verified that a single linear layer adapter showed 5.71% even better performance on
average against a 2-layer MLP adapter. These characteristics make the linear layer beneficial for
TTA. Detailed results are provided in Appendix G.3.
The streaming protocol for leakage prevention is as follows (let the last adaptation was performed
in t−1):
1. Prediction: At time t, base model generates prediction Y(0)
t from input Xt.
2. Correction: Feed Y(0)
t and context Ct into COSA to generate the corrected prediction ˆYt.
3. Observation: After delay ∆ ≥0, values of ground truth of the prediction horizonYtrue
t are
sequentially observed.
4. Adaptation: Collect the most recent B prediction, ground truth pairs {ˆYt+i−1, Ytrue
t+i−1},
and perform adaptation that updates COSA parameters {W , b, g}.
3.3 O UTPUT -SPACE RESIDUAL CORRECTION
For time t, we concatenate the original prediction of base model and context vector to create the
adapter input:
X(a)
t = [Y(0)
t ∥ Ct].
The residual is computed using a linear transformation:
Ht = W X(a)
t + b.
The correction magnitude is controlled through gating to compose the final output:
ˆYt = Y(0)
t + tanh(g) Ht.
The tanh activation stabilizes the correction magnitude.
3.4 C ONTEXT CONSTRUCTION
To prevent information leakage, the context summarizes previously observed ground truth informa-
tion. For time t, we compute batch-wise aggregation as:
µt = agg

ytrue
t−(kB)+i) : 1 ≤ i ≤ B}, 1 ≤ k ≤ K.
where the aggregation function agg can use statistics such as mean, median, etc. We construct the
context vector by stacking the most recent K aggregated values:
Ct = [ µ1, µ2, . . . , µK ]⊤.
This context vector summarizes level/scale changes and gradual drift patterns to help interpret the
relative magnitude of the base prediction Y(0)
t (reducing to single time-series values when B =1).
3.5 A DAPTATION OBJECTIVE AND SCHEDULING
Because targets arrive with a delay, we employ a direct objective with weight decay:
L =
BX
i=1
 ˆYt−i−1 − Ytrue
t−i−1
2
2 + λ
 
∥W ∥2
F + ∥b∥2
2 + ∥g∥2
2

. (1)
When B forecast–target pairs have been enqueued, we runS gradient steps on the adapter parameters
using a cosine–adaptive learning-rate schedule, simplyCALR. We apply cosine annealing within the
S steps,
η(s+1) = ηmin + 1
2
 
η(s) − ηmin

1 + cossπ
S

. (2)
and then adjust η online, based on short-horizon loss trends to encourage fast but stable convergence
(decrease η on loss upticks; mildly increase on plateaus). When a new batch arrives, it is always
5
Published as a conference paper at ICLR 2026
initialized with the same learning rate, and thereafter the learning rate for the next step within the
batch is determined through Equation 2 according to the loss. Early stopping and gradient clip-
ping are also implemented. The threshold values for learning rate adjustment are stability-induced
by balancing adaptation speed against stability. Conservative thresholds ensure convergence while
aggressive values enable faster response to distribution shifts. Full pseudocode and thresholds are
given in Algorithm 1 in Appendix A.
COSA targets TSF-TTA under non-stationary environments in which the distribution of time-series
data changes over time. In such environments, the classical notion of convergence toward a fixed
optimal point is not well-defined. Instead, stable learning within each adaptation window is critical.
CALR guarantees uniformly bounded step-wise updates through the following four mechanisms,
which structurally prevent error amplification and thus ensure stability during adaptation.
1. Upper-bounded learning rate: The learning rate is constrained by η ≤ ηmax, limiting the
maximum magnitude of a single-step update.
2. Gradient clipping: At Line 18 of Algorithm 1, the gradient norm is adaptively bounded as
∥gϕ∥ ← min(∥gϕ∥, max(c, L)).
3. L2 regularization: The weight-decay term in Equation 1, λ(∥W∥2
F + ∥b∥2
2 + ∥g∥2
2), con-
strains parameter magnitude.
4. Bounded gating: Because α = tanh(g) ∈ [−1, 1], the correction magnitude is structurally
limited.
For every new batch, the learning rate is reinitialized to ηmax (Line 2 of Algorithm 1), giving
each batch an equal opportunity for adaptation. The learning rate is then adapted according to the
batch’s loss behavior. When the loss spikes, we reduce the learning rate as η ← max(0.5η, ηmin),
temporarily lowering update intensity. When the loss decreases stably, we increase it as η ←
min(1.1η, ηmax), strengthening adaptation. This enables stable learning even when short-term per-
turbations or anomalies appear in the input data, allowing rapid recovery.
4 E XPERIMENTS
4.1 E XPERIMENTAL SETTINGS
We evaluate COSA on six benchmark datasets (ETTh1/2, ETTm1/2, Exchange Rate, and Weather)
with a fixed look-back window (W = 96) and four prediction horizons ( L ∈ {96, 192, 336, 720}).
We used six representative base models spanning different architectures: Transformer-based (iTrans-
former (Liu et al., 2023), PatchTST (Nie et al., 2023)), linear-based (DLinear (Zeng et al., 2023),
OLS (Toner & Darlow, 2024)), and MLP-based (FreTS (Yi et al., 2023), MICN (Wang et al., 2023)).
By default, all input time series are treated as variable-wise univariate forecasting tasks, standard
normalization is applied, and MSE serves as the performance comparison metric.
We compare COSA (our method) with Baseline (without TTA), TAFAS (Kim et al., 2025), and
PETSA (Medeiros et al., 2025). All experiments were conducted according to the official bench-
mark library (Wang et al., 2024) 1. The train:valdiation:test ratio is 7:1:2 for all datasets.
Unless otherwise noted, we fix the adapter hyperparameters toK=10 and S=3, enabled CALR. We
utilize the average as agg. Ablation studies for the variations of agg are provided in Appendix G.1.
We report two variants for COSA: COSA-F, which uses a
```
