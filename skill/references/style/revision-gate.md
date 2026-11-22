# Revision Gate：交付前的强制失败条件

语言门禁不是评分建议。任何非例外命中都意味着候选文本不能交付。检查的目的，是阻止模型把熟悉但生硬的工程表达和模板句再次带入论文。

## 1. 第一层：词汇与短语硬检查

对最终候选文本运行：

```bash
python tools/scripts/check_prose.py -
```

通过标准输入提供完整文本，不要只检查抽出的句子。脚本从 `skill/data/prose-gate.json` 读取规则，命中时返回非零状态。

无执行环境时，读取同一 JSON 并逐项人工扫描。两种情况下都必须：

- 检查大小写、复数和常见词形变化；
- 检查原文已有的表达，不因“保留原文”而豁免；
- 检查 Voice Match 输出，不因作者样本而豁免；
- 只接受 `plain-ec-english.md` 定义的窄技术例外；
- 不输出带有剩余命中的文本。

## 2. 第二层：模板与重复硬检查

以下情况必须返工：

- `rather than` 和作为其绕过形式的 `instead of`；
- 用 `stated procedure`、`prespecified procedure`、`fixed rule` 等近义表达保留原来的空泛对比；这类对比应整体删除；
- 格式化的 `not X but Y` 和 `not only ... but also ...`；
- `It is worth noting`、`plays a crucial role`、`This highlights the importance`、`serves as` 等空泛模板；
- `one of the most active research areas`、`has attracted growing interest` 等空泛研究兴趣开场；
- `may significantly` 等叠加限定、`do not claim` 防御性免责声明和 `wins everywhere` 等口语化全称比较；
- 未说明扰动与证据的 `robust`、未说明规模维度与证据的 `scalable`，以及用 `stable as the problem size grows` 等说法保留无依据规模化结论；
- 同一个 `Moreover`、`Furthermore`、`In addition` 或 `Besides` 在候选文本中多次用于句首；
- 相邻句或相邻段机械重复连接词；
- 连续三句以相同的两个词开头；
- 同一个非技术性六词序列重复出现；
- 每段都按相同顺序展开、机械凑三点贡献或 RQ、每个结果后都解释“重要性”。

必要的技术术语可以重复，重复术语优于不断更换名称。门禁针对的是无信息句式重复，不是术语一致性。

## 3. 第三层：未入表的同类问题

自动词表不能穷尽 AI 腔。即使脚本返回 0，也必须继续检查：

- 是否仍有软件、管理、营销或审计隐喻；
- 是否仍有只增加“高级感”而没有技术信息的抽象词；
- 是否每句都同样平滑、对称和完整；
- 是否靠连接词维持本应由事实顺序承担的衔接；
- 是否把显而易见的观察再总结一遍；
- 是否出现读者无法直接理解的修饰语或名词堆叠；
- 是否把无依据的 robust/scalable/significant 改成 stable、steady、substantially 或“随规模增长仍稳定”等同义说法；
- 是否从方法名称虚构了筛选、训练集、模型更新、归档或预算分配步骤；
- 是否在没有实验材料时写出 tested problems、compared algorithms 或性能结果；
- 是否用两个连续句子重复同一信息，以制造已经充分改写的假象；
- 是否改变 `only/within/at least`、`fewer/a few`、单复数或“从集合中选择一个/应用整个集合”等数量与范围含义；
- 是否把 statistical test 泛化为 experimental setup，使 p 值或显著性失去检验口径；
- 稀疏 Draft 是否超过 80 词，或擅自生成完整引言和计划实验。

任何一项存在，都不能把“脚本通过”当成交付理由。

## 4. 命中后的返工方式

1. 回到该句或该段的语义清单。
2. 删除隐喻和模板所占据的句法位置。
3. 用具体对象与动作重新写整个句子或段落。
4. 不补充原材料没有提供的机制或证据。
5. 重新扫描完整候选文本，而不是只检查改过的词。

禁止把 `rather than` 统一替换为另一个高频对比连接词，禁止把违禁词统一替换为更生僻的近义词。

## 5. 最后一层：事实与声音回查

语言通过后，逐项核对：

- 数字、百分比、引用、DOI、公式和符号；
- 算法、基线、benchmark、指标和实验条件；
- FEs、generations、runtime、model cost 等成本口径；
- convergence、diversity、feasibility、PS/PF 等领域含义；
- 因果、统计显著性、最优性和结论范围；
- 负结果、例外、必要限制和不确定表述。

文本应读起来像研究者为了清楚表达而修改过，而不是像完成了某个风格转换任务。

## 6. 输出纪律

正常 Rewrite、Draft 和 Voice Match 只输出通过门禁的英文正文。不要附加检查表、通过说明、词汇统计或“如果你愿意我还可以……”等助手话术。

`Verified with`、`exit code`、工具命令和自检结论同样不得出现在论文正文或 Audit 的 Revised text 中。门禁需要删除效率与代数/迭代次数之间的无依据等价关系，也需要删除带 `design goal`、`maintaining consistent performance` 等外壳的规模化同义主张。

只有用户明确要求 Audit 时才输出诊断；诊断中的 Revised text 仍须重新通过全部门禁。
