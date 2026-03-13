# Time Series Research Radar

一个面向时序研究者的开源研究情报整理项目。

## 项目定位
Time Series Research Radar 用于持续跟踪时间序列相关会议论文，并自动产出：
- 会议论文跟踪清单
- topic clustering
- method map
- benchmark map
- rebuttal / reviewer pattern mining
- weekly digest

本项目当前聚焦 **ICLR / NeurIPS / ICML / AAAI / KDD** 中与时间序列相关的论文，优先支持 OpenReview 公开讨论内容的结构化整理。

## 当前阶段
当前处于 **Phase 1: 最小闭环搭建**。

当前最小闭环：
1. 维护会议/年份分类的公开论文资料目录
2. 保存公开的 OpenReview 审稿 / rebuttal 线程整理
3. 生成 markdown 索引与 weekly digest 骨架
4. 后续在公开资料层上继续做 topic clustering、method map、benchmark map

## 目录结构
```text
radar/
  data/
    conferences/
    raw/
    curated/
  outputs/
    papers/
    digests/
    maps/
  config/
  docs/
scripts/
```

## 安装
```bash
python -m venv .venv
. .venv/Scripts/activate
pip install -r requirements.txt
```

## 使用方式
### 1. 初始化目录
```bash
python scripts/init_workspace.py
```

### 2. 生成会议索引
```bash
python scripts/build_conference_readme.py
```

### 3. 生成基础 paper index
```bash
python scripts/build_index.py --input radar/data/curated/papers.json --output radar/outputs/paper_index.md
```

### 4. 生成周报骨架
```bash
python scripts/generate_digest.py --week 2026-W11
```

## 当前公开资料入口
- `radar/data/conferences/ICLR/2026/`

## 适用对象
- 博士生 / 硕士生
- AI 研究员
- 做时序建模、投稿、rebuttal、文献追踪的人

## 为什么做这个项目
当前时序论文信息分散在 OpenReview、arXiv、公众号、社媒与仓库中。研究者往往花大量时间做低价值筛选，而不是做高价值判断。这个项目希望把“检索、分类、归档、比较、每周更新”这条链条做成可复用、可维护的公共工具。

## 开源维护原则
- 公开仓库
- 来源可追溯
- 输出尽量结构化
- 允许人工修订优先于全自动覆盖
- 不伪造评审、实验和引用信息
- 不将私人研究核心笔记直接并入公开资料层

## Roadmap
见 `ROADMAP.md`

## 更新日志
见 `CHANGELOG.md`

## 许可证
暂定 MIT（后续可根据数据来源边界调整）
