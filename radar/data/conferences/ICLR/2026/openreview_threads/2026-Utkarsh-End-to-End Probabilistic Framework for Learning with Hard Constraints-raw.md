# End-to-End Probabilistic Framework for Learning with Hard Constraints — OpenReview Raw Thread

- Forum: https://openreview.net/forum?id=RPowYXiRmW
- PDF: https://openreview.net/pdf?id=RPowYXiRmW
- Section: 二、时间序列预测：分布鲁棒、多变量建模与后处理优化
- Zhihu score: 6.5
- Venue status: ICLR 2026 Poster

## Submission metadata
- Authors: Utkarsh Utkarsh, Danielle C. Maddix, Ruijun Ma, Michael W. Mahoney, Bernie Wang
- Primary area: applications to physical sciences (physics, chemistry, biology, etc.)
- Keywords: scientific machine learning, conservation laws, physically constrained machine learning, partial differential equations, time series forecasting, uncertainty quantification

## Abstract
We present ProbHardE2E, a probabilistic forecasting framework that incorporates hard operational/physical constraints and provides uncertainty quantification. Our methodology uses a novel differentiable probabilistic projection layer (DPPL) that can be combined with a wide range of neural network architectures. DPPL allows the model to learn the system in an end-to-end manner, compared to other approaches where constraints are satisfied either through a post-processing step or at inference. ProbHardE2E optimizes a strictly proper scoring rule, without making any distributional assumptions on the target, which enables it to obtain robust distributional estimates (in contrast to existing approaches that generally optimize likelihood-based objectives, which can be biased by their distributional assumptions and model choices); and it can incorporate a range of non-linear constraints (increasing the power of modeling and flexibility). We apply ProbHardE2E in learning partial differential equations with uncertainty estimates and to probabilistic time-series forecasting, showcasing it as a broadly applicable general framework that connects these seemingly disparate domains.  Our code is available at https://github.com/amazon-science/probharde2e.

## Reviews
### Reviewer_LXk5
- summary: This paper proposes an end-to-end probabilistic framework that strictly enforces hard constraints during training while producing full predictive distributions (mean + covariance) for uncertainty quantification (UQ). The technical core is the Differentiable Probabilistic Projection Layer (DPPL), which projects an unconstrained probabilistic prediction onto the constraint manifold. For equality/linear constraints, the projection/transformation has closed forms. For nonlinear/convex constraints, the DPPL layer uses Newton/KKT iterations to compute the projection and implicit differentiation (lin
- strengths: 1. The main nolvety of this paper is to propose an end-to-end enforcement of hard constraints, where constraints are optimized as part of learning, not only enforced at post-processing or inference as in convention.

2. It also enables joint UQ and constraint satisfaction, thus suitable for safety/physics/constrained engineering tasks.

3. The sample-free & closed-form CRPS, combined with analytic projection propagations gives substantial training speedups.

4. Generality: the framework covers l
- weaknesses: 1. The major concern is that the method relies on first-order approximations to linearize the nonlinear function transformation, the KKT system, and the constraints, which together may bring too much estimation errors. Specifically, the covariance propagation relies on a first-order approximation of the Jacobian, thus the UQ under strong nonlinearity constraint can be misestimated. Also the linearized KKT system is only locally valid and can fail to converge or even diverge if the constraint is highly nonlinear or the initial point is far from feasible. 

2. The closed-form sample-free CRPS loss depends on using tractable distribution families (e.g., Gaussian). For multimodal/complex posteriors, it still requires sampling or approximations, thus the advantage of computational efficiency is not guaranteed.

3. In some places, the experimental results are not consistent with the claims made in the paper.
- questions: 1. Is it possible to provide a synthetic analysis of the effect of the first-order approximations on the results, or compute the approximation errors? Have you considered other methods than the linearized KKT, such as Gauss-Newton augmented Lagrangian for nonlinear constraints? The experimental results are not strong enough to support the superior performance of the proposed method (details in the 2nd question below), so maybe relaxing some of the approximations would improve the peformance.
 
2. The paper overclaims its performance based on the experimental results in some places. When analyzing these results,  sometimes it is hard to relate the numbers in the tables to the conclusions stated in the paper. For example, 
   - When addressing Q1, the paper stated "Specifically, when measure
- rating: 6 | confidence: 4

### Reviewer_8rdZ
- summary: The paper proposes ProbHardE2E, a unified probabilistic framework for learning under hard constraints with uncertainty quantification. The core module DPPL turns an unconstrained probabilistic predictor (e.g., DeepVAR for time series or VarianceNO for PDEs) into a constraint-satisfying probabilistic model in an end-to-end pipeline. Training is sample-free: the model predicts location–scale parameters $(\mu, \Sigma)$ and DPPL projects these to constrained parameters $(\hat{\mu}, \hat{\Sigma})$ via a delta-method linearization of a projection map $T$, and the paper optimizes CRPS on the constrai
- strengths: - The method is clearly formulated in a principled “predictor–corrector” view.
- The authors provide an exact handling for linear constraints.
- The training objective is close-formed and sampling free.
- weaknesses: - First-order DPPL approximation with no error bounds (risk under strong nonlinearity/variance). 
- Loss/evaluation assume independence while the projected posterior is generally correlated. 
- Practical experiments lock $Q$ to diagonal/identity, limiting the benefits of oblique projections and potentially biasing outcomes. 
- Nonlinear equality projection claims “strict feasibility,” but non-convexity and active-set issues are largely handled numerically without theoretical or robustness analysis. 
- Inequality-constraint metrics are thin (CE defined for equalities), so support for those claims is more qualitative than quantitative.
- questions: 1. Can you provide error bounds (or at least empirical error studies) for the delta-method approximation vs exact sampling across varying nonlinearity/variance.
2. Can you report multivariate calibration checks (e.g., energy score/logS), not just diagonal-CRPS, given the fact that you are doing multivariate forecasting, where CRPS is not strictly proper. 
3. Include ablations on $Q$ (identity vs diagonal vs low-rank) with runtime/accuracy trade-offs, since $Q$ defines the projection geometry. 
4. The claim "We demonstrate the importance of using a strictly proper scoring rule for evaluating probabilistic predictions, e.g., the CRPS, rather than negative log-likelihood (NLL)." is completely wrong, NLL is strictly proper.
- rating: 6 | confidence: 4

### Reviewer_971x
- summary: The authors present ProbHardE2E, a probabilistic forecasting framework that incorporates hard operational and physical constraints while providing uncertainty quantification. Their methodology introduces a novel differentiable probabilistic projection layer (DPPL) that can be integrated with a wide range of neural network architectures. The DPPL enables the model to learn the system in an end-to-end manner, in contrast to other approaches where constraints are enforced only through post-processing or during inference.

ProbHardE2E optimizes a strictly proper scoring rule without making any dis
- strengths: 1. The proposed method uses strictly proper scoring rules (e.g., CRPS) instead of log-likelihood objectives, reducing the learning bias caused by incorrect distributional assumptions.
2. The training process can be sample-free, offering potential efficiency advantages.
3. In both time-series forecasting and PDE-solving tasks, the proposed method demonstrates strong empirical performance.
- weaknesses: 1. During inference, the authors indicate that a projection must be computed at every step. Does this imply that the computational cost during inference could be substantial? Could the authors provide an analysis of the time complexity for both training and inference? Similarly, although the training process is sampling-free, repeatedly computing the Jacobian matrix can also increase computational time, especially when dealing with high-dimensional data or scenarios involving multiple constraints.
- questions: please refer to the weakness
- rating: 8 | confidence: 3

### Reviewer_MxEb
- summary: The paper presents *ProbHardE2E*, an end-to-end probabilistic prediction framework that incorporates hard constraints. The approach first trains an unconstrained probabilistic backbone using the CRPS, chosen for its robustness and existence properties compared to the NLL. The main contribution is the *differentiable probabilistic projection layer (DDPL)*, which projects unconstrained predictions onto constrained probabilistic outputs (mean and covariance) during training and onto corresponding random samples during inference.  

For a location–scale predictive family, the authors derive closed
- strengths: The paper provides an interesting combination of probabilistic learning and optimization under hard constraints. To my best judgement, the author have a good grasp of the theory and provide detailed proofs for their theoretical claims. I particularly enjoyed the idea of analyzing the push-forward distribution of the constrained optimization problem and showing ways to derive the anyltical solution for a location-scale family.
The numerical experiments support the author's claims, showing improve
- weaknesses: I believe, the presentation and readability could be improved, and some details of the method might need further clarification, see questions.
- questions: ## CRPS notation
Equation (2) uses the CRPS from Gneiting & Raftery (2007):  
$$
\mathrm{CRPS}(Y,y)=\tfrac12\mathbb{E}|Y-Y'|-\mathbb{E}|Y-y|.
$$
However, this corresponds to a proper scoring rules that is defined such that $S(Q,Q)\ge S(P,Q)$, i.e., the true distribution maximizes the score. This conflicts with the minimization objectives in (3) and (4).  
Since the closed-form in §3.5 is derived for minimization, as opposed to (2), the sign in (2) should be flipped for consistency. This is likely a notational issue and easily corrected.

---

## Notation in §3.1
The notation in §3.1 is somewhat inconsistent.
You define $\mathcal{Y} \subset \mathbb{R}^{k}$ as the space of predicted distribution parameters,(l. 104), but later (l. 111) use $\mathcal{Y}$ for the space of constrained distributi
- rating: 6 | confidence: 3

## Author comments / rebuttal
### Author comment
We are happy that we have addressed your concerns and that you maintain your positive score.  We have fixed that remaining typo in the revised version. Thank you again for your detailed review that helped improve the paper's clarity.

### Summary of our rebuttal
Dear AC, PC, and SAC,

We understand that this is a challenging period, and that the new ICLR policies have significantly increased your workload. We would like to highlight that all four reviewers expressed a positive assessment of the submission both pre- and post-rebuttal, and we successfully further addressed all comments and concerns during the rebuttal. We are grateful for the thoughtful evaluations provided by all four reviewers, which have helped to improve the quality and thoroughness of the paper. We have added the changes to the revised manuscript in red. To help minimize the time you need to spend, we have summarized each reviewer's feedback along with our corresponding rebuttal below:
- **Reviewer LXk5** emphasizes the novelty of our end-to-end enforcement of hard constraints and the generality of the constraint families supported by our framework, and maintained a positive score of **6** after our clarifications.
- **Reviewer 8rdZ** highlights that our method is clearly formulated in a principled predictor–corrector view, and confirmed that our rebuttal fully addressed the core concerns, maintaining a positive evaluation of **6**.
- **Reviewer 971x** underscores that our work introduces a novel differentiable probabilistic projection layer (DPPL) that integrates seamlessly with diverse architectures, and that our approach shows strong empirical performance; they confirmed that all questions regarding computation and analysis were effectively addressed and retained their positive score of **8**.
- **Reviewer MxEb** highlighted our work as having a clear contribution, sound theoretical derivations, and strong empirical validation. They acknowledged that our responses fully resolved the minor issues around notation and problem formulation and increased their score from **6 to 8** after our rebuttal, describing the paper as "a strong and well-suited contribution for the venue."

Across reviewers, there is **unanimous agreement** that the paper presents a novel and valuable framework (ProbHardE2E), offers strong theoretical grounding, and demonstrates solid empirical results. We hope this summary is helpful, and we appreciate the committee's efforts under the unusual circumstances.

Best regards,

The Authors

### Author comment
We thank the reviewer for their continued positive perception and support of the paper,  highlighting it being a "strong and well-suited contribution for the venue". We are glad that our responses satisfactorily addressed your concerns, and your consideration in increasing our rating of the paper. Your comments and questions were helpful in improving the quality and thoroughness of the paper.  Thank you again for your meticulous review and constructive feedback.

### Author comment
We thank the reviewer for the follow-up. We are glad that our revisions satisfactorily addressed the core concerns, and we appreciate the reviewer's positive assessment of the paper. Thank you again for the careful reading and constructive feedback.

### Author comment
We thank the reviewer for the careful reading and constructive feedback. We are especially grateful for the positive assessment that our work is “a well-written and valuable paper with a clear contribution, sound theoretical derivations, and strong empirical validation.” We also appreciate the comment that the analysis of the push-forward distribution and the derivation of analytic solutions for location–scale families were particularly effective. We address the reviewer’s comments and questions below.

We appreciate the reviewer’s thorough analysis and attention to notation and presentation. We have updated these in the revised manuscript and address your questions below.

### CRPS notation

We thank the reviewer for catching this and agree that the sign in equation (2) should be flipped for consistency, as we refer to the minimization of CRPS. We have updated this in our revised manuscript.

### Notation in §3.1

Yes, $\mathcal{Y}$ denotes the space of constrained distribution parameters, which is the output of the neural network $f\_{\theta}$, where $\theta \in \Theta$ denotes the network parameters and $\phi^{(i)} \in \Phi $ denotes the input training data. Our notation $\mathbf{Y}\_{\theta}(\phi^{(i)})$ denotes the conditional predictive distribution given $\phi^{(i)}$. You are also correct that $\mathbf{Y}_{\theta}$ is a random variable that is the output of the reparameterization function $r(\hat{f}\_\theta(\phi^{(i)}), \xi)$ in Eqn. 6, for noise $\xi \sim p(\xi) \in \mathbb{R}^n$. Any constrained sample drawn from $\mathbf{Y}\_{\theta}$ is in $\mathbb{R}^n$. We have clarified this and corrected the notation in Section 3.1 of the revised version.


### Framing of log-likelihood and CRPS

We agree that our motivation to use CRPS is for its advantageous properties, especially under misspecification. We have rephrased this sentence in the abstract and Section 3.1 of the revised version to focus more on these advantages and observed empirical gains. The past baseline methods, e.g., ProbConserv and Operator-ProbConserv in the PDEs community, had been using NLL, and we empirically showed in our work the benefit of training with CRPS.

Yes, it is a very interesting direction to test ProbHardE2E with other proper scoring rules, e.g., energy or kernel scores, and leave this as an exciting direction for future work.

### Discussion of unique solutions

We agree that ProbHardE2E with linear constraints is designed for underdetermined systems.  On lines 243-244, we stated that the $q \times n$ matrix needs to be full row-rank $q$, where $q \le n$. We have clarified that ProbHardE2E applies to underdetermined systems when $q < n$ in the revised version. In addition, we have added a discussion on the uniqueness and degeneration to point predictions when $q=n$ to the end of Appendix C.1. In the case of $q = n$, other baselines, e.g., HardC from ProbConserv, have not projected the covariance. We have experimental results with this HardC baseline in Table 

### Author comment
We thank the reviewer for recognizing the novelty of our “broadly applicable general” framework that “bridges seemingly disparate domains.” We are grateful that the reviewer highlighted the contribution of our differentiable probabilistic projection layer (DPPL), the benefits of optimizing strictly proper scoring rules such as CRPS, and the advantages of our sample-free training procedure. We address your questions below.


### Inference cost

We agree with the reviewer’s interpretation that, indeed, during inference, the projection must be computed at every step. However, the computational cost is not as large as incorporating sampling during training, where backpropagation through many samples introduces substantial compute and memory overhead. This design is intentional: ProbHardE2E keeps DPPL training sampling-free for efficiency, while at inference DPPL projects samples to ensure strict feasibility, which is important in safety-critical applications. Certain structures (e.g., linear constraints) further alleviate this cost, and we explicitly derive closed-form expressions for these cases. Solving a nonlinear system via Newton’s method typically requires $(O(n^3))$ per iteration, while linear constraints reduce this to $(O(n^2))$. All projections are parallelized across batch dimensions. We are not aware of any work that models arbitrary nonlinear constraints as hard requirements while being computationally more efficient.

### Training cost and comparison to sampling

We agree that computing the Jacobian matrix increases computational time. In our case, we compute the Jacobian using reverse-mode automatic differentiation, which is significantly faster than finite-difference or forward-mode approaches. By design, we automatically handle multiple constraints; even for nonlinear PME we use IC, BC, and conservation constraints together, forming a full row-rank $q \times n$ structure ($q < n$), where reverse-mode AD requires only $q$ evaluations. The computational complexity matches that of the projection itself: $O(n^3)$ for nonlinear constraints and $O(n^2)$ for linear constraints. The additional memory cost for backpropagating through the linearized KKT system is approximately $O(n^2)$ to store intermediate matrices. For our Gauss-Newton case, the linear solve is cheaper at only $O(q^3)$. (See Appendix C.2 for details).

By contrast, sampling-based UQ methods incur $O(Sq^3)$ computation per iteration, where $S$ (often 50–200) denotes the number of samples, since each sample requires both projection and differentiation. They also require storing and backpropagating through all sample paths, incurring $O(S,n^2)$ memory. Avoiding this multiplicative sampling factor is exactly why DPPL training is kept sampling-free. We further parallelize Jacobian computation using vectorized maps. Algorithms such as Jacobian-free Newton–Krylov methods [1], which rely only on Jacobian-vector products, could further reduce compute and memory costs; we leave this f

### Author's Response (3/3)
### NLL Clarifications

We agree with the reviewer that the NLL is a strictly proper scoring rule, and have rephrased that sentence in the revised version. To clarify, we purposely propose to use the CRPS since it has some better properties, e.g., it is robust to probabilistic model misspecification. This is echoed by **Reviewer 971x**, who states our main motivation that with the CRPS “ProbHardE2E optimizes a strictly proper scoring rule without making any distributional assumptions about the target, allowing it to produce robust distributional estimates. This stands in contrast to existing likelihood-based methods, which are often biased by their distributional assumptions and model choices.” While it is true that CRPS and NLL are proper scoring rules, CRPS has theoretical advantages over NLL under distributional miscalibration [6]. This does not automatically imply superior performance in constrained generative settings. For instance, NLL can still perform well even if the predictive distribution is sharp and well-calibrated, even under hard constraints. 

Therefore, we do not claim that CRPS is universally superior; rather, we empirically validate that CRPS leads to better constraint satisfaction and predictive accuracy in our constrained settings. CRPS has been commonly used in the time series literature [7], and is especially true in scientific ML applications (e.g., PDE forecasting), where the feasibility of individual samples is critical. Our experiments in Table 2 confirm this advantage of the CRPS objective (See our Q3).

### References
[1] Bertsekas, Dimitri P. "Nonlinear programming." Journal of the Operational Research Society 48.3 (1997): 334-334.

[2] Amos, Brandon, and J. Zico Kolter. "Optnet: Differentiable optimization as a layer in neural networks." International conference on machine learning. PMLR, 2017.

[3] Pineda, Luis, et al. "Theseus: A library for differentiable nonlinear optimization." Advances in Neural Information Processing Systems 35 (2022): 3801-3818.

[4] Agrawal, Akshay, et al. "Differentiable convex optimization layers." Advances in neural information processing systems 32 (2019).

[5] LeVeque, Randall J. Finite volume methods for hyperbolic problems. Vol. 31. Cambridge university press, 2002.

[6] Gneiting, Tilmann, and Raftery, Adrian E.. "Strictly proper scoring rules, prediction, and estimation." Journal of the American statistical Association 102.477 (2007): 359-378.

[7] Hyndman, Rob J., and George Athanasopoulos. Forecasting: principles and practice. OTexts, 2018.

### Author's Response Part (2/3)
### Diagonal vs. Low-Rank $Q$ Matrix and Energy-Score Metric
We clarify that our use of a diagonal covariance is a **deliberate and common design choice** in scalable probabilistic modeling frameworks. Notably, prior works, e.g., **ProbConserv**, **Operator-ProbConserv** and **HierE2E** employ diagonal Σ and still achieve strong performance on constrained forecasting and simulation tasks. In our setting, the diagonal assumption allows efficient training and inference in high-dimensional PDE regimes, where full Σ estimation would be prohibitively expensive.

Moreover, we highlight in **Appendix E (Table 6\)** that diagonal Σ can serve as an **implicit regularizer**, which avoids overfitting in data-sparse regimes. We also discuss the practical trade-offs: while full or low-rank covariance may increase expressiveness, it introduces substantial computational and memory overhead, and may not translate into improved constraint satisfaction or UQ in practice. 

We have added an additional experiment in Table B below, which compares training with a diagonal to low-rank $Q$ matrix, where the rank $r=100$. In this experiment, we also report the Energy Score, as suggested, as another metric for multivariate distributions. We see that on some more challenging problems with shocks, e.g., linear advection and Stefan, there are benefits to the low-rank covariance. We plan to further explore structured approximations in future work with low-rank and dense parameterizations, as mentioned in the conclusion section.
### Table B: PDE performance with diagonal vs. low-rank $Q$ matrix.

| Dataset         | Metric       | Diagonal       | Low-rank  |
|-----------------|--------------|----------------|----------------|
| **Heat**        | MSE          | **5.1532e-07**     | 4.6246e-06     |
|                 | Energy Score | **0.0063**         | 0.0180         |
| **PME**         | MSE          | **5.3510e-05**     | 0.0001         |
|                 | Energy Score | **0.1562**         | 0.2123         |
| **Linear Adv.** | MSE          | 0.0020         | **0.0007**         |
|                 | Energy Score | 0.8699         | **0.5367**         |
| **Stefan**      | MSE          | 0.0030         | **0.0019**         |
|                 | Energy Score | 0.5629         | **0.4567**         |


### Feasibility of the Constraints in Nonlinear Optimization
We thank the reviewer for highlighting the challenges associated with non-convexity and active-set behavior. These issues are well known in the nonlinear optimization literature, and our setting inherits the same characteristics. As in classical nonlinear programming, feasibility and convergence depend on local curvature, initialization, and conditioning of the KKT system: properties that also arise in widely used methods such as IPOPT, line-search, and trust-region Newton methods, and other constrained Newton-type solvers [1].
In our implementation, DPPL calls a standard constrained optimizer inside the forward pass. T

### Author's Response Part (1/3)
We thank the reviewer for the detailed and insightful evaluation. We appreciate the recognition of our method as a principled “predictor–corrector” framework, the acknowledgment of our “exact handling for linear constraints,” and the appreciation of our “closed-form, sampling-free training objective.” We are also grateful that the reviewer highlighted the clarity of our formulation and the generality of DPPL across linear, nonlinear, and convex constraints. We address the reviewer’s questions and concerns point-by-point below.

### Linearization of KKT Conditions

Yes, our method uses a linearization of the KKT conditions, similar to approaches in nonlinear optimization, e.g., Sequential Quadratic Programming (SQP) and Gauss-Newton [1]. We understand the concern of first-order approximation of the Jacobian and the estimation errors, and that they are only locally accurate. We emphasize that our method does not rely solely on linearization. The delta method is used **only during training**, where it provides closed-form gradients for location-scale families  and avoid sampling variance, which enables stable optimization and **significant speedups** (**3–5×** faster for linear constraints, as shown in Figure 1a). At inference, we do not linearize but instead solve a constrained optimization problem for each sample via a Newton solver, enforcing hard constraints in their exact (nonlinear) form, which is **crucial in strongly nonlinear regimes**.  Our use of the delta method is a deliberate model design decision that balances training speed with accuracy. 

To appease these concerns, we have added additional experiments in Table A below on PME with $m \in [2,3]$ that directly project the samples and avoid our linear approximation with the delta method during training. We see that ProbHardE2E is approximately **9-45x** faster for approximately the same accuracy. We see that while the accuracy of the sampling approach does increase with more samples $S$, the runtime increases linearly with $S$, and it is already significantly higher than that for our ProbHardE2E. This trade-off between computational efficiency and approximation accuracy is particularly important in high-dimensional spatio-temporal scientific ML problems, where training time is a bottleneck. 

### Table A: Performance comparison on the PME with nonlinear conservation law constraint for ProbHardE2E versus sampling-based baselines with 10 and 50 samples.

| PME m ∈ [2,3] | Metric | ProbHardE2E | Sampling-10 | Sampling-50 |
|---------------|--------|-------------|-------------|-------------|
|               | MSE    | **5.04E-06**    | 1.35E-02    | 2.93E-05    |
|               | CE     | 0           | 0           | 0           |
|               | CRPS   | **8.648E-04**   | 5.01E-02    | 2.03E-03    |
|               | Time   | **1.54 s**      | 14.17 s     | 70.65 s     |

In terms of theoretical guarantees, Theorem 3.1, whose proof is in Appendix F, shows that the approximation error be

### Author's Response Part (2/2)
### Closed-form CRPS

We thank the reviewer for acknowledging that the CRPS training loss can be generalized to a broad class of probabilistic models. Among continuous distributions, we experimented with Gaussian variables, which have closed-form CRPS.  We show in our experimental results on PDEs and time series that even when the underlying probabilistic distribution is unknown, our ProbHardE2E performs well and the Gaussian assumption is robust. Beyond tractable univariate distributions, as the reviewer pointed out, sample-based projection is agnostic to distributional form.  Thus, the framework can be extended to skewed, bounded, or heavy-tailed distributions using, e.g., normalizing flows or rejection sampling, albeit at additional computational cost during training. This represents an exciting direction of future work, where we can incorporate sampling or other distributions into our framework.


### Experimental Results Performance

We did not intend to overclaim and have clarified the following points in the revised version:

- We clarify in the revised version that we consistently outperform in our target metric of CRPS, which is the preferred metric for probabilistic forecasts [3] . Note our approach is not guaranteed to improve MSE and we are targeting the uncertainty quantification metrics. For the PDE datasets, we clarify that all existing baselines in their original papers were trained with NLL, including ProbConserv [4]. To make it comparable in our ablations and test the effect of CRPS vs. NLL in Q3, we also train it with CRPS, as described in Evaluation Paragraph of Section 4 (lines 331-333).  We see that these other methods have improved performance when trained using CRPS, but they are trained using NLL in their original form.
- We use Table 3 to discuss the computational efficiencies in Q4, and do not use Table 3 to address the CRPS vs. NLL ablation in Q3, which is conducted in Table 2. We also do not perform this ablation in Table 3, primarily because it is well-established in the hierarchical time series community [6] that CRPS is an effective training loss (e.g., from HierE2E). We do not claim accuracy improvement over HierE2E (See Appendix D.1 for its connection to our method). In particular, we show that we can improve the computational performance of HierE2E by projecting directly on the parameter distributions rather than projecting on the samples, as done in HierE2E, during training, and in the linear constraint case, an exact closed form solution exists. This leads to the  **3-5x** improvement in training time in Figure 1a. 
- We have clarified in the revised version that these specific performance numbers are upper bounds and occur when $m \in [2,3]$. We still see improved performance compared to the baselines for the other powers of $m$.
- We clarify the results in Figure 1b-1c.  In Figure 1b, our ProbHardE2E (shown in purple) is directly on top of the exact solution, and the variance is so small that it is difficult

### Author's Response Part (1/2)
We thank the reviewer for their thoughtful evaluation and for highlighting the core strengths of our work. We appreciate the recognition that “the main novelty of this paper is to propose an end-to-end enforcement of hard constraints” and that our approach “enables joint UQ and constraint satisfaction.” We are also grateful for the reviewer’s comments on the “substantial training speedups” from sampling-free CRPS and analytic projections, as well as the “generality” of our framework across linear, nonlinear, and convex constraints. Below, we will try address the your concerns.


### Linearization of KKT Conditions

Yes, our method uses a linearization of the KKT conditions, similar to approaches in nonlinear optimization, e.g., Sequential Quadratic Programming (SQP) and Gauss-Newton [1]. We understand the concern of first-order approximation of the Jacobian and the estimation errors, and that they are only locally accurate. We emphasize that our method does not rely solely on linearization. The delta method is used **only during training**, where it provides closed-form gradients for location-scale families  and avoid sampling variance, which enables stable optimization and **significant speedups** (**3–5×** faster for linear constraints, as shown in Figure 1a). At inference, we do not linearize but instead solve a constrained optimization problem for each sample via a Newton solver, enforcing hard constraints in their exact (nonlinear) form, which is **crucial in strongly nonlinear regimes**.  Our use of the delta method is a deliberate model design decision that balances training speed with accuracy. 

To appease these concerns, we have added additional experiments in Table A below on PME with $m \in [2,3]$ that directly project the samples and avoid our linear approximation with the delta method during training. We see that ProbHardE2E is approximately **9-45x** faster for approximately the same accuracy. We see that while the accuracy of the sampling approach does increase with more samples $S$, the runtime increases linearly with $S$, and it is already significantly higher than that for our ProbHardE2E. This trade-off between computational efficiency and approximation accuracy is particularly important in high-dimensional spatio-temporal scientific ML problems, where training time is a bottleneck. 

### Table A: Performance comparison on the PME with nonlinear conservation law constraint versus sampling-based baselines with 10 and 50 samples.

| PME m ∈ [2,3] | Metric | ProbHardE2E | Sampling-10 | Sampling-50 |
|---------------|--------|-------------|-------------|-------------|
|               | MSE    | **5.04E-06**    | 1.35E-02    | 2.93E-05    |
|               | CE     | 0           | 0           | 0           |
|               | CRPS   | **8.648E-04**   | 5.01E-02    | 2.03E-03    |
|               | Time   | **1.54 s**      | 14.17 s     | 70.65 s     |

In terms of theoretical guarantees, Theorem 3.1, whose proof is in Appendix F, s

### Summary
We appreciate the reviewers’ valuable feedback to help improve the clarity of our manuscript. We are glad that the reviewers found our work an important and novel contribution to the field and all voted for acceptance. To summarize:
 - **Reviewer LXk5** highlights the “novelty” of our “end-to-end enforcement of hard constraints”, and “generality” of the various constraint types supported by our framework.
 - **Reviewer 8rdZ** acknowledges that our “method is clearly formulated in a principled “predictor–corrector” view.”
- **Reviewer 971x** highlights that our work “​​introduces a novel differentiable probabilistic projection layer (DPPL) that can be integrated with a wide range of neural network architectures” and that our “proposed method demonstrates strong empirical performance.”
- **Reviewer MxEb** states that our work “is a well-written and valuable paper with a clear contribution, sound theoretical derivations, and strong empirical validation.”
We address the reviewers’ comments below, and have also updated the manuscript with the changes highlighted in red in the rebuttal version.

### End-to-End Probabilistic Framework for Learning with Hard Constraints


## Meta review / decision
### Paper Decision
Accept (Poster)

## PDF extracted text (first pages)
```text
Published as a conference paper at ICLR 2026
END-TO-E ND PROBABILISTIC FRAMEWORK FOR
LEARNING WITH HARD CONSTRAINTS
Utkarsh∗
MIT CSAIL
utkarsh5@mit.edu
Danielle C. Maddix †
AWS
dmmaddix@amazon.com
Ruijun Ma
Amazon SCOT
ruijunma@amazon.com
Michael W. Mahoney
Amazon SCOT
zmahmich@amazon.com
Yuyang Wang
AWS
yuyawang@amazon.com
ABSTRACT
We present ProbHardE2E, a probabilistic forecasting framework that incorpo-
rates hard operational/physical constraints, and provides uncertainty quantification.
Our methodology uses a novel differentiable probabilistic projection layer (DPPL)
that can be combined with a wide range of neural network architectures. DPPL
allows the model to learn the system in an end-to-end manner, compared to other
approaches where constraints are satisfied either through a post-processing step or
at inference. ProbHardE2E optimizes a strictly proper scoring rule, without mak-
ing any distributional assumptions on the target, which enables it to obtain robust
distributional estimates (in contrast to existing approaches that generally optimize
likelihood-based objectives, which can be biased by their distributional assump-
tions and model choices); and it can incorporate a range of non-linear constraints
(increasing the power of modeling and flexibility). We apply ProbHardE2E
in learning partial differential equations with uncertainty estimates and to prob-
abilistic time-series forecasting, showcasing it as a broadly applicable general
framework that connects these seemingly disparate domains. Our code is available
at https://github.com/amazon-science/probharde2e.
1 I NTRODUCTION
Recently, machine learning (ML) models have been applied to a variety of engineering and scientific
tasks, including probabilistic time series forecasting (Rangapuram et al., 2021; Hyndman et al.,
2011; Taieb et al., 2017; Olivares et al., 2024b) and scientific applications (Krishnapriyan et al.,
2021; Hansen et al., 2023; N ´egiar et al., 2023; Mouli et al., 2024). Exact enforcement of hard
constraints can be essential in domains where any violation of operational or physical requirements
(e.g., coherency in hierarchical forecasting, conservation laws in physics, and non-negativity in
economics and robotics) is unacceptable (Gould et al., 2022; Hansen et al., 2023; Donti et al., 2021).
Limitations of data-driven ML approaches arise in various disciplines where constraints need to
be satisfied exactly (Rangapuram et al., 2021; Hansen et al., 2023). Within ML, constraints are
typically incorporated as soft penalties, e.g., with a regularization term added to the loss function
(Raissi et al., 2019; Li et al., 2024); but they are sometimes incorporated via post-training correction
mechanisms, e.g., to enforce a hard constraint (Hansen et al., 2023; Mouli et al., 2024; Cheng et al.,
2025). Some methods have managed to enforce hard constraints “end-to-end” in a general framework
as a differentiable solver (N´egiar et al., 2023; Chalapathi et al., 2024; Rackauckas et al., 2020), as a
differentiable optimization layer (Amos & Kolter, 2017; Agrawal et al., 2019; Min et al., 2024), or as
an auxiliary procedure (Donti et al., 2021).
The aforementioned hard-constrained models typically provide point estimates without uncertainty
quantification (UQ), limiting their use cases in operational and physical domains requiring probabilis-
tic forecasts. Generating output distribution statistics under hard constraints is often computationally
∗Work done during internship at AWS.
†Correspondence to: Danielle C. Maddix <dmmaddix@amazon.com>.
1
Published as a conference paper at ICLR 2026
expensive or yields only approximate solutions (Robert et al., 1999; Szechtman & Glynn, 2001;
Girolami & Calderhead, 2011). There have been domain-specific works in hierarchical probabilistic
time series forecasting, which enforce coherency constraints using end-to-end deep learning models
(Olivares et al., 2024b; Rangapuram et al., 2021). However, these works either apply only to linear
constraints, or they require a computationally expensive sampling procedure in training. Similar
approaches have been proposed for computing probabilistic solutions to partial differential equations
(PDEs) that satisfy constraints (Hansen et al., 2023; Mouli et al., 2024; Cheng et al., 2025; Gao
et al., 2023; Utkarsh et al., 2025). In these works, however, the constraints are only applied as a
post-processing step, and they do not lead to an end-to-end solution (of interest in the common
situation that one wants to incorporate a hard-constrained model within a larger model, and then
optimize the larger model) that optimizes the evaluation accuracy. In both the forecasting and PDE
application domains, none of this prior UQ work can handle complex nonlinear (hard) constraints.
In this work, we propose a novel probabilistic framework, ProbHardE2E, that integrates a broad
class of hard constraints (including non-linear constraints) in an end-to-end fashion, while incorporat-
ing UQ. By leveraging key results from statistics and optimization in a novel way, we predict both the
mean and covariance of the output data, moving beyond point estimate predictions. ProbHardE2E
enforces nonlinear constraints with an efficient sampling-free method to generate distribution statis-
tics. Our probabilistic approach enables the effective handling of exogenous spikes and jumps (or
other discontinuities) by leveraging data heteroscedasticity, enhancing the model’s robustness and
flexibility under varying data conditions.
We summarize our key contributions as follows.
• We introduce ProbHardE2E, as a general framework to learn a function in an end-to-
end manner by optimizing an objective under hard constraints. The framework enables
UQ by learning parameters of a multivariate probabilistic distribution. We show that
ProbHardE2E can incorporate a broad class of deep learning backbone models.
• The key technical novelty of ProbHardE2E is a differentiable probabilistic projection
layer (DPPL) that extends standard projection methods to accommodate UQ while enforcing
hard constraints. ProbHardE2E can handle constraints ranging from linear equality to
general nonlinear equality to convex inequality constraints.
• We use the DPPL to impose constraints directly on the marginals of the multivariate distri-
bution for an efficient sampling-free approach for posterior distribution estimation, which
reduces the computational overhead by up to 3–5× during training.
• We show that ProbHardE2E is effective in two (seemingly-unrelated, but technically-
related) tasks, where hard constraints are important: probabilistic time series forecasting; and
solving challenging PDEs in scientific machine learning (SciML). We provide an extensive
empirical analysis demonstrating that ProbHardE2E results in up to 15× lower mean-
squared error (MSE) in mean forecast and 2.5× improved uncertainty estimates, measured
by the Continuous Ranked Probability Score (CRPS), compared to the baseline methods.
• We show that training with the continuous-ranked probability score (CRPS), rather than
negative log-likelihood (NLL) leads to better predictive performance. While the need for
this is well-known in, e.g., time series forecasting, previous PDE learning works commonly
use NLL-based metrics for UQ.
2 R ELATED WORK
There is a large body of related work from various communities, ranging from imposing constraints on
neural networks for point estimates (Min et al., 2024; Donti et al., 2021), to probabilistic time series
forecasting with constraints (Rangapuram et al., 2021; 2023; Olivares et al., 2024b), to imposing
constraints on deep learning solutions to PDEs (N´egiar et al., 2023; Hansen et al., 2023). Table 5 in
Appendix A summarizes some advantages and disadvantages of these methods that are motivated by
enforcing hard constraints in these domains. (See Appendix A for additional details.)
3 PR O BHA R DE2E: A U NIFIED PROBABILISTIC OPTIMIZATION FRAMEWORK
In this section, we introduce ProbHardE2E. See Algorithm 1 for a summary. (See also Appendix B
for a universal approximation guarantee.) In Section 3.1, we discuss the proper evaluation metric
2
Published as a conference paper at ICLR 2026
Algorithm 1 ProbHardE2E: Training and Inference
Require: Training data {(ϕ(i), u(i))} ∼ D , test data ϕ and constraints g(·) ≤ 0, h(·) = 0.
Ensure: Learnable function ˆfθ : Φ → Y that outputs constrained distribution parameters.
1: Pick a model classΘ, initialize weights θ ∈ Θ for probabilistic unconstrained model fθ : Φ → Z .
2: while θ not converged do
3: Predict unconstrained distribution parameters (µθ(ϕ(i)), Σθ(ϕ(i))).
4: Training Mode: Project parameters (ˆµθ(ϕ(i)), ˆΣθ(ϕ(i))) = DPPL((µθ(·), Σθ(·)), g(·), h(·)).
5: Update θ ∈ ¯Θ by minimizing the CRPS loss ℓ(Yθ(ϕ(i)), u(i)).
6: end while
7: Inference Mode: Project random variable Yθ(ϕ) = DPPL(Zθ(ϕ), g(·), h(·)), where Zθ(ϕ) and
Yθ(ϕ) denote the unconstrained and unconstrained random variables, respectively.
8: Return Feasible predicted sample u∗(zθ(ϕ)) ∼ Yθ(ϕ), where zθ(ϕ) ∼ Zθ(ϕ).
for a constrained probabilistic learner, and we define our objective function that corresponds to that
evaluation metric. In Section 3.2, we propose our differentiable probabilistic projection layer (DPPL)
that enforces the hard constraints. In Section 3.3, we describe how to compute the parameters of the
resulting constrained posterior distribution. In Section 3.4, we discuss update rules for various types
of constraints (linear equality, nonlinear equality, and convex inequality constraints). In Section 3.5,
we propose a sample-free formulation for satisfying the constraints while optimizing for the objective.
3.1 P ROBABILISTIC EVALUATION METRICS AND OBJECTIVE FUNCTION
We formulate the problem of probabilistic learning under constraints. The goal of this problem is
to learn a function ˆfθ : Φ → Y , where Φ ⊂ Rm denotes the input space, θ ∈ ¯Θ ⊆ Θ denotes the
feasible parameter space, and Y ⊂ Rk denotes the space of predicted distribution parameters that meet
the constraints. Given a multivariate distribution class, these learned parameters induce a predictive
multivariate random variable Yθ(ϕ(i)), where (ϕ(i), u(i)) ∼ D , where ϕ(i) ∈ Φ, u(i) ∈ Rn, and
D denotes training data from a distribution D. Each realization of ˆu(ϕ(i)) ∼ Yθ(ϕ(i)) ∈ Rn is
required to satisfy predefined hard constraints of the form g(ˆu(ϕ(i))) ≤ 0 and h(ˆu(ϕ(i))) = 0. We
can formulate this constrained optimization problem as follows:
arg min
θ∈Θ, g (Yθ(ϕ(i)))≤0, h (Yθ(ϕ(i)))=0
E(ϕ(i),u(i))∼D ℓ
 
Yθ(ϕ(i)), u(i)
, (1)
where denotes a proper scoring rule.
One widely-used (strictly) proper scoring rule for continuous distributions is the continuous ranked
probability score (CRPS) (Gneiting & Raftery, 2007). The CRPS simultaneously evaluates sharpness
(how concentrated or “narrow” the distribution is) and calibration (how well the distributional
coverage “aligns” with actual observations). More formally, for an observed scalar outcomey and a
corresponding probabilistic distributional estimate, Y , the CRPS is defined as:
CRPS(Y, y) = EY |Y − y| − 1
2 EY |Y − Y ′|, (2)
where Y ′ denotes an i.i.d. copy of Y . Compared to other scoring rules, e.g., the log probability scoring
rules, which require assumptions on the outcome variable, the CRPS is robust to probabilistic model
mis-specification. Because of this unique property, the CRPS is widely used as the evaluation metric
in many applications, e.g., probabilistic time series forecasting (Gasthaus et al., 2019; Rangapuram
et al., 2021; Park et al., 2022; Olivares et al., 2024b), quantile regression (Fakoor et al., 2023),
precipitation nowcasting (Ravuri et al., 2021; Gao et al., 2023) and weather forecasting (Rasp &
Lerch, 2018; Kochkov et al., 2024; Price et al., 2025).
We align our training objective with the proposed evaluation metric above, by directly optimizing the
CRPS in Eq. (2) in Problem 1. We define the loss as the sum of the univariate CRPS:
ℓ
 
Yθ(ϕ(i)), u(i)
=
nX
j=1
CRPS((Yθ(ϕ(i)))j, u(i)
j ). (3)
3
Published as a conference paper at ICLR 2026
The CRPS naturally aligns with the goal of producing feasible and well-calibrated predictions, as
the metric rewards distributions that closely match observed outcomes. Enforcing our constraints in
the distribution space guarantees that every sample from the predicted distribution is physically or
operationally valid. Consequently, modeling the loss through the CRPS provides a principled way to
reconcile domain constraints with distributional accuracy.
3.2 D IFFERENTIABLE PROBABILISTIC PROJECTION LAYER (DPPL)
We transform the constrained Problem 1 into the unconstrained optimization problem:
arg min
θ∈¯Θ
E(ϕ(i),u(i))∼D ℓ
 
Yθ(ϕ(i)), u(i)
, (4)
where ¯Θ ⊆ Θ denotes the feasible parameter space that ensures constraint satisfaction, and ℓ denotes
the loss function in Eq. (3). We solve this using a two-step procedure: first define a predictive output
distribution, then project it onto the constraint manifold using a differentiable probabilistic projection
layer (DPPL) for end-to-end optimization.
Our framework begins with an established probabilistic backbone model. This can be a Gaussian
Process (Rasmussen & Williams, 2006), neural process (Kim et al., 2019), DeepV AR (Salinas et al.,
2019; Rangapuram et al., 2021), or ensembles of neural networks or operators (Mouli et al., 2024).
The base model fθ : Φ → Rk predicts the distribution parameters (mean µθ(ϕ(i)) and covariance
Σθ(ϕ(i)), for θ ∈ Θ) – without constraint awareness. We then use a reparameterization function
r : Rk × Rn → Rl to define the distribution in one of two ways: either as an identity map, where
l = k, that returns fθ(ϕ(i)) =
 
µθ(ϕ(i)), Σθ(ϕ(i))

for our efficient sample-free paradigm during
training; or as a map, where l = n, that combines the distribution parameters with noise ξ ∼ p(ξ)
∈ Rn, where p denotes a tractable sampling distribution, and gives a sample zθ(ϕ(i)) ∼ Zθ(ϕ(i))
∈ Rn from the predicted distribution to generate constrained samples at inference. This dual-mode
design balances training efficiency with strict constraint feasibility at inference.
The reparameterization function induces the base (unconstrained) distribution parameters or predictive
random variable as:
r(fθ(ϕ(i)), ξ) =
 
µθ(ϕ(i)), Σθ(ϕ(i))

, (Training)
Zθ(ϕ(i)), (Inference) (5)
Following this Predictor Step above, we use the DPPL in the Corrector Step to restrict the parameter
space to ¯Θ ⊆ Θ, such that for all ˆuθ(ϕ(i)) ∼ Yθ(ϕ(i)), the constraints g(ˆuθ(ϕ(i))) ≤ 0 and
h(ˆuθ(ϕ(i))) = 0 are satisfied. The DPPL is our core architecture innovation for leveraging the base
model to learn predictions that satisfy the given constraints. We define the projected distribution
parameters or projected predictive random variable as:
DPPL(r(fθ(ϕ(i)), ξ), g(·), h(·)) = r( ˆfθ(ϕ(i)), ξ) =
 
ˆµθ(ϕ(i)), ˆΣθ(ϕ(i))

, (Training)
Yθ(ϕ(i)), (Inference) (6)
for r(fθ(ϕ(i)), ξ) in Eq. (5), where ˆfθ : Φ → Y ⊂ Rk denotes the probabilistic model that outputs
the constrained distribution parameters (ˆµθ(ϕ(i)), ˆΣθ(ϕ(i))). Our DPPL yields a constraint-satisfying
realization u∗ ∼ Yθ(ϕ(i)) as the final predictive random variable.
This two-step approach mirrors predictor-corrector methods (Boyd & Vandenberghe, 2004; Bertsekas,
1997), with the DPPL serving as our key architectural innovation for ensuring constraint satisfaction.
Equivalently, the DPPL can be formulated as a constrained least squares problem on the samples of
Zθ(ϕ(i)). (See Appendix C for details.) Prior works on imposing hard constraints in time series and
solving PDEs (Rangapuram et al., 2021; Hansen et al., 2023) reduce to special cases of our method
with linear constraints. (See Appendix D for details.) We draw zθ(ϕ(i)) ∼ Zθ(ϕ(i)), and we solve
the following constrained optimization problem:
u∗(zθ(ϕ(i))) := arg min
ˆuθ(ϕ(i))∈Rn,g(ˆuθ(ϕ(i)))≤0,h(ˆuθ(ϕ(i)))=0
∥ˆuθ(ϕ(i)) − zθ(ϕ(i))∥2
Q, (7)
where u∗(zθ(ϕ(i))) denotes a predicted sample of Yθ(ϕ(i)), and where ∥x∥Q =
p
x⊤Qx for some
symmetric positive semi-definite matrix Q. (See Appendix E for details on the flexibility of learning
various forms of Q.)
4
Published as a conference paper at ICLR 2026
3.3 DPPL ON THE DISTRIBUTION PARAMETERS FOR LOCATION -SCALE DISTRIBUTIONS
In this subsection, we detail how to directly compute the parameters for the constrained distribution by
applying our DPPL on the base distribution parameters for an efficient, sampling-free during training.
To do so, we can assume that the prior distribution F belongs to a multivariate, location-scale family,
i.e., a distribution such that any affine transformation Y of a random variable Z = µ + Σ1/2ξ ∼
F(µ, Σ) and ξ ∼ F (0, 1), remains within the same distribution family F. This is an example of how
to compute the random variable in Eq. (5) for a multivariate location-scale distribution. A familiar
case of this is when Z ∼ N (µ, Σ) and Y = AZ + B is an affine transformation; in which case
Y ∼ N (Aµ + B, AΣA⊤). Alternatively, we can show that when Y is a nonlinear transformation
of Z, it has approximately (to first-order) the same distribution Z, with an appropriately-chosen set
of parameters (given in Eq. (8) below). We state this result more formally in Theorem 3.1. The
proof, given in Appendix F, uses a first-order Taylor expansion to linearize the nonlinear function
transformation, and is similar to the Multivariate Delta Method (Casella & Berger, 2001).
Theorem 3.1. Let Z ∼ F (µ, Σ) be a random variable, where the underlying distribution F belongs
to a multivariate location-scale family of distributions, with mean µ and covariance Σ; and let
T be a function with continuous first derivatives, such that JT (µ)ΣJT (µ)⊤ is symmetric positive
semi-definite. Then, the transformed distribution Y = T (Z) converges in distribution with first-
order accuracy to F(ˆµ, ˆΣ) with mean ˆµ = T (µ) and covariance ˆΣ = JT (µ)ΣJT (µ)⊤, where
JT (µ) = ∇T (µ)⊤ denotes the Jacobian of T with respect to z evaluated at µ.
Let Z ∼ F (µ, Σ) denote the prior distribution andz ∼ Z. We apply Theorem 3.1 withT (z) = u∗(z),
where u∗(z) denotes the solution of the constrained least squares problem in Problem (7). In this
case, the projected random variable satisfies Y ∼ F (ˆµ, ˆΣ) with updated parameters:
ˆµ = T (µ), ˆΣ = JT (µ) ΣJT (µ)⊤. (8)
3.4 DPPL FOR VARIOUS CONSTRAINT TYPES
In this subsection, we discuss how to compute the DPPL for various constraint types (linear equality,
nonlinear equality, and convex inequality) for both train and inference modes. Table 1 shows these
constraints types require different treatments: linear equality have closed-form projections, nonlinear
equality can be solved with iterative methods, and convex inequality require optimization solvers.
Table 1: Summary of DPPL in ProbHardE2E for various constraint types. For linear equality
constraints, the oblique projection PQ−1 = I − Q−1A⊤(AQ−1A⊤)−1A; for nonlinear equality
constraints, R denotes the first-order optimality conditions.
Constraint Type Solution u∗(z) Solver Type Jacobian JT
Linear Equality PQ−1 z + (I − PQ−1)A†b closed-form PQ−1
Nonlinear Equality (u∗, λ∗) s.t. R(u∗, λ∗; z) = 0 nonlinear implicit differentiation
Convex Inequality argmin
h(ˆu)=0, g(ˆu)≤0
∥ˆu − z∥2
Q convex opt. sensitivity analysis;
argmin differentiation
3.4.1 L INEAR EQUALITY CONSTRAINTS
For linear equality constraints, we have an underdetermined linear systemh(ˆu) = Aˆu − b = 0, where
A ∈ Rq×n, q < n , and has full row rank q. In this case, we can derive a closed-form solution to the
constrained least squares Problem (7). In this case, both training and inference modes are equivalent
since the DPPL projection is exact. (See Appendix C.1.)
3.4.2 N ONLINEAR EQUALITY CONSTRAINTS
For nonlinear equality constraints, h(ˆu) = 0, we can no longer derive the exact closed-form expres-
sion for the solution. Instead, we can provide an expression which is satisfied by the optimal solution.
In particular, we approximate 
```
