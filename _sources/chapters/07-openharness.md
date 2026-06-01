---
status: draft
chapter-type: case-study
case-study-kind: open-source
---

# 案例研究：OpenHarness

> *开源世界里，最接近"教科书级马具"的那一具。*

OpenHarness 由香港大学数据科学实验室（HKUDS）编写，以 MIT 许可开源发布 {cite}`hkuds2025openharness`。它是本书最常回头引用的那份参考实现。读它的感觉，就像作者们已经先写过第 05 章：仓库整齐地分成十个子系统，每一个都刚好对应到"三护法 × 四区域"矩阵里的某一格、或某一小簇格子。本章逐个走过这些子系统、引用 Agent Loop 核心那一小段代码，并给整个项目按第 05 章的矩阵打一次分。

## 07.1 —— 一眼看清十个子系统

以 2026-03 的快照为准，OpenHarness 围绕十个子系统组织，大致对应上游仓库 `src/openharness/` 下面的十个目录：

1. `api/` —— OpenAI 兼容的客户端，以及 Copilot 认证适配器。
2. `autopilot/` —— 那个长期运行的智能体服务，本书第 02 章第 4 阶段的例子就隐指它。
3. `channels/` —— 与 Slack、Discord、飞书、Telegram 以及另外八个消息面的集成。
4. `config/` —— schema、settings、路径助手；教科书式的 SDD × 护栏。
5. `coordinator/` —— 智能体定义的注册表。
6. `engine/` —— Agent Loop 本身（见下文 07.2）。
7. `hooks/` —— 事件总线，驱动那道以 hook 为核心的护栏。
8. `mcp/` —— MCP 客户端接线；工具使用的那条通道。
9. `memory/` —— 会话记忆管理器。
10. `sandbox/` —— 基于 Docker 的执行隔离；Runtime 层的牧场。

想逐条核对本章说法的读者，可以在一份全新的 [`HKUDS/OpenHarness`](https://github.com/HKUDS/OpenHarness) 克隆里 `ls src/openharness/`，会看到同样这十个名字。这份分类学是 *从代码里抽取出来* 的，不是外部强加上去的。

## 07.2 —— Agent Loop（不超过 20 行，MIT 署名）

任何一具马具的核心，都是它的 agent loop。OpenHarness 的 `engine/query_engine.py` 把 ReAct 式循环 {cite}`yao2022react` 压缩成一种既便于审计、也便于埋点的形态。为便于讲解，这里略作删节：

```python
# Adapted from OpenHarness/src/openharness/engine/query_engine.py
# MIT License, Copyright (c) 2025 HKUDS.
def step(self, state):
    messages = self.memory.window(state)
    plan = self.model.complete(messages, tools=self.tools.schemas())
    if plan.tool_calls:
        outputs = [self.tools.invoke(c) for c in plan.tool_calls]
        state = self.memory.extend(state, plan, outputs)
        return state, "continue"
    return self.memory.extend(state, plan, []), "halt"
```

对本书的论点而言，重要的不是这不到二十行本身，而是它们把三项决定编码了进去：(a) 模型把工具调用当作一等结构化输出发出，而不是自由文本；(b) 记忆管理器 *持有* 上下文窗口策略；(c) 这个循环 *显式地* 把"continue"和"halt"两种状态分开。这三项决定，对人类评审者都是 *可见* 的——而正是这份可见性，让这具马具可以被审计。

## 07.3 —— 43 个工具的分类（Toolformer 风格）

在 2026-03 的快照里，OpenHarness 自带 43 个一方工具 {cite}`hkuds2025openharness`。部分分组如下：

```{list-table}
:header-rows: 1
:widths: 30 25 45

* - 分组
  - 数量
  - 例子
* - 文件与代码浏览
  - 9
  - `read_file`、`grep`、`list_dir`、`semantic_search`
* - 编辑
  - 6
  - `write_file`、`str_replace`、`apply_patch`、`delete_file`
* - Shell 与进程
  - 5
  - `run_command`、`await_job`、`tail_terminal`、`kill_job`、`cat_terminal`
* - VCS
  - 4
  - `git_status`、`git_diff`、`git_commit`、`git_log`
* - Web 与抓取
  - 3
  - `web_search`、`web_fetch`、`read_lints`
* - MCP 客户端
  - 3
  - `mcp_call`、`mcp_fetch_resource`、`mcp_list_resources`
* - 其他杂项
  - 13
  - 记忆、sandbox、channel、notebook 及各类辅助工具
```

这份分组，把 Toolformer 式的论点 {cite}`schick2023toolformer` 做成了具体的东西：工具不是事后补上的附属品，它们是智能体 *行动* 所经过的首要平面。MCP 规范 {cite}`anthropic2024mcp` 把这个面进一步延伸到了第三方工具。

## 07.4 —— 十二格亮点图

本书的每一章案例研究，都会按第 05 章的十二格、以 0–5 分制给马具打分，并用 1–3 句话、引用 `oss/OpenHarness/` 下的具体文件作为证据。

```{list-table}
:header-rows: 1
:widths: 20 8 72

* - 格子
  - 得分
  - 证据
* - SDD × 缰绳
  - 4
  - `README.md`、`src/openharness/prompts/system_prompt.py`，以及 `openharness/prompts/context.py` 打包在一起引导智能体的行为。
* - SDD × 护栏
  - 4
  - `config/schema.py` ＋ `config/settings.py` 校验每一次启动时的配置；坏配置直接让进程终止。
* - SDD × 牧场
  - 3
  - 没有显式的验收表模式；评审依赖上游的 PR review，加上 `autopilot/service.py` 的状态机。
* - SDD × 梳理
  - 3
  - `plugins/loader.py` 和 `commands/registry.py` 会刷新进程内注册表，但对"活文档"的梳理是临时性的。
* - TDD × 缰绳
  - 3
  - `tests/` 下上游测试套件分量很足，但不是"先 commit 为红"那种模式；智能体的上下文默认不会读测试。
* - TDD × 护栏
  - 4
  - `sandbox/adapter.py` ＋ `sandbox/docker_backend.py` 拒绝任何 Docker 之外的代码执行；`permissions/checker.py` 按策略拒绝工具调用。
* - TDD × 牧场
  - 3
  - CI 会在 PR 上跑 `pytest`；没有故障注入或敌意测试套件。
* - TDD × 梳理
  - 2
  - 没有公开的 flaky 测试隔离区；上游的分诊是人工的。
* - MDD × 缰绳
  - 3
  - `engine/stream_events.py` 与 `services/__init__.py` 暴露了事件流——这是一个不错的 *潜在* 北极星，但未被正式宣布。
* - MDD × 护栏
  - 4
  - `permissions/checker.py` ＋ `sandbox/path_validator.py` 作为代码实现的成本上限与爆炸半径上限。
* - MDD × 牧场
  - 3
  - 有发布 staging（tag + changelog）；没有公开的 SLI 关卡。
* - MDD × 梳理
  - 2
  - 没有公开的每周审计脚本；dashboard 由部署 OpenHarness 的运维自行托管。
```

最强的两列：**护栏**（均值 4）与 **缰绳**（均值 3.3）。最弱的一列：**梳理**（均值 2.3）。这个分布与一个偏研究倾向的开源项目很一致——关卡和上下文做得出色，反复发生的维护则留给运维去做。

## 07.5 —— 哪些值得拷贝，哪些应该跳过

- **值得拷。** 那种分成十个子系统的目录切法、Agent Loop 的形状（{cite}`yao2022react`）、`permissions/` 下"以代码表达的权限"、以及 `sandbox/` 下的沙箱隔离。
- **可以跳过**（或当作脚手架处理）。`channels/impl/` 里那十一个通道适配器——它们本身很有价值，但不是 *马具核心* 的一部分；想为另一个产品造马具的读者，可以在第一天就删掉 `channels/` 目录，方法论上不会丢失任何东西。

### OpenHarness *不* 适合被当作哪些事的范本

一个案例研究一旦变成圣人传记，它的教学价值就没了；OpenHarness 有三处短板值得点名，方便读者只拷它的优点、不把它的盲区一起拷走。

- **梳理被留给了运维。** 07.4 里梳理列 2.3 的均值是诚实的信号：这个项目交付的是一台引擎和一台沙箱，而不是一套维护纪律。若一支团队把 OpenHarness 整套搬进来，不加上自己的每周审计、自己的 doc-sync 检查、自己的 HarnessCard 节奏，那这具马具的衰减速度会和任何一份没人照料的仓库一样——第 06 章的那份熵关切，*不会* 由这个框架替你提供。
- **没有宣布过一条北极星度量。** 07.4 给 MDD × 缰绳 的打分是 3（*"事件流存在，但没有一条被正式宣布的北极星"*）。第 04 章的警告在这里适用：一具没有人持有、没有阈值看护的北极星的马具，会收集一堆 dashboard，却哪一块都引导不了。OpenHarness 给的是原料，宣布度量这件事是你的职责。
- **43 个工具的表面是把双刃剑。** 一个丰富的工具面，会降低造一个智能体的成本，但会提高 *推理"这个智能体能做什么"* 的成本。若一支团队不做裁剪就把全部 43 个工具上到生产，等于默默接受了 43 个攻击面、43 个成本中心、以及 43 处 schema 漂移可能会悄悄打断东西的位置。Harness Engineering 的打法是：先采用一个小子集，按需扩宽。

```{admonition} 陷阱——把目录结构当作 cargo cult
:class: warning

一支团队读了 07.1，在自己仓库里照 OpenHarness 的名字建了十个顶级目录——`autopilot/`、`channels/`、`coordinator/` 等等——然后把这副骨架上线了。六周之后，这些目录要么是空的（因为这个团队的产品不需要 coordinator），要么塞了一堆弯弯绕的胶水代码（因为这个团队的 coordinator 映射不到 OpenHarness 的那层抽象上）。**为什么**：十个子系统的布局，是 OpenHarness 所处问题域（多通道、长期运行的智能体服务）的 *涌现* 属性；把它套到一个不同的问题上，等于把 Conway 律 {cite}`conway1968law` 反着用一次。**解法**：把 *原理*（以代码表达的权限、沙箱隔离、可审计的 agent loop）拷进你产品真正需要的那种目录结构里。马具是一副契合特定负载的形状；借走那种 *思维模式*，而不是文件名清单。
```

## HarnessCard

```{list-table}
:header-rows: 1
:widths: 35 65

* - 字段
  - 值
* - HarnessCard schema 版本
  - CAR-HarnessCard v0.2 {cite}`car2025decomposition`
* - 对象
  - OpenHarness，2026-03 快照 {cite}`hkuds2025openharness`
* - 许可证
  - MIT（代码）、CC-BY-4.0（文档）
* - Control 层（CAR）
  - 有明显主张；`coordinator/agent_definitions.py` ＋ `prompts/` 设定了强默认值。
* - Agency 层（CAR）
  - 43 个工具，后面由显式权限和一只 Docker 沙箱看着。
* - Runtime 层（CAR）
  - Python 3.11，基于 Docker 的沙箱，可插拔的 LLM 后端。
* - SDD（0–5，Bridle／Fence／Paddock／Groom 的均值）
  - 3.5
* - TDD（0–5）
  - 3.0
* - MDD（0–5）
  - 3.0
* - 主要引用
  - {cite}`hkuds2025openharness`
```

## 研究脉络

- **ReAct** {cite}`yao2022react` —— OpenHarness 核心那具 Agent Loop 的学术谱系。
- **Toolformer** {cite}`schick2023toolformer` —— "把工具使用当作首要动作平面的一等事物"这一思路的学术谱系。
- **MCP 规范** {cite}`anthropic2024mcp` —— 让 OpenHarness 不用自己写胶水就能接入第三方工具生态的那份行业规范。
- **上游 OpenHarness 的 README** {cite}`hkuds2025openharness` —— 关于"仓库里交付了什么、在什么许可证下"的权威记录；全书作为一手来源引用。
- **Anthropic 的 Claude Code 发布博客** {cite}`anthropic2024claudecode` —— OpenHarness 在与之对位时所处的行业语境。

## 动手环节

在 `source/_handson/07-openharness/` 下，住着两份可直接拷走的制品：

- `quickstart.sh` —— 克隆 → 安装 → 跑一轮验证会话。
- `custom-tool.py` —— 一份最小可用的"添加一个自定义工具"示例，改编自上游文档，并附署名。
