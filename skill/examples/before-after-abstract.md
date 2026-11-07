# Before/After: Abstract

## Before

> With the rapid development of evolutionary computation, large-scale multiobjective optimization has become a hot topic. It is worth noting that existing algorithms may not be efficient enough when facing complex decision spaces. Therefore, this paper proposes a novel and efficient DE-based algorithm. The experimental results may potentially indicate that the proposed method significantly outperforms state-of-the-art algorithms, although we do not claim that it is universally optimal for all problems.

## Problems

- 宏大开场；
- `hot topic`、`novel and efficient` 空泛；
- `may potentially` 叠加 hedging；
- `significantly` 无统计依据；
- `We do not claim` 防御性。

## After

> Large-scale multiobjective optimization problems (LSMOPs) remain difficult for evolutionary algorithms because the evaluation budget grows much more slowly than the decision space. This paper proposes a DE-based MOEA that partitions interacting decision variables before generating trial vectors, allowing each update to search a lower-dimensional subspace. On LSMOP instances with 100 to 1000 variables, the proposed algorithm obtained lower mean IGD+ values than NSGA-II and MOEA/D under the same number of function evaluations. The current evaluation is limited to unconstrained continuous problems.

## Why it reads more human

先给具体困难，再给机制和实际证据，最后用一句正向范围限定收尾，没有宣传语或道歉。
