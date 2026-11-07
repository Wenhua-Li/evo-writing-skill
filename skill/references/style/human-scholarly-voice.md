# Human Scholarly Voice

目标不是把句子写得“高级”，而是让文本像一位熟悉 EC 的研究者经过思考后写出的稿子。核心特征是：选择具体、详略有别、节奏自然、评论克制。

## 1. 具体优先

用可核查的技术对象替代抽象评价。

少写：

- important
- challenging
- effective
- powerful
- promising
- crucial

多写：

- evaluation budget
- interacting variables
- feasibility ratio
- reference point
- nondominated front
- model update cost
- independent runs
- parameter sensitivity

例：

```text
Weak: Variable grouping plays a crucial role in improving the efficiency of evolutionary algorithms.
Better: Variable grouping reduces the number of decision variables changed in each trial vector, allowing the search to spend fewer evaluations on irrelevant dimensions.
```

## 2. 一段只做一件事

不要把背景、缺口、方法、限制和贡献塞进同一段。每段先确定它的任务，再决定句子。

常见段落任务：

- 给出问题；
- 解释困难；
- 比较路线；
- 说明设计选择；
- 报告结果；
- 解释例外；
- 限定结论。

## 3. 节奏不能像模板

避免连续段落都具有相同结构、相同长度和相同连接词。自然学术写作会：

- 用短句收束一个明确判断；
- 用较长句处理条件和机制；
- 在必要时重复术语，而不是强行找同义词；
- 在常识处少说，在关键区别处多说。

需要检查：

- 是否每句都以 `The proposed method` 开头；
- 是否每段都有三点；
- 是否连续使用 `Moreover` / `Furthermore` / `In addition`；
- 是否每个结果后都跟一句解释其重要性。

## 4. 少用元话语

以下表达只有在确实改变理解时保留：

- It is worth noting that
- It should be pointed out that
- As is well known
- Obviously
- Clearly
- In fact
- Indeed

通常更好的做法是直接写出事实。

## 5. 不要过度解释常识

面向 EC 读者时，不必反复解释：

- diversity matters；
- constraints reduce the feasible region；
- expensive evaluations limit the budget；
- large-scale search spaces are difficult。

只有在这些性质与本文机制发生具体关系时才解释。

## 6. 允许有重点的不对称

人手写作会根据重要性分配篇幅。不要为了“结构完整”让每个路线、每个参数、每个实验都平均展开。核心机制应比辅助细节得到更多文字。

## 7. 保留作者声音

如果用户提供样本，匹配其：

- 平均句长和句长波动；
- 常用连接方式；
- 是否偏好 `we`；
- 术语和缩写习惯；
- 标点；
- 直接程度；
- 段落长度。

不要为了统一风格抹去作者原有的合理个性。

## 8. 读出声检查

最终文本应当：

- 没有聊天口吻；
- 没有宣传口吻；
- 没有合规报告口吻；
- 没有机械重复；
- 没有每句都过分完整、平滑和对称。
