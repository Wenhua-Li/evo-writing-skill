# Before/After: Experiments

## Before

> To fully demonstrate the outstanding performance of the proposed algorithm, extensive experiments are conducted on many benchmark problems. All parameters are carefully chosen according to previous experience. The results clearly prove that our algorithm is superior to state-of-the-art algorithms in terms of effectiveness, efficiency, robustness, and scalability.

## Problems

- `fully demonstrate`、`clearly prove` 过度；
- 没有 benchmark、参数、预算或指标；
- 四个优势全是标签；
- 没有失败或边界。

## After

> We compare the proposed algorithm with NSGA-II, MOEA/D, and a fixed-grouping DE variant on 30 continuous LSMOP instances. All algorithms use the same population size and a budget of 100,000 function evaluations. IGD+ and hypervolume are computed after normalizing the objective values, and each algorithm is run independently 20 times. The proposed algorithm obtains lower mean IGD+ values on 21 instances. Its advantage decreases on problems with weak variable interactions, where the grouping step adds overhead without changing the search distribution.

## Why it reads more human

比较条件、指标和结果都可核查，并且如实保留了不利场景。
