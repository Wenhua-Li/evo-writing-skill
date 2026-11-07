# Experiments、Results 与 Discussion

实验章节的目标不是展示大量表格，而是让读者判断：结论在哪些条件下由哪些证据支持。

## 1. 先写研究问题

推荐在实验设计前列出 RQ：

- RQ1: Does the proposed method improve overall performance under a fair budget?
- RQ2: Which component is responsible for the observed improvement?
- RQ3: How does performance scale with dimensionality, objectives, constraints, noise, or dynamics?
- RQ4: What additional computational overhead is introduced?

RQ 应与 Introduction 中的缺口一一对应。

## 2. 实验设置

必须交代：

- benchmark/dataset/instance 及选择理由；
- 对比算法及版本来源；
- 参数设置与调参协议；
- population size、终止条件、评价预算；
- 独立运行次数、随机种子或复现实验材料；
- 指标方向、归一化、参考点/参考集；
- 统计检验和显著性阈值；
- 硬件、软件、实现语言（当运行时间重要时）。

## 3. 公平比较

- 相同预算不等于相同 generations；应按 FEs、真实评价成本或问题相关预算比较。
- 如果模型训练昂贵，模型成本必须计入或明确说明为何可忽略。
- 如果基线参数采用文献默认，说明原因；如果调参，所有方法应有可比调参预算。
- 多目标比较不能只看一个指标而不解释指标偏差。

## 4. 结果呈现

### 4.1 表格

- 说明均值、标准差、中位数、最佳/最差值的含义。
- 最优结果高亮规则必须明确。
- 统计符号必须在表注解释。
- 表格应支持正文论点，不是数据堆砌。

### 4.2 图

- 收敛曲线、Pareto front、决策空间分布和敏感性图回答不同问题，不能互相替代。
- 图题应自包含，说明算法、问题、指标和比较条件。
- 正文引用图时必须告诉读者应观察什么。

### 4.3 结果段落

推荐顺序：

```text
As shown in [TABLE/FIGURE], [OBSERVATION].
The difference is concentrated on [SUBSET/CONDITION], suggesting that [MECHANISM/EXPLANATION].
However, [EXCEPTION/LIMITATION] indicates that [BOUNDARY].
```

## 5. 统计语言

- `significant` 只用于已定义的统计检验。
- `better on average` 不自动等于 statistically significant。
- 多实例比较时注意多重比较和排名方法的解释。
- 报告均值时也要考虑方差、稳健性或最差情况（当问题相关）。
- 不要把单次运行图示写成普遍结论。

## 6. 消融与敏感性

- 消融组件必须与贡献列表对应。
- 参数敏感性不是简单扫参后说“稳定”；要指出性能何时下降。
- 如果新算法含多个机制，不能只比较完整算法和旧算法。

## 7. Discussion

Discussion 应解释：

- 为什么某些问题获益；
- 哪些假设导致例外；
- 机制与结果之间是否有替代解释；
- 实践者何时应使用该算法；
- 计算成本和实现复杂度是否值得。

## 8. 常见失败

- 只报告最终指标，不报告预算。
- 只与弱基线比较。
- 用指标名称代替结果解释。
- 图很多但正文没有引导。
- 没有失败案例或例外。
- `extensive experiments` 替代具体证据。
