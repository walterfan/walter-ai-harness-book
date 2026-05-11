# 驾驭工程：给 AI 套上缰绳

*一本关于 **驾驭工程** 的长篇中文技术书 —— 一种刻意塑造 AI 编码智能体所处环境的实践，好让它们生产出来的软件是可验证、可观测、可理解的。*

| | |
|--|--|
| **作者** | Walter Fan |
| **许可证** | CC-BY-NC-ND-4.0（正文）· MIT（代码样例） |
| **状态** | 草稿 —— 骨架就位，章节正在撰写中 |
| **源码** | [`source/`](https://github.com/walterfan/async-harness-book/tree/main/source) |

## 本书怎么读

本书循一条六段式的论证弧线 —— **为什么 → 是什么 → 怎么做 → 例子 → 结语 → 参考**。大多数读者应当把第一、第二部分顺着读下去，然后进第三部分挑自己最需要的那一份方法论，再从第四部分挑一两份贴近自身技术栈的案例研究。第五部分短小、偏行动；第六部分是参考。

本书最前头还有一份 **Part 0 · Presentation**（公开分享），它面向的是另一类读者：任何人若在一次会议前只剩六十分钟，又需要把整本书当成一场 *talk 讲出去* —— 那就从这一 Part 开始。它把全书压成一份一小时的讲稿，外加一份分钟级的 speaker outline 与一份每页一张 slide 的大纲。只想读论证的读者可以跳过 Part 0；需要把这套论证 *再次传递* 给同事的读者，应当从这里起步。

每一份有实质内容的章（第 02 至第 12 章）都在正文下方遵循同一副双节骨架：``## 研究脉络`` 把论证钉在可引用的先前工作之上，``## 动手环节`` 则至少交付一件可跑起来的制品。这些章节是刻意把理论与实践配对的。

```{toctree}
:maxdepth: 2
:caption: Part 0 · 公开分享

chapters/00-presentation/index
```

```{toctree}
:maxdepth: 2
:caption: 第一部分 · 为什么

chapters/01-foreword
chapters/02-four-stage-evolution
```

```{toctree}
:maxdepth: 2
:caption: 第二部分 · 是什么

chapters/03-what-is-harness-engineering
chapters/03a-agent-memory-anatomy
chapters/03b-agent-loop-anatomy
```

```{toctree}
:maxdepth: 2
:caption: 第三部分 · 怎么做

chapters/04-three-guardians
chapters/05-harness-anatomy
chapters/06-operating-a-harness
```

```{toctree}
:maxdepth: 2
:caption: 第四部分 · 例子

chapters/07-openharness
chapters/08-superpowers
chapters/09-lazy-scrum-team
chapters/10-claude-code
chapters/11-lazy-ai-coder
```

```{toctree}
:maxdepth: 2
:caption: 第五部分 · 结语

chapters/12-where-we-go-from-here
```

```{toctree}
:maxdepth: 2
:caption: 第六部分 · 参考

chapters/13-appendices/index
references
colophon
```
