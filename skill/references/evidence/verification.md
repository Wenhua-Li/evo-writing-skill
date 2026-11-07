# 本地验证记录

本文件记录公开发布前的可说明验证。内部语料路径、会话文件和原始论文内容不包含在公开仓库中。

## 1. 语料与统计

- 主语料候选：1,517 个 Markdown 文件，年份范围 1997–2023。
- 语言统计：1,358 篇；高噪声复核：100 篇；仅元数据：59 篇。
- 三类合计与候选文件数一致。
- 公开 CSV 中年份字段未发现 2024 年及以后记录。
- 摘要、章节、领域、词频、搭配和修辞统计脚本均可运行，重跑输出一致。

## 2. v0.4.0 结构验证

- 根目录精简为 15 项（不含 `.git`、`build/`、`dist/`）。
- Skill 运行时材料统一位于 `skill/`；文档与视觉资产位于 `docs/`；开发工具位于 `tools/`。
- `SKILL.md` 的运行时路径已更新为 `skill/references/...` 和 `skill/templates/...`。
- `install-manifest.txt` 与公开文件清单一致，共 96 个文件。
- Release ZIP 顶层为 `evo-write/`，并包含 `evo-write/SKILL.md` 与 `evo-write/skill/`。

## 3. 视觉验证

- 新版 banner、logo 和 social preview 均为本地 SVG，无外部图片依赖。
- Pages 首页通过本地浏览器截图验证。
- 发现并修复了 `.fade` 元素默认 `opacity: 0` 的可访问性问题；动画现在只是增强效果，不会导致 reduced-motion 或截图状态下内容不可见。
- HTML 文件通过基础解析检查，Markdown 相对链接检查无断链。

## 4. 安装与真实调用

- `install.sh` 通过 `bash -n` 语法检查。
- Python 脚本通过 `py_compile`。
- 本地执行 `./install.sh --agent kimi --force` 成功。
- `./install.sh --agent kimi --doctor` 验证安装有效。
- Release ZIP 解压后的安装结构验证通过。
- 使用 Kimi Code CLI 0.41.0 调用 `evo-write` 成功，输出：

> The proposed method outperforms the compared state-of-the-art algorithms on the problems tested.

行为符合预期：删除宏大开场、空泛 `novel`、堆叠 hedging、空泛 `state-of-the-art` 和防御性免责声明，只返回英文文本。

## 5. 未自动化项

- 没有声称人工逐字精读全部 1,517 篇；定性证据来自全语料自动分析和 150 篇分层重点阅读。
- 自然度验证基于真实调用与人工判读，尚未进行多人盲评实验。
- PowerShell 安装脚本已做静态检查，但当前验证环境没有 `pwsh` 可执行文件，未进行真实 PowerShell 安装。
