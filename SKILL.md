---
name: evo-write
description: >-
  Rewrites Evolutionary Computation papers so they read like a careful researcher wrote them. Use EvoWrite for TEVC/EC/EA/EMO abstracts, introductions, related work, methods, experiments, and conclusions, for full-section rewrites, drafting from notes, matching an author's voice, and pre-submission checks. AI-sounding paragraphs are rebuilt from the research meaning: software metaphors, inflated wording, formulaic contrasts, and repeated LLM phrasing are removed, and every draft must pass a fixed word-and-structure gate before delivery. Facts, numbers, citations, and standard EC terminology are preserved; missing evidence is never invented, including citations, experiments, results, statistical tests, theorems, and conclusions. Output is English paper text; a diagnostic report is written only when asked.
metadata:
  version: "0.6.0"
---

# EvoWrite

把 EC 论文写成研究者清楚、直接、容易理解的英文。专业感来自准确的概念、具体的机制和可信的证据，不来自生僻词、软件隐喻、抽象名词或过分工整的句式。

首要产物是**可直接使用的英文论文文本**。检查在后台完成；只有用户明确要求审查、解释或风险评估时才输出诊断报告。

## 0. 不可协商的原则

1. **保留研究含义。** 不新增、不删除、不弱化有依据的事实、数值、引用、机制、比较、定理、负结果或结论。
2. **不编造证据。** 没有提供的内容不能写成事实。不得为了把句子写顺而补充实验设置、数值、因果关系或限制。
3. **技术准确优先。** 标准 EC 术语、指标、空间、成本口径和符号不能为了“通俗”而改错。
4. **语言门禁不可豁免。** 原文已有、作者声音匹配、追求句式变化或自认为更高级，都不是保留违禁表达的理由。
5. **命中必须返工。** 不得把命中项解释为“可以接受”后交付，也不得输出带剩余警告的文本。
6. **不以欺骗 AI 检测器为目标。** 验收标准是研究者读起来清楚、自然、没有工程腔和模板腔。

优先级为：事实与证据 > 技术准确 > 语言门禁 > 作者声音与其他风格偏好。技术例外只按 `skill/references/style/plain-ec-english.md` 的窄规则处理。

## 1. 任务模式

### Rewrite / Humanize（默认）

对已有英文或中文草稿进行段落级重建。默认只返回修改后的英文文本。

### Draft

从研究笔记或实验信息起草。先静默建立 claim–evidence 对应，再写英文；证据不足的主张不写死。

**方法名称不等于内部机制。** 只给出“GP-assisted DE”或类似名称时，不得自行补写候选筛选、训练集构造、模型更新、归档、预算分配或选择步骤。不得添加分钟数、评价次数、benchmark、基线或实验结果作为“示例”。成熟领域背景只能用于解释普遍概念，不能用来虚构本文设计。

**稀疏材料启用短草稿模式。** 如果输入只有问题、方法名称和目标，没有机制与证据，禁止生成完整多段 Introduction。论文正文最多 80 个英文词，只写“本文研究什么、用于什么问题、目标是什么”；随后最多列三项缺失信息，优先询问机制。不得写文献路线评价、具体算法流程、planned experimental study、固定预算、指标或结果。缺少这些信息时，短而完整的安全文本优于看似充实但虚构的引言。

### Voice Match

从作者样本提取句长、段落长度、人称、连接方式和术语习惯。样本只影响节奏与声音，**不能重新引入门禁禁止的词汇和句式**。不得从样本或自身推测为目标段落添加时间顺序、分组数量、单个/多个算子或内部机制；目标段落没有提供的事实一律不得出现。

### Section Pass

按章节任务精修：Abstract 直接具体；Introduction 快速进入问题与设计动机；Method 清楚可复现；Experiments/Results 先给条件和观察再解释；Conclusion 收束发现与范围。

### Audit

只有用户明确要求审查、诊断、风险报告或投稿前检查时才输出报告。报告可以讨论命中项，但其中的 Revised text 仍须通过全部门禁与证据检查。

用户没有提供实验、基线或结果时，Revised text 不得写 `on the tested problems`、`the compared algorithms`、`outperformed` 或其他暗示已有比较证据的句子。无法安全保留性能主张时，只写研究目的或设计对象；连这些也不清楚时，说明无法在不补充证据的情况下修订，不得编造一个看似完整的版本。

对只有一个过强句子的 Audit，安全回退可以只写 `The proposed algorithm is designed for [PROBLEM].`。不得自行添加 small/limited budget、approximate the Pareto front、评价成本构成或算法目标；这些信息必须来自原材料。

## 2. 强制读取与补充路由

**所有写作、起草、改写和声音匹配任务都必须读取：**

- `skill/references/style/plain-ec-english.md`
- `skill/references/style/revision-gate.md`
- `skill/data/prose-gate.json`

“最少文件”只适用于以下补充资料，不能用来跳过上述三份门禁文件：

- 证据与术语：`skill/references/style/claim-calibration.md`、`skill/references/style/terminology.md`
- 从零起草：`skill/references/workflow.md`、相应 `article-types/`、`sections/`、`domains/`
- 多目标或问题环境：`skill/references/domains/multiobjective.md`、`skill/references/domains/problem-environments.md`
- 方法谱系：`skill/references/domains/method-families.md`
- 投稿前检查：`skill/templates/submission-checklist.md`
- 语料证据边界：`skill/references/evidence/`

## 3. 强制重写管线

### 第一步：建立语义清单

静默记录问题、方法、输入输出、条件、数字、引用、公式、基线、指标、成本口径、因果强度和结论范围。后续只能重组这些已有信息，不能借润色补充研究内容。

### 第二步：确定每段任务

判断该段是在定义问题、解释困难、比较方法、描述机制、报告观察、解释结果还是限定范围。一段不要同时承担过多任务。

### 第三步：脱稿重建

放下原句的表面形式，根据语义清单重新写段落。允许拆分、合并、改变主语、调整信息顺序和删除无信息句子。

如果原文含有工程隐喻、密集抽象名词、重复模板或明显的 AI 腔，禁止沿用原句骨架做近义词替换。原有文字已经自然准确时，不做为改而改。

### 第四步：执行 Plain-EC 重写

把抽象评价改成具体对象与动作，把软件/管理/营销隐喻改成实际算法操作，把格式化对比改成直接陈述。优先使用普通学术动词，不追求“高级”替换词。

### 第五步：扫描候选成稿

对**准备交付的完整最终文本**检查：

- `prose-gate.json` 中的全部词汇、变体和短语；
- 连续重复连接词、相同句首、相同段首和非技术性重复 n-gram；
- 未入表但同属工程隐喻、宣传腔或无信息抽象表达的措辞；
- 机械三点贡献、强制 RQ、均匀段落和每句过度平滑完整等结构问题。

有执行环境时，从 Skill 根目录将最终候选文本通过标准输入交给：

```bash
python tools/scripts/check_prose.py -
```

没有执行环境时，必须按同一份 JSON 和规范逐项自检。不得声称未实际运行的检查已经通过。

### 第六步：命中后重建并重新扫描

任何非例外命中都判定为失败。回到整个句子或段落重建，不做孤立的同义词替换，然后重新扫描完整文本，直到没有命中。

### 第七步：事实回查

逐项核对语义清单。特别检查数字、引用、算法名称、公式、比较条件、指标方向、统计含义、负结果和适用范围。语言变简单不能以提高主张强度为代价。

强主张不能用同义或隐含说法绕过：无规模化证据时删除 `stable as the problem size grows` 等表述；无鲁棒性证据时不得改成 `stable/reliable`；无统计检验时不得改成 `substantially/markedly`；无比较证据时不得写 `on the tested problems` 或 `outperformed the compared algorithms`。检查的是实际主张，不只是关键词。

数量、范围和集合操作也必须保持不变：不得混淆 `only/within/at least`、`fewer/a few`，不得把单数操作写成应用整个集合，也不得改变选择范围。`only 20 generations` 中的宣传性强调应改为中性的 `exactly 20 generations`，不能改成上界 `within 20 generations`。p 值和显著性必须保留明确的 statistical test，不能泛化成 experimental setup。

## 4. 技术例外与保留文本

例外只保护不可替代的技术含义，例如 DE 的 `trial vector`、机器人实际运动轨迹、明确的 `synthetic data`、图形的实际坐标轴和已有文献中的 `extreme solutions`。

不得主动引入例外词做风格变化。原文没有该技术含义时不能使用；存在普通且同样准确的表达时优先普通表达。引用标题、正式算法名称、公式和直接引语保持原样。

## 5. 缺失信息

- 缺失不影响当前句子：不写备注，直接完成。
- 缺失影响局部主张：删除或改为材料能够支持的一般表述。
- 缺失影响整段成立：跳过该段，文后最多列三项关键缺失。
- 只有用户明确要求 skeleton/outline 时才使用 `[MISSING]` 占位符。

## 6. 输出约定

### 默认改写、起草与 Voice Match

```text
[只输出已经通过门禁的英文论文文本]
```

起草因信息不足无法完成时，可在文后最多增加三项关键缺失信息。除此之外不输出词表扫描结果、修改总结或自检说明。

### Audit

```markdown
## Main issues
## Evidence and scope risks
## Revised text
## Remaining decisions for the author
```

只有 Revised text 属于论文正文；报告其他部分可以引用被检查的问题词。

## 7. 交付条件

只有同时满足以下条件才可以交付：

- 没有未获窄技术例外的门禁命中；
- `rather than` 和格式化 `not X but Y` 没有出现；
- 不是对 AI 腔原文的浅层替换；
- 没有连续模板句和不必要的重复连接词；
- 事实、证据、术语与比较范围保持不变；
- 文本对 EC 读者直接、清楚、可理解。
