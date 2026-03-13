# CTBench: Cryptocurrency Time Series Generation Benchmark — OpenReview Raw Thread

- Forum: https://openreview.net/forum?id=RzT2sombPD
- PDF: https://openreview.net/pdf?id=RzT2sombPD
- Section: 一、时间序列生成：因果性、多样性与领域适配
- Zhihu score: 6.0
- Venue status: ICLR 2026 Poster

## Submission metadata
- Authors: Yihao Ang, Qiang Wang, Qiang Huang, Yifan Bao, Xinyu Xi, Anthony Kum Hoe Tung, Chen Jin, Zhiyong Huang
- Primary area: datasets and benchmarks
- Keywords: Time Series Generation, Crypto-centric Benchmark, Cryptocurrency Markets, Financial Evaluation Measure Suite

## Abstract
Synthetic time series are vital for data augmentation, stress testing, and prototyping in quantitative finance. Yet in cryptocurrency markets, characterized by 24/7 trading, extreme volatility, and rapid regime shifts, existing Time Series Generation (TSG) methods and benchmarks often fall short, jeopardizing practical utility. Most prior work targets non-financial or traditional financial domains, focuses narrowly on classification and forecasting while neglecting crypto-specific complexities, and lacks critical financial evaluations, particularly for trading applications. To bridge these gaps, we introduce \textbf{CTBench}, the first \textbf{C}ryptocurrency \textbf{T}ime series generation \textbf{Bench}mark. It curates an open-source dataset of 452 tokens and evaluates models across 13 metrics spanning forecasting accuracy, rank fidelity, trading performance, risk assessment, and computational efficiency. A key innovation is a dual-task evaluation framework: the Predictive Utility measures how well synthetic data preserves temporal and cross-sectional patterns for forecasting, while the Statistical Arbitrage assesses whether reconstructed series support mean-reverting signals for trading. We systematically benchmark eight state-of-the-art models from five TSG families across four market regimes, revealing trade-offs between statistical quality and real-world profitability. Notably, CTBench provides ranking analysis and practical guidance for deploying TSG models in crypto analytics and trading applications. The source code is available at \url{https://github.com/MilleXi/CTBench/}.

## Reviews
### Reviewer_hL6x
- summary: The paper introduces CTBench, an open-source benchmark for crypto time‑series generation. It provides a curated, hourly panel of 452 USDT pairs on Binance (2020–2024) and a two-track evaluation for crypto time-series generation. Representative generators are tested across four market regimes using a finance-first metric stack that spans several aspects. The results document model utility in different regimes.
- strengths: - Empirically, the authors observe the regime-dependent trade-offs between fidelity and tractability, i.e., high fidelity does not directly imply tradability. This is an important insight for generating synthetic financial data.

- Emphasizing rank-based metrics and arbitrage capacity over purely generative scores moves the discussion toward decision-useful validation.

- The authors offer useful guidance on model selection for practical uses.
- weaknesses: - Results are tied to a single forecasting model. Without testing a variety of forecasters, it’s unclear whether conclusions generalize.

- Insufficient diagnostic analysis of model performance differentials. The paper does not investigate why the TSG models diverge in outcomes, leaving the observations unexplained.
- questions: - Do you evaluate the covariance and eigenspectrum alignment between synthetic and real returns? This might explain why Fourier-Flow yields stable rank metrics but limited arbitrage.

- Compared with those used in finance economics, such as ARMA-GARCH and the bootstrap, do the learning-based TSG models provide better synthetic data?

- Have you tested alternative forecasters (e.g., linear model, random forest, and MLP)? Do the relative model performance and rankings persist?
- rating: 6 | confidence: 4

### Reviewer_8b4R
- summary: This paper provides an open-source cryptocurrency dataset and the first benchmark for time series generation in cryptocurrency, named CTBench. Moreover, it introduces a novel dual-task evaluation framework to assess how well the temporal dynamics captured by synthetic data can be used for downstream forecasting and whether they can reconstruct market structure and isolate tradable signals. CTBench specifically evaluates the capability of eight state-of-the-art generative models for time series, using abundant metrics in different financial applications. Experimental results benchmark the perfo
- strengths: - This paper offers a valuable open-source cryptocurrency dataset, which bridges the gap between research on time series generation and cryptocurrency.
    
- The benchmark discussed in this paper is comprehensive, involving most of recent deep generative models and evaluation metrics widely used in finance.
    
- This paper provides some intriguing practical findings that are critical for future research and applications: (i) current generative models achieve diverse performance across tasks, 
- weaknesses: - The predictive utility task fixes the forecasting model to XGBoost for its robustness and interpretability. However, some conclusions may change with alternative predictors, given that different setups have large impacts on the model performance.
    
- [Minor] Dual-task evaluation module in Figure 2 is visually unclear. Perhaps its readability can be improved by simplifying the contents like the other modules, since Figure 3 already shows the details.
- questions: - Is it possible that generative models may have different performance using forecasting models other than XGBoost?
    
- Are all feature windows strictly backward-looking and computed within the split? Are any scalers fit only on training data? Do all the results hold using different splits?

- A small typo: Citation formatting at line 041 is incorrect.
- rating: 8 | confidence: 4

### Reviewer_WGHC
- summary: CTBench is the benchmark tailored for Time Series Generation  in cryptocurrency markets, addressing limitations of existing benchmarks in domain generality, task scope, and crypto-specific evaluation. It features a curated dataset of OHLC data, dual-task evaluation, 13 financial metrics across 5 dimensions, and 8 TSG models from 5 families. Experiments across bull, volatile, consolidation, and mean-reverting regimes reveal trade-offs between statistical fidelity and trading profitability. CTBench enables rigorous TSG evaluation for crypto trading, bridging synthetic data generation with practi
- strengths: 1. Captures unique traits of crypto markets including 24/7 volatility, absence of intrinsic valuation and irregular liquidity that are not addressed in traditional benchmarks.
2. Links TSG to real-world use cases through two complementary tasks focusing on forecasting capabilities and tradable signal extraction rather than just statistical similarity.
3. Integrates 13 diverse metrics covering error measurement, rank correlation, trading performance, risk assessment and computational efficiency f
- weaknesses: 1. Relies solely on Binance’s spot hourly data, lacking the diversity of cross-exchange data, alternative crypto asset types such as futures contracts, and different sampling frequencies. Besides, it remains unknown whether this generation method can be effectively extended to a broader range of asset classes, which limits the method’s scalability.
2. All TSG models' generated data are used with the same XGBoost model for downstream prediction. Different TSG models may be better suited for different types of predictors as some models like Transformer are more sensitive to long-term dependencies, so using a fixed predictor may introduce evaluation bias and fail to fully reflect the generality of the generated data.
3. Diffusion-based models included in the benchmark may exhibit long training and inference times, providing comparisons of generation efficiency across different models would help alleviate concerns in this regard.
- questions: See Weakness.
- rating: 4 | confidence: 3

## Author comments / rebuttal
### Revision Summary for AC
Dear AC,

Thank you for coordinating the review process and for the constructive feedback from Reviewers **hL6x**, **8b4R**, and **WGHC**. 
We are encouraged that all three reviewers highlighted CTBench's strengths: its crypto-centric dataset, dual-task evaluation (predictive utility + statistical arbitrage), and comprehensive financial metric suite, and regarded the benchmark as timely and valuable for the TSG community.

Below, we summarize the key concerns raised and the corresponding revisions, additions, and clarifications made in the updated manuscript.

>**1. Dependence on a Single Forecaster (hL6x Q3; 8b4R W1/Q1; WGHC W2)**

All reviewers asked whether the findings depend on using **XGBoost** in the Predictive Utility task.

To address this, we added a **new ablation study (Section 4.4, Figure 10)** comparing five forecasting architectures: Linear Regression, Random Forest (RF), MLP, Transformer, and XGBoost. 

Across all TSG models and time periods, **XGBoost consistently provides the strongest combination of low error and high IC/IR**, while other forecasters either underfit (Linear/MLP) or capture short-term noise rather than tradable structure (RF/Transformer).
This confirms that **CTBench's conclusions are robust** and that XGBoost is an appropriate default evaluator of tradable structure.

>**2. Comparison with Classical Finance Baselines (hL6x Q2)**

Reviewer hL6x asked how learning-based TSG compare with traditional econometric approaches.
We added two widely used baselines:
- **ARMA-GARCH** (VAR-DCC-GARCH): Evaluated on both Predictive Utility and Statistical Arbitrage.
- **Bootstrap**: Evaluated on Predictive Utility (non-predictive by construction).

**Findings:**
- Classical models can be competitive on error metrics but struggle on **rank-based and trading metrics**, especially when cross-sectional dispersion or regime shifts matter.
- Learning-based TSG models, particularly **TimeVAE, COSCI-GAN, and KoVAE**, better preserve alpha structure and deliver **higher Sharpe/CAGR with comparable or lower tail risk**.

These results help position CTBench as a bridge between traditional financial modeling and modern TSG methods.

>**3. Benchmark Scope and Extensibility (WGHC W1)**

We clarified that CTBench is a **model-agnostic, dataset-agnostic benchmark**, not a generation method.
The data loader, feature extraction, and evaluation pipeline are **fully modular** and can incorporate:
- multi-exchange spot data,
- futures or derivatives data (with funding-rate extensions),
- alternative sampling frequencies.

Binance hourly USDT pairs were selected for **liquidity, data quality, and public reproducibility**, not as a limitation. We expanded Appendix B to explicitly explain this design choice and the benchmark's extensibility.

> **4. Clarification and Presentation Improvements (8b4R W2/Q2/Q3)**

Reviewer 8b4R requested clarifications on feature engineering, scaling, and figure readability.

In the revision:
- All features are confirm

### Official Comment by Authors (2/2)
> W2. All TSG models' generated data are used with the same XGBoost model for downstream prediction. Different TSG models may be better suited for different types of predictors as some models like Transformer are more sensitive to long-term dependencies, so using a fixed predictor may introduce evaluation bias and fail to fully reflect the generality of the generated data.

Thank you for raising this concern.
To directly test the sensitivity of CTBench's conclusions to the choice of predictor, we conducted a **comprehensive ablation over five forecasting architectures: Linear Regression, Random Forest, MLP, Transformer, and XGBoost**, all trained on synthetic data from every TSG model and evaluated on real returns using the same walk-forward protocol. Full results are now reported in **Section 4.4 (Ablation Study)**.

Across all experiments, three robust patterns emerge:
- **Linear Regression and MLP** produce large MSE/MAE and near-zero IC/IR, showing weak predictive and cross-sectional ability.
- **Random Forest and Transformer** reduce prediction errors but retain near-zero IC/IR, capturing short-term noise rather than tradable structure.
- **XGBoost** consistently provides the strongest combination of low error and high rank correlation, making it the *most discriminative* and *trading-relevant* forecaster.

These findings demonstrate that **XGBoost is the most reliable evaluator of tradable structure**, justifying its use as the default forecaster in CTBench.


> W3. Diffusion-based models included in the benchmark may exhibit long training and inference times, providing comparisons of generation efficiency across different models would help alleviate concerns in this regard.

We agree that efficiency is critical, especially for frequently retrained crypto systems.
CTBench already includes such comparisons: **Section 4.3 and Figure 9** report wall-clock **training and inference times** for all eight TSG models, including both diffusion models (Diffusion-TS, FIDE).
We also explicitly discuss the **accuracy-efficiency trade-off**, showing that diffusion models yield high fidelity but are better suited for offline pipelines due to their longer runtimes.

We will emphasize this more clearly in the revision to ensure readers do not overlook the included efficiency analysis.

**Summary of Revisions**

In response to the reviewer, we have:
- Clarified that **CTBench is model-agnostic** and justified the dataset choice based on market representativeness, data quality, accessibility, and reproducibility.
- Conducted a **multi-forecaster ablation**, confirming that CTBench's comparative insights are robust across diverse predictors.
- Highlighted existing **efficiency evaluations** and improved clarity around runtime comparisons, especially for diffusion models.
- Improved the paper by adding explanations on extensibility and clarifying the scope of CTBench.

We thank the reviewer again for the thoughtful and constructive feedback and believe these re

### Official Comment by Authors (1/2)
We thank the reviewer for the careful reading and for highlighting both the crypto-specific strengths of CTBench and the practical value of our dual-task evaluation and financial-metric design. 
We respond to each point below.

> W1. Relies solely on Binance's spot hourly data, lacking the diversity of cross-exchange data, alternative crypto asset types such as futures contracts, and different sampling frequencies. Besides, it remains unknown whether this generation method can be effectively extended to a broader range of asset classes, which limits the method's scalability.

We appreciate this important comment and would like to clarify a key point upfront: **CTBench is a benchmark, not a generation method**. 

The dual-task pipeline in Section 3 is **explicitly model-agnostic**: any TSG method that outputs a multivariate return series can be plugged in. Our goal is to standardize **data, tasks, and evaluation**, not to propose a specific generative model that must scale to all markets.

Importantly, **nothing in the benchmark is specific to Binance, spot trading, or hourly frequency**. Any return panel, across exchanges, assets, or frequencies, could be integrated as an additional dataset module.

We chose **Binance spot USDT pairs** for CTBench for three practical and scientific reasons, which we will make explicit in **Appendix B**:

**(1) Market Representativeness**

Multiple independent industry sources confirm that Binance is the **largest centralized exchange by global spot volume** (35~47% in 2024--2025) [1,2,3], and Binance is also among the **largest derivatives exchanges** by 24h trading volume and open interest [4,5]. 
Aggregator sites such as CoinGecko [6] and CoinDesk [7] similarly list Binance as the top CEX by volume and number of markets. Focusing on Binance spot thus **covers the most liquid and widely used venue** in crypto markets, capturing a large fraction of real trading activity. 

Moreover, nearly all major Binance pairs are also listed elsewhere, meaning these prices are informative for the broader market while avoiding the confounding effects of cross-exchange differences in fee structures, matching engines, and data formats.

**(2) Data Quality, Coverage, and Accessibility**

Our curated dataset (in Section 3.1) contains **452 USDT pairs** with continuous hourly data from 2020--2024, covering large-cap, mid-cap, altcoins, and DeFi assets. Hourly frequency offers a strong balance of:
- reduced microstructure noise,
- alignment with common systematic trading horizons,
- tractable panel size for 5-year coverage with 452 assets.

Crucially, Binance provides this entire history **publicly and for free**. Comparable datasets from other major exchanges (e.g., Coinbase [8]) typically require **institutional paid access**, which would make CTBench **non-reproducible** for many academic users. Ensuring **open reproducibility** is a core design principle of CTBench. 

**(3) Benchmark Focus and Extensibility**

CTBench provides a

### Author comment
We thank the reviewer for the positive and detailed assessment, and we appreciate the constructive suggestions. 
We are glad that you find the dataset, benchmark design, and empirical findings valuable for advancing research and applications in financial time-series generation. 
Below we address each concern in turn.

> W1. The predictive utility task fixes the forecasting model to XGBoost for its robustness and interpretability. However, some conclusions may change with alternative predictors, given that different setups have large impacts on the model performance.

> Q1. Is it possible that generative models may have different performance using forecasting models other than XGBoost?

We appreciate this important observation. 
To directly assess whether our conclusions depend on the choice of forecaster, we conducted a **comprehensive ablation across five forecasting architectures: Linear Regression, Random Forest, MLP, Transformer, and XGBoost**, all trained on synthetic data from every TSG model and evaluated on real returns using the same walk-forward protocol. Full results are now reported in **Section 4.4 (Ablation Study)**.

Across all experiments, we observe three consistent patterns:
- **Linear Regression and MLP** exhibit high MSE/MAE and near-zero IC/IR, indicating limited ability to extract either pointwise or cross-sectional signals from synthetic data.
- **Random Forest and Transformer** reduce prediction errors but still fail to capture rank structure, yielding weak IC/IR.
- **XGBoost** consistently achieves the best balance of low error and strong rank correlation, providing the clearest differentiation among TSG models.

These findings confirm that **XGBoost offers the most stable and discriminative evaluation signal for tradable structure**, validating its role as the default forecasting model in CTBench.


> Q2. Are all feature windows strictly backward-looking and computed within the split? Are any scalers fit only on training data? Do all the results hold using different splits?

We appreciate the opportunity to clarify these design choices:
1. **Feature computation is strictly backward-looking**. 
All features, including technical indicators, are computed within each rolling-window split using *only past returns*. No look-ahead leakage occurs.

2. **Scaling follows standard practice**.
When normalization is applied, the scaler is fit exclusively on training features and then applied to the corresponding test features within each split.

3. **Results are robust to split configuration**.
Our evaluation averages over multiple walk-forward splits spanning four distinct market regimes (2021--2024) under a 500-day / 30-day train-test structure, which aligns with real-world crypto backtesting standards. We found that relative model rankings remain stable across these regimes.


> W2. [Minor] Dual-task evaluation module in Figure 2 is visually unclear. Perhaps its readability can be improved by simplifying the contents like the othe

### Author comment
**Summary of Revisions**

To comprehensively address reviewer concerns, we added:
- **Ablation over five forecasters**, confirming XGBoost as the most discriminative evaluator.
- **Two classical baselines (ARMA-GARCH and Bootstrap)** and detailed comparisons on both tasks.
- **Covariance and eigenspectrum diagnostics**, explaining model-specific behaviors such as Fourier-Flow's mismatch between rank fidelity and arbitrage utility.

Together, these additions significantly strengthen CTBench's robustness, interpretability, and practical relevance.

We hope these revisions satisfactorily address all concerns and further improve the clarity and scientific value of the benchmark.

### Author comment
We sincerely thank the reviewer for the careful reading and thoughtful comments. 
We are encouraged that you found CTBench's empirical insights, dual-task design, and finance-first evaluation perspective valuable. 
We have carefully addressed all concerns, added new analyses, and incorporated the corresponding revisions in the updated manuscript. Below, we respond to each point in detail.

> W1. Results are tied to a single forecasting model. Without testing a variety of forecasters, it's unclear whether conclusions generalize. 

> Q3. Have you tested alternative forecasters (e.g., linear model, random forest, and MLP)? Do the relative model performance and rankings persist?

We appreciate this important observation. 
To directly address potential evaluator bias, we conducted a comprehensive ablation over **five forecasting architectures: Linear Regression, Random Forest, MLP, Transformer, and XGBoost**, all trained on synthetic data from every TSG model and evaluated on real returns using the same walk-forward protocol. Full results are now reported in **Section 4.4 (Ablation Study)**.

Across all experiments, three robust patterns emerge:
- **Linear Regression and MLP** produce large MSE/MAE and near-zero IC/IR, showing weak predictive and cross-sectional ability.
- **Random Forest and Transformer** reduce prediction errors but retain near-zero IC/IR, capturing short-term noise rather than tradable structure.
- **XGBoost** consistently provides the strongest combination of low error and high rank correlation, making it the *most discriminative* and *trading-relevant* forecaster.

These findings confirm that **XGBoost is the most reliable evaluator of tradable structure**, justifying its use as the default forecaster in CTBench.


> Q2. Compared with those used in finance economics, such as ARMA-GARCH and the bootstrap, do the learning-based TSG models provide better synthetic data?

We appreciate the suggestion to compare CTBench's TSG models with classical econometric approaches. In the revised manuscript, we add two widely used baselines:
- **ARMA-GARCH (VAR-DCC-GARCH implementation) [1]:** Captures conditional mean, volatility clustering, and dynamic correlation structure of returns. We use a VAR(1) specification for the conditional mean (corresponding to an ARMA(1,0) structure in each marginal series), univariate GARCH(1,1) processes for the conditional variances, and a DCC(1,1) structure for the time-varying conditional correlations. 
- **Bootstrap (Bayesian bootstrap) [2]:** Resamples real returns to preserve marginal distribution and local dependence.

On the **Predictive Utility** task:
- ARMA-GARCH and Bootstrap underperform on MSE/MAE, IC/IR, Sharpe, and CAGR.
- ARMA-GARCH provides conservative but low-alpha signals.
- Bootstrap produces moderate fidelity but weak tradability.
- Learning-based TSG models significantly outperform them in rank metrics and trading performance, capturing cross-sectional alpha and regime shifts that classi

### CTBench: Cryptocurrency Time Series Generation Benchmark


## Meta review / decision
### Paper Decision
Accept (Poster)

## PDF extracted text (first pages)
```text
Published as a conference paper at ICLR 2026
CTBENCH: CRYPTOCURRENCYTIMESERIESGENER-
ATIONBENCHMARK
Yihao Ang1 Qiang Wang1 Qiang Huang2,∗ Yifan Bao1 Xinyu Xi1
Anthony K. H. Tung1 Chen Jin1 Zhiyong Huang1
1Department of Computer Science, National University of Singapore
2School of Intelligence Science and Engineering, Harbin Institute of Technology (Shenzhen)
{yihao ang, yifan bao, atung, huangzy}@comp.nus.edu.sg
{qwang, xinyu xi}@u.nus.edu disjinc@nus.edu.sg
huangqiang@hit.edu.cn
ABSTRACT
Synthetic time series are vital for data augmentation, stress testing, and prototyp-
ing in quantitative finance. Yet in cryptocurrency markets, characterized by 24/7
trading, extreme volatility, and rapid regime shifts, existing Time Series Genera-
tion (TSG) methods and benchmarks often fall short, jeopardizing practical util-
ity. Most prior work targets non-financial or traditional financial domains, fo-
cuses narrowly on classification and forecasting while neglecting crypto-specific
complexities, and lacks critical financial evaluations, particularly for trading ap-
plications. To bridge these gaps, we introduceCTBench, the firstCryptocurrency
Time series generationBenchmark. It curates an open-source dataset of 452 to-
kens and evaluates models across 13 metrics spanning forecasting accuracy, rank
fidelity, trading performance, risk assessment, and computational efficiency. A
key innovation is a dual-task evaluation framework: the Predictive Utility mea-
sures how well synthetic data preserves temporal and cross-sectional patterns for
forecasting, while the Statistical Arbitrage assesses whether reconstructed series
support mean-reverting signals for trading. We systematically benchmark eight
state-of-the-art models from five TSG families across four market regimes, re-
vealing trade-offs between statistical quality and real-world profitability. Notably,
CTBench provides ranking analysis and practical guidance for deploying TSG
models in crypto analytics and trading applications. The source code is available
athttps://github.com/MilleXi/CTBench/.
1 INTRODUCTION
Time Series Generation (TSG) has become foundational for numerous downstream tasks, including
data augmentation (Bao et al., 2024; Ramponi et al., 2018), anomaly detection (Ang et al., 2023b;
Wang et al., 2021), privacy preservation (Jordon et al., 2018; Tian et al., 2024), and domain adap-
tation (Cai et al., 2021; Li et al., 2022b). The core objective of TSG is to synthesize sequences
that preserve the temporal dependencies and structural characteristics of real-world data. Despite
growing interest, the vast majority of existing TSG benchmarks and methods target domains such
as healthcare, mobility, or sensor data (Ang et al., 2023a; 2024). Financial time series, which are
inherently noisy, non-stationary, and adversarial, remain underexplored in the context of generative
modeling. More importantly, even financial TSG efforts primarily focus on stock data (Yoon et al.,
2019; Wiese et al., 2020), often under simplifying assumptions that fail to generalize to emerging
financial modalities. Consequently, the unique characteristics of modern financial markets, particu-
larly in the digital asset space, are largely overlooked.
Cryptocurrencies, as a prominent subclass of financial time series with a global market capital-
ization exceeding $4 trillion as of May 2025 (Reuters, 2025), introduce new modeling and eval-
uation challenges. Unlike traditional financial instruments, crypto markets operate 24/7, lack in-
trinsic valuation anchors, and exhibit extreme volatility driven by speculation, fragmented liquidity,
∗Corresponding author.
1
Published as a conference paper at ICLR 2026
Quant-GAN
COSCI-GAN
TimeVAE
KoVAE
Diffusion-TS
FIDE
Fourier-Flow
LS4
ARMA-GARCH
Bootstrap
  MSE
  MAE
  IC
  IR
CAGR Sharpe
MDD  
VaR  
ES  
CAGR   
Sharpe     
MDD  
VaR  
ES  
CAGR Sharpe
MDD
VaR
ES
10
9
8
7
6
5
4
3
2
1
Forecasting
CSM
LOTQ
PW
    CAGR
    Sharpe
MDDVaR
ES
CAGR    
Sharpe    
MDD VaR
ES
7
6
5
4
3
2
1
Zero Trading Fee
0.03% Trading Fee
Figure 1: Aggregate rankings of eight TSG models on both tasks
from 2021 to 2024: Predictive Utility (left) assesses fidelity and
predictive signal quality, and Statistical Arbitrage (right) evalu-
ates trading performance under realistic fee conditions. The re-
sults reveal distinct trade-offs across fidelity, tradability, and ro-
bustness, with no model uniformly dominating all measures.
and decentralized exchange in-
frastructure. These proper-
ties violate assumptions embed-
ded in existing financial bench-
marks (Hu et al., 2025; Wang
et al., 2025; Qiu et al., 2024),
which typically rely on regular
trading hours, stable macroeco-
nomic signals, or broad station-
arity assumptions.
While recent benchmarks for
financial time series, such
as FinTSB (Hu et al., 2025)
and FinTSBridge (Wang et al.,
2025), have advanced evaluation
practices, they fall short in three
critical aspects when applied to
cryptocurrency settings:
•Limited Domain Generality: Existing works (Ang et al., 2023a; Hu et al., 2025) focus primarily
on traditional assets such as equities and indices (e.g., SPX and CSI300) with lower volatility
and restricted trading hours, offering minimal support for cryptocurrency data. They overlook the
high-frequency, 24/7 dynamics of crypto markets.
•Narrow Task Scope: Most financial time series benchmarks emphasize classification and fore-
casting, neglecting generation and trading-centric tasks like arbitrage, which are vital for crypto-
specific applications such as arbitrage and market-neutral strategies. Moreover, TSG methods in
crypto contexts remain largely unexplored.
•Lack of Crypto-Specific Evaluation: Existing benchmarks underrepresent measures needed to
assess real trading utility. While TSGBench focuses on statistical fidelity, and FinTSB introduces
limited financial metrics, both rely on assumptions from traditional markets, failing to consider
continuous trading, heavy-tailed risk, and actionable signal quality unique to crypto assets.
To address these limitations, we introduceCTBench, the firstCryptocurrencyTime series gen-
erationBenchmark. It is an open-source benchmark for rigorous evaluation of TSG methods in
cryptocurrency markets, with three key contributions:
•Crypto-Centric Dataset.We provide a curated cryptocurrency dataset from major global ex-
changes, processed via a standardized pipeline with crypto-specific feature support. This ensures
analysis-ready data reflecting the volatility and structural nuances of crypto markets.
•Dual-Task Benchmarks.To operationalize the utility of synthetic data in real-world finance,
CTBench introduces a dual-task evaluation framework that jointly assesses predictive fidelity
and tradability. The Predictive Utility task trains forecasters on synthetic data and tests them on
real returns, while the Statistical Arbitrage task evaluates whether reconstructed residuals yield
tradable mean-reverting signals.
•Financial Metric Suite.CTBench introduces a comprehensive evaluation suite over diverse trad-
ing strategies spanning forecasting accuracy, rank-based measures, trading performance, and risk
metrics, designed to reflect crypto-specific market realities.
We benchmark eight state-of-the-art TSG models and analyze trade-offs across fidelity, tradability,
and robustness. Figure 1 shows aggregate rankings across two tasks, with measures radially ar-
ranged and averaged over strategies and fee settings. No model dominates universally, highlighting
distinct trade-offs between fidelity, tradability, and robustness, and underscoring CTBench’s value
for informed model selection in crypto trading contexts.
2 PRELIMINARIES
LetR∈R n×l denote the log-return matrix, wherenis the number of tradable crypto-assets and
lis the number of hourly return observations. At each timet≥1, the log-return vector across
all assets isr t = [r 1,t,· · ·, r n,t]∈R n, where each element is defined asr i,t = log pi,t
pi,t−1
, with
2
Published as a conference paper at ICLR 2026
MSE MAE
IC IR
CAGR SR MDD
VaR ES
Training
Time
Inference
Time
Growth
Curve
Ranking
Plot
TimeVAE
Fourier-Flow
Financial Metric Suite
Crypto-Centric Datasets Trading Strategies
TSG Model Zoo
Dual-Task Evaluation
LS4
Raw Data
Collection
Data
Preprocessing
Feature
Extraction
Cross-Sectional
Momentum
Long-Only
Top-Quantile
Proportional-
Weighting
Long
Quant-GANCOSCI-GAN
Diffusion-TS FIDE
📈  Trading Performance🔢  Error-based ⏱  Efficiency
📊  Rank-based ⚠  Risk Assessment 🌌  Visualization
VAE-based
Diffusion-based
GAN-based
Flow-based Mixed-Type
KoVAE
Botton Decile
Top Decile
Long
Short
Predictive Utility Statistical Arbitrage
Figure 2: Overall architecture ofCTBench. The framework unifies five modules: (1) crypto-centric
datasets, (2) dual-task evaluation (predictive utility and statistical arbitrage), (3) trading strategies,
(4) comprehensive financial metrics, and (5) diverse TSG models into a unified benchmark pipeline.
pi,t the price of assetiat hourt. To mimic real-world backtesting, we employ a rolling-window
protocol: Given a training window sizewand a test steps, we define split offsetsτ∈ O=
{w, w+s,· · ·, w+ (k−1)s}, wherek=⌊ l−w
s ⌋. Each offsetτyields a training and test split:
R(τ)
train = [rτ−w+1 ,· · ·,r τ],R (τ)
test = [rτ+1 ,· · ·,r τ+s].
For each split, a TSG modelg (τ) is trained onR (τ)
train and evaluated in two modes: (1)Generation
Mode: sampling synthetic sequences from Gaussian noise,R gen =g (τ)(z),z∼ N(0,I); (2)Re-
construction Mode: reconstructing training and test set, ˆRtrain =g (τ)(R(τ)
train), ˆRtest =g (τ)(R(τ)
test ).
We further define a basic portfolio simulation setup: Starting with initial capitalV0 >0, the strategy
allocates weightsη t = [η1,t,· · ·, η n,t]∈R n at each hourt, whereη i,t denotes the fraction invested
in asseti. The portfolio value then evolves asV t =V t−1 ×(η t ·r t), with hourly profit-and-loss given
by∆V t =V t −V t−1. A summary of notations is provided in Appendix A. To maintain clarity and
scope, CTBench restricts its benchmark design to datasets, trading strategies, evaluation measures,
and TSG models, as detailed in Appendix B.
3 CTBENCH
We presentCTBench, the first benchmark specifically designed to evaluate Time Series Generation
(TSG) models in cryptocurrency markets (Figure 2).
3.1 CRYPTO-CENTRICDATASETS
Data Overview and Preprocessing.Our benchmark leverages historical hourly data from all
USDT-denominated spot pairs on Binance (Binance Exchange, 2025b), spanning January 2020 to
December 2024 and capturing diverse market regimes such as bull runs, crashes, and consolidation
phases. To ensure quality, we exclude assets with missing records and retain only USDT pairs,
yielding 452 unique cryptocurrencies, a robust foundation for TSG evaluation.
Formally, letndenote the number of tradable crypto assets and(l+ 1)the number of hourly obser-
vations. Each asseti∈ {1,· · ·, n}at timet∈ {0,· · ·, l}is represented by four standard fields:
xi,t = [Oi,t, Hi,t, Li,t, Ci,t]∈R 4,
whereO,H,L, andCare theOpen,High,Low, andCloseprices (quoted in USDT), respectively.
Stacking across all assets yields the multi-asset OHLC data array:D= [x i,t]∈R n×(l+1)×4.
We focus primarily onCloseprices and define hourly log-returns as:r i,t = log Ci,t
Ci,t−1
, where
t∈ {1,· · ·, l}, giving the return matrixR∈R n×l.
3
Published as a conference paper at ICLR 2026
Prediction Return: 
Training Data 
Generation 
Feature Set
Forecasting 
Model 
Test Data 
TSG Model Feature Set
Input
Training Phase TradingPhase
Output
Trained Forecasting
Model 
(a) Predictive Utility task.
Training Data 
ResidualTSG Model 
Reconstruction OU Process 
with 
Test Data 
Reconstruction
Trained 
TSG Model 
Residual
Fitted
OU Process
Training Phase Trading Phase
Input
Trading Signal Generation: Portfolio Allocation: ,Output (b) Statistical Arbitrage task.
Figure 3: Architectures of dual-task benchmarks.
Feature Extraction.To capture key market dynamics, we extractdfeatures widely used in quan-
titative trading, such as Alpha101 factors (Kakushadze, 2016), Bollinger Bands, RSI, and moving
averages (Sun et al., 2023; Zhu & Zhu, 2025; Zhang et al., 2020; Tsai & Hsiao, 2010). These fea-
tures encode signals such as momentum, mean-reversion, and volatility. Applying the same pipeline
to both real and synthetic data enables consistent evaluation of TSG models’ ability to replicate the
statistical and structural properties vital for downstream tasks. Formally, letΦ={ϕ j}d
j=1 be the
feature set, where eachϕ j :R n×l →R n×l acts on the return matrixR. ApplyingΦyields a feature
tensor with shapeR n×l×d. The dataset exhibits strong cross-sectional dispersion and cap-dependent
volatility, motivating crypto-specific evaluation of predictive structure and cross-asset dynamics be-
yond marginal similarity (see Appendix C.1).
3.2 DUAL-TASKEVALUATION
To connect generation fidelity with financial utility, CTBench introduces dual-task evaluation as-
sessing both predictive realism and tradable structure. As shown in Figure 3, these tasks measure
whether synthetic data preserves useful forecasting signals (predictive utility) or enables the discov-
ery of stationary, market-neutral alpha (statistical arbitrage). Details are in Appendix C.2.
Predictive Utility Task.This task tests whether synthetic data can train forecasters that generalize
to real markets. As shown in Figure 3(a), given a training log-return windowR (τ)
train, a TSG model
ggenerates synthetic returnsR gen =g(z),z∼ N(0,I). FeaturesΦ(R gen)are extracted to
train a forecasting modelf, instantiated as XGBoost (Chen & Guestrin, 2016) for its robustness
to heterogeneous and noisy financial features (Vancsura et al., 2025; Liu et al., 2021; Yun et al.,
2021). The ablation in§4.4shows that XGBoost best balances low prediction error and strong
cross-sectional ranking fidelity, making it the most informative evaluator for trading utility.
The trainedfis deployed on real test dataR test to generate signals for a dollar-neutral long-short
portfolio, rebalanced hourly over a month. This setup tests whetherRgen preserves predictive signals
with measurable economic value. All components, the TSG model, features, and the forecaster, are
modular, allowing extensibility across architectures.
Statistical Arbitrage Task.In contrast to the generation-focused task, this task evaluates whether
TSG models can reconstruct market structure and isolate tradable, mean-reverting residuals for sta-
tistical arbitrage. As depicted in Figure 3(b), a modelgis trained on real returnsR train to produce
reconstructions ˆRtrain, and the residualsρ i,t =r i,t −ˆri,t are assumed to follow Ornstein–Uhlenbeck
(OU) processes (Uhlenbeck & Ornstein, 1930), parameterized by estimated(µ i, θi, σi)per asset.
On test data, new residualsϵ i,t are mapped to standardizeds-scoress i,t = (ϵi,t −µ i)/(σi/√2θi),
which drive trading decisions via thresholding (γ= 2) and weight normalization. Portfolios are
rebalanced hourly based on these signals. This task complements generation-focused evaluation
by assessing the model’s ability to reveal stationary, market-neutral alpha, thus bridging statistical
fidelity and practical trading utility.
3.3 TRADINGSTRATEGIES
CTBench is strategy-agnostic, evaluating TSG models across diverse trading paradigms. Profitabil-
ity and risk metrics (§3.4) are computed uniformly for all backtests, enabling rigorous stress testing
4
Published as a conference paper at ICLR 2026
whether models capture genuine market structure rather than overfitting specific strategies. We eval-
uate models under three canonical trading strategies commonly adopted in cryptocurrency markets:
•Cross-Sectional Momentum (CSM):take long positions in the top decile of predicted assets
while shorting the bottom decile, capturing relative momentum effects.
•Long-Only Top-Quantile (LOTQ):build an equal-weight portfolio of the top 20% of assets,
reflecting long-biased strategies often favored in practice.
•Proportional Weighting (PW):allocate capital in proportion to predicted returns, directly trans-
lating forecasts into position sizes.
This modular design supports plug-and-play integration of additional or proprietary strategies. Full
details are provided in Appendix C.3.
3.4 FINANCIALMETRICSUITE
Evaluating TSG models for financial applications requires more than mere statistical similarity, it
demands measuring whether synthetic data enables profitable and risk-aware trading. To this end,
CTBench defines thirteen core metrics, grouped into six practitioner-relevant categories:
•Error-based Evaluation:At the most fundamental level, do synthetic returns numerically re-
semble real ones? Metrics include Mean Squared Error (MSE), which emphasizes volatility
mismatches, and Mean Absolute Error (MAE), which is more robust to outliers.
•Rank-based Evaluation:Do synthetic returns preserve relative asset ordering? Information
Coefficient (IC) measures rank correlation, and Information Ratio (IR) evaluates its stability.
•Trading Performance:Does synthetic data yield actionable, profitable signals? Statistical accu-
racy does not guarantee financial profitability. We therefore use Compound Annual Growth Rate
(CAGR) for long-term growth and Sharpe Ratio (SR) for return-to-risk balance.
•Risk Assessment Metrics:Do models capture fat tails and downside risks? We compute Max-
imum Drawdown (MDD) for worst-case loss, Value at Risk (VaR) at 95% confidence, and Ex-
pected Shortfall (ES) for tail risk beyond VaR.
•Efficiency:Can models support real-time deployment? We trackTraining TimeandInference
Timeto assess adaptability in fast-moving crypto markets.
•Visualization:Do results exhibit contextual realism? We reportSimulated Growth Curves
for a $10,000 investment and cross-sectionalRanking Plotsacross market regimes to illustrate
interpretability and contextual realism.
Together, these metrics ensure balanced evaluation of fidelity, utility, and practicality. Full defini-
tions are in Appendix C.4.
3.5 TSG MODELZOO
Generative models for time series aim to capture temporal dependencies and structural patterns, with
backbones spanning GANs, V AEs, diffusion models, flow models, and mixed-type models (Ang
et al., 2023a; Nikitin et al., 2023) (see Table 3). Yet, nearly half of prior TSG works do not evaluate
in financial contexts, and those that do typically focus on traditional markets such as equities or
macroeconomic data, leaving a gap for cryptocurrency applications. To close this gap, CTBench
evaluates eight state-of-the-art models spanning five families:
•GANs: Quant-GAN(Wiese et al., 2020) andCOSCI-GAN(Seyfi et al., 2022), applied only in
forecasting tasks since GANs do not natively support reconstruction (Goodfellow et al., 2020).
•V AEs: TimeV AE(Desai et al., 2021) andKoV AE(Naiman et al., 2024b), which extend varia-
tional autoencoders for temporal dynamics.
•Diffusion Models: Diffusion-TS(Yuan & Qiao, 2024) andFIDE(Galib et al., 2024), leveraging
denoising-based generative processes for time series.
•Flow-based Models: Fourier-Flow(Alaa et al., 2021)), employing invertible transformations for
likelihood-based generation.
•Mixed-type Models: LS4(Zhou et al., 2023), designed to unify strengths across multiple gener-
ative paradigms.
These models are selected for their generative fidelity and practical relevance to financial down-
stream tasks. Further details are in Appendix C.5.
5
Published as a conference paper at ICLR 2026
10 5
10 3
10 1
MSE
10 3
10 2
10 1
MAE
2021 2022 2023 2024 -0.1
0
0.4
IC
2021 2022 2023 2024
100
0
101
IR
Quant-GAN COSCI-GAN TimeVAE KoVAE Diffusion-TS FIDE Fourier-Flow LS4 ARMA-GARCH Bootstrap
Figure 4: Annual forecasting performance of TSG models on the Predictive Utility task.
Quant-GAN COSCI-GAN TimeVAE KoVAE Diffusion-TS FIDE Fourier-Flow LS4 ARMA-GARCH Bootstrap
102
0
103
CAGR (%)
CSM
102
0
103 LOTQ
102
0
103 PW
101
0
102
Sharpe
101
0
102
101
0
102
0
25
   50
MDD (%)
0
50
100
0
50
100
0
  0.1
0.2
VaR (%)
0
1
2
0
1
2
2021 2022 2023
```
