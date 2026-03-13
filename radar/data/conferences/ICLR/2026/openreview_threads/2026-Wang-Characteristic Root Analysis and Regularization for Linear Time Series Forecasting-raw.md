# Characteristic Root Analysis and Regularization for Linear Time Series Forecasting — OpenReview Raw Thread

- Forum: https://openreview.net/forum?id=JTtwGRACte
- PDF: https://openreview.net/pdf?id=JTtwGRACte
- Section: 二、时间序列预测：分布鲁棒、多变量建模与后处理优化
- Zhihu score: 6.0
- Venue status: ICLR 2026 Poster

## Submission metadata
- Authors: Zheng Wang, Kaixuan Zhang, Wanfang Chen, Xiaonan Lu, Longyuan Li, Tobias Schlagenhauf
- Primary area: learning on time series and dynamical systems
- Keywords: long term time series forecasting, linear model, characteristic roots, modes, noise robustness, rank reduction, root purge

## Abstract
Time series forecasting remains a critical challenge across numerous domains, yet the effectiveness of complex models often varies unpredictably across datasets. Recent studies highlight the surprising competitiveness of simple linear models,  suggesting that their robustness and interpretability warrant deeper theoretical investigation. This paper presents a systematic study of linear models for time series forecasting, with a focus on the role of characteristic roots in temporal dynamics. We begin by analyzing the noise-free setting, where we show that characteristic roots govern long-term behavior and explain how design choices such as instance normalization and channel independence affect model capabilities. We then extend our analysis to the noisy regime, revealing that models tend to produce spurious roots. This leads to the identification of a key data-scaling property: mitigating the influence of noise requires disproportionately large training data, highlighting the need for structural regularization. To address these challenges, we propose two complementary strategies for robust root restructuring. The first uses rank reduction techniques, including Reduced-Rank Regression (RRR) and Direct Weight Rank Reduction (DWRR), to recover the low-dimensional latent dynamics. The second, a novel adaptive method called Root Purge, encourages the model to learn a noise-suppressing null space during training. Extensive experiments on standard benchmarks demonstrate the effectiveness of both approaches, validating our theoretical insights and achieving state-of-the-art results in several settings. Our findings underscore the potential of integrating classical theories for linear systems with modern learning techniques to build robust, interpretable, and data-efficient forecasting models. The code is publicly available at: https://github.com/Wangzzzzzzzz/RootPurge.

## Reviews
### Reviewer_xcu7
- summary: This paper analyzes linear time series forecasting via characteristic roots , identifying that noise creates "spurious roots" and a "data scaling law" that demands excessive data to mitigate this noise. To improve robustness and data efficiency, it proposes two structural regularization strategies: (1) post-hoc Rank Reduction (RRR) and (2) a novel "Root Purge" method. Root Purge is an adaptive training regularizer that encourages the model to learn a null space for the estimated noise (residuals).
- strengths: 1.Originality and Clarity: The "Root Purge" loss function is a novel, elegant, and intuitive regularization technique.

2.Quality and Significance: The paper provides a valuable insight into why simple linear models fail in noisy, low-data regimes.
- weaknesses: 1.Hyperparameter Sensitivity: The methods' performance relies heavily on tuning $\rho$ or $\lambda$. This data-specific tuning is difficult to estimate a priori and undermines the claim of robustness.

2.Contingent on Low-Rank Assumption: The methods are motivated by an assumption that the true signal is low-rank. However, on large, complex datasets, the paper's results show the optimal rank is often full , and the proposed methods offer minimal benefit . This limits the methods' generality.

3.Theory-Practice Gap (Trends): The theoretical analysis assumes homogeneous equations (constant/zero bias) . This is a poor fit for real-world data with non-stationary, dynamic trends.
- questions: 1. Does the Low-Rank Assumption limit the generality of method, making it effective only for a specific subset of (simpler) time series datasets? 

2.If we encounter a complex trend in the future that Instance Normalization can't flatten, does your Root Purge method just fail? How can you convince us that it's still robust in that scenario?
- rating: 4 | confidence: 4

### Reviewer_G42f
- summary: This work presents a comprehensive study of linear models for time series forecasting, focusing on the role of characteristic roots in shaping model expressivity. Experiments validate our theoretical claims and demonstrate the effectiveness of both methods across a range of forecasting tasks.
- strengths: 1. The research motivation of this manuscript is clear and its content is very rich。

2. This manuscript is theoretical.

3. Sufficient experiments have verified the effectiveness of the proposed method.
- weaknesses: 1. Theoretical analysis is an advantage of this work, but it can easily make it difficult for readers to understand. It is necessary to provide intuitive explanations in the key derivation process

2. The manuscript lacks a comprehensive discussion of related work, which hampers readers, particularly those less familiar with the domain. Thus, it remains unclear how the proposed approach advances the state of the art or distinguishes itself from existing methods.
- questions: 1. What is the transferability of the method?Can linear models be used in other areas than time series learning?

2. Why is the frequency-domain linear layer necessary for Root-Purge instead of a mere implementation detail?
- rating: 8 | confidence: 2

### Reviewer_zgN9
- summary: This paper advances a linear time-series forecasting framework centered on characteristic roots: in the noise-free regime, it shows that characteristic roots govern long-term dynamics; in noisy settings, it exposes the MSE training data-scaling law and the risk of spurious roots, indicating that simply enlarging the sample size is insufficient for robust generalization. Accordingly, the authors introduce two complementary structural regularization strategies: (i) low-rank constraints on the parameter matrix via Reduced-Rank Regression (RRR) and Direct Weight Rank Reduction (DWRR) to recover lo
- strengths: 1. According to the reported results, the proposed methods achieve strong empirical performance across multiple datasets, which is particularly notable given the simplicity of the designs.  

2. The paper provides substantial theoretical analysis with clear exposition to clarify the core concepts.  

3. A clear roadmap is presented, and overall readability is high.
- weaknesses: 1. The core insight “preserving dominant characteristic roots to suppress noise” is not novel and aligns with fundamental conclusions from classical Singular Spectrum Analysis (SSA).  

2. The technical contributions of DWRR and Root Purge appear simple.  

3. The Root Purge objective may induce model degeneration: the model could prefer mapping any input to zero, and the paper offers no theoretical guarantees to prevent or mitigate this failure mode.  

4. The theoretical analysis depends on i.i.d. Gaussian noise and stationarity assumptions to justify data efficiency and the regularizer; these assumptions often do not hold in practice, and no generalization beyond them is provided.
- questions: 1. Under complex, non-stationary noise typical of real-world series, do the proposed methods retain theoretical advantages?  

2. Can the approach be extended to more complex deep learning architectures?
- rating: 6 | confidence: 4

## Author comments / rebuttal
### Summary of Rebuttal to AC
Dear AC,

Thank you for handling the reviews and taking the time to read our rebuttal. To help streamline your assessment, we provide below a concise summary of each reviewer’s comments, our responses, and the key outcomes from our discussions.


## Reviewer xcu7

| Concerns | Our Responses/Arguments |
| :- | :- |
| W1: Hyperparameter Sensitivity | Each method (RRR, DWRR, Root Purge) uses only one hyperparameter. RRR/DWRR tuning is post-training and computationally inexpensive. Root Purge sensitivity is empirically validated (Figure 2). |
| W2/Q1: Low Rank Assumption & Generality | Experiment logs show the optimal rank is rarely full. Low-rank is a flexible modeling device whose meaning depends on model capacity (e.g., INC or longer lookback → effectively higher attainable rank). Lots of prior works confirm the generality of low rank modeling and our strong empirical results show robustness of our methods on complex datasets. |
| W3: Focus on only homogeneous difference equations | Many non-homogeneous equations can be rewritten as higher-order homogeneous ones. By the Stone–Weierstrass theorem, homogeneous linear recurrences universally approximate dynamics, consistent with the strong performance of linear forecasting models in practice. |
| Q2: IN fail to flatten trend → Root Purge failure? | IN does not remove trends; it enforces a fixed unit root. Root Purge operates on modifiable roots only and is independent of IN. Empirically, it also performs well on real-world data with complex trends. |

__Discusion:__ We did not receive any feedback about our response before the rating was reverted.

---

## Reviewer G42f

| Concerns | Our Responses/Arguments |
| :- | :- |
| W1: Add Intuitive Explanation of Theories. | Added a mind map (Fig. 5), a theory summary table (Table 4), and a content table to improve conceptual flow and accessibility. |
| W2: Insufficient Related Work | Clarified that an expanded related-work discussion appears in Appendix B.1 and added a direct pointer in the main text for seamless navigation. |
| Q1: Transferability; use of linear models beyond time series | Highlighted that linear models underpin regression, PCA, LoRA, probing, editing, pruning, and linearized networks. Our method transfers broadly via spectral tools (SVD), adaptive decomposition, and applies to tasks involving null-space discovery, low-rank structure, and operator learning. |
| Q2: Why frequency-domain linear layer? | Clarified that it is optional but improves stability and gradient quality (FITS, FreTS; Table 11). Also demonstrated that a time-domain version works effectively (Appendix E.7); differences likely arise from implicit gradient descent bias rather than architectural necessity. |

__Discusion: Reviewer G42f acknowledged that our clarifications resolved their concerns, and maintained their score.__

---

## Reviewer zgN9

| Concerns | Our Responses/Arguments |
| :- | :- |
| W1: Similar to SSA; novelty unclear | We discuss our novelty from SSA in 

### Author comment
---
Overall Response
---

We thank all reviewers for their valuable feedback and constructive comments, which have significantly improved the clarity and quality of our manuscript. We are encouraged that the reviewers recognized our work as a novel and important contribution to the field. A summary of their key observations is provided below:

* Reviewer **xcu7** described the Root Purge loss as "a novel, elegant, and intuitive regularization technique" and acknowledged that our paper offers "a valuable insight" into the failures of linear time series models in noisy, low-data regimes.

* Reviewer **G42f** highlighted the "clear motivation" and "rich theoretical content" of the manuscript, noting that "sufficient experiments" confirm the method’s effectiveness.

* Reviewer **zgN9** acknowledged the "strong empirical performance" achieved through "simple designs", supported by "substantial theoretical analysis" presented with clarity and high readability.

We have addressed each reviewer’s concerns in detail below their respective reviews. The following updates have been incorporated into the manuscript:

1. We have updated Appendix A.1 to include **a detailed mind-map**, added a **summary table of theorems** (Table 4), and provided a **content table** (page 14) for easier navigation through the paper. These additions are intended to enhance readability and flow, particularly in facilitating a quick understanding of the theoretical insights.

2. We have extended **Proposition 1** (lines 213–215) and **Proposition 6** (Appendix D.3) to **apply to any zero-mean noise with finite second moments**. Since our proofs rely on the law of large numbers, the central limit theorem, and Slutsky’s theorem—all of which are distribution-agnostic—our conclusions hold under these broader conditions.

3. We have **clarified concerns regarding the rank of complex datasets** such as Electricity and Traffic (lines 2910–2915, 2994-3001, 3469–3495) by including numerical analyses from RRR/DWRR experiment logs in the supplementary material. This clarification aims to demonstrate the commonality of low-rank structures and why a default regularization can potentially be beneficial for time series forecasting.

### Author comment
---
Question 2: Can the approach be extended to more complex deep learning architectures?
---

**Response.**

We sincerely appreciate the reviewer's feedback regarding the generalization of our methods on non-linear models. This brings up a broader and thought-provoking direction: how to generalize the idea of rank reduction to nonlinear architectures. Unlike in linear models, where spectral properties offer clear guidance, the definition and utility of "low-rank structure" in deep nonlinear models remain underexplored. Investigating principled ways to impose and leverage low-rank constraints in such models—potentially via architectural design, regularization, or representation learning—is a compelling area for future work, and we have noted it as one of the directions we plan to pursue.

To empirically probe this question, we applied DWRR to Transformer and PatchTST models by inserting DWRR into their linear blocks to reduce effective rank. The results are shown below:

|Dataset|Horizon|Transformer|PatchTST|
|-|-|-|-|
| ETTh1|96|0.573→0.553|0.404→0.404|
| |192|0.555→0.522|0.437→0.436|
| |336|0.637→0.565|0.453→0.453|
| |720|0.755→0.676|0.481→0.477|
| ETTh2|96|0.348→0.344|0.290→0.290|
| |192|0.473→0.469|0.352→0.351|
| |336|0.474→0.473|0.373→0.371|
| |720|0.519→0.496|0.406→0.403|
| ETTm1|96|0.376→0.356|0.298→0.296|
| |192|0.445→0.416|0.330→0.330|
| |336|0.473→0.458|0.371→0.369|
| |720|0.530→0.526|0.419→0.417|

As for Root Purge, the situation is more nuanced (For this section, we kindly ask the reviewer to take $z_{\text{fut}} = \hat{y}_{\text{fut}}$ as we cannot get the equation compliation to work properly):

1. Since there is no direct analogue of the rank–nullity principle in nonlinear settings, we apply Root Purge only to the final linear projection layer. 
2. In the linear model, Root Purge follows the formulation in __Equation (3)__. Since we assume we cannot forecast future noise, the model forecast ($z_{\text{fut}}$) and the noisy ground truth ($y_{\text{fut}}$) can form a pair where their difference estimates the noise on the signal. Extending this to nonlinear architectures requires feeding $z_{\text{fut}}$ and $y_{\text{fut}}$ back into the model to obtain a pair of latent encoding, so $z_{\text{fut}}$ must span at least a full lookback window. Consequently, results are available only for forecasting horizons greater than or equal to the lookback length.

We have summarized our results on a MLP model as follows:

|Dataset|Horizon|MLP|
|-|-|-|
| ETTh1|336|0.438→0.429|
| |720|0.455→0.447|
| ETTh2|336|0.381→0.368|
| |720|0.413→0.408|
| ETTm1|336|0.364→0.360|
| |720|0.428→0.424|


These results indicate that our methods can yield performance improvements even in more complex architectures, suggesting meaningful potential for generalization to nonlinear cases.

That said, we respectfully highlight several reservations from theoretical and practical perspectives:
- **Lack of clear physical interpretation**: Our methods are primarily motivated

### Author comment
---
Question 1: Under complex, non-stationary noise typical of real-world series, do the proposed methods retain theoretical advantages?
---

**Response.**

Thank you for this insightful question, which allows us to extend the discussion from the previous point. We fully agree that real-world time series often exhibit complex, non-stationary noise patterns.

Building directly from our previous response, where we clarified that **our theoretical insights hold for any zero-mean noise with finite moments** and that our algorithm is entirely **distribution-agnostic**, we argue that our methods retain their advantages for the following key reasons:

1. **Noise-Agnostic Regularization Framework**:  
   Both our proposed methods—Root Purge and rank reduction techniques—are fundamentally **distribution-agnostic**. They do not assume specific noise properties (Gaussianity, stationarity, etc.). Instead, they operate on the principle that:
   - Noise typically manifests as **spurious characteristic roots** and contributes to **small singular values** in the learned dynamics
   - By promoting low-rank structure or learning a noise-suppressing null space, our methods **filter out components that do not generalize**, regardless of their statistical distributions.


2. **Empirical Validation Across Diverse Real-World Settings**:  
Our extensive experiments across **8 real-world benchmarks** (__Table 1, Appendix E.4__) include datasets with inherently complex, non-stationary noise profiles (See Figure 12 for some examples). The consistent superiority of our methods—particularly on smaller or noisier datasets like Exchange and ETT—provides strong evidence that they **retain advantages under realistic, non-ideal noise conditions**.

### Author comment
---
Weakness 4: The theoretical analysis depends on i.i.d. Gaussian noise and stationarity assumptions to justify data efficiency and the regularizer; these assumptions often do not hold in practice, and no generalization beyond them is provided.
---

**Response.** We thank the reviewer for this important observation regarding the assumptions underlying our theoretical analysis.

- **Purpose of the Gaussian and stationarity assumptions**
In Section 3.2 (Proposition 1), we adopt the i.i.d. Gaussian noise and stationarity assumptions primarily to **facilitate analytical tractability**. These assumptions allow us to derive a closed-form expression that elucidates the noise sensitivity and scaling properties of characteristic roots. Without them, a rigorous closed-form analysis is not feasible.

- **Relaxation of Gaussianity**
Upon revisiting the proof in Appendix D.3 and Proposition 1, we note that the Gaussian assumption can be **relaxed to any zero-mean noise with finite second-order moments**. We have revised the manuscript to clarify this point and emphasize that the theoretical insights hold under a broader class of noise distributions.

- **Algorithmic robustness in practice**
Importantly, in both our algorithm design and experimental evaluation, **no assumptions on the data distribution are required**. Root Purge and rank-regularization operate directly on the characteristic roots of the estimated linear model, making the approach fully applicable to real-world time series, including those with non-Gaussian, heteroscedastic, or non-stationary noise.

We have updated the manuscript to explicitly highlight these clarifications, demonstrating that our theoretical analysis provides insightful guidance while our method remains practically robust across diverse datasets.

### Author comment
---
Weakness 3: The Root Purge objective may induce model degeneration: the model could prefer mapping any input to zero, and the paper offers no theoretical guarantees to prevent or mitigate this failure mode.
---

**Response.** We sincerely thank the reviewer for raising this important point regarding potential model degeneration under the Root Purge objective. We would like to kindly argue first that model degeneration is __never__ observed with the reasonable $\lambda$ values used in our paper. Further, we kindly argue that over-regularization is a well-known challenge in machine learning, and it is **not specific to our method** and similarly affects widely used techniques such as L1/L2 regularization, dropout, spectral penalties, and norm-based constraints. As with any regularization strategy, the practical solution lies in controlling its strength rather than attempting to rule out extreme pathological cases entirely.

In Root Purge, while a very large $\lambda$ could in principle drive the model toward trivial outputs, this behavior is no different from what occurs with overly strong classical regularizers. In practice, however, the goal is to use a **moderate $\lambda$** that enhances generalization while maintaining full expressive capacity. Our empirical studies consistently demonstrate that Root Purge is stable and beneficial across a broad range of reasonable hyperparameter settings.

- **Empirical performance in Table 1**
With appropriately chosen $\lambda$, Root Purge yields substantial performance gains across datasets and architectures. A degenerate solution would cause severe degradation, which we never observe. 

- **Ablation studies in Figure 2 and Table 13**
Our ablations show that Root Purge provides improvements even for small values of $\lambda$, and maintains consistent benefits across a wide range. Performance only degrades when $\lambda$ becomes unrealistically large—precisely the same behavior observed with any strong regularizer. These results indicate that Root Purge does not inherently push the model toward trivial outputs under typical usage.

- **Singular value dynamics in Figure 3**
By analyzing the evolution of singular values of the weight matrix $\mathbf{W}$, we observe that the dominant singular values remain stable even under relatively strong regularization. This directly counters the concern that Root Purge collapses the model by shrinking all singular values to zero. Instead, Root Purge selectively suppresses unstable modes while preserving the core representational capacity.

In summary, while extreme regularization can theoretically cause degeneration, this behavior is neither unique to Root Purge nor observed in any realistic setting. Our empirical results, ablation studies, and singular-value analyses collectively demonstrate that Root Purge is robust, stable, and effective when used with reasonable hyperparameter values.

### Author comment
---
Weakness 2: The technical contributions of DWRR and Root Purge appear simple.
---

**Response.** Thank you for the comment. We genuinely appreciate this observation, and we would actually interpret it as a compliment rather than a weakness.

- **Simplicity is a feature, not a flaw — consistent with engineering principles**
From an engineering-philosophy perspective, we believe that the most elegant and effective solutions are often simple ones that capture the essence of the problem. The deep learning community has repeatedly witnessed this: Dropout, BatchNorm, RevIN, ResNet skip connections—all are conceptually simple, yet they solved foundational problems precisely because they distilled the core issue to its essence.
Simplicity is in line with Occam's Razor: do not introduce unnecessary complexity. When a simple method reliably addresses a complex phenomenon, that typically indicates that the method is grounded in the right underlying principle.

- **Our method is derived *ab initio* from first principles**
Conceptually, our method is derived from first principles. Instead of starting from architectural heuristics or empirical design patterns, we return to the fundamental questions:
    - What is the core difficulty of time-series forecasting?
    - What is the essence of generalization in dynamical systems?

  By analyzing the analytic and algebraic properties of differential equations (Corollary 1 and 2), we derive algorithms (DWRR and Root Purge) that look simple on the surface precisely because they are rooted in the correct theoretical primitives. Simplicity here is the consequence of identifying the right abstraction, not a lack of depth.

  As in phenomenology, we aim to "return to the thing itself"—to the essential structure of the problem, rather than building layers of unnecessary machinery.

- **Simplicity has long been associated with mathematical and scientific beauty**
There is also a long intellectual tradition, both Eastern and Western, that views simplicity as a hallmark of truth:
    - In ancient Greek philosophy, from Pythagoras to Plato, the highest natural laws were believed to be simple, harmonious, and mathematically expressive.
    - In the Eastern tradition, the idea of **大道至简** ("the great way is supremely simple") captures thousands of years of philosophical and aesthetic wisdom.
    
  By adopting the simplest operator that correctly captures the fundamental roots of the dynamics, DWRR and Root Purge follow this tradition of mathematical elegance.

We sincerely thank the reviewer for raising this point. In our view, the fact that the final algorithms are simple is precisely what demonstrates the strength and clarity of the underlying theoretical insight. Simplicity, when achieved through first principles, is often the strongest indication that the method has captured the true nature of the problem.

### Author comment
Thank you very much for your valuable and insightful comments! Below, we address your concerns point by point.

---
Weakness 1: The core insight “preserving dominant characteristic roots to suppress noise” is not novel and aligns with fundamental conclusions from classical Singular Spectrum Analysis (SSA).
---

**Response.** Thank you for raising this point — it is an insightful observation, and we appreciate the opportunity to clarify the distinction. We have also provided a systematic discussion of SSA and related work in Appendix B.1.

At first glance, our method may appear similar to SSA because both involve spectral analysis. However, the core principles, operational mechanisms, and theoretical motivations of the two approaches differ fundamentally.

- **Singular Spectrum Analysis (SSA)**
SSA is essentially an application of Taken's embedding theorem from dynamical-systems theory [1, 2]. When one cannot directly observe the full state-space evolution, Taken's theorem [3] states that a delay-coordinate embedding can reconstruct a space that is topologically conjugate to the true underlying dynamics. SSA uses this principle to perform Hankelization in the reconstructed state space.

  During forecasting, SSA then requires de-Hankelization to enforce certain consistency constraints （e.g. overlapped part of the original series must be the same). However, this step is heuristic: it lacks theoretical guarantees and is known to introduce additional reconstruction error.

- **Our Method**
By contrast, our work identifies a different underlying principle of generalization in time-series learning: we leverage both
    - **the analytic properties** of the governing differential equations (Corollary 1), and  
    - **the algebraic properties** of the governing differential equations (Corollary 2).
    
  This perspective leads us to directly characterize how one should extract the true characteristic roots of the dynamics in the presence of noise. Unlike SSA, which operates in a reconstructed state space, we show that performing spectral analysis in the weight space is significantly more effective for isolating the dominant dynamical modes.

  Furthermore, in our approach, Hankelization is not intended to reconstruct a hidden state space or approximate the original dynamics via a Taken-style embedding. Rather, it serves a much simpler and more direct role:
    - to slice the raw time series into fixed-length training segments, and
    - to express the optimization objective in a more compact and tractable form.

  Thus, the Hankelization in our method is a data preprocessing and formulation device, not a dynamical reconstruction mechanism as in SSA.

- **Summary of Key Differences**
We summarize the key differences below:

| Aspect | SSA | Our Method |
|--------|-----|------------|
| **Theoretical foundation** | Taken's embedding theorem | Analytic & algebraic properties of differential equations |
| **Working space** | Reconstructed state space | Weigh

### Author comment
---
Question 2: Why is the frequency-domain linear layer necessary for Root-Purge instead of a mere implementation detail?
---

**Response.** We thank the reviewer for this insightful question regarding the necessity of the frequency-domain linear layer in Root Purge. 
- **Practical Motivation**
The frequency-domain linear layer has been adopted in recent time series works such as FITS [1] and FreTS [2], which demonstrate **improved training stability and empirical performance**. We have also confirmed this observation in our experiments: see **Table 11** in the Appendix, where frequency-domain linear layers show consistent advantages in gradient-based Root Purge training. Since Root Purge relies on gradient-based optimization, we follow this design choice to leverage these practical benefits.

- **Effectiveness in the Time Domain**
Root Purge is not inherently tied to the frequency domain. We conducted parallel experiments using a **time-domain linear layer**, reported in **Appendix E.7**, and observed **strong performance improvements** as well. This indicates that the algorithm itself is robust and effective regardless of whether the linear layer operates in the time or frequency domain.


- **Implicit Bias and Training Dynamics**
Finally, while the detailed investigation of training dynamics is potentially beyond the scope of this paper, we note that the observed empirical differences may arise from **implicit biases introduced by gradient descent**. Similar phenomena have been studied in the context of deep linear networks (networks with identity activations) as discussed in [4].

In summary, the frequency-domain linear layer is **not strictly necessary** for Root Purge to be effective, but it provides practical advantages for gradient-based optimization. Both theoretical and empirical evidence supports that Root Purge is robust across domain choices.

#### Reference
1. Xu, Z., Zeng, A., & Xu, Q. FITS: Modeling Time Series with $10 k$ Parameters. In The Twelfth International Conference on Learning Representations.
2. Yi, K., Zhang, Q., Fan, W., Wang, S., Wang, P., He, H., ... & Niu, Z. (2023). Frequency-domain MLPs are more effective learners in time series forecasting. Advances in Neural Information Processing Systems, 36, 76656-76679.
3. Toner, W., & Darlow, L. N. (2024, July). An Analysis of Linear Time Series Forecasting Models. In International Conference on Machine Learning (pp. 48404-48427). PMLR.
4. Vardi, G. (2023). On the implicit bias in deep-learning algorithms. Communications of the ACM, 66(6), 86-93.

### Author comment
---
Question 1: What is the transferability of the method? Can linear models be used in other areas than time series learning?
---

**Response.** Thank you for the thoughtful questions. Since the second question concerns the generality of linear models, we address that one first.

- **On the Generality of Linear Models Beyond Time-Series Learning**
Regarding the second question, the broad applicability of linear models is well-established in both classical machine learning and statistics. Linear regression, PCA, and related techniques offer solid theoretical grounding, interpretability, and well-understood optimization properties. In Appendix B.1, we briefly survey the development of linear prediction theory, which has historically played a central role in many areas of data analysis.

  Importantly, the relevance of linear models has not diminished in the deep learning era. On the contrary, linear components are fundamental to a wide range of modern techniques, such as:
    - **LoRA** [1] - low-rank adaptation of large language models;
    - **Linear probing** [2] - model analysis through linear classifiers;  
    - **Model editing** [3] - modifying model behavior via linear interventions;
    - **Model pruning** [4] - compressing models using linear constraints.

  Furthermore, recent work has taken a differential-geometric perspective and defined new operations under which neural networks become linear [5]. These developments collectively reinforce that linear structures remain central to contemporary machine-learning methodologies.

- **On the Transferability of Our Method**
The transferability of our method can be discussed from two complementary perspectives:

    1. **Generality of Spectral Methods**
    In the narrow sense, the spectral method we use is based on SVD. Its utility extends far beyond time-series analysis. SVD and related spectral tools are widely used in:
        - Signal processing
        - Recommendation systems  
        - Community detection
        - Ranking problems
        - Structured matrix recovery
        
        These applications rely on spectral methods' ability to uncover latent low-rank or orthogonal structures that are intrinsic to a wide variety of datasets. We provide a more detailed discussion of spectral methods in __Appendix B.1__, and we also refer the reviewer to [6], which offers an excellent introductory overview of the theoretical and practical power of spectral techniques.

    2. **Generality of Adaptive Decomposition**

       A second key aspect is the adaptive decomposition that our method performs. Our approach learns an operator whose null space is aligned with the intrinsic structure of the data—crucially, without requiring any prior knowledge of that structure. This adaptivity makes the method fundamentally data-driven: any scenario where one aims to identify or exploit a meaningful null space, or more broadly a latent linear structure, stands to benefit from our approach. Thus, any task

### Author comment
---
Weakness 2: The manuscript lacks a comprehensive discussion of related work, which hampers readers, particularly those less familiar with the domain. Thus, it remains unclear how the proposed approach advances the state of the art or distinguishes itself from existing methods.
---

**Response.** We thank the reviewer for emphasizing the need for a comprehensive discussion of prior work.

While the “Related Work” section in the main text is concise, we provide an extensive discussion in Appendix B.1, which situates our method relative to multiple prior approaches. Here we summarize the key distinctions below:

- **Transformer-based and deep time-series models** focus on capturing complex non-linear dependencies and long-range patterns using attention mechanisms and seasonal-trend decomposition. In contrast, our method leverages linear characteristic root analysis to identify and regularize spurious roots in linear models, offering a principled and interpretable mechanism to improve long-term forecast robustness without relying on large neural architectures.

- **Minimalist and linear models** emphasize efficiency by separating trend and seasonality or exploiting low-dimensional linear structure. Our work goes further by analyzing the full spectrum of characteristic roots and systematically purging those corresponding to noise or unstable dynamics, which improves both stability and accuracy over standard linear decompositions.

- **Spectral and low-rank methods** (e.g., SSA) exploit low-rank structure or singular value decomposition for denoising and dimensionality reduction. Our approach extends these ideas by directly connecting low-rank recovery with characteristic roots, using Root Purge to remove spurious roots while preserving true latent dynamics, providing a theoretically grounded and practically effective regularization strategy.

- **Koopman operator-inspired methods** extract linear representations from nonlinear dynamics via operator-theoretic frameworks. Unlike these approaches, our method remains within a linear time-series forecasting paradigm, but leverages characteristic root analysis to achieve robust long-term prediction and interpretability with minimal model complexity.

In the revised manuscript, we now explicitly direct readers from the main text to __Appendix B.1__, highlighting how our method builds on and differs from prior work. 

We appreciate the reviewer’s feedback, which allows us to make these distinctions more visible and accessible to all readers, including those less familiar with the domain.

### Author comment
Thank you very much for your valuable and insightful comments! Below, we address your concerns point by point.

---
Weakness 1: Theoretical analysis is an advantage of this work, but it can easily make it difficult for readers to understand. It is necessary to provide intuitive explanations in the key derivation process
---

**Response:** 

We thank the reviewer for this valuable suggestion. In response, we have substantially improved the accessibility of the theoretical section. Specifically, we have added 
1. a mind map summarizing the key concepts and their relationships in __Appendix A, Figure 5__, and 
2. a concise, reader-oriented summary of the main theoretical results in __Appendix A, Table 4__. 

Given the length of the paper (65 pages), we additionally introduced a detailed **table of contents** to help readers navigate the derivations and theoretical arguments more intuitively. We hope these additions make the theoretical flow clearer and easier to follow.

### Author comment
---
Question 2: If we encounter a complex trend in the future that Instance Normalization can't flatten, does your Root Purge method just fail? How can you convince us that it's still robust in that scenario?
---

**Response:** 

We sincerely thank the reviewer for raising this important question regarding the robustness of our method when Instance Normalization (IN) may not fully “flatten” complex trends. We interpret “flatten” as “remove trend,” and please kindly let us know if this interpretation differs from your intention. We would like to offer several clarifications.

- **IN is not designed to remove trends, and it does not succeed at doing so even in simple cases**
As originally proposed in [1], IN is primarily intended to mitigate distribution shift by removing the mean/variance discrepancy across segments. It is not a trend-removal mechanism.
Indeed, IN cannot fully remove even simple deterministic trends (e.g., exponential or high-order polynomial). This is also reflected empirically in NLinear [2], where replacing IN with a simple “subtract-the-last-value” operation yields similar performance. This shows that IN’s ability to “flatten trends” plays a limited role in practice, since even if we weaken the trend removal capability of IN, it remains competitive.

- **Theoretical role of IN: it always inserts a fixed unit root**
In our analysis (__Remark 1; Appendix C.4__), we show that IN’s effect in linear models is equivalent to imposing a fixed characteristic root at 1, corresponding to shift-invariance. Formally, IN forces the general solution to take the form $$y_t = f(t) + C$$ where the value of $C$ is being lively determined. This is a hard constraint on the characteristic polynomial and does not depend on the complexity of the underlying trend. Thus, IN does not “fail” in the sense relevant to our method: it always guarantees the presence of a __fixed__ unit root and therefore always performs its theoretical function.

- **Root Purge operates independently of IN**
Root Purge focuses exclusively on the __modifiable__ characteristic roots. Its purpose is to identify and suppress roots associated with noise or spurious temporal patterns. Since IN only affects the single __fixed__ root at 1, and has no impact on the remaining roots learned by the model, Root Purge operates on a completely separate part of the spectrum. Therefore, even if IN imperfectly removes trends, Root Purge continues to function as intended. 

- **Empirical Evidence on the Robustness of Root Purge**
As shown in __Table 1__, Root Purge consistently achieves strong performance across datasets with varying levels of non-stationarity. For example, in ETTh1, there are strong drifts and complex trends too complex to be removed by IN as previously discussed, yet our method remains robust and achieves state-of-the-art results. This confirms that Root Purge does not depend on IN successfully flattening complex structure.

#### Reference

1. Kim, T., Kim, J., Tae, Y., Park,

### Author comment
---
Question 1: Does the Low-Rank Assumption limit the generality of method, making it effective only for a specific subset of (simpler) time series datasets?
---

**Response.** Please refer to our response to the Weakness 2 above.

### Author comment
---
Weakness 3: Theory-Practice Gap (Trends): The theoretical analysis assumes homogeneous equations (constant/zero bias) . This is a poor fit for real-world data with non-stationary, dynamic trends.
---

**Response.** We sincerely thank the reviewer for raising this important point regarding the applicability of our homogeneous formulation to real-world data with non-stationary trends. We clarify below that the theoretical framework based on homogeneous linear difference equations is in fact **fully expressive** for the trend components relevant in practice. Our response is grounded in two well-established facts in linear systems theory.

1. **Nonhomogeneous linear systems can always be rewritten as homogeneous systems of higher order**
Consider the nonhomogeneous linear recurrence
\begin{equation}
y_t+a_1 y_{t-1}+\cdots+a_n y_{t-n}=f(t).
\end{equation}
Suppose the forcing term  $f(t)$ itself satisfies a linear homogeneous difference equation of order $m$:
\begin{equation}
f(t)+b_1 f(t-1)+\cdots+b_m f(t-m)=0.
\end{equation}
This setup covers all structured trend families commonly used in practice—**polynomials, exponentials, sinusoids, and their finite sums**.

    By successively shifting the original equation and substituting out all appearances of $f(t-k)$ using the above relation, one obtains a **single homogeneous linear difference equation of order** $n+m$ involving only $y_t$. This is a classical construction in linear recurrence theory.

    **Implication**:
Any linear forecasting model with a structured trend component (seasonal, polynomial, exponential, oscillatory, etc.) is **exactly representable** as a homogeneous recurrence after a finite increase in order. All trend types examined in Corollary 1 fall within this category.

2. **Arbitrary continuous trends can be approximated by solutions of homogeneous systems**

    To address more general real-world nonstationary trends, we invoke a standard approximation principle based on the following theorem:

    **Stone–Weierstrass Approximation Theorem:** Any continuous function on a compact interval can be uniformly approximated by polynomials.

    Since a polynomial of degree $d$ satisfies $\Delta^{d+1} P_d(t) = 0$, it solves a homogeneous linear difference equation of finite order. Therefore, we have the following:

    **Corollary:** For any continuous forcing term $f(t)$ and any $\epsilon>0$, there exists a polynomial $P_d(t)$—hence a function satisfying a homogeneous difference equation—such that $\sup_t |f(t) - P_d(t)| < \epsilon.$

    Replacing $f(t)$ with $P_d(t)$ yields a linear system that is:

    - **arbitrarily close** to the original nonhomogeneous system in prediction error, and
    - **exactly reducible** to a higher-order homogeneous system.

    Thus, **homogeneous linear difference equations form a universal approximating family for models with continuous trend components.**

3. **Practical relevance to forecasting models**
State-of-the-art linear forecasting archite

### Author comment
---
Weakness 2: **Contingent on Low-Rank Assumption**: The methods are motivated by an assumption that the true signal is low-rank. However, on large, complex datasets, the paper's results show the optimal rank is often full , and the proposed methods offer minimal benefit. This limits the methods' generality.
---

**Response.** Thank you for this thoughtful comment. We apologize for any confusion caused by the presentation in the initial submission. After re-examining both the RRR and DWRR experiment logs (included in the original __supplementary zip__, under `Rank_Reduction` folder with logs `RRR.log` and `DWRR.log`), we confirm that the optimal ranks tends to be below full rank even for complex data such as ECL and Traffic. For convenience, we summarize the results below. We have also revised our manuscript to prevent further confusion.

| Data   | Horizon | RRR optimal rank | DWRR optimal rank |
|--------|---------|-----|------|
| ECL    | 96      | 96  | 96   |
|        | 192     | 180 | 192  |
|        | 336     | 204 | 240  |
|        | 720     | 294 | 210  |
| Traffic| 96      | 96  | 96   |
|        | 192     | 172 | 192  |
|        | 336     | 144 | 174  |
|        | 720     | 150 | 198  |

In addition, we address the concern from several perspectives.

- **Low-rank structure is a well-established assumption in time-series modeling**
The low-rank assumption is not specific to our work; rather, it is a foundational principle that has been extensively used across time-series analysis and signal processing [1,2]. Many classical models, such as ARMA processes, seasonal patterns, and systems with smooth dynamics, exhibit strong low-dimensional structure in their predictive operators or latent states. We survey the relevant literature in __Appendix B.1__ and explain why low-rank structure appears naturally in many practical time-series settings.

- **"Low-rank" is a relative notion in linear prediction**
Importantly, rank must be understood relative to model capacity, not as an absolute property. In linear prediction, we can choose a longer lookback window to increase model capacity. Furthermore, by adopting individual channel modeling, we can effectively extend the degree of freedom /rank to enhance model capacity, as demonstrated by the results in __Table 2__, where Root Purge brings significantly more improvements than in CI setting. Under such settings, "low-rank" refers to the structure of the signal relative to this enlarged capacity. The effective rank that matters is therefore problem-dependent and adjustable, constrained mainly by computational budget rather than theoretical limitations.

- **Even complex dynamics admit effective reduced-order models**
Even when the underlying dynamics are highly complex or full-rank in an absolute sense, reduced-order modeling is a standard and powerful approach. Many real-world high-dimensional dynamics systems are governed by extremely can be approximated well by low-dimensional representations. e

### Author comment
Thank you very much for your valuable and insightful comments! Below, we address your concerns point by point.

---
Weakness 1: **Hyperparameter Sensitivity**: The methods' performance relies heavily on tuning $\rho$ or $\lambda$. This data-specific tuning is difficult to estimate a priori and undermines the claim of robustness.
---

**Response:** We sincerely thank the reviewer for raising this point. We would like to clarify that our methods actually exhibit low hyperparameter sensitivity in practice:

- **Only a single hyperparameter is required for each model.**
$\rho$ is the __only__ hyperparameter for RRR and DWRR, and $\lambda$ is the __only__ hyperparameter for Root Purge. This keeps the search space minimal and avoids the complexity typically associated with multi-parameter tuning in time-series forecasting models.

- **For RRR and DWRR: $\rho$ is selected via post-training cross-validation rather than manual tuning.**
Since $\rho$ is determined automatically using a simple  validation procedure with **Rank-MSE trade-off** on a validation set, it does not require problem-specific heuristics or extensive hyperparameter sweeps. This makes the procedure practical and reproducible across datasets. We have showcased some representative examples for the Rank-MSE trade-off curves in **Figures 15 and 16 in Appendix E**.

- **For Root Purge, the model is not sensitive to the choice of $\lambda$.**
We observe that $\lambda$ is effective even at very small values (e.g., 1/32) and it offers benefit for $\lambda$ up to, e.g., 1/2. Additionally, the model performance follows a clear and smooth trend: first increasing and then decreasing within a reasonable range (e.g., $\lambda\in\{1/32, 1/16, 1/8, 1/4, 1/2, 1, 2\}$); see __Figure 2__. More importantly, as a rule of thumb, a good choice of lambda is usually one of $\{0.125, 0.25, 0.5\}$, aligning with the setting we used in the main experiment. As a result, the optimal value can be identified reliably and with minimal search effort.

Overall, we believe these properties indicate that our approach is stable and easy to tune, rather than heavily reliant on dataset-specific hyperparameters.

### Characteristic Root Analysis and Regularization for Linear Time Series Forecasting


## Meta review / decision
### Paper Decision
Accept (Poster)

## PDF extracted text (first pages)
```text
Published as a conference paper at ICLR 2026
CHARACTERISTICROOTANALYSIS ANDREGULARIZA-
TION FORLINEARTIMESERIESFORECASTING
Zheng Wang1,†,∗, Kaixuan Zhang1,†, Wanfang Chen1,†, Xiaonan Lu1,†,
Longyuan Li1,†, Tobias Schlagenhauf2
1Bosch (China) Investment Co., Ltd., 2Robert Bosch GmbH
†{david.wang3, kaixuan.zhang, wanfang.chen, xiaonan.lu
longyuan.li}@cn.bosch.com
ABSTRACT
Time series forecasting remains a critical challenge across numerous domains, yet
the effectiveness of complex models often varies unpredictably across datasets.
Recent studies highlight the surprising competitiveness of simple linear models,
suggesting that their robustness and interpretability warrant deeper theoretical
investigation. This paper presents a systematic study of linear models for time
series forecasting, with a focus on the role of characteristic roots in temporal
dynamics. We begin by analyzing the noise-free setting, where we show that
characteristic roots govern long-term behavior and explain how design choices
such as instance normalization and channel independence affect model capabilities.
We then extend our analysis to the noisy regime, revealing that models tend to pro-
duce spurious roots. This leads to the identification of a key data-scaling property:
mitigating the influence of noise requires disproportionately large training data,
highlighting the need for structural regularization. To address these challenges,
we propose two complementary strategies for robust root restructuring. The first
uses rank reduction techniques, includingReduced-Rank Regression (RRR)
andDirect Weight Rank Reduction (DWRR), to recover the low-dimensional
latent dynamics. The second, a novel adaptive method calledRoot Purge, encour-
ages the model to learn a noise-suppressing null space during training. Extensive
experiments on standard benchmarks demonstrate the effectiveness of both ap-
proaches, validating our theoretical insights and achieving state-of-the-art results
in several settings. Our findings underscore the potential of integrating classical
theories for linear systems with modern learning techniques to build robust, inter-
pretable, and data-efficient forecasting models. The code is publicly available at:
https://github.com/Wangzzzzzzzz/RootPurge.
1 INTRODUCTION
Time series forecasting is a foundational task in a wide range of critical applications, including
finance, weather prediction, traffic modeling, and energy systems (Hamilton, 2020). Despite its
importance, long-term forecasting remains a particularly challenging problem due to inherent uncer-
tainty, noise, and complex temporal dependencies in real-world data (Kong et al., 2025). In response,
the research community has devoted substantial efforts to developing increasingly sophisticated
model architectures (Woo et al., 2023; Xu et al., 2023; Zhou et al., 2022; Nie et al., 2022), from deep
recurrent networks to attention-based transformers, in an attempt to capture long-range dependencies
and improve accuracy.
However, as emphasized in the position paper (Brigato et al., 2025), no single model consistently
outperforms others across all datasets and forecasting horizons. This observation echoes the"No
Free Lunch" theorem(Adam et al., 2019): in the absence of strong assumptions or domain-specific
priors, it is impossible to design a universally superior forecasting model. This limitation prompts a
rethinking of current approaches and highlights the need for more fundamental, theory-driven insights
into what makes a time series model effective.
∗Corresponding todavid.wang3@cn.bosch.com
1
Published as a conference paper at ICLR 2026
Linear ModelsonTime Series Analysis:	𝐘=𝐗𝐖Generalization Foundations: Characteristic Roots  𝑦!+𝑎"𝑦!#"+⋯+	𝑎$𝑦!#$=0		↔		𝑟",𝑟%,⋯,𝑟$Fact 1 + Prop. 4General Modeling PrinciplesNoise-free Case: üLookback WindowüForecasting HorizonüInstance NormalizationFact 2 + Prop. 5 
Noisy Case: üData Scaling LawüChannel IndependenceProp. 1, 3, 6
Algorithm DesignRank ReductionProp. 2, 7 𝐖	≈	𝐔!𝚺	𝐕!"üError Bound: Prop. 8, 9üRobustness: Prop. 10, 11
Root Purge𝐘−𝐗𝐖𝟐+	(𝐘−𝐗𝐖)𝐖𝟐üError Bound: Prop. 12, 13üConvergence: Prop. 15
Essence: Rank-Nullity Thm.RelationshipProp. 14 
Algorithm connects back to characteristic roots:  Prop. 16 Generalization foundations guide analysis of modeling principles
Analysismotivatesalgorithm design
Figure 1: Structure of the paper and its main contributions.
Recent studies show that linear systems, despite their simplicity, often match or exceed the perfor-
mance of complex nonlinear models, particularly in long-term forecasting (Zeng et al., 2023; Toner
and Darlow, 2024; Li et al., 2023). Their robustness, interpretability, and analytical clarity make
them a strong foundation for forecasting. Motivated by this, we develop a theoretical framework to
study the core properties of linear systems, focusing on the role of dominant characteristic roots that
encode the essential structure of the data. At the same time, real-world time series are rarely clean;
they are typically contaminated with noise that obscures the underlying structure (Lim and Zohren,
2021). Complex deep learning models are especially prone to overfitting such noise, often resulting
in poor generalization and unreliable forecasts. To address this, we draw inspiration from recent
findings (Shi et al., 2024) showing that only a small subset of data components—those capturing the
essential structure—meaningfully impact the prediction accuracy. In linear dynamical systems, these
correspond to dominant characteristic roots that govern the system behavior. Our approach focuses
on identifying these core roots while systematically suppressing noise and spurious dynamics.
In this work, we present a systematic analysis of linear models for time series forecasting, emphasizing
the role of characteristic roots in determining model expressivity and dynamic behavior (refer to
Figure 1 for a road map of this paper). We begin by examining how forecasting horizon and lookback
window interact with characteristic roots in noise-free settings, showing that common practices such
as instance normalization and channel-independent modeling naturally arise from this framework.
We then extend our analysis to noisy settings, where models tend to learn spurious roots—artifacts
of noise that distort prediction and obscure true dynamics. This reveals a key data-scaling property:
mitigating the impact of noise demands significantly more training data. This reduces data efficiency
and underscores the need for structural regularization. Motivated by these insights, we propose two
complementary strategies for robust root identification. The first leverages rank reduction, including
Reduced-Rank Regression(Izenman, 1975) andDirect Weight Rank Reduction, to enforce a
low-dimensional structure aligned with the latent dynamics. The second introducesRoot Purge,
a novel adaptive training method that promotes the learning of an appropriate null space, actively
suppressing noise while preserving informative signal components. We evaluate both approaches on a
range of standard time series forecasting benchmarks and demonstrate that they consistently enhance
model robustness and accuracy, often achieving state-of-the-art performance. Side experiments and
controlled toy examples further validate our theoretical insights. Overall, our findings emphasize the
value of integrating classical linear system theory with modern optimization techniques, and pave the
way for future work on robust, interpretable, and scalable forecasting models. The contributions in
this paper can be summarized as follows:
• Theoretical Analysis: We provide a systematic study of linear models for time series forecasting,
analyzing the role of characteristic roots in both noise-free and noisy settings, and uncovering a
key data-scaling property that motivates structural regularization.
• Proposed Methods: We introduce two strategies for robust root identification: rank reduction
techniques to enforce a low-dimensional structure, and Root Purge, a novel adaptive training
method that suppresses noise via null-space learning.
• Empirical Validation: We verify the effectiveness of our approaches through strong performance
on standard benchmarks. We also validate our theory with additional controlled experiments.
2
Published as a conference paper at ICLR 2026
2 BACKGROUND
Related Work.Time series forecasting aims to predict future values by learning patterns like trends
and seasonality from historical data. Various modeling paradigms have emerged to tackle long-term
forecasting challenges (Kong et al., 2025). Transformer-based models have been prominent: Nie et al.
(2022) segments series into patch-level tokens with channel-wise modeling, while Zhou et al. (2022)
combines seasonal-trend decomposition with transformers. Woo et al. (2023) proposes time-index
models that condition on future timestamps to support both interpolation and extrapolation. Beyond
time-domain methods, frequency-based approaches like Xu et al. (2023) apply low-pass filtering and
complex linear layers to enhance long-term modeling. In parallel, minimalist models have gained
traction: Lin et al. (2024) achieves strong results with just 1,000 parameters via structured sparsity,
and Zeng et al. (2023) shows that simple linear models can outperform transformers by separately
modeling trend and seasonality. Recent evaluations (Brigato et al., 2025) show that no single method
dominates across all settings, emphasizing the need for diverse benchmarks and context-aware model
selection. Motivated by this, we pursue a theoretical perspective on time series forecasting, aiming
for models that balance simplicity, interpretability, and robustness across diverse temporal dynamics.
To see a detailed related work and further background, please refer to Appendix B.1.
Problem Formulation.Let {yt}T
t=1 be a multi-channel time series of length T , where each
observation yt ∈R m represents an m-dimensional vector at time t. The goal of multi-horizon
forecasting is to learn a mappingfthat predicts future values as
ˆYt+1:t+H =f(y t,y t−1, . . . ,yt−L+1),
where ˆYt+1:t+H = [ ˆyt+1, ˆyt+2, . . . ,ˆyt+H ] is an m×H matrix of forecasts. Here, H is the length
of forecasting horizon, L is the length of lookback window, and f is the forecast model, which is
required to capture temporal dependencies, account for noise and non-stationarity, and generalize
historical patterns to unseen future data.
Preliminary.We consider the class of single-channel (i.e., m= 1 )homogeneous linear difference
equationsdue to their analytical tractability in modeling temporal dependencies, taking the form:
yt +a 1yt−1 +· · ·+a pyt−p = 0,
where p is the order of the difference equation and {ai}p
i=1 are constant coefficients. The general
solution1 at time steptis a linear combination ofcharacteristic rootsraised to powert:
yt =C 1rt
1 +C 2rt
2 +· · ·+C prt
p,
where {Ci}p
i=1 are constants determined by initial conditions, and {ri}p
i=1 are obtained by solving
thecharacteristic equation:r p +a 1rp−1 +· · ·+a p = 0.
3 THEORETICALANALYSIS
Linear dynamical models strike a valuable balance between analytical simplicity and expressive
power, making them effective at capturing core temporal patterns such as trends, oscillations, and
exponential behaviors. In this section, we explore the foundations of linear modeling in time series
forecasting. Our goal is to understand the principles governing linear dynamics through the lens of
characteristic roots, enabling us to interpret, justify, and generalize widely used modeling choices.
We begin by formalizing the core problem following standard conventions. Given a normalized
single-channel time series, we define linear forecasting as the solution to the least-squares objective2:
min
W
∥Yfut −Y hisW∥2
F ,(1)
where Yhis ∈R N×L and Yfut ∈R N×H represent the collection of N history and future segments
from the same normalized sequence, W∈R L×H represents the coefficient matrix. Each row in Yhis
1Here we consider the simplest case where all characteristic roots are distinct.
2The omission of a bias term is justified by the fact that linear difference equations with constant biases can
be algebraically transformed into equivalent homogeneous systems; see Appendix B.3 and C.1 for justifications.
3
Published as a conference paper at ICLR 2026
and Yfut, denoted as yhis ∈R L, yfut ∈R H, corresponds to one observed history and future segment,
respectively. Solving Equation (1) is equivalent to independently estimating the j-th column of Yfut,
corresponding to thej-th forecasting horizon (jsteps ahead to the future), by solving:
min
W
X
t
 
yt+j −
LX
k=1
Wkj ·y t−k+1
!2
, j= 1, . . . , H.(2)
This formulation reflects a regression-based interpretation of temporal forecasting and serves as a
direct proxy for learning the underlying recurrence relations.
3.1 ROLE OFCHARACTERISTICROOTS ANDNOISE-FREELINEARMODELINGPRINCIPLES
Recall from Section 2 that for linear models governed by difference equations, solutions are de-
termined by their characteristic roots. Therefore, we can arrive at Fact 1 as follows, derived from
the properties of general solutions. This highlights a key generalization property of linear models:
the ability to cover a wide range of temporal behaviors (details in Appendix D.1, Corollary 1, and
Corollary 2) through appropriate choice of roots, rather than through complex parameterization.
Fact 1.A linear model can represent any time series whose characteristic roots
are a subset of its own.
For better illustration of this fact, we provide a toy example in Appendix C.3. Based on Fact 1, in the
noise-free setting, the optimization objective defined in Equation (1) can often achieve zero given
appropriate model capacity. This allows us to convert a linear time series model into a difference
equation and study the impact of key design choices of forecasting horizon and lookback window.
It is common practice (Xu et al., 2023; Lin et al., 2024) to model each forecast step independently
as in Equation (2), resulting in H separate regression problems, each corresponding to a specific
forecasting horizon. Further, it is common that we use a long lookback window length L, whereas
the underlying process follows a simpler minimal recurrence relation of order K, with K < L . Both
of these choices introduce redundancy in the input representation. Nonetheless, this redundancy is
not detrimental to learning and can, in fact, offer flexibility in parameterization. We summarize our
key insight as follows, with more details in Appendix C.2 and D.2:
Fact 2.The characteristic root set of a linear higher-horizon model, or one with
an extended lookback window, always preserves, as a subset, the roots that govern
the fundamental system dynamics.
This observation offers theoretical support for independently modeling each horizon, as higher-
horizon models remain consistent with the system’s true dynamics. Moreover, increasing the lookback
window does not alter the set of roots but rather introduces multiple equivalent representations.
We highlight two common time series modeling techniques that align with our framework above,
with more details in Appendix C.4. A further empirical study of Channel-independent (CI) modeling
and an alternative technique called INC is provided in Table 3, Section 5.4.
Remark 1.Instance normalization introduces a unit root, allowing the model to generalize across
sequences with arbitrary mean shifts. Channel-independent modeling remains effective when the
model has sufficient degrees of freedom to capture the union of characteristic roots across all channels.
3.2 DATASCALINGPROPERTYUNDERNOISYOBSERVATIONS
In practical applications, time series data are often contaminated with stochastic noise, which presents
a fundamental challenge for model estimation and generalization. In the presence of noise, the
least-squares loss for a linear forecasting model takes the following form for a single segment:
E

∥(y∗
fut −W ⊤y∗
his) + (εfut −W ⊤εhis)∥2
2

,
where y∗
fut, y∗
his are noise-free history and future segments, respectively, and εhis, εfut denote additive
noise on these segments. This loss naturally decomposes into two components: signal fitting error
and noise-induced error. In theover-idealizedcase where the learned weight matrix W perfectly
recovers the signal dynamics, only the noise termE

∥εfut −W ⊤εhis∥2
2

remains.
4
Published as a conference paper at ICLR 2026
To better understand the noise sensitivity of mean squared error (MSE)-based linear models, we
analyze a simplified setting in which both inputs and outputs consist solely of Gaussian noise. The
following proposition summarizes such asymptotic behavior (see details in Appendix C.5 and D.3):
Proposition 1.For a linear model forecasting a zero-mean noise with finite second
moments, the learned weights converge at a rate proportional to O(1/
√
T) , where
Tis the length of the observed time series.
This result illustrates an important limitation of classical least squares training: despite its consistency
and unbiasedness, convergence is slow under noise. Even with perfect signal recovery, noise
effects decay only at a sublinear rate. This scaling behavior highlights that MSE-based training is
data-inefficient in high-noise regimes, requiring a substantial number of observations to achieve
low-variance estimates of the underlying dynamics.
4 NOISE-AWARELINEARFORECASTING VIAROOTRESTRUCTURING
In noisy environments, the data-scaling property highlights a key limitation of linear forecasting
models: robustness to noise requires a substantial amount of data. This challenge is compounded
when the model must also accurately recover the underlying signal dynamics, as misidentifying them
leads to fitting errors. From the perspective of characteristic roots, reliable forecasting hinges on
correctly identifying and preserving the roots that capture the signal’s temporal structure. However,
noise can obscure these roots. To address this, we next present two complementary approaches
designed to improve root restructuring and enhance robustness in practical settings.
4.1 RANKREDUCTIONMETHODS
In time series forecasting, the lookback window lengthL and the structure of the underlying dynamics
jointly determine the model’s expressive capacity. In the absence of noise, the matrixY∗
his formed by
slicing a deterministic time series has rank min(L, K), where K denotes the number of characteristic
roots. However, once noise is introduced, this low-rank structure becomes obscured—the observed
data matrix typically becomes full rank with high probability, even when the underlying signal
remains confined to a lower-dimensional subspace.
This observation motivates the use ofrank reductionas a denoising strategy. A straightforward, though
suboptimal, approach involves applying truncated singular value decomposition (SVD) directly to
the history matrix Yhis and future matrix Yfut. By projecting these matrices onto lower-dimensional
subspaces, one can suppress the variance introduced by noise and partially recover the latent signal
structure. However, direct manipulation of Yhis and Yfut is neither necessary nor ideal. It can be
shown that imposing a low-rank constraint on the model’s weight matrixW achieves an equivalent
effect (see Proposition 2 below). This constraint implicitly projects the input and output data onto
learned low-dimensional subspaces during training, without the need to alter the raw sequences
themselves. A low-rank W functions as a bottleneck, aligning Yhis and Yfut along directions of
maximal shared variation and filtering out noise-dominated components.
Proposition 2.Constraining W to be low-rank implicitly projects Yhis and Yfut
onto low-dimensional subspaces.
See Appendix D.4 for a detailed version and its proof. See also Appendix D.6 for how this improves
noise robustness. To operationalize this idea, we propose two practical strategies 
```
