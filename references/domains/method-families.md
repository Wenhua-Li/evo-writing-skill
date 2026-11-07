# 方法谱系写作逻辑

## 1. GA / ES / EP

### GA

强调：

- 表示与遗传算子是否匹配；
- 编码是否造成冗余、非法解或 locality 问题；
- selection、crossover、mutation 的相互作用；
- 问题知识进入编码还是算子。

### ES

强调：

- 变异分布、步长、协方差或自适应机制；
- 选择记号如 `(μ + λ)`、`(μ, λ)` 必须准确；
- 连续优化中的收敛速率和理论模型；
- 不要把 ES 泛称为所有实数编码 EA。

### EP

强调：

- 表示和变异驱动的搜索；
- 与 GA 的历史差异不应写成简单优劣；
- 应用或理论模型中的评价方式。

## 2. DE

写 DE 时必须明确：

- mutation strategy，如 `rand/1`、`best/1`、`current-to-pbest/1`；
- crossover：binomial/exponential 或离散变体；
- `F`、`Cr`、population size；
- target/donor/trial vector 的术语；
- 参数自适应和外部 archive；
- 连续空间假设；若用于组合问题，必须解释代数或映射。

避免只写“采用 DE 提高性能”而不说明变体。

## 3. GP / Grammatical Evolution

强调：

- 程序/规则/表达式的表示；
- function set、terminal set、grammar；
- 语义合法性、类型约束；
- bloat、解释性、泛化；
- 适应度评价成本；
- 训练/验证/测试划分；
- evolved solution 是否可读、可部署。

不要把树结构图当作解释性证据。

## 4. PSO / ACO / Swarm Intelligence

### PSO

- velocity/position 更新规则；
- inertia、acceleration、neighborhood topology；
- personal/global/local best；
- 离散问题中位置和速度的含义；
- 稳定性和参数敏感性。

### ACO

- 构造图；
- pheromone 和 heuristic information；
- 解构造过程；
- 蒸发、更新和精英策略；
- 组合问题的可行性。

不要把生物隐喻当作机制解释；必须写清计算规则。

## 5. EDA / Model-based Search

强调：

- 概率模型学习什么变量关系；
- 采样和模型更新频率；
- 模型复杂度与数据量；
- 与 surrogate 的区别：EDA 模型常用于生成分布，surrogate 常用于近似评价；
- 模型误差如何传播。

## 6. Memetic / Local Search Hybrids

强调：

- 全局搜索与局部 refinement 的分工；
- refinement 频率、强度、对象选择；
- Lamarckian/Baldwinian 继承（如相关）；
- 局部搜索成本；
- 是否因局部搜索减少多样性。

## 7. Coevolution / Multipopulation

强调：

- 子种群代表什么；
- 合作或竞争关系；
- 适应度是否相对；
- 通讯/迁移/共享机制；
- 额外种群成本；
- 与单一种群基线的公平比较。

## 8. Neuroevolution / ML-assisted EC

强调：

- 进化的是结构、参数、规则还是学习组件；
- 训练数据与测试数据隔离；
- 学习模型是否在线更新；
- 模型开销；
- 泛化和过拟合；
- 与直接 ML 基线比较。

2020–2023 的相关实践应标为近期范式，不要声称其自 1997 年以来就是稳定写作规范。

## 9. Hyper-heuristics / Automatic Design

强调：

- 搜索的是启发式、组件配置还是完整算法；
- high-level 与 low-level heuristic 的分工；
- 训练实例和测试实例隔离；
- 自动配置预算；
- 泛化到未见实例的证据。
