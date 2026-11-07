# Method

Method 章节必须让读者理解并复现“算法如何运作”，同时看出每个组件为何存在。

## 1. 推荐结构

1. **Overview**：总体框架、输入输出和流程图。
2. **Problem formulation / representation**：解如何表示，目标与约束如何评价。
3. **Core components**：按逻辑顺序写机制，而不是按代码文件顺序。
4. **Complete algorithm**：伪代码和步骤说明。
5. **Complexity and parameters**：成本、参数作用、默认值或自适应机制。
6. **Implementation details**：影响复现但不妨碍主线的内容。

不同论文可合并这些部分，但不能缺失关键逻辑。

## 2. 组件写法

每个组件采用同一问题链：

1. 这个组件处理什么困难？
2. 输入是什么，输出是什么？
3. 操作规则是什么？
4. 与已有方法的关键差异是什么？
5. 成本、参数和适用条件是什么？

```text
To address [DIFFICULTY], [COMPONENT] [OPERATION].
Given [INPUT], it first [STEP], then [STEP], and finally returns [OUTPUT].
This design differs from [PRIOR MECHANISM] in that [EXACT DIFFERENCE].
```

## 3. 伪代码

- 伪代码应是主循环和关键逻辑的可复现摘要。
- 输入、输出、初始化、终止条件、每代更新必须可见。
- 不要只给方程而没有执行顺序。
- 正文应解释伪代码中非显然步骤，而不是逐行翻译。

## 4. 公式

- 公式前说明目的，公式后解释符号和含义。
- 公式编号与正文引用一致。
- OCR 或导出错误造成的不完整公式不能作为写作范例。
- 若符号过多，使用 notation table。

## 5. 复杂度

明确成本口径：

- per-generation time complexity；
- per-evaluation simulation cost；
- surrogate/model training cost；
- memory；
- total FEs；
- wall-clock runtime。

`The algorithm is efficient` 必须落到上述至少一种可测量口径。

## 6. 参数

参数表后仍应解释：

- 参数控制什么；
- 默认值来自哪里；
- 是否调参；
- 敏感性如何；
- 是否随问题规模变化。

## 7. 与已有方法的关系

如果是组合已有组件：

- 明确哪些是直接使用；
- 哪些是修改；
- 哪些是新增；
- 组合后产生什么单独组件没有的行为。

## 8. 检查表

- [ ] 读者能从伪代码和正文复现主循环。
- [ ] 每个模块都有明确输入、输出和目的。
- [ ] 复杂度没有和实验运行时间混写。
- [ ] 参数作用和来源清楚。
- [ ] 与直接前驱的差异明确。
