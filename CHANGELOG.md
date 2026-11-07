# Changelog

## v0.3.3

### Fixed

- 修复 Bash 安装器在命令替换中混入下载日志的问题；该问题会导致 Release ZIP 已下载成功但安装路径解析失败。
- 下载进度和错误信息现在输出到 stderr，安装源路径只通过 stdout 返回。

## v0.3.2

### Changed

- 安装器默认安装最新 Release ZIP，而不是从 Git 分支下载源码包。
- 远程安装顺序改为：Release asset 优先，`install-manifest.txt` + raw.githubusercontent.com 逐文件下载作为后备。
- 为远程下载增加重试和受限网络容错。

## v0.3.1

### Fixed

- 安装器从 GitHub tarball/codeload 下载改为 `install-manifest.txt` + raw.githubusercontent.com 逐文件下载，提高在受限网络中的一键安装成功率。
- 新增 `install-manifest.txt`，使远程安装内容可枚举、可校验。

## v0.3.0

### Changed

- 项目品牌从 `ec-writing` 改为 `EvoWrite`；Skill 名称改为 `evo-write`。
- README 重构为开源产品首屏：品牌图、before/after、一键安装、竞品对比、证据边界和引用信息。
- 发布包顶层安装目录改为 `evo-write/`。

### Added

- 英文 README 与 `README.zh-CN.md`
- `assets/` 品牌图与社交预览图
- `docs/index.html` GitHub Pages 落地页
- `docs/comparison.md`、`docs/quickstart.md`、`docs/prompts.md`
- `install.sh`、`install.ps1`、`INSTALL.md`
- `CITATION.cff`
- `CONTRIBUTING.md`、`CODE_OF_CONDUCT.md`、`THIRD_PARTY_NOTICES.md`
- GitHub issue/PR templates
- `evals/` 行为评测说明与案例

## v0.2.0

### Changed

- 将核心目标从“证据合规优先”改为“自然 EC 学术成稿优先”。
- 默认输出从中文诊断报告改为直接英文论文文本。
- 证据检查改为后台静默执行，Audit 仅在用户请求时启用。
- 占位符策略收紧：只有用户明确要求 skeleton 时才使用 `[MISSING]`。
- 降低贡献列表、RQ 和固定章节模板的使用优先级。

### Added

- `references/style/human-scholarly-voice.md`
- `references/style/ec-ai-tells.md`
- `references/style/anti-defensive-ec.md`
- `references/style/claim-calibration.md`
- `voice/` 下四类论文声音配置
- `examples/` 下 EC 专用 before/after 样本

## v0.1.0

首个公开候选版本：语料分析、证据库、分章节/领域写作规则、风险表达体系和可复跑脚本。
