# CauKer: Classification Time Series Foundation Models Can Be Pretrained on Synthetic Data — OpenReview Raw Thread

- Forum: https://openreview.net/forum?id=xBW2FIfswU
- PDF: https://openreview.net/pdf?id=xBW2FIfswU
- Section: 一、时间序列生成：因果性、多样性与领域适配
- Zhihu score: 6.0
- Venue status: ICLR 2026 Oral

## Submission metadata
- Authors: Shifeng Xie, Vasilii Feofanov, Jianfeng Zhang, Themis Palpanas, Ievgen Redko
- Primary area: learning on time series and dynamical systems
- Keywords: Time Series Foundation Model, Time Series Classification

## Abstract
Time series foundation models (TSFMs) have recently gained significant attention due to their strong zero-shot capabilities and widespread real-world applications. Such models typically require a computationally costly pretraining on large-scale, carefully curated collections of real-world sequences. To allow for a sample-efficient pretraining of TSFMs, we propose CauKer, a novel algorithm designed to generate diverse, causally coherent synthetic time series with realistic trends, seasonality, and nonlinear interactions. CauKer combines Gaussian Process (GP) kernel composition with Structural Causal Models (SCM) to produce data for sample-efficient pretraining of state-of-the-art classification TSFMs having different architectures and following different pretraining approaches. Additionally, our experiments reveal that CauKer-generated datasets exhibit clear scaling laws for both dataset size (10K to 10M samples) and model capacity (1M to 783M parameters), unlike real-world datasets, which display irregular scaling behavior.

## Reviews
### Reviewer_Ztoq
- summary: This paper proposes CAUKER, a synthetic data generation framework combining Gaussian Process kernel composition and SCM for time series foundation models for classification tasks. Unlike most prior work focusing on forecasting, CAUKER targets classification and demonstrates that synthetic pretraining can yield competitive or superior performance to real world datasets. It also reveals scaling laws for synthetic pretraining in terms of dataset and model size.
- strengths: * Addresses a clear gap, synthetic pretraining for classification TSFMs.
* The causal kernel composition is conceptually elegant and well motivated.
* Benchmarks across multiple models and datasets .
* Includes scaling law analyses for data, model, and compute.
* Outperforms real-data pretraining in several zero-shot setups.
* The method is explained clearly, with schematic diagrams and pseudocode.
- weaknesses: * Both GP based and SCM based data generation already exist, the novelty lies mostly in combining them.
* Evaluation confined to zero-shot classification. would benefit from downstream fine-tuning or transfer learning results.
* The contribution of causal graph depth/branching remains unclear.
* While interesting, the scaling analysis is somewhat descriptive without deeper theoretical grounding
- questions: * How does CAUKER handle multivariate dependencies beyond univariate channel concatenation?

* Can CAUKER generalize to forecasting or imputation pretraining tasks?

* How computationally expensive is CAUKER compared to kernel only methods?
- rating: 8 | confidence: 4

### Reviewer_uHPf
- summary: The manuscript presents CAUKER, a synthetic data generation pipeline for pretraining classification time-series foundation models. CAUKER composes Gaussian-process kernels and mean functions within a structural causal model (SCM) graph, producing causally coherent sequences for self-supervised pretraining of contrastive (Mantis) and masked-reconstruction (MOMENT) encoders. Empirically, models pretrained solely on CAUKER data achieve competitive zero-shot accuracy on UCR and exhibit monotonic scaling with both dataset size and model capacity.
- strengths: 1. Integrating kernel composition with SCM-based propagation yields diverse dynamics and inter-series dependencies aligned with classification objectives.
2. Evaluation across contrastive and masked-reconstruction pretraining objectives increases the generality and external validity of the findings.
3. Experiments demonstrate data/model scaling laws and strong zero-shot transfer, offering a compelling empirical performance.
- weaknesses: 1. Pretraining on pure synthetic data and obtaining strong results is not particularly surprising, as prior work (e.g., TabPFN-TS) has already demonstrated the potential of synthetic data. This manuscript would benefit from sharper positioning of what is substantively novel in methodology part. 
2. This paper does not clearly articulate the challenges in transferring synthetic data generation methods designed for forecasting tasks to classification tasks—what the specific difficulties are and how they are addressed. The introduction reads largely as an integration of existing generators applied to classification, with empirical observations such as scaling laws, but as a research contribution this positioning feels insufficient.
3. The evaluation scope remains narrow (largely UCR-style, often univariate and fixed-length), with limited robustness analysis on generator hyperparameters and little evidence for multivariate, irregularly sampled settings.
- questions: 1. What are the concrete, theoretically grounded challenges when porting forecasting-oriented synthetic pipelines to classification (label generation, class balance, inter-class separability, invariance desiderata), and how does each CAUKER design choice mitigate them?
- rating: 4 | confidence: 4

### Reviewer_Mojr
- summary: This paper proposes CAUKER, a novel and sophisticated pipeline for generating synthetic time series data specifically tailored for the pre-training of classification-oriented Time Series Foundation Models (TSFMs). The core idea is to combine two methodologies: Gaussian Process (GP) kernel composition, which generates realistic temporal patterns (trends, seasonality), and Structural Causal Models (SCMs), which impose a causal graph structure to create complex, non-linear interactions and meaningful clusters. The authors conduct extensive experiments showing that TSFMs pre-trained on CAUKER data
- strengths: *   **Novelty and Formulation:** The primary strength of this work is its well-motivated. Rather than creating a monolithic generator, the authors identify two key requirements for classification data—realistic temporal dynamics and discriminative clustering structure—and solve them by combining the strengths of two distinct fields. Using GP kernel composition (common in forecasting) for temporal patterns and SCMs (from the causality and tabular learning literature) for creating underlying class
- weaknesses: I have concerns about the evaluation process and specially related to the complexity of the proposed generator, the framing of its comparison to real-world data, and the scope of the architectural evaluation.

1.  **High Generator Complexity and Opaque Design Choices:** The CAUKER pipeline is a complex amalgamation of multiple components: three distinct function banks (kernel, mean, activation), random kernel composition, and random DAG generation. This introduces a large number of "meta-hyperparameters" (e.g., the specific contents and size of the banks, the distribution of DAG parameters). While the appendix provides a sensitivity analysis for a few of these, the process for designing the function banks themselves is not fully justified. It is unclear if the chosen set of 36 kernels or the specific activation functions are uniquely effective, or if a much simpler subset could achieve comparable results. This complexity could pose a significant barrier to adoption and reproducibility 
- questions: Based on these weaknesses, here my questions to the authors:

*   **Question 1:** The CAUKER pipeline is composed of several stochastic modules and expertly curated function banks. How were the specific contents of these banks (e.g., the 36 kernels, the set of mean/activation functions) selected and validated? Is the performance highly sensitive to these specific choices, or is the framework robust to using a simpler, more generic set of components?

*   **Question 2:** The hyperparameter sensitivity analysis in Appendix C.3 is helpful. However, to better understand the generator's failure modes, have you investigated scenarios where deliberately poor choices (e.g., using only linear activations, forcing very shallow DAGs, or using only a single kernel type) cause the method to fail or deg
- rating: 6 | confidence: 5

### Reviewer_zLKs
- summary: The authors propose CAUKER, a synthetic data generation algorithm that leverages Gaussian Process kernel composition and Structural Causal Models to produce diverse time series for augmenting training data in time series classification tasks. The paper evaluates the proposed approach against other synthetic data generation techniques for several time series foundation models.
- strengths: - The paper introduces a novel synthetic data generation technique leveraging structural causal models (SCMs) for time series.
- The work is a focused study on synthetic data augmentation for time series classification, an understudied area in time series literature.
- Two time series foundation models (TSFMs) are evaluated with supervised and contrastive learning pre-training schemes
- Several synthetic data augmentation approaches are systematically compared in Table 1, highlighting relative e
- weaknesses: I would be happy to increase my score if the following concerns/points are addressed.

- Zero-shot evaluation methodology: The study claims to evaluate TSFMs in a zero-shot setting, but the models are allowed to be pre-trained on the training set of the same dataset used for evaluation. This means the evaluation is not strictly zero-shot, as the train and test sets are likely in-distribution (Lines 122–124): “In practice, if we evaluate a given TSFM on a test set from a UCR (Dau et al., 2019) dataset, we ensure that the TSFM was not pre-trained on it, but we allow for the train set of this same dataset to be used for pre-training.” 

- Missing baseline comparisons: Results without synthetic data augmentation are not reported in Table 1. Including these and quantifying the lift from augmentation would be helpful.

- No text-based or experimental comparison with the synthetic data generation process used by TabPFN, which also leverages structural causal models.

- No comparison with non-
- questions: 1. Are the TSFMs pre-trained from scratch on synthetic data, or are they fine-tuned on synthetic data (using models already pre-training on real data)?
2. How do the models perform without any synthetic data augmentation?

Suggestion: It would be interesting to include the combined scaling laws for the UEA and Cauker datasets on the same plot in Figure 3 to show cross-dataset scaling laws.
- rating: 6 | confidence: 4

## Author comments / rebuttal
### Author comment
We would like to sincerely thank the AC for their efforts in handling the unexpected situation around the rebuttal process, and all reviewers for their thoughtful comments.

Reviewer **Ztoq** (score 8) was very positive about the work, highlighting the contribution and experimental design. In response to their questions, we clarified how CauKer handles multivariate structure conceptually, explained the extension to forecasting and added a detailed runtime breakdown showing that the SCM component introduces negligible computational compared to GP sampling.

Reviewer **zLKs** initially raised concerns mainly about the exact “zero-shot” protocol. We clarified the pretraining and evaluation pipeline, and added non-foundation baselines. After these clarifications and additions, their score was raised from 6 to 8.

With Reviewer **Mojr** (score 6), we had a very constructive exchange. In response to their questions about generator complexity, failure modes, and real-data scaling, we (i) described the design of the kernel/mean/activation banks, (ii) added new ablations where CauKer is forced to use only a single kernel family, (iii) discussed why UEA is not an ideal large-scale pretraining corpus and how CauKer can act as a scalable alternative, and (iv) added attention-rollout visualizations. The reviewer explicitly stated that these additions fully addressed their questions and “made the paper even stronger”.

Reviewer **uHPf** (score 4) focused on the specific challenges of moving from forecasting to classification. We clarified the methodological differences between forecasting-oriented generators and classification-oriented data (role of non-zero mean functions and SCM mixing for discriminative patterns), sharpened the positioning with respect to TabPFN-style synthetic pretraining. We also extended the evaluation to irregular multivariate clinical benchmarks and fine-tuning experiments on UCR. Following their follow-up comment on wording of P19 dataset evulation, we also replaced the phrase “slightly worse” with the exact number. While we have not received further comments from the reviewer, to the best of our understanding, all the raised issues have been addressed in our response.

Overall, our contribution is to demonstrate that a carefully designed causal-kernel synthetic generator (CAUKER) can pretrain classification TSFMs purely on synthetic data, achieving competitive zero-shot performance and clear data/model scaling laws while greatly reducing reliance on large real-world corpora. 

We once again thank the AC for their careful consideration of our work and for their efforts in guiding the review process under these exceptional circumstances.

### Authors’ follow-up reply
We thank the reviewer for the clarification.

On the P19 dataset, the AUPRC changes from 0.5368 to 0.5005, which corresponds to an absolute decrease of 3.63%. Because AUPRC is bounded within the [0,1] interval, we compared model performance in absolute terms. To the best of our knowledge, reporting relative percent changes (in this case, 6.8% as the reviewer correctly notes) is not commonly used for [0,1]-bounded metrics such as AUPRC, although it is indeed relevant for unbounded or scale-sensitive metrics.

Nevertheless, we agree with the reviewer that the phrasing “slightly worse” is not sufficiently precise. In the revised version, we replace this wording with the exact numbers in the performance as mentioned above. 

We appreciate the reviewer’s attention to the precision of the description. Importantly, this adjustment affects only the wording and does not change the interpretation of the experimental findings: the CauKer-pretrained model remains competitive across the large-scale experimental study, in both regular and irregular time series settings.

Finally, we would like to confirm whether the reviewer has any remaining concerns regarding the methodology, experimental setup, or the newly added irregular-time evaluations. We are fully open to further suggestions.

### Authors' reply (part 2/2)
---


### Weakness 3: evaluation scope and irregular/multivariate settings

---

We agree that broadening the evaluation scope is important. UCR is currently the de facto benchmark for time series classification, which is why it plays a central role in our study. Nevertheless, we would like to note that the original manuscript already includes additional experiments on the multivariate WOODS benchmark. We have not included irregularly sampled sequences in the initial version because the public implementations of TSFMs assume regularly sampled inputs.

Following the reviewer’s suggestion, we further evaluated Mantis on two irregular, multivariate clinical benchmarks (P12[1] and P19[2]), using the same frozen encoder, zero-shot protocol. We compare the original Mantis checkpoint (1.89M real data pretraining) with Mantis pretrained on CauKer-100K and CauKer-1M:

| Dataset | Model                         | AUROC  | AUPRC  | 
| ------- | ----------------------------- | ------ | ------ | 
| P12     | Mantis (real-data)            | 0.8121 | 0.4340 | 
| P12     | Mantis (CauKer-100K)          | 0.7984 | 0.4276 | 
| P12     | Mantis (CauKer-1M)            | 0.8189 | 0.4592 |
| P19     | Mantis (real-data)            | 0.8846 | 0.5368 | 
| P19     | Mantis (CauKer-100K)          | 0.8534 | 0.4954 |
| P19     | Mantis (CauKer-1M)            | 0.8709 | 0.5005 |


On both irregular clinical tasks, the CauKer-1M model achieves strong AUROC and AUPRC performance, outperforming Mantis on P12 and being slightly worse on P19. These results support that CauKer pretrained TSFMs remain competitive beyond UCR, regularly sampled benchmarks, and can transfer to irregular settings as well. We've added these new results to Appendix N and referenced them on page 9.

[1] Goldberger, A. L., Amaral, L. A., Glass, L., Hausdorff, J. M., Ivanov, P. C., Mark, R. G., Mietus, J. E., Moody, G. B., Peng, C.-K., and Stanley, H. E. Physiobank, physiotoolkit, and physionet: components of a new research resource for complex physiologic signals. circulation, 101(23): e215–e220, 2000.
[2] Reyna, M. A., Josef, C., Seyedi, S., Jeter, R., Shashikumar, S. P., Westover, M. B., Sharma, A., Nemati, S., and Clifford, G. D. Early prediction of sepsis from clinical data: the physionet/computing in cardiology challenge 2019. In 2019 Computing in Cardiology (CinC), pp. Page–1. IEEE, 2019.

----
Once again, we thank the reviewer for the careful assessment and constructive suggestions. We hope that our clarifications, additional experiments, and repositioning of the contributions address the raised concerns. All corresponding changes have been incorporated into the revised manuscript and are highlighted in **brown** for ease of reference. We remain fully open to further questions or suggestions that could help improve the work.

### Authors' reply (part 1/2)
We thank the reviewer for the careful reading of our work and for the thoughtful comments. We respond to the main weaknesses and the question below.

---

### Weakness 1: novelty of synthetic pretraining on pure synthetic data

---

Although the results obtained by TabPFN were our source of inspiration, we would respectfully disagree that the strong performance we achieved by pure synthetic pretraining "is not surprising". First, we would like to note that there does exist a difference between forecasting and classification methodology, which makes the transfer from one field to another subtle. We will discuss this in the response to Weakness 2. 

Second, even in the forecasting community, the question of whether purely synthetic pretraining can match large real data corpora remains an active debate. For example, Chronos explicitly showed that synthetic-only pretraining leads to suboptimal performance. In their second version of the model (Chronos-2, October 2025), they reconfirmed it, emphasizing the need for large real-world corpora to reach the top of forecasting leaderboards. As for TabPFN-TS and ForecastPFN, their performance today is quite far from the most recent forecasting TSFMs (see GIFT-Eval leaderboard), and only very recent TempoPFN (October 2025) manages to be close to the forecasting state-of-the-art.

---

### Weakness 2 and Question: Forecasting and classification synthetic data

---

First, we would like to note the inherent difference between forecasting and classification data. A typical forecasting-oriented dataset emphasizes global or low-frequency structure: trends, seasonality, and the governing dynamical equations. Classification-oriented data usually relies more on local or high-frequency cues: spikes, abrupt changes, short behavior, and texture-like patterns. This naturally causes the use of different (pre-)training objectives, pretraining corpora, and hidden implementation details.

Forecasting generators such as KernelSynth mainly focus on zero-mean GP samples that highlight smooth extrapolation of trends and seasonality, lacking high-frequency information. To overcome this and generate classification-oriented data, we propose two changes: (a) we add a mean function library that explicitly includes anomaly-like and spike-like patterns, so that class-discriminative signals can be carried in the mean level and local patterns, (b) we incorporate the SCM that introduces nonlinear mixing and local interactions across nodes, which can partially “break” the global smoothness imposed by the GP and create cluster structure between series. In Section 4.1 and Appendix D, we empirically show that both the non-zero mean functions and the SCM component are important.

Another difference that is important to note is that classification foundation models like Mantis are based on a contrastive pre-training strategy used solely for classification. By conducting this research, we have found that synthetic data is particularly relevant f

### Authors' reply (part 2/2)
---

### Question 4. Interaction with non-Transformer architectures

---
We share the reviewer’s interest in how CauKer would interact with models that have different inductive biases.

Recent successes such as Tirex and TempoPFN suggest that non-Transformer TSFMs (e.g., xLSTMs or RNN-like architectures) can be highly competitive. However, in the classification TSFM setting, all existing foundation models we are aware of are Transformer-based. The reviewer’s example InceptionTime is indeed a strong CNN-based classifier, but it is supervised and not straightforward to adapt into a self-supervised, large-scale foundation model.

Given that TiRex already uses kernel-based synthetic data and achieves excellent results, we are optimistic that CauKer-style data would also be beneficial for xLSTM- or SSM-based TSFMs. Unfortunately, Tirex’s full training code is not yet publicly available, which prevented us from including such experiments in this version. 

---

### Question 5. GP vs. SCM and the role of attention

---

We thank the reviewer for this insightful question. To probe how CauKer’s structure interacts with attention, we applied Attention Rollout to visualize the layer-aggregated attention maps of Mantis trained on CauKer-100K versus the original Mantis （trained on 1.89M real data）. As shown in the updated Appendix L, the CauKer-pretrained model exhibits sharper and more localized attention maps, assigning higher importance to short subsequences that carry clear discriminative patterns, whereas the real-data model tends to produce more diffuse attention. 

---

### Question 6. The relation between classification and forecasting data

---
Our Chronos experiments use exactly the same CauKer pipeline, without any task-specific modifications.

Concerning whether “good classification data is a superset of good forecasting data”, we find this question not trivial. On the one hand, forecasting models such as Chronos and TimesFM often include classification-type signals or tasks in their training mixtures and empirically benefit from them, which suggests that some of the structure useful for classification is also valuable for forecasting. Our results show that Chronos models pre-trained solely on 0.5B CauKer timepoints can match the zero-shot performance of models trained on 84B real tokens, indicating that CauKer-generated data is also well suited for forecasting.
On the other hand, forecasting places additional emphasis on long-horizon temporal coherence and extrapolation. For this reason, we prefer not to make the strong claim that “good classification data is a strict superset of good forecasting data”. Instead, our current conclusion is: the same CauKer pipeline appears to provide a high-quality training signal for both tasks. 

---
Once again, we sincerely thank the reviewer for the thorough reading and the high-quality, thought-provoking questions. We have incorporated the corresponding changes into the revised manuscript, where all updates re

### Authors' reply (part 1/2)
We thank the reviewer for the very professional and insightful questions, and we are glad to have the opportunity to discuss them.

---

### Question 1. Function-bank design and sensitivity

---

Our kernel bank currently contains 36 kernels drawn from five families: ExpSineSquared, DotProduct, RBF, RationalQuadratic, and WhiteKernel. Each family is chosen to capture a distinct aspect of time-series behavior:

- ExpSineSquared: periodic structure,
- DotProduct: linear trends,
- RBF: smooth functions with local correlations,
- RationalQuadratic: mixtures of length scales behavior,
- WhiteKernel: noise components.

Within these families, hyperparameters are chosen to encode realistic patterns and scales. For example, ExpSineSquared kernels include periods corresponding to 24 hours and 60 minutes, which we found useful for mimicking common real-world seasonality patterns.

We also experimented with adding Matérn kernels or ExpSineSquared variants kernels, but did not observe consistent performance gains. An important point is that CauKer randomly samples a small number of kernels from the bank for each composite GP, so enlarging or slightly modifying the bank does not increase computational cost. The current 36-kernel configuration is used as a practical default.

---

### Question 2. Deliberately poor design choices and failure modes

---
We thank the reviewer for this original and helpful question. Our kernel bank consists of five kernel families; here, we report an experiment where we force CauKer to use only a single kernel family (plus SCM) to generate 100K samples for Mantis pre-training. The average test accuracies on UCR (also added in Appendix C, p. 19) are:

| Kernel family (single-kernel CauKer) | UCR test accuracy |
| ------------------------------------ | ----------------- |
| DotProduct (linear)                  | 0.7679            |
| RBF (smooth)                         | 0.7807            |

DotProduct-only GPs can generate essentially linear trends; even after SCM nonlinear mixing, the resulting data are too simple, and performance degrades substantially. In contrast, RBF-based smooth curves combined with SCM still yield acceptable performance, confirming that kernel diversity and sufficiently rich nonlinear structure are important. When the SCM is made very shallow, the generator effectively collapses towards a kernel-only model; this degradation pattern is consistent with the ablations reported in Section 4.1.

---

### Question 3. Real-data scaling, especially UEA

---

We thank the reviewer for raising this interesting question. 
In our view, the poor scaling behavior on UEA arises from several concrete properties of currently available real classification corpora:

- UEA was proposed before the "foundation model era" with the goal to provide a collection of multivariate classification datasets, so their combination of datasets can be suboptimal for the pre-training task.
- It is highly imbalanced as the sample size of datasets

### Authors' reply
We thank the reviewer for the very positive and constructive assessment of our work and for the helpful questions and suggestions. Below, we address the questions and clarify the corresponding weaknesses.

---

### Q1. Multivariate dependencies beyond channel concatenation

---

In CauKer, time series sampled from a single SCM (one channel per node) can be interpreted as different channels that share a common causal structure. While in this paper, we restrict the pre-training to univariate inputs because both Mantis and MOMENT are pre-trained in the univariate setting (each channel is treated as an individual series), we believe that CauKer is also well-suited to multivariate pre-training in classification. We added a paragraph to the revised PDF to elaborate on this (end of page 4).

We agree that leveraging explicit multivariate dependencies is an important next step, especially to take into account exogenous variables (as in forecasting TSFM Chronos-2) and leave this for future work. 

---

### Q2. Generalization to forecasting/imputation pretraining

---

We already explored the extension of CauKer beyond classification in Section 4.4 (Extension to forecasting): We pre-train Chronos exclusively on 0.5B timepoints of CauKer-generated time series. The resulting models achieve zero-shot forecasting accuracy that is statistically indistinguishable from the original Chronos models trained on 84B timepoints of mixed real + synthetic data.

This suggests that the same CauKer pipeline, without tuning, can be used as a sample-efficient pretraining source for forecasting TSFMs. Our preliminary results indicate that CauKer can become a drop-in replacement for KernelSynth used previously in the pre-training of TSFMs.

In this submission, we did not explicitly evaluate imputation tasks, which can be a good subject of future work. Conceptually, imputation tasks have similarities with both forecasting (periodical behavior) and classification (non-linear dependencies, spikes). Given that CauKer works well both for classification and forecasting pre-training, it is reasonable to try it for imputation as well.

---

### Q3. Computational cost comparison with kernel-only generators

---

To quantify the computational overhead of introducing SCM structure, we compared CauKer to a simple GP kernel-only（KernelSynth）baseline under the same setting. For CauKer, we use SCMs with 10 nodes, a maximum in-degree of 4, and we sample 5 nodes per SCM to obtain the final univariate series.

The end-to-end wall-clock times are:

| Method                 | Series | Length | Time (s) |
|------------------------|----------|--------|-----------------|
| CauKer                 | 1,000    | 512    | 121.64     |
| Simple GP              | 1,000    | 512    | 182.25    |

We also break down the internal timing of CauKer:

| Component                   | Time (s) | 
|-----------------------------|----------|
| Simple GP                   | 118.54   | 
| SCM structure + propagation | 

### Authors' response
We thank the reviewer for constructive suggestions. Below, we clarify the experimental protocol and address each concern.

---

 ### 1. Clarifying the “zero-shot” evaluation and pre-training protocol (Weakness 1, 2, 5 and Question 1, 2)

---
We apologize for the confusion created by the current wording in Section 3.1.

* In all experiments that involve CauKer, the pre-training corpus consists *only* of CauKer-generated synthetic time series.
* The **TSFM is always used as a frozen encoder** during evaluation: given a downstream dataset $D = {(x_i, y_i)}$, we compute embeddings $z_i = F(x_i)$ with a frozen TSFM $F$, then train a lightweight classifier $h$ (Random Forest for Mantis, SVM for MOMENT) on the training split embeddings only, and report accuracy on the disjoint test split. Thus, in the evaluation pipeline, the TSFM acts purely as a frozen feature extractor.

Taking Section 4.4 as an example:

* We **pre-train Mantis from scratch** on 100K CauKer time series samples and evaluate on UCR. This yields an average accuracy of 78.55%, and is strictly out-of-distribution, since the encoder has never seen UCR or other real-world classification datasets during pre-training.
* For comparison, we also report the original Mantis model pre-trained on its official 1.89M-samples corpus, which includes UCR training sequences (but **no labels and no UCR test data**). This model achieves 78.66% on UCR, which is therefore an in-distribution no-leakage test.

In the revision, we explicitly separate OOD zero-shot results (our CauKer pre-trained models) from in-distribution results (original Mantis and MOMENT checkpoints whose pre-training corpora contain UCR train splits) and clarify this distinction in Section 3.1 and Section 4 of the updated PDF.

We believe this directly addresses Weaknesses 1, 2, 5, and Questions 1, 2. We would be pleased to provide any additional clarification that may be deemed necessary.

---

### 2. Relation to TabPFN and the SCM baseline (Weakness 3)

---

We thank the reviewer for pointing out the connection to TabPFN.

As the official code for SCM is not available, the “SCM” synthetic corpus in Section 4.1 refers to our re-implementation of the structural causal generator introduced in TabPFN. As we emphasize in the text, this generator does not model temporal dependencies but concentrates on correlating the covariates. This explains why it underperforms the time series aware generators in Table 1.

We hope this addresses Weakness 3.

---

### 3. Non-foundation model baselines (Weakness 4)

---

We agree that including non-foundation baselines would make the empirical picture more complete. We report the UCR average test accuracy of these non-foundation baselines:

| Model               | UCR test accuracy |
| ------------------- | ----------------- |
| Random Forest       | 0.7325            |
| XGBoost             | 0.6917            |
| Logistic Regression | 0.6812            |


In the revised version, we add standard non-TSFM 

### CauKer: Classification Time Series Foundation Models Can Be Pretrained on Synthetic Data


## Meta review / decision
### Paper Decision
Accept (Oral)

## PDF extracted text (first pages)
```text
Published as a conference paper at ICLR 2026
CAUKER: C LASSIFICATION TIME SERIES FOUNDATION
MODELS CAN BE PRETRAINED ON SYNTHETIC DATA
Shifeng Xie
Universit´e Paris Cit´e
Huawei Noah’s Ark Lab
xidainxieshifeng@gmail.com
Vasilii Feofanov
Huawei Noah’s Ark Lab
42.com
Jianfeng Zhang
Huawei Noah’s Ark Lab
Themis Palpanas
Universit´e Paris Cit´e
Ievgen Redko
Huawei Noah’s Ark Lab
ABSTRACT
Time series foundation models (TSFMs) have recently gained significant atten-
tion due to their strong zero-shot capabilities and widespread real-world appli-
cations. Such models typically require a computationally costly pre-training
on large-scale, carefully curated collections of real-world sequences. To allow
for a sample-efficient pre-training of TSFMs, we propose CAUKER, a novel al-
gorithm designed to generate diverse, causally coherent synthetic time series
with realistic trends, seasonality, and nonlinear interactions. CAUKER com-
bines Gaussian Process (GP) kernel composition with Structural Causal Mod-
els (SCM) to produce data for sample-efficient pre-training of state-of-the-art
classification TSFMs having different architectures and following different pre-
training approaches. Additionally, our experiments reveal that CAUKER-generated
datasets exhibit clear scaling laws for both dataset size (10K to 10M samples)
and model capacity (1M to 783M parameters), unlike real-world datasets, which
display irregular scaling behavior. The source code is publicly available at
https://github.com/ShifengXIE/CauKer.
1 I NTRODUCTION
Time series data are ubiquitous in applications ranging from healthcare (Gnassounou et al., 2025)
and human activity recognition (Chen et al., 2025a) to industrial monitoring (Susto et al., 2018).
Recently, the time series community has devoted significant effort to developing large-scale pre-
trained time series foundation models (TSFMs). Inspired by advances in natural language processing
and computer vision, these models aim to achieve strong zero-shot performance in out-of-distribution
(OOD) settings. TSFMs have been proposed for both forecasting (Ansari et al., 2024; Woo et al.,
2024; Bhethanabhotla et al., 2024) and classification tasks (Goswami et al., 2024; Lin et al., 2024;
Feofanov et al., 2025), showing promising results. TSFMs are usually trained on large-scale pre-
training dataset collections gathered from different application domains. Recent works used as many
as 300 billion timepoints for model pre-training (Shi et al., 2025).
Despite the prevalence of large-scale pre-training in the development of TSFMs, several works
(Hoo et al., 2024; Dooley et al., 2023; Taga et al., 2025; Liu et al., 2025) showed that comparable
performance can be achieved by training them purely on synthetic data. The latter approach has
several important advantages. First, it removes the need for time-consuming data collection and
curation. This is especially important in time series classification that lacks diverse and rich pre-
training corpora. Second, it allows for generating arbitrarily large datasets for model scaling. Finally,
it makes the OOD evaluation more meaningful, mitigating the risk of data leakage. Inspired by
the recent success of foundation models in tabular classification (Hollmann et al., 2023), our paper
proposes a novel sample-efficient pre-training framework for TSFMs in classification based purely on
synthetic data. Contrary to tabular and forecasting synthetic data generation pipelines, our proposal
seeks to generate sequences with meaningful correlations between samples and realistic temporal
1
Published as a conference paper at ICLR 2026
dependencies within them. We provide an in-depth, large-scale study of its benefits compared to
pre-training on commonly used time series classification corpora.
Findings Overall, our findings can be summarized as follows:
1. A carefully designed synthetic data generation pipeline can be efficiently used in training
classification TSFMs. We propose such a pipeline and show that it requires rethinking
synthetic data generators proposed previously for tabular data and time series forecasting.
2. Pre-training on synthetic data reveals clear scaling laws both in terms of dataset size and
model size. We illustrate this finding by showing that such scaling laws are broken when
using common classification benchmarks for pre-training, likely due to the lack of diversity
in existing classification datasets.
3. Distinct from forecasting (Yao et al., 2025), where the leaderboard (with the exception of
(Hollmann et al., 2023)) is still dominated by models pre-trained on large-scale real-world
datasets, we show that pre-training on solely synthetic data can lead to state-of-the-art
performance in classification.
The rest of this paper is organized as follows. In Section 2, we present recent advances in TSFMs and
describe commonly used pre-training datasets. In Section 3, we present the problem setup considered
in our work and the proposed synthetic data generation pipeline. In Section 4, we empirically validate
the effectiveness of CAUKER-generated synthetic data through extensive experiments, demonstrating
its strong generalization, scalability, and superiority over existing synthetic generation methods.
Finally, we conclude our work and its limitations in Section 5.
2 R ELATED WORK
Time series foundation models Recent advances in TSFM have followed two primary directions:
(1) training models from scratch on large-scale, diverse time series datasets (Ansari et al., 2024;
Goswami et al., 2024; Das et al., 2024; Gao et al., 2024; Rasul et al., 2024; Wang et al., 2024; Woo
et al., 2024; Bhethanabhotla et al., 2024; Lan et al., 2025; Gao et al., 2024; Lin et al., 2024; Liu et al.,
2024b; Cohen et al., 2024; Auer et al., 2025), and (2) leveraging large language models (LLMs)
as backbones for time series tasks (Chang et al., 2023; Gruver et al., 2024; Zhou et al., 2023; Xue
& Salim, 2023; Cao et al., 2023; Jin et al., 2023; Liu et al., 2024a). The first approach focuses on
developing architectures specifically tailored for time series, while the second approach explores
encoding time series data into textual formats or extending the model’s input mechanisms to natively
handle sequential numeric data. Among the TSFMs mentioned above, a vast majority were proposed
for time series forecasting, with only (Feofanov et al., 2025; Gao et al., 2024; Goswami et al., 2024;
Chang et al., 2025; Lin et al., 2024; Zhang et al., 2025) natively supporting time series classification.
In particular, (Feofanov et al., 2025; Lin et al., 2024; Roschmann et al., 2025) specifically target
classification by contrastively pre-training encoder-only models over time series gathered from
popular classification benchmarks. They achieve state-of-the-art results in this task. Goswami et al.
(2024) is an encoder-decoder model used for classification and other popular time series tasks, such
as forecasting, imputation, and anomaly detection. Gao et al. (2024) relies on a custom architecture
and is used in generative and prediction tasks by leveraging task-specific tokens. Finally, Chang et al.
(2025) fine-tunes an LLM by adding an appropriate encoder for input data and a classification head
to generate predictions.
Pre-training datasets The training data for TSFM generally fall into three categories: real-world,
synthetic, or hybrid datasets combining the two. Models trained (or fine-tuned in case of LLM-based
TSFMs) exclusively on real data (Das et al., 2024; Gao et al., 2024; Rasul et al., 2024; Wang et al.,
2024; Feofanov et al., 2025; Gao et al., 2024; Lin et al., 2024; Chang et al., 2023; Gruver et al.,
2024; Zhou et al., 2023; Xue & Salim, 2023; Cao et al., 2023; Jin et al., 2023) typically leverage
extensive collections (ranging from 300k to 50M distinct time series) drawn from diverse domains
such as traffic, finance and environmental monitoring. Training on these datasets, however, may be
suboptimal scaling-wise as Quan et al. (2024) obtained comparable performance using < 1% of the
original 27B pre-training dataset from (Woo et al., 2024), while Yao et al. (2025) showed that famous
forecasting TSFMs have very flat scaling laws in the multivariate setting. Meanwhile, forecasting
2
Published as a conference paper at ICLR 2026
models such as Chronos (Ansari et al., 2024) and TimesFM (Das et al., 2024) enhance their training
corpus by incorporating synthetic time series data alongside real-world data. Beyond sequence-native
TSFMs, there is a complementary line of work (Chen et al., 2025b) that maps time series into
image-like representations and then applies vision Transformers. Finally, such methods as TimePFN
(Taga et al., 2025) and ForecastPFN (Dooley et al., 2023) are pre-trained solely on synthetic data.
In all these forecasting models, synthetic data is commonly generated through structured statistical
procedures, including Gaussian process (kernel-based) methods or piecewise linear and seasonal
pattern constructions with additive noise (for more details, we refer the interested reader to Appendix
A.) To the best of our knowledge, no prior work has proposed classification-oriented synthetic data
generation methods for training time series foundation models.
3 O UR CONTRIBUTIONS
We now introduce the task of zero-shot time series classification using TSFMs. We then formally
present the common pre-training strategies and introduce our synthetic data generation pipeline.
3.1 P ROBLEM SETUP
Zero-shot classification As done in prior work on unsupervised representation learning (Franceschi
et al., 2019; Yue et al., 2022), we see a TSFM as an encoderF : Rt → Rq that is kept frozen during the
evaluation. For a downstream classification dataset D = {(xi, yi)}n
i=1 with labels yi ∈ {1, . . . , C},
we use a TSFM to obtain embeddings zi = F (xi) and train a lightweight classifier h : Rq →
{1, . . . , C} solely on {(zi, yi)}. At test time, an unseen series x∗ is classified by ˆy = h
 
F (x∗)

. As
F is kept frozen, the resulting accuracy measures the quality of its learned representations.
To quantify OOD generalization ability, we follow Yao et al. (2025) and evaluate the studied TSFMs
only on samples not seen during their pre-training. In practice, if we evaluate a given TSFM on a
test set from a UCR (Dau et al., 2019) dataset, we ensure that the TSFM was not pre-trained on it.
Our CAUKER-pretrained models are trained only on CAUKER-generated synthetic series and never
see UCR (or any real-world classification benchmark) during pre-training. The original Mantis and
MOMENT (Feofanov et al., 2025; Goswami et al., 2024) checkpoints, as well as other TSFMs we
compare to, are pre-trained on large real-world corpora that include UCR train sets (but never UCR
test data), following the standard protocol in prior work. Therefore, original Mantis and MOMENT
are, to some extent, in the in-distribution setup.
Self-supervised pre-training Self-supervised learning (SSL) has emerged as a powerful training
paradigm for foundation models, allowing them to effectively learn discriminative representations
from large-scale unlabeled datasets, significantly reducing dependency on costly data labeling (Jaiswal
et al., 2020). SSL methods are categorized into two principal types: contrastive learning and masked
(reconstruction) learning (Liu et al., 2023). Contrastive learning focuses on distinguishing between
similar (positive) and dissimilar (negative) data pairs to learn meaningful representations. Conversely,
masked learning leverages reconstruction objectives by training models to predict masked parts of
the input, thereby gaining robust contextual understanding (Zhang et al., 2022).
In our work, we cover both pre-training regimes. To this end, we consider Mantis (Feofanov et al.,
2025), an open-source FM pre-trained contrastively, and MOMENT (Goswami et al., 2024), which
is a masked-based pre-trained model. Detailed formulations of the loss functions and architecture
specifics for these models are provided in the Appendix B.
3.2 C AUKER: SYNTHETIC DATA GENERATION FOR TIME SERIES CLASSIFICATION
We now present our proposed synthetic data generation pipeline, termedCAUKER for Causal-Kernel
generation. To develop our intuition about it, we note that the synthetic data for the time series
classification task needs to combine two key ingredients. On the one hand, the generated sequences
should exhibit common time series patterns such as seasonality, periodicity, and trend. On the other
hand, successful classification assumes that individual time series have a meaningful clustering
structure that allows the trained model to successfully learn how to disentangle the underlying clusters
during training. Below, we present a generation pipeline that satisfies these desiderata.
3
Published as a conference paper at ICLR 2026
Generated �me series
Combined 
kernels
Selected
kernels
Generate with 
selected mean
SCM with selected 
ac�va�on func�ons
Ac�va�on 
func�on
Figure 1: An illustration of the proposed CAUKER pipeline. Kernels sampled from the kernel bank
K are randomly combined and used together with sampled mean functions to form GP priors. Time
series sampled from these GP priors act as root nodes in a directed acyclic graph that encodes causal
dependencies between nodes. Each edge of this graph applies an activation function from a predefined
activation function bank and aggregates over incoming edges using a random linear transformation
to propagate transformed time series through the graph. Intermediate node outputs are optionally
interpolated to fixed length, forming the final synthetic dataset. This procedure yields rich, diverse,
and causally consistent time series for self-supervised pre-training.
Proposed approach To proceed, we now define three banks of functions, namely: kernel, mean and
activation banks denoted as K = {κi(t, t′)}nK
i=1, M = {µi(t)}nM
i=1 and A = {σ(t)i}nA
i=1, respectively.
For the kernel bank, we use the same kernel functions as Ansari et al. (2024). For mean functions,
we consider a linear function ax + b, exponential function aebx, and anomaly mean function that
inserts random values from U(−5, 5) at random indexes. Finally, the activation functions we use for
A are a linear function ax + b with a ∼ U (0.5, 2), b ∼ U (−1, 1)], ReLU activation, sigmoid, sine
function, element-wise modulo operation x mod c for c ∼ U [1, 5], and Leaky ReLU with a random
negative slope from U(0.01, 0.3). For simplicity, in what follows we let {si}n
i=1 ∼ S denote an i.i.d.
sampling (without replacement) of n elements from a set S.
Our generative pipeline, illustrated in Figure 1, then proceeds in five steps as follows:
Step 1. Kernel bank sampling We start by sampling candidate kernels from the kernel bank, ie,
{κi(t, t′)}K
i=1
i.i.d.
∼ K for some random number of candidate kernels K ∼ U (1, nK).
Step 2. Kernel composition We define a composite kernel based on K − 1 randomly sampled
binary operations (+ and ×). More formally, for a random sequence {⋆i}K−1
i=1 ∼ {+, ×},
we let κ∗ = κ1(t, t′) ⋆i · · · ⋆K−1 κK(t, t′).
Step 3. Root nodes generation We draw M mean functions {µi(t)}M
i=1
i.i.d.
∼ M , M ∼ U (1, nM)
and repeat Step 1 and Step 2 M times to obtain composite kernels {κ∗
i }M
i=1. We further
define M GP priors to sample from {GP (µi, κ∗
i )}M
i=1.
Step 4. Activation bank sampling We sample a set of E activation functions from the activation
bank, ie, {σi}E
i=1 ∼ A, E ∼ U (1, nA).
Step 5. Causal graph propagation We randomly generate a directed acyclic graph (DAG)(V, E)
with |E| = E, |V| = V , and M < V root nodes, i.e., nodes with in-degree zero. We
then define a bijection ϕ : V → { σ1, σ2, . . . , σV } such that each node vi is uniquely
associated with a function σl, i.e., ϕ(vi) = σl. We then associate a time series ti ∈ RL
sampled from GP (µi, κ∗
i )} to each of the M root nodes. The value tvj associated with a
given non-root vertex vj is then calculated as follows. First, we concatenate all incoming
edges e.j and aggregate them using a randomly initialized linear layer with weights and
biases W, b ∼ N (0, 1), then we apply a randomly sampled activation function to get
tvj = ϕ(vj)(W × [e.j] + b).
A complete pseudocode of this procedure, as well as the composition and visualizations of the kernel,
mean, and activation banks, are provided in Appendix C.
Design choices The synthetic datasets generated using our CAUKER approach effectively encode
diverse, realistic patterns and causal dynamics characteristic of real-world classification problems. Un-
like the kernel-only generator of Ansari et al. (2024) (Steps 1,2), which was designed for forecasting
4
Published as a conference paper at ICLR 2026
and therefore draws zero-mean Gaussian-process samples that emphasize smooth trend extrapolation,
our task calls for retaining the mean level itself (Step 3) as a discriminative cue – a choice that is
empirically confirmed in Section 4.4. Conversely, the structural causal model (SCM) generator (Steps
4,5) originally proposed for tabular classification (Hollmann et al., 2023) produces rich non-linear
dependencies but lacks hallmark time series motifs such as seasonality or linear trends. By unifying
kernel composition with an SCM processing, CAUKER inherits the periodic structure of Gaussian
processes while simultaneously injecting causal semantics through directed edges. Finally, we note
that different nodes of the same SCM in CAUKER can be interpreted as different channels of a
multivariate time series that share a common causal structure. This hints at the potential of CAUKER
for pre-training inherently multivariate models as well. We further ablate the structure of the SCM in
C.3 and the impact of kernel bank composition in C.2.
Positioning our method While synthetic data generation has been explored for time series fore-
casting and tabular classification, adapting these pipelines to time series classification TSFMs is far
from trivial. Forecasting-oriented generators (e.g., kernel-based method with zero means(Ansari
et al., 2024)) are optimized for smooth extrapolation and often neglect class-conditional structure and
inter-class separability. Conversely, tabular SCM generators (e.g., TabPFN(Hollmann et al., 2023))
discard temporal structure. Our method, CAUKER, bridges this gap by unifying kernel-composed
Gaussian processes with structural causal models, resulting in synthetic corpora that exhibit discrimi-
native clusters and well-behaved scaling laws, in sharp contrast to current real-world classification
collections whose heterogeneous, imbalanced composition makes them unreliable for pre-training of
TSFMs.
Our experiments in Section 4 demonstrate that foundation models pre-trained on such data exhibit
improved out-of-distribution generalization and meaningful scaling behavior, outperforming models
trained solely on traditional synthetic benchmarks and performing with those trained on much larger
real-world time series corpora. We restrict our pre-training experiments to univariate inputs and treat
each node’s trajectory as an individual series, in order to match the univariate pre-training regime of
TSFMs.
4 E XPERIMENTAL RESULTS
We now empirically evaluate the effectiveness of our proposedCAUKER framework for pre-training
classification TSFMs. Our experiments aim to answer the following key questions:
Q1. How does C AUKER compare to alternative synthetic data generation methods?
Q2. Do TSFMs trained on C AUKER data exhibit meaningful data and model scaling laws?
Q3. Can CAUKER-generated synthetic data be a competitive replacement for real-world bench-
marks in training TSFMs?
In all our experiments, we consider two recent TSFMs, namely Mantis and MOMENT. Mantis is
an 8M encoder-only model pre-trained using contrastive learning. We use the 77M version of the
MOMENT model. The latter is an encoder-decoder model pre-trained based on masked reconstruction.
Considering these two models allows us to compare two differe
```
