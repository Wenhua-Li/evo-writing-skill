# 新算法与改进算法论文

算法论文的中心不是证明“提出了一个新东西”，而是说明：针对一个可定义的问题困难，本文做了哪种有理由的搜索改变，并用什么证据验证它。

## 1. Introduction

按“困难—路线—缺口—设计”推进：

1. 问题的具体性质；
2. 现有路线的共同假设；
3. 该假设在目标问题中为什么不合适；
4. 本文改变哪个环节；
5. 用什么条件验证。

不要把 GA/DE/PSO 基础教材写半页，除非目标读者确实需要。

## 2. Method

方法章节要像“可复现的技术说明”，不是宣传文案。

每个组件回答：

- 输入和输出；
- 执行规则；
- 为什么采用该规则；
- 与直接前驱的差异；
- 参数和成本。

如果方法只是组合已有模块，必须写清组合后的行为，而不是把每个模块分别介绍一遍。

## 3. Experiments

实验不必机械使用 RQ 编号，但必须能让读者看出：

- 总体性能如何比较；
- 新机制是否起作用；
- 性能随问题性质如何变化；
- 额外成本是否值得。

预算口径必须与论文主张一致：

- expensive optimization 看真实评价次数和模型成本；
- large-scale optimization 看维度、预算和复杂度；
- dynamic optimization 看变化后的跟踪；
- multiobjective optimization 同时看 convergence、diversity，必要时看 feasibility。

## 4. Results

先写观察，再写解释：

```text
[ALGORITHM] obtained lower mean IGD+ values on [SUBSET]. The gains were concentrated on [CONDITION], which is consistent with the role of [MECHANISM]. On [OTHER SUBSET], the improvement disappeared because [SUPPORTED EXPLANATION OR UNKNOWN].
```

如果没有证据解释原因，写 `The reason for this behavior remains unclear` 比编造机制更专业。

## 5. Conclusion

结论应说明：

- 方法针对什么问题；
- 证据显示何时有效；
- 何时无效或未验证；
- 下一步最值得研究什么。

避免 `great potential`、`broad prospects`、`fully demonstrates`。

## 6. 常见失败

- 把“组合模块”写成创新而不解释交互；
- 基线缺少直接前驱；
- 消融不能归因；
- 只报告均值，不报告预算、方差或失败案例；
- 每个贡献都写成 novel/effective；
- 用固定模板写贡献列表和 RQ，导致文章像生成稿。
