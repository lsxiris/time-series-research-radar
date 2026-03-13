# CoRA: Boosting Time Series Foundation Models for Multivariate Forecasting through Correlation-aware Adapter — OpenReview Raw Thread

- Forum: https://openreview.net/forum?id=JRlNrcTllN
- PDF: https://openreview.net/pdf?id=JRlNrcTllN
- Section: 二、时间序列预测：分布鲁棒、多变量建模与后处理优化
- Zhihu score: 6.0
- Venue status: ICLR 2026 Poster

## Submission metadata
- Authors: Hanyin Cheng, Xingjian Wu, Yang Shu, Zhongwen Rao, Lujia Pan, Bin Yang, Chenjuan Guo
- Primary area: learning on time series and dynamical systems
- Keywords: Multivariate Time Series Forecasting, Time Series Foundation Models, Correlation

## Abstract
Most existing Time Series Foundation Models (TSFMs) use channel independent modeling and focus on capturing and generalizing temporal dependencies, while neglecting the correlations among channels or overlook the different aspects of correlations. However, these correlations play a vital role in Multivariate time series forecasting. To address this, we propose a Correlation-aware Adapter (**CoRA**), a lightweight plug-and-play method that requires only fine-tuning with TSFMs and is able to capture different types of correlations, so as to improve forecast performance. Specifically, to reduce complexity, we innovatively decompose the correlation matrix into low-rank Time-Varying and Time-Invariant components. For the Time-Varying component, we further design learnable polynomials to learn dynamic correlations by capturing trends or periodic patterns. To learn positive and negative correlations that appear only among some variables, we introduce a novel dual contrastive learning method that identifies correlations through projection layers, regulated by a Heterogeneous-Partial contrastive loss during training, without introducing additional complexity in the inference stage. Extensive experiments on 10 real-world datasets demonstrate that CoRA improves the state-of-the-art TSFMs in average forecast performance.

## Reviews
### Reviewer_k2Aw
- summary: This paper proposes CoRA (Correlation-aware Adapter), a lightweight, plug-and-play module designed to enhance existing Time Series Foundation Models (TSFMs) for multivariate forecasting. The central premise is that many TSFMs, while powerful in capturing temporal dependencies, neglect the complex inter-channel correlations that are vital for accurate multivariate prediction in downstream tasks. The main contributions of the paper can be summarized as follows:
1. A Unified Framework for Complex Correlations: The paper provides a structured view by categorizing inter-channel relationships into t
- strengths: This paper proposes CoRA, a novel correlation-aware adapter designed to enhance the multivariate forecasting capabilities of Time Series Foundation Models (TSFMs) on specific downstream tasks.
1. Originality: The paper is the first to propose a unified framework that simultaneously addresses the dynamic, heterogeneous, and partial aspects of inter-channel correlations.
2. Quality: The paper is of high quality, featuring a rigorous methodology, clear theoretical derivations, and practical efficie
- weaknesses: This paper could be improved in the following areas:
1. Lack of Direct Experimental Validation for Partial Correlation (PCorr): The paper claims to model three types of correlations: DCorr, HCorr, and PCorr. While experiments provide strong evidence for DCorr (e.g., Fig. 7) and HCorr (separation of positive/negative spaces), the validation for PCorr is less direct. The ablation study (Table 2) shows the overall benefit of the HPCL module but does not disentangle the specific contributions of modeling HCorr versus PCorr. The visualization in Fig. 7 implicitly shows PCorr through clustering but fails to highlight or analyze it separately.
2. Omission of Experimental Details: The paper states that the thresholdεis a "learnable" parameter but does not detail how it is optimized. Furthermore, the main results in Table 1 are based solely on a 5% few-shot setting. It is suggested that the authors include experiments conducted with full-dataset fine-tuning.
3. Confusing Notation: The authors u
- questions: 1. Regarding the Explicit Validation of Partial Correlation (PCorr): The paper's core thesis is the unified modeling of DCorr, HCorr, and PCorr. While the evidence for DCorr and HCorr is quite direct, the support for PCorr modeling appears more implicit. Could you provide a more direct piece of evidence to demonstrate that CoRA is effectively learning and leveraging partial correlations?
2. Regarding the Optimization of the Learnable Threshold ε: Could you please clarify the specific mechanism that allows gradients to flow back toεduring the training process?
3. Regarding Performance in Data-Rich Scenarios: The main experiments are conducted in a 5% few-shot setting. However, how does CoRA perform when fine-tuned on the full training dataset (100% data)? Does the performance gap between th
- rating: 8 | confidence: 5

### Reviewer_iXBW
- summary: This paper proposes a way to fine-tune multivariate time series foundation models as to better capture correlation between variables. Key ideas are to estimate a correlation matrix between features that has a time-dependent and time-invariant decomposition, and to screen for which variables to actually focus on in terms of positive or negative correlations via a contrastive learning strategy.
- strengths: - I appreciate that the paper is trying to separately handle different types of correlation (DCorr, HCorr, PCorr)
- I find the idea of using a time-varying and time-invariant decomposition to be valuable, along with the idea of finding pairs of features with strong enough positive or negative correlation
- The experimental results appear to be very impressive (although as pointed out in weaknesses, I would like to see more baselines and some additional experiments)
- weaknesses: - At least in how it is stated now, it's hard for me to see why Theorem 1 should hold since equation (15) in Theorem 1 disagrees with equation (5) and the decomposition showed earlier in Figure 3.
- In stating theoretical guarantees, I would suggest also providing intuition for why the guarantee should hold (this intuition should be in the main paper and not in an appendix/supplemental material as it helps the reader understand/interpret the guarantee) and whether the proof uses any nontrivial ideas, or if it's largely just based on an existing result. Maybe I'm missing something but Theorem 2 seems to be a known result regarding polynomial approximation using a variant of the mean value theorem? If the result was not previously known, what are the closest known existing theoretical results (which can help provide the reader with point(s) of comparison as to what proof techniques/ideas are novel)? Also can you comment on the extent to which the assumption holds for real data?
- Experim
- questions: Please see weaknesses (I raised a number of concerns there).
- rating: 2 | confidence: 4

### Reviewer_bdjv
- summary: To address the limitation that existing time series foundation models often overlook inter-channel modeling, this paper proposes a lightweight adapter, termed CoRA. CoRA innovatively decomposes the correlation matrix into time-varying and time-invariant components. It leverages learnable polynomials to capture dynamic patterns and introduces a novel dual contrastive learning mechanism to distinguish between positive and negative correlations. Optimized via a heterogeneous-local contrastive loss, CoRA incurs minimal computational overhead during the inference stage. Empirical results demonstrat
- strengths: 1. The paper is well-motivated, addressing the critical challenge of modeling complex inter-channel dependencies in multivariate time series.
2. The manuscript is well-written, featuring clear and consistent notation throughout.
3. The empirical evaluation demonstrates that CoRA consistently surpasses state-of-the-art baselines across a diverse set of real-world datasets.
- weaknesses: 1. The projection layers are not much different from the related modeling methods in existing methods (such as TSMixer [1]), a more detailed clarification is needed.
2. The set of baselines for comparison is not comprehensive, as it omits recent state-of-the-art foundation models like TimerXL [2].	
3. Discuss and comparison with classical baselines (e.g., PatchTST  [3], Leddam [4], iTransformer [5], Autoformer [6], DLinear [7]) is suggested.

*[1] TSMixer: An All-MLP Architecture for Time Series Forecasting.*

*[2] Timer-XL: Long-Context Transformers for Unified Time Series Forecasting.*

*[3] A Time Series is Worth 64 Words: Long-term Forecasting with Transformers.*

*[4] Revitalizing Multivariate Time Series Forecasting: Learnable Decomposition with Inter-Series Dependencies and Intra-Series Variations Modeling.*

*[5] iTransformer: Inverted Transformers Are Effective for Time Series Forecasting.*

*[6] Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series
- questions: 1. How does CoRA, as a plug-and-play module, accommodate the fundamental architectural differences between encoder-only and encoder-decoder models, particularly with respect to their distinct training objectives and inference processes?
2. What is the underlying rationale for incorporating rule-based correlation relationships when the model is already designed to capture these dependencies through a learnable mechanism?
- rating: 8 | confidence: 4

### Reviewer_TnwM
- summary: This paper introduces CoRA, a lightweight and plug-and-play module designed to enhance Time-Series Foundation Models (TSFMs) by better modeling inter-channel correlations. CoRA employs a correlation decomposition mechanism combining global time-invariant matrices and learnable polynomial bases, capturing both static and dynamic dependencies. Importantly, CoRA does not require re-pretraining of the base TSFM and can be applied during few-shot fine-tuning, making it a practical adaptation method.
- strengths: 1. Clear Motivation and Positioning:
The paper clearly identifies a key limitation in existing TSFM-based forecasting—insufficient modeling of heterogeneous inter-channel correlations—and proposes a theoretically grounded yet efficient mechanism to address this.

2. Lightweight and Practical Design:
CoRA's plug-in design allows easy integration with existing TSFMs during fine-tuning without requiring re-pretraining. Its parameter efficiency and low inference overhead make it appealing to practit
- weaknesses: 1. Limited Empirical Evaluation Scope:
Table 1 focuses on few-shot MSE benchmarks using standard datasets but lacks evaluation under out-of-distribution shifts, missing channels, or nonstationary regimes—critical aspects for real-world TSFM deployment.
Figure 4 presents relative MSE changes, which obscures absolute performance deltas; including absolute values alongside relative improvements (as in Table 1) would increase transparency.

2. Assumption Boundaries Underexplored:
Theoretical guarantees rely on local stationarity and bounded smoothness assumptions that may not hold in volatile domains (e.g., finance, IoT, environmental data). The paper does not examine edge cases such as abrupt regime shifts or high-noise inputs.

3. Potential Overstatement of Generality:
The paper claims CoRA "captures various correlations with O(N) inference complexity." While this is theoretically sound, real-world multivariate systems may involve nonlinear or hierarchical dependencies that exceed the cu
- questions: 1. Statistical Significance and Robustness:
Are the improvements in Tables 1 and 2 statistically significant? Please report standard deviations, confidence intervals, or results across multiple random seeds to validate robustness.

2. Adaptation in Nonstationary Environments:
How does CoRA behave under regime shifts or nonstationary dynamics where the global time-invariant assumption may break down? Could it be extended to support online updates or adaptive windowing?

3. Scalability to Very High-Dimensional Settings:
For extremely large N (> 500), do global correlation matrices introduce memory or numerical bottlenecks? Any empirical or theoretical evidence on efficiency and convergence at that scale?

4. Extensibility Beyond Forecasting:
Could the proposed correlation decomposition frame
- rating: 6 | confidence: 3

## Author comments / rebuttal
### Rebuttal Summary (Pre-Incident Scores: 8, 6, 8, 8; Average 7.5)
**Dear Reviewers, ACs, SACs, and PCs,**

We sincerely appreciate your dedication to this conference.

We were sorry to learn about the recent technical issues with OpenReview, and we fully support the remedial actions proposed by the committee. Fortunately, thanks to the diligence and responsiveness of our reviewers, we had essentially concluded our meaningful discussions by **Nov. 25**, well prior to the incident on **Nov. 27**.


To facilitate your final assessment, we have summarized **the score evolution**, **the acknowledged on key strengths**, and **the outcomes of the rebuttal discussion** below:

**1. Score improvement as of Nov. 25.**

|Reviewer| Changes of Score| Date of Change|Score Changes History Link|
|-|:-:|:-:|:-:|
|**k2Aw**|8 $\textcolor{green}{➜}$ 8 |-|-|
|**iXBW**|2 $\textcolor{red}{➜}$ 6|**Nov. 24**|https://openreview.net/revisions?id=hhItBSo2Mo|
|**bdjv**|8 $\textcolor{green}{➜}$ 8|-|-|
|**TnwM**|6 $\textcolor{red}{➜}$ 8|**Nov. 23**|https://openreview.net/revisions?id=et89TmFFlA|
|**Average**|6.0 $\textcolor{red}{➜}$ 7.5|**Nov. 24**|

**2. Acknowledged on Strengths.**

It is encouraging to see that reviewers agree on the following strengths of our work:

- **High Quality & Clear Motivation**: The work is well-motivated, addressing critical challenges with rigorous methodology, clear notation, and high writing quality. (bdjv, TnwM, k2Aw)

- **Novel Unified Framework**: The first to simultaneously address dynamic, heterogeneous, and partial correlations through a theoretically grounded decomposition. (k2Aw, iXBW)

- **Practical & Lightweight Design**: An efficient, plug-in design that allows easy integration with TSFMs for fine-tuning without high overhead. (k2Aw, TnwM)


**3. Summary of Discussion and Rebuttal Outcomes.**

During the rebuttal phase, we addressed the reviewers' concerns through:
- **Additional experiments**: We extended backbones and evaluated robustness in OOD, non-stationary, and high-noise settings to ensure a comprehensive evaluation.
- **Detailed theoretical explanations**: We provided intuition for **Theorems 1 & 2** and discussed the validity of our assumptions on real data.
- **Manuscript refinement**: Corrected typographical errors and improved clarity.

We are pleased that **Reviewers iXBW, bdjv, and TnwM** have explicitly confirmed that **their concerns were addressed**, supporting our work by **raising or maintaining their positive scores**.

We once again thank all reviewers for keeping active communication with us throughout the rebuttal period and for their support of our work, and we look forward to the further assessment of our submission.

Best regards, 

Authors of CoRA

### Author comment
Dear Reviewer iXBW:

We sincerely appreciate the valuable suggestions you have dedicated to improving the quality of our manuscript. We are truly delighted to hear that our responses have addressed your main concerns, and we greatly appreciate your support for our work. 

To address these presentation issues and typos, we have made targeted revisions to the manuscript.

For the exposition around line 212-213:

- To address the **grammatical error** and **unclear phrasing** in the original sentence:
    'Where, $\boldsymbol{R}$ denotes the rule-based correlation matrix.' We have revised it to: 'Here, $\boldsymbol{R}\in \mathbb{R}^{N\times N}$ denotes the rule-based correlation matrix which is added to the learnable part to incorporate more prior knowledge for enhancing correlation estimation.'

- Regarding **the division by 2** in Equation (5), our original intent was to numerically align the values with the $[−1,1]$ range of the correlation matrix $\boldsymbol{M}_t^{corr}$. However, we agree that this step is procedurally unnecessary. Therefore, we have removed this operation from Equation (5) and revised Figure 3 by adding a depiction of **additive aggregation** to more clearly illustrate the aggregation process.

We have also resolved the issues regarding the non-standard **theorem environment** and corrected the **typos** you mentioned. 

Once again, we express our **sincere appreciation** for your feedback and your thoroughness and attention to detail. We will perform a **thorough proofreading** of the entire paper to ensure high quality.

Best regards,

Authors

### Author comment
Dear Reviewer bdjv:

Thank you so much for your encouraging feedback and for your support toward the acceptance of our paper. We sincerely appreciate your time and constructive comments throughout the review process.

Best regards,

Authors

### Author comment
Dear Reviewer TnwM,

We are thrilled that our responses have effectively addressed your questions and comments. We really appreciate your efforts during this tight review timeline and the recognition of the strengths of our paper. 

Best regards,

Authors

### Author comment
Dear Reviewer bdjv, thank you for providing your detailed and constructive feedback.

---
### Response to W1:
Thank you for your thoughtful comments.

A key distinction from the Channel Mixer layers in TSMixer is that our projection layers operate on the feature dimension( $\mathbb{R}^d \to \mathbb{R}^d$ ） rather than the channel dimension($\mathbb{R}^N \to \mathbb{R}^N$). This design choice allows us to avoid the complexity $\mathcal{O}(N^2)$ associated with the number of channels. Furthermore, to enhance the representational power of these layers, we introduce an adaptive mechanism that aggregates contextual information over time to dynamically compute the projection weights among channels. The specifics of this mechanism are detailed in Equations 6-8.

---
### Response to W2:
Thank you for your valuable and constructive comments.
Following your suggestion, we have added more experiment on fine-tuning CoRA alone and have also evaluated the Timer-XL backbone.

|Method|ETTh1|ETTh2|ETTm1|ETTm2|
|:---|---|---|---|---|
| **Timer-XL** | 0.439  | 0.351  | 0.355  | 0.258  |
| **Timer-XL+CoRA** | **0.434** | **0.345** | **0.349** | **0.250** |


---
### Response to W3:
We sincerely thank you for this constructive feedback.
Our evaluation is specifically based on a 5% fine-tuning regime for the foundation model, which is distinct from the full training used for traditional end-to-end models. Consequently, directly comparing their performance may be inherently inequitable.

Regarding channel relationship modeling, the majority of existing methods adopt a Channel-Independence strategy (PatchTST, Autoformer, DLinear).

Regarding channel relationship modeling, the majority of existing methods adopt a Channel-Independence strategy. While models like Leddam and iTransformer treat individual channels as tokens to facilitate interaction via attention mechanisms, they exhibit significant limitations. First, by treating the entire sequence within a window as a single token, they fail to effectively model the Dynamic Correlation. Second, these methods do not explicitly distinguish between positive and negative correlations, thereby overlooking the Heterogeneous Correlation. Finally, they perform direct interactions across all channels without considering the partial Correlation, making them more susceptible to noise.



---

### Response to Q1:
We appreciate this insightful question. CoRA operates as a non-invasive plugin, avoiding any alterations to the architecture or training objectives of TSFMs. Instead, it leverages the robust representations generated by the backbone, incorporates multiple correlation relationships to inject additional channel information, and performs independent predictions with these enhanced representations to augment the backbone's performance.

---

### Response to Q2:

We are grateful for this opportunity to clarify the design rationale of our model.

The rationale lies in the complementary nature of rule-based and learnable mechanisms

### Author comment
### Response to Q3:
We are grateful for your constructive comments.  Our method features a parameter complexity of $\mathcal{O}(N)$, ensuring that it does not introduce significant memory overhead for high-dimensional time series.  Furthermore, as dimensionality increases, the correlation structure becomes more complex. Explicitly modeling DCorr, HCorr, and PCorr is therefore more beneficial for the model to capture these intricate relationships.

We selected three datasets with more than 500 variables. The MSE and maximum GPU memory usage for these datasets are reported in the table below.

|Dataset|Traffic|$N=862$|Covid-19|$N=948$|Wike2000|$N=2000$|
|:-|:-:|:-:|:-:|:-:|:-:|:-:|
|**Metric**|**MSE**|**Max-GPU-Memroy**|**MSE**|**Max-GPU-Memroy**|**MSE**|**Max-GPU-Memroy**|
|**GPT4TS**|0.441|7.73G|1.972|12.53G|547.024|23.96G|
|**GPT4TS+CoRA**|**0.430**|8.95G|**1.924**|14.24G|**545.315**|28.44G|
|**Moment**|0.453|5.37G|2.356|6.21G|525.352|11.12G|
|**Moment+CoRA**|**0.437**|7.02G|**2.307**|7.89G|**521.468**|17.41G|

The results above show that even for a dataset with 2,000 variables, our method only introduces reasonable memory costs. Moreover, it is still able to learn correlations to a certain degree, leading to performance enhancements for the TSFMs. 


We have also added this analysis to Appendix F.7 (Lines 1232-1244).  We hope our additional experiments can address your concerns.



---

### Response to Q4:
We thank you for this insightful question.
We strongly agree with the idea of generalizing CoRA to other tasks. In fact, we can extend our model to anomaly detection or classification tasks by replacing the linear head used for forecasting in Equation (14) with a reconstruction or classification head.

To explore the capabilities of CoRA on tasks beyond forecasting, we conducted relevant experiments. For anomaly detection, we use the **MSL** and **SMAP** as evaluation datasets [1]. For classification, we select the **FaceDetection**, **Heartbeat**, and **PEMS-SF** as evaluation datasets [2].

For the anomaly detection task, we evaluate performance using the **VUS_ROC** and **VUS_PR** metrics. For the classification task, we use **Accuracy**. The results of all experiments are summarized in the tables below.

|Dataset|MSL||SMAP||
|:-|:-:|:-:|:-:|:-:|
|**Metric**|**VUS-ROC**|**VUS-PR**|**VUS-ROC**|**VUS-PR**|
|**GPT4TS**|0.624|0.195 |0.504|0.147|
|**+CoRA**|**0.628**|**0.200**|**0.510**|**0.149**|
|**Moment**|0.663|0.212|0.474|0.127|
|**+CoRA**|**0.667**|**0.214**|**0.483**|**0.130**|

|Dataset|FaceDetection|Heartbeat|PEMS-SF|
|:-|:-:|:-:|:-:|
|**GPT4TS**|0.683|0.776|0.874|
|**+CoRA**|**0.688**|**0.791**|**0.876**|
|**Moment**|0.675|0.786|0.866|
|**+CoRA**|**0.681**|**0.789**|**0.873**|

The results indicate that although CoRA was not specifically designed for these tasks, its direct application still yields performance improvements. This demonstrates CoRA's effectiveness in enhancing TSFMs by capturing correlation.

We have included this analy

### Author comment
### Response to W2:
We appreciate you for this insightful comment. 

- **For regime shifts**:
To further investigate the model's robustness under regime shifts scene, we conducted experiments across datasets that exhibit varying rates of shift intensity. These rates are calculated following the TFB and are detailed below.

    |Dataset|Weather|ETTh2|NYSE|
    |:-|:-:|:-:|:-:|
    |**Shift Rate**|0.213|0.404|0.620|

    The shift rate ranges from 0 to 1, where a larger value indicates a more significant shift effect. We summarize the MSE results of the relevant experiments in the table below.

    |**Dataset**|**Weather**|**ETTh2**|**NYSE**|
    |:-|:-:|:-:|:-:|
    |**GPT4TS**|0.254|0.377|0.715|
    |**+CoRA**|**0.243**|**0.361**|**0.711**|
    |**Moment**|0.251|0.369|0.763|
    |**+CoRA**|**0.243**|**0.356**|**0.761**|

    Notably, our method achieves consistent gains even under a substantial shift rate of 0.620. This observation
    underscores our model's robustness to regime shifts.

- **For high-noise input**:
    For the analysis of high-noise input environments, we injected noise into the raw data in both fine-tuning and test datasets at intensities of 5%, 15%, 25%, and 35%, respectively, and conducted a comprehensive evaluation.

    |Weather|0%|5%|15%|25%|35%|
    |:-|:-:|:-:|:-:|:-:|:-:|
    |**GPT4TS**|0.254|0.257|0.265|0.271|0.279|
    |**+CoRA**|**0.243**|**0.251**|**0.259**|**0.268**|**0.275**|
    |**Moment**|0.251|0.258|0.262|0.268|0.284|
    |**+CoRA**|**0.243**|**0.254**|**0.257**|**0.262**|**0.280**|

    The results show that our method is capable of adapting to noise within a certain range. Notably, our approach is compatible with most existing denoising techniques, such as the frequency filtering module employed in FilterNet [1], to further mitigate the interference of noise.

[1] FilterNet: Harnessing frequency filters for time series forecasting. NeurIPS 2024

---

### Response to W3:
Thank you for this very important and insightful comment. To address your concerns and ensure the precision of our claims, we revise the manuscript to be more specific. Specifically, we have replaced the general term "various correlations" with more precise phrases such as "the mentioned three types of correlations" in several key locations (e.g., lines 95, 105, and 421). 


---
### Response to Q1:
We appreciate your valuable suggestion. To validate the robustness of CoRA, we have added standard deviations and confidence intervals to Table 1 (Lines 432-454) and Table 2 (Lines 473-482) in the manuscript. 

---
### Response to Q2:
We are grateful for this constructive feedback. Regarding the behavior of CoRA under regime shifts and non-stationary dynamics, please refer to our responses to W2 and W1, respectively.

To extend our method to support online updates or adaptive windowing, we can generate a separate Time-Invariant matrix $\boldsymbol{V}$ for each window independently, utilizing all time points within that window. This capability enha

### Author comment
Dear Reviewer TnwM, thank you for providing your detailed and constructive feedback.

---

### Response to W1:

We appreciate your constructive suggestion to broaden the evaluation scope. We fully agree that real-world TSFM deployment requires robustness against out-of-distribution shifts, missing channels, and nonstationary regimes. We provide a detailed discussion on each of these aspects individually below. 

- **Out-of-distribution shifts:**
    Our method combines both a rule-based and a learnable correlation matrix, which enhances its robustness against shifts. We would also like to clarify that the fine-tuning datasets and the pre-training datasets of TSFMs have already followed the out-of-distribution mechanism.

    To further evaluate our robustness against distribution shifts, we conducted experiments on datasets from the TFB benchmark [1] exhibiting varying degrees of shift intensity. These rates are calculated by computing the Wasserstein Distance [2] between the distributions of the fine-tuning data and test data at each of the following datasets, and are detailed below.
    
    |Dataset|Weather|Electricity|Wike2000|
    |:-|:-:|:-:|:-:|
    |**OOD Rate**|43.63|230.63|1890.06|
    
    The OOD rate ranges from 0 to positive infinity, where a larger value indicates a more significant shift effect. We summarize the MSE results of the relevant experiments in the table below.

    |Dataset|Weather|Electricity|Wike2000|
    |:-|:-:|:-:|:-|
    |**GPT4TS**|0.254|0.207|547.024|
    |**+CoRA**|**0.243**|**0.201**|**545.315**|
    |**Moment**|0.251|0.200|525.352|
    |**+CoRA**|**0.243**|**0.196**|**521.468**|
    
    As observed from the results, CoRA can boost forecasting accuracy, even in scenarios where the Wasserstein Distance between the fine-tuning and testing distributions is as high as 1890.06.

- **Missing channels:**

    Since CoRA avoids explicit global channel interaction during the inference phase, it is inherently capable of accommodating channel missing. We verified this robustness by fine-tuning the model on the complete dataset and conducting evaluations with random channel dropout rates of 10%, 20%, 30%, and 40%.

    |Weather|10% missing|20% missing|30% missing|40% missing|
    |:-|:-:|:-:|:-|:-|
    |**GPT4TS**|0.263|0.259|0.247|0.226|
    |**+CoRA**|**0.256**|**0.248**|**0.234**|**0.223**|
    |**Moment**|0.269|0.257|0.242|0.221|
    |**+CoRA**|**0.260**|**0.250**|**0.230**|**0.217**|

    These results validate our method's ability to handle missing channels and deliver performance gain for TSFMs.

- **Non-stationary regimes:**
    To address the potential challenges posed by non-stationarity, our method inherently incorporates the series normalization strategy used in Non-stationary Transformers [3]. This approach effectively mitigates the adverse impact of non-stationary data on the model.

    To evaluate our capability of handling non-stationary data, we conducted experiments on datasets from TFB with diverse de

### Author comment
### Response to W6: 
We would like to express our sincerest and most profound gratitude for your exceptionally detailed and meticulous review. The time and effort you have dedicated to identifying issues related to exposition, typos, and potential logical inconsistencies are truly remarkable. Your feedback has been invaluable in helping us to significantly improve the clarity and quality of our manuscript.

We have thoroughly revised and proofread the entire manuscript based on your comments. We have carefully rectified all the errors highlighted in your review, including:

- (Line ~17): Corrected "**Cor**relation-aware **A**dapter" to "**CoR**relation-aware **A**dapter" to be consistent with "CoRA".

- (Line ~125): Revised "LLMs enable" to "LLMs to enable."

- (Line ~155 & ~271): Formatted plain text letters like "L" into their proper mathematical variable form, L.

Furthermore, your detailed feedback prompted us to conduct another thorough proofread of the entire manuscript, where we identified and corrected additional similar errors. For example:

- (Line ~76): Corrected "possess" to "possesses".
- (Line ~227): Corrected "are" to "is".
- (Line ~283): Corrected "sapces" to "spaces".

We sincerely thank you again for your tremendous effort in helping us improve the quality of our manuscript.

---

**Thanks for your sincere suggestions again! If you have any additional questions, we can have further discussions!** 😊

### Author comment
### Response to W3:
Thank you for this valuable suggestion. To provide a more comprehensive comparison, we have conducted additional experiments with channel-dependent TSFMs (such as Moirai and UniTS). The Mean Squared Error (MSE) results are summarized in the table below.

|Method|Moirai|Moirai+CoRA|UniTS|UniTS+CoRA|TTM|TTM+CoRA|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|ETT(Avg.)|0.353$\scriptstyle\pm 0.004$|0.344$\scriptstyle\pm 0.002$|0.347$\scriptstyle\pm 0.003$|0.339$\scriptstyle\pm 0.001$|0.342$\scriptstyle\pm 0.003$|**0.329**$\boldsymbol{\scriptstyle\pm 0.002}$|
|Weather|0.257$\scriptstyle\pm 0.003$|0.241$\scriptstyle\pm 0.003$|0.235$\scriptstyle\pm 0.002$|0.220$\scriptstyle\pm 0.002$|0.226$\scriptstyle\pm 0.003$|**0.214**$\boldsymbol{\scriptstyle\pm 0.002}$|
|AQShunyi|0.690$\scriptstyle\pm 0.003$|**0.672**$\scriptstyle\pm 0.002$|0.717$\scriptstyle\pm 0.002$|0.685$\scriptstyle\pm 0.002$|0.701$\scriptstyle\pm 0.003$|0.678$\boldsymbol{\scriptstyle\pm 0.002}$|
|ZafNoo|0.519$\scriptstyle\pm 0.003$|0.497$\scriptstyle\pm 0.001$|0.508$\scriptstyle\pm 0.004$|0.491$\scriptstyle\pm 0.002$|0.505$\scriptstyle\pm 0.003$|**0.483$\boldsymbol{\scriptstyle\pm 0.001}$**|

As the table illustrates, existing foundation models with channel-dependent mechanisms do not always achieve superior performance on downstream tasks. Furthermore, these models yield further performance improvements when integrated with CoRA. 

We have also added this experiment to Appendix F.4 (Lines 1188-1201). 

---

### Response to W4:
We appreciate your valuable suggestion. 
To give a better sense of variability, we have added standard deviations and confidence intervals to Table 1 (Lines 432-454) and Table 2 (Lines 473-482) in the manuscript. 

---

### Response to W5:

Thank you for this insightful question. To analyze how the amount of available fine-tuning data affects performance, we conducted additional experiments using varying amounts of data.
Specifically, we fine-tune the TTM and CALF backbones on the ETTm2 and Weather datasets, using 3%, 5%, 10%, and 20% of the available training data. The MSE results are summarized in the table below.

|Dataset|ETTm2||||Weather||||
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|**Data percentage**|**3%**|**5%**|**10%**|**20%**|**3%**|**5%**|**10%**|**20%**|
|**TTM**|0.263$\scriptstyle\pm 0.005$|0.259$\scriptstyle\pm 0.003$|0.256$\scriptstyle\pm 0.003$|0.250$\scriptstyle\pm 0.002$|0.237$\scriptstyle\pm 0.003$|0.226$\boldsymbol{\scriptstyle\pm 0.002}$|0.224$\scriptstyle\pm 0.002$|0.216$\boldsymbol{\scriptstyle\pm 0.001}$|
|**TTM+CoRA**|**0.261$\scriptstyle\pm 0.004$**|**0.249$\scriptstyle\pm 0.002$**|**0.248$\scriptstyle\pm 0.001$**|**0.245$\scriptstyle\pm 0.001$**|**0.234$\scriptstyle\pm 0.003$**|**0.214$\boldsymbol{\scriptstyle\pm 0.002}$**|**0.212$\boldsymbol{\scriptstyle\pm 0.001}$**|**0.210$\boldsymbol{\scriptstyle\pm 0.001}$**|```
|**CALF**|0.285$\scriptstyle\pm 0.005$|0.274$\scriptstyle\pm 0.003$|0.268$\scriptstyle\pm 0.004$|0.261$\scriptstyle\pm 0.003

### Author comment
### Response to W2:
We sincerely thank you for these constructive comments. Your suggestions on contextualizing our theoretical guarantees are invaluable and have helped us significantly improve the clarity of our manuscript. We address your points below:

**1. Intuition for the Guarantees:**
- **For Theorem 1:** Time-varying correlations can often be modeled as a stable, long-term component (time-invariant part) combined with dynamic fluctuations (time-varying part). A common approach is to decompose the correlation matrix into the sum of two square matrices, representing the time-invariant and time-varying components, respectively. To reduce parameter complexity, we further propose a multiplicative decomposition: $\boldsymbol{Q}_t\boldsymbol{V}\boldsymbol{Q}_t^T$. By learning the low-rank time-varying $\boldsymbol{Q}_t^T$ and time-invariant matrix $\boldsymbol{V}$, our approach attains an expressive power equivalent to the additive approach, yet operates with greater efficiency.

- **For Theorem 2:** If the correlation patterns in a time series evolve smoothly over time, then this smooth evolution can be effectively approximated by a well-behaved mathematical function, such as a polynomial. Taylor's theorem provides the formal basis for this, showing that a higher-degree polynomial can capture more complex dynamics, with the approximation error decreasing accordingly.

We have revised the manuscript to incorporate these intuitions (Lines 212-217 and 234-237).

**2. Purpose of the Proof for Theorem 2:**

We would like to clarify that the purpose of the proof for Theorem 2 is not to use nontrivial ideas, but to provide theoretical support for our primary contribution.

For the learning of Dynamic Correlation, our primary contribution lies in proposing the Time-varying and Time-invariant decomposition and designing learnable polynomials to estimate the time-varying component.

As for Theorem 2, which is an extension of Taylor's theorem with the Lagrange remainder term, we do not emphasize the proof itself as a major contribution; rather, it serves to theoretically demonstrate that accurate correlation estimation can be achieved through the proposed Learnable Time-aware Polynomial.


**3. The extent to which the assumption holds for real data:**
We would like to clarify that the smoothness assumption for $ \mathcal{F}(\boldsymbol{q})$ is well-founded in real-world scenarios, as the underlying reasons of correlation shifts, such as the continuous evolution of traffic flow and gradual system degradation, typically induce smooth drifts in correlations rather than erratic jumps.

In real-world scenarios, by selecting an appropriate degree K, we can ensure that the error incurred by using learnable polynomials to approximate correlations is practically negligible without compromising computational efficiency. We leverage Theorem 2 to theoretically justify this statement:

Empirically, we find that the values of both $\boldsymbol{q}$ and the derivative t

### Author comment
Dear Reviewer iXBW, thank you for providing your detailed and constructive feedback.

---
### Response to W1:
Thank you very much for your valuable feedback and for pointing out this issue. We would like to offer the following clarification and update the manuscript accordingly.

We revised Figure 3 (Lines 204-215) by adding the rule-based correlation part $\boldsymbol{R}$, thereby aligning it more closely with Equation 5.

Equation 5 defines the correlation matrix $\boldsymbol{M}^{corr}_t$ as a composition of a rule-based component $\boldsymbol{R}$ and a learnable component $\boldsymbol{Q}_t\boldsymbol{V}\boldsymbol{Q}_t^T$. Since $\boldsymbol{R}$ is a rule-based term that remains invariant within the window, our analysis primarily focuses on the learnable component $\boldsymbol{Q}_t\boldsymbol{V}\boldsymbol{Q}_t^T$.

The primary purpose of Theorem 1 is to demonstrate that our method effectively decomposes the learnable component of correlation matrix into time-varying and time-invariant components. Specifically, the decomposition scheme $\boldsymbol{Q}_t\boldsymbol{V}\boldsymbol{Q}_t^T$ is functionally equivalent to the conventional additive decomposition [1, 2] like $\boldsymbol{M}_i +  \boldsymbol{M}_v$. Here $\boldsymbol{M}_i$ and $\boldsymbol{M}_v$ denote the time-invariant matrix and time-varying matrix, respectively. 

Accordingly, to enhance the clarity of the manuscript, we have revised the presentation of Theorem 1 (Lines 363-377) and the corresponding content in the Appendix C.1 (Lines 819-837) to focus specifically on demonstrating $\boldsymbol{Q}_t\boldsymbol{V}\boldsymbol{Q}_t^T = \boldsymbol{M}_v +  \boldsymbol{M}_i$. 

Theorem 1 demonstrates that $\boldsymbol{Q}_t\boldsymbol{V}\boldsymbol{Q}_t^T$ can be decomposed into the sum of a time-varying matrix and a time-invariant matrix. Consequently, the correlation matrix $\boldsymbol{M}_t^{corr}$ Equation 5 can also be decomposed into the sum of time-varying and time-invariant.

[1] Graph WaveNet for Deep Spatial-Temporal Graph Modeling. IJCAI 2019

[2] Enhancenet: Plugin neural networks for enhancing correlated time series forecasting. ICDE 2021

### Author comment
Dear Reviewer k2Aw, thank you for providing your detailed and constructive feedback.

---
### Response to W1&Q1:
Thank you very much for your valuable feedback and for pointing out this issue. 

The key to partial correlation is that not every pair of channels is related. Instead, each channel shows significant correlation only with a specific subset of other channels and remains independent of the rest.

As shown in Figure 7 (Lines 1161-1182), the similarity we visualized is sparse in most cases. This indicates that associations are not established between all channels, which aligns with the characteristics of partial correlation.

---
### Response to W2&Q2:
We appreciate you for raising this crucial point regarding the trainability of $\epsilon$.

In the actual implementation, we employ a soft masking technique to ensure gradient backpropagation.

Specifically, to obtain $\boldsymbol{M}_t^{pos}$, apply the following operations to $\boldsymbol{M}_t^{corr}$：

$\boldsymbol{W_{mask}}= \text{sigmoid}(\frac{\boldsymbol{M}_t^{corr} - \epsilon }{1e-5})$

$\boldsymbol{M}_t^{pos} = \boldsymbol{W_{mask}} \odot \boldsymbol{M}_t^{corr}$

where $\boldsymbol{W_{mask}}$ denotes the weights after applying the soft mask. Specifically, values smaller than $\epsilon$ are suppressed towards 0, while those exceeding $\epsilon$ approach 1.

Regarding the experiments using full-dataset fine-tuning, please refer to our response to Q3.

---
### Response to W3:
We sincerely thank you for this helpful suggestion regarding mathematical notation.

We have updated the manuscript to use distinct symbols for clarity. We have carefully checked the text to ensure that the same letter is not used to represent different concepts, regardless of the font style. The notation is now consistent throughout the paper.

---

### Response to Q3:

We thank you for this valuable suggestion regarding the evaluation in data-rich scenarios.

Due to the large-scale parameters and slow training speeds inherent to many TSFMs, it is computationally prohibitive to fine-tune all baseline models on the complete dataset. To analysis the evaluation in data-rich scenarios, we selected two computationally efficient TSFMs as backbones to perform the full-data fine-tuning experiments. The MSE results are summarized as follows:

|**Data**|**5%**||**100%**||
|:-:|:-:|:-:|:-:|:-:|
|**Method**|**CALF**|**CALF+CoRA**|**CALF**|**CALF+CoRA**|
|**ETT(Avg.)**|0.367|**0.356**|0.340|**0.335**|
|**Weather**|0.238|**0.229**|0.227|**0.221**|
|**AQShunyi**|0.732|**0.714**|0.689|**0.675**|
|**Method**|**TTM**|**TTM+CoRA**|**TTM**|**TTM+CoRA**|
|**ETT(Avg.)**|0.342|**0.329**|0.334|**0.327**|
|**Weather**|0.226|**0.214**|0.220|**0.210**|
|**AQShunyi**|0.701|**0.678**|0.682|**0.669**|

Although the performance gap over the baseline narrows in data-rich scenarios, our method still achieve consistent improvements for TSFMs.


---

**Thanks for your sincere suggestions again! If you have any additional questions, we can have fur

### CoRA: Boosting Time Series Foundation Models for Multivariate Forecasting through Correlation-aware Adapter


## Meta review / decision
### Paper Decision
Accept (Poster)

## PDF extracted text (first pages)
```text
Published as a conference paper at ICLR 2026
CORA: B OOSTING TIME SERIES FOUNDATION MOD-
ELS FOR MULTIVARIATE FORECASTING THROUGH
CORRELATION -AWARE ADAPTER
Hanyin Cheng1, Xingjian Wu1, Yang Shu1, Zhongwen Rao 2, Lujia Pan 2
Bin Yang1, Chenjuan Guo 1B
1East China Normal University
2Huawei Noahs Ark Lab
{hycheng,xjwu}@stu.ecnu.edu.cn,
{raozhongwen,panlujia}@huawei.com,
{yshu,byang,cjguo}@dase.ecnu.edu.cn,
ABSTRACT
Most existing Time Series Foundation Models (TSFMs) use channel indepen-
dent modeling and focus on capturing and generalizing temporal dependencies,
while neglecting the correlations among channels or overlooking the different as-
pects of correlations. However, these correlations play a vital role in Multivariate
time series forecasting. To address this, we propose a CoRrelation-aware Adapter
(CoRA), a lightweight plug-and-play method that requires only ﬁne-tuning with
TSFMs and is able to capture different types of correlations, so as to improve
forecast performance. Speciﬁcally, to reduce complexity, we innovatively de-
compose the correlation matrix into low-rank Time-V arying and Time-Invariant
components. For the Time-V arying component, we further design learnable poly-
nomials to learn dynamic correlations by capturing trends or periodic patterns. To
learn positive and negative correlations that appear only among some channels,
we introduce a novel dual contrastive learning method that identiﬁes correlations
through projection layers, regulated by a Heterogeneous-Partial contrastive loss
during training, without introducing additional complexity in the inference stage.
Extensive experiments on 10 real-world datasets demonstrate that CoRA can im-
prove TSFMs in multivariate forecasting performance.
1 I NTRODUCTION
Time Series Foundation Models (TSFMs) that show strong generalization are proposed recently.
Through pre-training on large-scale time series data ( Wang et al., 2025d; Goswami et al., 2024; Liu
et al., 2024e; Wang et al., 2025e) or the use of large language models ( Zhou et al. , 2023; Liu et al. ,
2024d;b; Jin et al. , 2024), these models maintain strong reasoning abilities when handling new or
unseen data.
At the same time, multivariate time series forecasting, as a pivotal domain in data analysis, is widely
applied in various industries ( Qiu et al., 2025c; Wu et al., 2025c; Liu et al., 2026a; Qiu et al., 2025e;
Liu et al., 2026b; Wang et al., 2024b; Qiu et al., 2025b). Properly modeling and utilizing correlations
in multivariate time series can signiﬁcantly improve the performance of forecasting models ( Zhang
& Y an, 2022; Liu et al. , 2024c; Wu et al. , 2020). Based on different interaction characteristics
among channels, as shown in Figure 1a, correlation can be summarized into three aspects: dynamic
correlation (DCorr) describes the variation of channel relationships over time ( Zhao et al. , 2023;
Cirstea et al., 2021); heterogeneous correlation (HCorr) focuses on how channels interact with each
other by considering positive and negative correlations ( Huang et al. , 2023); partial correlation
(PCorr) emphasizes that correlation exists only among certain channels, and modeling interactions
across all channels can easily introduce noise ( Chen et al., 2024; Qiu et al., 2025d; Liu et al., 2024a).
Considering more comprehensive correlations provides richer information for the models.
1
Published as a conference paper at ICLR 2026
However, most existing TSFMs focus on capturing and generalising temporal dependencies and ne-
glect relationships among channels ( Goswami et al. , 2024; Ansari et al. , 2024; Liu et al. , 2024e;b;
Jin et al. , 2024; Shi et al. , 2025). Although some models like TTM ( Ekambaram et al. , 2024b),
UniTS ( Gao et al. , 2024), and Moirai ( Woo et al. , 2024) employ different methods to model the
correlations among channels, they do not comprehensively consider multiple aspects of the correla-
tions. For example, TTM employs an MLP-based channel mixing approach, but the MLP weights
remain unchanged across different time steps, thereby failing to model DCorr while indiscriminately
modelling interactions among all channels, and thus failing to capture HCorr and PCorr explicitly.
Dynamic Correlation (DCorr)
Strong Weak
Heterogeneous Correlation
 (HCorr)
Partial Correlation (PCorr)
(a) Various Correlations (b) Efficient Plugins for Learning Correlations
PipelineVarious Correlations
Pre-trainDownstream
CCMCoRA (ours)
Positive Negative 
Dependent
Independent
Dependent C-LoRA
Projector
E2EM
C-LoRATSFM
CoRA
Projector
TSFM
Projector
Multi-source
E2EM
Single-source 
E2EM CCM (C)
CCM (P)
CCM (C)
CCM (P)
End-to-End Model
E2EM
Time Series 
Foundation Model
TSFM
CCM (C)
CCM Cluster Maker
CCM (P)
CCM Projector
No pre-train
Legend
Figure 1: (a) Illustration of three different types of correlations,
the formal deﬁnitions are provided in Appendix A. (b) Compar-
isons of different plugins for learning correlations
While the attention mecha-
nisms used in UniTS and
Moirai assign different atten-
tion scores at different time
points, they still interact all
channels simultaneously with-
out considering HCorr and
PCorr, thus leading to subopti-
mal correlation modeling. Fur-
thermore, due to the variations
in correlations across different
datasets, it is difﬁcult to capture
generalized correlations during
the pre-training phase ( Ekam-
baram et al., 2024b).
Thus, it motivates us to de-
sign a plugin that can be
ﬁne-tuned alongside TSFMs,
which avoids issues caused by
correlation differences across
datasets during the pre-training
phase. Meanwhile, it possesses
the ability to depict various correlations while also incorporating a lightweight design. However,
this faces a major challenge: balancing the complete modeling of various correlations with the
lightweight design. It is intrinsically difﬁcult to model all three correlations in a uniﬁed manner.
Although some models could address DCorr ( Zhao et al., 2023; Cirstea et al., 2021), HCorr (Huang
et al., 2023) and PCorr ( Qiu et al., 2025d; Liu et al., 2024a) individually, they struggle to effectively
encompass various correlations simultaneously. Moreover, existing channel interaction methods of-
ten rely on MLPs ( Ekambaram et al. , 2023; 2024a), Transformers ( Liu et al. , 2024c; Jiang et al. ,
2023) and GNNs ( Wu et al., 2020; Cai et al. , 2024), etc., which have a time complexity of O(N 2),
where N denotes the number of channels. Some methods ( Zhang & Y an, 2022; Chen et al. , 2024;
Nie et al. , 2024) have made efforts in reducing the complexity. However, end-to-end models such
as Crossformer ( Zhang & Y an, 2022) require modifying or redesigning the entire model structure,
and thus cannot be directly used as plugins for TSFMs. Existing plugins are primarily designed for
end-to-end forecasting models. CCM ( Chen et al. , 2024) requires additional pre-training together
with the end-to-end models before it can be plugged in. C-LoRA ( Nie et al. , 2024) is designed to
be trained with an end-to-end backbone from scratch. Overall, there is a lack of an efﬁcient plugin
speciﬁcally designed for downstream ﬁne-tuning of TSFMs. More importantly, considering various
correlations in these methods would lead to a higher complexity.
To address this, we propose CoRA, a lightweight plug-and-play method that only requires training
on a few samples with TSFMs during the ﬁne-tuning phase. By considering various correlations,
CoRA utilises internal representations and original predictions from TSFMs to generate an enhanced
prediction, as shown in Figure 1b. To complete modeling the mentioned three types of correlation,
we ﬁrst propose the Dynamic Correlation Estimation (DCE) module which can learn dynamic
correlation matrices. Then we design the Heterogeneous-Partial Correlation Contrastive Learn-
ing (HPCL) that uses the correlation matrices from DCE to learn HCorr and PCorr adaptively.
Speciﬁcally, to achieve lightweight, we innovatively decompose the correlation matrices into two
low-rank components: Time-V arying and Time-Invariant in DCE module. To better understand how
DCorr evolves, we propose a learnable polynomial to capture trend or periodic patterns within the
DCorr effectively. Afterwards, to better distinguish of HCorr, we propose channel-aware projec-
2
Published as a conference paper at ICLR 2026
tions to map the representations into positive and negative correlation spaces. The projections are
guided by the novel Heterogeneous-Partial Contrastive Loss during the training process, which en-
ables adaptive learning of PCorr in the two HCorr spaces. As a result, we can capture the mentioned
three types of correlations with linear complexity w.r.t. the number of channels during inference.
Our contributions are summarized as follows:
• We design a universal, lightweight plugin that allows TSFMs to capture the mentioned
three types of correlations without re-pre-training the TSFMs.
• We propose a lightweight Dynamic Correlation Estimation module that explicitly models
the dynamic patterns of correlations in a lightweight manner.
• We propose a novel Heterogeneous-Partial Correlation Contrastive Learning, which learns
HCorr and PCorr through projection layers regulated by dual contrastive loss.
• We conducted extensive experiments on 10 real-world datasets. The results show that
CoRA effectively improves the performance of TSFMs in multivariate forecasting.
2 R ELATED WORK
2.1 F OUNDATION MODELS FOR TIME SERIES FORECASTING
TSFMs for forecasting can be divided into two sections: 1) LLM-based Models: These methods
leverage the strong representational capacity and sequential modeling capability of LLMs to cap-
ture complex patterns for time series modeling. Among them, GPT4TS ( Zhou et al. , 2023) and
CALF (Liu et al., 2025) selectively modify certain parameters of LLMs to enable the model to adapt
to time series data. On the other hand, UniTime( Liu et al. , 2024b), S 2IP-LLM ( Pan et al. , 2024),
LLMMixer (Kowsher et al. , 2025), and Time-LLM ( Jin et al. , 2024) focus on creating prompts to
trigger time series knowledge within LLMs. 2) Time Series Pre-trained Models: Pre-training on
multi-domain time series equips these models with strong generalization capabilities. Among them,
ROSE (Wang et al., 2024a) and Moment ( Goswami et al. , 2024) restore the features of time series
data, enabling them to extract valuable information in an unsupervised manner. On the other hand,
TimesFM (Das et al. , 2024) and Timer ( Liu et al. , 2024e), using an autoregressive approach, em-
ploy next-token prediction to learn time series representations. Generally speaking, most TSFMs
are based on channel-independent strategies, with only a few ( Gao et al. , 2024; Ekambaram et al. ,
2024b; Woo et al., 2024) modeling relatively simple inter-channel relationships. The effects of more
complex correlations in TSFMs remain under-explored.
2.2 C ORRELATION OF CHANNELS IN TIME SERIES FORECASTING
Channel correlation plays a crucial role in enhancing the predictions( Qiu et al., 2025a). They can be
divided into specialized models and plugins from a paradigm perspective. 1) Correlation Models:
These models are typically based on foundational architectures such as MLP ( Ekambaram et al. ,
2024a; 2023), GNN (Shang et al., 2021; Cai et al., 2024), and Transformer (Liu et al., 2024c; Zhang
& Y an, 2022). For example, TSMixer( Ekambaram et al., 2023) and TTM(Ekambaram et al., 2024a)
directly mix all channels using MLP . MTGNN( Wu et al. , 2020) and Ada-MsHyper( Shang et al. ,
2024a) treat different channels as distinct nodes, performing message passing to facilitate channel
interactions. Furthermore, iTransformer( Liu et al. , 2024c) and Crossformer( Zhang & Y an, 2022)
treat different channels as distinct tokens and utilize transformers to realize channel interaction.
2) Correlation Plugins: Some plugins enhance the predictive capability of models by learning
correlation (Cirstea et al. , 2022; 2021). For example, LIFT ( Zhao & Shen , 2024) leverages locally
relationships to extract correlations. CCM (Chen et al., 2024) further performs clustering and creates
dedicated prediction heads for each cluster. However, the methods above either lack comprehensive
correlation modeling capabilities or possess substantial complexity.
3 P RELIMINARIES
Time Series Forecasting. Given a multivariate time series Xt = ( xi
t−L:t)N
i=1 ∈ RN ×L with a
look-back window L and N channels, the forecasting task aims to predict the future F steps ˆYt =
(ˆ xi
t:t+F )N
i=1 ∈ RN ×F , corresponding to the ground truth Yt = (xi
t:t+F )N
i=1.
3
Published as a conference paper at ICLR 2026
Correlation-Aware Adapter for Foundation Models. Consider a pre-trained Time Series Founda-
tion Model (TSFM), denoted by F. During the downstream ﬁne-tuning phase, the model processes
the input data Xf t
t to generate initial predictions, formulated as ˆYf t
t = F(Xf t
t ). Concurrently,
the TSFM extracts the intermediate series representation, denoted as ˜Xf t
t . Given the downstream
input Xf t
t , its corresponding ground truth Yf t
t , the initial predictions ˆYf t
t , and the latent represen-
tations ˜Xf t
t , a correlation-aware adapter is to ﬁne-tune the base model F to yield an adapted model
F ∗. Here, F ∗ represents the foundation model augmented with the proposed adapter. During the
inference phase, predictions on unseen test data are generated via ˆYtest
t = F ∗(Xtest
t ).
4 M ETHODOLOGY
Multivariate 
Series
H-PCorr Contrastive Learning
Final PredictionOriginal Prediction
Internal
Representation
Gated Add
DCorr Estimation
(a) (c)
DCorr Estimation 
(b)
Learnable 
Correlation
Rule-based 
Correlation
T-T Composition
Time-aware Polynomial
Heterogeneous Fusion
Corr Matrix
Heterogeneous Division
H-PCorr Contrastive Learning 
� t
corr
� t
pos
� t
pos � t
neg
� t
neg
� t
pos � t
neg
e
e
Foundation 
Model
CoRA Architecture
� t
corr
Negative Correlation
Channel
Positive 
Pairs 
Negative 
Pairs
Negative 
Pairs
Positive
Pairs 
Channel
Positive Correlation
1 2 3 4 5
1
2
3
4
5
1 2 3 4 5
1
2
3
4
5
43
12
5
1
5
4
3
2
� t
neg
� t
pos
� �
� �
Figure 2: The framework of CoRA. (a) CoRA begins by learning DCorr in Dynamic Correlation
Estimation module. Heterogeneous Division module projects representations into positive and neg-
ative spaces for HCorr. Then CoRA conducts H-PCorr Contrastive Learning in each space to guide
projection and capture PCorr. (b) The DCorr Estimation module estimates correlations by combin-
ing Rule-based Correlations and Learnable Correlations, which are computed by Time-aware Poly-
nomial and Time-V arying and Time-Invariant (T-T) Composition. (c) H-PCorr contrastive learn-
ing minimizes distances between strongly correlated channels and maximizes separation between
weakly correlated channels in both positive and negative spaces.
In this work, we propose a Correlation-aware Adapter ( CoRA), a lightweight plugin that allows
the TSFMs to capture various correlations during the ﬁne-tuning stage. The framework of CoRA
is visualized in Figure 2 . CoRA operates on input series, original predictions, and representations
from TSFMs to enhance the prediction accuracy. Our method consists of four processes: (i) Dy-
namic Correlation Estimation. This module utilize representations from TSFMs and input series
to learn dynamic correlations and generate correlation matrices that guide subsequent contrastive
learning. (ii) Heterogeneous Division. Some channels show dependencies on positive correlations,
whereas some others show negative correlations. To better capture HCorr, we design the this module
to process the representations from the backbone and learn representations of positive and negative
correlations separately. (iii) Heterogeneous Partial Correlation (H-PCorr) Contrastive Learn-
ing. We propose H-PCorr Contrastive Learning within each representation of HCorr to learn PCorr
by clustering only correlated channels. (iv) Heterogeneous Fusion and Prediction. Finally, we
fuse the representations after contrastive learning for positive and negative correlations in Hetero-
geneous Fusion module and generate new predictions. Then, both original and new predictions are
gated and added together.
4.1 D YNAMIC CORRELATION ESTIMATION
Channels exhibit both stable dependencies that do not change across time and ﬂuctuations that
change across time. Motivated by this, we introduce an innovative method that decomposes the
learnable part of correlation matrix M corr
t ∈ RN ×N at time t into two low-rank components:
Time-V aryingQt ∈ RN ×M and Time-Invariant V ∈ RM ×M , which can separate distinct correla-
tion components, as illustrated in Figure 3. Here, R ∈ RN ×N denotes the rule-based correlation
4
Published as a conference paper at ICLR 2026
matrix which is added to the learnable part to incorporate more prior knowledge for enhancing
correlation estimation. M is the hyperparameter for the post-decomposition rank, with M < N .
This decomposition of the learnable part offers greater parameter efﬁciency, yet remains function-
ally equivalent to conventional additive decomposition ( Cirstea et al. , 2021), as formally proven in
Theorem 1.
? (?) =  ? ???(?, ? ) =  ? 0,? × ? 0 + ? 1,? × ? 1 + . . . + ? ? ,? × ? ?
 Learnable Time-aware Polynomial 
Dynamic Correlation Estimation 
Time-Varying and Time-Invariant Composition
Time-Varying Time-Invariant All Positivate Negative
? ?
????
? ?
? ??
? ?
? ??
N
+?
M
? ? × ×?N
M N
M? ?
?
Figure 3: The details of DCorr Estimation
We estimate the two components separately
and then compose them back into the orig-
inal correlation. The Time-V arying compo-
nent represents the ﬂuctuations in correlations
across time. As time series data inherently have
trends and periodic characteristics, the correla-
tions that measure their dependencies also ex-
hibit such variations across the entire time se-
ries ( Liu et al. , 2022). Thus, we propose
Learnable Time-aware Polynomials to estimate
the changes, as polynomials can be effective in
modeling temporal patterns by sharing a com-
mon basis across different time steps. Based on
a global adaptive method, the Time-Invariant
component aims to capture the stable depen-
dencies among channels that do not change over time. Finally, we compute the correlation matrix
M corr
t by composing learnable correlations and combining with the rule-based correlation R. This
correlation matrix is then used for H-PCorr Contrastive Learning.
4.1.1 L EARNABLE TIME -AWARE POLYNOMIALS
Most existing approaches ( Shang et al. , 2024a; Cirstea et al. , 2021; Zhao et al. , 2023) struggle to
accurately express the time-varying characteristics of DCorr due to the lack of explicit modeling of
dynamic regularities.
In a stationary time series, we can use a well-behaved mathematical function to effectively approx-
imate the ﬂuctuations of the correlation. Considering that high-order polynomials provide better
non-linear capacity than ﬁrst-order ones, we use learnable polynomials to estimate Qt. The proof
of this approximation capability is detailed in Theorem 2.
We construct a K-order Time-aware Polynomials with a shared matrix basis:
Qt =
KX
i=0
Ci,tqi, (qi = q ⊙ q ⊙ · · · ⊙ q| {z }
i times
) , (1)
where Qt ∈ RN ×M denote the Time-V arying component at time step t. Ci,t ∈ RN is the i-th
coefﬁcient that varies over time, while q ∈ RN ×M is the globally learnable basis, which represents
the pattern of changes over time. We deﬁne qi as the i-times Hadamard product of the matrix q,
where the operation ⊙ is the element-wise Hadamard product.
For convenience, we deﬁne the collection of Ci,t as the matrix Ct = ( C0,t, · · · CK,t) ∈ RN ×K. It
is the dependency coefﬁcient of each channel for pattern qi and exhibits different values at different
times, determined by speciﬁc data. Therefore, we learn the mapping f between the representations
of time series ˜Xt and coefﬁcients Ct to estimate it :
Ct = f ( ˜Xt) ∈ RN ×K . (2)
Since only the polynomial coefﬁcients need to be estimated with f ,
```
