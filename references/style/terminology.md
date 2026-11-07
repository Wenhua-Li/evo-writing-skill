# EC 术语与符号规范

目标是让术语承担准确技术含义，而不是用近义词做风格变化。

## 1. 高频但必须精确的术语

| 术语 | 规范用法 | 常见错误 |
|---|---|---|
| solution | 搜索/决策空间中的候选解 | 与 algorithm、model 混用 |
| individual / particle / chromosome | 特定算法谱系中的个体表示 | 不考虑谱系而混用 |
| objective function | 优化问题中定义的目标 | 与 fitness 不加区分 |
| fitness | 算法选择所使用的适应度，可由目标转换而来 | 在多目标中把每个目标都直接叫 fitness 而不解释 |
| convergence | 接近最优/Pareto 区域的过程 | 与 diversity 或 feasibility 混写 |
| diversity | 决策空间或目标空间的分布性质 | 不说明空间和度量 |
| feasible solution | 满足约束的解 | 与 high-quality solution 混用 |
| constraint violation | 约束违反量 | 与 penalty value 混用 |
| function evaluations (FEs) | 真实目标/适应度评价次数 | 与 generations 或 wall-clock time 混用 |
| runtime | 必须有口径：CPU、wall-clock、generations、FEs | 单独写 runtime 而无定义 |
| complexity | 理论复杂度或操作成本 | 与实验运行时间混写 |
| optimal | 有数学定义和保证的最优 | 用来修饰最好实验结果 |
| near-optimal | 接近已知或参考最优的经验表述 | 没有参考依据时使用 |
| Pareto-optimal set/front | PS/PF 有严格空间区别 | 将二者互换 |

## 2. 缩写

- 第一次出现：`evolutionary algorithm (EA)`、`multiobjective evolutionary algorithm (MOEA)`。
- 之后保持一致，不在 `EA`、`algorithm`、`optimizer`、`search method` 之间无意义切换。
- `PSO`、`GA`、`DE` 这类稳定缩写可使用，但首次仍应定义。
- 避免自定义过多缩写；如果缩写没有节省重复成本，用全称。

## 3. 单复数和拼写

- `multiobjective optimization` 与 `multi-objective optimization` 都在文献中出现；一篇论文选一种并保持。
- `many-objective` 通常保留连字符。
- `real-world` 作定语；`in the real world` 作名词短语。
- 算法复数可用 `EAs`、`MOEAs`；不要写 `EA's` 表示复数。
- `Pareto front`、`Pareto set`、`Pareto dominance` 保持标准拼写。

## 4. 容易误导的搭配

### efficient

必须说明效率口径：

- fewer function evaluations
- lower wall-clock time
- lower model-training overhead
- lower memory requirement
- better anytime behavior

### robust

必须说明对什么鲁棒：

- noise level
- parameter perturbation
- dynamic changes
- model approximation error
- instance variation

### scalable

必须说明随什么扩展：

- decision variables
- objectives
- constraints
- instances
- population size
- data samples

### general

必须说明覆盖范围；否则改为 `across the tested instances`。

## 5. 符号一致性

- 一个符号只表示一个对象。
- 决策变量、目标向量、种群、代数、指标分别使用清楚符号。
- 在公式后定义所有符号，即使看似常见。
- 若 `N` 同时想表示 population size 和样本数，必须改一个。
- 最小化/最大化方向在定义、指标和结果表中一致。

## 6. 中英文术语映射

Skill 解释时可使用中文，但英文成稿应以标准英文术语为准。不要为了中文解释创造直译，例如：

- 环境选择：environmental selection
- 交配选择：mating selection
- 非支配排序：nondominated sorting
- 拥挤距离：crowding distance
- 参考向量：reference vector
- 代理模型管理：surrogate management
- 首次命中时间：first hitting time
