# Tackling Time-Series Forecasting Generalization via Mitigating Concept Drift — OpenReview Raw Thread

- Forum: https://openreview.net/forum?id=emkvZ7NanK
- PDF: https://openreview.net/pdf?id=emkvZ7NanK
- Section: 二、时间序列预测：分布鲁棒、多变量建模与后处理优化
- Zhihu score: 6.0
- Venue status: ICLR 2026 Poster

## Submission metadata
- Authors: Zhiyuan Zhao, Haoxin Liu, B. Aditya Prakash
- Primary area: learning on time series and dynamical systems
- Keywords: Time-Series Forecasting, Distribution Shift, Concept Drift

## Abstract
Time-series forecasting finds broad applications in real-world scenarios. Due to the dynamic nature of time series data, it is important for time-series forecasting models to handle potential distribution shifts over time. In this paper, we initially identify two types of distribution shifts in time series: concept drift and temporal shift. We acknowledge that while existing studies primarily focus on addressing temporal shift issues in time series forecasting, designing proper concept drift methods for time series forecasting has received comparatively less attention.

Motivated by the need to address potential concept drift, while conventional concept drift methods via invariant learning face certain challenges in time-series forecasting, we propose a soft attention mechanism that finds invariant patterns from both lookback and horizon time series. Additionally, we emphasize the critical importance of mitigating temporal shifts as a preliminary to addressing concept drift. In this context, we introduce ShifTS, a method-agnostic framework designed to tackle temporal shift first and then concept drift within a unified approach. Extensive experiments demonstrate the efficacy of ShifTS in consistently enhancing the forecasting accuracy of agnostic models across multiple datasets, and outperforming existing concept drift, temporal shift, and combined baselines.

## Reviews
### Reviewer_8foj
- summary: This paper addresses the problem of **distribution shifts in time-series forecasting**, focusing specifically on **concept drift**—a relatively under-explored issue compared to temporal shift. The authors propose:

1. **SAM**: A mechanism to identify invariant patterns in exogenous features across lookback and horizon windows, enabling more stable conditional distribution modeling.
2. **ShiftS**: A unified, model-agnostic framework that first mitigates temporal shift (via normalization) and then concept drift (via SAM), improving generalization across diverse forecasting models.

Extensive exp
- strengths: - **Originality**: SAM is a novel approach to handling concept drift without relying on environment labels or online retraining.
- **Quality**: The method is well-designed, with careful attention to both theoretical motivation and practical implementation.
- **Clarity**: The problem formulation and methodology are clearly explained, and the experiments are thorough and convincing.
- **Significance**: The paper fills a clear gap in the literature and provides a practical tool for improving time-s
- weaknesses: - **Theoretical Guarantees**: The method lacks theoretical analysis (e.g., error bounds or convergence guarantees), which is noted in the limitations but could strengthen the contribution.
- **Dependence on Horizon Exogenous Data**: SAM relies on $\mathbf{X}^H$ , which may not always be available or accurately predictable in practice. The paper addresses this via surrogate forecasting, but the impact of prediction error on final performance is not deeply analyzed.
- **Limited Scope**: The method is evaluated only on univariate forecasting with exogenous features. Its applicability to multivariate or purely endogenous settings remains unclear.
- questions: 1. How does SAM perform when $\mathbf{X}^H$ is not available during training or is highly noisy? Have you tested scenarios with missing or imperfect exogenous data?
2. Could SAM be adapted for online settings where concept drift occurs continuously? The paper criticizes online methods but does not explore whether SAM can be extended in that direction.
3. The mutual information analysis is insightful—have you considered using $ I(\mathbf{X}^H; \mathbf{Y}^H) $ as a criterion for applying SAM in practice?
4. The framework currently uses RevIN for temporal shift mitigation. Have you experimented with more advanced methods (e.g., SAN) in the full ShiftS pipeline, and if so, how do they compare?
- rating: 6 | confidence: 4

### Reviewer_ytQx
- summary: This paper categorizes the general concept drift in time series into types: concept drift and temporal shift (as defined more precisely in Definition 2.1 and Definition 2.2). To solve the concept drift problem, it proposes the soft attention mechanism (SAM) to find the invariant patterns in lookback and horizon windows. The core idea of this paper is illustrated well in Fig. 1. A method-agnostic framework called ShiftTS is proposed to deal with both temporal and concept drifts in a unified framework. Experiments demonstrate the good performance of the proposed method.
- strengths: 1.	The paper is well written and easy to follow. The idea proposed is simple. 
2.	The invariant patterns are learned through the surrogate feature $X_{SUR}$ and this is the core contribution of this paper. The basic idea is to concatenate the lookback and horizon windows, and model the conditional distributions for local patterns using the soft attention matrix M. 
3.	Experiments demonstrate the good performance of the proposed method.
- weaknesses: 1.	The categorization of temporal shift and concept drift is very similar to different sources of concept outlined in Section 2.1 in [R1], but in the context of time series with some differences (the temporal shift is for Y, and the concept drift is the same as Source II in [R1] ). 
2.	The method mitigating temporal shift (or the marginal distribution shift of Y) looks quite standard in the literature. 
3.	The proposal of mitigating concept drift may be incremental for some datasets and base algorithms.
- questions: 1.	The analysis in Section 4.2 looks reasonable to me. The improvement of the proposed method depends on the data and the base algorithm simultaneously. Fig.3(a) plots the performance gain vs. the mutual information between X and Y. In fact, this plot studies the effectiveness of ShiftTS w.r.t. the so-called concept drift defined in Def 2.2 in this paper. A good example is the Exchange dataset, which shows low mutual information but high performance improvement. Thus, it suggests that the performance is mainly due to the mitigation of the so-called temporal concept drift. This is also consistent of Fig. 3(b), which shows that the most significant performance improvement is between ShiftTS\TS and Base. Therefore, at least on the Exchange dataset, the proposal of learning form surrogate feat
- rating: 6 | confidence: 3

### Reviewer_YbKf
- summary: This paper identifies two types of distribution shifts in time series forecasting: temporal shift (marginal distribution) and concept drift (conditional distribution). The authors propose a new method, SAM (soft attention masking), to mitigate concept drift by learning invariant patterns from both lookback and *horizon* exogenous features ($X^L$ and $X^H$). This mechanism learns a surrogate feature, $X^{SUR}$, which is predicted as an auxiliary task. The paper also presents ShifTS, a model agnostic framework that first uses normalization (like RevIN) to handle temporal shift, and then uses a b
- strengths: - The paper clearly distinguishes between temporal shift and concept drift, tackling a significant and practical problem in time series forecasting.
- The core idea of using *horizon* exogenous features ($X^H$) to define a stable surrogate target ($X^{SUR}$) is novel. This surrogate acts as an effective regularization target during training, forcing the model to learn future relevant patterns.
- The ShifTS framework is practical and model agnostic. It cleanly integrates a known temporal shift so
- weaknesses: - The claim that SAM finds "invariant patterns" is not well supported by the mechanism. The method (Equation 1) is a learnable attention mask, not an explicit invariance optimization like in IRM. It seems to learn a *useful compression* of future features, but calling it "invariant" is a strong claim that needs better justification.
- The paper introduces significant complexity with the SAM module and the aggregation MLP. However, the performance gains on SOTA models like iTransformer are sometimes small (e.g., <5% MAE gain on ETTh2/ETTm2). The marginal benefit versus the added complexity is questionable in these cases.
- A critical and much simpler baseline is missing. The paper argues predicting raw $X^H$ is too hard, but $X^{SUR}$ is easier. This assertion must be tested by comparing ShifTS to a simpler multi task model that just predicts the raw $X^H$ as the auxiliary task.
- questions: 1.  Can you please clarify how the SAM mechanism (Equation 1) specifically enforces invariance? The high weight patterns are defined as invariant, but it is unclear how the optimization process encourages this property over just learning a stable predictive signal.
2.  To justify the complexity of SAM, could you add a baseline that replaces the $X^{SUR}$ target with the raw $X^H$? This would involve a multi task loss $\mathcal{L} = \mathcal{L}_{TS} + \lambda \cdot MSE(X^H, \hat{X}^H)$. This comparison is essential to prove that the SAM slicing and attention is superior to just predicting the raw future features.
3.  What is the impact of applying ShifTS to "near-stationary" datasets like Traffic or Weather, which were excluded? Does the method degrade performance in the absence of signific
- rating: 6 | confidence: 4

## Author comments / rebuttal
### Rebuttal to Reviewer YbKf
We appreciate the valuable comments from the reviewer, and we are willing to address the concerns.

**Response to W1 & Q1: Invariant**

Thank you for the comment. We agree that “invariant patterns” is a term often associated with domain adaptation settings, where explicit domain labels exist and methods such as IRM perform optimization to enforce domain-level invariance. In contrast, time-series forecasting rarely provides domain annotations, making explicit invariance optimization infeasible in our setting.

Our intention is therefore different: SAM does not enforce invariance in the IRM sense, but instead aims to identify stable conditional relationships that persist across different temporal slices (lines 195–214). First, we construct sliding windows over both the look-back and horizon intervals, and compute the conditional distributions associated with each temporal slice. Then, at each time step, SAM produces a learnable weighting over these conditional distributions. By averaging these weights over time, we obtain a measure of how consistently each conditional distribution contributes to prediction across the entire time series. Conditional distributions that receive consistently high weights are those that remain useful across many time steps, reflecting temporal stability rather than domain-level invariance. Our use of the term “invariant” refers to this stability across temporal contexts, not IRM-style enforced invariance.

**Response to W2: Performance Gain and Cost**

As discussed in lines 408–416, we acknowledge that when ShifTS is applied to more advanced models such as iTransformer, the average improvement may appear smaller. However, we emphasize that the gains are still substantial on several datasets. For example, on ILI and Exchange, ShifTS delivers over 10% improvement, which is highly significant even for strong baselines. More importantly, the bottom line is that ShifTS does not degrade model performance, while still offering measurable improvements even on the advanced baselines.

Regarding computational overhead, ShifTS adds only a small number of parameters. The training cost increase is reasonable; for example, on ETTh1 with iTransformer, the per-epoch time changes only from 3.6s to 6.3s with iTransformer on ETTh1-96-96 (15.1s to 18.5s with Crossformer). This indicates that the method delivers performance gains at very low additional complexity, making it practical even when the improvements are modest.

**Response to W3 & Q2: Multi-task Baseline**

Thank you for the suggestion. We conducted an additional experiment that incorporates the proposed multi-task baseline. We report the results at https://anonymous.4open.science/r/shifts_iclr-ED40/multi.pdf. The findings show that ShifTS consistently outperforms the multi-task baseline, particularly with longer horizons. This supports our intuition that predicting the entire future exogenous sequence is almost as difficult as forecasting the target itself. In contrast, SAM sele

### Rebuttal to Reviewer ytQx
We appreciate the valuable comments from the reviewer, and we are willing to address the concerns.

**Response to W1: Categorization**

We agree that distribution shift has been extensively studied for decades, and therefore our definitions naturally align with prior formulations in general machine learning. From this perspective, the terminology itself is not intended as a novel theoretical contribution. However, we emphasize that very few time-series forecasting studies explicitly differentiate these two forms of shift. In our work, we not only make this distinction explicit in the time-series context but also provide real-world examples illustrating how temporal shift and concept drift are different in practice through visualization (e.g., Figures 4 & 5 on page 14). This conceptual understanding is important to appear in the problem definition section because it directly motivates the design of ShifTS and helps practitioners understand when and why the method is beneficial.

**Response to W2: Standard Temporal Shift Method**

We acknowledge that the temporal-shift mitigation techniques used in ShifTS are standard in the literature. However, we would like to emphasize that proposing a new method for mitigating temporal shift is not the main contribution of our work. Our primary focus is on addressing concept drift, and Section 3.2 is intended to clarify why mitigating temporal shift is a necessary prerequisite before one can effectively mitigate concept drift. This motivation is essential for understanding the design of the ShifTS framework. Thus, while the temporal-shift component itself is not novel, the insight into its necessity and its role within a broader concept-drift mitigation framework is both valuable and, we believe, novel.

**Response to W3 & Q1: Incremental Gains**

Thank you for the insightful comment. We agree that, in some cases, the performance improvements of ShifTS appear incremental. However, we believe this is common and understandable that a rare single forecasting method can consistently outperform all baselines across all datasets and model architectures by far, and moreover, we are aiming to mitigate concept drift issues via ShifTS for agnostic models, rather than beating the SOTA.

Nevertheless, our results show that the bottom line of ShifTS does not degrade performance even in scenarios where the gain is modest. And more importantly, we explain and identify when ShifTS is expected to be effective by linking its performance to a measurable data property. This provides practitioners with a practical guideline to assess the potential benefits of ShifTS on their own datasets, rather than relying on universal dominance.

### Rebuttal to Reviewer 8foj
We appreciate the valuable comments from the reviewer, and we are willing to address the concerns.

**Response to W1: Theoretical Gaurantee**

We appreciate the reviewer for raising this point. We acknowledge that our work does not include a comprehensive theoretical analysis (e.g., error bounds or convergence guarantees). However, we do offer conceptual guidance, for example, illustrating the necessity of handling temporal shift before concept drift, or the trade-off between the difficulty of predicting farther-ahead exogenous features and the benefit they bring to forecasting the target series, and we empirically demonstrate that the benefits outweigh the drawbacks in practice.

More importantly, we identify when ShifTS is likely to be beneficial through a simple mutual-information-based measurement. While this does not give a formal theoretical guarantee, it provides a practical and interpretable criterion for real-world usage, which we believe is valuable for practitioners. We believe theoretical analysis on ShifTS is a promising future research study, but currently out of our scope.

**Response to W2 & Q1: Availability and Quality of Exogenous Data**

Thank you for raising this important point. We clarify that the unobserved target-aligned exogenous features $X^H$ are not missing during training in typical forecasting pipelines. For example, in exchange rate prediction, all historical exogenous features at all historical time steps are fully observed. By definition, $X^H$ corresponds to the exogenous inputs at the same time steps as the training labels $Y^H$. Since both belong to the historical portion of the time series, they are naturally available and do not require forecasting during training.

For data quality, we evaluate ShifTS on datasets such as ETT, which are well known for their irregular and noisy time-series patterns. The empirical results show that ShifTS consistently improves forecasting accuracy even under such imperfect conditions, suggesting robustness to realistic levels of noise.

**Response to W3: Limited Scope**

Thank you for raising this point. However, we respectfully disagree with the characterization that our scope is limited. First, univariate forecasting with exogenous features (often referred to as multi-single forecasting) is itself a widely used and practically important setting. Many real-world applications, such as epidemic forecasting or industrial demand forecasting, rely on predicting a single target series supported by multiple external signals, which aligns directly with our setup. Second, ShifTS can be potentially extended to multivariate forecasting. One can view each output dimension as a target series and treat the remaining dimensions as exogenous inputs, applying ShifTS separately to each dimension. This provides a straightforward path toward a multivariate variant of our framework. While such an extension is promising, it is currently beyond our primary scope and thus remains for future work.

**

### Tackling Time-Series Forecasting Generalization via Mitigating Concept Drift


## Meta review / decision
### Paper Decision
Accept (Poster)

## PDF extracted text (first pages)
```text
Published as a conference paper at ICLR 2026
TACKLINGTIME-SERIESFORECASTINGGENERALIZA-
TION VIAMITIGATINGCONCEPTDRIFT
Zhiyuan Zhao
Georgia Institute of Technology
leozhao1997@gatech.edu
Haoxin Liu
Georgia Institute of Technology
hliu763@gatech.edu
B. Aditya Prakash
Georgia Institute of Technology
badityap@cc.gatech.edu
ABSTRACT
Time-series forecasting finds broad applications in real-world scenarios. Due to
the dynamic nature of time series data, it is important for time-series forecasting
models to handle potential distribution shifts over time. In this paper, we initially
identify two types of distribution shifts in time series: concept drift and temporal
shift. We acknowledge that while existing studies primarily focus on addressing
temporal shift issues in time series forecasting, designing proper concept drift
methods for time series forecasting has received comparatively less attention.
Motivated by the need to address potential concept drift, while conventional con-
cept drift methods via invariant learning face certain challenges in time-series
forecasting, we propose a soft attention mechanism that finds invariant patterns
from both lookback and horizon time series. Additionally, we emphasize the
critical importance of mitigating temporal shifts as a preliminary to addressing
concept drift. In this context, we introduce ShifTS, a method-agnostic framework
designed to tackle temporal shift first and then concept drift within a unified ap-
proach. Extensive experiments demonstrate the efficacy ofShifTS in consistently
enhancing the forecasting accuracy of agnostic models across multiple datasets,
and outperforming existing concept drift, temporal shift, and combined baselines.
1 INTRODUCTION
Time-series forecasting finds applications in various real-world scenarios such as economics, urban
computing, and epidemiology (Zhu & Shasha, 2002; Zheng et al., 2014; Deb et al., 2017; Mathis et al.,
2024). These applications involve predicting future trends or events based on historical time-series
data. For example, economists use forecasts to make financial and marketing plans, while sociologists
use them to allocate resources and formulate policies for traffic or disease control.
The recent advent of deep learning has revolutionized time-series forecasting, resulting in a series of
advanced forecasting models (Lai et al., 2018; Torres et al., 2021; Salinas et al., 2020; Nie et al., 2023;
Zhou et al., 2021). However, despite these successes, time-series forecasting faces certain challenges
from distribution shifts due to the dynamic and complex nature of time series data. The distribution
shifts in time series can be categorized into two types (Granger, 2003). First, the data distributions
of the time series data themselves can change over time, including shifts in mean, variance, and
autocorrelation structure, which is referred to as non-stationarity or temporal drift issues in time-series
forecasting (Shimodaira, 2000; Du et al., 2021). Second, time-series forecasting is compounded
by unforeseen exogenous factors, which shifts the distribution of target time series. These types of
phenomena, categorized as concept drift problems in time-series forecasting (Gama et al., 2014; Lu
et al., 2018), make it even more challenging.
While prior research has investigated strategies to mitigate temporal shifts (Liu et al., 2022; Kim et al.,
2021; Fan et al., 2023), addressing concept drift issues in time-series forecasting has been largely
overlooked. Although concept drift is a well-studied problem in general machine learning (Sagawa
1
Published as a conference paper at ICLR 2026
et al., 2019; Arjovsky et al., 2019; Ahuja et al., 2021), adapting these solutions to time-series
forecasting is challenging. Many of these methods require environment labels, which are typically
unavailable in time-series datasets (Liu et al., 2024a). Indeed, the few concept drift approaches
developed for time-series data are designed exclusively for online settings (Guo et al., 2021), which
requires iterative retraining over time steps and is infeasible when applied to standard time-series
forecasting tasks.
Therefore, we aim to close this gap in the literature in this paper, that is, to mitigate concept drift in
time-series forecasting for standard time-series forecasting tasks. The contributions of this paper are:
1. Concept Drift Method:We introduce soft attention masking ( SAM) designed to mitigate
concept drift by using the invariant patterns in exogenous features. The soft attention allows
the time-series forecasting models to weigh and ensemble of invariant patterns at multiple
horizon time steps to enhance the generalization ability.
2. Distribution Shift Generalized Framework:We show the necessity of addressing temporal
shift as a preliminary when addressing concept drift. We therefore propose ShifTS, a
practical, distribution shift generalized, model-agnostic framework that tackles temporal
shift and concept drift within a unified approach.
3. Comprehensive Evaluations:We conduct extensive experiments on various time series
datasets with multiple advanced time-series forecasting models. The proposed ShifTS
demonstrates effectiveness by consistent performance improvements to agnostic forecasting
models, as well as outperforming distribution shift baselines in better forecasting accuracy.
We provide related works on time-series analysis and distribution shift generalization in Appendix A.
2 PROBLEMFORMULATION
2.1 TIME-SERIESFORECASTING
Time-series forecasting involves predicting future values of one or more dependent time series based
on historical data, augmented with exogenous covariate features. Let denote the target time series as
Y and its associated exogenous covariate features as X. At any time step t, time-series forecasting
aims to predict YH
t = [yt+ 1, y t+2, . . . , yt+H ]∈Y using historical data (XL
t ,Y L
t ), where L
represents the length of the historical data window, known as thelookback window, andH denotes the
forecasting time steps, known as thehorizon window. Here, XL
t = [x t−L+1, xt−L+2, . . . , xt]∈X
and YL
t = [y t−L+1, yt−L+2, . . . , yt]∈Y . For simplicity, we denote YH ={Y H
t } for ∀t as the
collection of horizon time-series of all time steps, and similar for YL and XL. Conventional time-
series forecasting involves learning a model parameterized by θ through empirical risk minimization
(ERM) to obtain fθ : (X L,Y L)→Y H for all time steps t. In this study, we focus on univariate
time-series forecasting with exogenous features, whered Y = 1andd X ≥1.
2.2 DISTRIBUTIONSHIFT INTIMESERIES
Given the time-series forecasting setups, a time-series forecasting model aims to predict the target
distribution P(YH ) = P(Y H |YL)P(YL) + P(Y H |XL)P(XL), which should be generalizable
for both training and testing time steps. However, due to the dynamic nature of time-series data,
forecasting faces challenges from distribution shifts, categorized into two types: temporal shift and
concept drift. These two types of distribution shifts are defined as follows:
Definition 2.1 (Temporal Shift (Shimodaira, 2000; Du et al., 2021)) Temporal shift (also known
as virtual shift (Tsymbal, 2004)) refers to phenomenon that the marginal probability distributions
change over time, while the conditional distributions are the same.
Definition 2.2 (Concept Drift (Lu et al., 2018)) Concept drift (also known as real concept
drift (Gama et al., 2014) 1) is the phenomenon where the conditional distributions change over
time, while the marginal probability distributions are the same.
1(Gama et al., 2014) defines concept drift as both virtual shift and real concept drift. Our concept drift
definition is consistent with the definition of real concept drift in (Gama et al., 2014).
2
Published as a conference paper at ICLR 2026
Intuitively, a temporal shift indicates unstable marginal distributions (e.g. P(YH )̸= P(Y L)),
while a concept drift indicates unstable conditional distributions ( P(YH
i |XL
i )̸= P(Y H
j |XL
j ) for
some i, j∈t ). Existing methods for distribution shifts in time-series forecasting typically focus on
mitigating temporal shifts through normalization, ensuring P(YH ) = P(Y L) by both normalizing
to standard 0-1 distributions (Kim et al., 2021; Liu et al., 2022; Fan et al., 2023). In contrast, concept
drift remains relatively underexplored in time-series forecasting.
Nevertheless, time-series forecasting does face challenges from concept drift: The correlations
between X and Y can change over time, making the conditional distributions P(YH |XL) unstable
and less predictable. A demonstration visualizing the differences and relationships between temporal
shift and concept drift is provided in Appendix B.
While the concept drift issue has received considerable attention in existing studies on general
machine learning, applying them, mostly invariant learning approaches, to time-series forecasting
tasks presents certain challenges. Firstly, conventional approaches to mitigate concept drift are
through invariant learning. However, these invariant learning methods typically rely on explicit
environment labels as input (e.g., labeled rotation or noisy images in image classification), which are
not readily available in time series datasets. Second, these invariant learning methods assume that
all correlated exogenous features necessary to fully determine the target variable are accessible (Liu
et al., 2024a), which are often not applied to time series datasets (e.g., lookback window information
is not sufficiently determining the horizon target). Indeed, a few concept drift methods not based on
invariant learning have been proposed for time-series forecasting (Guo et al., 2021). However, these
methods are designed for the online setting which does not fit standard time-series forecasting, and
are only validated on limited synthetic datasets rather than complicated real-world ones.
3 METHODOLOGY
The main idea of our methodology is to address concept drift through SAM by modeling stable
conditional distributions on surrogate exogenous features with invariant patterns, rather than the
sole lookback window. Furthermore, we recognize that effectively mitigating temporal shifts is
preliminary for addressing concept drift. To this end, we propose ShifTS that effectively handles
concept drift by first resolving temporal shifts as a preliminary step within a unified framework.
3.1 MITIGATINGCONCEPTDRIFT
Methodology Intuition.As defined in Definition 2.2, concept drift in time-series refers
to the changing correlations between X and Y over time ( P(Y H
i |XL
i )̸=P(Y H
j |XL
j ) for
i, j∈t ), which introduces instability when modeling conditional distribution P(Y H |XL).
Figure 1: Comparison between conventional
time-series forecasting and our approach. Our
approach identifies invariant patterns in lookback
and horizon window as XSU R and then models
a stable conditional distribution accordingly to
mitigate concept drift.
This instability arises because, for a given exoge-
nous feature X, its lookback window XL alone
may lack sufficient information to predict YH,
while learning a stable conditional distribution
requires that the inputs provide sufficient informa-
tion to predict the output (Sagawa et al., 2019; Ar-
jovsky et al., 2019). There are possible patterns in
the horizon window XH, joint with XL, that influ-
ence the target. Thus, modeling P(Y H |XL,X H )
leads to a more stable conditional distribution com-
pared to P(Y H |XL), as [XL,X H ] captures addi-
tional causal relationships across future time steps.
We assume that incorporating causal relationships
from the horizon window enables more complete
causality modeling between that exogenous fea-
ture and target, given that the future cannot influ-
ence the past (e.g., XH
t+1 ↛Y H
t ). However, these
causal effects from the horizon window, while im-
portant for learning stable conditional distributions, are often overlooked by conventional time-series
forecasting methods, as illustrated in Figure 1(a).
3
Published as a conference paper at ICLR 2026
Therefore, we propose leveraging both lookback and horizon information from exogenous features
(i.e., [XL,X H ]) to predict the target, enabling a more stable conditional distribution. However, di-
rectly modeling P(Y H |XL,X H ) in practice presents two challenges. First, XH typically represents
unknown future values during testing. To model P(Y H |XL,X H ), it may require to first predict XH
by modeling P(X H |XL), which can be as challenging as predicting YH directly. Second, not every
pattern in XH at every time step holds a causal relationship with the target. Modeling all patterns
from XL and XH may introduce noisy causal relationships (as invariant learning methods aim to
mitigate) and reduce the stability of conditional distributions.
To address the above challenges, instead of directly modeling P(Y H |XL,X H ), we propose a two-
step approach: first, identifying patterns in [XL,X H ] that lead to stable conditional distributions
(namely invariant patterns), and then modeling these conditional distributions accordingly. To
determine stability, a natural intuition is to assess whether a pattern’s correlation with the target
remains consistent across all time steps. For instance, if a subsequence of [XL,X H ] consistently
exhibits stable correlations with the target over all or most time steps (e.g., an increase of the
subsequence always results in an increase of the target), then its conditional distribution should be
explicitly modeled due to the stability. Conversely, if a subsequence demonstrates correlations with
the target only sporadically or locally, these correlations are likely spurious, which are unstable
conditional distributions to other time steps. We leverage this intuition to identify all invariant patterns
and aggregate them into a surrogate feature XSUR, accounting for the fact that the target can be
determined by multiple patterns. For instance, an influenza-like illness (ILI) outbreak in winter can
be triggered by either extreme cold weather in winter or extreme heat waves in summer (Nielsen
et al., 2011; Jaakkola et al., 2014). By incorporating this information, we model the corresponding
conditional distributionP(Y H |XSUR), as illustrated in Figure 1(b).
The effectiveness of XSUR in predicting YH stems from two key insights. First, P(Y H |XSUR) is a
stable conditional distribution to model, as it captures invariant patterns across both the lookback
and horizon windows. Second, while there is a trade-off— P(Y H |XSUR) provides stability, but
estimating XSUR may introduce additional errors—practical evaluations demonstrate that the benefits
of constructing stable conditional distributions outweigh the potential estimation errors of XSUR.
This is because XSUR contains only partial information, which is easier to predict than the entire XH.
Methodology Implementation.Recognizing that P(Y H |XSU R) is the desirable conditional distri-
bution to learn, the remaining challenge is to identify XSU R in practice. To achieve this, we propose
a soft attention masking mechanism (SAM), that operates as follows: First, we concatenate [XL,X H ]
to form an entire time series of length L+H . The entire series is then sliced using a sliding window
of size H, resulting in L+ 1 slices. This process extracts local patterns ( [XH
t−L, . . . ,XH
t ] at each
time stept), which are subsequently used to identify invariant patterns.
Second, we model the conditional distributions for all local patterns
[P(Y H
t |XH
t−L), . . . , P(YH
t |XH
t )] at each time step t, with applying a learnable soft atten-
tion matrix M to weigh each local pattern. This matrix incorporates softmax, sparsity, and
normalization operations, which can be mathematically described as:
Softmax :M j = Softmax(M j)
Sparsity :M ij =M ij ·1 (Mij −µ(Mj ))≥0
Normalize :M j = Mj
|Mj|
(1)
where i, j are the first and second dimensions of M. These operations are essential for SAM
identifying invariant patterns. The intuition is that we consider sliced windows from the lookback
and horizon over time steps as candidates of invariant patterns. We use the softmax operation to
compute and update the weights of each pattern contributing to the target YH. We then apply a
sparsity operation to filter out patterns with low weights, leaving only the patterns with high weights.
These high-weight patterns, which consistently contribute to the target across all instances at all time
steps, are regarded as invariant patterns over time. These patterns intuitively are invariant patterns as
P(Y H
i |XH
i−k)≈P(Y H
j |XH
j−k ) for some k∈[0, L] and i, j∈t . While multiple invariant patterns
may be identified, we compute a weighted sum of these patterns, proportional to their contributions
4
Published as a conference paper at ICLR 2026
Figure 2: Diagram of ShifTS, consisting of three components: (a) normalization at the start (c)
denormalization at the end to address temporal shifts, and (b) a two-stage forecasting process-The first
stage predicts surrogate exogenous features, ˆXSUR, identified by the SAM, which capture invariant
patterns essential for forecasting the target; The second stage uses both the predicted surrogate
exogenous features and the originalY L to predictY H.
in predicting the target. The weighted-sum patterns formulate the surrogate feature XSU R. For
simplicity, we denote this process as:
XSUR =SAM([X L,X H ]) =
X
L+1
M(Slice([XL,X H ]))(2)
where Slice(·) represents slicing the time series [L+H, d X]→[H, L+ 1, d X], and M ∈R L+1×dX
is the learnable soft attention as in Equation 1.
In practice, XSUR may include horizon information unavailable during testing. To address this, SAM
estimates the surrogate features ˆXSUR using agnostic forecasting models. The surrogate loss that
aims to estimate ˆXSUR is defined as:
LSUR = MSE(X SUR, ˆXSUR)(3)
3.2 MITIGATINGTEMPORALSHIFT
While the primary contribution of this work is to mitigate concept drift in time-series forecasting,
addressing temporal shifts is equally critical and serves as a prerequisite for effectively managing
concept drift. The key intuition is that SAM seeks to learn invariant patterns that result in a stable
conditional distribution, P(Y H |XSUR). However, achieving this stability becomes challenging if the
marginal distributions (e.g., P(Y H ) or P(X SUR)) are not fixed, as these distributions may change
over time because of the temporal shift issues.
To address this issue, a natural solution is to learn the conditional distribution under standardized
marginal distributions. This can be achieved using temporal shift methods, which employ instance
normalization techniques to stabilize the marginals. The core intuition behind popular temporal shift
methods is to normalize data distributions before the model processes them and to denormalize the
outputs afterward. This approach ensures that the normalized sequences maintain consistent mean
and variance between the inputs and outputs of the forecasting model. Specifically, P(X L
Norm)≈
P(X H
Norm)∼Dist(0,1) and P(Y L
Norm)≈P(Y H
Norm)∼Dist(0,1) , thereby mitigating temporal
shifts (i.e., shifts in marginal distributions over time).
Among the existing methods, Reversible Instance Normalization (RevIN) (Kim et al., 2021) stands out
for its simplicity and effectiveness, making it the method of choice in this work. Advanced techniques,
such as SAN (Liu et al., 2023) and N-S Transformer (Liu et al., 2022), have also demonstrated
promise in addressing temporal shifts. However, these methods often require modifications to
forecasting models or additional pre-training strategies. While exploring these advanced temporal
shift approaches remains a promising avenue for further performance improvements, it is beyond the
scope of this study and not the primary focus of this work.
5
Published as a conference paper at ICLR 2026
3.3SH I FTS: THEINTEGRATEDFRAMEWORK
To address concept drift 
```
