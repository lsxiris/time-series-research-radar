# DistDF: Time-series Forecasting Needs Joint-distribution Wasserstein Alignment — OpenReview Raw Thread

- Forum: https://openreview.net/forum?id=VrdLwUmzBy
- PDF: https://openreview.net/pdf?id=VrdLwUmzBy
- Section: 二、时间序列预测：分布鲁棒、多变量建模与后处理优化
- Zhihu score: 6.0
- Venue status: ICLR 2026 Poster

## Submission metadata
- Authors: Eric Wang, Licheng Pan, Yuan Lu, Zhixuan Chu, Xiaoxi Li, Shuting He, Zi Ciu Chan, Qingsong Wen, Haoxuan Li, Zhouchen Lin
- Primary area: learning on time series and dynamical systems
- Keywords: time-series forecasting

## Abstract
Training time-series forecast models requires aligning the conditional distribution of model forecasts with that of the label sequence. The standard direct forecast (DF) approach seeks to minimize the conditional negative log-likelihood  of the label sequence, typically estimated using the mean squared error. However, this estimation proves to be biased in the presence of label autocorrelation.  In this paper, we propose DistDF, which achieves alignment by alternatively minimizing a discrepancy between the conditional forecast and label distributions. Because conditional discrepancies are difficult to estimate from finite time-series observations, we introduce a newly proposed joint-distribution Wasserstein discrepancy for time-series forecasting, which provably upper bounds the conditional discrepancy of interest. This discrepancy admits tractable, differentiable estimation from empirical samples and integrates seamlessly with gradient-based training. Extensive experiments show that DistDF improves the performance diverse forecast models and achieves the state-of-the-art forecasting performance. Code is available at https://anonymous.4open.science/r/DistDF-F66B.

## Reviews
### Reviewer_ZpGW
- summary: The paper addresses time series forecasting and proposes aligning the predictive conditional distribution with the true conditional distribution by minimizing the joint-distribution Wasserstein discrepancy. This approach mitigates the bias introduced by autocorrelation when using maximum log-likelihood objectives to train forecasting models.
- strengths: * Good observation that both frequency and PCA components exhibit autocorrelation, which affects their learning bias; this provides a well-motivated basis for applying optimal transport theory.

* The incorporation of DistDF in existing frameworks is straightforward

* Comprehensive experiments; I appreciate the effort to compare with other distributional discrepancies and the application of DistDF to other approaches
- weaknesses: * The central hypothesis of this work is that aligning conditional distributions is beneficial, and the authors provide theoretical justifications along with empirical evidence through forecasting error metrics. However, it is unclear whether the conditional distributions actually align for the best alpha values reported in Tables 5 and 6. In other words, the hypothesis is not directly evaluated in the experiments through distributional discrepancy, but rather indirectly through forecasting performance.

* Improvements wrt to existing SOTA methods look rather small; however, they are consistent across models and datasets
- questions: Please address my first point in the weaknesses. If no distributional discrepancy needs to be shown in the experiments, please elaborate why.
- rating: 6 | confidence: 4

### Reviewer_aY9s
- summary: The paper proposes a Wasserstein-based discrepancy measure for time series that captures label autocorrelation and demonstrates the benefits of using it for time series alignment compared to established methods. Several experiments were conducted to support this claim.
- strengths: The presented Wasserstein discrepancy seems original and effective. The experiments seem comprehensive and well carried out.
- weaknesses: I think the paper should discuss the assumption of Gaussian distributed data more. It seems absolutely necessary to derive the discrepancy measure and yet I suppose the benchmark datasets do not satisfy this property.

I consider this a mild weakness but the theory regarding the general Wasserstein metric is presented mostly for discrete measures. Given that a Gaussian data distribution is assumed, it could be discussed how the presented results for empirical measures relate to the original Gaussian data distribution.

Minor
-------
The Bures-Wasserstein discrepancy is spelled as “Bruce-Wasserstein” in Lemma 3.5. Also in this Lemma, the equality to the W_2 metric should be made clear.
- questions: Perhaps I am missing something, but Table 1 seems confusing. DistDF, which is a discrepancy measure, is compared to other models. It should be pointed out which model was used with DistDF loss.
- rating: 8 | confidence: 3

### Reviewer_c2pc
- summary: This paper proposes DistDF, a new training objective for time-series forecasting that aims to align the conditional distributions of forecasts and labels, rather than relying on point-wise MSE. Since conditional discrepancies are difficult to estimate from limited data, the authors introduce a joint-distribution Wasserstein discrepancy, optimized between the distributions of (history, labels) and (history, predictions). The method is model-agnostic and can be plugged into existing forecasting models. Experiments show performance improvements on multiple benchmarks.
- strengths: - Strong and clearly articulated motivation regarding autocorrelation bias in likelihood-based objectives.
- Solid theoretical foundation, including alignment guarantees and non-negativity properties of the objective.
- Method is architecture-agnostic, enabling integration with a broad range of forecasting models.
- Extensive benchmarking shows consistent improvements, supported by ablation studies demonstrating contribution of components.
- Generally clear writing and clean presentation of the 
- weaknesses: - A key limitation is that the proposed discrepancy objective lacks guaranteed convergence or clear interpretability during training, making its practical effect on conditional alignment somewhat uncertain. Because the loss must be combined with MSE, the discrepancy may act more like a regularizer than a principled stand-alone objective. Additional empirical analysis of its optimization dynamics and correlation with performance would strengthen the claims.
- More comprehensive experiments are needed to isolate the contribution of the proposed objective. Given that the method relies on a weighted combination with MSE, it should be compared not only against plain MSE training but also against other established time-series learning objectives (e.g., Dilate, Soft-DTW) when similarly combined with MSE. Such comparisons would help determine whether the observed gains stem from the specific discrepancy formulation or simply from augmenting the loss with an auxiliary term.
- Evaluation is rest
- questions: - Since the proposed objective must be combined with MSE for stable training, can the authors provide evidence that the improvement does not simply arise from a regularization effect? For example, how does the discrepancy term alone behave, and how strongly does its reduction correlate with forecasting accuracy?
- The distinction between DistDF and existing learning-objective methods such as Time-o1, FreDF, Koopman-based losses, and Soft-DTW remains somewhat unclear. Can the authors more explicitly highlight the conceptual and practical differences, particularly regarding theoretical guarantees and optimization behavior?
- The discussion of likelihood bias focuses primarily on MSE. Do similar issues arise in probabilistic forecasting frameworks using alternative objectives (e.g., quantile 
- rating: 4 | confidence: 4

### Reviewer_6qSb
- summary: This paper proposes Distribution-aware Direct Forecast (DistDF), which achieves alignment by minimizing joint-distribution Wasserstein discrepancy between conditional forecast and label distributions to enhance forecast accuracy.
- strengths: 1. This paper is well written and polished. Notations and equations are clearly presented and explained.
2. This paper is well-motivated and offers an extremely thorough explanation.
3. Experiments are comprehensive.
- weaknesses: 1. Experimental comparison (Tab. 2) lacks some most recent works, e.g., [*1]. The proposed method might not outperform these new works. TQNet [*1] achieves **0.377** MSE, **0.393** MAE on ETTm1.
2. Experimental results could not fully support the significance of the method. The improvement is marginal when compared to prior art, e.g., TimeBridge, Time-o1, and TQNet [*1]. 
3. Improvement on presentation:
 - For results in the table, should not use **Bold** and $\underline{\text{Underline}}$ when two numbers are the same, use Bold for both.
 - (minor) In Section 4.3, the reference to Table 4 should be changed to Table 2.
 - (minor) Use consistent table style. Use \toprule for Tab. 5 & 6


[*1] Lin, Shengsheng, et al. "Temporal Query Network for Efficient Multivariate Time Series Forecasting." Forty-second International Conference on Machine Learning.
- questions: See weaknesses.
- rating: 6 | confidence: 3

## Author comments / rebuttal
### Author Final Remarks
Dear AC and all reviewers,

We sincerely appreciate your great efforts in evaluating our paper despite your busy schedules.  We are encouraged that 3 out of 4 reviewers are currently in the positive side, with all scores 8, 6, 6, and 4, recognizing our paper
- `provides a well-motivated basis` (Reviewer ZpGW),
- `seems original and effective`, with experiments `comprehensive and well carried out` (Reviewer aY9s),
- has `strong and clearly articulated motivation` and `solid theoretical foundation` (Reviewer c2pc),
- `well-motivated and offers an extremely thorough explanation` (Reviewer 6qSb).

Meanwhile, Reviewer c2pc gave an initial rating 4 with no further response. Due to the updated policy of ICLR-26, we understand Reviewer c2pc cannot provide us with further discussions. For facilitate checking, we summarize that the c2pc’s initial concerns are mainly on (1) Optimization dynamics and correlation with performance, (2) Presentation of experiment results, and (3) Performance on different scenarios, with our responses detailed as follows.

> Additional empirical analysis of its **optimization dynamics** and **correlation** with performance would strengthen the claims.
- We add experiments on the **optimization dynamics** of the proposed loss function (Figure 8).
- We quantify the **correlation** between the performance improvement trajectory and the optimization dynamics of the proposed loss function. It reveals a strong and consistent correlation, demonstrating that forecast accuracy consistently improves as the loss function is minimized

> Explicitly **specifying the base architecture** for each dataset (e.g., as done in **Scaleformer**, ICLR 2023) would improve clarity and ensure a fair interpretation of the reported gains.
- We add experiments **specifying 5 different base architectures** (Table 15), following the format of **Scaleformer**. 
- We add a tablenote in Table 1 to **specify the base architectures** on different datasets.

> How well does DistDF extend to **multivariate forecasting**, **probabilistic output formulations**, or **multi-scale architectures**? Additional experiments under an **autoregressive setting** would be valuable.
- We add experiments to apply DistDF to **probabilistic output formulations**,  **multi-scale architectures** and **autoregressive settings**. In all three scenarios, DistDF consistently improved the performance of the base architectures. 
- Regarding multivariate forecasting, **we respectfully clarify that the main results presented in the manuscript were already conducted under a multivariate setting**, confirming the method's effectiveness in this scenario.

We are confident that our responses can thoroughly address Reviewer c2pc's concerns.  Considering Reviewer c2pc doesn’t response to us after we posting the rebuttal, we respectfully ask you to consider this context when making your final recommendation.

Thank you in advance,

Authors of #8696

### Author comment
Thank you so much for your encouraging evaluation and appreciation of our **presentation, motivation, and empirical studies**. Below are our responses to the specific query raised.

#### [W1] Experimental comparison (Tab. 2) lacks some most recent works, e.g., [1]. The proposed method might not outperform these new works. **TQNet** [*1] achieves 0.377 MSE, 0.393 MAE on ETTm1.

**Response.** Thank you very much for your meticulous observation. Our response to this query is structured as follows:

- Firstly, we would clarify that as a learning objective, the performance of DistDF is highly impacted by the forecasting model used. Therefore, to investigate the applicability of DistDF over TQNet, we should compare TQNet trained with MSE and TQNet trained with DistDF.
- **Additional experiments.** We add experiments to evaluate how DistDF performs when specifying TQNet and TimeBridge as the forecasting models. The results are available in the table below, where TQNet$^\dagger$ and TimeBridge$^\dagger$ are trained via DistDF. Overall, TQNet$^\dagger$ and TimeBridge$^\dagger$ consistently outperform TQNet and TimeBridge, respectively, **validating the utility of DistDF over state-of-the-art forecasting models.**
- **Revision.** We add the table below in the revised manuscript (Table 15), to demonstrate the efficacy of DistDF to improve TQNet and TimeBridge.


| Dataset | TQNet (MSE) | TQNet (MAE) | TQNet$^\dagger$ (MSE) | TQNet$^\dagger$ (MAE) | TimeBridge (MSE) | TimeBridge (MAE) | TimeBridge$^\dagger$ (MSE) | TimeBridge$^\dagger$ (MAE) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **ETTh1** | 0.449 | 0.439 | 0.438 | 0.431 | 0.442 | 0.440 | 0.434 | 0.436 |
| **ETTh2** | 0.375 | 0.400 | 0.371 | 0.399 | 0.377 | 0.403 | 0.373 | 0.398 |
| **ETTm1** | 0.376 | 0.391 | 0.375 | 0.391 | 0.387 | 0.400 | 0.383 | 0.397 |
| **ETTm2** | 0.277 | 0.321 | 0.272 | 0.318 | 0.281 | 0.326 | 0.280 | 0.323 |
| **ECL** | 0.175 | 0.265 | 0.171 | 0.262 | 0.176 | 0.271 | 0.172 | 0.267 |
| **Weather** | 0.246 | 0.270 | 0.244 | 0.269 | 0.252 | 0.277 | 0.248 | 0.275 |

#### [W2] Experimental results could not fully support the significance of the method. The improvement is marginal when compared to prior art, e.g., **TimeBridge, Time-o1, and TQNet [*1].**

**Response.** Thank you very much for your detailed and meticulous comment. We would like to address this concern as follows.

- Firstly, we would clarify that **DistDF can effectively improve the performance of different architectures**, such as **TimeBridge and TQNet**, as discussed in the response to [W1].
- Secondly, we recognize that compared to Time-o1, the performance improvement achieved by DistDF is **moderate (yet consistent)**. However, it is important to emphasize that **with respect to the widespread direct forecasting framework based on MSE optimization, DistDF yields substantial gains**, which provides empirical validation on the benefit of the proposed discrepancy-based objective to e

### Author comment
#### [Q4] How well does DistDF extend to **multivariate forecasting**, **probabilistic output formulations**, or **multi-scale architectures**? Providing results or analysis in these more general settings would help verify that the proposed approach is broadly applicable beyond the current scope.

**Response.** We express sincere gratitude once again for the meticulous and helpful suggestions. We kindly note that: (i) In the current manuscript, the experiments are conducted under **multivariate forecasting** setting, i.e., involving multiple covariates in the label sequence. (ii) In the response to [Q3], the utility of DistDF for **probabilistic output formulations** has been investigated. Therefore, we focus here on the remaining aspect regarding **multi-scale architectures**.

- **Additional experiments.** We select TimeMixer and SCINet, two competitive multi-scale architectures based on CNN and MLP respectively as the testbed. In the variants TimeMixer$^\dagger$ and SCINet$^\dagger$, we train the architectures via DistDF. The results are presented in the table below, where TimeMixer$^\dagger$ and SCINet$^\dagger$ consistently outperform TimeMixer and SCINet, respectively, **validating the utility of DistDF to improve the performance of multi-scale architectures.**

- **Revision.** We add the table below in the revised manuscript (Table 18), to demonstrate the efficacy of DistDF to improve multiscale architectures.
| Dataset   | TimeMixer (MSE) | TimeMixer (MAE) | TimeMixer$^\dagger$ (MSE) | TimeMixer$^\dagger$ (MAE) | SCINet (MSE) | SCINet (MAE) | SCINet$^\dagger$ (MSE) | SCINet$^\dagger$ (MAE) |
|-----------|-----------------|-----------------|---------------------------|---------------------------|--------------|--------------|------------------------|------------------------|
| **ETTm1**   | 0.422           | 0.423           | 0.401                     | 0.411                     | 0.418        | 0.416        | 0.389                  | 0.399                  |
| **ETTh1**   | 0.501           | 0.476           | 0.456                     | 0.446                     | 0.467        | 0.450        | 0.459                  | 0.443                  |
| **ECL**     | 0.176           | 0.273           | 0.172                     | 0.267                     | 0.173        | 0.273        | 0.169                  | 0.268                  |
| **Weather** | 0.262           | 0.285           | 0.252                     | 0.280                     | 0.253        | 0.280        | 0.250                  | 0.278                  |

### Author comment
The comparison results are provided in the table above, and the detailed analysis is presented as follows.
- **Time-o1 and FreDF** are label transformation methods, which transform the label sequence into latent components with reduced autocorrelation bias. They are model agnostic and have analytical forms. However, as discussed in the manuscript (section 3.1), they are not fully debiased since they can only generate marginal decorrelated components, not conditional decorrelated components, rendering residual bias.
- **Koopman** is a dynamic system training acceleration method, which accelerates the training of dynamic system models by using FFT. It has an analytical form but is not model agnostic since it requires the underlying model to be an RNN-like dynamic system that performs recurrent inference for multi-step forecasts. Moreover, its research problem is not related to eliminating the autocorrelation bias. 
- **Soft-DTW** is a shape alignment method, which aligns the shape of the predicted and label sequences. It is model agnostic but does not have an analytical form: it requires solving a constrained optimization problem to obtain the value. Besides, although it considers label autocorrelation by treating forecasting as a shape alignment problem, no theoretical guarantees are provided to ensure that it eliminates the bias caused by label autocorrelation.
- **DistDF** is a distribution alignment method, which aligns the conditional distribution of the predicted and label sequences. It has an analytical form and is model agnostic. Moreover, it has theoretical guarantees to eliminate the autocorrelation bias (see Theorem 3.4, alignment property).

#### [Q3] The discussion of likelihood bias focuses primarily on MSE. **Do similar issues arise in probabilistic forecasting frameworks** using alternative objectives (e.g., quantile loss, CRPS)? If so, is DistDF compatible with or beneficial under such setups?

**Response.** Thank you for your sincere comment. We agree that it is valuable to explore the utility of DistDF to enhance probabilistic forecasting frameworks.  Our response is structured as follows:
- **Additional experiments.** We select D3U, the state-of-the-art probabilistic forecasting framework as the testbed. In the variant denoted as  D3U$^\dagger$, we regularize the learning objective of D3U with DistDF. The results are presented in the table below, where D3U$^\dagger$ exhibits consistent performance improvement, **validating the utility of DistDF in recent probabilistic forecasting frameworks.**
- **Revision.** We add the table below in the revised manuscript (Table 17), to demonstrate the efficacy of DistDF to improve probabilistic forecasting frameworks.

| Dataset   | Horizon | D3U (MSE) | D3U (MAE) | D3U (CRPS) | D3U (CRPS$_{sum}$) | D3U$^\dagger$ (MSE) | D3U$^\dagger$ (MAE) | D3U$^\dagger$ (CRPS) | D3U$^\dagger$  (CRPS$_{sum}$) |
|-----------|---------|---------|---------|----------|------------------------|------------------

### Author comment
#### [Q1] Since the proposed objective must be combined with MSE for stable training, can the authors provide evidence that the improvement does not simply arise from a regularization effect? For example, **how does the discrepancy term alone behave, and how strongly does its reduction correlate with forecasting accuracy?**

**Response.** Thank you for this insightful suggestion. As the aspect concerning “how strongly does its reduction correlate with forecasting accuracy” is addressed in our response to [W1], we focus here on the remaining aspect regarding the behavior of the discrepancy term when used in isolation. Our response is structured as follows:

- **First, we add experiments to assess the effect of employing the discrepancy term as the sole objective.** Specifically, we evaluate three settings across four datasets: (1) direct forecasting using only MSE ($\alpha=0$), (2) the discrepancy term alone ($\alpha=1$), and (3) DistDF as a regularizer ($\alpha=\alpha^*$). The empirical results indicate that the discrepancy term alone does not lead to consistent improvements: performance degrades on the ECL and Weather datasets. In contrast, utilizing the discrepancy term as a regularizer alongside MSE consistently enhances direct forecasting performance, empirically validating our methodological choice, in line with established practices [1-2].
- **Second, we elucidate the critical role that the MSE term plays in fully realizing the performance benefits of DistDF**. By Lemma 3.5, the Bures-Wasserstein discrepancy quantifies the divergence between the mean and covariance of the joint distributions of the forecast and label sequences. This term involves important distributional characteristics, but it discards elementwise correspondences between forecast and label sequences—information critical for forecasting tasks. While mini-batch stochastic gradient descent may partly compensate for this loss via sampling diversity, it cannot fully restore pairwise correspondence information. Therefore, the inclusion of MSE as an additional objective is needed to recover the pairwise correspondence, which is essential to train an accurate forecasting model.

- **Revision.** We add limitation discussion in the conclusion section, explicitly stating that DistDF’s primary benefit is as a regularization term complementing standard MSE loss.

| $\alpha$ | ETTm1 MSE | ETTm1 MAE | ETTm2 MSE | ETTm2 MAE | ECL MSE | ECL MAE | Weather MSE | Weather MAE |
|--------|---------|---------|---------|---------|-------|-------|------------|--------|
| $\alpha=0$      | 0.387 | 0.398 | 0.280 | 0.324 | 0.191 | 0.284 | 0.261 | 0.282 |
| $\alpha=1$      | 0.404 | 0.408 | 0.283 | 0.326 | 0.239 | 0.326 | 0.268 | 0.290 |
| $\alpha=\alpha^*$    | **0.380** | **0.395** | **0.277** | **0.322** | **0.175** | **0.267** | **0.255** | **0.278**



[1] FreDF: Learning to Forecast in the Frequency Domain. ICLR 2025.

[2] Time-o1: Time-Series Forecasting Needs Transformed Label Alignment. NeurI

### Author comment
#### [W4] In Table 1, it is **unclear which underlying model architectures DistDF is applied to**. Since DistDF is a learning objective rather than a new architecture, and the table compares against architectural baselines, the presentation may confuse readers regarding what is being evaluated. Clarifying the base model used for each dataset would improve readability. **Explicitly specifying the base architecture for each dataset (e.g., as done in Scaleformer, ICLR 2023)** would improve clarity and ensure a fair interpretation of the reported gains.
**Response.** Thank you for this sincere suggestion. We address this concern by (i) clarifying the underlying model architectures in Table 1 and (ii) providing a new table following Scaleformer. 
- **Firstly, we clarify that in Table 1, DistDF employs the top-performing baseline on each dataset as the forecasting model** (highlighted in blue). This approach is consistent to pioneer works (FreDF [ICLR 2025], Time-o1 [NeurIPS 2025]). It allows us to evaluate whether DistDF is able to consistently enhance the performance of the best existing forecasting models across various datasets, even though the top-performing model may differ from one dataset to another.

- **Secondly, we provide new results following the protocol of Scaleformer**, to evaluate how DistDF performs given specific forecasting models. We select forecasting models recently released: TimeBridge [ICML 2025], TQNet [ICML 2025], FredFormer [KDD 2024], iTransformer [ICLR 2024] and FreTS [NeurIPS 2023]. The results are available as follows, where DistDF can effectively improve different forecasting models.

- **Revision.** We add a tablenote in Table 1: `DistDF employs the underlined baseline that performs best on each dataset as the forecast model.`, to address issue (i) above. Moreover, we add the table below in the revised manuscript (Table 15), to address issue (ii) above.


| Dataset | TQNet (MSE) | TQNet (MAE) | TQNet$^\dagger$ (MSE) | TQNet$^\dagger$ (MAE) | TimeBridge (MSE) | TimeBridge (MAE) | TimeBridge$^\dagger$ (MSE) | TimeBridge$^\dagger$ (MAE) | Fredformer (MSE) | Fredformer (MAE) | Fredformer$^\dagger$ (MSE) | Fredformer$^\dagger$ (MAE) | iTransformer (MSE) | iTransformer (MAE) | iTransformer$^\dagger$ (MSE) | iTransformer$^\dagger$ (MAE) | FreTS (MSE) | FreTS (MAE) | FreTS$^\dagger$ (MSE) | FreTS$^\dagger$ (MAE) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **ETTh1** | 0.449 | 0.439 | 0.438 | 0.431 | 0.442 | 0.440 | 0.434 | 0.436 | 0.447 | 0.434 | 0.430 | 0.429 | 0.452 | 0.448 | 0.447 | 0.444 | 0.489 | 0.474 | 0.479 | 0.467 |
| **ETTh2** | 0.375 | 0.400 | 0.371 | 0.399 | 0.377 | 0.403 | 0.373 | 0.398 | 0.377 | 0.402 | 0.367 | 0.393 | 0.386 | 0.407 | 0.379 | 0.405 | 0.524 | 0.496 | 0.466 | 0.467 |
| **ETTm1** | 0.376 | 0.391 | 0.375 | 0.391 | 0.387 | 0.400 | 0.383 | 0.397 | 0.387 | 0.398 | 0.378 | 0.394

### Author comment
|           |        | Time-o1|      | FreDF|        | Koopman |     | Dilate|       | LDTW  |       | Soft-DTW |    | DTW  |        | DF  |         |
|-----|--------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|       |    | MSE  | MAE   | MSE  | MAE   | MSE  | MAE   | MSE  | MAE   | MSE  | MAE   | MSE  | MAE   | MSE  | MAE   | MSE  | MAE   |
| **TimeBridge** | ETTm1  | 0.386 | 0.394 | 0.398 | 0.396 | 0.543 | 0.489 | 0.937 | 0.632 | 0.387 | 0.400 | 1.047 | 0.637 | 0.620 | 0.488 | 0.387 | 0.400 |
|           | ETTh1  | 0.451 | 0.441 | 0.443 | 0.438 | 0.757 | 0.593 | 0.915 | 0.650 | 0.464 | 0.452 | 0.971 | 0.632 | 0.879 | 0.597 | 0.442 | 0.440 |
|           | ECL    | 0.172 | 0.262 | 0.336 | 0.371 | 7.845 | 1.577 | 1.124 | 0.841 | 0.352 | 0.402 | 1.252 | 0.824 | 1.162 | 0.787 | 0.176 | 0.271 |
|           | Weather| 0.255 | 0.276 | 0.256 | 0.277 | 0.283 | 0.303 | 0.329 | 0.340 | 0.252 | 0.277 | 0.305 | 0.311 | 0.264 | 0.283 | 0.252 | 0.277 |
| **Fredformer** | ETTm1  | 0.385 | 0.393 | 0.385 | 0.393 | 0.467 | 0.449 | 0.719 | 0.564 | 0.389 | 0.400 | 0.735 | 0.558 | 0.637 | 0.498 | 0.387 | 0.398 |
|           | ETTh1  | 0.431 | 0.429 | 0.438 | 0.434 | 0.571 | 0.513 | 0.715 | 0.577 | 0.477 | 0.457 | 0.870 | 0.609 | 0.832 | 0.585 | 0.447 | 0.434 |
|           | ECL    | 0.178 | 0.270 | 0.179 | 0.271 | 0.399 | 0.462 | 0.864 | 0.766 | 0.219 | 0.311 | 0.304 | 0.366 | 0.327 | 0.384 | 0.191 | 0.284 |
|           | Weather| 0.255 | 0.276 | 0.256 | 0.277 | 0.264 | 0.285 | 0.293 | 0.322 | 0.265 | 0.286 | 0.295 | 0.308 | 0.270 | 0.287 | 0.261 | 0.282 |




#### [W3] Evaluation is restricted to direct forecasting, limiting evidence of robustness across different training paradigms. **Additional experiments under an autoregressive setting** would be valuable to validate whether the proposed objective is broadly applicable across different forecasting architectures and training pipelines.

**Response.** Thank you very much for your detailed suggestion. We address this concern through the following points.
- Overall, DistDF is dedicated to **address the autocorrelation within the label sequence**. In the autoregressive setting, there is only one-step label in the label sequence in each update, so the **label autocorrelation does not seem to be present or significant**, which hampers the direct use of DistDF in this setting. Nevertheless, in the autoregressive setting, **different covariates in the label could have significant correlations**. It would be intuitive to investigate **whether DistDF can accommodate the covariate correlation and improve performance** in the autoregressive setting, to showcase the broad applicability of DistDF.
- **Additional experiment.** We select TimeBridge and FredFormer as the forecasting models in this test due to their competitive performance. **We modify them to perform autoregression-based prediction**, and apply DistDF for training. Notably, here we use DistDF to model the covariate correlations, so the transport matrix siz

### Author comment
We sincerely appreciate the reviewer for the meticulous comments and appreciation of our **motivation**, **theoretical foundation**, **implementation**, **benchmarking** and **presentation**. We have taken every effort to address the raised concerns through additional explanations and experiments. Below are our responses to the specific query raised.

---

#### [W1] A key limitation is that the proposed discrepancy objective **lacks guaranteed convergence** or clear interpretability during training, making its practical effect on conditional alignment somewhat uncertain. Because the loss must be combined with MSE, the discrepancy may act more like a regularizer than a principled stand-alone objective. Additional empirical analysis of **optimization dynamics** and **correlation with performance** would strengthen the claims.

**Response.** Thank you for your thoughtful comment. We agree that it is essential to discuss the convergence, optimization dynamics, and their correlation with performance. We structure our response as follows.
- Firstly, **we add experiments to discuss the convergence** of BW discrepancy and **analyze its optimization dynamics**. 
  - **Setup.** Using BW discrepancy as the learning objective, we monitored its trajectory across epochs on the ECL, ETTh1, and ETTm1 datasets. The results are illustrated below.
  - **Result analysis.** **The optimization dynamics confirm the convergence of the BW discrepancy**: (i) the loss value decreases consistently throughout the training process; and (ii) it stabilizes at a specific equilibrium with minimal fluctuation after several epochs.
| Epoch  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|-|--|--|--|--|--|--|--|--|--|-|
| ECL  | 0.287  | 0.229  | 0.225  | 0.217  | 0.219  | 0.207  | 0.201  | 0.208  | 0.201  | 0.201 |
| ETTh1  | 0.209  | 0.172  | 0.175  | 0.168  | 0.166  | 0.169  | 0.170  | 0.166  | 0.164  | 0.164 |
| ETTm1  | 0.461  | 0.421  | 0.385  | 0.407  | 0.372  | 0.394  | 0.367  | 0.379  | 0.372  | 0.382 |
- Secondly, **we add experiments to discuss the correlation between performance and BW dynamics.** 
  - **Setup.** Following the above setup, we further track the trajectory of MAE and MSE on the validation set. Then, we calculate the Pearson correlation coefficient between the BW discrepancy trajectory on the training and validation sets and the MAE/MSE trajectories on the validation set. This quantifies the correlation between the BW discrepancy and the performance metrics. The results are illustrated below.
  - **Result analysis.** **The results confirm the positive correlation between the BW discrepancy and the performance.** In particular, the correlation coefficient between the BW discrepancy trajectory on the training set and the MSE trajectory on the validation set is 0.999, which indicates a strong positive correlation. This implies that minimizing the BW discrepancy can effectively improve the MAE and MSE performance.
| Correlation coef. | MSE (valid.) | MAE (valid.) |

### Author comment
- One may wonder **how the Bures-Wasserstein discrepancy behaves when the Gaussianity assumption is not fully satisfied.** As addressed in the response to [W1], the Bures-Wasserstein discrepancy measures differences only in the first- and second-order moments—i.e., the mean and covariance. While these two moments fully characterize Gaussian distributions, non-Gaussian distributions additionally require higher-order moments for complete characterization. Nonetheless, the mean and covariance remain essential descriptors for any distribution. As a result, in cases where data deviate from strict Gaussianity, the Bures-Wasserstein discrepancy remains a valuable tool for distribution alignment by matching these fundamental moments.

#### **[W3] The Bures-Wasserstein discrepancy is spelled as "Bruce-Wasserstein" in Lemma 3.5. Also in this Lemma, the equality to the $\mathcal{W}_2$ metric should be made clear.**
**Response.** Thank you very much for your meticulous comment! We have revised these typographical errors in the revised manuscript and highlight the equality.
- We have replaced `Bruce-Wasserstein` with `Bures-Wasserstein`.
- We have highlighted the equality to the $\mathcal{W}_2$ metric in Lemma 3.5.

#### [Q1] Perhaps I am missing something, but Table 1 seems confusing. DistDF, which is a discrepancy measure, is compared to other models. **It should be pointed out which model was used with DistDF loss.**

**Response.** Thank you very much for your careful observation. We agree that it is necessary to point out which forecasting model was used with DistDF loss in Table 1.

- Firstly, we clarify that in Table 1, DistDF employs the top-performing baseline (highlighted in blue) on each dataset as the forecasting model. This approach allows us to evaluate whether DistDF is able to consistently enhance the performance of the best existing forecasting models across various datasets, even though the top-performing model may differ from one dataset to another.

- **Additional experiments.** We add experiments to evaluate how DistDF performs given specific forecasting models. We select forecasting models recently released: TimeBridge [ICML 2025], TQNet [ICML 2025], FredFormer [KDD 2024], iTransformer [ICLR 2024] and FreTS [NeurIPS 2023]. **The results are available as follows, where we explicitly point out which forecasting model is used.** Overall, DistDF can effectively improve different forecasting models.

| Dataset | TQNet (MSE) | TQNet (MAE) | TQNet$^\dagger$ (MSE) | TQNet$^\dagger$ (MAE) | TimeBridge (MSE) | TimeBridge (MAE) | TimeBridge$^\dagger$ (MSE) | TimeBridge$^\dagger$ (MAE) | Fredformer (MSE) | Fredformer (MAE) | Fredformer$^\dagger$ (MSE) | Fredformer$^\dagger$ (MAE) | iTransformer (MSE) | iTransformer (MAE) | iTransformer$^\dagger$ (MSE) | iTransformer$^\dagger$ (MAE) | FreTS (MSE) | FreTS (MAE) | FreTS$^\dagger$ (MSE) | FreTS$^\dagger$ (MAE) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---

### Author comment
Thank you so much for your positive evaluation and appreciation of **our novelty and empirical studies**. Below are our responses to the specific query raised.

----

#### [W1] I think the paper **should discuss the assumption of Gaussian distributed data more.** It seems absolutely necessary to derive the discrepancy measure and yet I suppose the benchmark datasets do not satisfy this property.

**Response.** Thank you very much for your thoughtful comment. We acknowledge that the Gaussian distribution assumption may not precisely hold for real-world datasets. Nonetheless, we would like to clarify two points: (i) the adoption of the Gaussian assumption is a well-established and prevalent practice in the time-series forecasting literature, and (ii) the Bures-Wasserstein (BW) discrepancy remains instrumental for non-Gaussian data.

- **First, we recognize that assuming Gaussianity underpins many standard methodologies and theoretical developments in time-series forecasting.** For instance, **data standardization**—a ubiquitous preprocessing step—assumes Gaussianity; several theoretical analyses (e.g., Theorem 3.1 in the pioneering work [1]) are grounded in this assumption. Our adoption of the Gaussian hypothesis is thus consistent with established works and **does not introduce stringent assumptions that are not used in established forecasting pipelines**.

- Second, although the BW discrepancy is theoretically derived under the Gaussian assumption, **we note that it is effective to align non-Gaussian data.** Specifically, the BW discrepancy measures the difference of the **first and second moments (mean and covariance)**. While higher-order moments are necessary for a complete characterization of non-Gaussian distributions, the first and second moments nonetheless capture **the most salient distributional characteristics**. As such, BW discrepancy can substantially align distributions in practice, even in non-Gaussian settings.

- **Revision.** **We have added a dedicated discussion regarding the limitations of the Gaussian assumption at the end of Appendix A.** We also highlight that BW discrepancy aligns distributions by matching first- and second-order moments, which remains effective to a large extent even when the data is not Gaussian.


[1] Time-o1: Time-series forecasting needs transformed label alignment[C]//The Thirty-ninth Annual Conference on Neural Information Processing Systems. 2025.

#### **[W2] I consider this a mild weakness but the theory regarding the general Wasserstein metric is presented mostly for discrete measures. Given that a Gaussian data distribution is assumed, it could be discussed how the presented results for empirical measures relate to the original Gaussian data distribution.**

**Response.** Thank you for highlighting this important theoretical point. We agree that clarifying the relationship between the presented results for empirical measures and their Gaussian counterparts is necessary. We elaborate on this c

### Author comment
- **Result analysis.** There are two primary observations. (i) DistDF consistently achieves the lowest Disc values across various learning objectives, providing empirical evidence for the effectiveness of DistDF in aligning distributions and the associated benefits for forecasting accuracy. (ii) The values of $\alpha$ that minimize MSE and Disc exhibit strong concordance across different datasets, further supporting the claim that distributional alignment is conducive to improved forecasting performance. 
- **Revision.** **We have added the distributional discrepancy results as a supplement in Appendix D.8 (Table 12-14).**

#### **[W2] Improvements wrt to existing SOTA methods look rather small; however, they are consistent across models and datasets.**

**Response.** Thank you very much for your kind comment and recognition of the improvement consistency.
- Firstly, we agree that compared to SOTA learning objective, typically Time-o1, the performance improvement achieved by DistDF is consistent yet moderate. However, we note that **with respect to the prevalent direct forecasting (DF) approach using MSE as objective, DistDF yields very substantial gains**, which provides empirical validation on the limitation of MSE and the benefit of DistDF to enhance forecasting performance.
- Secondly, as stated in your strength 1, DistDF contributes beyond empirical improvements in two key aspects: (i) it **identifies an inherent theoretical limitation** of the Time-o1 learning objective; and (ii) it **reformulates time-series forecasting as a distribution alignment challenge**, underscoring the importance of distribution alignment. This establishes conceptual links to research areas based on distribution alignment such as transfer learning, which brings new insights to the time-series forecasting field.
- Finally, to further substantiate the consistency of DistDF's improvements, we incorporate an additional learning objective (LDTW) as a supplementary baseline. The results are available as follows.


| Model | Dataset  | **DistDF** (MSE) | **DistDF** (MAE) | Time-o1 (MSE) | Time-o1 (MAE) | FreDF (MSE) | FreDF (MAE) | Koopman (MSE) | Koopman (MAE) | Dilate (MSE) | Dilate (MAE) | LDTW (MSE) | LDTW (MAE) | Soft-DTW (MSE) | Soft-DTW (MAE) | DTW (MSE) | DTW (MAE) | DF (MSE) | DF (MAE) |
|:--:|:--:|:--:|:--:|:--:|:--:|:-:|:-:|:-:|:-:|:--:|:--:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **TimeBridge** | ETTm1 | **0.383**| **0.397**| 0.383 | 0.397 | 0.386| 0.398| 0.460  | 0.438  | 0.387 | 0.400 | 0.387 | 0.400 | 0.395 | 0.402 | 0.394| 0.401| 0.387  | 0.400  |
| | ETTh1 | **0.434**| **0.436**| 0.439 | 0.438 | 0.439| 0.436| 0.459  | 0.449  | 0.464 | 0.452 | 0.464 | 0.452 | 0.452 | 0.445 | 0.455| 0.446| 0.442  | 0.440  |
| | ECL| **0.172**| **0.267**| 0.175 | 0.268 | 0.175| 0.267| 0.182  | 0.277  | 0.176 | 0.271 | 0.182 | 0.275 | 0.173 | 0.268 | 0.178| 0.273| 0.176  | 0.271  |
| | Weather  | **0.248**| **0.275**| 0.250 | 0.275 | 0.254| 0.276| 0.269  | 0.293  | 0.252 | 0.277 |

### Author comment
Thank you so much for your encouraging support and appreciation of **our observation, methodology, and empirical studies**. Below are our responses to the specific query raised.

---

#### [W1,Q1] The central hypothesis of this work is that aligning conditional distributions is beneficial, and the authors provide theoretical justifications along with empirical evidence through forecasting error metrics. However, it is unclear whether the conditional distributions actually align for the best alpha values reported in **Tables 5 and 6**. In other words, the hypothesis is not directly evaluated in the experiments through distributional discrepancy, but rather indirectly through forecasting performance. If no **distributional discrepancy needs to be shown** in the experiments, please elaborate why.

**Response.** Thank you for your insightful question. **We agree that it is essential to evaluate the distributional discrepancy**.
- **Additional experiment.** We add experiments based on **Tables 2, 5, and 6** to evaluate distributional discrepancy. As stated in this paper, the conditional distribution discrepancy is intractable. Therefore, we report the joint distribution discrepancy, which is the upper bound of the conditional discrepancy. The metric is denoted as Disc in the tables below.

**The joint discrepancy results as a supplement to Table 2.**
| Model| Dataset  | **DistDF** | Time-o1 | FreDF  | Koopman | Dilate | LDTW  | Soft-DTW | DTW| DF |
|-|-|:-:|:-:|:-:|:-:|:-:|:--:|:--:|:--:|:--:|
| **TimeBridge** | ETTm1 | **0.230** | 0.231| 0.231  | 0.271| 0.231  | 0.231 | 0.238  | 0.237 | 0.232 |
|| ETTh1 | **0.326** | 0.331| 0.330  | 0.350| 0.352  | 0.352 | 0.340  | 0.344 | 0.332 |
|| ECL| **0.129** | 0.135| 0.137  | 0.139| 0.136  | 0.139 | 0.133  | 0.140 | 0.136 |
|| Weather  | **0.147** | 0.148| 0.149  | 0.157| 0.148  | 0.148 | 0.153  | 0.150 | 0.148 |
| **Fredformer** | ETTm1 | **0.227** | 0.228| 0.231  | 0.232| 0.233  | 0.233 | 0.240  | 0.239 | 0.232 |
|| ETTh1 | **0.324** | 0.325| 0.333  | 0.349| 0.349  | 0.350 | 0.356  | 0.355 | 0.342 |
|| ECL| **0.130** | 0.133| 0.134  | 0.142| 0.140  | 0.144 | 0.153  | 0.151 | 0.143 |
|| Weather  | 0.148  | **0.148** | 0.149  | 0.150| 0.150  | 0.152 | 0.152  | 0.152 | 0.152 |

**The joint discrepancy results as a supplement to Table 5.**

 
| $\alpha$ | ETTh2 (MSE) | ETTh2 (MAE) | ETTh2 (Disc) | ECL (MSE) | ECL (MAE) | ECL (Disc) | Weather (MSE) | Weather (MAE) | Weather (Disc) |
|:--:|:-:|:-:|:--:|:-:|:-:|:-:|:--:|:--:|:-:|
| 0  | 0.377  | 0.403  | 0.292 | 0.176| 0.271| 0.136  | 0.252 | 0.277 | 0.148|
| 0.001 | 0.378  | 0.402  | 0.292 | 0.172| 0.267| 0.130  | 0.250 | 0.276 | 0.148|
| 0.002 | 0.377  | 0.402  | 0.291 | 0.173| 0.267| **0.130**| 0.250 | 0.276 | 0.148|
| 0.005 | 0.376  | 0.401  | 0.291 | **0.172**| **0.267**| 0.130  | 0.250 | **0.276**| 0.148|
| 0.01  | 0.376  | 0.400  | 0.291 | 0.172| 0.267| 0.130  | **0.249**| 0.276 | **0.146**  |
| 0.02  | 0.376  | 0.400  | 0.291 | 0.174| 0.269| 0.133  | 0.249 

### DistDF: Time-series Forecasting Needs Joint-distribution Wasserstein Alignment


## Meta review / decision
### Paper Decision
Accept (Poster)

## PDF extracted text (first pages)
```text
Published as a conference paper at ICLR 2026
DISTDF: TIME-SERIESFORECASTINGNEEDS
JOINT-DISTRIBUTIONWASSERSTEINALIGNMENT
Hao Wang1,2 Licheng Pan1 Yuan Lu1 Zhixuan Chu3 Xiaoxi Li1 Shuting He4
Zhichao Chen5 Qingsong Wen6 Haoxuan Li7† Zhouchen Lin5,8†
1Xiaohongshu Inc. 2College of Control Science and Technology, Zhejiang University
3College of Computer Science and Technology, Zhejiang University
4School of Computing and Artificial Intelligence, Shanghai University of Finance and Economics
5State Key Lab of General AI, School of Intelligence Science and Technology, Peking University
6Squirrel AI 7Center for Data Science, Peking University
8Institute for Artificial Intelligence, Peking University
ABSTRACT
Training time-series forecast models requires aligning the conditional distribution
of model forecasts with that of the label sequence. The standard direct forecast
(DF) approach resorts to minimizing the conditional negative log-likelihood of
the label sequence, typically estimated using the mean squared error. However,
this estimation proves to be biased in the presence of label autocorrelation. In
this paper, we propose DistDF, which achieves alignment by alternatively min-
imizing a discrepancy between the conditional forecast and label distributions.
Because conditional discrepancies are difficult to estimate from finite time-series
observations, we introduce a newly proposed joint-distribution Wasserstein dis-
crepancy for time-series forecasting, which provably upper bounds the conditional
discrepancy of interest. This discrepancy admits tractable, differentiable estimation
from empirical samples and integrates seamlessly with gradient-based training.
Extensive experiments show that DistDF improves the performance of diverse
forecast models and achieves the state-of-the-art forecasting performance. Code is
available athttps://github.com/Master-PLC/DistDF.
1 INTRODUCTION
Time-series forecasting, which entails predicting future values based on historical observations,
plays a critical role in numerous applications, such as stock trend analysis in finance (Li et al.,
2025a), website traffic prediction in e-commerce (Chen et al., 2023), and trajectory forecasting in
robotics (Fan et al., 2023). In the era of deep learning, the development of effective forecast models
hinges on two aspects (Wang et al., 2025f):(1) How to design neural architecture serving as the
forecast models?and(2) How to design learning objective driving model training?Both aspects are
essential for achieving high forecast performance.
The design of neural architectures has been extensively investigated in recent studies. A central
challenge involves effectively capturing the autocorrelation structures inherent in the input sequences.
To this end, a variety of neural architectures have been proposed (Wang et al., 2023b; Lin et al., 2024).
Recent discourse emphasizes the comparison between Transformer-based models—which leverage
self-attention mechanisms to capture autocorrelation and scale effectively (Nie et al., 2023; Liu et al.,
2024; Piao et al., 2024)—and linear models, which use linear projections to model autocorrelation and
often achieve competitive performance with reduced complexity (Yi et al., 2023b; Zeng et al., 2023;
Yue et al., 2025). These developments illustrate a rapidly evolving aspect in time-series forecasting.
In contrast, the design of learning objectives remains comparatively under-explored (Li et al., 2025c;
Qiu et al., 2025a; Kudrat et al., 2025). Current approaches typically define the learning objective by
estimating the conditional likelihood of the label sequence. In practice, this is often implemented
†Corresponding authors.
1
Published as a conference paper at ICLR 2026
as the mean squared error (MSE), which has become a standard objective for training forecast
models (Lin et al., 2025). However, MSE neglects the autocorrelation structure of the label sequence,
leading to biased likelihood estimation (Wang et al., 2025g). Some efforts transform the label
sequence into conditionally decorrelated components to eliminate the bias (Wang et al., 2025f;g).
Nevertheless, as demonstrated in this work, such conditional decorrelation cannot be guaranteed in
practice; thus, the bias persists.Therefore, likelihood-based methods are fundamentally limited by
biased likelihood estimation that impedes model training.
To bypass the limitation of previous widely used likelihood-based methods, we propose Distribution-
aware Direct Forecast (DistDF), which trains forecast models by minimizing the discrepancy between
the conditional distributions of forecast and label sequences. Since directly estimating conditional
discrepancies is intractable given finite time-series observations, we introduce the joint-distribution
Wasserstein discrepancy for unbiased time-series forecasting. It upper-bounds the conditional discrep-
ancy of interest, enables differentiation, and can be estimated from finite time-series observations,
making it well-suited for integration with gradient-based optimization of time-series forecast models.
Our main contributions are summarized as follows:
• We demonstrate a fundamental limitation in prevailing likelihood-based learning objectives for
time-series forecasting: biased likelihood estimation that hampers effective model training.
• We propose DistDF, a training framework that aligns the conditional distributions of forecasts and
labels, with a newly proposed joint-distribution Wasserstein discrepancy, ensuring the alignment of
conditional distributions and admitting tractable estimation from finite time-series observations.
• We perform comprehensive empirical evaluations to demonstrate the effectiveness of DistDF, which
enhances the performance of state-of-the-art forecast models across diverse datasets.
2 PRELIMINARIES
2.1 PROBLEM DEFINITION
In this paper, we focus on the multi-step time-series forecasting problem. We use uppercase letters
(e.g., X) to denote matrices and lowercase letters (e.g.,x) to denote scalars. Given a time-series dataset
S with D covariates, the historical sequence at time step n is defined as X= [S n−H+1, . . . , Sn]∈
RH×D, and the label sequence is defined as Y= [S n+1, . . . , Sn+T]∈R T×D, where H is the
lookback window size and T is the forecast horizon. Modern models adopt a direct forecasting (DF)
approach, generating all T forecast steps simultaneously (Liu et al., 2024). Thus, the target is to learn
a modelg:R H×D →R T×D that mapsXto a forecast sequence ˆYapproximatingY 1.
The development of forecast models encompasses two principal aspects: (1) neural network archi-
tectures that effectively encode historical sequences (Zeng et al., 2023; Liu et al., 2024), and (2)
learning objectives for training neural networks (Wang et al., 2025f;g). It is important to emphasize
that this work focuses on the design of learning objectives rather than proposing novel architectures.
Nevertheless, we provide a concise review of both aspects for contextual completeness.
2.2 NEURAL NETWORK ARCHITECTURES IN TIME-SERIES FORECASTING
Architectural developments aim to encode historical sequences to obtain informative representa-
tion (Wu et al., 2025; Qiu et al., 2025b). Representative classic architectures include recurrent neural
networks (Gu et al., 2021), convolutional neural networks (Luo and Wang, 2024), and graph neural
networks (Yi et al., 2023a). A central theme in recent literature is the comparison of Transformer
and non-Transformer architectures. Transformers (e.g., PatchTST (Nie et al., 2023), TQNet (Lin
et al., 2025), TimeBridge (Liu et al., 2025)) demonstrate strong scalability on large datasets but often
entail substantial computational cost. In contrast, non-Transformer models (e.g., TimeMixer (Wang
et al., 2024), FreTS (Yi et al., 2023b)) offer greater computational efficiency but may be less scal-
able. Recent advances include hybrid architectures that combine Transformer and non-Transformer
components for their complementary strengths (Lin et al., 2024), as well as the integration of Fourier
analysis for efficient learning (Piao et al., 2024; Yi et al., 2025).
1Hereafter, we consider the univariate case (D = 1) for clarity. In the multivariate case, each variable can be
treated as a separate univariate case when computing the learning objectives.
2
Published as a conference paper at ICLR 2026
2.3 LEARNING OBJECTIVES IN TIME-SERIES FORECASTING
Learning objective developments have largely focused on aligning the conditional distributions of
model forecasts P( ˆY|X) with those of the label sequence P(Y|X) . To this end, the most common
objective is the MSE, which measures the point-wise error between the forecast and label sequences
(Dai et al., 2024; Chen et al., 2025; Lin et al., 2025):
Lmse =
Y|X − ˆY|X

2
2
=
TX
t=1

Y|X,t − ˆY|X,t
2
,(1)
where Y|X is the label sequence given historical sequence X, ˆY|X is the forecast sequence. However,
the MSE objective is known to be biased since it overlooks the presence of label autocorrelation (Wang
et al., 2025g). To mitigate this issue, several alternative learning objectives have been proposed.
One line of work advocates aligning the overall shape of the forecast and label sequence (e.g.,
Dilate (Le Guen and Thome, 2019) and PS (Kudrat et al., 2025)). These approaches accommodate au-
tocorrelation by emphasizing sequence-level differences, but lack theoretical guarantees for achieving
an unbiased objective. Another line of work transforms labels into decorrelated components before
alignment. This strategy reduces bias and improves forecasting performance (Wang et al., 2025f;g),
showcasing the benefits of refining learning objectives for time-series forecasting.
3 METHODOLOGY
3.1 MOTIVATION
The primary objective in training time-series forecast models is to align the conditional distribution
of model-generated forecasts with that of the label sequence. Likelihood-based approaches seek this
by maximizing the conditional likelihood of the label sequence. A common practice is to estimate the
negative log-likelihood through the mean squared error (MSE), which has become the predominant
objective for training time-series forecast models (Lin et al., 2025). However, MSE treats each future
step as an independent prediction task and thus ignores the autocorrelation structure of the label
sequence, where each observation typically depends on its predecessors (Zeng et al., 2023). Such an
oversight renders MSE biased from the true negative log-likelihood of the label sequence. This issue
is termed as autocorrelation bias and formalized in Theorem 3.1.
Theorem 3.1(Autocorrelation bias).Suppose Y|X ∈R T is the label sequence given historical
sequence X, ˆY|X ∈R T is the forecast sequence, Σ|X ∈R T×T is the conditional covariance of Y|X.
The bias of MSE from the negative log-likelihood of the label sequence givenXis expressed as:
Bias =
Y|X − ˆY|X

2
Σ−1
|X
−
Y|X − ˆY|X

2
2
.(2)
where∥v∥ 2
Σ−1
|X
=v ⊤Σ−1
|X v. It vanishes if the conditional covarianceΣ |X is the identity matrix2.
Some might argue that the bias can be eliminated by first transforming the label sequence into
conditionally decorrelated components and then applying MSE component-wise. For example,
FreDF(Wang et al., 2025g) uses Fourier transform to obtain frequency components;Time-o1(Wang
et al., 2025f) employs principal component analysis to obtain principal components. This strategy
does eliminate the bias if the resulting components were truly conditionally decorrelated (see Theo-
rem 3.1). However, one key distinction warrants emphasis: both Fourier and principal component
transformations guarantee onlymarginally decorrelatedof the obtained components (i.e., diagonal
Σ), not the requiredconditional decorrelation(i.e., diagonal Σ|X)3; thus the bias persists.Hence,
likelihood-based methods are limited by biased likelihood estimation which hampers model training.
2The pioneering work (Wang et al., 2025f) derives the bias from the marginal likelihood ofY assuming it
follows a Gaussian distribution. In contrast, this work clarifies that it is the conditional distribution of Y given
Xthat is Gaussian. Consequently, we derive the bias from the conditional log-likelihood ofY.
3According to Theorem 3.3 (Wang et al., 2025g) and Lemma 3.2 (Wang et al., 2025f), the components
obtained by Fourier and principal component transformations are marginal decorrelated.
3
Published as a conference paper at ICLR 2026
0
32
64
96
128
160
192
0
32
64
96
128
160
192 0.000
0.001
0.010
0.100
1.000
(a) Raw labels.
0
32
64
96
128
160
192
0
32
64
96
128
160
192 0.000
0.001
0.010
0.100
1.000 (b) FreDF components.
0
32
64
96
128
160
192
0
32
64
96
128
160
192 0.000
0.001
0.010
0.100
1.000 (c) Time-o1 components.
Figure 1: The conditional correlation of label components given X, where the forecast horizon is set
to T = 192. The correlation matrices are computed for the raw labels (a), the frequency components
in FreDF (b) (Wang et al., 2025g) and the principal components in Time-o1 (c) (Wang et al., 2025f).
Case study.We conduct a case study on the Traffic dataset to illustrate the limitations of likelihood-
based methods. As shown in Fig. 1(a), the conditional correlation matrix reveals substantial off-
diagonal values—over 50.3% exceed 0.1—illustrating the presence of autocorrelation effects. In
contrast, Fig. 1(b) presents the conditional correlations of the latent components extracted by FreDF
and Time-o1 (Wang et al., 2025g;f). While the non-diagonal elements are notably reduced, residual
correlations remain, indicating that these methods do not fully eliminate autocorrelation in the
transformed components. Consequently, applying a point-wise loss to these transformed components
continues to ignore autocorrelation and yields bias.
Given the substantial challenges faced by likelihood-based methods, it is worthwhile to explore
alternative strategies to align conditional distributions for model training. One plain strategy is directly
minimizing adistributional discrepancy between the conditional distributions(Courty et al., 2017),
which can effectively achieve alignment while bypassing the complexity of likelihood estimation.
Importantly, there are two questions that warrant investigation.How to devise a discrepancy to align
the two conditional distributions? Does it effectively improve forecast performance?
3.2 ALIGNING CONDITIONAL DISTRIBUTIONS VIA JOINT-DISTRIBUTION BALANCING
In this section, we aim to align the conditional distributions,i.e., P ˆY|X and PY|X , by minimizing
a discrepancy metric between them. As with general distribution alignment tasks, the choice of
discrepancy metric is crucial (Xu et al., 2021). We select the Wasserstein discrepancy from optimal
transport theory, which measures the discrepancy between two distributions as the minimum cost
required to transform one into the other. Its ability to remain informative for distributions with
disjoint supports, combined with its robust theoretical properties and proven empirical success, makes
it a principled choice for this work (Courty et al., 2017). An informal definition is provided in
Definition 3.2.
Definition 3.2(Wasserstein discrepancy).Let α and β be random variables with probability distri-
butions Pα and Pβ; Sα = [α1, ..., αn] and Sβ = [β1, ..., βm] be empirical samples from Pα and Pβ.
The optimization problem seeks a feasible planP∈R n×m
+ to transportαtoβat the minimum cost:
Wp(Pα,P β) := min
P∈Π(α,β)
⟨D, P⟩,
Π(Pα,P β) :=
( Pi,1 +...+P i,m =a i, i= 1, ...,n,
P1,j +...+P n,j =b j, j= 1, ...,m,
Pi,j ≥0, i= 1, ...,n, j= 1, ...,m,
(3)
where Wp denotes the p-Wasserstein discrepancy; D∈R n×m
+ represents the pairwise distances
calculated as Di,j =∥α i −β j∥p
p; a= [a 1, . . . , an] and b= [b 1, . . . , bm] are the weights of samples
inαandβ, respectively;nandmare the numbers of samples;Πdefines the set of constraints.
A natural approach to aligning the conditional distributions is to minimize the Wasserstein discrepancy
Wp(PY|X ,P ˆY|X ). However, this approach suffers from anestimation difficulty. For any given X,
a typical dataset often provides only a single associated label sequence Y , and the forecast model
4
Published as a conference paper at ICLR 2026
produces only a single output ˆY . Thus, the empirical sets ( SY|X and S ˆY|X ) each contain only a
single sample, which is insufficient to represent the underlying conditional distributions and renders
the discrepancy uninformative. Crucially, this limitation is not unique to the Wasserstein discrepancy;
any distributional discrepancy metric becomes degenerate in the absence of multiple samples.
Lemma 3.3(Kim et al. (2022)).For any p≥1 , the joint-distribution Wasserstein discrepancy upper
bounds the expected conditional-distribution Wasserstein discrepancy:
Z
Wp(PY|X ,P ˆY|X )dP(X)≤ W p(PX,Y ,P X, ˆY ).(4)
where the equality holds ifp= 1or the conditional Wasserstein term is constant with respect toX.
To bypass this estimation difficulty, we advocate the joint-distribution Wasserstein discrepancy,
Wp(PX,Y ,P X, ˆY ), for training time-series forecast models. This proxy is advantageous for two
reasons. First, it provides a provableupper boundon the expected conditional discrepancy (see
Lemma 3.3), ensuring that minimizing the joint discrepancy effectively aligns the conditional dis-
tributions of interest. Second, it is readilyestimablefrom finite time-series observations, since the
empirical samples SX,Y and SX, ˆY can be constructed from the entire dataset, yielding sufficient
samples to compute a meaningful and informative discrepancy.
Theorem 3.4(Alignment property).The conditional distributions are aligned, i.e., PY|X =P ˆY|X if
the joint-distribution Wasserstein discrepancy is minimized to zero, i.e.,Wp(PX,Y ,P X, ˆY ) = 0.
Lemma 3.5(Peyr ´e and Cuturi (2019)).Suppose PX,Y and PX, ˆY obey Gaussian distributions
N(µ X,Y ,Σ X,Y ) and N(µ X, ˆY ,Σ X, ˆY ), respectively. The squared W2 discrepancy can be calculated
as the Bures-Wasserstein discrepancy:
BW(µ X,Y , µX, ˆY ,Σ X,Y ,Σ X, ˆY ) =
µX,Y −µ X, ˆY

2
2
+B(Σ X,Y ,Σ X, ˆY ),(5)
where B(ΣX,Y ,Σ X, ˆY ) = Tr

ΣX,Y + ΣX, ˆY −2
q
Σ1/2
X,Y ΣX, ˆY Σ1/2
X,Y

, Tr(·) denotes matrix trace.
Theoretical Justification.Theorem 3.4 shows that minimizing the joint-distribution Wasserstein
discrepancy to zero guarantees the alignment of conditional distributions. This result enables using the
joint discrepancy as a learning objective for training forecast models. Under a Gaussian assumption
(likewise MSE), this discrepancy has an analytical form (Lemma 3.5), obviating the need to solve the
complex transport problem of Definition 3.2. The proof is available in Appendix A.
The use of Wasserstein discrepancy for distribution alignment is highly inspired by domain adaptation
field (Courty et al., 2017). However, one key distinction warrants emphasis. Domain adaptation
dominantly aligns themarginal distributions of inputsto improve generalization; in contrast, we
align theconditional distributionsof model outputs and labels to perform supervised training. To our
knowledge, this represents a technically innovative strategy.
3.3 MODEL IMPLEMENTATION
In this section, we present the implementation specifics of DistDF, a framework that leverages the
joint-distribution Wasserstein discrepancy to enhance the training of time-series forecast models. The
principal steps of the algorithm are formalized in Algorithm 1.
Given historical sequences X and corresponding label sequences Y∈R B×T, where B denotes
batch size and T denotes forecast horizon; the forecast model g is employed to generate the forecast
sequences, denoted as ˆY (step 1). Subsequently, we define two joint sequences, which are constructed
by concatenating X with Y and ˆY along the time axis, respectively (step 2), expressed asZ= [X, Y]
and ˆZ= [X, ˆY].
Algorithm 1The workflow of DistDF.
Input:X: historical sequences,Y: label sequences.
Parameter: α: the relative weigh
```
