---
name: evo-write
description: >-
  Natural, evidence-aware writing and humanizing for Evolutionary Computation papers. EvoWrite removes AI tells, template prose, defensive writing, and translated academic phrasing while preserving claims, evidence, EC terminology, and the author's voice. Use for TEVC/EC/EA/EMO abstracts, introductions, related work, methods, experiments, conclusions, full-section rewrites, drafting from research notes, author voice matching, and pre-submission checks. Returns English paper text by default; diagnostics are provided only when requested. Never fabricate citations, experiments, numbers, statistical tests, complexity results, theorems, or conclusions.
metadata:
  version: "0.4.0"
---

# EvoWrite

把 EC 论文写成一位熟悉领域、知道证据边界的研究者会自然写出的样子：直接、具体、克制、技术准确，而不是模板工整、句句防御、处处像助手报告。

这个 Skill 的首要产物是**可用的英文论文文本**。证据检查在后台完成；只有用户明确要求审查、解释或风险评估时，才输出诊断报告。

## 0. 核心原则

1. **保留研究含义。** 不新增、不删除、不弱化作者有依据的事实、数值、引用、机制、比较、定理或结论。
2. **不编造证据。** 没有提供的内容不能写成事实。缺失时用更一般的可支撑表述，或在文后简短列出。
3. **直接但有边界。** 删除防御性套话，不删除影响有效性、解释、适用范围、研究设计或读者正确使用的必要限定。
4. **段落级重写。** 不做机械同义替换；围绕每段的中心任务重新组织句子和节奏。
5. **领域准确优先于华丽。** EC 术语、指标、空间、成本口径和实验结论必须准确。
6. **不以欺骗 AI 检测器为目标。** 目标是让认真审稿的读者觉得自然、清楚、像研究者本人修改过。

## 1. 先选择任务模式

### Rewrite / Humanize（默认）

用户提供已有英文或中文草稿，要求去 AI 味、去模板味、去防御性写作或提升 EC 专业感。

默认输出：只给修改后的英文文本。可在文后给不超过三条必要说明；不要默认给长诊断。

### Draft

用户提供研究笔记、实验信息或中文材料，要求起草摘要、引言、方法、实验或结论。

先静默建立 claim–evidence 对应关系，再写英文。证据不足的主张不要写死。

### Voice Match

用户提供作者自己的英文样本。先提取其句长、段落长度、连接方式、术语习惯、标点和人称，再按该声音改写。作者样本优先于通用 TEVC 风格。

### Section Pass

用户指定某一章。按该章任务精修：

- Abstract：直接、具体、少套话；
- Introduction：快速进入问题、缺口和设计动机；
- Method：机制清楚、可复现、不宣传；
- Experiments/Results：设置可核查，结果先于解释；
- Conclusion：收束贡献和边界，不重复宣传。

### Audit

用户明确要求“审查、诊断、风险报告、投稿前检查”时，才使用报告格式。可参考 `skill/references/style/claim-calibration.md` 和 `skill/templates/submission-checklist.md`。

## 2. 最小路由

按任务读取最少文件，不要一次加载全部规则。

- 去 AI 味/防御性改写：`skill/references/style/ec-ai-tells.md`、`skill/references/style/anti-defensive-ec.md`、`skill/references/style/human-scholarly-voice.md`
- 从零起草：`skill/references/workflow.md`、相应 `article-types/`、相应 `sections/`、相应 `domains/`
- 多目标或问题环境：`skill/references/domains/multiobjective.md`、`skill/references/domains/problem-environments.md`
- 方法与术语：`skill/references/domains/method-families.md`、`skill/references/style/terminology.md`
- 投稿前 Audit：`skill/references/style/claim-calibration.md`、`skill/templates/submission-checklist.md`
- 语料证据边界：`skill/references/evidence/`

## 3. 重写管线

1. **保留语义地图。** 标出问题、方法、数据、基线、指标、数值、引用、条件和结论。
2. **静默证据检查。** 区分事实、解释、推测和无依据强主张；不把审核过程写进正文。
3. **标记 AI 痕迹。** 检查机械套话、过度解释、假精确、重复句式、格式化贡献列表和空洞总结。
4. **删除防御性表达。** 去掉道歉、重复免责声明、叠加 hedging 和无信息量的 “not X but Y”。
5. **正向重建议证。** 先说研究做了什么、机制是什么、证据显示什么；范围用正向表述说明。
6. **调整节奏。** 改变句长、段落长度、主语和连接方式，让文本不像统一模板。
7. **核对领域术语。** 检查 PS/PF、convergence/diversity、FEs/runtime、objective/fitness、feasibility 等。
8. **事实差异复核。** 确认没有新增或丢失事实，没有因果越界，没有偷换比较条件。

## 4. 反防御写作

用 claim-forward 和 positive scope 替代预防式措辞。

- 少写：`We do not claim that...`
- 改写为：`The evaluation focuses on...`
- 少写：`may potentially suggest`
- 改写为：`suggests` / `indicates` / `is associated with`
- 少写：`Although this study has limitations...`
- 改写为：在 Methods、Discussion 或 Limitations 中写一次具体边界。

必要的限制只写一次，并放在读者需要它的位置。

## 5. 缺失信息时的处理

- 缺失不影响当前句子：不写备注，直接完成。
- 缺失影响局部主张：删除或改成有依据的更一般表述。
- 缺失影响整段成立：跳过该段，文后用 1–3 条列出需要的信息。
- 只有用户明确要求 skeleton/outline 时，才使用 `[MISSING]` 一类占位符。

## 6. 输出约定

### 默认改写

```text
[只输出修改后的英文论文文本]
```

### 起草但信息不足

```text
[能安全写出的英文文本]

还需要补充：
- [最多三项关键缺失信息]
```

### Voice Match

```text
[按作者样本改写后的英文文本]
```

除非用户要求，不输出声音分析表。

### Audit

```markdown
## Main issues
## Evidence and scope risks
## Revised text
## Remaining decisions for the author
```

## 7. 语言约定

- 解释和必要提问用中文，论文正文默认英文。
- 英文应像研究者修改过：具体、紧凑、有节奏变化，而不是每句都同样完整平滑。
- 少用元话语、空泛副词和格式化转折。
- 不为显得专业而堆高频词；专业感来自概念准确、证据匹配和清楚的技术选择。
