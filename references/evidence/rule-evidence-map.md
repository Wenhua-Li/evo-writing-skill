# 规则证据映射

本表把 Skill 的主要规则与语料证据、样本观察和证据等级关联。公开版本不包含论文全文或长摘录。

| ID | 规则 | 等级 | 主要依据 |
|---|---|---|---|
| R-001 | 按问题、方法和贡献类型三维路由，不按算法名单套模板 | A | 全语料标题/摘要候选标签；150 篇分层样本 |
| R-002 | 算法论文建立“困难—现有路线—缺口—机制—证据”链条 | A | NSGA-II、ParEGO、CLPSO、CCPSO2、DSDE 等样本 |
| R-003 | 相关工作按设计原则分类并比较限制 | A | 参数控制综述、DE 综述、memetic computation 综述、ParEGO |
| R-004 | 独立 Related Work 不强制；可融入 Introduction 或 Preliminaries | A | 独立 Related Work 覆盖约 19.6%，章节结构统计 |
| R-005 | 方法章节必须说明输入、输出、流程、参数、成本和与直接前驱差异 | A | 新算法和算子论文样本一致结构 |
| R-006 | 实验先定义研究问题，再报告设置和结果 | B | 近年算法论文更常显式使用；早期也存在等价组织 |
| R-007 | `significant` 只能绑定统计检验 | C | 术语准确性规则；部分语料存在混用，不能因常见而继承 |
| R-008 | `efficient` 必须区分 FEs、runtime、模型成本和实现成本 | A | 昂贵优化、并行和大规模样本反复强调成本口径 |
| R-009 | 多目标结果必须区分 convergence 与 diversity | A | MOEA 样本、指标论文、NSGA-II 和许多高目标论文 |
| R-010 | 约束论文同时报告可行性和目标质量 | A | 约束优化、CMOP 与 runtime analysis 样本 |
| R-011 | 昂贵优化必须说明真实评价预算与 surrogate 管理 | A | ParEGO、trauma system、multifidelity benchmark 样本 |
| R-012 | 动态优化评价应覆盖变化检测/跟踪而非只报告静态收敛 | A | dynamic test problems、dynamic optimization 综述样本 |
| R-013 | 理论论文先限定模型、假设和结果类型 | A | NFL、runtime analysis、PSO stability、ES theory 样本 |
| R-014 | Benchmark 论文必须说明现有覆盖盲区和构造原则 | A | 动态测试问题、约束测试套件、niching/multifidelity benchmark 样本 |
| R-015 | 综述必须有范围、分类轴和批判性综合 | A | 参数控制、uncertain environments、DE、memetic computation、CCEA 综述 |
| R-016 | 应用论文必须有领域约束、领域基线和实际意义 | A | VLSI、routing、trauma system、scheduling、robotics 等样本 |
| R-017 | 结论要对应证据并写出边界，不是摘要复述 | A | 早期至近期结论样本及高频 `future work` |
| R-018 | 近期 ML/ablation 实践需标注时代范围 | B | `ablation study` 主要出现于 2021–2023；ML-hybrid 候选标签增长 |
| R-019 | 高频词不直接等于推荐表达 | C | 词表含通用词、OCR 噪声和证据不足表述，需要人工过滤 |
| R-020 | OCR/双栏串字不得作为写作风格学习 | A | 构建质量报告和人工抽查确认 |

## 代表来源示例

用于人工精读和规则校准的代表性论文包括：

- 1997 `No Free Lunch Theorems for Optimization`
- 1997 `Evolutionary Computation: Comments on the History and Current State`
- 1999 `Parameter Control in Evolutionary Algorithms`
- 2002 `A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II`
- 2004 `Dynamic Multiobjective Optimization Problems: Test Cases, Approximations, and Applications`
- 2006 `ParEGO: A Hybrid Algorithm With On-Line Landscape Approximation for Expensive Multiobjective Optimization Problems`
- 2007 `A Runtime Analysis of Evolutionary Algorithms for Constrained Optimization Problems`
- 2011 `Differential Evolution: A Survey of the State-of-the-Art`
- 2011 `A Multi-Facet Survey on Memetic Computation`
- 2016 `Data-Driven Surrogate-Assisted Multiobjective Evolutionary Optimization of a Trauma System`
- 2018 `A Generic Test Suite for Evolutionary Multifidelity Optimization`
- 2019 `A Taxonomy for Metamodeling Frameworks for Evolutionary Multiobjective Optimization`
- 2021–2023 的大规模、迁移、昂贵、动态和学习辅助研究样本

这些示例用于说明规则来源，不构成“唯一范文”。
