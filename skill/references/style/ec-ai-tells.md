# EC 论文中的 AI 痕迹

这些规则针对结构性“默认选择”，不是词汇黑名单。单独出现一次不一定需要修改；同一段中反复出现时必须重写。

## A. 机械学术开场

### A1. 宏大背景

```text
With the rapid development of artificial intelligence and big data, evolutionary computation has attracted increasing attention.
```

改为直接进入具体问题：

```text
Large-scale multiobjective optimization becomes difficult when the evaluation budget grows more slowly than the decision space.
```

### A2. 空洞重要性

避免：

- plays a crucial role
- has become a hot topic
- is of great significance
- attracts extensive attention

改成这个对象具体影响什么。

### A3. 教科书式定义堆砌

不要连续解释 EC、EA、population、fitness，除非读者或后文确实需要。

## B. 机械结构与节奏

### B1. 强制三点贡献

不是所有 Introduction 都需要三条贡献。能用一个自然段落说清时，不要拆成列表。

### B2. 强制 RQ

实验章节可以按比较、消融、敏感性、应用自然组织，不必硬凑 RQ1–RQ4。

### B3. 每句一个连接词

减少连续使用：

- Moreover
- Furthermore
- In addition
- Besides
- Therefore

让事实顺序本身承担衔接。

### B4. 相同主语反复开头

例如连续五句都以 `The proposed algorithm` 开头。改主语、合并句子或让机制成为主语。

### B5. 表格化段落

不要把正文写成：

```text
First, ...
Second, ...
Third, ...
Finally, ...
```

除非步骤本身确实需要编号。

## C. 假精确与假权威

### C1. 无证据强主张

- `significantly outperforms`
- `state-of-the-art`
- `novel`
- `robust`
- `scalable`
- `optimal`

没有相应证据时删除或改成具体、有限的事实。

### C2. 泛化失败

避免从有限 benchmark 推出：

- always
- all problems
- universal
- superior in general
- fully solves

### C3. 伪文献姿态

不要为了显得严谨写：

- `To the best of our knowledge`
- `It is well known that`
- `Many studies have shown`

除非有明确文献支撑且这句话有必要。

## D. LLM 式解释欲

### D1. 每个事实后都解释重要性

```text
The population size is set to 100, which is important for maintaining diversity.
```

如果没有实验或理论解释，删去后半句。

### D2. 替读者总结显而易见的内容

```text
This demonstrates the importance of the proposed mechanism.
```

删除。让结果自己说话。

### D3. 重复同义限定

- `carefully designed`
- `properly selected`
- `appropriately adjusted`
- `effectively improved`

除非说明怎样 careful/proper/effective。

## E. EC 特定模板味

### E1. 万能问题动机

`The problem is NP-hard` 不能自动证明 EA 合理。必须说明搜索结构、约束、评价成本或领域基线。

### E2. 万能多目标动机

不要只写目标冲突；说明为什么需要近似整个 PF、偏好区域还是特定 trade-off。

### E3. 万能昂贵优化动机

不要只写“评价昂贵”；写清每次评价成本、可用预算、模型管理和模型误差。

### E4. 万能大规模动机

不要只写维度高；说明变量交互、分组误差、预算分配或复杂度增长。

## F. 结尾和宣传口吻

避免：

- The future looks promising.
- This opens a new direction.
- The method has great potential.
- Extensive experiments fully demonstrate...

改成具体结论：

```text
The results indicate that the grouping rule is most useful when interacting variables dominate the search error. Extending the analysis to overlapping groups remains open.
```
