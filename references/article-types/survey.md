# 综述论文

综述论文的贡献不是“读了很多文献”，而是建立可辩护的分类、比较和评价框架，使读者能理解领域结构、共识、矛盾与未解决问题。

## 1. 综述的贡献类型

常见贡献包括：

- 术语澄清：区分 tuning/control/adaptation/self-adaptation 等易混概念。
- 分类法：按问题、机制、模型管理、应用环境或证据类型建立多维分类。
- 批判性综合：指出不同研究假设、协议和结论为何不可直接比较。
- 研究空白：从分类和证据缺口推出未来方向，而不是泛泛写“more work is needed”。

## 2. Introduction 的组织

1. 领域为什么需要此刻的综述。
2. 现有综述覆盖了什么、没有覆盖什么。
3. 本文的范围边界：纳入哪些方法/问题/年代，不覆盖什么。
4. 分类轴和选择理由。
5. 综述贡献：不是逐篇罗列，而是回答哪些研究问题。

避免：

- 从生物进化史开始写很长背景，却没有说明综述问题。
- 只写 `We review recent advances` 而不定义 recent 和纳入标准。
- 把未来方向写成与综述证据无关的愿望清单。

## 3. 分类法写作

每个分类轴必须有判别功能：

- 这个分类能解释方法行为、适用条件或证据差异吗？
- 类别是否互斥；如果不互斥，是否允许多标签？
- 边界案例放在哪里？
- 分类是否来自文献实际差异，而不是为了表格整齐？

推荐写法：

```text
We classify existing approaches according to [AXIS], because this dimension determines [BEHAVIOR/COST/APPLICABILITY].
This dimension is orthogonal to [OTHER AXIS]; therefore, a method may belong to [COMBINATION].
```

## 4. 文献综合

每个类别至少回答：

- 共同假设是什么？
- 核心机制是什么？
- 解决什么困难？
- 引入什么新成本或偏差？
- 证据通常来自什么 benchmark、理论或应用？
- 哪些结论不能横向比较？

不要写成：

```text
A proposed X. B proposed Y. C proposed Z.
```

应改成：

```text
These approaches differ primarily in [MECHANISM].
Methods based on [PRINCIPLE A] reduce [COST], but depend on [ASSUMPTION]; methods based on [PRINCIPLE B] avoid [LIMITATION], at the cost of [TRADEOFF].
```

## 5. 表格和图

- 分类表应列方法、假设、适用问题、优势、成本、证据类型，而不是只列作者和年份。
- 时间线用于展示范式转变，不应替代比较。
- 图应解释分类关系或工作流程，而不是装饰。

## 6. 结论和未来方向

未来方向必须从证据缺口推出：

- 哪些类别缺乏理论分析；
- 哪些协议导致结论不可比；
- 哪些应用场景缺少真实评价；
- 哪些成本（模型训练、参数调优、人工定义）被忽略；
- 哪些新领域只有近期证据，不能包装成长期共识。

## 7. 风险

- 范围不明导致读者不知道综述是否完整。
- 引用堆砌但没有综合。
- 分类标准在不同层级混用。
- 只总结成功案例，不讨论失败和限制。
- 对 2020 后主题做过度确定的历史归纳。
