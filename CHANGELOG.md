# CHANGELOG

## 0.3.0 - 2026-03-13
### Added
- 增加 `NeurIPS/2026`、`ICML/2026`、`KDD/2026` 目录骨架
- 增加统一论文下载脚本 `download_papers.py`
- 增加会议 manifest 模板 `conference_template.json`
- 增加多会议索引生成脚本 `build_all_conference_indexes.py`
- 增加下载策略说明 `DOWNLOAD_POLICY.md`

### Notes
- 这一版本先把多会议维护能力搭起来，下一步再补各会议第一批公开论文元数据。

## 0.2.0 - 2026-03-13
### Added
- 增加 `radar/data/conferences/ICLR/2026/` 公开资料目录
- 增加 14 篇 ICLR 2026 时间序列论文的 manifest（论坛链接 / PDF 链接 / 分类）
- 复制 14 组对应的 OpenReview 审稿线程整理（raw / structured）
- 增加会议索引生成脚本 `build_conference_readme.py`
- 增加公开资料层边界文档 `SOURCE_POLICY.md`

### Changed
- README 调整为“公开资料层优先”定位
- 移除对私有博士级样板笔记的挂接说明

## 0.1.0 - 2026-03-13
### Added
- 初始化仓库结构
- 增加 README、ROADMAP、CHANGELOG
- 增加基础脚本：初始化、索引生成、周报生成
- 增加 ICLR2026 示例数据与输出目录

### Notes
- 当前版本为最小闭环原型，目标是先形成真实可维护仓库，而不是一次性做大。
