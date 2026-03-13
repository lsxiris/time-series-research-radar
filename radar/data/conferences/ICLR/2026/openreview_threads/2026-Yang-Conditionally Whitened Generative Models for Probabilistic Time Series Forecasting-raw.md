# Conditionally Whitened Generative Models for Probabilistic Time Series Forecasting — OpenReview Raw Thread

- Forum: https://openreview.net/forum?id=GG01lCopSK
- PDF: https://openreview.net/pdf?id=GG01lCopSK
- Section: 一、时间序列生成：因果性、多样性与领域适配
- Zhihu score: 6.0
- Venue status: ICLR 2026 Poster

## Submission metadata
- Authors: Yanfeng Yang, Siwei Chen, Pingping Hu, Zhaotong Shen, Yingjie Zhang, Zhuoran Sun, Shuai Li, Ziqi Chen, Kenji Fukumizu
- Primary area: generative models
- Keywords: Diffusion Model, Probabilistic Time Series Forecasting, Conditional Generation

## Abstract
Probabilistic forecasting of multivariate time series is challenging due to non-stationarity, inter-variable dependencies, and distribution shifts. While recent diffusion and flow matching models have shown promise, they often ignore informative priors such as conditional means and covariances. In this work, we propose Conditionally Whitened Generative Models (CW-Gen), a framework that incorporates prior information through conditional whitening. Theoretically, we establish sufficient conditions under which replacing the traditional terminal distribution of diffusion models, namely the standard multivariate normal, with a multivariate normal distribution parameterized by estimators of the conditional mean and covariance improves sample quality. Guided by this analysis, we design a novel Joint Mean-Covariance Estimator (JMCE) that simultaneously learns the conditional mean and sliding-window covariance. Building on JMCE, we introduce Conditionally Whitened Diffusion Models (CW-Diff) and extend them to Conditionally Whitened Flow Matching (CW-Flow). Experiments on five real-world datasets with six state-of-the-art generative models demonstrate that CW-Gen consistently enhances predictive performance, capturing non-stationary dynamics and inter-variable correlations more effectively than prior-free approaches. Empirical results further demonstrate that CW-Gen can effectively mitigate the effects of distribution shift.

## Reviews
### Reviewer_Nwt6
- summary: The paper introduces CW-Gen, including CW-Diff and CW-Flow. It proposes a novel JMCE to simultaneously estimate the conditional mean and sliding-window covariance of future time series, which guides the whitening process. The authors provide theoretical guarantees showing conditions under which their approach improves the generative model's sample quality by reducing the KL divergence between the conditional distribution and the model's terminal distribution. Experimental evaluations demonstrate improvements in probabilistic forecasting accuracy, capturing non-stationary dynamics and inter-var
- strengths: 1. The paper establishes conditions that justify why replacing the traditional terminal Gaussian distribution with one parameterized by estimated conditional mean and covariance improves sample quality.
2. The JMCE simultaneously learns accurate conditional means and sliding-window covariances with eigenvalue control to ensure stability and robustness—this nuanced approach effectively addresses non-stationarity and heteroscedasticity.
3. Experiments show the outperformed performance over baselin
- weaknesses: 1. The approach involves computationally expensive operations, particularly eigen-decomposition for whitening covariance matrices, which scales cubically with dimensionality. For very high-dimensional datasets, CW-Gen can become quite slow, limiting real-time deployment scenarios.
2. The framework's reliance on complex joint estimators and whitening transformations may impose a higher barrier to adoption compared to simpler baseline models.
3. The paper ablates hyperparameters but does not isolate the individual contributions of conditional mean estimation versus covariance estimation. Which component drives most improvements?
- questions: See above
- rating: 6 | confidence: 2

### Reviewer_skbS
- summary: The paper proposes CW-Gen, which whitens data using learned conditional means and covariances from a Joint Mean-Covariance Estimator before training generative models. The idea to align the model priors with data statistics is sound and yields consistent empirical gains across datasets.
- strengths: - Tackle a challenging, important and underrepresented aspect for time-series modelling: multivariate time-series.
- Clear motivation: Proposes a method that allows for a new prior, that is closer to the data-distribution.
- Well written and theoretically founded.
- Extensive evaluation, which show that the proposed prior actually improves state-of-the art models.
- weaknesses: - Unclear connection of DKL reduction in Theorem 1 to actual practical guarantees: Can you (a) clarify the tightness of the bound; (b) give intuition / toy examples showing when the condition is achievable (or not); (c) explicitly discuss regimes where the condition can fail
- Unclear estimator quality: Covariance targets are noisy; stability and regularization not analyzed.
- The paper notes that CW requires eigen-decomposition per sample / per time step but then glosses over practical limitations. More precise complexity analysis and discussion of remedies (approximate eigen/svd, diagonal + low-rank approximation, block-diagonalization, randomized SVD or factor models) could benefit the paper.
- The paper argues joint mean+full covariance is important. But it’s not fully convincing which component drives gains. There are some ablations (backbone/wEigen) but I don’t see a simple controlled ablation that compares: (a) subtract mean only, (b) subtract mean and scale by diagonal variance
- questions: - Can you be very explicit on how your proposed method compare to other (univariate) flow-based and diffusion-based methods that introduced flexible priors, e.g., [1,2]
- Can you add a short experiment showing numeric values of both sides of Equation (3) on training/validation examples so readers can see how far the estimators are from satisfying the bound in practice.
- Choice of sliding window length (95 for most datasets, 15 for ILI) needs justification. Why 95? How sensitive are results to this hyperparameter?


1. Modeling temporal data as continuous functions with stochastic process diffusion, ICLR 2023
2. Flow Matching with Gaussian Process Priors for Probabilistic Time Series Forecasting, ICLR 2025
- rating: 6 | confidence: 4

### Reviewer_pWon
- summary: The paper introduces conditionally whitened generative models that incorporate information in the noising process. The authors tailor diffusion and flow matching processes by including conditional information obtained via a mean and covariance estimator (termed JMCE). Their approach is theoretically motivated and empirically demonstrated to improve generative performance.
- strengths: - The methodology is theoretically justified, and the authors show under which conditions the distance between the prior and conditional distribution is minimized.
- A simple mean and covariance estimator is introduced and well-motivated to parametrize the generative process.
- The proposed conditional whitening leads to empirical performance improvements.
- The framework includes diffusion and flow matching.
- weaknesses: - The model requires a two-stage process now. First fit JMCE, then train the generative model.
- The derived diffusion process requires the inversion of the covariance matrix, resulting in a higher runtime complexity compared to standard diffusion models. A runtime comparison would aid the comparison.
- The limitations of the method should be discussed more thoroughly. Furthermore, I recommend separating the related work section from the introduction.

Minors:

- L260: Sentence incomplete
- questions: - Can the model be trained in an end-to-end fashion or does it require a two-stage process?
- Did you try diagonal covariance parametrizations to reduce the runtime complexity?
- Can you elaborate more on the performance of the JMCE model itself? How does it compare in forecasting?
- rating: 6 | confidence: 4

### Reviewer_wUr1
- summary: The authors propose to use a separate model to predict sliding-window means and covariances and subsequently use those to whiten to prediction targets of generative forecasting models.
Their method improves forecasting results for a broad selection of generative forecasting models on several datasets.
- strengths: 1. Consistent improvements in experimental results
1. Clear graphical illustration of method
- weaknesses: 1. As far as I understand from the algorithms in the appendix, conditional whitening with a JMCE is a wrapper or pre/postprocessing around a generative forecasting model. While this can be interwoven with the diffusion/flow matching dynamics in Section 4, this does not seem essential. If I am correct, I think it would be an advantage to highlight the simplicity of the final method.
- questions: 1. Do you train the JMCE model jointly with the generative model?
1. Line 313: How can this be done more efficiently exactly?
1. Are you modifying the generative models themselves? Or do you train the models on the conditionally whitened data as they are?
1. Have you ablated the different components of your JMCE loss?
- rating: 6 | confidence: 3

## Author comments / rebuttal
### To AC, PC, SAC: A summary of review and our rebuttal (skbS)
Dear AC, PC, SAC,

This is the summary of skbS's review and our rebuttal. Reviewer skbS gave a detailed and constructive review, recognizing our paper to be 'tackling a challenging task', 'clearly motivated', 'well written' and 'extensively evaluated'. skbS also raised good questions regarding theorem, numeric results of JMCE, computational speed of CW-Gen, the contribution of individual prior components, comparison with other pioneer (univariate) models, and the ablations of the length of sliding-window. Their feedback substantially improved the paper, and our rebuttal directly addressed every weakness with new theory clarifications, new experiments, and new analyses. skbS increased their rating from 6 to 8 before the leakage incident. Below is a detailed summary for the AC.

**Major concern 1: practical relevance of Theorem 1**

W1: The connection between the KL reduction in Theorem 1 and practical guarantees is unclear.

**Our rebuttal**

We added **substantial new theoretical clarification**, including:

1. A clear explanation of why Theorem 1 matters in practice (guides JMCE’s loss construction).

2. Discussion of the non-tightness of existing diffusion TV bounds and why tightness is beyond scope (with citations to Chen 2023; Fu 2024; Tian 2025).

3. Intuitive explanations and a 1D Gaussian toy example illustrating when Condition (3) is achievable in practice.

4. Discussion of failure regimes and an explicit explanation of how JMCE’s eigenvalue regularization and loss design are tailored to mitigate these issues.

**Major concern 2: numeric results of JMCE and the both-hand sides of Eq. (3)**

W2: Since the covariance targets are noisy, the estimator quality, stability and regularization should be analyzed. 

Q2: both-hand sides of Eq. (3) in training/validation sets should be provided.

**Our rebuttal**

First we clarify that our learning target is **sliding-window covariance** which is not noisy due to the sliding-window. New visualizations of JMCE's prediction targets and outputs of training/test sets are provided in Figure 4 of Appendix D.4. Alougth the true both-hand sides of Eq. (3) is not computable,  the Figure 4 shows non-stationarity time series has a larger right-hand side, which means our theorem 1 is valid in practice. 

We also provided the abalation study about the estimator quality, stability and regularization in Table 9-11.

**Major concern 3: computational speed of CW-Gen**

W3: CW-Gen requires extensive computation, while some matrix approximation methods can benefit the paper. In addition, more precise complexity analysis is needed. 

**Our rebuttal**

We implemented multiple new efficiency strategies, including compute the inverse matrices of the lower-triangle matrices, and training JMCE and generative model together (CW-E2E). More detailed description can be found in our response to NWT6's W1 and W2. We also added a more precise complexity analysis in Table 19. 

**Major concern 4: the contribution of individual prio

### To AC, PC, SAC: A summary of review and our rebuttal (wUr1)
Dear AC, PC, SAC,

This is the summary of pWon's review and our rebuttal. Reviewer wUr1 gave our work a positive assessment, highlighting consistent improvements and clear illustrations. pWon's main questions centered on: (1) the pipeline of the CW-Gen, (2) how efficiency of CW-Flow is achieved, (3) whether we modify underlying generative models, and (4) ablations of JMCE’s loss. Our rebuttal directly addressed all these concerns with proper clarification and clear explanations summarized below.

**Major concern 1: the pipeline of the CW-Gen**

W1 and Q1: The pipeline of CW-Gen and the training method of JMCE. And can we jointly train JMCE and generative models?

**Our rebuttal**

We clarified the 3 steps of CW-Gen and emphasized its conceptual and implementation simplicity. We also explained how CW-Diff and CW-Flow differ in postprocessing. In addition, we introduced a new end-to-end training strategy (CW-E2E) in Appendix D.10, which jointly trains JMCE and generative models. Results in Table 18 show CW-E2E has better ProbCorr, lower CRPS and FID. 

**Major concern 2: the efficiency of CW-Flow**

Q2: How the CW-Flow can be more efficiently exactly?


**Our rebuttal**

We clarified that CW-Flow needs **no** conditional whitening (CW) and its reverse operation, directly using JMCE’s mean & covariance as terminal distribution.

**Major concern 3: the modification of underlying generative models**

Q3: Did we changed the generative models, or just CW the data?

**Our rebuttal**

We provided a complete technical clarification. The diffusion models remain unchanged (same forward SDE, same reverse process, same loss). Flow matching uses a different terminal distribution (JMCE mean & covariance) but trains directly on raw data without further transforms. 

**Major concern 4: the ablation study of JMCE loss**

Q4: Have we ablated the different components of your JMCE loss?

**Our rebuttal**

We have ablated the different components of our JMCE loss in Tables 9-11. In the revised submission, we have included a visualization of JMCE in Fig. 4 of Appendix D.4.

**wUr1's final response**

Reviewer wUr1 kept their positive score after our rebuttal.

We greatly appreciate wUr1's insightful review and the contribution of the staff of ICLR.

### To AC, PC, SAC: A summary of review and our rebuttal (pWon)
Dear AC, PC, SAC,

This is the summary of pWon's review and our rebuttal. pWon provided a constructive review, recognizing our work as theoretically justified, well-motivated and improving performance. pWon also raised good questions regarding training strategy, runtime, diagonal approximations, and JMCE performance. Our rebuttal directly addressed each concern with new methods, new experiments, and new analyses, which led pWon to increase their rating from 6 to 8 before the leakage incident. Below is a concise summary for the AC.

**Major concern 1: two-stage training, first JMCE then generative model**

W1 and Q1: CW-Gen required a two-stage process, first training JMCE then training  generative model. Is it able to be trained in an end-to-end (E2E) fashion?

**Our rebuttal**

**New end-to-end training scheme CW-E2E (Appendix D.10).** The two-stage CW-Gen can indeed be trained in a E2E fashion. New empirical results (Table 18) show CW-E2E is competitive or better on some metrics (e.g., CRPS, ProbCorr, FID).

**Major concern 2: higher runtime due to covariance inversion**

W2: A detailed runtime analysis is needed.

Q2: Diagonal covariance parametrizations can help reduce the runtime complexity.

**Our rebuttal**

We added a comprehensive runtime comparison (Appendix F, Table 19), including training a JMCE, conditional whitening (CW), and training a generative model. We also discussed the acceleration techniques in Appendix D.9 and D.10, including: inverting triangular-matrixs for CW, and training CW-Gen in an E2E fashion. The diagonal covariance parameterizations has some theoretical concerns. And the rebuttal to Reviewer NWT6’s W3 shows more evidence about the performance of diagonal covariance. 

**Major concern 3: Performance of JMCE itself**

Q3: The performance of the JMCE itself and its forecasting ability should be further highlighted

**Our rebuttal**

We have a full JMCE ablation study in Appendix D.4, showing that compared with the baseline model, JMCE has higher mean accuracy, covariance accuracy, eigenvalue stability. We also added new visualization of JMCE outputs in Figure 4.

**Major concern 4: Limitations and organization of the paper**

W3: Limitations should be more thorough. The related work section should be separated from the the introduction.

W4: An incomplete sentence in L260

**Our rebuttal**

We will re-write the involved parts according to the instruction. But now we have to strictly follow the page limit of the ICLR submission format. The sentence in L260 is not incomplete, and we will polish it.


**pWon's final response**

pWon raised the rating from 6 to 8 before the document leakage incident.

We are very grateful for pWon's thoughtful and insightful review and for the effort of the staff of ICLR.

### To AC, PC, SAC: A summary of review and our rebuttal (Nwt6)
Dear AC, PC, SAC,

We understand that we are in a hard period, and the new ICLR policies have significantly increased your workload. To help minimize the time you need to spend, we have summarized each reviewer's feedback and our corresponding rebuttal below each review.

We first would like to thank Reviewer Nwt6, who acknowledged our work as novel, theoretically sound, and performance-improving. Nwt6's concerns mainly focused on (1) computational efficiency, and (2) the contribution of individual prior components. Our rebuttal provided substantial new technical content, new experiments, and concrete improvements that directly addressed each concern. Below is a concise summary for the AC.

**Major concern 1: computational cost** 

W1: Eigen-decomposition and conditional whitening (CW) may be too slow for high-dimensional datasets. 

W2: The algorithm may have a higher barrier compared to simpler baseline models.

**Our rebuttal**

1. **New method to avoid eigen-decomposition entirely (Appendix D.9).** We show that whitening can be implemented via inverting a lower-triangular matrix, yielding a dramatic speed-up. On Solar Energy dataset (137-dim), the time of CW can be reduced from 14,460s to 52.7s.
2. **New end-to-end training scheme CW-E2E (Appendix D.10).** CW-E2E jointly trains JMCE and the generative model, eliminating redundant computations. Total time On Solar Energy dataset can be reduced from 39,329s to 8,120s. New empirical results (Table 18) show CW-E2E is competitive or better on some metrics (e.g., CRPS, ProbCorr, FID).
3. Indeed that training CW-Gen introduces additional computational cost. But compared with simpler baseline models, CW-Gen improves performance across the vast majority of metrics (Tables 2-8). 

**Major concern 2: unclear contributions of individual parts of the prior model** 

W3: Which component (mean, variance, covariance) contributes most?

**Our rebuttal**

We added a new ablation study to show the contribution of individual parts of the prior model (Appendix D.6, Table 14), covering: Mean only, Var only, Cov only, Mean & Var and Mean & Cov. The key findings are:

1. Conditional mean provides the largest single improvement.
2. Mean & Cov performs best overall, confirming that our CW-Gen algorithm is reasonable and effective.
3. Cov is better than Var in capturing inter-variable correlations (ProbCorr metric).


**Nwt6's final response**

Reviewer Nwt6 kept their positive score after our rebuttal.

Again, we would like to express our sincere gratitude to Nwt6's insightful review, and to all organizers and staff.

### Thank you!
Thank you very much for your response. We are grateful for your thoughtful and insightful review, which has provided meaningful guidance for our study.

### Thank you!
Thank you for your response. We greatly appreciate your insightful review again. It has been truly helpful for our work.

### Thank you!
Thank you for your response. Again, we sincerely appreciate your thoughtful and insightful review, which provides important guidance for our work.

### Thank you!
Thank you very much for your response. We would like to express our gratitude again for your insightful review, which has been highly valuable for our work.

### Rebuttal to Q3
Thank you for your review. The choice of the sliding window length is indeed something that needs to be justified. In short, our choice of 95 is inspired by NsDiff. Due to implementation convenience, we set the length to 95 instead. Similar to the ETTh1 dataset (95/192), the window length on ILI also covers roughly half of the prediction window (15/32).  

We have added an ablation study of the length of the sliding window (written in lowercase as requested) in Appendix D.7 of the revised submission. The effects of different window lengths on CW-Gen can be found in Tables 15 and 16. Overall, changing the sliding window length has little impact on ETTh1, because the window is sufficiently long and modifying its length does not significantly affect the resulting sliding-window covariance. On the other hand, the variability introduced by changing the window length is slightly larger on the ILI dataset, but still remains within a reasonable range.


Finally, we sincerely thank you again for your review. Your insightful questions and comments have helped us identify the shortcomings of our work and significantly improve the paper.

### Rebuttal to Q2
Thank you for your review. We agree that understanding the both-hand side term of the theoretical equation is indeed crucial. However, for real-world time series datasets, the conditional mean and the conditional covariance cannot be explicitly obtained, and therefore the both-hand side cannot be computed explicitly either. To address this concern, we have added new visualizations of the ETTh1 time series in Figure 4 of the revised submission. As shown in the figure, ETTh1 exhibits highly non-stationary and periodic patterns, indicating that the conditional mean is strongly shifted away from zero. This further implies that the right-hand side, i.e., $\mu_{\mathbf{X}\mid \mathbf{C}}$, is significantly greater than zero in practice.

### Rebuttal to Q1
Thank you for your question. Comparing our method against univariate generative models that also incorporate prior information is indeed very important. In Appendix D.8 of the revised submission, we provide a detailed discussion of the similarities and differences between our CW-Gen and DSPD [1] and TsFlow [2].

In brief, DSPD leverages kernel functions (e.g., $\exp(-\gamma |t_i - t_j|)$) to help diffusion models better capture temporal correlations within the prediction window. However, such prior information is not conditioned on the historical temporal context, resulting in insufficient prior strength to support forecasting tasks. Moreover, DSPD lacks conditional mean priors—an omission that negatively impacts its predictive performance, as illustrated in Figure 5 of the revised version.

TsFlow models the conditional mean and variance within the prediction window using Gaussian processes, but Gaussian processes are limited by kernel choices. More importantly, computing the mean and variance of a Gaussian process requires inverting a matrix of size equal to the historical observation length (i.e., $\mathbb{R}^{T_h \times T_h}$), which poses computational challenges for long-range forecasting.

Furthermore, we applied DSPD and TsFlow to each dimension of the ETTh1 dataset and evaluated their performance using the same four metrics as in the main paper. The results are presented in Table 17, and visualizations of the means and variances of the generated samples are provided in Figure 5. The results show that both types of univariate models perform slightly worse than the proposed CW-Gen model.

### Rebuttal to W4
Thank you for your suggestion. It is indeed very important to analyze the benefits contributed by each component of the prior model. In the revised submission, we have added the corresponding experiments in **Table 14 of the Appendix D.6**. In brief, we systematically evaluated the performance of CW-Gen under the following prior information configurations: conditional mean only (Mean), diagonal conditional covariance only (Var), full conditional covariance only (Cov), conditional mean combined with conditional variance (Mean \& Var), and conditional mean combined with full covariance (Mean \& Cov). Table 14 shows that the Mean \& Cov configuration performs best, followed by Mean \& Var, with Mean alone in third place.

### Rebuttal to W3
Thank you for your valuable comments. Computational complexity analysis is indeed essential for any algorithm. In the revised submission, we have updated Table 19 to report in detail the runtime of each component of our method. Thanks to the parallel computing capabilities of modern GPU frameworks, the eigen-decomposition performed per sample or per timestep can be processed in parallel, and therefore does not constitute a major source of additional computational cost. We have also implemented additional strategies to further improve computational efficiency while maintaining competitive performance. Please refer to our response to Reviewer NWT6, Weakness 1, for the detailed description of these techniques. We greatly appreciate your suggestions in this regard. Due to time constraints, we have not yet fully implemented the approach you proposed, but it will have significant influence on our future work.

### Rebuttal to W2
Thank you for your review. Examining the behavior of JMCE when learning covariance matrices is indeed highly important.

First, JMCE does not learn the true conditional covariance, as it cannot be directly computed. Instead, it is trained to learn the conditional covariance within a sliding window. The noise level of this covariance is substantially reduced due to the sliding window. To illustrate this phenomenon, we have added visualizations of JMCE's prediction targets and outputs in Figure 4 of Appendix D.4 in the revised submission.

Second, in Tables 9-11, we reported the ratio between 1 and the minimum eigenvalue, which can be viewed as an evaluation of the regularization effect. We also reported its standard deviation which can be viewed as the stability. In addition, we study how the minimum eigenvalue $\lambda_{\min}$ and the weight of the regularization term $w_{\text{eigen}}$ influences JMCE. Consequently, we also reported the influence of these parameters on CW-Gen, with the corresponding results reported in Tables 12 and 13.

### Rebuttal to W1 continue
(c) First, if $\mu\_{X|C}=0$, then the right-hand side in (3), $\| \mu\_{X|C} \|\_2^2$, equals zero, while the left-hand side of (3) is dominated by estimation error. In this case, even small estimation errors can cause the inequality in (3) to fail. In practice, however, for non-stationary time series, $\mu\_{X|C}$ often exhibits sharp variations and thus deviates from zero, so this scenario is unlikely to occur. 

Second, When $\min_{i \in \{ 1,\ldots,d_x \} } \widehat{\lambda}\_{X|C,i}$ is very small, the factor $\left( \min\_{i \in \{ 1,\ldots,d\_x \} } \widehat{\lambda}\_{X|C,i} \\right)^{-1}$ in (3) can blow up, so even modest deviations $\| \mu\_{X|C} - \widehat{\mu}\_{X|C} \|\_2^2$ and $\| \\Sigma\_{X|C} - \widehat{\Sigma}\_{X|C} \|\_N$ may violate the condition. This motivates the explicit eigenvalue regularization in our JMCE loss in (4), which enforces strictly positive eigenvalues bounded away from zero. 

Finally, Condition (3) explicitly involves the estimation errors $\| \mu\_{X|C} - \widehat{\mu}\_{X|C} \|\_2^2$, $\| \Sigma\_{X|C} - \widehat{\Sigma}\_{X|C} \|\_N$, and $\| \Sigma\_{X|C} - \widehat{\Sigma}\_{X|C} \|_F$. If $(\widehat{\mu}\_{X|C},\widehat{\Sigma}\_{X|C})$ are not good estimators of $(\mu\_{X|C},\Sigma\_{X|C})$, then these terms on the left-hand side of (3) become large and may easily exceed $\| \mu\_{X|C} \|\_2^2$ on the right-hand side. To mitigate this, we deliberately design JMCE as a joint conditional mean and covariance estimator whose loss directly mirrors the left-hand side of (3). The experiments in Section D.4 show that JMCE achieves small estimation error, providing empirical evidence that our estimator yields sufficiently accurate $(\widehat{\mu}\_{X|C},\widehat{\Sigma}\_{X|C})$.

### Rebuttal to Q4
Thank you for your question. We have indeed ablated the different components of our JMCE loss. We record $L_2$, $L_F$, $L_{\text{SVD}}$, as well as the ratio between 1 and the minimum eigen value in Tables 9-11. In the revised submission, we have included a visualization of JMCE in Fig. 4 of Appendix D.4.



Finally, we thank you again for your review. Your questions and comments guided us to address the weaknesses and improve the paper greatly.

### Rebuttal to Q3
Thank you for your question; it raises a very important point. In fact, we didn't modify diffusion model and modified the flow matching model. 

For diffusion models, our forward process follows Eq. (6). However, the SDE in Eq. (6) is equivalent to the SDE in Eq. (7), and the SDE in Eq. (7) is identical to that of the original diffusion model. This means that the forward process of CW-Diff is the same as that of traditional diffusion models. The loss function and reverse process of CW-Diff are also identical to those of standard diffusion models. The key difference is that CW-Diff learns the conditional distribution of the whitened time series, and after sampling, an inverse whitening operation is applied.



For flow matching, the original flow-matching framework uses a terminal distribution that is a Gaussian with zero mean and identity covariance. In contrast, CW-Flow also adopts a Gaussian terminal distribution, but its mean and covariance are given by the conditional mean and conditional sliding-window covariance estimated by JMCE. Moreover, CW-Flow is trained directly on the raw time-series data, and no additional transformation is required after generating samples with CW-Flow.

### Rebuttal to W1
We thank the reviewer for pointing out that the statement of Theorem 1 could be better connected to practice. Below we (a) clarify the tightness of the bound in (3), (b) provide intuition / toy examples illustrating when the condition is (or is not) achievable, and (c) explicitly discuss regimes where the condition may fail.

(a) Our use of Theorem 1 is primarily to provide theoretical guidance for designing the loss function in JMCE and to show that the optimization objective in JMCE drives down the KLD between the terminal distribution and the true conditional distribution $P_{X|C}$. This KLD appears as a factor in an upper bound on the total variation distance between the conditional diffusion-generated distribution and the true conditional distribution (Chen et al., 2023). Establishing the tightness of this bound is beyond the scope of the present work. Indeed, to the best of our knowledge, existing studies that derive convergence rates for conditional diffusion models in total variation or related divergences also do not establish tightness or minimax lower bounds for these rates (Fu et al., 2024; Tian & Shen, 2025; Wang et al., 2025). Proving tightness or minimax lower bounds for diffusion-type conditional generative models is an interesting but technically demanding problem, which we view as an important direction for future research rather than a goal of this paper.

(b) We have already provided intuition for when the condition in Theorem 1 is achievable (see the paragraph below Theorem 1). In particular, condition (3) is more likely to hold when both $\mu_{X|C}$ and $\Sigma_{X|C}$ can be accurately estimated and $\mu_{X|C}$ is appreciably different from zero, which is common in non-stationary time series. The regimes where the condition fails are discussed in our response to point (c) below. Here, we present a toy example to further illustrate when the condition is achievable. Suppose $d_x=1$ and $X|C\sim N(\mu_{X|C},\sigma^2_{X|C})$. Then $Q_0= N(0,1)$ and $\widehat{Q}= N(\widehat{\mu}\_{X|C}, \sigma^2\_{X|C})$. In this case, the nuclear and Frobenius norms reduce to absolute values, and condition (3) becomes $$\frac{(\mu\_{X|C}-\widehat{\mu}\_{X|C})^2+|\sigma^2\_{X|C}-\widehat{\sigma}^2\_{X|C}|}{\widehat{\sigma}^2\_{X|C}}+|\sigma^2\_{X|C}-\widehat{\sigma}^2\_{X|C}|\leq \mu\_{X|C}^2.$$ Intuitively, this inequality requires that the signal level $\mu\_{X|C}^2$ (how far the conditional mean is from zero) must dominate the estimation error $(\mu\_{X|C}-\widehat{\mu}\_{X|C})^2/\widehat{\sigma}^2\_{X|C}$,  $|\sigma^2\_{X|C}-\widehat{\sigma}^2\_{X|C}|/\widehat{\sigma}^2\_{X|C}$, and $|\sigma^2\_{X|C}-\widehat{\sigma}^2\_{X|C}|$. In non-stationary time series, $\mu\_{X|C}$ is typically non-negligible, and our JMCE module is trained exactly to drive $(\mu\_{X|C}-\widehat{\mu}\_{X|C})^2/\widehat{\sigma}^2\_{X|C}$, $|\sigma^2\_{X|C}-\widehat{\sigma}^2\_{X|C}|/\widehat{\sigma}^2\_{X|C}$ and $|\sigma^2\_{X|C}-\widehat{\sigma}^2\_{X|C}|$ to be small

### Rebuttal to Q2
In CW-Flow, we directly replace the terminal distribution with the conditional mean and conditional covariance outputted by a trained JMCE. This removes the need to conditionally whiten the dataset. And after generating samples with CW-Flow, we no longer need to apply the inverse CW transformation. For these reasons, we describe this modification as making the algorithm more efficient.

### Rebuttal to Q1
We greatly appreciate your wise question. In our original submission, we train JMCE and generative model separately. However, motivated by your comment, we explored training JMCE and the generative model jointly in an end-to-end fashion. We have submitted a revised version of our paper. In Appendix D.10 of the revised submission, We successfully trained JMCE and generative models jointly. The results in Table 18 show that the end-to-end approach allows CW-Gen to better capture the correlations in the data and achieves lower CRPS and FID. Although the end-to-end training slightly decreases QICE, the overall performance remains superior to generative models that do not use any prior information.

### Rebuttal to W1
We thank the reviewer for this constructive suggestion and recognizing our paper to have 'consistent improvements' and to be 'clear graphical illustrated'. We address each weakness and questions below. 

Your understanding is correct. Training a CW-Gen model consists of three steps:  
(1) pre-training JMCE,  
(2) conditionally whitening the dataset, and  
(3) training the generative model.  
For CW-Diff, we additionally use the outputs of JMCE to invert the conditional whitening operation during sampling, whereas CW-Flow does not require this step. This separate training pipeline indeed provides simplicity in both implementation and conceptual design. Due to the limit of the ICLR submission format, we will elaborate it in future.

### Rebuttal to Q3
Of course! We are happy to provide more information regarding the predictive performance of JMCE. In Appendix D.4, we include an ablation study for JMCE , and Tables 9-11 report detailed results about its behavior. The 'Separate' setting in Table 11 can be viewed as a baseline, and the experiments show that JMCE provides a more stable eatimation of conditional mean, estimates the sliding-window covariance more accurately and effectively controls the minimum eigenvalue. Moreover, we have added a visualization of JMCE in Fig. 4 of Appendix D.4.


Finally, we would like to thank you again for your review. Your questions and comments have been invaluable in helping us refine the weaknesses and strengthen the paper.

### Rebuttal to Q2
We first use JMCE to obtain the conditional covariance matrix and then apply its diagonal form in CW-GEN. Using only the diagonal conditional covariance (or conditional variances) can indeed substantially accelerate training. We have added a discussion of this point in Appendix D.9 of the revised submission. Furthermore, as shown in Table 14, using only the conditional variances as prior information still yields significant improvements for the generative model; please also refer to our rebuttal to Reviewer NWT6’s W3 for additional details.



We did not consider diagonal covariance parameterizations in the JMCE because a diagonal covariance matrix cannot approximate a general covariance matrix well in terms of the nuclear norm. Diagonal covariance parameterizations lose the ability to control the minimum eigenvalue of the conditional covariance matrix, and therefore the theoretical foundations of JMCE no longer apply.

### Rebuttal to W4
Thank you for your review. We appreciate the time you spent carefully reading our paper. The sentence you mentioned is not incomplete. It is intended to briefly recall the output of JMCE introduced in Section 3.2 and define a new notation. We will improve this sentence in the future.

### Rebuttal to W3
Thank you for your suggestion. We plan to provide a more detailed discussion of the limitations of our method in future work, and we will also separate the related work section from the introduction. However, due to the strict page limit of the ICLR submission format, it is difficult for us to make these changes in the current version.

### Rebuttal to W2
Thanks for the review. The runtime comparison is indeed important. In the revised submission, we add a thorough comparison in Appendix F, Table 19. Besides, we also discussed some accelerating way in Appendix D.9 and D.10.

### Rebuttal to W1 and Q1
We thank the reviewer for the detailed feedback and for recognizing that our work 'theoretically justified', 'well-motivated' and 'improving performance'. Below, we address the specific comments and outline the improvements we have made based on these suggestions.

Thank you for your review. Your suggestion has been extremely valuable to our work. The current training procedure of CW-Gen is indeed two-stage. Inspired by your comment, we explored an end-to-end training strategy in Appendix D.10 of the revised submission, where JMCE and the generative model are trained jointly. The results in Table 18 show that the end-to-end approach allows CW-Gen to better capture the correlations in the data and achieves lower CRPS and FID. Although the end-to-end training slightly decreases QICE, the overall performance remains superior to generative models that do not use any prior information.

### Rebuttal to W3
Thank you for your review. We acknowledge that the original submission unintentionally omitted an evaluation of the independent contributions of different prior components. In the revised submission, we have added the corresponding experiments in **Table 14 of the Appendix D.6**. In brief, we systematically evaluated the performance of CW-Gen under the following prior information configurations: conditional mean only (Mean), diagonal conditional covariance only (Var), full conditional covariance only (Cov), conditional mean combined with conditional variance (Mean \& Var), and conditional mean combined with full covariance (Mean \& Cov). Based on the results in Table 14, we can conclude that the **conditional mean provides the largest individual improvement**. However, **combining the conditional mean with  the conditional variance/covariance yields even better performance**. The performance ranking is as follows: **the Mean & Cov configuration performs best**, followed by Mean \& Var, with Mean alone in third place. When Var or Cov is used individually, CW-Gen exhibits performance degradation; however, it is noteworthy that Cov consistently outperforms Var in the ProbCorr metric, indicating that the full covariance indeed helps the generative model capture inter-variable dependencies more effectively.


Finally, we would like to once again thank you for your review. Your questions and comments have helped us address the weaknesses of our work and improve the overall quality of the paper.

### Rebuttal to W2
We acknowledge that training CW-Gen introduces additional computational cost. However, Tables 2-8 demonstrate that even when paired with simpler baseline models, CW-Gen improves performance across the vast majority of metrics. Moreover, CW-Gen can be applied to high-dimensional datasets, such as the 137-dimensional Solar Energy dataset. In addition, as discussed in our rebuttal to W1, we provide several techniques to further accelerate computation.

### Rebuttal to W1
We sincerely thank the reviewer for recognizing our work to be "novel," "theoretically sound" and "improving performance." We greatly appreciate the constructive feedback. We address each weakness in detail below.

Thank you for your insightful review. Training a CW-Gen model consists of three steps:  
(1) training the JMCE,  
(2) conditionally whitening the dataset, and  
(3) training the generative model.  
The first two steps involve computationally expensive eigen-decomposition and SVD operations. We acknowledge that they may affect the efficiency of CW-Gen on high-dimensional datasets; however, we have made the following efforts to significantly improve computational efficiency while maintaining competitive performance, thereby facilitating real-time deployment in high-dimensional scenarios.


In step (2), the conditional whitening stage, we added Appendix D.9 in the revised submission. In short, suppose $X \in \mathbb{R}^d$ is a random variable with covariance $\mathrm{Cov}(X) = \Sigma = L L^\top$, where $L$ is a lower-triangular matrix. Then it is straightforward to verify that $\mathrm{Cov}(L^{-1} X) = L^{-1} L L^\top L^{\top^{-1}} = I_d$. Therefore, we can avoid eigen-decomposition and instead compute an inverse of a **lower-triangular matrix**. We also added some timing results in Appendix F. On the higher-dimensional dataset (Solar Energy), we are able to reduce the time of step (2) from 14,460 seconds to 52.7 seconds! 

For steps (1) and (3), we have proposed an end-to-end joint training scheme for JMCE and generative models (CW-E2E) in Appendix D.10 of the revised submission. On the Solar Energy dataset, the total training time of the CW-E2E model has been significantly reduced from 39,329 seconds to 8,120 seconds. We also present the practical performance of CW-E2E in Table 18. The results demonstrate that CW-E2E remains competitive across all metrics; in fact, it even outperforms the method proposed in the main paper in terms of CRPS, ProbCorr and Conditional FID.

### Conditionally Whitened Generative Models for Probabilistic Time Series Forecasting


## Meta review / decision
### Paper Decision
Accept (Poster)

## PDF extracted text (first pages)
```text
Published as a conference paper at ICLR 2026
CONDITIONALLY WHITENED GENERATIVE MODELS
FOR PROBABILISTIC TIME SERIES FORECASTING
Yanfeng Yang*
Graduate University of Advanced Studies & The Institute of Statistical Mathematics
Tokyo, Japan
yanfengyang0316@gmail.com
Siwei Chen, Pingping Hu, Zhaotong Shen, Yingjie Zhang, Zhuoran Sun, Shuai Li,
Ziqi Chen*
East China Normal University,
Shanghai, China
zqchen@fem.ecnu.edu.cn
Kenji Fukumizu*
The Institute of Statistical Mathematics
Tokyo, Japan
fukumizu@ism.ac.jp
ABSTRACT
Probabilistic forecasting of multivariate time series is challenging due to non-
stationarity, inter-variable dependencies, and distribution shifts. While recent dif-
fusion and flow matching models have shown promise, they often ignore informa-
tive priors such as conditional means and covariances. In this work, we propose
Conditionally Whitened Generative Models (CW-Gen), a framework that incorpo-
rates prior information through conditional whitening. Theoretically, we establish
sufficient conditions under which replacing the traditional terminal distribution
of diffusion models, namely the standard multivariate normal, with a multivari-
ate normal distribution parameterized by estimators of the conditional mean and
covariance improves sample quality. Guided by this analysis, we design a novel
Joint Mean-Covariance Estimator (JMCE) that simultaneously learns the condi-
tional mean and sliding-window covariance. Building on JMCE, we introduce
Conditionally Whitened Diffusion Models (CW-Diff) and extend them to Con-
ditionally Whitened Flow Matching (CW-Flow). Experiments on five real-world
datasets with six state-of-the-art generative models demonstrate that CW-Gen con-
sistently enhances predictive performance, capturing non-stationary dynamics and
inter-variable correlations more effectively than prior-free approaches. Empirical
results further demonstrate that CW-Gen can effectively mitigate the effects of
distribution shift.
1 I NTRODUCTION
Time series analysis has a long history, with classical approaches such as ARIMA, state-space
models, and vector autoregressions (V AR) (Box & Jenkins, 1976; Durbin & Koopman, 2012;
L¨utkepohl, 2007). Although these methods have been widely applied, they often struggle with
high-dimensionality and complex data structures that arise in modern applications. More recently,
neural architectures have demonstrated superior predictive accuracy, such as recurrent neural net-
works (RNN), Long Short-Term Memory (LSTM), and Transformers (Sherstinsky, 2020; Hochre-
iter & Schmidhuber, 1997; Vaswani et al., 2017). However, these neural models primarily focus on
forecasting the conditional mean of future sequences given historical observations, while providing
All authors contributed equally. *Corresponding authors.
1
Published as a conference paper at ICLR 2026
little to uncertainty quantification. These limitations have motivated the development of probabilis-
tic forecasting, which seeks to model not only point predictions but also the associated uncertainty.
Multivariate time series probabilistic forecasting has recently emerged as a key methodology for
quantifying predictive uncertainty, enabling informed decision-making in numerous real-world ap-
plications in diverse domains such as finance, healthcare, environmental science, and transportation
(Lim & Zohren, 2021). Formally, the task involves learning the probability distribution PX|C of a
future time series X0 ∈ Rd×Tf of discrete time conditioned on its corresponding historical obser-
vations C ∈ Rd×Th, where the integers Tf and Th denote the lengths of future and historical time
series, respectively, and d represents the dimensionality of each time step. However, this task still
remains highly challenging, primarily due to (i) non-stationary characteristics, manifested through
long-term trends, seasonal effects, and heteroscedasticity (Li et al., 2024; Ye et al., 2025); (ii) com-
plex inter-variable dependency structures (Yuan & Qiao, 2024); (iii) inherent data uncertainty, such
as short-term fluctuations (Ye et al., 2025); and (iv) potential distribution shifts between training and
testing data (Kim et al., 2022).
In response to these challenges, recent advances in generative learning, especially diffusion mod-
els, focus on accurately estimating the conditional distribution PX|C. TimeGrad employs a RNN to
encode historical observations and generates forecasts autoregressively, but suffers from cumulative
errors and slow computation (Rasul et al., 2021). CSDI uses a 2D-Transformer for imputation and
forecasting (Tashiro et al., 2021), while SSSD employs a Structured State Space Model to reduce
computational cost and emphasize temporal dependence (Alcaraz & Strodthoff, 2023). Neverthe-
less, CSDI, SSSD, and TimeGrad all struggle with long-term forecasting (Shen & Kwok, 2023).
Diffusion-TS leverages a transformer to decompose time series into trend, seasonal, and residual
components for generation, whereas FlowTS accelerates generation using rectified flow (Yuan &
Qiao, 2024; Hu et al., 2025).
Although the aforementioned generative models have achieved promising performance, they ignore
informative priors. Such priors, derived from historical observations or auxiliary models, can sub-
stantially improve conditional generative modeling. To the best of our knowledge, CARD is the
first model to incorporate prior information into conditional diffusion models (Han et al., 2022). It
pretrains a regressor to estimate the conditional mean E [X0|C] and integrates this regressor into the
diffusion process, thereby enhancing conditional generation. In time series forecasting, regressing
the conditional mean and incorporating it into diffusion models as a prior has become a common
practice, as it alleviates the difficulty of modeling non-stationary distributions. TimeDiff adopts a
linear regressor to capture short-term patterns and employs a future mixup strategy during training
to mitigate boundary disharmony (Shen & Kwok, 2023). However, its linear design limits the ability
to capture complex trends and fluctuations. TMDM addresses this limitation by integrating a non-
linear regressor into the variational inference framework, enabling joint training of the regressor and
the diffusion model (Li et al., 2024). The regressor for E [X0|C] (hereafter referred to as the mean
regressor) can capture trends, seasonality, and fluctuations but is vulnerable to heteroscedasticity.
Building on this line, NsDiff addresses this by introducing two pretrained models: a mean regressor
and a variance regressor, the latter estimating the conditional variance of each variable within a slid-
ing window (Ye et al., 2025). By incorporating both regressors into the diffusion process, NsDiff
models heteroscedasticity more effectively. Despite these innovations, the method still suffers from
certain limitations, particularly the overly complex reverse process and the neglect of correlations
among variables. A detailed discussion of these limitations is provided in Appendix A.1. Beyond
diffusion models, S2DBM employs a diffusion bridge variant and incorporates the mean regressor in
the same manner as CARD (Yang et al., 2024), which limits its ability to handle heteroscedasticity.
TsFlow uses Gaussian Processes (GPs) as both the mean and variance regressors (Kollovieh et al.,
2025), but its design is restricted to univariate forecasting with short horizons and inherits the typical
drawbacks of GPs, including kernel sensitivity and cubic computational cost.
Building on the preceding literature, it is well established that carefully designed priors can sub-
stantially enhance generative models. Yet several key questions remain unresolved: How exactly do
priors contribute to these improvements, and how accurate must the mean and variance regressors
be to provide tangible benefits? How can such regressors be effectively trained, and are there theo-
retical guarantees supporting their impact? Most existing approaches incorporate mean and variance
regressors into diffusion models by following the designs of CARD and DDPM (Han et al., 2022;
2
Published as a conference paper at ICLR 2026
Ho et al., 2020). This raises a further question: is this mechanism redundant or inefficient, and could
it be simplified within more flexible diffusion frameworks?
Motivated by these questions, we introduce the Conditional Whitened Generative Models (CW-
Gen). Our main contributions are:
• We develop a unified framework for conditional generation, CW-Gen, with two instantiations:
the Conditional Whitened Diffusion Model (CW-Diff) and the Conditional Whitened Flow
Matching (CW-Flow). Several prior methods (Han et al., 2022; Li et al., 2024; Ye et al., 2025) can
be viewed as special cases of this framework. Furthermore, CW-Gen allows seamless integration
with diverse diffusion models.
• We provide theoretical analysis that establishes sufficient conditions under which CW-Gen im-
proves sample quality, as stated in Theorem 1 and Theorem 2 in Appendix C.
• Motivated by Theorems 1 and 2, we propose a novel joint estimation procedure for the condi-
tional mean and sliding-window covariance of time series. Empirically, it achieves high accuracy
while effectively controlling covariance eigenvalues, ensuring stability and robustness in genera-
tive modeling.
• We integrate CW-Gen with six state-of-the-art generative models and evaluate them on five real-
world datasets. Empirical results show consistent improvements in capturing non-stationarity,
inter-variable dependencies, and overall sample quality, while also mitigating distribution shift.
2 P RELIMINARIES
2.1 D ENOISING DIFFUSION PROBABILISTIC MODELS (DDPM)
Most of the diffusion models discussed in Section 1 follow the DDPM framework (Ho et al., 2020),
which we review below in a general conditional setting. Let (X0, C) be a random vector with the
joint distribution PX,C, where X0 ∈ Rdx and C ∈ Rdc. The (conditional) DDPM aims to learn the
conditional distribution PX|C and generate samples that match this distribution through a forward
and a reverse process. In the forward process, Gaussian noises are gradually added into X0 by a
stochastic differential equation (SDE):
dXτ = − 1
2 βτ Xτ dτ +
p
βτ dWτ , τ ∈ [0, 1], X 0 ∼ PX|C,
where βτ > 0 and Wτ is a Brownian motion in Rdx. We use τ for the time of diffusion throughout
this paper, while t is the index for time series. From the properties of Ornstein–Uhlenbeck-process
(OU-process), we derive the marginal distribution of Xτ :
Xτ
d
= ατ X0 + στ ϵ, ϵ ∼ N(0, Idx),
where ατ := exp

−
R τ
0 βsds/2
	
, σ2
τ := 1 − α2
τ ,
d
= denotes equality in distribution, and Idx is the
dx-dimensional identity matrix. By construction of βτ , the integral
R 1
0 βsds is sufficiently large, so
the distribution of X1 (the terminal distribution) is well-approximated by N(0, Idx). In the reverse
process, a standard Gaussian noise
←
X1 is gradually denoised by an SDE:
d
←
X τ =

− 1
2 βτ
←
X τ − βτ ∇x log pτ(
←
X τ |C)

dτ +
p
βτ d
←
W τ , (1)
where τ starts from τ = 1 and ends at τ = τmin, with τmin being an early stopping time close
to 0, and
←
W τ is a Brownian motion. In (1), pτ(·|C) and ∇x log pτ(·|C) denote the conditional
density and score function of Xτ given C, respectively. Since the conditional score function is
intractable, Ho et al. (2020) and Song et al. (2021) proposed approximating it with a neural network
sθ parameterized by θ, trained by minimizing:
E(X0,C),τ,ϵ ∥sθ (ατ X0 + στ ϵ, C, τ) + ϵ/στ ∥2 ,
where τ ∼ U(0, 1] and ϵ ∼ N(0, Idx). Finally, substituting ∇x log pτ(
←
X τ |C) in (1) with
sθ(
←
X τ , C, τ) yields the reverse process:
d
←
X τ =

− 1
2 βτ
←
X τ − βτ sθ(
←
X τ , C, τ)

dτ +
p
βτ d
←
W τ , τ ∈ [τmin, 1].
3
Published as a conference paper at ICLR 2026
2.2 F LOW MATCHING
Unlike diffusion models based on SDEs, Flow Matching (FM) employs an ordinary differential
equation (ODE) to connect Gaussian noise ϵ ∼ N(0, Idx) with the data X0 ∼ PX|C (Lipman et al.,
2023):
dXτ = (ϵ − X0)dτ, τ ∈ [0, 1]. (2)
A neural network vψ, parameterized by ψ, learns the vector field of (2) by minimizing:
E(X0,C),τ,ϵ∥ϵ − X0 − vψ(X0 + τ(ϵ − X0), C, τ)∥2.
Given the learned vector field, FM generates samples by solving the ODE:
d
←
X τ = −vψ(
←
X τ , C, τ)dτ
from τ = 1 to τ = τmin, where
←
X1 is Gaussian noise. The final state
←
X τmin is the generated sample.
3 T HEORY AND JOINT MEAN –COVARIANCE ESTIMATOR (JMCE)
3.1 T HEORETICAL FOUNDATION
A key question addressed in this subsection is how modifying the terminal distribution N(0, Idx)
can enhance generation quality. The total variation distance between the generated distribution of
a diffusion model and the true distribution grows as the convergence error of the forward process
increases, where the latter involves the Kullback–Leibler divergence (KLD) between PX|C and the
terminal distribution DKL
 
PX|C ∥ N(0, Idx)

as a factor in the error (Oko et al., 2023; Chen et al.,
2023; Fu et al., 2024). Hence, a smaller value of this KLD leads to samples that better match PX|C.
This insight motivates replacing the standard terminal distribution N(0, Idx) with N(µX|C, ΣX|C),
where µX|C and ΣX|C are the true conditional mean and covariance of X given C. Since these
quantities are unknown in practice, they must be estimated by bµX|C andbΣX|C. The advantage of
this replacement can then be measured by the reduction in
DKL

PX|C ∥ N(bµX|C,bΣX|C)

relative to DKL
 
PX|C ∥ N(0, Idx)

.
This raises the fundamental question of when replacing the terminal distribution N(0, Idx) with
N(bµX|C,bΣX|C) improves generation quality, which the following theorem addresses.
Theorem 1 Let PX|C denote the true conditional distribution ofX ∈ Rdx given C, with conditional
mean µX|C and positive-definite conditional covariance ΣX|C. Define Q0 := N(0, Idx) and bQ :=
N(bµX|C,bΣX|C), wherebµX|C andbΣX|C are estimators ofµX|C and ΣX|C, respectively. LetbλX|C,i
denote the i-th eigenvalues of bΣX|C, for i = 1 , 2, . . . , dx. A sufficient condition ensuring that
DKL(PX|C ∥bQ) ≤ DKL(PX|C ∥ Q0) is:

min
i∈{1,...,dx}
bλX|C,i
−1
∥µX|C −bµX|C∥2
2 + ∥ΣX|C −bΣX|C∥N

+
p
dx ∥ΣX|C −bΣX|C∥F ≤ ∥µX|C∥2
2.
(3)
where
ΣX|C −bΣX|C

N
=Pdx
i=1esi andesi is the i-th singular value of ΣX|C −bΣX|C.
Theorem 1 states that when (3) holds, replacing Q0 with bQ reduces the KLD between PX|C and the
terminal distribution, thereby improving generation quality. Importantly, it provides a foundation for
designing loss functions to estimateµX|C and ΣX|C, as detailed in Equation (4) below. We emphasize
that the estimators of µX|C and ΣX|C are obtained by minimizing the sample counterpart of the left-
hand side of (3), as detailed in the next subsection.
In order for (3) to hold, it is necessary to obtain accurate estimators of both µX|C and ΣX|C.
The estimation accuracy of ΣX|C is measured in terms of both the Frobenius norm and the nu-
clear norm, with the latter characterized by Pdx
i=1esi. We employ a Cholesky decomposition
4
Published as a conference paper at ICLR 2026
and introduce a penalty term into the loss function (4) to enforce that the smallest eigenvalue,
mini∈{1,...,dx}{bλX|C,i}, remains strictly positive and bounded away from zero, as detailed in the
next subsection. Furthermore, in non-stationary time series, µX|C often exhibits sharp variations
and thus deviates from zero. Consequently, (3) is more likely to hold when accurate estimators of
both µX|C and ΣX|C are available. Conversely, (3) may fail to hold in unfavorable regimes—for
example, when the signal magnitude ∥µX|C∥2
2 is small, the estimators of µX|C and ΣX|C are in-
accurate, or the inverse of the smallest eigenvalue becomes large. In such cases, incorporating the
corresponding prior models can potentially degrade performance. In the next subsection, we design
a novel loss function to mitigate this risk. A detailed discussion can be found in Appendix D.
We further identify the scenarios in which our proposed replacement outperforms TMDM and Ns-
Diff (Li et al., 2024; Ye et al., 2025), as formally established in Theorem 2 in Appendix C.
3.2 J OINT MEAN –COVARIANCE ESTIMATOR (JMCE)
Theorem 1 establishes that accurate estimators of both the conditional mean and covariance can
improve the quality of samples generated by diffusion models. Guided by the sufficient conditions
(3), we design a novel Joint Mean–Covariance Estimator (JMCE).
In terms of time series, directly estimating the true conditional covariance is extremely challenging,
as it is often highly complex and non-smooth, which makes consistent estimation difficult. Instead,
the sliding-window covariance is preferable, as it not only offers more accurate approximations but
also improves computational efficiency (Iwakura et al., 2008; Chen et al., 2024). Motivated by this,
we estimate the sliding-window conditional covariance, rather than the true conditional covariance.
LeteΣX0,t ∈ Rd×d denote the sliding-window covariance at time t, and let bΣX0,t|C ∈ Rd×d be an
estimator of eΣX0,t for t = 1 , . . . , Tf . We design a non-autoregressive model to simultaneously
output:
bµX|C,bL1|C, . . . ,bLTf |C = JMCE(C)
with bΣX0,t|C := bLt|CbL⊤
t|C, for t = 1 , . . . , Tf and all bLt|C are lower-triangle matrices. This de-
sign, inspired by Cholesky decomposition, guarantees that all bΣX0,t|C are positive semi-definite
(PSD). The detailed algorithm of JMCE(C) can be found in Appendix B. In our implementa-
tion, we use a Non-stationary Transformer (Liu et al., 2022) as the backbone of JMCE. Based
on (3) in Theorem 1, we construct the trainning loss in JMCE by combining three compo-
nents: L2 := E(X0,C)
X0 −bµX|C
2
2 , LF := E(X0,C)
PTf
t=1
eΣX0,t −bΣX0,t|C

F
, and LSVD :=
E(X0,C)
PTf
t=1
eΣX0,t −bΣX0,t|C

N
. The smallest eigenvalues of bΣX0,t|C have a crucial impact on
the magnitude of the left-hand side of inequality (3). We thus introduce a regularization term that
enforces the smallest eigenvalues ofbΣX0,t|C to remain strictly positive and bounded away from zero,
thereby avoiding numerical instability and rank deficiency. Let λmin be a tunable hyperparameter.
The penalty term is defined as:
Rλmin
 bΣX0,t|C

:=
dX
i=1
ReLU
 
λmin −bλbΣX0 ,t|C,i

,
wherebλbΣX0 ,t|C,i(i = 1, . . . , d) denote the eigenvalues ofbΣX0,t|C, and ReLU(x) = max{x, 0}. It is
indicated that any eigenvalue smaller thanλmin will be penalized. The overall training loss in JMCE
for the conditional mean and covariance is defined as:
LJMCE = L2 + LSVD + λmin
p
d · Tf LF + wEigen ·
TfX
t=1
Rλmin

bΣX0,t|C

, (4)
where wEigen is a hyperparameter that controls the strength of the penalty. Empirically, we choose
wEigen ∼ O(λ−1
min). It is important to note that (4) is specifically designed to ensure that (3) holds.
The algorithm of the joint estimator can be found in Appendix B. JMCE excels at estimating the
conditional mean and covariance while controlling the minimal eigenvalue. We conduct a substantial
ablation study to show the advantages, and discuss them in Appendix E.
5
Published as a conference paper at ICLR 2026
4 C ONDITIONAL WHITENED GENERATIVE MODELS (CW-G EN)
In this section, we propose Conditionally whitened diffusion models (CW-Diff) and Conditionally
whitened flow matching (CW-Flow). Together, we call them Conditionally Whitened Generative
Models (CW-Gen).
4.1 C ONDITIONALLY WHITENED DIFFUSION MODELS (CW-D IFF)
Our JMCE outputs bµX|C ∈ Rd×Tf and bΣX0|C := [bΣX0,1|C, . . . ,bΣX0,Tf |C] ∈ Rd×d×Tf . Since all
bΣX0,t|C are positive definite, we can compute bΣk
X0|C := [bΣk
X0,1|C, . . . ,bΣk
X0,Tf |C] ∈ Rd×d×Tf for
k ∈ {− 0.5, 0.5} via eigen-decomposition. Let ϵ := [ ϵ1, . . . , ϵTf ] ∈ Rd×Tf , where each column
ϵt ∼ N(0, Id) and the columns ϵ1, . . . , ϵTf are mutually independent. We define the tensor operation
bΣ0.5
X0|C ◦ ϵ := [bΣ0.5
X0,1|C · ϵ1, . . . ,bΣ0.5
X0,Tf |C · ϵTf ] ∈ Rd×Tf . (5)
Accordingly, we say that a tensor follows N (bµX|C,bΣX0|C) if it has the same distribution asbΣ0.5
X0|C ◦
```
