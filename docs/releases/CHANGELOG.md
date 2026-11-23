# Changelog

## v0.6.0

### Changed

- 用 Skill 自身的重写规则改写项目对外文案:SKILL.md description、双 README、docs 指南与站点页面,去除 AI 腔词汇、宣传措辞和格式化对比,事实、数字与命令保持不变。
- 改写后的英文文案通过 `tools/scripts/check_prose.py` 检查;Before 演示文本作为反例保留。
- Skill 规则、参考资料、示例与数据与 v0.5.0 完全一致,无行为变化。
- 安装器默认版本升级为 `v0.6.0`。

## v0.5.0

### Changed

- 将建议式润色重构为“语义清单—脱稿重建—Plain-EC 重写—强制门禁—事实回查”流程。
- 所有写作模式必须读取统一语言规范；Voice Match 与原始草稿不再豁免违禁表达。
- 合并重复、软弱的 AI 痕迹规则，旧风格文件仅保留兼容入口。
- 移除方法与实验指南中的固定段落、强制 RQ 和统一结果句式倾向。
- 清理正向示例和推荐表达中的工程隐喻、格式化对比及生僻词。
- 根据新旧版本真实配对实测，进一步拦截 `instead of` 绕过、空泛研究兴趣开场、防御性免责声明和同义保留强主张。
- Draft 不得从方法名称推断内部步骤；Audit 的 Revised text 不得虚构已有实验与比较。
- 发布包严格按 `install-manifest.txt` 构建，不再混入未列入清单的开发素材。

### Added

- 新增 `plain-ec-english.md` 与 `revision-gate.md` 两份强制规范。
- 新增 `skill/data/prose-gate.json`，集中管理词汇、词形、句式、重复规则和窄技术例外。
- 新增 `tools/scripts/check_prose.py`，对完整候选文本执行可重复检查并以状态码报告失败。
- 新增 12 个真实语言改写用例、确定性 fixtures 和单元测试。
- 发布构建现在检查所有推荐的 After 示例，防止示例重新引入违禁表达。

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
