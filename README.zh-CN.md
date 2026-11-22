<div align="center">

<img src="docs/assets/banner.svg" alt="EvoWrite banner" width="100%">

# EvoWrite

**面向 Evolutionary Computation 论文的普通、自然、证据感知写作 Skill。**

基于 **1,517 篇 TEVC 论文（1997–2023）** 和 150 篇分层样本复核构建。EvoWrite 重建 AI 腔段落，去除工程隐喻和模板表达，同时保留研究主张、实验证据、标准 EC 术语和作者声音。

[English](README.md) · [快速开始](docs/quickstart.md) · [案例](docs/cases.html) · [文档](docs/)

[![Release](https://img.shields.io/badge/release-v0.5.0-38bdf8)](https://github.com/Wenhua-Li/evo-writing-skill/releases)
[![Agent Skills](https://img.shields.io/badge/agent--skills-compatible-14b8a6)](https://agentskills.io)
[![License](https://img.shields.io/badge/license-MIT%20%2B%20CC--BY--4.0-blue)](LICENSE)
[![Corpus](https://img.shields.io/badge/TEVC%20corpus-1997--2023-94a3b8)](skill/references/evidence/methodology.md)

</div>

---

## 直接看效果

<table>
<tr><th>修改前：AI 味 + 防御性</th><th>修改后：清楚的 EC 学术表达</th></tr>
<tr><td>

> With the rapid development of evolutionary computation, large-scale multiobjective optimization has become a hot topic. It is worth noting that our proposed method may potentially significantly outperform state-of-the-art algorithms, although we do not claim that it is universally optimal for all problems. The main contributions are as follows: 1) We propose a novel framework. 2) We design an efficient operator. 3) We conduct extensive experiments.

</td><td>

> Large-scale multiobjective optimization becomes harder as the number of decision variables increases. This paper presents a search framework and a variation operator for this setting. On the tested problems, the proposed algorithm outperforms the algorithms included in the comparison.

</td></tr>
</table>

不编造结果，不写防御性免责声明，也不保留通用 AI 套话。

## 为什么不是普通 humanizer？

普通 humanizer 可能只把句子改顺，却保留抽象、夸大或工程化的措辞。EvoWrite 同时执行段落重建、EC 证据检查和强制语言门禁：

- 原句 AI 腔明显时，根据研究含义重新组织句子，不做表面同义替换；
- 拦截软件、管理、营销和行政隐喻；
- 违禁词和格式化对比必须重写，不能作为警告随正文一起交付；
- 区分 function evaluations、墙钟时间、模型训练成本和实现复杂度；
- 区分 convergence、diversity、feasibility、objective value 和 fitness；
- 理解昂贵、约束、动态、大规模、多峰、多目标等优化环境；
- 保留必要的方法学边界，但只写一次并放在正确章节；
- 作者声音匹配只学习节奏与习惯，不能复制样本中的违禁措辞。

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

### 脱稿重建，而非浅层润色

对工程隐喻、抽象名词和 AI 模板明显的段落，先记录研究含义，再重新安排主语、句子和信息顺序。原本已经自然准确的文字不做为改而改。

### 强制普通 EC 英文

硬门禁覆盖 `axes`、`synthetic`、`provenance`、`admission`、`extreme`、`declared`、`protocol`、`tie`、`saturated`、`trajectories`、`certified`、`menus`、`audit`、`inferred`、`rather than`、`trial`、`rival`、`refinement` 及常见变体，并扩展拦截同类 LLM 和工程化措辞。

任何非例外命中都必须重新改写。只有不可替代的标准技术含义可以窄例外，例如 DE 的 `trial vector`、实际机器人运动轨迹、明确的数据类别 `synthetic data`、坐标轴和已有技术语境中的 `extreme solutions`。完整规则见 [`skill/data/prose-gate.json`](skill/data/prose-gate.json)。

### 句式与重复检查

门禁拦截 `rather than`、`instead of`、格式化 `not X but Y`、空泛研究兴趣开场、`do not claim` 免责声明、无依据的鲁棒性与规模化表述、重复句首连接词、连续三句相同两词开头和重复的非技术六词序列。自动检查通过并不等于自然度合格，仍需人工阅读判断。

### 证据与术语保护

保留引用、数值、负结果、定理条件、benchmark、基线、指标、预算和统计检验。区分真实评价次数、代数、运行时间和模型成本，不把语言简化变成主张加强。

### 防御性写作与主张检查

用正向范围替代 `We do not claim...` 等防御性表达。Audit 模式检查 `significant`、`optimal`、`robust`、`scalable`、`efficient` 等主张的证据边界。

## 强制检查器

有执行环境时，可将完整候选英文通过标准输入交给：

```bash
python tools/scripts/check_prose.py -
```

脚本只依赖 Python 标准库。没有执行环境时，Skill 按同一份 JSON 逐项检查，不能跳过门禁。

## 证据边界

公开包不包含原始论文，只包含原创规则、模板、脚本和聚合统计。

- 主语料：1997–2023 年 TEVC，共 1,517 篇；
- 语言统计：1,358 篇质量可控论文；
- 定性复核：150 篇分层样本；
- 排除：2024 年及以后、年代不明的 early access；
- 语料用于领域校准和确认常见 EC 表达，不用于生成固定模板，也不能推翻禁用规则。

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
  version = {0.5.0},
  url     = {https://github.com/Wenhua-Li/evo-writing-skill},
  license = {MIT and CC-BY-4.0}
}
```

## 许可证

- 脚本：[MIT License](LICENSE)
- Skill 文档、规则、模板、示例和聚合数据：[CC BY 4.0](LICENSE-CC-BY-4.0)
