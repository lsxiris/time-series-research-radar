# Aurora: Towards Universal Generative Multimodal Time Series Forecasting — OpenReview Raw Thread

- Forum: https://openreview.net/forum?id=VVJ6Ck9JBl
- PDF: https://openreview.net/pdf?id=VVJ6Ck9JBl
- Section: 一、时间序列生成：因果性、多样性与领域适配
- Zhihu score: 6.0
- Venue status: ICLR 2026 Poster

## Submission metadata
- Authors: Xingjian Wu, Jianxin Jin, Wanghui Qiu, Peng Chen, Yang Shu, Bin Yang, Chenjuan Guo
- Primary area: learning on time series and dynamical systems
- Keywords: Time Series Forecasting, Multimodality

## Abstract
Cross-domain generalization is very important in Time Series Forecasting because similar historical information may lead to distinct future trends due to the domain-specific characteristics. Recent works focus on building unimodal time series
foundation models and end-to-end multimodal supervised models. Since domain-specific knowledge is often contained in modalities like texts, the former lacks the explicit utilization of them, thus hindering the performance. The latter is tailored for end-to-end scenarios and does not support zero-shot inference for cross-domain scenarios. In this work, we introduce Aurora, the first Multimodal Time Series Foundation Model, which supports multimodal inputs and zero-shot inference. Pretrained on Cross-domain Multimodal Time Series Corpus, Aurora can adaptively extract and focus on key domain knowledge contained in corresponding text or image modalities, thus possessing strong cross-domain generalization capability. Through tokenization, encoding, and distillation, Aurora can extract multimodal domain knowledge as guidance and then utilizes a Modality-Guided Multi-head Self-Attention to inject them into the modeling of temporal representations. In the decoding phase, the multimodal representations are used to generate the conditions and prototypes of future tokens, contributing to a novel Prototype-Guided Flow Matching for generative probabilistic forecasting. Comprehensive experiments on 5 well-recognized benchmarks, including TimeMMD, TSFM-Bench, ProbTS, TFB, and EPF, demonstrate the consistent state-of-the-art performance of Aurora on both unimodal and multimodal scenarios.

## Reviews
### Reviewer_MY6v
- summary: The authors propose Aurora, a multimodal time series foundation model. By leveraging multimodal information fusion, Aurora achieves impressive zero-shot forecasting performance. The paper also introduces a new decoder design. Experimental results demonstrate that the proposed method outperforms baseline models across various datasets.
- strengths: - The authors propose a powerful zero-shot time series foundation model that effectively integrates multimodal information for prediction.
- The proposed method integrates different modules and achieves remarkable performance in terms of robustness.
- weaknesses: ### **Experiment Setting and Performance**

The proposed method achieves better zero-shot performance than baselines. However, MAE and MSE are greater than 0.5, as seen in PEMS08, Traffic, and Wind. I am not sure whether the metrics are calculated based on normalized results. If so, a high MAE or MSE may not be better than a straight line or random output.


### **Inference time**

The work focuses on few-shot learning and zero-shot learning. However, compared to the training cost, such a large model increases the inference time and requires more GPU resources. I suggest that the author include an experiment to compare the proposed 16G model with iTransformer on ETT, traffic, or weather, in terms of total running time (training time + inference time for a fair comparison). I am curious about whether the training time and inference time of a small model may be quicker than that of a large model. 

### **Baselines**

I noticed the author only chose large foundation models to evaluate few
- questions: I am willing to adjust the rating based on the authors' feedback, particularly regarding my concerns about baselines, benchmarks, and experiment settings.
Please refer to the weakness.
- rating: 4 | confidence: 4

### Reviewer_t5fV
- summary: This paper presents Aurora, which is a generative foundation model to unify time series forecasting across diverse domains and modalities. First, it has token distillation and modality alignment modules for cross-modality fusion, then the modality-guided attention will inject textual and visual knowledge into temporal encoding. Lastly, in the  decoding stage, a prototype-guided flow matching will improve generative probabilistic forecasting by using learned trend and periodic prototypes. Through the experiments on TimeMMD, TSFM-Bench, and ProbTS, the authors demonstrate Aurora's good performan
- strengths: 1. It really focuses on the limitations of the existing multimodal TS forecaster and foundation models. It introduces a novel multimodal pretraining paradigm with datasets, which is a huge contribution to this field. 
2. The architecture is novel. The modality guided attention bridges domain knowledge with temporal information. The prototype guided flow matching improves the interpretability of probabilistic forecasting.
3. Aurora is evaluated on diverse benchmarks with both deterministic and pr
- weaknesses: 1. Using LLM to generate a textual description can be problematic. The paper provides no analysis of data leakage or the quality analysis of generated texts for pretraining data. Also, the paper should provide a more rigorous clarification regarding whether the pretraining data has any overlap with the benchmark datasets.
2. Prototypes give more interpretability for this paper, but have no analysis or visualization of learned prototypes. 
3. Missing TTM[1] in related work and baseline comparison. 


[1] Ekambaram, Vijay, et al. "Tiny time mixers (ttms): Fast pre-trained models for enhanced zero/few-shot forecasting of multivariate time series." Advances in Neural Information Processing Systems 37 (2024): 74147-74181.
- questions: 1. Is the use of Flow Matching in the decoder essential, or could other generic multimodal decoding frameworks be applied instead?
2. Could you provide specific examples where your model demonstrates advantages to your claim: cases where similar historical patterns lead to different future trends due to domain-specific characteristics?
- rating: 6 | confidence: 4

### Reviewer_qDZm
- summary: This work makes a timely and impactful contribution: it is, to the best of my knowledge, the first universal generative foundation model that unifies multimodal inputs (text + image + time series) for cross-domain zero-shot forecasting. Prior foundation models (e.g., MOIRAI, Chronos, Sundial) are unimodal; prior multimodal models (e.g., Time-LLM, CALF, GPT4MTS) are supervised and non-generative. Aurora bridges this gap. The prototype-guided flow matching is also a compelling design that provides interpretable inductive bias (trend/periodicity) to the generative process, improving sample effici
- strengths: - First generative multimodal foundation model enabling cross-domain zero/few-shot time series forecasting.
- Novel cross-modal encoder (modality-guided attention) and prototype-guided decoder design boost generalization and probabilistic prediction quality.
- Extensive experiments across diverse benchmarks (TimeMMD, TSFM-Bench, ProbTS) consistently outperform unimodal/multimodal baselines.
- weaknesses: - Prototype scalability: The prototype bank contains 1,000 learnable patterns. How does performance vary with the number of prototypes (e.g., M = 100 vs. 1,000 vs. 10,000)? Is there a trade-off between forecast accuracy, training stability, and inference latency? A small ablation would clarify whether this component is over-parameterized.
- The method assumes that text and image modalities are faithful and aligned with the time series. However, in real-world settings: Text may be vague, outdated, or incorrect; and images rely on FFT-based period estimation, which can be unreliable for non-stationary or chaotic series. The paper does not evaluate modality corruption robustness (e.g., masking text, perturbing image tokens), which is critical for practical adoption.
- Can Aurora be extended to other multimodal time series tasks (e.g., anomaly detection)?
- questions: See the weaknesses
- rating: 8 | confidence: 5

### Reviewer_UdWk
- summary: This paper proposes Aurora, a multimodal time series foundation model for zero-shot forecasting. Aurora is pretrained on cross-domain corpus with time series, text descriptions, and endogenous images. The encoder uses token distillation and modality-guided self-attention to fuse multimodal features. The decoder employs prototype-guided flow matching for probabilistic forecasting, where prototypes encode periodicity/trend initialized from text and image features. Experiments on TimeMMD, TSFM-Bench, and ProbTS show SOTA performance on both multimodal and unimodal tasks.
- strengths: **S1. Novel multimodal foundation model architecture**

Aurora introduces a well-designed multimodal architecture with token distillation and modality-guided self-attention. The modality-guided mechanism (Equations 12-16) explicitly uses cross-modality correlations to adjust temporal attention, enabling domain knowledge injection. The prototype-guided flow matching is innovative, retrieving learned period/trend prototypes as starting points rather than Gaussian noise. Ablations (Table 4) validat
- weaknesses: **W1. Insufficient ablation on modality contributions:** Table 4 only ablates entire mechanisms but does not quantify individual modality contributions. The paper lacks experiments comparing time-only, time+text, time+image, and time+text+image performance. This omission makes it impossible to understand what each modality provides. Since images are deterministic transformations of time series (Equations 3-7), readers cannot assess whether images truly add information beyond text or simply provide redundant patterns already in the time series.

**W2. Insufficient ablations on modality-guided attention design:** Variant 1 removes the entire modality-guided mechanism, but the paper lacks finer-grained ablations to validate specific design choices. The Corr matrix computation (Equation 14) multiplies $VAttn$, learnable metric $W$, and $TAttn^T$, but alternative designs (text-only guidance, image-only guidance, additive combination) are not tested. The necessity of the learnable metric W i
- questions: **Q1. Can you provide individual modality ablations?**

Report performance with time-only, time+text, time+image, and time+text+image to quantify each modality's contribution and validate that each adds value.

**Q2. Can you provide finer ablations of modality-guided attention?**

Test text-only guidance, image-only guidance, alternative combination methods, and ablate the learnable metric W to validate design choices in Equations 12-14.

**Q3. Can you visualize and characterize learned prototypes?**

Show visualizations of the 1000 prototypes, analyze whether they form interpretable clusters, and demonstrate which prototypes are retrieved for different domains and patterns.

**Q4. What are typical LLM-generated description examples?**

Provide more examples beyond Figure 7. How do you ens
- rating: 6 | confidence: 4

## Author comments / rebuttal
### The summary of Rebuttal (average rating 6.0 → 6.5)
**Dear Reviewers, ACs, SACs, and PCs,**

We sincerely appreciate your dedication to this conference.

We were sorry to learn about the recent technical issues with OpenReview, and we fully support the remedial actions proposed by the committee. Fortunately, thanks to the diligence and responsiveness of our reviewers, we had essentially concluded most meaningful discussions by **Nov. 26**, well prior to the incident on **Nov. 27**.


To assist in the final assessment of our submission, we have summarized the consensus on our work's **strengths** and the **results of the discussion** below:

It is encouraging to see that reviewers agree on the following strengths of our work:

- **High Novelty and Originality**: Our work proposes Aurora, **the first multimodal time series foundation model**, focusing on the real-world cross-domain forecasting problem. (qDZm, t5fV, UdWk)
- **Exquisite Multimodal Modules**: Both the encoder (**Modality-guided Self-attention**) and decoder (**Prototype-guided Flow Matching**) of Aurora adopt novel designs to ensure the sufficient utilization of cross-domain multimodal knowledge.  (MY6v, qDZm, t5fV, UdWk)
- **Strong Empirical Performance**: Aurora is demonstrated to achieve **state-of-the-art** performance on versatile forecasting tasks, including unimodal, multimodal, and probabilistic scenarios. (MY6v, qDZm, t5fV, UdWk)

During the rebuttal phase, we managed to address the reviewers' concerns through:

- **Additional experiments**: To ensure comprehensive evaluations and ablations.
- **Interpretability analysis**: To visualize the learned prototypes and attention scores.
- **Manuscript refinement**: To include all the revisions into our draft.

We are pleased that **Reviewers qDZm, t5fV, and UdWk** have explicitly confirmed that **their concerns were addressed**, supporting our work by **raising or maintaining their positive scores**. For **Reviewer MY6v**, he/she showed the willingness in the original comments to adjust the score after the rebuttal. Unfortunately, this incident of OpenReview prevented further discussions.

We also summerize Reviewers' scores before/after discussion till **Nov. 26**.

| Reviewer    |                       Changes of Score                       | Date of Changes |
| ----------- | :----------------------------------------------------------: | :-------------: |
| **MY6v**    |    4 $\textcolor{green}{➜}$ 4 (**No substantive reply**)     |        -        |
| **t5fV**    | 6 $\textcolor{green}{➜}$ 6 (**Replied and maintained positive scores**) |   **Nov. 26**   |
| **qDZm**    | 8 $\textcolor{green}{➜}$ 8 (**Replied and maintained positive scores**) |   **Nov. 26**   |
| **UdWk**    | 6 $\textcolor{red}{➜}$ 8 (**Replied and raised the scores**) |   **Nov. 20**   |
| **Average** |             **6.0** $\textcolor{red}{➜}$ **6.5**             |        -        |

**Reviewer MY6v**'s suggestions are all about experimental details, such as adding short-term tasks, few-shot/full-shot compariso

### Request for further discussions
Reviewer MY6v,

We are very grateful for your open-mindedness and constructive suggestions during the reviewing and rebuttal phases. Since you mentioned a week ago that you would continue to update the comments later, we are kindly reminding that the rebuttal phase seems to end soon.

We hope you can reconsider the scores based on our current response, and if you have more questions we can make further discussions.

Best regards,
Authors of "Aurora: Towards Universal Generative Multimodal Time Series Forecasting"

### Author comment
Dear Reviewer qDZm,

We are very grateful for the efforts you have put into reviewing the manuscript and provide such insightful and detailed reviews! In the future, we will follow your advice to further study on constraining the similarity between prototypes.

Best regards,
Authors.

### Author comment
Dear Reviewer t5fv,

We really appreciate your efforts during this tight review timeline and the recognition of the strengths of our paper.

Best regards,

Authors.

### Thanks for your efforts
Dear Reviewer UdWk, we are thrilled that our responses have effectively addressed your questions and comments. We would like to express our sincerest gratitude for taking the time to review our paper and provide us with such detailed feedback!

### Author comment
We are very grateful for the efforts you have put into reviewing the manuscript and your instant responses. If there are more questions, we can discuss them further. 

Best wishes!

### About the Experimental Settings
Dear Reviewer MY6v, the full-shot results of **TimeXer, iTransformer, PatchTST, and TimesNet** are directly fetched from the paper of TimeXer, where the input sequence length is set to 96. For more advanced baselines TimePro, TimeKAN and AMD, we also follow their original results if their settings are the same as TimeXer. If not, we evaluate them using the same settings.

The motivation for doing this is that in some early works, the tricky of "Drop Last" [1][2] was adopted, leading to inaccurate results. We confirmed that TimeXer did not do this, so its results are reliable, and in the process of our own experiments, we also strictly adhered to not adopting this tricky.

[1] Fundamental limitations of foundational forecasting models: The need for multimodality and rigorous evaluation

[2] TFB: Towards Comprehensive and Fair Benchmarking of Time Series Forecasting Methods

We have claimed not to use "Drop Last" in the Appendix A.4, for more settings of the full-shot baselines, we will update them in the revised draft.

### Summary of Our Rebuttal
Dear Reviewers:

       We have submitted all the rebuttal and the revised draft. In our revised draft, we have marked the newly added or modified parts in darkblue. We hope our response can effectively address your concerns. If you have more questions, we can discuss further! 

      Thanks again for your efforts during the review process and for such detailed and insightful comments. From the authors of "Aurora: Towards Universal Generative Multimodal Time Series Forecasting".

Best wishes!

### Response for Q4 and Q6
Following your advice, we provide more examples **in Figure 8 of Appendix A.1.** In the generation process of textual descriptions, the quality of texts is exactly important so we do adopt some techniques to ensure that. After a GPT4 agent generates the textual descriptions, we first **coarsely check the quality with another GPT4 agent**. If the quality is low, the process will be redone. After a batch of textual descriptions are generated, **we randomly sample from them (5%) and check the quality manually**, then determine whether to regenerate this batch of data and tune the prompts. We think this process does not involve data leakage problem because we only input GPT4 with the contextual time series in a single conversation.

**We further clarify the pretraining datasets we use in Figure 7 of Appendix A.1** in the revised draft, including the ratios of domains, the specific datasets used, and the lengths and sources of them. We also revise the corresponding texts to add more implementation details. **Note that there exists no overlap in pretraining and testing datasets.**

### Response for W6
Actually, the inference time we report is already with the sampling number equal to 100, and we have already reported the pretraining cost in the Appendix A.4:

“All experiments are executed on only 8 NVIDIA A800 GPUs, each equipped with 80GB of GPU
memory, which takes about 30 days to train Aurora from scratch.”

To make the zero-shot and few-shot efficiency more clear, we then compare Aurora (zero-shot) and Aurora (10% few-shot) with full-shot supervised models, i.e., TimeXer, PatchTST, iTransformer, and TimesNet. We report the training time and inference time of them on datasets with different scales, i.e., ETTh1, ETTm2, Weather, Electricity, and Traffic. **Please refer to the Table below or the Figure 9 in Appendix A.7 of our revised draft.**

| Datasets | Aurora (Zero-shot) |  | Aurora (10% few-shot) |  | TimeXer |  | iTransformer |  | PatchTST |  | TimesNet |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Metrics | Training Time | Inference Time | Training Time | Inference Time | Training Time | Inference Time | Training Time | Inference Time | Training Time | Inference Time | Training Time | Inference Time |
| ETTh1 | 0 | 4.728 | 148.925 | 4.728 | 46.471 | 1.22 | 34.285 | 1.029 | 21.133 | 0.991 | 105.977 | 1.912 |
| ETTm2  | 0 | 12.825 | 282.958 | 12.825 | 92.019 | 4.712 | 72.703 | 5.288 | 71.09 | 4.919 | 249.692 | 7.073 |
| Weather | 0 | 26.811 | 707.382 | 26.811 | 174.909 | 4.764 | 78.961 | 5.133 | 265.171 | 10.856 | 705.421 | 14.967 |
| Electricity | 0 | 109.773 | 1471.924 | 109.773 | 354.459 | 6.775 | 158.857 | 8.889 | 1373.411 | 22.723 | 1428.109 | 78.912 |
| Traffic  | 0 | 275.921 | 2974.827 | 275.921 | 676.938 | 11.016 | 262.631 | 24.696 | 2783.825 | 38.924 | 3855.15 | 186.625 |

It is observed that the inference time of zero-shot Aurora (no training required) is consistently and largely less than the total time (training time + inference time) of full-shot models, demonstrating the strong efficiency with accurate performance. Considering the 10% few shot Aurora, though its time cost is a bit more than TimesNet, it can lead to state-of-the-art performance in most cases.

### Response for W5, Q7
Thanks for the advice. However, conducting experiments on multiple datasets and evaluation settings across various benchmarks is an effective way to verify the capabilities of foundation models, and this approach is widely used not only in the field of time series but also in NLP and CV. 

In this work, we use three benchmarks in the submission version for following reasons:

1. Using TimeMMD to evaluate the multimodal forecasting capability of Aurora
2. Using TSFM-Bench to evaluate the unimodal deterministic forecasting capability of Aurora
3. Using ProbTS to evaluate the probabilistic forecasting capability of Aurora

**These three benchmarks are used to evaluate different capabilities of Aurora respectively.** Currently, a unified benchmark for all does not exist and this can be an interesting research direction.

### Response for W4, Q3
Following your advice, we conduct visual analysis in the following two aspects:

1. we visualize the 1,000 learned prototypes in PrototypeBank **in Figure 14 of Appendix C.2, which includes versatile prototypes like linear trends, sinusoids, seasonality as you mentioned. You can also refer to the Figures 15—17 in Appendix C.3, which involve 28 specific visualization cases in forecasting.** 
It is observed that Aurora can retrieve-then-generate proper prototypes for predictions, which contains periodic or trend implications for future horizons. For example, in Figures 15 (b)—(d), the generated prototypes do imply the future periods in the power transformer systems (ETTs). In Figures 15 (e), (f), (i), (j), the generated prototypes reveal the future trends in the domains of Traffic, Weather, and Energy. 
2. To reveal how attention weights change with and without modality guidance (the impact of Corr on them), we also conduct experiments in **Figures 18—21 of Appendix C.4.** 
For example, In Figure 18, It is observed that the predictions with modality guidance are more accurate. The 4 patches (T1—T4) of the contextual time series show similar correlations without modality guidance. While with the modality guidance, the correlations between T1 and T2 are further focused on, because their correlations are similar to the T4 and future values, with a trend of first decreasing and then increasing. Additionally, the correlations between T4 and T1 are also focused on for prediction.

### Response for W3, Q5
Thanks for the suggestions! Our original intention is to indicate that Aurora can outperform end-to-end models trained with all data by fine-tuning with only 10% data. To make the comparisons more clear and demonstrate Aurora’s capability, we separate the settings of zero-shot and few-shot in the following two Tables, you can also refer to our revised draft (see Tables 20—21 in Appendix D):

| Models | Aurora  (zero-shot) |  | Sundial (zero-shot) |  | VisionTS (zero-shot) |  | ROSE (zero-shot) |  | MOIRAI (zero-shot) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Metric | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE |
| Agriculture | **0.272** | 0.348 | 0.373 | 0.392 | 0.290 | **0.336** | 0.345 | 0.372 | 0.272 | 0.403 |
| Climate | **0.865** | **0.749** | 1.154 | 0.881 | 1.307 | 0.930 | 1.475 | 0.987 | 1.921 | 1.095 |
| Economy | **0.033** | **0.146** | 0.291 | 0.432 | 0.301 | 0.442 | 0.289 | 0.433 | 0.405 | 0.512 |
| Energy | **0.255** | 0.370 | 0.272 | **0.367** | 0.304 | 0.420 | 0.386 | 0.479 | 0.324 | 0.417 |
| Environment | **0.276** | **0.379** | 0.336 | 0.416 | 0.354 | 0.436 | 0.392 | 0.456 | 0.351 | 0.403 |
| Health | **1.553** | **0.850** | 1.970 | 0.992 | 2.436 | 1.221 | 2.598 | 1.201 | 2.736 | 1.241 |
| Security | 72.475 | 4.084 | **70.441** | **4.005** | 79.598 | 4.597 | 84.324 | 4.765 | 93.245 | 5.173 |
| Social Good | **0.838** | **0.516** | 1.036 | 0.573 | 1.126 | 0.618 | 1.141 | 0.581 | 1.430 | 0.651 |
| Traffic | **0.161** | **0.289** | 0.271 | 0.405 | 0.281 | 0.407 | 0.341 | 0.451 | 0.406 | 0.468 |

| Models | Aurora (10% few-shot) |  | GPT4MTS (10% few-shot) |  | TATS (10% few-shot) |  | CALF (10% few-shot) |  | TimeVLM (10% few-shot) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Metric | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE |
| Agriculture | **0.212** | **0.293** | 7.277 | 1.695 | 5.793 | 1.512 | 0.275 | 0.344 | 0.332 | 0.365 |
| Climate | **0.862** | **0.746** | 1.015 | 0.821 | 1.033 | 0.828 | 1.428 | 0.970 | 1.477 | 0.983 |
| Economy | **0.016** | **0.099** | 0.274 | 0.424 | 0.232 | 0.390 | 0.034 | 0.150 | 0.273 | 0.414 |
| Energy | **0.230** | **0.329** | 0.948 | 0.730 | 1.408 | 0.893 | 0.473 | 0.536 | 0.331 | 0.433 |
| Environment | **0.265** | **0.372** | 0.738 | 0.596 | 0.652 | 0.564 | 0.334 | 0.397 | 0.437 | 0.472 |
| Health | **1.343** | **0.776** | 3.885 | 1.377 | 2.781 | 1.167 | 1.762 | 0.939 | 1.947 | 0.992 |
| Security | **70.062** | **3.988** | 81.078 | 4.670 | 85.677 | 4.858 | 181.619 | 7.312 | 103.113 | 5.344 |
| Social Good | **0.814** | **0.494** | 10.579 | 1.716 | 11.612 | 1.500 | 1.037 | 0.457 | 1.017 | 0.527 |
| Traffic | **0.157** | **0.290** | 3.013 | 1.340 | 2.613 | 1.121 | 0.334 | 0.422 | 0.280 | 0.397 |

We have the following important observations:

1. In the zero-shot comparisons, Aurora consistently outperforms time series foundation models, demonstrating the effectiveness of multimodal modeling.
2. In the 10%

### Response for W1, W2, Q1, Q2
Thanks for the suggestions. According to the suggested ablation studies, we conduct additional experiments to study on the modality ablations and finer ablations of modality-guided attention. Since we have considered the modality absence phenomena in model design and training phases, so each corresponding multimodal modules can be directly removed to conduct the experiments in a zero-shot paradigm. 

Specifically, we make ablation studies on six variants, including three modality variants (Time-Only, Time + Text, Time + Image) and three variants of modality-guided attention (Text-Guidance, Image-Guidance, without the learnable metric W). These experiments can provide more details about how each part influences the performance. We report the full results here and have revised the draft (see Tables 18—19 in Appendix D):

| Models | Aurora |  | Time-Only |  | Time + Text |  | Time + Image |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Metrics | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE |
| Agriculture | **0.272** | **0.348** | 0.337 | 0.382 | 0.304 | 0.355 | 0.294 | 0.351 |
| Climate | **0.865** | **0.749** | 1.287 | 0.926 | 1.167 | 0.904 | 1.228 | 0.897 |
| Economy | **0.033** | **0.146** | 0.064 | 0.198 | 0.046 | 0.167 | 0.039 | 0.152 |
| Energy | **0.255** | **0.370** | 0.324 | 0.426 | 0.292 | 0.413 | 0.285 | 0.406 |
| Environment | **0.276** | **0.379** | 0.352 | 0.404 | 0.334 | 0.397 | 0.325 | 0.394 |
| Health | **1.553** | **0.850** | 2.305 | 1.147 | 1.962 | 0.987 | 1.874 | 0.972 |
| Security | **72.475** | **4.084** | 92.822 | 5.092 | 81.294 | 4.800 | 77.928 | 4.628 |
| Social Good | **0.838** | **0.516** | 1.387 | 0.692 | 1.018 | 0.576 | 1.037 | 0.572 |
| Traffic | **0.161** | **0.289** | 0.345 | 0.472 | 0.271 | 0.418 | 0.198 | 0.334 |

| Models | Aurora |  | Text-Guidance |  | Image-Guidance |  | w/o W |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Metrics | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE |
| Agriculture | **0.272** | **0.348** | 0.287 | 0.350 | 0.279 | 0.353 | 0.274 | 0.351 |
| Climate | **0.865** | **0.749** | 0.885 | 0.767 | 0.898 | 0.785 | 0.876 | 0.755 |
| Economy | **0.033** | **0.146** | 0.040 | 0.157 | 0.038 | 0.154 | 0.034 | 0.148 |
| Energy | **0.255** | **0.370** | 0.274 | 0.387 | 0.262 | 0.374 | 0.265 | 0.376 |
| Environment | **0.276** | **0.379** | 0.294 | 0.386 | 0.285 | 0.389 | 0.280 | 0.381 |
| Health | **1.553** | **0.850** | 1.750 | 0.944 | 1.688 | 0.923 | 1.568 | 0.859 |
| Security | **72.475** | **4.084** | 75.742 | 4.382 | 76.922 | 4.482 | 73.294 | 4.187 |
| Social Good | **0.838** | **0.516** | 0.882 | 0.545 | 0.868 | 0.531 | 0.848 | 0.522 |
| Traffic | **0.161** | **0.289** | 0.184 | 0.296 | 0.188 | 0.304 | 0.166 | 0.293 |

We have the following important observations:

1. In the modality variants, using the single time modality leads to the worst performance in the multimodal forecasting scenarios. And adding either Text or Image modality can improve the performance

### Response for W3
Thanks for this question! As far as we know, foundation models that support forecasting can often naturally support anomaly detection, and some unimodal foundation models are evaluated in some benchmarks [1] to demonstrate this point.  However, multimodal anomaly detection is yet a new task, and lacks high-quality labels for evaluating accuracy, so that we do not conduct corresponding experiments. We set this as an important and promising future work, and thanks for your valuable suggestions again!

[1] TAB: Unified Benchmarking of Time Series Anomaly Detection Methods

### Response for W2
Thanks for this insightful advice! The ill-modality problem you mentioned exactly has practical significance. In our work, since the textual modality is exogenous, we have considered the issue of its absence during the model design and training phases, and our model also achieves SOTA on unimodal datasets, so that the potential problems of text can be handled well. 

Considering the endogenous image modality, which relies on the time series data, we have also designed some mechanisms to ensure the robustness when facing unreliable scenarios that FFT fails:

1. When the periodicity is vague and FFT fails, we adopt the patch size as the alternative.
2. If the time series is too short, even shorter than one Patch, we will set the periodicity as the whole length.

The above mechanisms are applied both in pretraining and inference phases, so that the imaging process of time series is robust. And some experimental results have also demonstrated the effectiveness:

1. The datasets Security, ILI, NYSE, and Exchange have no periodicity and exhibit drift phenomena, while Aurora shows competitive performance on them. **You can refer to the Tables 1—3 of our revised paper for the results.**
2. The 8,068 short-term datasets in TFB are very short, with short input lengths (8 — 24), while Aurora achieves the state-of-the-art performance on them against all baselines, including zero-shot foundation models and full-shot small models. **You can refer to the Figure 5 and Tables 10—11 in our revised paper.**

### Response for W1
Thanks for this valuable suggestion! Actually, we have ever studied the prototype scalability, though we did not report the results initially. Specifically, we have tried variants of 500, 1000, and 5000 and choose 1000 as the default setting. We provide the results as follows and have revised the draft (see Table 17 in Appendix D):

| Models | 500 |  | 1000 |  | 5000 |  |
| --- | --- | --- | --- | --- | --- | --- |
| Metrics | MSE | MAE | MSE | MAE | MSE | MAE |
| Agriculture | 0.288 | 0.364 | 0.272 | 0.348 | **0.269** | **0.344** |
| Climate | 0.893 | 0.760 | 0.865 | **0.749** | **0.863** | 0.752 |
| Economy | 0.034 | 0.152 | 0.033 | 0.146 | **0.032** | **0.144** |
| Energy | 0.271 | 0.391 | **0.255** | **0.370** | 0.260 | 0.373 |
| Environment | 0.302 | 0.413 | 0.276 | 0.379 | **0.268** | **0.372** |
| Health | 1.587 | 0.866 | **1.553** | **0.850** | 1.561 | 0.854 |
| Security | 75.017 | 4.118 | 72.475 | 4.084 | **71.551** | **4.036** |
| Social Good | 0.862 | 0.547 | 0.838 | 0.516 | **0.833** | **0.507** |
| Traffic | 0.187 | 0.304 | **0.161** | **0.289** | 0.164 | 0.296 |

We observe that when the size of PrototypeBank increases from 500 to 1000, the performance of downstream tasks improves a lot. But when the size achieves 5000, there exists a phenomenon of marginal improvement, and some settings even have worse performance. Therefore, we choose to use 1000 as the default setting to preserve both the accuracy and efficiency. 

Following your advice, we further visualize the 1000 learned prototypes in our revised draft, **please refer to the Figure 14 in Appendix C.2.** It is observed that the diversity of these 1000 prototypes is relatively high, which is helpful for generating the proper prototypes for forecasting.

### Response for Q2
We have provided specific examples in our revised draft. **Please refer to Figures 10—13 in Appendix C.1.** Among them, **Figures 10 and 11 indicate the cases that datasets from distinct domains possess similar historical time series but dissimilar future values. In Figures 12 and 13, the cases show that datasets from similar domains can even show dissimilar future values**, It is proving that this phenomenon is universal. So that, considering the multimodal knowledge in forecasting is essential.

### Response for Q1
Thanks for this insightful question. From our perspective, using the proposed Prototype-Guided Flow Matching can better utilize the multimodal information in the following three aspects:

1. Like most generative models, Aurora also integrates the multimodal information in condition networks, thus can model the conditional probabilistic distributions.
2. Based on the motivation that the future trends and periods are implied by multimodal information, we propose the Prototype-Guided mechanism to adaptively generate prototypes as the starting points by using visual and textual information, which can help the flow matching head forecast accurately.
3. Current end-to-end multimodal models often adopt decoders like unimodal models, i.e., MLP-based flatten heads. And they simply fuse multimodal information through extra MLPs in the decoding parts, which are not proper in foundation models.

Actually, we have tried other mechanisms like VAE, Diffusion, and Normalized Flow, though we did not report the results initially. Empirically, all of them are not as strong as the proposed Prototype-Guided Flow Matching. We list the comparison results as follows:

| Models | Aurora |  | VAE |  | Diffusion |  | Normalization Flow |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Metrics | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE |
| Agriculture | **0.272** | **0.348** | 0.347 | 0.388 | 0.289 | 0.367 | 0.301 | 0.354 |
| Climate | **0.865** | **0.749** | 1.261 | 0.927 | 1.317 | 0.894 | 0.992 | 0.783 |
| Economy | **0.033** | **0.146** | 0.065 | 0.278 | 0.125 | 0.402 | 0.075 | 0.341 |
| Energy | **0.255** | **0.370** | 0.273 | 0.395 | 0.261 | 0.375 | 0.258 | 0.381 |
| Environment | **0.276** | **0.379** | 0.347 | 0.448 | 0.351 | 0.460 | 0.328 | 0.427 |
| Health | **1.553** | **0.850** | 1.648 | 0.872 | 1.577 | 0.863 | 1.781 | 0.901 |
| Security | **72.475** | **4.084** | 83.821 | 4.692 | 74.951 | 4.633 | 93.182 | 5.029 |
| Social Good | **0.838** | **0.516** | 1.055 | 0.608 | 0.982 | 0.503 | 1.152 | 0.617 |
| Traffic | **0.161** | **0.289** | 0.247 | 0.382 | 0.195 | 0.304 | 0.197 | 0.311 |

### Response for W3
Following your advice, we introduce TTM in related works and baselines, and then compare its performance with Aurora in Table 2 (Deterministic Forecasting). Note that TTM is a deterministic model, which cannot support probabilistic forecasting. **You can refer to the revised draft for more information.** We also list its performance here:

| Models |  | Aurora |  | TTM |  |
| --- | --- | --- | --- | --- | --- |
| Metric |  | MSE | MAE | MSE | MAE |
| ETTm1 | 96 | **0.294** | **0.351** | 0.738 | 0.541 |
|  | 192 | **0.331** | **0.374** | 0.698 | 0.547 |
|  | 336 | **0.359** | **0.391** | 0.670 | 0.533 |
|  | 720 | **0.398** | **0.414** | 0.660 | 0.550 |
|  | Avg | **0.346** | **0.383** | 0.692 | 0.543 |
| ETTm2 | 96 | **0.179** | **0.270** | 0.226 | 0.309 |
|  | 192 | **0.232** | **0.307** | 0.311 | 0.360 |
|  | 336 | **0.275** | **0.337** | 0.350 | 0.383 |
|  | 720 | **0.338** | **0.380** | 0.446 | 0.435 |
|  | Avg | **0.256** | **0.324** | 0.333 | 0.372 |
| ETTh1 | 96 | **0.340** | **0.381** | 0.364 | 0.389 |
|  | 192 | **0.377** | **0.405** | 0.386 | 0.407 |
|  | 336 | **0.399** | **0.422** | 0.404 | 0.422 |
|  | 720 | 0.428 | 0.450 | **0.424** | **0.448** |
|  | Avg | **0.386** | **0.415** | 0.395 | 0.417 |
| ETTh2 | 96 | **0.259** | **0.325** | 0.277 | 0.335 |
|  | 192 | **0.324** | **0.370** | 0.334 | 0.373 |
|  | 336 | **0.360** | **0.401** | 0.362 | 0.402 |
|  | 720 | **0.403** | **0.441** | 0.408 | 0.444 |
|  | Avg | **0.337** | **0.384** | 0.345 | 0.389 |
| Weather | 96 | **0.160** | **0.207** | 0.183 | 0.242 |
|  | 192 | **0.202** | **0.247** | 0.229 | 0.285 |
|  | 336 | **0.252** | **0.288** | 0.289 | 0.330 |
|  | 720 | **0.307** | **0.327** | 0.359 | 0.370 |
|  | Avg | **0.230** | **0.267** | 0.265 | 0.307 |
| Electricity | 96 | **0.134** | **0.234** | 0.166 | 0.263 |
|  | 192 | **0.161** | **0.258** | 0.191 | 0.286 |
|  | 336 | **0.193** | **0.287** | 0.237 | 0.336 |
|  | 720 | **0.224** | **0.320** | 0.292 | 0.384 |
|  | Avg | **0.178** | **0.275** | 0.222 | 0.317 |
| Traffic | 96 | **0.435** | **0.314** | 0.514 | 0.347 |
|  | 192 | **0.465** | **0.328** | 0.543 | 0.373 |
|  | 336 | **0.525** | **0.355** | 0.575 | 0.389 |
|  | 720 | **0.670** | **0.411** | 0.622 | 0.433 |
|  | Avg | **0.524** | **0.352** | 0.564 | 0.386 |
| Solar | 96 | **0.185** | **0.272** | 0.863 | 0.664 |
|  | 192 | **0.198** | **0.282** | 0.823 | 0.695 |
|  | 336 | **0.211** | **0.294** | 0.835 | 0.741 |
|  | 720 | **0.218** | **0.307** | 0.738 | 0.738 |
|  | Avg | **0.203** | **0.289** | 0.815 | 0.710 |
| PEMS08 | 96 | **0.463** | **0.513** | 1.284 | 0.888 |
|  | 192 | **0.599** | **0.577** | 1.638 | 1.039 |
|  | 336 | **0.560** | **0.546** | 1.979 | 1.160 |
|  | 720 | **0.629** | **0.570** | 2.020 | 1.175 |
|  | Avg | **0.563** | **0.552** | 1.730 | 1.066 |
| Wind | 96 | **0.951** | **0.664** | 1.077 | 0.701 |
|  | 192 | **1.115** | **0.747** | 1.350 | 0.825 |
|  | 336 | **1.229** | **0.799** | 1.473 | 0.891 |
|  | 720 | **1.309** | **0.840** | 1.447 | 0.899 

### Response for W2
Following your advice, we visualize the 1,000 learned prototypes in PrototypeBank **in Figure 14 of Appendix C.2. You can also refer to the Figures 15—17 in Appendix C.3, which involve 28 specific visualization cases in forecasting.** 

It is observed that Aurora can retrieve-then-generate proper prototypes for predictions, which contains periodic or trend implications for future horizons.

### Response for W1
Thanks for the insightful suggestions. In the generation process, the quality of texts is exactly important so we do adopt some techniques to ensure that. After a GPT4 agent generates the textual descriptions, we first **coarsely check the quality with another GPT4 agent**. If the quality is low, the process will be redone. After a batch of textual descriptions are generated, **we randomly sample from them (5%) and check the quality manually**, then determine whether to regenerate this batch of data and tune the prompts. We think this process does not involve data leakage problem because we only input GPT4 with the contextual time series in a single conversation.

**We further clarify the pretraining datasets we use in Figure 7 of Appendix A.1** in the revised draft, including the ratios of domains, the specific datasets used, and the lengths and sources of them. We also revise the corresponding texts to add more implementation details. **Note that there exists no overlap in pretraining and testing datasets.**

### Response for Ethics Concerns
We did not use LLM in writing. As we mentioned in the section "THE USE OF LARGE LANGUAGE MODELS (LLMS)", we only involved LLM in our methodology. 

The example you mentioned is a definition of the metric NMAE, **which is widely defined in a large number of papers. Therefore, to avoid potential content overlapping problems, we rewrite such definitions in the Appendix through manually adjusting the grammar and syntax, which may make them look like LLM-generated texts and cause misunderstandings.** We feel sorry about this, we will make more professional revision later.

### Response for Benchmarks
Thanks for your valuable suggestions. First, we want to clarify that not all forecasting tasks adopt the input-96-output-720 setting, that is, prediction is not always 7.5 times the input length. In TSFM-Bench and TimeMMD, the evaluation protocols are different across datasets, including multiple horizons (6, 8, 10, 12, 24, 36, 48, 60, 96, 192, 336, 720). Second, **we have included some multimodal short-term forecasting scenarios** in our original submission version, e.g., Agriculture, Climate, Economy, Security, Social Good and Traffic in TimeMMD are all short-term forecasting datasets, and Aurora shows SOTA performance on these settings. 

To demonstrate the performance of Aurora on more unimodal short-term forecasting scenarios, we follow your advice to conduct additional experiments on short-term benchmarks:

1. We **add two more short-term benchmarks**, i.e.,TFB, and EPF. In TFB, there exists 8,068 short-term datasets with different frequencies. In EPF, there exists five datasets about electricity prices, which are widely used in short-term forecasting. For EPF, the forecasting horizon is fixed as 24.
2. We **add datasets NYSE and ILI (illness)** separately in evaluations on zero-shot deterministic forecasting and zero-shot probabilistic forecasting tasks. For NYSE and ILI, the forecasting horizons are (24, 36, 48, 60).

**Please refer to the newly-added Table 4 (EPF) and Figure 5 (TFB) in the main text of our revised draft,** they report the performance of Aurora on EPF and TFB. Results show that Aurora **outperforms all foundation models on EPF, and achieves competitive performance against end-to-end full shot models like TimeXer.** It is because TimeXer can additionally utilize the covariates in EPF to help forecast, while Aurora only inputs the target variable and makes forecasts. On TFB, Aurora **consistently outperforms all the baselines**, with the lowest mean MASE and msMAPE values on 8,068 short-term datasets. **We show the results of EPF here:**

|Models|Aurora||Sundial||VisionTS||ROSE||MOIRAI||
|------|---------|---------|---------|---------|--------|-----|-----|-----|------|-----|
|Metric|MSE|MAE|MSE|MAE|MSE|MAE|MSE|MAE|MSE|MAE|
|NP|0.288|0.312|**0.256**|**0.277**|0.510|0.461|0.666|0.536|0.660|0.538|
|PJM|**0.084**|**0.183**|0.088|0.189|0.251|0.366|0.311|0.402|0.330|0.423|
|BE|**0.361**|**0.257**|0.371|0.270|0.679|0.457|0.815|0.514|0.837|0.534|
|FR|**0.387**|**0.206**|0.392|0.207|0.625|0.393|0.746|0.447|0.751|0.454|
|DE|**0.539**|**0.475**|0.541|0.484|0.961|0.687|1.276|0.778|1.251|0.779|

|Models|Aurora||TimeXer||iTransformer||PatchTST||TimesNet||
|------|---------|---------|---------|---------|------------|-----|--------|-----|--------|-----|
|Metric|MSE|MAE|MSE|MAE|MSE|MAE|MSE|MAE|MSE|MAE|
|NP|0.288|0.312|**0.238**|**0.268**|0.265|0.300|0.267|0.284|0.250|0.289|
|PJM|**0.084**|**0.183**|0.088|0.188|0.097|0.197|0.106|0.209|0.097|0.195|
|BE|**0.361**|0.257|0.374|**0.241**|0.394|0.270|0.403|0.264|0.419|0.288|
|FR|0.387|**0.206**|**

### Response for Full-shot Settings
Thanks for the valuable suggestions. Following your advice, we include 8 advanced small models, i.e., TimeKAN (2025), AMD (2025), TimePro (2025), TimeXer (2024), Fredformer (2024), iTransformer (2024), PatchTST (2023), and TimesNet (2023). We compare them with Aurora (zero-shot) on commonly-used unimodal datasets and report the mean results as follows:

| Models | Aurora | TimeKAN | AMD | TimePro | TimeXer | Fredformer | iTransformer | PatchTST | TimesNet |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Metric | MSE | MSE | MSE | MSE | MSE | MSE | MSE | MSE | MSE |
| ETTm1 | **0.346** | 0.384 | 0.389 | 0.391 | 0.375 | 0.385 | 0.407 | 0.387 | 0.400 |
| ETTm2 | **0.256** | 0.282 | 0.278 | 0.281 | 0.278 | 0.281 | 0.288 | 0.281 | 0.291 |
| ETTh1 | **0.386** | 0.431 | 0.438 | 0.438 | 0.431 | 0.448 | 0.454 | 0.469 | 0.458 |
| ETTh2 | **0.337** | 0.391 | 0.371 | 0.377 | 0.378 | 0.378 | 0.383 | 0.387 | 0.414 |
| Weather | **0.230** | 0.245 | 0.254 | 0.252 | 0.254 | 0.256 | 0.258 | 0.266 | 0.259 |
| Electricity | 0.178 | 0.197 | 0.187 | **0.169** | 0.180 | 0.178 | 0.178 | 0.216 | 0.193 |
| Traffic | 0.524 | 0.455 | 0.500 | 0.447 | 0.447 | 0.434 | **0.428** | 0.555 | 0.620 |

| Models | Aurora | TimeKAN | AMD | TimePro | TimeXer | Fredformer | iTransformer | PatchTST | TimesNet |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Metric | MAE | MAE | MAE | MAE | MAE | MAE | MAE | MAE | MAE |
| ETTm1 | **0.383** | 0.401 | 0.396 | 0.401 | 0.391 | 0.398 | 0.410 | 0.400 | 0.406 |
| ETTm2 | **0.324** | 0.330 | 0.323 | 0.326 | 0.323 | 0.324 | 0.332 | 0.326 | 0.333 |
| ETTh1 | **0.415** | 0.429 | 0.430 | 0.438 | 0.432 | 0.435 | 0.448 | 0.455 | 0.450 |
| ETTh2 | **0.384** | 0.412 | 0.397 | 0.404 | 0.403 | 0.403 | 0.407 | 0.407 | 0.427 |
| Weather | **0.267** | 0.273 | 0.280 | 0.276 | 0.277 | 0.278 | 0.278 | 0.281 | 0.287 |
| Electricity | 0.275 | 0.286 | 0.281 | **0.262** | 0.274 | 0.270 | 0.270 | 0.304 | 0.295 |
| Traffic | 0.352 | 0.318 | 0.324 | 0.302 | 0.295 | 0.289 | **0.282** | 0.362 | 0.336 |

The zero-shot performance of Aurora can outperform full-shot small models on most cases, and achieves competitive performance on Electricity and Traffic. **Please refer to Table 15 in Appendix B of our revised draft for full results.**

### Response for Baselines
Thanks for this question. In our original submission version, we have compared Aurora (10% few-shot) with most advanced full-shot end-to-end multimodal models, i.e., TimeVLM (2025), CALF (2025), GPT4MTS (2025) and TATS (2025). **Less data usage and stronger performance have demonstrated the advantages of Aurora.** 

Following your advice, we conduct additional experiments on TimeMMD with small models, i.e., iTransformer, PatchTST, TimesNet and DLinear, which possess different model structures. We also consider different budgets in few-shot learning, i.e., 10% and 20%.

| Models | Aurora (Zero) |  | Aurora (10%) |  | PatchTST (10%) |  | iTransformer (10%) |  | TimesNet (10%) |  | DLinear (10%) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Metric | MSE | MAE | **MSE** | **MAE** | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE |
| Agriculture | 0.272 | 0.348 | **0.212** | **0.293** | 5.793 | 1.512 | 7.127 | 1.676 | 7.594 | 1.757 | 10.631 | 2.157 |
| Climate | 0.865 | 0.749 | **0.862** | **0.746** | 1.033 | 0.828 | 1.257 | 0.915 | 1.338 | 0.938 | 1.150 | 0.875 |
| Economy | 0.033 | 0.146 | **0.016** | **0.099** | 0.232 | 0.390 | 0.179 | 0.339 | 0.278 | 0.437 | 0.523 | 0.589 |
| Energy | 0.255 | 0.370 | **0.230** | **0.329** | 1.408 | 0.893 | 2.666 | 1.185 | 4.202 | 1.546 | 1.234 | 0.858 |
| Environment | 0.276 | 0.379 | **0.265** | **0.372** | 0.652 | 0.564 | 0.562 | 0.520 | 0.564 | 0.513 | 0.812 | 0.742 |
| Health | 1.553 | 0.850 | **1.343** | **0.776** | 2.781 | 1.167 | 2.595 | 1.121 | 3.143 | 1.259 | 2.403 | 1.035 |
| Security | 72.475 | 4.084 | **70.062** | **3.988** | 85.677 | 4.858 | 76.893 | 4.428 | 82.246 | 5.518 | 83.689 | 5.881 |
| Social Good | 0.838 | 0.516 | **0.814** | **0.494** | 11.612 | 1.500 | 6.492 | 1.142 | 6.534 | 1.180 | 5.631 | 1.199 |
| Traffic | 0.161 | 0.289 | **0.157** | **0.290** | 2.613 | 1.121 | 2.291 | 1.032 | 2.821 | 1.252 | 2.642 | 1.251 |

| Models | Aurora (Zero) |  | Aurora (10%) |  | PatchTST (20%) |  | iTransformer (20%) |  | TimesNet (20%) |  | DLinear (20%) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Metric | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE |
| Agriculture | 0.272 | 0.348 | **0.212** | **0.293** | 1.557 | 0.804 | 1.644 | 0.822 | 1.887 | 0.881 | 4.713 | 1.632 |
| Climate | 0.865 | 0.749 | **0.862** | **0.746** | 1.542 | 1.013 | 1.531 | 1.005 | 1.524 | 1.009 | 1.417 | 0.971 |
| Economy | 0.033 | 0.146 | **0.016** | **0.099** | 0.036 | 0.152 | 0.079 | 0.148 | 0.047 | 0.177 | 0.158 | 0.326 |
| Energy | 0.255 | 0.370 | **0.230** | **0.329** | 1.555 | 0.943 | 1.433 | 0.883 | 1.403 | 0.909 | 1.277 | 0.861 |
| Environment | 0.276 | 0.379 | **0.265** | **0.372** | 0.485 | 0.494 | 0.476 | 0.488 | 0.510 | 0.492 | 0.801 | 0.726 |
| Health | 1.553 | 0.850 | **1.343** | **0.776** | 2.420 | 1.071 | 2.364 | 1.070 | 2.530 | 1.216 | 2.416 | 1.128 |
| Security | 72.475 | 4.084 | **70.062** | **3.988** | 82.684 

### Response for inference time
Thanks for your advice. Since Aurora is a large multimodal foundation model, we mainly focus on its few-shot and zero-shot efficiency on downstream tasks. To make a fair comparison, we compare Aurora (zero-shot) and Aurora (10% few-shot) with full-shot supervised models, i.e., TimeXer, PatchTST, iTransformer, and TimesNet. We report the training time and inference time of them on datasets with different scales, i.e., ETTh1, ETTm2, Weather, Electricity, and Traffic. **Please refer to the Table below or the Figure 9 in Appendix A.7 of our revised draft.**

| Datasets | Aurora (Zero-shot) |  | Aurora (10% few-shot) |  | TimeXer |  | iTransformer |  | PatchTST |  | TimesNet |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Metrics | Training Time | Inference Time | Training Time | Inference Time | Training Time | Inference Time | Training Time | Inference Time | Training Time | Inference Time | Training Time | Inference Time |
| ETTh1 | 0 | 4.728 | 148.925 | 4.728 | 46.471 | 1.22 | 34.285 | 1.029 | 21.133 | 0.991 | 105.977 | 1.912 |
| ETTm2  | 0 | 12.825 | 282.958 | 12.825 | 92.019 | 4.712 | 72.703 | 5.288 | 71.09 | 4.919 | 249.692 | 7.073 |
| Weather  | 0 | 26.811 | 707.382 | 26.811 | 174.909 | 4.764 | 78.961 | 5.133 | 265.171 | 10.856 | 705.421 | 14.967 |
| Electricity | 0 | 109.773 | 1471.924 | 109.773 | 354.459 | 6.775 | 158.857 | 8.889 | 1373.411 | 22.723 | 1428.109 | 78.912 |
| Traffic | 0 | 275.921 | 2974.827 | 275.921 | 676.938 | 11.016 | 262.631 | 24.696 | 2783.825 | 38.924 | 3855.15 | 186.625 |

It is observed that the inference time of zero-shot Aurora (no training required) is consistently and largely less than the total time (training time + inference time) of full-shot models, demonstrating the strong efficiency with accurate performance. Considering the 10% few shot Aurora, though its time cost is a bit more than TimesNet, it can lead to strong performance in most cases.

### Response for Experiment Setting and Performance
Thanks for your insightful suggestions. Following the convention in time series analytics, we use the normalized results of MSE and MAE. We would like to clarify that the values of normalized MSE and MAE greater than 0.5 does not necessarily mean that the forecasting results are straight lines or random outputs. To demonstrate it, we conduct an experiment to compare Aurora with NaiveMean and NaiveRepeat on PMES08, Traffic, and Wind, where the **NaiveMean** outputs a straight line with the mean values of normalized input time series, and the **NaiveRepeat** outputs another straight line with the last value of normalized input time series. The results are shown as:

| Models | Horizons | Aurora |  | Timer |  | NaiveMean |  | NaiveRepeat |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Metric |  | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE |
| Traffic | 96 | **0.435** | **0.314** | 0.625 | 0.580 | 1.410 | 0.805 | 2.714 | 1.077 |
|  | 192 | **0.465** | **0.328** | 0.798 | 0.661 | 1.413 | 0.806 | 2.747 | 1.085 |
|  | 336 | **0.525** | **0.355** | 0.910 | 0.716 | 1.429 | 0.809 | 2.788 | 1.094 |
|  | 720 | **0.670** | **0.411** | 1.131 | 0.824 | 1.451 | 0.813 | 2.809 | 1.097 |
|  | Avg | **0.524** | **0.352** | 0.866 | 0.695 | 1.426 | 0.808 | 2.765 | 1.088 |
| PEMS08 | 96 | **0.463** | **0.513** | 0.946 | 0.659 | 2.213 | 1.259 | 1.480 | 0.914 |
|  | 192 | **0.599** | **0.577** | 1.142 | 0.758 | 2.305 | 1.260 | 2.452 | 1.246 |
|  | 336 | **0.560** | **0.546** | 1.300 | 0.830 | 1.834 | 1.053 | 2.032 | 1.074 |
|  | 720 | **0.629** | **0.570** | 1.417 | 0.884 | 1.990 | 1.108 | 2.288 | 1.163 |
|  | Avg | **0.563** | **0.552** | 1.201 | 0.783 | 2.086 | 1.170 | 2.063 | 1.099 |
| Wind | 96 | **0.951** | **0.664** | 0.388 | 0.409 | 1.145 | 0.750 | 1.253 | 0.725 |
|  | 192 | **1.115** | **0.747** | 0.778 | 0.613 | 1.308 | 0.820 | 1.552 | 0.847 |
|  | 336 | **1.229** | **0.799** | 1.200 | 0.792 | 1.527 | 0.899 | 1.836 | 0.950 |
|  | 720 | **1.309** | **0.840** | 1.584 | 1.000 | 1.723 | 0.968 | 2.145 | 1.053 |
|  | Avg | **1.151** | **0.763** | 0.988 | 0.704 | 1.426 | 0.859 | 1.697 | 0.894 |

We have the following important observations:

1. Timer’s pre-training datasets do not overlap with these three datasets, while the values of normalized MSE and MAE are also greater than 0.5. So that values greater than 0.5 may not necessarily indicate poor forecasts.
2. It is observed that such naive cases cause the collapse of performance, about **25% —500% worse** than Aurora. 

**You can also find more intuitive showcases in our revised draft, please see Figures 15 (f), (h), (j) in Appendix C.3, where Aurora accurately predicts the periods and trends on these datasets, instead of straight lines or random outputs.**

### Aurora: Towards Universal Generative Multimodal Time Series Forecasting


## Meta review / decision
### Paper Decision
Accept (Poster)

## PDF extracted text (first pages)
```text
Published as a conference paper at ICLR 2026
AURORA:TOWARDSUNIVERSAL GENERATIVE
MULTIMODAL TIME SERIES FORECASTING
Xingjian Wu, Jianxin Jin, Wanghui Qiu, Peng Chen, Yang Shu, Bin Yang, Chenjuan Guo B
East China Normal University
{xjwu,jxjin,onehui,pchen}@stu.ecnu.edu.cn,
{yshu,byang,cjguo}@dase.ecnu.edu.cn
ABSTRACT
Cross-domain generalization is very important in Time Series Forecasting because
similar historical information may lead to distinct future trends due to different
domain-specific characteristics. Recent works focus on building unimodal time
series foundation models and end-to-end multimodal supervised models. Since
domain-specific knowledge is often contained in modalities like texts, the for-
mer lacks the explicit utilization of them, thus hindering the performance; and
the latter is tailored for end-to-end scenarios and does not support zero-shot in-
ference for cross-domain scenarios. In this work, we introduce Aurora,the first
Multimodal Time Series Foundation Model, which supports multimodal inputs and
zero-shot inference. Pretrained on Cross-domain Multimodal Time Series Corpus,
Aurora adaptively extracts and focuses on key domain knowledge contained in
corresponding text or image modalities, thus possessing strong cross-domain gen-
eralization capability. Through tokenization, encoding, and distillation, Aurora
extracts multimodal domain knowledge as guidance and then utilizes a Modality-
Guided Multi-head Self-Attention to inject them into the modeling of temporal
representations. In the decoding phase, the multimodal representations are used
to generate the conditions and prototypes of future tokens, contributing to a novel
Prototype-Guided Flow Matching for generative probabilistic forecasting. Com-
prehensive experiments on 5 well-recognized benchmarks, including TimeMMD,
TSFM-Bench, ProbTS, TFB, and EPF, demonstrate the consistent state-of-the-art
performance of Aurora on both unimodal and multimodal scenarios.
https://github.com/decisionintelligence/Aurora.
https://huggingface.co/DecisionIntelligence/Aurora.
1 INTRODUCTION
Time series forecasting has gained sustained attention for decades of years due to its significant
values in multiple domains, including economy, transportation, meteorology, and public health.
In recent years, the key pivot comes with the surge of deep learning, which brings the boom of
merticulously-designed deep forecasting models (Cirstea et al., 2022; Nie et al., 2023; Qiu et al.,
2025e; Wu et al., 2025d). Through learning the inherent dynamics within the raw data, deep learn-
ing models can outperform classic statistical methods (Box & Pierce, 1970; Mei et al., 2014) and
obey the scaling law (Shi et al., 2024a; Yao et al.). Due to the success, it also brings the most
commonly-used forecasting paradigm, which utilizes the past information to infer how the series
goes in the coming horizon. Although this paradigm contributes to impressive performance under
domain-specific scenarios, its effectiveness is uncertain when facing cross-domain inference, where
similar historical information may lead to different futures due to domain differences.
As shown in Figure 1, current research of time series forecasting explores the cross-domain adap-
tation in two main perspectives: 1) pre-training on cross-domain time series corpus for unimodal
time series foundation models, which partially possess cross-domain generalization capabilities;
1
Published as a conference paper at ICLR 2026
Cross-Domain Multimodal Time Series Corpus
  
  
time
time time
time
Time Series Forecasters
A traffic flow time series of a major 
urban highway in Los Angeles. The data 
shows a strong cyclical pattern with 
daily peaks during morning rush hours 
and evening rush hours, followed by 
troughs during late-night hours.
A series of daily temperatures in 
Chicago during late autumn. Suddenly, 
due to an early Arctic cold front 
sweeping across the Midwest, the 
temperature drops sharply above 15°C 
within a short period.
...
Pretrained End-to-End Unimodal Multimodal
Initialized
Backbone
PatchTST
TimesNet
Pathformer
DLinear
CALF
TATS
GPT4MTS
TimeVLM
Aurora
(Ours)
Sundial
ROSE
LightGTS
VisionTS
Initialized
Backbone
Pretrained
Backbone
Pretrained
Backbone
......
...
Figure 1: Aurora is pretrained oncross-domain
multimodaltime series corpus, supporting both
text and image information to enhance zero-shot
time series forecasting.
2) utilizing cross-modality information in train-
ing end-to-end multimodal supervised mod-
els, which effectively integrates domain knowl-
edge in forecasting. For time series founda-
tion models, the cross-domain generalization
capabilities mainly come from the sensitivity
to subtle differences in historical information
from different domains. Some of them (Shi
et al., 2024b; Liu et al., 2025e) are pretrained
on trillion-scale corpus with heavy backbones,
thus possessing certain cross-domain adaption
capabilities. Others (Wang et al., 2025f;e; Wu
et al., 2025a) have specific structures, which ex-
cels at capturing cross-domain features. How-
ever, their capabilites come from single time
modality and lack explict domain knowledge
guidance, thus hindering the performance. For
end-to-end multimodal supervised models (Jin
et al., 2024; Liu et al., 2025b), though they con-
sider the multimodal knowledge to enhance the
domain-specific forecasting, they lack the abil-
ity to support zero-shot forecasting in cross-
domain scenarios. In our view, theauroraof
next-generation time series foundation model lies in pretraining a cross-modality model on cross-
domain time series corpus, which canutilize the domain knowledge within modalities and serve as
a versatile out-of-the-box forecaster in complex scenarios.
See Figure 1, we proposeAurora, which pioneers the exploration of multimodal time series founda-
tion model. Specifically, we pretrain Aurora on Cross-Domain Multimodal Time Series Corpus, with
time series data and sample-wise, domain-specific text descriptions. Since previous works (Chen
et al., 2024a; Yu et al., 2025c) point out the endogenous images of time series contain additional
geometric information, we also consider them into cross-modality learning. Considering the model
architecture, Aurora adopts a novel cross-modality Encoder. Taking pretrained Bert (Devlin et al.,
2019) and ViT (Liu et al., 2021) as modality encoders, Aurora then adopts token distillation to extract
the key information in different modalities. To effectively model the cross-modality interaction, we
propose a novelModality-Guided Self-Attention Mechanismto utilize the external domain knowl-
edge to adjust the attention of internal information within the time series data to obtain temporal
features, and then fuse them with text and image features.
In the Aurora Decoder, we devise a novel flow-matching to fully utilize the fused cross-modality
features to support multimodal cross-domain generative probabilistic forecasting. First, we use a
ConditionDecoder to generate multimodal conditions for flow matching. Since the future trend
of time series is often implied by external text information, and the inherent periodicity of time
series is often contained in the endogenous images, we then design a Prototype Bank initialized by
Period and Trend prototypes, and leverage a PrototypeRetriever to retrieve the “future prototypes”
based on the inherent domain knowledge from texts and images. Compared with DDPM (Ho et al.,
2020), Flow Matching (Lipman et al., 2023) serves as a stochastic interpolant, which can start from
a random distribution instead of a Gaussian noise, with more flexibilities. We take the generated
future prototypes as starting points, which contains the rudiments of periodicity and trend for future
tokens, thus can simplify the flow matching process. Our contributions are summarized as follows:
• We propose a multimodal time series foundation model, called Aurora, which is pretrained on
cross-domain multimodal time series corpus and supports generative probabilistic forecasting.
Through effectively fusing multimodal information during pretraining, Aurora serves as a strong
zero-shot forecaster, and can make accurate cross-domain inference.
• We devise a novel cross-modality encoder in Aurora, consisting of token distillation and modal-
ity guiding, implemented by merticulously-designed attention structures. It can enhance the
temporal representations while effectively fusing representations from texts and images.
2
Published as a conference paper at ICLR 2026
• We design a novel flow-matching process in the Aurora Decoder. It obtains multimodal condi-
tions through a Transformer, and obtains future prototypes containing periodic and trend infor-
mation as the starting points, thus enhancing the ability of flow-matching.
• Experimentally, Aurora achieves state-of-the-art performance on 5 well-recognized bench-
marks, including datasets from TimeMMD (Liu et al., 2024b), TSFM-Bench (Li et al., 2025c),
ProbTS (Zhang et al., 2024), TFB (Qiu et al., 2024), and EPF (Olivares et al., 2023), cover-
ing comprehensive scenarios, i.e., unimodal, multimodal, deterministic, and probabilistic, thus
demonstrating a strong out-of-the-box tool of decision intelligence.
2 RELATED WORKS
2.1 TIMESERIESFORECASTING
Time Series Forecasting is vital in decision-making and has fascinated people for decades of years,
which facilitates the emergence of a series of works. In recent years, deep-learning models are
widely studied, among them, Autoformer (Wu et al., 2021), Triformer (Cirstea et al., 2022), Times-
Net (Wu et al., 2023), Pathformer (Chen et al., 2024b), PatchTST (Nie et al., 2023), Dlinear (Zeng
et al., 2023), FiTS (Xu et al., 2024), SparseTSF (Lin et al., 2024a), PDF (Dai et al., 2024a),
DUET (Qiu et al., 2025e), and TimeMixer++ (Wang et al.), continuously advancing the state-of-
the-arts. However, though they possess the capabilities to extract the inherent dynamics in raw
time series data, they only adapt to unimodal end-to-end forecasting scenarios, and often fall short
in multimodal forecasting scenarios where the domain knowledge is widely contained in the text
modality.
Recently, some works are proposed to explore the multimodal end-to-end supervised models. In
summary, they utilize Large Language Models’ strong reasoning capabilities to integrate textual
domain knowledge to prompt temporal modeling. Among them, Unitime (Liu et al., 2024c), Time-
LLM (Jin et al., 2024) and CALF (Liu et al., 2025b) utilize the endogenous textual descriptions as
prompts, GTP4MTS (Jia et al., 2024), TATS (Li et al., 2025d) and TimeMMD (Liu et al., 2024b)
supports exogenous textual domain knowledge. However, they do not possess generalization capa-
bilities in zero-shot scenarios.
2.2 TIMESERIESFOUNDATIONMODELS
To support cross-domain generalization, unimodal Time Series Foundation Models are widely stud-
ied. The majority of them adopt Tranformer-based architectures, which are pretrained on time se-
ries corpus of billion- or trillion- scale to obtain the strong generalization capabilities. Among
them, Sundial (Liu et al., 2025e), VisionTS (Chen et al., 2024a), ROSE (Wang et al., 2025f), Light-
GTS (Wang et al., 2025e),Time-MoE (Shi et al., 2024b), MOIRAI (Woo et al., 2024), TTM (Ekam-
baram et al., 2024), Chronos (Ansari et al.), UniTS (Gao et al., 2024), Timer (Liu et al., 2024e),
and TimesFM (Das et al., 2024) demonstrate strong zero-shot forecasting performance on unimodal
tasks, even outperforming those full-shot supervised models in many cases. Considering the fore-
casting paradigm, Sundial, MOIRAI, Chronos, and Lag-Llama (Rasul et al., 2023) also support
probabilistic forecasting, which provides additional robustness and versatility for decision-making.
Despite their endeavors to enhance cross-domain generalization capabilities, when historical series
exhibit similarities, the forecasts they generate remain static. This lack of adaptability renders them
unable to accommodate the diverse and changing real-world domains.
In this work, we propose Aurora to pioneer the exploration of multimodal time series foundation
models. Through pretraining on Cross-Domain Multimodal Time Series Corpus, Aurora can extract
the key domain knowledge within the text and image modalities to enhance the modeling of temporal
features. Aurora also supports generative probabilistic forecasting, thus covering versatile tasks,
including unimodal, multimodal, deterministic and probabilstic forecasting.
3 AURORA
In this work, we pretrain Aurora in a cross-modality paradigm, which adopts Channel-
Independence (Nie et al., 2023) on time series data, and models corresponding multimodal inter-
3
Published as a conference paper at ICLR 2026
Here’s the stock price series of NVIDIA. 
In 9:00 a.m,  NVIDIA announces a 
partnership with OpenAI to integrate its 
next-generation GPUs into large-scale AI 
training infrastructure.
time
periods
time
image
time
text
 TextEncoder
VisionEncoder
Tokenizer
Tokenizer
Tokenizer
MSA
Add&Norm
Add&Norm
FFN
Q
K
V
VisionDistiller 
TextDistiller
...
TextGuider
VisionGuider
...
Modality-Guided Multi-
head Self-Attention
...
...
...
 Aurora
Encoder
Modality
Fuser
Aurora
Decoder
time
...
Prototype Bank
...
...
 PrototypeRetriever
Period Trend
MSA
Add&Norm
Add&Norm
FFN
Q
K
V
Mask
Causal-Transformer                   Cross-Transformer
ConditionDecoder
L x️
MCA
Add&Norm
Add&Norm
FFN
L x️
Q
K
V
RoPE
Prototype-Guided 
Flow Matching
i
3
2
1...
......
...
Flow-Matching Net
Condition
Prototype
Time &
Noise
Velocity
i
2
1
......
K x️
Sinusoidal
Figure 2: The overview of Aurora. In the Aurora Encoder, the multimodal information is extracted,
distilled, and fused. Modality-Guided Multi-head Self-Attention is introduced to inject the domain-
specific knowledge into temporal modeling. In the Aurora Decoder, the Prototype-Guided Flow
Matching is introduced to support generative probabilistic forecasting.
action to inject domain knowledge. Note that each variable of time series is first normalized through
Instance Normalization (Ulyanov et al., 2016) to mitigate the value discrepancy. As shown in Fig-
ure 2, Aurora mainly consists of two phases: 1) in Aurora Encoder, we tokenize and encode each
modality into modal features, then fuse them to form multimodal representations; 2) in Aurora De-
coder, we utilize a Condition Decoder to obtain the multimodal conditions of future tokens, leverage
a Prototype Retreiver to retrieve the future prototypes based on the domain knowledge, and conduct
flow matching on them to make generative probabilistic forecasts.
3.1 ENCODING
3.1.1 MULTIMODALTOKENIZATION
Aurora inherits the strong encoding capabilities from ViT (Liu et al., 2021) and Bert (Devlin
et al., 2019) to extract the representations from images and texts, and adopts a temporal Channel-
Independent Transformer as the main backbone. Therefore, inputs of all modalities are required to
be tokenized first.
Given a univariate time seriesX∈R T , we adopt RevIN (Kim et al., 2021) technique to mitigate
the inherent non-stationarity of time series. The time series tokensX time are formed through non-
overlapped Patching and Embedding (Cirstea et al., 2022; Nie et al., 2023):
X ′ =LeftPad(X), X P =Patching(X ′)∈R ntime×ptime
,(1)
X time =Embedding(X P )∈R ntime×dtime
,(2)
where Embedding is a linear projection,X time ∈R ntime×dtime
are the embeded time series tokens,
withn time representations of dimensiond time.
4
Published as a conference paper at ICLR 2026
To obtain the endogenous image tokens, we utilize the rendering techniques (Chen et al., 2024a) to
make the transformation:
A=Amp(FFT(X)),F=argmax(A),P =⌈T /F⌉,(3)
˜X=LeftPeriodPad(X,P), X 2D =Reshape( ˜X)∈R m×P,(4)
X3D =Resize(Repeat(X 2D))∈R 3×w×h,(5)
˜X3D =ImagePatching(X 3D)∈R
nimage×3× w
pimage × h
pimage (6)
X image =Embedding(Flatten(( ˜X3D))∈R nimage×dimage
,(7)
where the time series is first processed into 2D structureX 2D ∈R m×P based on the periodP.
Then the endogenous imageX 3D ∈R 3×w×h is rendered through repeatingX 2D along channel
dimension, and resizing into the standard input size of ViT. Finally, the image tokensX image ∈
Rnimage×dimage
are obtained through ImagePatching and Embedding.
For the corresponding texts, the text tokensX text ∈R ntext×dtext
can be easily obtained through
tokenization and retrievement from the vocabulary of Bert.
3.1.2 TOKENDISTILLATION
After obtaining the tokens from all the modalities, the hidden representations of texts and images
are then generated through the pretrained VisionEncoder (ViT) and TextEncoder (Bert):
˜X image =VisionEncoder(X image)∈R nimage×dimage
,(8)
˜X text =TextEncoder(X text)∈R ntext×dtext
(9)
Inituitively, there exists informative redundancy in texts and images for multimodal time series fore-
casting. For texts as additional domain knowledge, key descriptions which can affect the future
trend of time series often deserve only several words. For the endogenous image, we consider it as
a technique to extract the varying inherent periodic information in time series data from multiple
domains, where the information is also sparse. Therefore, we distill the tokens from text and image
modalities to extract the key information and improve the efficiency:
Ximage =VisionDistiller(R image, ˜X image)∈R Kimage×dimage
,(10)
Xtext =TextDistiller(R text, ˜X text)∈R Ktext×dtext
,(11)
where VisionDistiller and TextDistiller are based on the Multi-head Cross-Attention Mechanism.
TheR image ∈R Kimage×dimage
andR text ∈R Ktext×dtext
are learnable vectors (withK text <
ntext, Kimage < n image), which are the queries and can serve as semantic clustering cen-
troids (Zhang & Yan, 2022) to help compress the information in ˜X image and ˜X text. AndX image
andX text are the distilled image and text tokens.
3.1.3 MULTIMODALALIGNMENT
In multimodal time series forecasting, the time series modality occupies the dominant role and
information from other modalities can serve as domain-specific knowledge to guide the extraction
of temporal representations, thus enhancing the cross-domain generalization capability. In Aurora,
we explicitly implement the above informative flow through a Modality-Guided Multi-head Self-
Attention mechanism. First, we capture the correlations between the time series modality and others
through Cross-Attention based VisionGuider and TextGuider:
V Attn=VisionGuider(X time,X image)∈R ntime×K image
,(12)
TAttn=TextGuider(X time,X text)∈R ntime×K text
,(13)
Corr=V Attn·W·TAttn T ∈R ntime×ntime
,(14)
where V Attn and TAttn are unnormalized attention scores, separately denoting the correlations be-
tween time modality and image or text modality. Corr∈R ntime×ntime
denotes the inherent correla-
tions inside the time series modality, bridged through the text-image correlations. We also introduce
5
Published as a conference paper at ICLR 2026
W∈R Kimage×K text
as a learnable metric (Qiu et al., 2025e) to further tune the semantic distances.
Therefore, this process helps bridge the correlations between time series tokens via a perspective of
multimodal domain information. We then inject Corr into the temporal encoding process:
Q=X time ·W Q, K=X time ·W K, V=X time ·W V (15)
S= (Q·K T +Corr)/
√
dtime, O=Softmax(S)·V,(16)
Onorm =LayerNorm(X time +O),(17)
Xtime =LayerNorm(FeedForward(O norm) +O norm),(18)
whereW Q, W K, W V ∈R dtime×dtime
.X time ∈R ntime×dtime
denotes the generated temporal
representations. The Corr matrix contains domain knowledge, which guides the attention scores to
focus on the appropriate time series tokens (empirically validated in Section C.4). Finally, we fuse
the representations from three modalities through a Cross-Attention based modality fuser:
˜Ximage =CrossAttn(X time,X image)∈R ntime×dtime
,(19)
˜Xtext =CrossAttn(X time,X text)∈R ntime×dtime
,(20)
Xf use = Xtime + ˜Ximage + ˜Xtext,(21)
whereX f use ∈R ntime×dtime
are the fused multimodal representations.
3.2 DECODING
3.2.1 CONDITIONDECODING
Inspired by DiT (Peebles & 
```
