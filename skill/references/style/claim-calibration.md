# Claim Calibration

本文件用于 Audit 模式和后台证据检查。目标不是把文本写得越来越谨慎，而是让主张强度与证据一致。

## 1. 先判断主张类型

- **事实**：定义、设置、已有结果、实验观察。
- **解释**：对结果原因的说明。
- **推测**：合理但尚未验证的机制或推广。
- **理论**：由假设和证明支持。
- **应用价值**：需要领域指标和实际约束支撑。

不同类型不能互相冒充。

## 2. 强主张所需证据

| 表达 | 需要 |
|---|---|
| statistically significant | 明确的检验、样本/运行数、显著性水平，最好有效应量或多重比较说明 |
| optimal | 已知最优值、形式定义和证明/精确方法依据 |
| robust | 明确的扰动类型、范围和评价指标 |
| scalable | 明确的规模维度、范围和复杂度/预算证据 |
| efficient | 明确成本口径：FEs、runtime、模型训练、内存或实现复杂度 |
| state-of-the-art | 具体、相关且近期/强基线及公平协议 |
| novel | 与直接前驱的明确差异 |
| proves | 形式证明，不用于纯实验结果 |

## 3. 证据不足时的处理

按顺序选择：

1. 缩小范围；
2. 改成可支撑的观察；
3. 删除该句；
4. 在 Audit 中说明缺失证据。

不要通过叠加 `may`、`potentially`、`to some extent` 保留原强主张。

也不得通过改换说法保留同一强主张：

- 无规模化证据时，不能将 `scalable` 改为 `stable as the problem size grows`；
- 无鲁棒性证据时，不能将 `robust` 改为 `stable`、`reliable` 或 `consistent`；
- 无统计检验时，不能将 `significantly` 改为 `substantially`、`markedly` 或 `clearly better`；
- 无比较证据时，不能写 `on the tested problems`、`the compared algorithms` 或任何实际性能优劣；
- 不得把无依据的 `outperforms` 改成 `aims to outperform` 或类似研究目标，用目的句式保留同一宣传主张；
- 无验证证据时，不得把 `certify/certified` 改成 `verify/verified/verification`；若实际行为只是比较搜索结果，写 `compare`。

### Audit 中的 Revised text

Audit 可以指出缺失证据，但修订文本同样受证据约束。用户没有提供实验时，不得为了给出完整句子而虚构 tested problems、compared algorithms、结果或实验范围。无法安全保留性能主张时，改成研究目的或设计对象；连研究目的也不清楚时，明确写无法在不补充证据的情况下修订该主张。

对只有一个过强句子的 Audit，安全回退可以只写 `The proposed algorithm is designed for [PROBLEM].`。不要自行补充 small/limited budget、Pareto front approximation、评价成本构成或其他设计目标。

强主张的释义、同义词和隐含版本与原始措辞接受同样的证据检查。

## 4. 因果边界

- 消融结果支持机制归因，但仍要看实验设计是否排除了替代解释。
- 相关趋势不能直接写成因果。
- 理论保证只适用于其模型和假设。
- 单个应用案例不能直接推广到整个行业。

## 5. 最终检查

- 每个强形容词是否有证据；
- 每个 `better` 是否有比较对象和指标；
- 每个 `efficient` 是否有成本口径；
- 每个结论是否能回到摘要、实验或理论；
- 必要的范围限定是否写一次并放在正确位置。
