"""One-shot translator for Ch.07 OpenHarness."""
import polib

PATH = 'source/locale/zh_CN/LC_MESSAGES/chapters/07-openharness.po'
T = {}

T['Case Study: OpenHarness'] = '案例研究：OpenHarness'

T['*The closest thing to a textbook harness that ships as open source.*'] = \
    '*开源世界里，最接近"教科书级挽具"的那一具。*'

T['OpenHarness, authored by the HKU Data Science Lab (HKUDS) and released as MIT-licensed open source {cite}`hkuds2025openharness`, is the reference implementation the book returns to most often. It reads as if its authors had already written Chapter 05: the repository is neatly divided into ten subsystems, each of which maps onto a specific cell or small cluster of cells in the three-guardian × four-zone matrix. This chapter walks through those subsystems, quotes the Agent Loop core, and scores the whole project against the Ch.05 matrix.'] = \
    'OpenHarness 由香港大学数据科学实验室（HKUDS）编写，以 MIT 许可开源发布 {cite}`hkuds2025openharness`。它是本书最常回头引用的那份参考实现。读它的感觉，就像作者们已经先写过第 05 章：仓库整齐地分成十个子系统，每一个都刚好对应到"三护法 × 四区域"矩阵里的某一格、或某一小簇格子。本章逐个走过这些子系统、引用 Agent Loop 核心那一小段代码，并给整个项目按第 05 章的矩阵打一次分。'

T['§07.1 — Ten subsystems at a glance'] = '§07.1 —— 一眼看清十个子系统'

T['OpenHarness as of the 2026-03 snapshot is organised around ten subsystems that roughly correspond to the ten directories under `src/openharness/` in the upstream tree:'] = \
    '以 2026-03 的快照为准，OpenHarness 围绕十个子系统组织，大致对应上游仓库 `src/openharness/` 下面的十个目录：'

T['`api/` — OpenAI-compatible clients and Copilot auth adapters.'] = \
    '`api/` —— OpenAI 兼容的客户端，以及 Copilot 认证适配器。'
T["`autopilot/` — the long-running agent service that the book's Chapter 02 stage-4 example alludes to."] = \
    '`autopilot/` —— 那个长期运行的智能体服务，本书第 02 章第 4 阶段的例子就隐指它。'
T['`channels/` — integrations with Slack, Discord, Feishu, Telegram, and eight more messaging surfaces.'] = \
    '`channels/` —— 与 Slack、Discord、飞书、Telegram 以及另外八个消息面的集成。'
T['`config/` — schema + settings + path helpers; a textbook SDD × Fence.'] = \
    '`config/` —— schema、settings、路径助手；教科书式的 SDD × 护栏。'
T['`coordinator/` — agent-definition registry.'] = \
    '`coordinator/` —— 智能体定义的注册表。'
T['`engine/` — the Agent Loop itself (see §07.2 below).'] = \
    '`engine/` —— Agent Loop 本身（见下文 §07.2）。'
T['`hooks/` — event bus powering the hook-driven fence.'] = \
    '`hooks/` —— 事件总线，驱动那道以 hook 为核心的护栏。'
T['`mcp/` — MCP client wiring; the channel for tool use.'] = \
    '`mcp/` —— MCP 客户端接线；工具使用的那条通道。'
T['`memory/` — conversation memory manager.'] = \
    '`memory/` —— 会话记忆管理器。'
T['`sandbox/` — Docker-backed execution isolation; a Runtime-layer paddock.'] = \
    '`sandbox/` —— 基于 Docker 的执行隔离；Runtime 层的牧场。'

T['A reader who wanted to verify every claim in this chapter would `ls src/openharness/` in a fresh clone of [`HKUDS/OpenHarness`](https://github.com/HKUDS/OpenHarness) and see the same ten names. The taxonomy is extracted *from the code*, not imposed on it.'] = \
    '想逐条核对本章说法的读者，可以在一份全新的 [`HKUDS/OpenHarness`](https://github.com/HKUDS/OpenHarness) 克隆里 `ls src/openharness/`，会看到同样这十个名字。这份分类学是 *从代码里抽取出来* 的，不是外部强加上去的。'

T['§07.2 — The Agent Loop (≤ 20 lines, MIT-attributed)'] = '§07.2 —— Agent Loop（不超过 20 行，MIT 署名）'

T["The heart of any harness is its agent loop. OpenHarness's `engine/query_engine.py` compresses the ReAct-style loop {cite}`yao2022react` into a form that is easy to audit and easy to instrument. The shape of the loop — slightly shortened here for exposition — is:"] = \
    '任何一具挽具的核心，都是它的 agent loop。OpenHarness 的 `engine/query_engine.py` 把 ReAct 式循环 {cite}`yao2022react` 压缩成一种既便于审计、也便于埋点的形态。为便于讲解，这里略作删节：'

code_18 = '''# Adapted from OpenHarness/src/openharness/engine/query_engine.py
# MIT License, Copyright (c) 2025 HKUDS.
def step(self, state):
    messages = self.memory.window(state)
    plan = self.model.complete(messages, tools=self.tools.schemas())
    if plan.tool_calls:
        outputs = [self.tools.invoke(c) for c in plan.tool_calls]
        state = self.memory.extend(state, plan, outputs)
        return state, "continue"
    return self.memory.extend(state, plan, []), "halt"
'''
T[code_18] = code_18

T['What matters for the book\'s argument is not the ≤ 20 lines themselves but the three decisions they encode: (a) the model emits tool-calls as first-class structured output rather than free-form text; (b) the memory manager owns the context-window policy; (c) the loop *explicitly distinguishes* "continue" from "halt" states. All three decisions are visible to the human reviewer, which is what makes this harness auditable.'] = \
    '对本书的论点而言，重要的不是这不到二十行本身，而是它们把三项决定编码了进去：(a) 模型把工具调用当作一等结构化输出发出，而不是自由文本；(b) 记忆管理器 *持有* 上下文窗口策略；(c) 这个循环 *显式地* 把"continue"和"halt"两种状态分开。这三项决定，对人类评审者都是 *可见* 的——而正是这份可见性，让这具挽具可以被审计。'

T['§07.3 — The 43-tool taxonomy (Toolformer-style)'] = '§07.3 —— 43 个工具的分类（Toolformer 风格）'

T['OpenHarness ships 43 first-party tools at the 2026-03 snapshot {cite}`hkuds2025openharness`. A partial grouping:'] = \
    '在 2026-03 的快照里，OpenHarness 自带 43 个一方工具 {cite}`hkuds2025openharness`。部分分组如下：'

T['Group'] = '分组'
T['Count'] = '数量'
T['Examples'] = '例子'
T['File & code navigation'] = '文件与代码浏览'
T['9'] = '9'
T['`read_file`, `grep`, `list_dir`, `semantic_search`'] = '`read_file`、`grep`、`list_dir`、`semantic_search`'
T['Editing'] = '编辑'
T['6'] = '6'
T['`write_file`, `str_replace`, `apply_patch`, `delete_file`'] = '`write_file`、`str_replace`、`apply_patch`、`delete_file`'
T['Shell & process'] = 'Shell 与进程'
T['5'] = '5'
T['`run_command`, `await_job`, `tail_terminal`, `kill_job`, `cat_terminal`'] = '`run_command`、`await_job`、`tail_terminal`、`kill_job`、`cat_terminal`'
T['VCS'] = 'VCS'
T['4'] = '4'
T['`git_status`, `git_diff`, `git_commit`, `git_log`'] = '`git_status`、`git_diff`、`git_commit`、`git_log`'
T['Web & fetch'] = 'Web 与抓取'
T['3'] = '3'
T['`web_search`, `web_fetch`, `read_lints`'] = '`web_search`、`web_fetch`、`read_lints`'
T['MCP client'] = 'MCP 客户端'
T['`mcp_call`, `mcp_fetch_resource`, `mcp_list_resources`'] = '`mcp_call`、`mcp_fetch_resource`、`mcp_list_resources`'
T['Miscellaneous'] = '其他杂项'
T['13'] = '13'
T['memory, sandbox, channel, notebook, and helper tools'] = '记忆、sandbox、channel、notebook 及各类辅助工具'

T['The grouping makes a Toolformer-style {cite}`schick2023toolformer` argument concrete: the tools are not an afterthought, they are the primary surface the agent acts through. The MCP specification {cite}`anthropic2024mcp` extends this surface to third-party tools.'] = \
    '这份分组，把 Toolformer 式的论点 {cite}`schick2023toolformer` 做成了具体的东西：工具不是事后补上的附属品，它们是智能体 *行动* 所经过的首要平面。MCP 规范 {cite}`anthropic2024mcp` 把这个面进一步延伸到了第三方工具。'

T['§07.4 — 12-cell highlight map'] = '§07.4 —— 十二格亮点图'

T['Every case-study chapter in the book scores the harness against the twelve Ch.05 cells on a 0–5 scale, with 1–3 sentences of evidence citing specific files under `oss/OpenHarness/`.'] = \
    '本书的每一章案例研究，都会按第 05 章的十二格、以 0–5 分制给挽具打分，并用 1–3 句话、引用 `oss/OpenHarness/` 下的具体文件作为证据。'

T['Cell'] = '格子'
T['Score'] = '得分'
T['Evidence'] = '证据'

T['SDD × Bridle'] = 'SDD × 缰绳'
T['`README.md`, `src/openharness/prompts/system_prompt.py` and the `openharness/prompts/context.py` bundle steer agent behaviour.'] = \
    '`README.md`、`src/openharness/prompts/system_prompt.py`，以及 `openharness/prompts/context.py` 打包在一起引导智能体的行为。'
T['SDD × Fence'] = 'SDD × 护栏'
T['`config/schema.py` + `config/settings.py` validate every launch-time config; bad config aborts the process.'] = \
    '`config/schema.py` ＋ `config/settings.py` 校验每一次启动时的配置；坏配置直接让进程终止。'
T['SDD × Paddock'] = 'SDD × 牧场'
T['No explicit acceptance-table pattern; review relies on upstream PR review + the `autopilot/service.py` state machine.'] = \
    '没有显式的验收表模式；评审依赖上游的 PR review，加上 `autopilot/service.py` 的状态机。'
T['SDD × Groom'] = 'SDD × 梳理'
T['`plugins/loader.py` and `commands/registry.py` refresh in-process registries but living-doc grooming is ad-hoc.'] = \
    '`plugins/loader.py` 和 `commands/registry.py` 会刷新进程内注册表，但对"活文档"的梳理是临时性的。'
T['TDD × Bridle'] = 'TDD × 缰绳'
T['Upstream test suite under `tests/` is substantial but not committed-red-first; agent context does not read tests by default.'] = \
    '`tests/` 下上游测试套件分量很足，但不是"先 commit 为红"那种模式；智能体的上下文默认不会读测试。'
T['TDD × Fence'] = 'TDD × 护栏'
T['`sandbox/adapter.py` + `sandbox/docker_backend.py` refuse code execution outside Docker; `permissions/checker.py` refuses tool calls by policy.'] = \
    '`sandbox/adapter.py` ＋ `sandbox/docker_backend.py` 拒绝任何 Docker 之外的代码执行；`permissions/checker.py` 按策略拒绝工具调用。'
T['TDD × Paddock'] = 'TDD × 牧场'
T['CI runs `pytest` on PR; no fault-injection or adversarial suite.'] = \
    'CI 会在 PR 上跑 `pytest`；没有故障注入或敌意测试套件。'
T['TDD × Groom'] = 'TDD × 梳理'
T['2'] = '2'
T['No published flaky-test quarantine; upstream triage is manual.'] = \
    '没有公开的 flaky 测试隔离区；上游的分诊是人工的。'
T['MDD × Bridle'] = 'MDD × 缰绳'
T['`engine/stream_events.py` and `services/__init__.py` expose event streams — a good *potential* north-star but not a declared one.'] = \
    '`engine/stream_events.py` 与 `services/__init__.py` 暴露了事件流——这是一个不错的 *潜在* 北极星，但未被正式宣布。'
T['MDD × Fence'] = 'MDD × 护栏'
T['`permissions/checker.py` + `sandbox/path_validator.py` are cost and blast-radius caps implemented as code.'] = \
    '`permissions/checker.py` ＋ `sandbox/path_validator.py` 作为代码实现的成本上限与爆炸半径上限。'
T['MDD × Paddock'] = 'MDD × 牧场'
T['Release staging exists (tag + changelog); no public SLI gate.'] = \
    '有发布 staging（tag + changelog）；没有公开的 SLI 关卡。'
T['MDD × Groom'] = 'MDD × 梳理'
T['No public weekly-audit script; dashboards are self-hosted by ops who deploy OpenHarness.'] = \
    '没有公开的每周审计脚本；dashboard 由部署 OpenHarness 的运维自行托管。'

T['Strongest columns: **Fence** (mean 4) and **Bridle** (mean 3.3). Weakest column: **Groom** (mean 2.3). The pattern is consistent with a research-leaning open-source project: gates and context are excellent, recurring maintenance is left to the operator.'] = \
    '最强的两列：**护栏**（均值 4）与 **缰绳**（均值 3.3）。最弱的一列：**梳理**（均值 2.3）。这个分布与一个偏研究倾向的开源项目很一致——关卡和上下文做得出色，反复发生的维护则留给运维去做。'

T['§07.5 — What to copy, what to skip'] = '§07.5 —— 哪些值得拷贝，哪些应该跳过'

T['**Copy.** The 10-subsystem directory split, the Agent Loop shape ({cite}`yao2022react`), the permissions-as-code in `permissions/`, and the sandbox isolation in `sandbox/`.'] = \
    '**值得拷。** 那种分成十个子系统的目录切法、Agent Loop 的形状（{cite}`yao2022react`）、`permissions/` 下"以代码表达的权限"、以及 `sandbox/` 下的沙箱隔离。'

T["**Skip** (or treat as scaffolding). The eleven channel adapters in `channels/impl/` — they are valuable in their own right but they are not part of the *harness core*; a reader trying to build a harness for a different product can delete the `channels/` directory on day one and lose nothing methodological."] = \
    '**可以跳过**（或当作脚手架处理）。`channels/impl/` 里那十一个通道适配器——它们本身很有价值，但不是 *挽具核心* 的一部分；想为另一个产品造挽具的读者，可以在第一天就删掉 `channels/` 目录，方法论上不会丢失任何东西。'

T['What OpenHarness is *not* a model of'] = 'OpenHarness *不* 适合被当作哪些事的范本'

T['A case study loses its teaching value the moment it becomes hagiography; three OpenHarness weaknesses deserve naming so the reader copies its strengths without the blind spots.'] = \
    '一个案例研究一旦变成圣人传记，它的教学价值就没了；OpenHarness 有三处短板值得点名，方便读者只拷它的优点、不把它的盲区一起拷走。'

T["**Grooming is left to the operator.** The `Groom` column's 2.3 mean score in §07.4 is the honest signal: the project ships an engine and a sandbox, not a maintenance discipline. A team adopting OpenHarness wholesale without adding its own weekly audit, its own doc-sync check, and its own HarnessCard cadence will find the harness decays at the same rate as any other unattended repository — Ch.06's entropy concern is *not* supplied by the framework."] = \
    '**梳理被留给了运维。** §07.4 里梳理列 2.3 的均值是诚实的信号：这个项目交付的是一台引擎和一台沙箱，而不是一套维护纪律。若一支团队把 OpenHarness 整套搬进来，不加上自己的每周审计、自己的 doc-sync 检查、自己的 HarnessCard 节奏，那这具挽具的衰减速度会和任何一份没人照料的仓库一样——第 06 章的那份熵关切，*不会* 由这个框架替你提供。'

T['**No north-star metric is declared.** §07.4 scores MDD × Bridle at 3 (*"event streams exist, not a declared north-star"*). The Chapter 04 warning applies: a harness without an owned, threshold-gated north- star will collect dashboards and steer by none of them. OpenHarness gives you the raw material; declaring the metric is your job.'] = \
    '**没有宣布过一条北极星度量。** §07.4 给 MDD × 缰绳 的打分是 3（*"事件流存在，但没有一条被正式宣布的北极星"*）。第 04 章的警告在这里适用：一具没有人持有、没有阈值看护的北极星的挽具，会收集一堆 dashboard，却哪一块都引导不了。OpenHarness 给的是原料，宣布度量这件事是你的职责。'

T['**The 43-tool surface is a double-edged gift.** A rich tool surface lowers the cost of building an agent but raises the cost of *reasoning about what the agent can do*. A team that ships all 43 tools into production without pruning has implicitly accepted 43 attack surfaces, 43 cost centres, and 43 places where a schema drift would silently break something. The harness engineering move is to adopt a small subset first and widen it by demand.'] = \
    '**43 个工具的表面是把双刃剑。** 一个丰富的工具面，会降低造一个智能体的成本，但会提高 *推理"这个智能体能做什么"* 的成本。若一支团队不做裁剪就把全部 43 个工具上到生产，等于默默接受了 43 个攻击面、43 个成本中心、以及 43 处 schema 漂移可能会悄悄打断东西的位置。Harness Engineering 的打法是：先采用一个小子集，按需扩宽。'

T['Pitfall — Cargo-culting the directory layout'] = '陷阱——把目录结构当作 cargo cult'

T["A team reads §07.1, creates ten top-level directories in their own repo matching OpenHarness's names — `autopilot/`, `channels/`, `coordinator/`, etc. — and ships the skeleton. Six weeks later the directories contain either nothing (because the team's product does not need a coordinator) or convoluted glue code (because the team's coordinator does not map onto OpenHarness's abstraction). **Why**: the ten-subsystem layout is an *emergent* property of OpenHarness's problem space (multi-channel long-running agent service); imposing it on a different problem is Conway's law {cite}`conway1968law` applied in reverse. **Fix**: copy the *principles* (permissions as code, sandbox isolation, auditable agent loop) into whatever directory structure your product actually needs. A harness is a shape that fits a specific load; borrow the pattern of thought, not the filename list."] = \
    '一支团队读了 §07.1，在自己仓库里照 OpenHarness 的名字建了十个顶级目录——`autopilot/`、`channels/`、`coordinator/` 等等——然后把这副骨架上线了。六周之后，这些目录要么是空的（因为这个团队的产品不需要 coordinator），要么塞了一堆弯弯绕的胶水代码（因为这个团队的 coordinator 映射不到 OpenHarness 的那层抽象上）。**为什么**：十个子系统的布局，是 OpenHarness 所处问题域（多通道、长期运行的智能体服务）的 *涌现* 属性；把它套到一个不同的问题上，等于把 Conway 律 {cite}`conway1968law` 反着用一次。**解法**：把 *原理*（以代码表达的权限、沙箱隔离、可审计的 agent loop）拷进你产品真正需要的那种目录结构里。挽具是一副契合特定负载的形状；借走那种 *思维模式*，而不是文件名清单。'

T['HarnessCard'] = 'HarnessCard'
T['Field'] = '字段'
T['Value'] = '值'
T['HarnessCard schema version'] = 'HarnessCard schema 版本'
T['CAR-HarnessCard v0.2 {cite}`car2025decomposition`'] = 'CAR-HarnessCard v0.2 {cite}`car2025decomposition`'
T['Subject'] = '对象'
T['OpenHarness, 2026-03 snapshot {cite}`hkuds2025openharness`'] = 'OpenHarness，2026-03 快照 {cite}`hkuds2025openharness`'
T['License'] = '许可证'
T['MIT (code), CC-BY-4.0 (docs)'] = 'MIT（代码）、CC-BY-4.0（文档）'
T['Control layer (CAR)'] = 'Control 层（CAR）'
T['Opinionated; `coordinator/agent_definitions.py` + `prompts/` set strong defaults.'] = \
    '有明显主张；`coordinator/agent_definitions.py` ＋ `prompts/` 设定了强默认值。'
T['Agency layer (CAR)'] = 'Agency 层（CAR）'
T['43 tools behind explicit permissions and a Docker sandbox.'] = \
    '43 个工具，后面由显式权限和一只 Docker 沙箱看着。'
T['Runtime layer (CAR)'] = 'Runtime 层（CAR）'
T['Python 3.11, Docker-backed sandbox, pluggable LLM backends.'] = \
    'Python 3.11，基于 Docker 的沙箱，可插拔的 LLM 后端。'
T['SDD (0–5, mean of Bridle/Fence/Paddock/Groom)'] = 'SDD（0–5，Bridle／Fence／Paddock／Groom 的均值）'
T['3.5'] = '3.5'
T['TDD (0–5)'] = 'TDD（0–5）'
T['3.0'] = '3.0'
T['MDD (0–5)'] = 'MDD（0–5）'
T['Primary citation'] = '主要引用'
T['{cite}`hkuds2025openharness`'] = '{cite}`hkuds2025openharness`'

T['Research Foundations'] = '研究脉络'

T['**ReAct** {cite}`yao2022react` — the academic lineage of the Agent Loop at the heart of OpenHarness.'] = \
    '**ReAct** {cite}`yao2022react` —— OpenHarness 核心那具 Agent Loop 的学术谱系。'
T['**Toolformer** {cite}`schick2023toolformer` — the academic lineage for first-class tool use as a primary action surface.'] = \
    '**Toolformer** {cite}`schick2023toolformer` —— "把工具使用当作首要动作平面的一等事物"这一思路的学术谱系。'
T['**MCP specification** {cite}`anthropic2024mcp` — the industry specification that lets OpenHarness plug into third-party tool ecosystems without bespoke glue.'] = \
    '**MCP 规范** {cite}`anthropic2024mcp` —— 让 OpenHarness 不用自己写胶水就能接入第三方工具生态的那份行业规范。'
T['**Upstream OpenHarness README** {cite}`hkuds2025openharness` — the canonical record of what ships in the repository and under what license; cited as primary source throughout.'] = \
    '**上游 OpenHarness 的 README** {cite}`hkuds2025openharness` —— 关于"仓库里交付了什么、在什么许可证下"的权威记录；全书作为一手来源引用。'
T['**Anthropic Claude Code launch post** {cite}`anthropic2024claudecode` — the industry context OpenHarness positions itself against.'] = \
    '**Anthropic 的 Claude Code 发布博客** {cite}`anthropic2024claudecode` —— OpenHarness 在与之对位时所处的行业语境。'

T['Hands-On'] = '动手环节'

T['Two copyable artefacts live under `book/source/_handson/07-openharness/`:'] = \
    '在 `book/source/_handson/07-openharness/` 下，住着两份可直接拷走的制品：'
T['`quickstart.sh` — clone → install → run one verification session.'] = \
    '`quickstart.sh` —— 克隆 → 安装 → 跑一轮验证会话。'
T['`custom-tool.py` — a minimum-viable "Add a Custom Tool" example adapted from upstream docs with attribution.'] = \
    '`custom-tool.py` —— 一份最小可用的"添加一个自定义工具"示例，改编自上游文档，并附署名。'


def main():
    po = polib.pofile(PATH)
    hit = 0
    miss = []
    for e in po:
        if not e.msgstr and not e.obsolete:
            if e.msgid in T:
                e.msgstr = T[e.msgid]
                hit += 1
            else:
                miss.append(e.msgid)
    po.save(PATH)
    print(f'translated {hit}; misses {len(miss)}')
    for m in miss[:10]:
        print('  MISS:', repr(m[:160]))

    po2 = polib.pofile(PATH)
    remaining = [e for e in po2 if not e.msgstr and not e.obsolete]
    print(f'remaining: {len(remaining)}')


if __name__ == '__main__':
    main()
