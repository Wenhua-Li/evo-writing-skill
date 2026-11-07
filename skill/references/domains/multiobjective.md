# 多目标与高目标优化写作逻辑

多目标论文的核心是同时处理 trade-off、收敛和多样性。只写“找到一组解”不够，必须说明这组解在什么意义上有质量。

## 1. 定义与术语

- **decision/search space**：决策变量所在空间。
- **objective space**：目标向量所在空间。
- **Pareto dominance**：必须按最小化/最大化方向正确表述。
- **Pareto-optimal set (PS)**：决策空间中的解集。
- **Pareto front (PF)**：PS 在目标空间的映射。
- **approximation set/front**：算法得到的近似，不要直接称为 true PF。
- **convergence**：接近 Pareto-optimal 区域。
- **diversity**：解集覆盖、分布、均匀性或决策空间多样性，需具体定义。
- **many-objective**：通常指目标数导致支配区分度、可视化和指标计算困难的问题；首次使用给出目标数范围或引用定义。

## 2. Introduction 的专属论证

1. 说明目标冲突和实际/理论意义。
2. 解释为什么单目标化不足。
3. 指出现有 MOEA 的具体困难：选择压力、多样性维护、指标计算、约束、规模或动态。
4. 将本文机制映射到这些困难。
5. 实验必须覆盖与困难相应的指标和问题。

## 3. 方法写作

常见设计位置：

- mating selection；
- variation/reproduction；
- environmental selection；
- archive；
- reference vector/point；
- decomposition/scalarization；
- dominance relation；
- density/diversity estimator；
- constraint handling；
- preference/knee region；
- surrogate or learning model。

写每个机制时说明它主要影响 convergence、diversity、feasibility、efficiency 中的哪一个；如果一个机制声称同时改善多项，需要相应证据。

## 4. 指标和比较

常用指标包括但不限于：

- Hypervolume (HV)
- IGD / IGD+
- Generational Distance (GD)
- Spread / spacing / diversity metrics
- Set coverage
- Runtime / FEs

写作要求：

- 指标方向必须明确。
- 参考点、参考集和归一化必须明确。
- HV 对参考点敏感，IGD 对参考集覆盖敏感。
- 指标结果应与图形观察一致；不一致时解释。
- 高目标问题中可视化方法不能替代定义清楚的指标。

## 5. 常见逻辑错误

- 把 `diversity` 写成目标空间覆盖，却在实验里只测决策空间距离。
- 把某一指标领先写成“整体 Pareto 质量更好”。
- 在约束问题中只比较目标指标，不报告可行性。
- 对大规模问题只增加变量数，不分析变量交互或评价预算。
- 用二维 PF 图支持 many-objective 结论。

## 6. 结果表达

```text
[ALGORITHM] obtained higher HV values on [PROBLEM SET], indicating better combined convergence and coverage under the specified reference point.
On [PROBLEM/CONDITION], however, [BASELINE] produced a more uniform distribution, suggesting that [LIMITATION].
```

## 7. 偏好与 knee

如果目标是偏好区域而非完整 PF：

- 明确偏好来源和决策者模型；
- 说明为什么不需要覆盖整个 PF；
- 指标和图形应聚焦目标区域；
- 不要用完整 PF 指标反向证明 knee-oriented 方法失败，除非研究问题如此设定。
