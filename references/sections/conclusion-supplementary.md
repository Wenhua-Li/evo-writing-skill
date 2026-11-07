# Conclusion、Future Work、图表与补充材料

## 1. Conclusion

结论不是摘要的同义改写。它应回答：

1. 本文做了什么；
2. 证据实际显示了什么；
3. 哪些条件或假设限制结论；
4. 对后续研究或实践有什么可执行启示。

语料中明确 Conclusion 的章节约覆盖 80.4%；没有独立结论标题不等于可以不收束贡献。

### 1.1 推荐结构

```text
This article has [PURPOSE/METHOD SUMMARY].
The results show that [EVIDENCE-BOUND FINDING], particularly under [CONDITION].
The analysis suggests that [INTERPRETATION/LIMITATION].
Future work will investigate [SPECIFIC EXTENSION], including [BOUNDED DIRECTION].
```

### 1.2 结论中的语言

- `show` / `indicate` / `suggest`：经验结果。
- `demonstrate`：证据较充分时使用。
- `prove`：只用于形式证明。
- `will find increasing attention` 等预测性表述少用；除非讨论领域意义，否则删除。

## 2. Future Work

`future work` 在语料中长期常见，但应具体：

不佳：

```text
Future work will focus on improving the algorithm and applying it to more problems.
```

更好：

```text
Future work includes analyzing [PARAMETER/MECHANISM] under [CONDITION], extending the evaluation to [PROBLEM FEATURE], and accounting for [COST/LIMITATION] that was not modeled here.
```

## 3. 图、表和算法

### 图题

应包含对象、条件和观察单位，例如：

```text
Fig. X. Mean IGD profiles of [ALGORITHMS] on [PROBLEM] with [DIMENSION/OBJECTIVES/BUDGET].
```

### 表题

应说明指标、运行次数和统计符号，不让读者回正文猜。

### 算法标题

`Algorithm 1: [Purpose/Procedure]` 比只写算法名更自解释。

## 4. 补充材料

补充材料适合放：

- 完整参数表；
- 额外实例结果；
- 长证明；
- 额外图；
- 数据和代码说明。

正文仍必须能独立支持主要结论，不能把关键证据完全移到补充材料。

## 5. 最终一致性检查

- [ ] 摘要、贡献、实验和结论没有互相矛盾。
- [ ] 每个贡献都有结果、理论或引用支持。
- [ ] 限制不是装饰性句子，而与证据范围一致。
- [ ] Future work 与当前缺口相连。
- [ ] 所有图表在正文被引用并解释。
