<div align="center">

<img src="docs/assets/banner.svg" alt="EvoWrite banner" width="100%">

# EvoWrite

**面向 Evolutionary Computation 论文的自然、证据感知写作 Skill。**

基于 **1,517 篇 TEVC 论文（1997–2023）** 和 150 篇分层样本复核构建。EvoWrite 在保留研究主张、实验证据、EC 术语和作者声音的前提下，去除 AI 味、模板味和防御性写作。

[English](README.md) · [快速开始](docs/quickstart.md) · [案例](docs/cases.html) · [文档](docs/)

[![Release](https://img.shields.io/badge/release-v0.4.0-38bdf8)](https://github.com/Wenhua-Li/evo-writing-skill/releases)
[![Agent Skills](https://img.shields.io/badge/agent--skills-compatible-14b8a6)](https://agentskills.io)
[![License](https://img.shields.io/badge/license-MIT%20%2F%20CC--BY--4.0-blue)](LICENSE)
[![Corpus](https://img.shields.io/badge/TEVC%20corpus-1997--2023-94a3b8)](skill/references/evidence/methodology.md)

</div>

---

## 直接看效果

<table>
<tr><th>修改前：AI 味 + 防御性</th><th>修改后：自然 EC 学术表达</th></tr>
<tr><td>

> With the rapid development of evolutionary computation, large-scale multiobjective optimization has become a hot topic. It is worth noting that our proposed method may potentially significantly outperform state-of-the-art algorithms, although we do not claim that it is universally optimal for all problems. The main contributions are as follows: 1) We propose a novel framework. 2) We design an efficient operator. 3) We conduct extensive experiments.

</td><td>

> Large-scale multiobjective optimization remains challenging for evolutionary algorithms as the number of decision variables increases. This paper addresses this setting and makes three contributions: a framework for large-scale multiobjective optimization, an efficient search operator, and an extensive experimental evaluation. On the tested problems, the proposed algorithm outperforms the state-of-the-art algorithms included in the comparison.

</td></tr>
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

```bash
npx skills add Wenhua-Li/evo-writing-skill
```

或：

```bash
curl -fsSL https://raw.githubusercontent.com/Wenhua-Li/evo-writing-skill/main/install.sh | bash
```

Windows PowerShell：

```powershell
iwr https://raw.githubusercontent.com/Wenhua-Li/evo-writing-skill/main/install.ps1 | iex
```

然后调用：

```text
Use evo-write. Rewrite this introduction to remove AI tells and defensive writing.
Return only the revised English.
```

更多选项见 [`docs/install.html`](docs/install.html)。

## 核心能力

- 去除 EC 论文中的宏大开场、空泛重要性、机械贡献列表和模板化结果段落；
- 用 positive scope 替代 `We do not claim...` 等防御性表达；
- 保留引用、数值、负结果、定理条件、benchmark、基线、指标、预算和统计检验；
- 在 Audit 模式下检查 `significant`、`optimal`、`robust`、`scalable`、`efficient` 等主张的证据边界；
- 支持作者英文样本的 voice matching。

## 证据边界

公开包不包含原始论文，只包含原创规则、模板、脚本和聚合统计。

- 主语料：1997–2023 年 TEVC，共 1,517 篇；
- 语言统计：1,358 篇质量可控论文；
- 定性复核：150 篇分层样本；
- 排除：2024 年及以后、年代不明的 early access；
- 语料用于领域校准，不用于生成固定模板。

详见 [`skill/references/evidence/methodology.md`](skill/references/evidence/methodology.md) 和 [`skill/references/evidence/limitations.md`](skill/references/evidence/limitations.md)。

## 限制

- EvoWrite 提升自然度与主张校准，不承诺论文录用；
- 目标不是欺骗 AI 检测器，而是让人类审稿读者觉得自然；
- 语料证据来自 TEVC，不代表 IEEE 或 TEVC 官方立场；
- 原始论文不包含在公开仓库中；
- 作者声音匹配效果取决于样本质量。

## 引用

```bibtex
@software{li_evowrite_2026,
  author  = {Li, Wenhua},
  title   = {EvoWrite: Natural Evolutionary Computation Paper Writing},
  year    = {2026},
  version = {0.4.0},
  url     = {https://github.com/Wenhua-Li/evo-writing-skill},
  license = {MIT and CC-BY-4.0}
}
```

## 许可证

- 脚本：[MIT License](LICENSE)
- Skill 文档、规则、模板、示例和聚合数据：[CC BY 4.0](LICENSE-CC-BY-4.0)
