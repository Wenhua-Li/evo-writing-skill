<div align="center">

<img src="assets/banner.svg" alt="EvoWrite banner" width="100%">

# EvoWrite

**面向 Evolutionary Computation 论文的自然、证据感知写作 Skill。**

基于 **1,517 篇 TEVC 论文（1997–2023）** 和 150 篇分层样本复核构建。EvoWrite 在保留研究主张、实验证据、EC 术语和作者声音的前提下，去除 AI 味、模板味和防御性写作。

[English](README.md) · [快速开始](#快速开始) · [示例](examples/) · [文档](docs/)

[![Release](https://img.shields.io/badge/release-v0.3.3-38bdf8)](https://github.com/Wenhua-Li/evo-writing-skill/releases)
[![Agent Skills](https://img.shields.io/badge/agent--skills-compatible-14b8a6)](https://agentskills.io)
[![License](https://img.shields.io/badge/license-MIT%20%2F%20CC--BY--4.0-blue)](LICENSE)
[![Corpus](https://img.shields.io/badge/TEVC%20corpus-1997--2023-94a3b8)](references/evidence/methodology.md)

</div>

---

## 直接看效果

<table>
<tr>
<th>修改前：AI 味 + 防御性</th>
<th>修改后：自然 EC 学术表达</th>
</tr>
<tr>
<td>

> With the rapid development of evolutionary computation, large-scale multiobjective optimization has become a hot topic. It is worth noting that our proposed method may potentially significantly outperform state-of-the-art algorithms, although we do not claim that it is universally optimal for all problems. The main contributions are as follows: 1) We propose a novel framework. 2) We design an efficient operator. 3) We conduct extensive experiments.

</td>
<td>

> Large-scale multiobjective optimization remains challenging for evolutionary algorithms as the number of decision variables increases. This paper addresses this setting and makes three contributions: a framework for large-scale multiobjective optimization, an efficient search operator, and an extensive experimental evaluation. On the tested problems, the proposed algorithm outperforms the state-of-the-art algorithms included in the comparison.

</td>
</tr>
</table>

不编造结果，不写防御性免责声明，也不保留通用 AI 套话。

## 为什么不是普通 humanizer？

通用 humanizer 可以让句子更顺，但它不知道 EC 论文中哪些话在技术上越界。EvoWrite 同时检查**人类可读性**和**领域证据口径**：

- 区分 function evaluations、墙钟时间、模型训练成本和实现复杂度；
- 区分 convergence、diversity、feasibility、objective value 和 fitness；
- 理解昂贵、约束、动态、大规模、多峰、多目标等优化环境；
- 去除宏大开场、模板贡献列表、机械 RQ、堆叠 hedging 和防御性免责声明；
- 保留必要的方法学边界，但只写一次并放在正确章节；
- 可以按作者自己的英文样本匹配句长、节奏和术语习惯。

## 快速开始

### 一键安装

```bash
npx skills add Wenhua-Li/evo-writing-skill
```

或使用安装脚本：

```bash
curl -fsSL https://raw.githubusercontent.com/Wenhua-Li/evo-writing-skill/main/install.sh | bash
```

Windows PowerShell：

```powershell
iwr https://raw.githubusercontent.com/Wenhua-Li/evo-writing-skill/main/install.ps1 | iex
```

手动安装时，将本仓库复制为 Agent 技能目录下的 `evo-write/`。Kimi Code 默认路径：

```text
%USERPROFILE%\.agents\skills\evo-write\
```

### 第一次改写

```text
Use evo-write. Rewrite this introduction to remove AI tells and defensive writing.
Return only the revised English.
```

### 作者声音匹配

```text
Use evo-write. Here are two paragraphs from my previous paper. Match their rhythm and terminology, then rewrite the following method section.
```

### 证据审查

```text
Use evo-write in Audit mode. Check this abstract for unsupported significance, robustness, scalability, and cost claims.
```

## 核心能力

### 去 AI 味

- 去除 `rapid development`、`hot topic`、`plays a crucial role` 等空泛开场；
- 降低机械三点贡献、固定 RQ、重复连接词和均匀段落；
- 处理无证据的 `novel`、`efficient`、`robust`、`scalable`、`state-of-the-art`；
- 从段落级重写，而不是同义词替换。

### 去防御性写作

- `We do not claim...` → `The evaluation focuses on...`
- `may potentially suggest` → `suggests` / `indicates` / 有边界的具体表述
- 摘要和结论中重复的限制 → 在方法、实验或讨论中写一次具体边界

### 保留研究含义

不新增或偷改：

- 引用、DOI、数值、负结果、不确定性、定理条件；
- benchmark、基线、指标、预算、统计检验；
- 算法机制、假设、应用约束。

### Audit 模式

用户明确要求时，检查：

- 无统计检验的 `statistically significant`；
- 无保证的 `optimal`；
- 未定义扰动的 `robust`；
- 未定义维度与预算的 `scalable`；
- 未定义成本口径的 `efficient`。

## 证据边界

公开包不包含原始论文，只包含原创规则、模板、脚本和聚合统计。

- 主语料：1997–2023 年 TEVC，共 1,517 篇；
- 语言统计：1,358 篇质量可控论文；
- 定性复核：150 篇分层样本；
- 排除：2024 年及以后、年代不明的 early access；
- 语料用于领域校准，不用于生成固定模板。

详见 [`references/evidence/methodology.md`](references/evidence/methodology.md) 和 [`references/evidence/limitations.md`](references/evidence/limitations.md)。

## 限制

- EvoWrite 提升自然度与主张校准，不承诺论文录用；
- 目标不是欺骗 AI 检测器，而是让人类审稿读者觉得自然；
- 语料证据来自 TEVC，不代表 IEEE 或 TEVC 官方立场；
- 原始论文不包含在公开仓库中；
- 作者声音匹配效果取决于样本质量。

## 贡献

欢迎提交：

- EC 专用 before/after 示例；
- 无证据强主张的行为案例；
- 覆盖不足领域的写作规则；
- 安装器与兼容性改进。

见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

## 引用

```bibtex
@software{li_evowrite_2026,
  author  = {Li, Wenhua},
  title   = {EvoWrite: Natural Evolutionary Computation Paper Writing},
  year    = {2026},
  version = {0.3.3},
  url     = {https://github.com/Wenhua-Li/evo-writing-skill},
  license = {MIT and CC-BY-4.0}
}
```

## 致谢

结构性 AI 痕迹处理思路受到 [blader/humanizer](https://github.com/blader/humanizer) 启发；claim-forward 与 positive scope 思路受到 [Kiterlin/anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing) 启发。本项目规则、示例和领域证据均针对 Evolutionary Computation 重新设计。

## 许可证

- 脚本：[MIT License](LICENSE)
- Skill 文档、规则、模板、示例和聚合数据：[CC BY 4.0](LICENSE-CC-BY-4.0)
