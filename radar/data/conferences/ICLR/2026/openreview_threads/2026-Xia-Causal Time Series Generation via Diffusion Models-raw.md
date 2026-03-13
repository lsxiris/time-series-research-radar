# Causal Time Series Generation via Diffusion Models — OpenReview Raw Thread

- Forum: https://openreview.net/forum?id=9bkzvYw9ds
- PDF: https://openreview.net/pdf?id=9bkzvYw9ds
- Section: 一、时间序列生成：因果性、多样性与领域适配
- Zhihu score: 7.33
- Venue status: ICLR 2026 Conference Desk Rejected Submission

## Submission metadata
- Authors: Yutong Xia, Chang Xu, Yuxuan Liang, Qingsong Wen, Roger Zimmermann, Jiang Bian
- Primary area: learning on time series and dynamical systems
- Keywords: Time Series Generation, Conditional Generation, Time Series Analysis

## Abstract
Time series generation (TSG) synthesizes realistic sequences and has achieved remarkable success. Among TSG, conditional models generate sequences given observed covariates, however, such models learn observational correlations without considering unobserved confounding. In this work, we propose a causal perspective on conditional TSG and introduce causal time series generation as a new TSG task family, formalized within Pearl’s causal ladder, extending beyond observational generation to include interventional and counterfactual settings. To instantiate these tasks, we develop CaTSG, a unified diffusion-based framework with backdoor-adjusted guidance that causally steers sampling toward desired interventions and individual counterfactuals while preserving observational fidelity. Specifically, our method derives causal score functions via backdoor adjustment and the abduction–action–prediction procedure, thus enabling principled support for all three levels of TSG.  Extensive experiments on both synthetic and real-world datasets show that CaTSG achieves superior fidelity and also supporting interventional and counterfactual generation that existing baselines cannot handle. Overall, we propose the causal TSG family and instantiate it with CaTSG, providing an initial proof-of-concept and opening a promising direction toward more reliable simulation under interventions and counterfactual generation.

## Reviews
### Reviewer_AVVu
- summary: The paper formalizes causal time-series generation by extending conditional TSG beyond observation $P(X\mid C)$ to interventional $P(X\mid do(C))$ and counterfactual $P(X'\mid X,C,C')$ tasks. It introduces CaTSG, a diffusion framework that derives causal score functions via backdoor adjustment and the abduction–action–prediction procedure, enabling interventional and counterfactual sampling without ground-truth interventions.  

CaTSG uses a learnable environment bank and an EnvInfer module to approximate latent confounders, trained with a swapped-prediction objective and an orthogonality regu
- strengths: * Thorough derivations and empirical study.
* Clear, well-structured presentation, helped by a consistent running example.
* Novel yet practical approach that avoids manual confounder hunting.
* Strong, natural integration with recent diffusion methods.
* Unified treatment of observational, interventional, and counterfactual generation.
- weaknesses: * Most points below are already acknowledged by the authors; they’re noted here to contextualize impact rather than as surprises.
* Dependence on a fixed SCM (E->C, E->X, C->X) can limit validity under feedback, mediators, or time-varying confounding; conclusions may be sensitive to misspecification.
* Finite “environment bank” approximates latent causes; the choice of $K$ and representation quality could leave residual confounding or introduce bias.
* Real-data counterfactuals lack ground truth; evidence necessarily leans on synthetic settings or qualitative case studies, which constrains external validity.
* Robustness to guidance/inference hyperparameters (e.g., the guidance scale $\omega$) could be probed more systematically across seeds/datasets.
* Baseline coverage for interventional/counterfactual settings could be expanded where applicable to strengthen comparative claims.
* Computational overhead from diffusion plus environment inference is non-trivial; clearer wall-clock and 
- questions: * If some confounders are observed, can CaTSG directly condition on them instead of learning an environment bank? What changes (if any) to training/sampling are needed?
* How easily can the framework adapt to other causal graphs (mediators, instrumental variables, partial feedback)? What concrete modifications to the guidance rules would that entail?
* What (if any) identifiability guarantees exist for the learned environments with finite $K$? Any recommended heuristics for choosing $K$ (and the guidance scale $\omega$) in practice?
* How do you diagnose and handle limited overlap/positivity in $(C,E)$ (e.g., rare environment–context pairs)? Would you recommend reweighting, trimming, or curriculum strategies?
- rating: 8 | confidence: 3

### Reviewer_wJr5
- summary: In this work, the authors propose a causal perspective on conditional time-series generation (TSG) and introduce causal TSG as a new task family. The paper makes three key contributions:
1.	Causal expansion of conditional TSG. The authors formalize causal TSG as an extension of conditional TSG along Pearl’s ladder, adding two tasks beyond association—interventional (Int-TSG) and counterfactual (CF-TSG)—to better align generative modeling with real-world decision making.
2.	Unified causality-guided diffusion framework. They derive causal score functions via backdoor adjustmentand abduction–acti
- strengths: The method demonstrates good originality. The idea of using the environment as additional conditioning information is an effective way to help the model learn more stable relationships between X and C. The use of the SwAV-style training paradigm is also an interesting and sensible approach to learn useful "clustering" of the (X,C) pairs, enabling the model to absorb the underlying factors that generate the variation in these pairs.

The paper presents thorough experiments across four datasets an
- weaknesses: The explanation of how the environment is learned and generated could be clearer. More intuition should be provided regarding why the SwAV-style training task is well-suited for learning the environment.

Adopting the backdoor-adjusted approach is not without its challenges, as it requires learning additional components. Specifically, for each environment, the model needs to learn a conditional distribution P(X∣C,E=e). The paper does not adequately discuss the potential cost of using backdoor adjustment. A possible experiment could involve using untrained or completely noisy environment variables to see how the model performs compared to the unadjusted approach. It would be insightful to observe the negative impact of using backdoor adjustment and how the dimension and complexity of the (uninformative) environment variable might affect performance.

Following up on the previous point, causal methods typically target bias reduction. In this case, adding a learned environment variable is
- questions: Questions:
1.	Have you considered using a continuous or high-dimensional environment variable E? In many cases, splitting the confounding information into K discrete clusters or categories of environments can lead to poor performance, especially when there are many weak confounders that cannot be easily separated into K discrete environments.
2.	Have you considered using additional data or information to aid in learning the confounders? For example, instead of using SwAV, could you use supervised learning with additional data/information to predict (X,C), which could help in learning better embeddings for the confounders?
3.	Have you considered an inverse probability weighting (IPW) formulation for the problem?
If you have considered the above questions, I would be interested to hear why t
- rating: 6 | confidence: 4

### Reviewer_zSS3
- summary: The paper proposes a diffusion-based framework that extends observational time series generation (TSG) to interventional and counterfactual TSG under Pearl’s causal hierarchy, addressing unobserved confounding. Specifically, the authors generalize the standard definition of score functions to their causal counterparts under the structural causal model (SCM) framework. Building on this formulation, they propose CaTSG, a model comprising an environment inference module (EnvInfer), a learnable environment bank with an encoder, and a denoiser that integrates both conditional and environmental vari
- strengths: •	The authors explain the effect of unobserved confounding in the introduction by using an intuitional example, which enhances readers’ understanding of the concept, though I think summer holidays do not “cause” high temperature, but only “coincide” with high temperature instead.

•	The concepts of “intervention” and “abduction” are well illustrated in Figure 2.

•	The idea of extending CFG and score functions to causal learning is interesting, though there exist some studies that follow similar
- weaknesses: •	It would be better to further discuss recent studies that utilize diffusion model or Classifier-free Guidance for counterfactual generation, such [1] and [2].

•	For other aspects of potential weaknesses, please refer to the “Questions” section.

References:

[1]. Komanduri, Aneesh, et al. "Causal diffusion autoencoders: Toward counterfactual generation via diffusion probabilistic models." arXiv preprint arXiv:2404.17735 (2024).

[2]. Wu, Shenghao, et al. "Counterfactual generative models for time-varying treatments." Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 2024.
- questions: •	What is the rationale behind the adoption of the swapped loss $\mathcal{L}_{sw}$? For example, can we use a SimSiam-style loss $\mathcal{L} = \frac{1}{2} \mathcal{D}(h’, w’’) + \frac{1}{2} \mathcal{D}(h’’, w’)$ where $\mathcal{D}(\cdot)$ is a similarity measure?

•	Since the environment bank $\textbf{E}$ is learnable, how shall we initialize it?

•	Although the authors do an ablation study on the hyperparameters of CaTSG including number of environment embeddings $K$ and their dimension $H$, the search space appears to be quite limited. To be specific, how shall we choose $K$ and $H$ when there might exist more than one unobserved confounder?

•	Have you tried the Flow Matching solver for the denoiser?
- rating: 8 | confidence: 3

## Author comments / rebuttal
### Author comment
Dear Area Chair,

We would like to sincerely thank you for handling our submission and the reviewers for their constructive feedback. We have carefully revised the manuscript in response to all comments, and a concise summary of the main changes is provided in the **Global Response and Summary of Revisions** section. 

Please kindly let us know if any further clarification would be helpful!

Best regards,

Authors

### Author Response
We sincerely thank the the reviewer for the constructive and insightful comments. We appreciate the reviewer’s positive assessment of our work’s presentation quality and the clarity of our causal formulation. To address the feedback, we have submitted an updated version of the manuscript, with all revisions highlighted in red. Below, we address each point in detail.

**[Weaknesses]**

**W1.** It would be better to further discuss recent studies [1] and [2].

**A1.** We thank the reviewer for suggesting these related works, and we agree they are relevant. CausalDiffAE [1] learns causal representation learning for static image data, aiming to disentangle latent factors and generate counterfactual images via DDIM sampling. In contrast, our work focuses on time series generative modeling. The second work [2] estimates counterfactual outcomes under time-varying treatment, using inverse-probability weighting and plug-in conditional generators. In contrast, our work instead provides a unified causal diffusion framework directly for interventional and counterfactual time series generation. We appreciate the suggestion and have included them in the revised version (Line 129-132).

**[Questions]**

**Q1.** The rationale behind SwAV-style loss? Can we use SimSiam-style loss?

**A1.** Thank you for the question. Our goal in EnvInfer is to discover latent environments and output a soft assignment over $K$ environment embeddings that later control diffusion sampling. A SwAV-style loss is better aligned with this objective: it learns by predicting cross-view embedding assignments, which (i) induces discrete, controllable environment clusters (the env bank), (ii) encourages separability and balanced prototype usage (via assignment competition/Sinkhorn), and (iii) yields assignments that can be directly used for interventional/counterfactual generation. While a SimSiam-style loss aligns continuous features without online clustering and it does not explicitly form prototype-level structure, making environment identifiability weaker (post-hoc clustering would be needed). Therefore, SwAV-style loss is more suitable in our case.

**Q2.** Since the environment bank $E$ is learnable, how shall we initialize it?

**A2.** Thank you for pointing this out. The environment bank $E$ is initialized with orthogonal initialization to encourage diversity among environment embeddings, followed by L2 normalization along the feature dimension. We have clarified this initialization process to the revision (Line 1124-1125). Thank you!

**Q3**. How shall we choose $K$ and $H$ when there might exist more than one unobserved confounder?

**A3.** Thank you for the insightful comment. The latent environment variable $E$ is intended to represent an effective abstraction over **all** unobserved confounders. Accordingly, both $K$ and $H$ control the capacity of this representation. Therefore, if multiple unobserved confounders are expected, we recommend increasing both $K$ and $H$ to allow t

### Author Response (Part 2)
**Q2.** Have you considered using additional data or information to aid in learning the confounders, instead of using SwAV?

**A2.** Thank you for the suggestion. Our setting assumes the confounders $E$ are **unobserved** and complex, composed of many latent factors. Thus, supervised prediction of $E$ from $(X, C)$ is infeasible in this setting. The SwAV-style loss design enables the model to discover latent environments without labels, which better matches realistic scenarios where such annotations do not exist. Nevertheless, we agree with the reviewer that if certain confounders are observed, they can be used to supervise the environment bank learning. In this case, no major changes to the training or sampling pipeline are required, only the loss for the environment bank needs to incorporate the observed confounder features as supervision signals.

**Q3.** Have you considered an IPW formulation for the problem? 

**A3.** Thank you for the insightful question. Indeed, backdoor adjustment and IPW are two ways to adjust for confounding and recover interventional distributions $p(x \mid do(c))$. Our method adopts the backdoor view: we introduce a latent environment variable ($E$) to capture unobserved confounding and incorporate the adjustment directly into the score function, allowing the generative process itself to perform the causal sampling without estimating explicit propensity scores. Nevertheless, we agree that an IPW formulation is conceptually possible: estimating $p(e \mid c)$, computing weights $1/p(e \mid c)$, and reweighting the objectives. Propensity estimation may become unstable and lead to identifiability issues, which are especially problematic in diffusion-based generation. For these reasons, we chose a backdoor adjustment that naturally fits our generative framework. Exploring explicit IPW-based weighting could be an interesting complementary direction. Thanks for raising this point.

We sincerely appreciate the reviewer’s detailed comments and valuable suggestions. We hope that our responses and revisions address all raised questions, and we would be very happy to provide further clarification if needed.

### Author Response (Part 1)
We sincerely thank the reviewer for the thoughtful feedback. We are pleased that the originality of our approach, the use of environment-based conditioning and the overall empirical strength across four datasets were positively received. In response to the reviewer’s comments, we have uploaded a revised manuscript in which all modifications are marked in red for easy reference. Below, we address the reviewer’s comments and questions point by point.

**[Weaknesses]**

**W1.** More intuition should be provided regarding why the SwAV-style training task is well-suited for learning the environment.

**A1.** We thank the reviewer for this valuable comment. Intuitively, the SwAV-style loss encourages **agreement within the same environment** and **diversity across environments**: two augmentations of the same sample are encouraged to produce consistent environment assignments (capturing shared causal context), while the orthogonality regularization keeps different environment embeddings distinct. This consistency-under-augmentation principle aligns closely with the causal goal of discovering latent environmental factors that remain stable across perturbations. We have added this clarification to the revision (Line 1079-1107).

**W2.** Adopting the backdoor-adjusted approach requires learning additional components.  Possible experiments could involve using untrained or completely noisy environment variables to see how the model performs.

**A2.** We thank the reviewer for the thoughtful comment. We agree that the backdoor-adjusted method will introduce additional cost, mainly arising from learning environment-aware components, but this overhead is small since the number of environments $K$ is limited (typically 2–8). As detailed in Appendix G.2, we already report comprehensive efficiency results (e.g., parameter size, GPU memory, and throughput) showing that CaTSG achieves near-linear scalability with moderate additional cost. 

Regarding the suggested experiment with uninformative or random environments, this is provided in our ablation study (Figure 5a, Section 5.5), where variants such as RandEnv, FrozenEnv, and w/o Env simulate noisy, untrained or no-environment settings. The results clearly demonstrate performance degradation in these cases, validating both the necessity and robustness of the environment-based backdoor adjustment. Furthermore, Figure 5d examines the effect of environment dimension and complexity ($K$ and $H$), showing that performance remains stable over a broad range with only mild variation, indicating robustness to environment size and representation capacity.

**W3.** Causal methods typically target bias reduction. Usually, the trade-off is an increase in variance.

**A3.** We thank the reviewer for highlighting this important point. For the variance analysis, we performed the standard deviation of uncertainty metrics across multiple random seeds (reported in Table 2). In response to the reviewer’s suggestion, we added a visual

### Author Response (Part 3)
**Q2.** What modifications to the guidance rules would that entail for other causal graphs?

**A2.** We thank the reviewer for the question. Our guidance rule is obtained by taking $\nabla_x \log$ of the identification formula for $p(x∣do(c))$ and then deriving it to get the final score function (Eqs.25–30). Thus, to handle other causal graphs (e.g., mediators/front-door, IV), we can simply replace the backdoor expression in Eq.25 with the appropriate identification formula and then do the derivation to get the new score function for guidance.

**Q3.** What identifiability guarantees exist for the learned environments with finite $K$? Any recommended heuristics for choosing $K$ and $\omega$?

**A3.** We appreciate the question. Regarding identifiability under finite $K$, please refer to our responses to **W2**. For discussions on the practical selection and robustness of $\omega$, please refer to our responses to **W4**. Thanks!

**Q4.** How do you diagnose and handle limited overlap/positivity in $(C,E)$ ? Would you recommend reweighting, trimming, or curriculum strategies?

**A4.** Thank you for your question. We address this in two parts:

- Regarding diagnosis, Figure 6a visualizes the learned environment posterior across train/val/test splits, showing consistent usage of all $e_k$ without collapse or mode dropping. Figure 6b further confirms that the latent environment representations form well-separated, stable clusters across splits. These suggest sufficient marginal support for each $e_k$. While we do not explicitly enumerate joint $(C, E)$ combinations, the soft posterior $q(e \mid x, c)$ maintains high entropy under diverse contexts, providing indirect evidence of adequate overlap.
- Regarding strategies, given the above, we did not observe a need to apply additional weighting or scheduling strategies. However, we agree that such techniques could be beneficial in highly imbalanced regimes. If there is an extreme lack of overlap, we can consider pruning the data appropriately to ensure that the basic balance is maintained. If we want to cover all combinations, it can be achieved by trying weighted learning combined with curriculum-based training to balance bias and variance. Thank you.

We thank the reviewer once again for the thoughtful and constructive feedback. We hope our revisions and clarifications address all concerns, and we would be very happy to provide any additional explanations if needed.

### Author Response (Part 2)
**W4.** Robustness to the guidance scale $\omega$ could be probed.

**A4.** We thank the reviewer for raising the point. Indeed, guidance strength plays a key role in conditional diffusion models. In response to the reviewer’s suggestion, we conducted an additional sensitivity analysis across multiple $ \omega $ values (including {0.1, 0.2, 0.5, 1}), evaluated on Harmonic-VM and Air Quality, shown in the table below.

| $ \omega $  | Harmonic-VM (MDD) | Harmonic-VM (KL) | Air Quality (MDD) | Air Quality (KL) |
| --- | --- | --- | --- | --- |
| 0.1 | 0.077 ± 0.001 | 0.011 ± 0.001 | 0.081 ± 0.000 | 0.316 ± 0.003 |
| 0.2 | 0.098 ± 0.001 | 0.017 ± 0.000 | 0.069 ± 0.000 | 0.301 ± 0.001 |
| 0.5 | 0.169 ± 0.001 | 0.069 ± 0.002 | 0.092 ± 0.000 | 0.409 ± 0.003 |
| 1 | 0.243 ± 0.002 | 0.171 ± 0.001 | 0.101 ± 0.000 | 0.512 ± 0.002 |

As shown in the table, small values of $\omega$ (e.g., 0.2) yield the best or near-best scores across datasets, while larger $\omega$ amplifies the conditional signal at the cost of diversity, leading to over-regularized generations. This trend justifies our default choice of $\omega = 0.2$. We also added this analysis in the revision (Table 12, Appendix G.6).

**W5.** Expand baseline comparisons for the interventional and counterfactual settings.

**A5.** We appreciate the reviewer’s suggestion. We would like to clarify that since the generative tasks for time series are, to the best of our knowledge, introduced in this work, existing TSG baselines are not designed to address these tasks. Specifically, prior models do not provide a formal mechanism to incorporate interventional operations, and they lack a generative interface that supports conditioning in a way suitable for counterfactual sampling. As such, existing methods cannot be directly applied to these tasks without significant modifications. One of the central contributions of our work is the proposal of a new model, CaTSG, that supports these tasks. We thank the reviewer for the opportunity to clarify this.

**W6.** Clearer wall-clock and memory reporting would help practitioners gauge trade-offs.

**A6.** Thank you for the comment. We would like to clarify that, though we only included partial results in Section 5.5 due to space constraints in the main text, Appendix G.2 (Tables 7–8, Fig. 14) reports all related experimental results, including parameter size, memory, runtime, and throughput, demonstrating moderate overhead and near-linear scalability.

**W7.** Minor nitpicks.

**A7.** We thank the reviewer for the insightful comment.

- Regarding the direct edge $C \rightarrow X$, this edge in our running example indeed contains two components: (i) a genuine causal relationship (as correctly noted by the reviewer), and (ii) a spurious component driven by contextual factors such as the school calendar, which simultaneously affects $C$ and $X$ (as discussed in our example). The observed dependence is therefore a **mixture** of structural and confounded effects, and our

### Author Response (Part 1)
We sincerely thank the reviewer for the encouraging feedback. We are glad that the derivations, empirical study, clarity of presentation, and our unified treatment of observational, interventional, and counterfactual generation resonated with the reviewer. To respond, we have uploaded a revised version of manuscript, with all changes highlighted in red. Below, we address the reviewer’s concerns point by point.

**[Weaknesses]**

**W1.** Dependence on a fixed SCM can limit validity.

**A1.** We thank the reviewer for raising this point. In our work, given that our primary objective is to establish a clear formulation for causal time series generation, we adopt a fixed and relatively simple SCM to serve as a conceptual abstraction. This structure captures the most common case where latent environments confound the observed variables and allows us to define counterfactual sampling clearly. We agree that this assumption may be restrictive in scenarios involving feedback or more complex dependencies, and extending CaTSG to support dynamic or adaptive causal graphs is an interesting and valuable direction for future work.

**W2.** Finite environment bank and representation quality could leave residual confounding or introduce bias.

**A2.** Thank you for pointing this out. We agree that a finite environment bank may under-represent latent confounders, especially when $K$ or the embedding dimension is small. In our work, we adopt this design as a tractable and interpretable approximation of the latent confounding space. To mitigate under-specification, our framework includes:

- soft environment inference with probabilistic weighting $w_k$ to reduce the effect of hard mis-assignment;
- diversity-promoting regularization (e.g., orthogonality loss) to encourage diversity; and
- the swapped loss, which promotes environment consistency under augmentations and avoids collapse.

These mechanisms help ensure that even with moderate $K$, the environment bank captures a sufficiently rich set of latent confounders for effective adjustment.

Nevertheless, we agree with the reviewer that residual confounding may persist when the capacity is too limited. Exploring hierarchical or multi-factor environment models is a promising direction for future work. We appreciate the reviewer for pointing this out, and we have added this discussion in the revision (Appendix H.3). Thanks!

**W3.** Real-data counterfactuals lack ground truth for evaluation.

**A3.** We thank the reviewer for raising this important and well-recognized challenge. Indeed, counterfactuals on real-world datasets inherently lack ground-truth labels, which makes quantitative validation difficult. 

In respond, we reflected on how to better substantiate our claims in the absence of counterfactual labels. As an initial step, we added new measurements and introduced three complementary evaluation metrics: E-FTSD, Env-KL, and C-Consis. These metrics respectively assess (1) the alignment of generated and real 

### Global Response and Summary of Revisions
We sincerely thank all reviewers for their constructive and insightful feedback. According to reviewers, our work was praised for its originality (R2), clear and well-structured presentation (R1, R3), and strong methodological contribution, including the environment-based conditioning and causal score-guided diffusion (R1–R3). Reviewers also highlighted the thorough experiments across four datasets and the model’s consistent strong performance (R1–R3).

A revised manuscript has been uploaded, with all **modifications highlighted in red**. Below we summarize the revisions made in response to reviewers’ comments, organized by theme:

- **Experiments:** added preliminary real-data counterfactual evaluation (Appendix G.4, Table 11), variance analysis (Appendix G.5, Figure 15), and guidance coefficient sensitivity experiments (Appendix G.6, Table 12).
- **Clarifications:** added intuition behind the SwAV-style loss (Line 1079–1107), detailed environment bank initialization (Line 1124–1125), expanded the discussion on choosing $K$ and $H$ (Line 1558–1560), and added discussion on genuine vs. spurious relationships and the finite environment bank (Appendix H.3).
- **Related Work:** expanded discussion on relevant literature [1–3]
- **Figures & Presentation:** improved readability of Figure 3 and corrected a figure reference error in Section 4.1.

We hope these revisions address the reviewers’ concerns, and we sincerely appreciate the valuable feedback.

*(Here, R1 = Reviewer AVVu, R2 = Reviewer wJr5, R3 = Reviewer zSS3)*

[1] Xia, Tian, et al. "Decoupled Classifier-Free Guidance for Counterfactual Diffusion Models." arXiv preprint arXiv:2506.14399 (2025).

[2] Komanduri, Aneesh, et al. "Causal diffusion autoencoders: Toward counterfactual generation via diffusion probabilistic models." arXiv preprint arXiv:2404.17735 (2024).

[3] Wu, Shenghao, et al. "Counterfactual generative models for time-varying treatments." KDD. 2024.

### Causal Time Series Generation via Diffusion Models


## Meta review / decision
### Submission Desk Rejected by Program Chairs
This submission has manipulated the ICLR template to have smaller margins and must be desk rejected.

## PDF extracted text (first pages)
```text
000
001
002
003
004
005
006
007
008
009
010
011
012
013
014
015
016
017
018
019
020
021
022
023
024
025
026
027
028
029
030
031
032
033
034
035
036
037
038
039
040
041
042
043
044
045
046
047
048
049
050
051
052
053
Under review as a conference paper at ICLR 2026
CAUSAL TIME SERIES GENERATION VIA DIFFUSION MODELS
Anonymous authors
Paper under double-blind review
ABSTRACT
Time series generation (TSG) synthesizes realistic sequences and has achieved remarkable success.
Among TSG, conditional models generate sequences given observed covariates, however, such mod-
els learn observational correlations without considering unobserved confounding. In this work, we
propose a causal perspective on conditional TSG and introduce causal time series generation as
a new TSG task family, formalized within Pearl’s causal ladder, extending beyond observational
generation to include interventional and counterfactual settings. To instantiate these tasks, we de-
velop CaTSG, a unified diffusion-based framework with backdoor-adjusted guidance that causally
steers sampling toward desired interventions and individual counterfactuals while preserving obser-
vational fidelity. Specifically, our method derives causal score functions via backdoor adjustment
and the abduction–action–prediction procedure, thus enabling principled support for all three lev-
els of TSG. Extensive experiments on both synthetic and real-world datasets show that CaTSG
achieves superior fidelity while also supporting interventional and counterfactual generation that ex-
isting baselines cannot handle. Overall, we propose the causal TSG family and instantiate it with
CaTSG, providing an initial proof-of-concept and opening a promising direction toward more reli-
able simulation under interventions and counterfactual generation. Our source code is available at
https://anonymous.4open.science/r/CaTSG_iclr26.
.
1 I NTRODUCTION
Time Series Generation (TSG) aims to synthesize realistic sequences that preserve temporal dependencies and inter-
dimensional correlations, and is crucial for many applications, e.g., data augmentation (Ramponi et al., 2018), privacy
preservation (Yoon et al., 2020) and simulation for downstream tasks including classification and forecasting (Ang
et al., 2023). A significant extension, conditional TSG, generates sequences under given conditions, enabling con-
trolled synthesis (Yoon et al., 2019; Coletta et al., 2023; Narasimhan et al., 2024). In most implementations, condi-
tional TSG aligns generated data with the observational conditional P (X | C) using correlation-fitting objectives,
e.g., adversarial training in conditional Generative Adversarial Networks(GANs) (Yoon et al., 2019) and conditional
diffusion with denoising score-matching objectives (Narasimhan et al., 2024). However, these approaches remain fun-
damentally correlation-driven: they learn statistical associations between conditions and outcomes without modeling
the underlying data-generating mechanisms.
However, real-world time series systems are rarely governed by observed variables alone. Consider a transportation
example: a dataset contains observational pairs (X, C), where X is school-neighborhood traffic volume and C is
temperature (Figure 1a). In reality, unobserved variables E usually simultaneously affect both X and C (Figure 1b).
For instance, summer holidays can be one of theE, which often coincide with higher temperatures while also reducing
commuting demand, thereby acting as a latent common cause. Given such dataset, a typical conditional TSG model
pθ(X | C) (Figure 1c) cannot account for E and may thus unknowingly capture spurious correlations, e.g., learning
that “higher temperature causes lower traffic”. This limits their applicability in real-world decision-making, where
the goal may not be merely to replicate what happened, but to answer counterfactual queries such as: “What would
happen if we changed the condition within the same environment (i.e., with the latent factors held fixed)?”
Moving beyond purely observational modeling, we adopt a causal view that makes the mechanisms linking condi-
tions and outcomes explicit. Pearl’s causal ladder (Pearl, 2009) offers a precise vocabulary for this extension, which
organizes causal tasks into three levels: association, intervention, and counterfactual. Within this framing, classical
conditional TSG seeks to approximate the observational conditional P (X | C), and we refer to this setting as ob-
servational TSG (Obs-TSG), which occupies the association level. We then formulate causal time series generation
as an extension with two higher-level tasks: interventional (Int-TSG) and counterfactual TSG (CF-TSG), shown in
Figure 1d. Specifically, Int-TSG generates samples from P (X | do(C)), where do(·) denotes an intervention oper-
1
054
055
056
057
058
059
060
061
062
063
064
065
066
067
068
069
070
071
072
073
074
075
076
077
078
079
080
081
082
083
084
085
086
087
088
089
090
091
092
093
094
095
096
097
098
099
100
101
102
103
104
105
106
107
Under review as a conference paper at ICLR 2026
𝑋: Online Study Time
𝐶: Reminder Frequency
𝐸: Student Motivation
𝑡
𝐶
𝑡
𝑋
𝑡
𝐶
𝑡
𝑋
𝐸
𝐸
 𝐸 → 𝐶: Summer holidays often coincide with 
high temperature. 
𝐸 → 𝑋: Summer holiday reduce commuter 
traffic around school.
𝑝𝜃(𝑋|𝐶) 
High 𝐶 ⇒ Low 𝑋?
(
 Spurious correlation)
𝑝𝜃(𝑋|do(𝐶)) 
Confounders? Let me adjust for 𝐸. Given do(𝐶), 
generate 𝑋 for an average day in a year.
𝑝𝜃 𝑋′ 𝑋, 𝐶, 𝐶′
For a specific hot summer holiday 
(observed 𝑋 and 𝐶), what if  we had a 
lower 𝐶′?
Temperature (°C) Traffic Flow 
(vehicles/hr)
Summer Holiday
Sample 1
Working Day
𝑡
𝐶 𝑋
𝑡
𝑝𝜃(𝑋|do(𝐶)) 
𝑝𝜃 𝑋′ 𝑋, 𝐶, 𝐶′
𝑝𝜃(𝑋|𝐶) 
𝐶 𝑋
𝐸
Only consider 
observed data
Consider both observed and 
unobserved variables
(e) Generated time series under three scenarios
(c)  
(a) Dataset: Observed Data (𝑋, 𝐶)
Conditional 
TS Generation 
Interventional
TS Generation
Counterfactual
TS Generation
Association
𝑃 𝑋 𝐶
Intervention
𝑃 𝑋 𝑑𝑜(𝐶)
Counterfactual
𝑃 𝑋′ 𝑋, 𝐶, 𝐶′
⇒
Seeing: 
(But         )
High temp, Low traffic
⇒
Doing: 
Intervene
High temp, Traffic?
⇒
Imaging: 
Same Environment
Low temp, Traffic?
𝑪 𝑿
𝑬
𝑝𝜃(𝑋|𝐶) 
Conditional TSG Model
(b) Real World: Unobserved Factors (𝐸) 
Unobserved confounder E 
impact both X and C
Causal Time Series Generation
(d)  
Sample 2
Figure 1: Motivation for causal time series generation. (a) We observe time seriesX and C, (b) yet unobserved factors
E may affect both. (c) Standard conditional TSG risk learning spurious correlations. (d) We extend this paradigm into
a causal TSG family with Int-TSG and CF-TSG. (e) Three tasks yield distinct outputs given same C.
ation that sets C independent of its causes, thereby removing confounding effects from latent variables to simulate
outcomes. CF-TSG generates samples from P (X ′ | X, C, C′), producing personalized alternative trajectories by re-
placing C ′ for C while holding the realized environment fixed. Conceptually, the outcomes under these tasks differ
(Figure 1e): Obs-TSG (gray) may reflect spurious correlations with C; Int-TSG (red) shows adjusted outcomes free
from latent-factor influences, yielding more natural and diverse generations; CF-TSG (blue) depicts an individual’s
specific alternative trajectory.
While introducing Int- and CF-TSG expands conditional TSG toward decision-oriented synthesis, it also raises several
challenges: ground truth dilemma, invisible confounders, and evaluation difficulty. First, real-world time series often
originate from human systems (e.g., mobility, health), where running interventions is ethically and practically infeasi-
ble (Xia et al., 2025b), thus causal supervision is rare and most datasets are observational (Matthay & Glymour, 2022).
Second, confounders that simultaneously influence conditions and outcomes (e.g., individual difference and latent ran-
domness) are typically unobserved and complex, making it non-trivial to model or adjust for them. Third, evaluating
the quality of generated time series under these two tasks is difficult. Unlike images, time series lack reliable visual
inspection, and their quality depends on preserving subtle statistical patterns (Narasimhan et al., 2024).
To address these challenges, motivated by the growing adoption of diffusion models in time series practice (Ho
et al., 2020; Yang et al., 2024), we introduce a diffusion-based framework CaTSG (Causality-grounded Time Series
Generation). CaTSG employs backdoor-adjusted guidance to steer sampling toward interventional targets without
ground-truth interventional labels and a learnable latent environment bank with an EnvInfer module to flexibly model
latent confounders (Challenges 1 and 2). For Challenge 3, we complement real-world evaluations with SCM-grounded
synthetic datasets that expose observable counterfactuals, enabling quantitative assessment of CF-TSG. Our contribu-
tions are summarized as follows:
• Causal Expansion of Conditional TSG Paradigm. We formalize causal time series generation as an extension of
conditional TSG along Pearl’s ladder, introducing two tasks beyond association, i.e., interventional (Int-TSG) and
counterfactual (CF-TSG), to open up richer generative capabilities aligned with real-world decision-making needs.
• A Unified Causality-Guided Diffusion Framework. We derive causal score functions via backdoor adjustment
and abduction–action–prediction, and instantiateCaTSG to embed these principles into diffusion sampling. Through
backdoor-adjusted guidance and a learnable latent environment bank,CaTSG supports observational, interventional,
and counterfactual generation within a single framework.
• Comprehensive Empirical Evaluation. Across four datasets, CaTSG consistently improves observational fidelity
and achieves competitive interventional performance, outperforming the second-best baseline with relative gains of
2.4% - 98.7% across four metrics. For counterfactuals, CaTSG yields accurate CF generations on synthetic datasets,
supported by environment analyses, and reasonable CF results on real-world datasets via case-study visualizations.
2 B ACKGROUND
Conditional Time Series Generation. Conditional TSG aims to synthesize realistic time series that conform to
specified auxiliary information. Early methods like conditional GANs (Esteban et al., 2017; Smith & Smith, 2020)
2
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
Under review as a conference paper at ICLR 2026
conditioned on discrete labels, but suffered from instability and mode collapse (Chen, 2021). Recent works adopt
diffusion-based models (Sohl-Dickstein et al., 2015; Ho et al., 2020) with side information injected into the re-
verse process, enabling stable conditional generation (Tashiro et al., 2021). To handle heterogeneous metadata,
TimeWeaver (Narasimhan et al., 2024) extends diffusion to categorical, continuous, and time-varying inputs. Other
methods leverage structured state-space models (Alcaraz & Strodthoff, 2023), score-based transformers (Yuan & Qiao,
2024), or constrained objectives (Coletta et al., 2023). To improve adaptability across domains, recent efforts explore
prompt-based control (Huang et al., 2025), disentanglement of dynamics and conditions (Bao et al., 2024), and textual
guidance (Li et al., 2025). Consequently, diffusion models are currently a prevalent choice for time series genera-
tion (Yang et al., 2024; Narasimhan et al., 2024).
Diffusion Models & Score Function. Diffusion probabilistic models (Sohl-Dickstein et al., 2015; Ho et al., 2020;
Song & Ermon, 2019) define a generative process by reversing a fixed forward noising process. Diffusion models can
also be interpreted as score-based generative models (Song & Ermon, 2019), The score function estimates the gradient
of the log-density of noisy samples: st(xt) = ∇xt log p(xt). Under the Gaussian forward process, the data score
satisfies ∇xt log q(xt | x0) = − 1
σt
ϵ, σ t = √1 − ¯αt. Accordingly, learning to predict the noise is equivalent to
estimating the score up to a time-dependent scaling factor. In the conditional setting, the score becomes
st(xt, c) = ∇xt log p(xt | c) ≈ − 1
σt
εθ(xt, t, c), (1)
which links the denoising network directly to the conditional score function at each timestep. Note that due to the
space limitation, we put preliminaries with more detail in Appendix B.
Causal Modeling for Generation. Causal views recently integrated into deep learning tasks e.g., representation
learning (Yang et al., 2021), vision-language grounding (Wang et al., 2025), and anomaly detection (Xia et al., 2025c).
In generative modeling (Komanduri et al., 2023), it has been explored across several modalities. In vision, mod-
els like CausalGAN (Kocaoglu et al., 2018), CausalDiffAE (Komanduri et al., 2024) and Counterfactual Generative
Networks (Sauer & Geiger, 2021) enable interventions and recombinations of disentangled factors for counterfactual
image synthesis. In addition, it has also been used for time-varying treatment effects (Wu et al., 2024), and decoupled
classifier-free guidance further reduces spurious shifts during counterfactual sampling (Xia et al., 2025a). In text gen-
eration, structural causal models guide interventions on latent narrative factors (Hu & Li, 2021), while in knowledge
graphs, they have been leveraged to generate hypothetical relations that enhance link prediction (Liu et al., 2021).
Despite these advances, causal modeling for generation remains largely unexplored in time series.
3 A C AUSAL VIEW FOR CONDITIONAL TIME SERIES GENERATION
Traditional approaches to conditional TSG focus solely on observational correlations. To move beyond, we adopt
a causal perspective and situate this generative task within Pearl’s causal ladder (Pearl, 2009), thereby motivating a
structured view across different causal levels.
Causal Ladder for TSG. Pearl’s Causal Ladder organizes reasoning into three levels: association, intervention, and
counterfactual. We adapt this hierarchy to the context of TSG, summarized in Table 1. Level 1 (association) captures
statistical correlations between observed contextual variables C (e.g., temperature) and the outcome X (e.g., traffic);
Level 2 (intervention) models the outcome under controlled changes to C while adjusting for potential confounding
from unobserved common causes; and Level 3 (counterfactual) simulates alternate outcomes X ′ had C been different,
given the observed sample X and C. This structured perspective enables us to unify and extend TSG tasks along the
causal hierarchy.
General Problem Statement. Let D = {(x, c)}N
i=1 denote a dataset consisting of N samples of multivariate time
series x ∈ RT ×D and paired contextual sequences c ∈ RT ×Dc. Each x = [x1, . . . ,xT ] represents a length-T time
series over D dimensions, and c contains auxiliary features in the same time span with dimension Dc. Our goal is
to learn a generative model Fθ such that the samples generated from Fθ(c) match a target distribution of the form
P (x⋆ | I ), where the form of the conditioning variable I determines the underlying generation task. Specifically, we
consider:
• Observational TSG (Obs-TSG): P (x | c), the standard conditional time series generation task;
• Interventional TSG (Int-TSG): P (x | do(c)),which simulates outcomes under an intervention on c, where the
do(·) operator sets c independent of its causes;
• Counterfactual TSG (CF-TSG): P (x′ | x, c, c′), which simulates an alternative outcome under a counterfactual
context c′ given an observed realization (x, c).
This causal view elevates conditional TSG from a purely observational setting to a principled hierarchy of generative
tasks. We refer to the latter two settings ascausal time series generation, as they go beyond observational associations
and involve reasoning over interventions and structured counterfactuals.
3
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
Under review as a conference paper at ICLR 2026
Causal Level Description Example in Transportation 1 Time Series Generation Task
Level 1:
Association
Seeing: Observe statis-
tical correlations
High temperature ⇒ Low traffic flow
(! May capture spurious correla-
tions, because both may be caused by
summer holiday)
Obs-TSG: P (X | C)
Generate time series X under condition
C
Level 2:
Intervention
Doing: Generate un-
der controlled change
of variables
Generate traffic flow when we set
temperature = high, regardless of
summer or not
Int-TSG: P (X | do(C))
Generate time series X given C, free
from unobserved common causes
Level 3:
Counterfactual
Imagining: Ask “what
if” on a real sample
Observed traffic flow on a hot sum-
mer holiday ⇒ what would the coun-
terfactual traffic flow have been if the
same holiday had been cool instead?
CF-TSG: P (X ′ | X, C, C ′)
Given observed (X, C), generate what
X ′ would look like under C ′
Table 1: Three levels of TSG following the causal ladder (Pearl, 2009). Color indicates semantic roles of variables:
blue for generated outcomes X, red for observed condition C, green for counterfactual condition C ′, yellow for
counterfactual outcomes X ′, and gray for latent or unobserved confounders (e.g., summer holiday).
4 M ETHODOLOGY
To instantiate Fθ for the causal generative tasks, we first introduce a unified Structural Causal Model (SCM) (Pearl
et al., 2000) as the theoretical foundation (Figure 2). We then derive the interventional and counterfactual objectives
using two classical tools (Pearl et al., 2016): backdoor adjustment for Int-TSG and abduction–action–prediction
procedure for CF-TSG. Given that diffusion models (Ho et al., 2020) have become a powerful technique for time
series modeling with strong performance and stable training (Yang et al., 2024), we adopt diffusion as the backbone.
Guided by the causal principles, within the diffusion framework, we derive a causal score function that guides the
sampling process, and introduce CaTSG (Figure 3), a generative model that instantiates causal objectives in practice.
4.1 SCM & C AUSAL TREATMENTS
Beyond the no-confounding assumption of Obs-TSG (Figure 2a), we consider an SCM that captures the causation
among observed sequences X, contextual variables C, and unobserved environment factors E (Figure 2b), that sup-
ports the identification of interventional and counterfactual distributions.
Backdoor Adjustment for Int-TSG (Figure 2c). To estimate the interventional distribution P (X | do(C)), we apply
the backdoor adjustment (Pearl et al., 2016), which controls for confounding by conditioning on the appropriate set of
variables that block all backdoor paths from C to X, i.e., C ← E → X. The interventional distribution can thus be
approximated via (full derivation in Eq. 9):
P (X | do(C)) =
X
e
P (X | C, E = e) P (E = e) (2)
Abduction–Action–Prediction (AAP) for CF-TSG (Figure 2d). To estimate the counterfactual distribution P (X ′ |
X, C, C′), which asks “what would the outcome X ′ have been if C had been C ′ instead,” we adopt the three-step
procedure (Pearl et al., 2016):
• Abduction: Infer the posterior over latent environment E from the observed sample (X, C), i.e., estimate P (E |
X, C). This step captures the specific environment in which the observed data occurred.
• Action: Replace the observed C with a counterfactual value C ′ by simulating an intervention, i.e., modify the SCM
by applying do(C = C ′).
• Prediction: Generate the counterfactual outcome X ′ based on the modified SCM and the inferred E, yielding
P (X ′ | do(C ′), E).
For example, in the transportation scenario, suppose we observe low traffic flowX on a hot day C. We first infer that
the latent environment E likely corresponds to a summer holiday based on our observationX and C 
```
