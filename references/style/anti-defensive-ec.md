# EC 论文中的反防御写作

目标是把“怕被审稿人质疑而写的话”改成“读者真正需要知道的话”。

## 1. 先区分两类限定

### 必须保留

如果删掉会影响以下内容，必须保留：

- 结论是否成立；
- 指标如何解释；
- 方法适用范围；
- 研究设计；
- 结果能否复现或正确使用。

这些限制写一次，放在 Methods、Experiments、Discussion 或 Limitations。

### 应该删除

- 预防式道歉；
- 重复免责声明；
- 自我贬低；
- 叠加 hedging；
- 想象中的审稿质疑；
- 与证据无关的“谨慎”。

## 2. Claim-forward

先说研究做了什么，再说边界。

不推荐：

```text
Although this study cannot solve all large-scale problems, it attempts to provide a preliminary investigation.
```

推荐：

```text
This paper investigates variable grouping in DE-based large-scale multiobjective optimization.
```

## 3. Positive scope

用研究范围表达边界。

不推荐：

```text
We do not claim that the method is applicable to all dynamic problems.
```

推荐：

```text
The evaluation covers dynamic problems with abrupt changes in the objective landscape.
```

## 4. Calibrated uncertainty

保留证据需要的 hedging，删除堆叠 hedging。

不推荐：

```text
may potentially suggest
```

可选：

- `suggests`
- `indicates`
- `is associated with`
- `under the tested conditions`

不要机械删除所有 `may`、`suggest`、`under these conditions`；按证据判断。

## 5. 常见防御句式

### “We do not claim...”

改为正向范围：

```text
The analysis focuses on continuous LSMOPs with up to 1000 variables.
```

### “This is not to say...”

直接陈述真正的关系：

```text
Grouping reduces the search dimension, but it can also separate interacting variables.
```

### “Although this study has limitations...”

写具体限制：

```text
The current evaluation does not include constrained or discrete LSMOPs.
```

### “only a preliminary attempt”

写具体研究形态：

```text
This paper presents an initial empirical study of ...
```

## 6. 实验结果不利时不要自我攻击

不推荐：

```text
The lower accuracy reveals an important limitation of our method.
```

推荐：

```text
The method reduces exact evaluations by 38%, with a 1.2-point lower mean accuracy than the baseline on the tested instances.
```

结果影响核心结论时必须保留并解释；不要把局部指标写成整体失败。

## 7. Abstract 和 Introduction 中的限制

摘要和引言不是不能写边界，但只有在缺少边界会误导主张时才写。常规做法是：

- 摘要用范围短语：`on the tested instances`、`for continuous LSMOPs`；
- 引言在贡献后或最后说明范围；
- 详细限制放实验和讨论。

## 8. Conclusion 中的限制

结论不应再次道歉。写法顺序：

1. 本文完成了什么；
2. 证据显示什么；
3. 适用范围；
4. 下一步问题。

例如：

```text
The proposed grouping strategy improved convergence on continuous LSMOPs with interacting variables. The current study does not evaluate discrete or constrained variants; extending the grouping rule to those settings is the next step.
```
