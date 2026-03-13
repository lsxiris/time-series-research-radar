# Causal Time Series Generation via Diffusion Models — OpenReview Structured Summary

- OpenReview ID: `9bkzvYw9ds`
- Forum: https://openreview.net/forum?id=9bkzvYw9ds
- PDF: https://openreview.net/pdf?id=9bkzvYw9ds
- Venue status: ICLR 2026 Conference Desk Rejected Submission
- 平均review分数（公开review）: 7.33
- 分数范围: 6.0-8.0

## reviewer concerns
- experimental adequacy: 2
- complexity/efficiency: 2
- robustness/hyperparameter: 2
- assumption/boundary: 1
- theory/identifiability: 1
- reproducibility/clarity: 1

## author responses
- 补实验/补指标: 1
- 补解释/补理论: 1
- 补相关工作: 1
- 收缩主张/承认局限: 1
- 补效率报告: 1
- 改表述/改图示: 1

## decision / meta review
- Submission Desk Rejected by Program Chairs
- This submission has manipulated the ICLR template to have smaller margins and must be desk rejected.

## global response highlights
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

## score change
- 暂未自动抓到显式 score change 记录；当前保留公开评审分数区间 `6.0-8.0` 作为 rebuttal 前窗口。
