# 语料主要发现

## 1. 结构不是单一模板

明确章节覆盖率为：

- Abstract：1,516/1,517；
- Introduction：1,355/1,517（约 89.3%）；
- Method 类章节：1,182/1,517（约 77.9%）；
- Results 类章节：706/1,517（约 46.5%）；
- Experiments 类章节：462/1,517（约 30.5%）；
- Discussion：348/1,517（约 22.9%）；
- Conclusion：1,219/1,517（约 80.4%）；
- 独立 Related Work：298/1,517（约 19.6%）；
- 独立 Preliminaries/Background：339/1,517（约 22.4%）。

解释：TEVC 论文有稳定的论证功能，但章节名称和合并方式很多。Skill 因此按功能路由，而不是强制固定标题。

## 2. 摘要

- 中位长度约 187 词。
- 常见功能包括背景、缺口、方法、结果、结论，但顺序并不唯一。
- cue-based 统计中 `other` 很多，说明摘要句式多样，不能把少数模板当成普遍模式。

## 3. 标题

在 1,517 篇主语料中：

- 约 12.9% 使用冒号；
- 约 26.1% 使用 `based on` / `using` / `via` / `with` 等关系结构；
- 约 2.97% 的标题含 `survey/review/taxonomy`；
- 约 6.86% 含 `analysis/study/investigation/evaluation`。

标题实践支持“直接说明对象和方法”，不支持统一使用副标题。

## 4. 高频语言

跨章节稳定词汇包括 `evolutionary algorithm`、`optimization problem`、`search space`、`population size`、`fitness function`、`selection/crossover/mutation operator`、`convergence`、`diversity`、`benchmark problems` 和 `function evaluations`。

典型修辞表达：

- `in this paper/article` 在 Introduction 和 Conclusion 中长期高频；
- `the remainder of this paper is organized as follows` 长期存在；
- `future work` 长期存在于结论；
- `compared with` 在实验与结果中长期存在。

这些表达可以作为可选功能，不应机械堆砌。

## 5. 领域变化

候选标签统计显示：

- 多目标、真实应用、组合/约束、机器学习任务和大规模问题覆盖较多；
- surrogate-assisted、large-scale、multitask/transfer 在 2020–2023 更突出；
- `ablation study` 的证据主要来自 2021–2023，因此标为近期良好实践而非历史惯例。

## 6. 精选样本观察

150 篇分层样本支持以下写作逻辑：

- 新算法：缺口—设计原则—组件—复杂度—实验问题—消融/边界。
- 理论：模型—假设—定理/界—证明—数值验证—适用范围。
- Benchmark：现有覆盖盲区—构造原则—可控性质—评价协议—使用边界。
- 综述：范围—分类轴—批判性综合—证据缺口—未来方向。
- 应用：领域约束—优化模型—领域基线—实际指标—部署边界。
