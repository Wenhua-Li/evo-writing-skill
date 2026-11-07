# Before/After: Method

## Before

> It is worth noting that the grouping strategy plays a crucial role in the proposed algorithm. Therefore, a carefully designed grouping method is adopted to properly divide the variables. After that, the improved DE operator is used to effectively generate promising offspring. This process can significantly enhance the search efficiency and guarantee better convergence performance.

## Problems

- `It is worth noting`、`plays a crucial role` 无信息；
- `carefully designed`、`properly`、`effectively` 假精确；
- `guarantee better convergence` 无证据；
- 没有说明输入、输出和操作。

## After

> At the beginning of each cycle, the algorithm estimates the interaction between decision variables from the current population. Variables whose estimated interaction exceeds θ are placed in the same group. Each group is then updated independently: for every target vector, the donor vector is constructed only from variables in the corresponding group, while the remaining variables are copied from the target. The updated vectors are recombined before environmental selection, so feasibility and dominance are still evaluated at the whole-solution level.

## Why it reads more human

机制、输入、输出和与整体评价的关系都清楚，没有宣传性副词。
