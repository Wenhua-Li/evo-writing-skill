# 本地验证记录

本文件记录公开发布前的可说明验证。内部语料路径、会话文件和原始论文内容不包含在公开仓库中。

## 1. 语料与统计

- 主语料候选：1,517 个 Markdown 文件，年份范围 1997–2023。
- 语言统计：1,358 篇；高噪声复核：100 篇；仅元数据：59 篇。
- 三类合计与候选文件数一致。
- 公开 CSV 中年份字段未发现 2024 年及以后记录。
- 摘要、章节、领域、词频、搭配和修辞统计脚本均可运行，重跑输出一致。

## 2. v0.2.0 写作行为验证

使用 Kimi Code CLI 0.41.0 验证：

- 默认英文人声改写：只返回英文，不输出中文诊断或风险报告；
- 信息不足起草：能写出可支撑内容，仅在文后列最多三项缺失，不使用 `[MISSING]` 污染正文；
- 显式 Audit：能识别 `proves/optimal`、`all`、`significantly`、`robust/scalable` 等证据问题；
- 已安装 Skill 能正确读取分层引用文件。

## 3. v0.3.0 开源产品化验证

### 包与安全

- Release 包包含 94 个公开文件；
- 包内不含 `build/`、`dist/`、`.git/`、`__pycache__/`；
- 包内不含 1997–2026 原始语料目录；
- 未发现本机绝对路径、会话路径或私有缓存路径；
- 公开 Markdown 相对链接检查无断链；
- ZIP 顶层目录为 `evo-write/`，入口 `SKILL.md` 声明 `name: evo-write`。

### 安装器

- `install.sh` 通过 `bash -n` 语法检查；
- Python 脚本通过 `py_compile`；
- 本地执行 `./install.sh --agent kimi --force` 成功；
- `./install.sh --agent kimi --doctor` 验证安装有效；
- `./install.sh --agent generic --dry-run` 正确显示来源、目标和备份行为；
- Release ZIP 解压后的安装结构验证通过。

### 真实调用

使用用户级技能目录中的 `evo-write/` 调用：

输入：

> With the rapid development of evolutionary computation, our novel method may potentially significantly outperform state-of-the-art algorithms, although we do not claim universal optimality.

输出：

> The proposed method outperforms the compared algorithms on the tested problems.

行为符合预期：

- 删除宏大开场；
- 删除无依据 `novel`、`may potentially significantly` 和空泛 `state-of-the-art`；
- 将 `we do not claim universal optimality` 转为 `on the tested problems` 的正向范围；
- 只返回英文文本，无诊断报告。

## 4. 未自动化项

- 没有声称人工逐字精读全部 1,517 篇；定性证据来自全语料自动分析和 150 篇分层重点阅读。
- 自然度验证基于真实调用与人工判读，尚未进行多人盲评实验。
- PowerShell 安装脚本已做静态检查，但当前验证环境没有 `pwsh` 可执行文件，未进行真实 PowerShell 安装。
