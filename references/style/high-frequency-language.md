# 高频词汇、搭配与修辞表达

本文件汇总 1,358 篇可用于语言统计的 TEVC 文档（1997–2023）。高频只表示常见实践，不表示强制或优秀。

## 1. 跨章节稳定术语

以下术语在长期语料中反复出现：

- `evolutionary algorithm(s)`
- `genetic algorithm(s)`
- `optimization problem(s)`
- `search space`
- `population size`
- `fitness function`
- `selection operator`
- `crossover operator`
- `mutation operator`
- `convergence`
- `diversity`
- `robustness`
- `benchmark problems`
- `function evaluations`
- `computational complexity`

## 2. 分章节内容词观察

### Introduction

高频内容词包括：`problem`、`algorithms`、`optimization`、`performance`、`search`、`solutions`、`methods`、`space`、`approach`、`research`、`function`、`population`、`design`。

典型修辞短语：

- `In this paper/article, ...`
- `We propose/present ...`
- `The remainder of this paper is organized as follows.`
- `Compared with ...`

其中 `in this paper` 在明确 Introduction 的 744 篇文档中出现，`we propose` 在 344 篇中出现，`the remainder...` 在 330 篇中出现。它们常见，但不应机械重复。

### Method

高频内容词包括：`algorithm`、`population`、`value`、`function`、`solution`、`selection`、`size`、`fitness`、`generation`、`randomly`。

常见搭配：

- `population size`
- `fitness function`
- `selection operator`
- `mutation operator`
- `crossover operator`
- `as follows`
- `the current population`
- `the next generation`

### Experiments / Results

高频内容词包括：`performance`、`results`、`test`、`function`、`population`、`obtained`、`compared`、`table`、`figure`、`evaluation`、`runs`、`average`。

常见功能搭配：

- `experimental results`
- `function evaluations`
- `statistical test`
- `compared with`
- `obtained by`
- `set to`
- `shown in Fig./Table`

### Conclusion

高频内容词包括：`results`、`performance`、`future`、`optimization`、`search`、`work`、`solutions`、`approach`、`research`、`convergence`、`diversity`。

常见搭配：

- `future work`
- `experimental results`
- `optimization problems`
- `real-world problems`
- `the effectiveness of`

## 3. 领域术语示例

术语统计中的稳定主题包括：

- `Pareto front` / `Pareto-optimal set`
- `nondominated sorting`
- `multiobjective evolutionary algorithm`
- `many-objective optimization`
- `constraint handling`
- `surrogate-assisted`
- `large-scale optimization`
- `dynamic optimization`
- `multimodal optimization`
- `hypervolume`
- `inverted generational distance (IGD)`

使用时应遵循 `terminology.md` 的定义和空间边界。

## 4. 近期才高频的实践

`ablation study` 在主语料中主要集中于 2021–2023，不能写成 1997 以来一直稳定存在的 TEVC 惯例。可以推荐消融，因为它有助于组件证据，但应标为“当前良好实践/编辑性建议”，而不是历史高频规则。

## 5. 常见修辞表达的使用建议

| 表达 | 用法 | 建议 |
|---|---|---|
| `In this paper/article` | 引出目的或贡献 | 可用，但不要每段重复 |
| `We propose` | 明确作者贡献 | 用在真正提出的方法/机制 |
| `The remainder...` | 全文导航 | 长文可用，不能替代贡献 |
| `To the best of our knowledge` | 谨慎声明首次/未知 | 少用，需检索支撑 |
| `It should be noted that` | 强调注意点 | 多数可删 |
| `As can be seen from` | 引导图表观察 | 确保图中确实可见 |
| `Experimental results show` | 引出经验结果 | 后接具体指标和范围 |
| `future work` | 收束限制 | 写具体方向，不写愿望 |

## 6. 不要把高频误作质量

`novel`、`state-of-the-art`、`significantly`、`optimal` 等词在语料中出现，并不等于所有使用都恰当。Skill 使用风险分级处理这些词，见 `claims-risk-rewrite.md`。
