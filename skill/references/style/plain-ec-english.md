# Plain EC English：强制语言规范

这份规范解决一个具体问题：模型常把软件、管理和营销语料中的表达误当作“高级学术英语”。EC 论文应把文字用在研究对象、操作和证据上，不让读者先解码隐喻或抽象名词。

本文件与 `skill/data/prose-gate.json` 同时生效。JSON 是机器检查的规范数据源；未列入 JSON 的同类表达并不自动获得许可。

## 1. 默认词汇必须普通、具体、准确

优先使用研究写作中的普通动词：`use`、`show`、`compare`、`update`、`select`、`generate`、`evaluate`、`improve`、`reduce`、`obtain`、`remain`、`change`、`cause`、`allow`。

优先写具体技术对象：decision variables、population、function evaluations、independent runs、reference points、constraint violation、nondominated solutions、model update cost。

不要用生僻名词替代可以直接说明的动作，不要为了变化而给同一个技术对象换多个名字。

## 2. 下列表达默认禁止出现在论文正文

命中时必须按原意重写。下表是改写方向，不是可以机械粘贴的同义词表。

| 禁止表达 | 根据实际含义改写 |
|---|---|
| `axes` | dimensions、objective coordinates；实际坐标轴除外 |
| `synthetic` | test problems、benchmark problems、simulated data；明确的数据类别除外 |
| `provenance` | source、origin |
| `admission` | acceptance、selection，或直接写哪个解能进入哪个集合 |
| `extreme` | largest/smallest values、boundary solutions；已有明确技术术语时除外 |
| `declared` | stated、specified、reported |
| `protocol` | experimental setup、procedure、settings；只要涉及 p 值或显著性，就必须明确写 statistical test，不能泛化成 setup |
| `tie` | equal scores、equal ranks、the same result |
| `saturated` | stops improving、reaches a plateau，或明确的容量状态 |
| `trajectories` | search histories、sequences of solutions、changes over generations |
| `certified` | verified、proved、guaranteed 只在有相应证据时使用；无证据时也不能换成 verify/verification，实际只是比较就写 compare |
| `menus` | choices、options，最好直接写实际选择操作 |
| `audit` | check、review、analysis；Audit 只作为任务模式名称 |
| `inferred` | estimated、derived、suggested by the results，按证据选择 |
| `rather than` | 重写对比关系；出现次数必须为 0 |
| `trial` | independent run、test、candidate solution；DE 的 trial vector 除外 |
| `rival` | competing algorithms、compared algorithms、baselines |
| `refinement` | local search、improvement、update 或具体操作 |

同时禁止 `leverage`、`harness`、`orchestrate`、`delve into`、`unlock`、`seamless`、`showcase`、`underscore`、`pivotal`、`realm`、`facilitate` 等典型 LLM/宣传措辞。软件隐喻如非技术语境的 `optimization engine`、`pipeline`、`governance` 也必须改成实际算法对象与步骤。完整匹配形式见 JSON。

## 3. 技术例外必须窄解释

只有同时满足以下条件才可保留例外：

1. 该词是研究对象或标准技术术语的一部分；
2. 原材料确实包含这个含义；
3. 替换会改变技术含义或造成歧义；
4. 使用它不是为了修辞变化。

例子：

- DE 的 `target vector`、`donor vector`、`trial vector` 是标准术语，不能把 trial 单独改成 candidate。
- 机器人、车辆或航天器的实际 `trajectory` 是研究对象；一般 EA 的“搜索轨迹”改写为 search history 或 sequence of solutions。
- 数据分类中的 `synthetic data` 可保留；用 synthetic 修饰一般 benchmark 不能自动豁免。
- 图形的 coordinate axes 可保留；用 axes 表示研究维度或贡献路线不可保留。
- 已明确作为技术对象的 extreme solutions 可保留；用 extreme 加强语气不可保留。

引用标题、正式算法名称、公式和直接引语不改动。例外不覆盖同一句中的其他问题。

## 4. 未列出的词也要过三道判断

### 隐喻判断

如果句子字面出现了菜单、准入、认证、引擎、对手、治理等对象，而论文实际讨论的并不是这些对象，就直接写出算法操作。

### 信息判断

如果一个抽象名词或形容词只让语气显得高级，却没有增加机制、条件、证据或范围信息，就删除它。

### 可理解性判断

如果 EC 读者需要先把一个隐喻翻译成常见术语才能理解句子，就使用那个常见术语重写。

## 5. 把抽象表达改成动作

- `orchestrates archive admission` → `controls which solutions enter the archive`
- `performance saturates` → `performance stops improving`
- `search trajectories` → `sequences of solutions visited during the search`
- `rival algorithms` → `compared algorithms`
- `leverages variable interactions` → `uses variable interactions`
- `facilitates convergence` → 写明实际变化，例如 `reduces the mean IGD value under the tested budget`

不要为了删除一个生僻词而补上未经提供的机制、数值或因果解释。

## 6. 对比关系直接写

错误输入：

> The method uses grouping rather than full-dimensional updates.

合格重写：

> The method updates one group of variables at a time while keeping the other variables fixed.

错误输入：

> The goal is not to improve convergence but to maintain diversity.

合格重写：

> The method prioritizes diversity when it conflicts with convergence.

错误输入：

> The method reduces not only FEs but also runtime.

合格重写：

> The method reduces both FEs and wall-clock time.

`rather than` 和 `instead of` 都不得用作格式化对比的捷径。先判断两个对象之间是选择、对比、排除还是取舍，再重写整个关系；能直接陈述实际操作时，不保留对比连接词。

如果被对比对象只是 `declared protocol`、`stated procedure`、`fixed rule` 等没有技术信息的泛称，删除整个对比尾巴。不得写成 `without relying on a stated procedure`、`no prespecified selection rule` 或 `does not depend on a fixed procedure` 来保留原来的官僚式对照。

## 7. 段落必须实质重建

对 AI 腔明显的段落，至少重新考虑句子的主语、边界和信息顺序，不能只换形容词与连接词。自然学术写作允许短句、重复必要术语和详略不对称；它不追求每句同样完整、每段同样长度、每段恰好三点。

最终文本应让读者的注意力落在研究上，而不是落在措辞本身。
