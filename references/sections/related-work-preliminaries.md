# Related Work、Background 与 Preliminaries

这些章节的作用不同，不应混写：

- **Related Work**：比较已有方法，定位缺口。
- **Background**：提供读者理解论文所需的领域或方法背景。
- **Preliminaries**：定义符号、问题形式、算法框架和理论概念。

## 1. Related Work

### 1.1 分类维度

优先按“设计原则”分类：

- dominance-based / indicator-based / decomposition-based；
- variable grouping / dimension reduction / direct search；
- penalty / repair / feasibility-rule / multiobjective constraint handling；
- surrogate model type / model management strategy；
- representation / variation operator / selection mechanism。

不要只按年份或作者分类。

### 1.2 每个类别的写法

```text
[ROUTE] methods address [ISSUE] by [SHARED PRINCIPLE].
They are effective when [CONDITION], but their reliance on [ASSUMPTION] makes them less suitable for [TARGET SETTING].
```

类别内比较应指出：

- 共同假设；
- 关键差异；
- 成本或偏差；
- 与本文的关系。

### 1.3 与本文差异

相关工作最后应回到本文，但不要重复贡献列表：

```text
The proposed method differs from [ROUTE] in that it [DIFFERENCE].
This difference is motivated by [PROBLEM PROPERTY] rather than by an additional heuristic component alone.
```

## 2. Background

Background 写给非本领域专家但必须读论文的人。只保留后文会用的概念：

- EC 基本框架只在读者可能不熟悉时简述。
- 应用领域知识只保留与建模有关的部分。
- 对经典概念引用权威来源，不在正文写长篇教材。

判断标准：如果删除某段背景，方法或实验仍完全可理解，该背景多半应删。

## 3. Preliminaries

### 3.1 内容

- 决策空间、目标空间、约束和可行域；
- Pareto dominance、PS、PF 等定义；
- 算法框架和伪代码；
- 指标、复杂度记号、统计模型；
- 后文所有反复使用的符号。

### 3.2 写作规则

- `Without loss of generality` 只在确实能等价转换时使用，并说明方向。
- 定义先直观解释，再正式定义。
- 公式后说明符号和含义，不把公式当作段落本身。
- 同一符号不能跨章节换含义。

## 4. 文献引用语言

- `X proposed ...`：陈述来源。
- `X showed ...`：用于作者确实展示的结果。
- `X demonstrated ...`：证据较强时使用。
- `X proved ...`：仅限形式证明。
- `X suggested ...`：用于提议、解释或启发，而非已验证结论。

## 5. 常见失败

- 将 Related Work 写成引用清单。
- 在 Preliminaries 中引入本文新贡献，导致“已有知识”和“本文方法”边界不清。
- 使用过时定义或不说明不同文献中术语冲突。
- 把 benchmark、算法和应用领域混在同一分类层级。
