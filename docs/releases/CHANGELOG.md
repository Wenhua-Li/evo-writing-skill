# Changelog

## v0.4.0

### Changed

- 仓库重构为产品化结构：根目录只保留 README、许可证、Skill 入口和安装入口。
- Skill 运行时内容统一移入 `skill/`：`references/`、`voice/`、`examples/`、`templates/`、`data/`。
- 公开文档、案例、发布记录和视觉资产统一移入 `docs/`。
- 分析脚本与行为评测统一移入 `tools/`。
- `CONTRIBUTING.md` 与 `CODE_OF_CONDUCT.md` 移入 `.github/`。
- `SKILL.md` 中所有运行时路径更新为 `skill/...`。
- 安装器默认版本升级为 `v0.4.0`。

### Added

- 新版品牌视觉：`docs/assets/banner.svg`、`logo.svg`、`social-preview.svg`。
- 新版 GitHub Pages 首页，包含导航、统计、案例切换、使用场景、EC 标签、安装卡片、证据边界与 FAQ。
- 新增 `docs/cases.html` 与 `docs/install.html`。

## v0.3.3

### Fixed

- 修复 Bash 安装器在命令替换中混入下载日志的问题；该问题会导致 Release ZIP 已下载成功但安装路径解析失败。

## v0.3.2

### Changed

- 安装器默认安装最新 Release ZIP，而不是从 Git 分支下载源码包。
- 远程安装顺序改为：Release asset 优先，`install-manifest.txt` + raw.githubusercontent.com 逐文件下载作为后备。

## v0.3.1

### Fixed

- 安装器从 GitHub tarball/codeload 下载改为 `install-manifest.txt` + raw.githubusercontent.com 逐文件下载。

## v0.3.0

### Changed

- 项目品牌从 `ec-writing` 改为 `EvoWrite`；Skill 名称改为 `evo-write`。
- README 重构为开源产品首屏。

## v0.2.0

### Changed

- 将核心目标从“证据合规优先”改为“自然 EC 学术成稿优先”。
- 默认输出从中文诊断报告改为直接英文论文文本。
