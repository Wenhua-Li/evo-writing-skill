# Introduction

Introduction 的目标不是把领域介绍完整，而是让读者尽快明白：这个问题为什么难、已有路线为什么留下缺口、本文为什么采用这种设计。

## 1. 自然的信息推进

常见但不强制的顺序是：

1. 给出研究对象和具体困难；
2. 概括已有路线及其适用边界；
3. 指出仍未解决的问题；
4. 说明本文设计动机；
5. 给出贡献和验证范围。

这不是固定模板。短论文可以压缩成两段；理论论文可以先限定模型；应用论文可以先写领域约束。

## 2. 第一段写具体困难

少用领域宣传。比较：

```text
Weak: With the rapid development of evolutionary computation, multiobjective optimization has attracted increasing attention.
Better: When the number of decision variables reaches several hundred, most MOEAs spend a large part of their evaluation budget on updates that do not change the nondominated set.
```

## 3. 相关工作按路线写

不要逐篇列作者。每条路线说明：

- 共同原则；
- 能解决什么；
- 在本文问题中留下什么限制。

如果缺口只是“效果不够好”，还不足以支撑方法设计；必须说明是哪一类问题、哪一种机制、哪一种成本或哪一种证据不足。

## 4. 贡献可以用段落写

贡献列表不是必须的。自然写法：

```text
The proposed method differs from fixed-grouping approaches in that it re-estimates variable groups as the search proceeds. We evaluate this design against fixed-grouping and transformation-based baselines under the same evaluation budget.
```

如果使用列表，每项必须有不同对象和证据，不要拆成“提出框架、设计算法、做实验”三个同义项。

## 5. Roadmap 可选

`The remainder of this paper is organized as follows` 在 EC 论文中长期存在，但不应机械使用。短文章或结构清楚的论文可以省略；长文可用一句话导航。

## 6. 检查

- 前两段是否已经出现具体困难；
- 每条路线的限制是否具体；
- 缺口是否能被方法回应；
- 贡献是否对应后文证据；
- 是否有“rapid development / crucial / meaningful / extensive”等空泛表达；
- 是否有防御性开场。
