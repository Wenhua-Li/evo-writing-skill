# 理论、基准与指标论文

本文件覆盖三类研究：理论分析、benchmark/test problem、performance indicator/评价协议。它们共同的重点是**定义、假设、适用范围和可复核性**。

## 1. 理论论文

### 1.1 证据结构

理论论文不是“公式很多的论文”。至少需要：

1. 分析对象：算法、算子、种群模型或评价协议。
2. 数学模型：哪些简化是分析模型的一部分。
3. 假设：有限搜索空间、独立同分布、选择方式、噪声模型等。
4. 命题：收敛、期望首次命中时间、稳定性、复杂度或界。
5. 证明或证明路线：关键引理、工具、附录位置。
6. 数值验证：验证预测，而不是用实验代替证明。
7. 边界：结果不能推广到哪些算法或问题。

### 1.1 引言写法

- 不要只说“理论很重要”。指出当前理论无法解释哪个实际机制或参数效应。
- 明确理论结果是 exact、asymptotic、upper/lower bound，还是基于近似模型。
- 如果分析的是简化算法，说明为什么该简化保留了研究问题的本质。

### 1.2 术语风险

- `convergence` 必须说明是 almost surely、in expectation、probability，还是实验上的指标下降。
- `runtime` 应区分 expected first hitting time、generations、function evaluations、CPU/wall-clock time。
- `optimal solution` 只在模型中存在明确定义时使用。
- 实验不能 `prove` 定理；定理也不能自动证明复杂算法的实际表现。

## 2. Benchmark / Test Suite 论文

### 2.1 核心论证

一个 benchmark 不是一组任意函数。需要说明：

1. 现有 benchmark 覆盖哪些性质。
2. 缺少哪些可控困难或真实问题特征。
3. 新问题的构造原则是什么。
4. 哪些参数控制难度、规模、约束、动态性、多峰性或 Pareto 几何。
5. 如何验证构造确实产生了预期性质。
6. 使用者应如何报告结果，避免选择性比较。

### 2.2 推荐组织

- Motivation and limitations of existing suites
- Design criteria
- Construction and formal properties
- Controllable difficulty dimensions
- Reference/known solutions（如适用）
- Evaluation protocol
- Demonstration experiments
- Usage guidance and limitations

### 2.3 写作风险

- 用“realistic”描述合成 benchmark，但没有真实问题证据。
- 只展示新算法在新 benchmark 上表现好，形成自我验证。
- 不公开生成参数、代码、参考解或评价协议。
- 把 benchmark 的覆盖范围写成“general-purpose”，但没有 instance-space 或性质覆盖分析。

## 3. Indicator / Performance Assessment 论文

### 3.1 证据结构

指标论文必须说明：

- 指标测量的属性是什么：convergence、diversity、spread、uniformity、feasibility、robustness还是复合质量。
- 参考集、参考点、归一化和目标方向如何影响结果。
- 指标满足或不满足哪些理论性质。
- 指标在哪些 Pareto 几何、目标数量或约束条件下会误导。
- 与已有指标相比，新增信息量是什么。

### 3.2 表述规则

- `better indicator value` 不等于 `better algorithm`，必须写清指标假设。
- Hypervolume、IGD、spacing 等指标不要互换其测量含义。
- 可视化不能替代指标，指标也不能替代 Pareto front 的几何检查。
- 如果指标本身需要大量计算，报告其计算成本。

## 4. 实验/验证在理论与基准论文中的位置

理论和基准论文仍可使用实验，但功能是：

- 验证定义和构造性质；
- 展示不同算法如何暴露 benchmark/指标的区分度；
- 检查理论预测与有限样本行为的差距；
- 展示错误使用协议时会发生什么。

不要把演示实验写成“新 benchmark 证明某算法全面最优”。

## 5. 结论

结论应回答：

- 本研究确立了什么定义、性质、界限或评价能力；
- 依赖哪些假设；
- 对算法设计或实验报告有什么直接影响；
- 哪些问题仍未覆盖。
