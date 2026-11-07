# Claim–Evidence Matrix

用于把写作主张和证据绑定。任何强主张都必须能放入表中。

| # | Claim（英文草写） | Claim type | Evidence | Scope/condition | Risk | Action |
|---|---|---|---|---|---|---|
| 1 |  | novelty / performance / efficiency / theory / application |  |  | R1/R2/R3 | keep / qualify / remove / need evidence |

## Claim type

- **novelty**：与哪个已有机制不同，差异是否只是组合已有模块。
- **performance**：在哪些问题上、相对哪些基线、使用哪个指标。
- **efficiency**：函数评价次数、墙钟时间、模型训练开销还是实现复杂度。
- **theory**：假设、命题、证明范围和适用算法。
- **application**：领域指标、实际约束、部署或决策价值。

## 常用降级方式

- `optimal` → `near-optimal` / `best-found` / `Pareto-optimal`（仅在有正式依据时）
- `efficient` → `requires fewer function evaluations under the tested budget`
- `scalable` → `maintains performance as the number of decision variables increases from ... to ...`
- `robust` → `is less sensitive to ... under the tested noise levels`
- `significantly better` → 写出统计检验，或改为非统计的 `achieved lower mean ...`
- `state-of-the-art` → 命名具体基线和协议，或删除标签
