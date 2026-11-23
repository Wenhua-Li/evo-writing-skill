<div align="center">

<img src="docs/assets/banner.svg" alt="EvoWrite banner" width="100%">

# EvoWrite

**把 Evolutionary Computation 论文改成自然、平实的英文，证据原样保留。**

规则来自 **1,517 篇 TEVC 论文（1997–2023）** 的统计和 150 篇分层抽样论文的逐篇复核。EvoWrite 重建 AI 腔段落，去掉工程隐喻和重复出现的 LLM 套话，研究主张、引用、标准 EC 术语和作者自己的写法保持不变。

[English](README.md) · [快速开始](docs/quickstart.md) · [案例](docs/cases.html) · [文档](docs/)

[![Release](https://img.shields.io/badge/release-v0.6.0-38bdf8)](https://github.com/Wenhua-Li/evo-writing-skill/releases)
[![Agent Skills](https://img.shields.io/badge/agent--skills-compatible-14b8a6)](https://agentskills.io)
[![License](https://img.shields.io/badge/license-MIT%20%2B%20CC--BY--4.0-blue)](LICENSE)
[![Corpus](https://img.shields.io/badge/TEVC%20corpus-1997--2023-94a3b8)](skill/references/evidence/methodology.md)

</div>

---

## 直接看效果

<table>
<tr><th>修改前:AI 腔 + 防御性写法</th><th>修改后:平实的 EC 学术表达</th></tr>
<tr><td>

> With the rapid development of evolutionary computation, large-scale multiobjective optimization has become a hot topic. It is worth noting that our proposed method may potentially significantly outperform state-of-the-art algorithms, although we do not claim that it is universally optimal for all problems. The main contributions are as follows: 1) We propose a novel framework. 2) We design an efficient operator. 3) We conduct extensive experiments.

</td><td>

> Large-scale multiobjective optimization becomes harder as the number of decision variables increases. This paper presents a search framework and a variation operator for this setting. On the tested problems, the proposed algorithm outperforms the algorithms included in the comparison.

</td></tr>
</table>

不编造结果,也不再写防御性的免责声明。

## 为什么不用普通 humanizer?

普通 humanizer 可以把句子改顺,但抽象、夸大、工程化的措辞常常原样留下。EvoWrite 先按研究含义重建段落,再对照固定规则逐项检查:

- 轻度编辑不够时,根据研究含义重写整段;
- 拦截软件、管理、营销隐喻;
- 违禁词和格式化对比必须返工,不能带着警告交付;
- 分清 function evaluations、墙钟时间、模型训练成本和实现复杂度;
- 分清 convergence、diversity、feasibility、objective value 和 fitness;
- 熟悉昂贵、约束、动态、大规模、多峰、多目标这些优化环境的写法;
- 必要的方法学限制只写一次,放在读者需要的章节;
- 作者声音匹配只学节奏和习惯,不复制门禁禁止的措辞。

## 快速开始

```bash
npx skills add Wenhua-Li/evo-writing-skill
```

或:

```bash
curl -fsSL https://raw.githubusercontent.com/Wenhua-Li/evo-writing-skill/main/install.sh | bash
```

Windows PowerShell:

```powershell
iwr https://raw.githubusercontent.com/Wenhua-Li/evo-writing-skill/main/install.ps1 | iex
```

然后调用:

```text
Use evo-write. Rewrite this introduction to remove AI tells and defensive writing.
Return only the revised English.
```

更多选项见 [`docs/install.html`](docs/install.html)。

## 具体做什么

### 重建,不是浅层润色

草稿充满 AI 腔时,EvoWrite 先记录每段实际说了什么,再重新写一遍。在原句骨架上换形容词和连接词不算改写。

### 强制平实的 EC 英文

禁用词表覆盖 `axes`、`synthetic`、`provenance`、`admission`、`extreme`、`declared`、`protocol`、`tie`、`saturated`、`trajectories`、`certified`、`menus`、`audit`、`inferred`、`rather than`、`trial`、`rival`、`refinement` 及常见词形变化,并拦截同类 LLM 措辞。

命中就返工,不存在带警告交付。窄技术例外保护标准用法,例如 DE 的 `trial vector`、机器人实际运动轨迹、明确的数据类别 `synthetic data`、坐标轴和已有技术语境中的 `extreme solutions`。完整规则见 [`skill/data/prose-gate.json`](skill/data/prose-gate.json)。

### 句式与重复检查

门禁同时拦截格式化 `rather than`、`instead of`、`not X but Y`、空泛的研究兴趣开场、`do not claim` 免责声明、没有证据说明的鲁棒性与规模化表述、重复的句首连接词、连续三句相同两词开头和重复的六词序列。扫描通过不代表文字自然,仍需人工通读。

### 去掉防御性写法

- `We do not claim...` → 直接写出评估范围;
- `may potentially suggest` → `suggests`、`indicates` 或有边界的表述;
- 反复出现的限制 → 在正确章节写一次具体限制。

### 保留研究含义

不编造研究内容,也不悄悄加强主张。引用、DOI、数值结果、不确定性、负结果、定理条件、benchmark、基线、指标、预算、统计检验、算法机制、假设和应用约束都原样保留。

### 应要求检查主张强度

Audit 模式标出证据不支持的主张:没有检验的 `statistically significant`、没有保证的 `optimal`、没有扰动模型的 `robust`、没有维度与预算范围的 `scalable`、没有成本口径的 `efficient`。

## 检查器

环境允许运行 Python 时,可以把完整候选文本交给:

```bash
python tools/scripts/check_prose.py -
```

脚本只依赖 Python 标准库。无法执行时,按同一份 JSON 手工逐项检查。

## 证据边界

公开包只有聚合统计和原创规则,不包含原始论文。

- 主语料:1997–2023 年 TEVC,共 1,517 篇;
- 语言统计:1,358 篇质量可控论文;
- 定性复核:150 篇跨时期、类型和研究设置的抽样论文;
- 排除:2024 年及以后、年代不明的 early access;
- 用途:让规则扎根于真实 EC 写作;语料频率再高也不能推翻禁用词表。

详见 [`skill/references/evidence/methodology.md`](skill/references/evidence/methodology.md) 和 [`skill/references/evidence/limitations.md`](skill/references/evidence/limitations.md)。

## 限制

- EvoWrite 改善可读性和主张校准,不承诺论文录用;
- 目标是让审稿人读着自然,不是对付 AI 检测器;
- 语料证据来自 TEVC,与 IEEE 或 TEVC 的官方立场无关;
- 仓库不含原始论文,只有聚合统计和原创规则;
- 作者声音匹配的效果取决于样本质量。

## 引用

```bibtex
@software{li_evowrite_2026,
  author  = {Li, Wenhua},
  title   = {EvoWrite: Natural Evolutionary Computation Paper Writing},
  year    = {2026},
  version = {0.6.0},
  url     = {https://github.com/Wenhua-Li/evo-writing-skill},
  license = {MIT and CC-BY-4.0}
}
```

## 许可证

- 脚本:[MIT License](LICENSE)
- Skill 文档、规则、模板、示例和聚合数据:[CC BY 4.0](LICENSE-CC-BY-4.0)
