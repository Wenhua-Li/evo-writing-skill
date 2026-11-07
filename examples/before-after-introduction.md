# Before/After: Introduction

## Before

> In recent years, multiobjective optimization has attracted increasing attention from researchers all over the world. Many excellent algorithms have been proposed, and they play a crucial role in many real-world applications. However, existing methods still have some shortcomings when solving large-scale problems. Therefore, it is necessary and meaningful to design a more effective algorithm. The main contributions are as follows: 1) We propose a novel framework. 2) We design an efficient operator. 3) We conduct extensive experiments.

## Problems

- 空泛背景和 importance signaling；
- “some shortcomings” 没有具体缺口；
- “necessary and meaningful” 是评价，不是论证；
- 贡献列表同义重复。

## After

> When a multiobjective problem contains hundreds of decision variables, a variation operator that updates all variables jointly rarely produces improving moves within a practical evaluation budget. Grouping-based MOEAs reduce this difficulty by partitioning the decision space, but most implementations determine the groups before the search and keep them fixed. This limits their use when variable interactions change as the population converges.
>
> This paper proposes a DE-based MOEA that re-estimates variable groups during the search and uses them to generate trial vectors at the group level. The design is intended to preserve the interaction structure while reducing the dimension of each update. We evaluate the method on continuous LSMOP instances and compare it with fixed-grouping, transformation-based, and operator-level baselines.

## Why it reads more human

第一段完成“困难—现有路线—具体限制”，第二段直接给设计差异和验证范围，没有模板化贡献列表。
