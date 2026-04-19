"""One-shot translator for Ch.08 Superpowers."""
import polib

PATH = 'source/locale/zh_CN/LC_MESSAGES/chapters/08-superpowers.po'
T = {}

T['Case Study: Superpowers'] = '案例研究：Superpowers'

T['*Not a framework. Not a platform. A library of skills that teach the agent how to think twice before it writes.*'] = \
    '*不是框架，不是平台。是一整套技能（skills），教智能体在动笔之前先想两遍。*'

T['Superpowers, authored by Joseph Vincent and released as open source under the `obra/superpowers` repository {cite}`vincent2025superpowers,vincent2025superpowersrepo`, is the philosophical opposite of OpenHarness: where OpenHarness ships a runtime and a sandbox, Superpowers ships *only* a set of `SKILL.md` files that structure *how* an agent (specifically, Claude Code) frames its own work. The whole project is essentially three dozen markdown files. That is the point.'] = \
    'Superpowers 由 Joseph Vincent 编写，以 `obra/superpowers` 仓库开源发布 {cite}`vincent2025superpowers,vincent2025superpowersrepo`。它在哲学上是 OpenHarness 的反面：OpenHarness 交付的是运行时和沙箱，Superpowers 交付的 *只是* 一组 `SKILL.md` 文件，用来塑造一个智能体（具体说是 Claude Code）"如何框自己的工作"。整个项目本质上就是三十来份 markdown 文件——这本身，就是它的论点。'

T['§08.1 — Skills-first workflow'] = '§08.1 —— 以技能为先的工作流'

T['The canonical Superpowers workflow is a five-step arc:'] = \
    'Superpowers 的经典工作流是一条五步弧：'

T['**Brainstorming** (`skills/brainstorming/SKILL.md`) — refuse to implement until intent is clarified.'] = \
    '**头脑风暴**（`skills/brainstorming/SKILL.md`）—— 在意图被澄清之前，拒绝开始实现。'
T['**Writing plans** (`skills/writing-plans/SKILL.md`) — compile the brainstorm into a written plan with review checkpoints.'] = \
    '**写计划**（`skills/writing-plans/SKILL.md`）—— 把头脑风暴编译成一份带评审节点的书面计划。'
T['**Test-driven development** (`skills/test-driven-development/SKILL.md`) — implement only against a failing test.'] = \
    '**测试驱动开发**（`skills/test-driven-development/SKILL.md`）—— 只对着一条失败的测试来实现。'
T['**Code review** (`skills/requesting-code-review/SKILL.md`) — explicit review with named rubric before merging.'] = \
    '**代码评审**（`skills/requesting-code-review/SKILL.md`）—— 合并之前，进行一次带有明确评价细则的显式评审。'
T['**Finishing** (`skills/finishing-a-development-branch/SKILL.md`) — integration, cleanup, PR.'] = \
    '**收尾**（`skills/finishing-a-development-branch/SKILL.md`）—— 集成、清理、提 PR。'

T["Each step is a skill the agent opts into (or is nudged into) via the `using-superpowers` meta-skill. Anthropic's skills documentation {cite}`anthropic2024skills` describes the mechanism; Superpowers is the most complete public library of skills authored against it."] = \
    '每一步都是智能体通过 `using-superpowers` 这条元技能 *选择* 进入（或被 *推* 进入）的一项技能。Anthropic 的 skills 文档 {cite}`anthropic2024skills` 描述了这套机制；Superpowers 是迄今为止、针对这套机制最完整的公开技能库。'

T['§08.2 — A representative skill (≤ 20 lines)'] = '§08.2 —— 一条代表性的技能（不超过 20 行）'

T['The `test-driven-development/SKILL.md` file is the load-bearing one; it is also the shortest. The excerpt below reproduces its core (with ellipses marking omitted prose) and is quoted under the upstream licence:'] = \
    '`test-driven-development/SKILL.md` 是承重的那一份，同时也是最短的一份。下面摘录了它的核心（用省略号标出省略的散文），并在上游许可证下引用：'

code_13 = '''# Test-Driven Development

## When to use

Use when implementing any feature or bugfix, before writing implementation code.

## What this skill does

1. Writes a failing test that captures the requirement.
2. Runs the test suite and confirms only this test fails.
3. Implements the minimum code to make the test pass.
4. Refactors while the test stays green.

## Red flags that stop this skill

- "I'll write the test after." — no. The skill exits.
- A passing first test — suspect; re-read the requirement.
'''
T[code_13] = code_13

T["This is a skill file, *not* a code module — the agent's behaviour is changed by reading prose, not by invoking an API. Mills' Socratic design essay {cite}`mills2015socratic` and Zeller's systematic debugging {cite}`zeller2009whyprogramsfail` are the intellectual ancestors: the skill asks the agent to interrogate itself before committing to action."] = \
    '这是一份技能文件，*不是* 一个代码模块——智能体的行为是靠读散文被改变的，而不是靠调用 API。Mills 的 Socratic design 论文 {cite}`mills2015socratic`、以及 Zeller 的系统性调试 {cite}`zeller2009whyprogramsfail`，是这类做法的思想先人：技能要求智能体在提交行动之前，先审问自己。'

T['§08.3 — OpenHarness vs Superpowers: complementary, not competing'] = '§08.3 —— OpenHarness vs Superpowers：互补，不是竞争'

T['OpenHarness provides the *engine*; Superpowers provides the *discipline*. A production harness usually wants both. The two projects differ along three axes worth making explicit for a reader choosing between them:'] = \
    'OpenHarness 提供的是 *引擎*；Superpowers 提供的是 *纪律*。一具生产级挽具通常两样都要。这两个项目沿着三条轴彼此不同，对于要在二者之间做取舍的读者，有必要把这三条轴显式列出：'

T['Axis'] = '轴'
T['OpenHarness'] = 'OpenHarness'
T['Superpowers'] = 'Superpowers'
T['Primary artefact'] = '首要制品'
T['Python package + Docker sandbox'] = 'Python 包 ＋ Docker 沙箱'
T['`~/.claude/skills/**/SKILL.md` markdown files'] = '`~/.claude/skills/**/SKILL.md` 这些 markdown 文件'
T['Guardian emphasis'] = '护法侧重'
T['TDD × Fence, MDD × Fence (via permissions, sandbox)'] = 'TDD × 护栏、MDD × 护栏（通过权限、沙箱）'
T['SDD × Bridle, TDD × Bridle (via skill invocations)'] = 'SDD × 缰绳、TDD × 缰绳（通过技能的被调用）'
T['Adoption cost'] = '采用成本'
T['High — new dependency, new runtime'] = '高——新依赖、新运行时'
T['Low — copy markdown into `~/.claude/skills/`'] = '低——把 markdown 拷进 `~/.claude/skills/` 就完'

T['§08.4 — 12-cell highlight map'] = '§08.4 —— 十二格亮点图'

T['Cell'] = '格子'
T['Score'] = '得分'
T['Evidence'] = '证据'

T['SDD × Bridle'] = 'SDD × 缰绳'
T['5'] = '5'
T["Entire project exists to strengthen this cell; `using-superpowers/SKILL.md` + ~30 sibling skills directly shape the agent's pre-edit context."] = \
    '整个项目的存在，就是为了强化这一格；`using-superpowers/SKILL.md` 加上约 30 条兄弟技能，直接塑造智能体动笔之前的上下文。'

T['SDD × Fence'] = 'SDD × 护栏'
T['2'] = '2'
T['Skills are prose; no schema validator for skill front-matter.'] = \
    '技能是散文；针对技能 front-matter 没有 schema 校验器。'

T['SDD × Paddock'] = 'SDD × 牧场'
T['4'] = '4'
T['`requesting-code-review/SKILL.md` + `receiving-code-review/SKILL.md` are role-scoped acceptance gates.'] = \
    '`requesting-code-review/SKILL.md` ＋ `receiving-code-review/SKILL.md` 构成按角色划定的验收关卡。'

T['SDD × Groom'] = 'SDD × 梳理'
T['3'] = '3'
T['`finishing-a-development-branch/SKILL.md` and the brainstorm-to-plan chain keep skills themselves fresh.'] = \
    '`finishing-a-development-branch/SKILL.md` 以及"头脑风暴 → 计划"那条链，本身就在让技能保持新鲜。'

T['TDD × Bridle'] = 'TDD × 缰绳'
T['`test-driven-development/SKILL.md` is load-bearing across the entire library.'] = \
    '`test-driven-development/SKILL.md` 在整个技能库里承重。'

T['TDD × Fence'] = 'TDD × 护栏'
T['Skill prose refuses to proceed on red tests; actual enforcement still relies on Claude Code hooks at the host repo.'] = \
    '技能里的散文在测试为红时拒绝继续；真正的执行层面，仍然依赖宿主仓库的 Claude Code hook。'

T['TDD × Paddock'] = 'TDD × 牧场'
T['No integration suite shipped by Superpowers itself.'] = \
    'Superpowers 自身不附带集成测试套件。'

T['TDD × Groom'] = 'TDD × 梳理'
T['Flaky-test policy not defined at library level.'] = \
    'flaky 测试的处置策略，在技能库层面并未定义。'

T['MDD × Bridle'] = 'MDD × 缰绳'
T['No north-star metric in the library.'] = \
    '技能库里没有一条北极星度量。'

T['MDD × Fence'] = 'MDD × 护栏'
T['1'] = '1'
T['No cost cap, no rate limit, no circuit breaker.'] = \
    '没有成本上限，没有限流，没有熔断。'

T['MDD × Paddock'] = 'MDD × 牧场'
T['No release SLIs (library is stateless markdown).'] = \
    '没有发布 SLI（这个库是一份无状态的 markdown）。'

T['MDD × Groom'] = 'MDD × 梳理'
T['Weekly audit not defined; upstream changelog captures drift.'] = \
    '没有定义每周审计；漂移由上游 changelog 捕捉。'

T['Strongest column: **Bridle** (mean 4.25). Weakest column: **MDD row** (mean 1.5). Superpowers leans all the way into SDD / TDD × Bridle, which is consistent with its purpose — it is a skill library, not a runtime.'] = \
    '最强的一列：**缰绳**（均值 4.25）。最弱的一条：**MDD 整行**（均值 1.5）。Superpowers 一整个往 SDD／TDD × 缰绳 那侧倾斜，这与它的目的一致——它是一个技能库，不是一套运行时。'

T['§08.5 — When to reach for Superpowers'] = '§08.5 —— 什么时候该抄起 Superpowers'

T['Your team already runs Claude Code and wants stronger pre-edit discipline without shipping a new platform.'] = \
    '你的团队已经在用 Claude Code，想要更强的"动笔前纪律"，又不想额外上一个新平台。'
T['You have a `CLAUDE.md` but notice agents still skip tests; the TDD skill will help.'] = \
    '你已经有一份 `CLAUDE.md`，但留意到智能体仍然跳过测试；TDD 技能能帮上忙。'
T["You want a review ritual that applies to *both* the agent's output and the human's; the code-review skills cover both."] = \
    '你想要一套评审仪式，*同时* 作用在智能体的产出和人类的产出上；code-review 系列技能两头都覆盖。'

T["*Don't* reach for Superpowers if you need runtime isolation (reach for OpenHarness or Claude Code's hooks + sandbox) or if you are working against a non-Claude agent that does not honour `SKILL.md` files."] = \
    '以下情况 *不要* 抄 Superpowers：你需要的是运行时隔离（应当抄 OpenHarness、或 Claude Code 的 hooks ＋ 沙箱），或者你面对的是一个不尊重 `SKILL.md` 的非 Claude 智能体。'

T['Where Superpowers is structurally weak'] = 'Superpowers 在结构上弱的地方'

T['The 12-cell scorecard in §08.4 makes the trade-off explicit: Superpowers is the strongest public example of SDD × Bridle and TDD × Bridle, and the weakest on the entire MDD row. The asymmetry is *structural* — a library of markdown files cannot enforce what it prescribes, and cannot observe whether it was followed. Two failure modes follow directly.'] = \
    '§08.4 那张十二格记分卡，把这份取舍摆得明明白白：在 SDD × 缰绳 与 TDD × 缰绳 两格上，Superpowers 是最强的公开范例；在整行 MDD 上，它则是最弱的。这种不对称是 *结构性* 的——一堆 markdown 文件，既不能强制执行它所开出的处方，也观测不到处方到底有没有被照办。两种失败模式直接由此而来。'

T['**Prescription without enforcement.** A skill\'s prose says "refuse to proceed on a red test". If no hook in the host repo *mechanically* refuses the proceed, the skill becomes compliance theatre (Chapter 02\'s Stage 3 pitfall applied at point-blank range). Superpowers is strongest when paired with Claude Code\'s hooks; standalone, it is a strongly-worded suggestion.'] = \
    '**开了方子，却没有执行力。** 一份技能的散文说"测试为红时拒绝继续"。若宿主仓库里没有哪一条 hook *机械地* 拒绝"继续"，这份技能就会变成"合规剧场"（第 02 章第 3 阶段那条陷阱，在这里贴脸适用）。Superpowers 与 Claude Code 的 hook 搭配时最强；单独使用时，它就是一条措辞强烈的建议而已。'

T['**No self-observability.** The library has no signal for "the team installed 30 skills and uses 4 of them regularly". Skill-sprawl (Chapter 02\'s Stage 3 pitfall) lands hardest in skills-only harnesses precisely because there is no metric on skill invocation rates.'] = \
    '**没有自我可观测性。** 这个库没有任何信号能告诉你"团队安装了 30 条技能，只有 4 条是常用的"。Skill-sprawl（第 02 章第 3 阶段那条陷阱）在"只有技能"的挽具里打得最狠，恰恰是因为根本没有"技能调用率"这一类度量。'

T['Pitfall — "Skills alone are our harness"'] = '陷阱——"技能就是我们的挽具"'

T["A team adopts Superpowers, copies thirty skills into `~/.claude/skills/`, and declares the harness complete. Three months later, measured output quality has not moved despite the team reporting high skill adoption in retros. **Why**: without a fence that *refuses* turns which skipped a skill, and without a metric that reports *which* skills fired, the skill library is operating on the honour system. The team's intent and the agent's behaviour are measured only through self-report. **Symptom**: retros describe the skills warmly; incident post-mortems reveal the relevant skill existed but was not invoked. **Fix**: pair every load-bearing skill with a `PreToolUse` hook that fails when the skill's preconditions were not met (red tests, unsigned-off design, missing acceptance table). Superpowers supplies the prescription; Claude Code's hooks supply the enforcement. Neither alone is a harness."] = \
    '一支团队采用了 Superpowers，把三十条技能拷到 `~/.claude/skills/` 下，然后宣称挽具造完了。三个月后，产出质量的可测量值没有动——尽管团队在复盘里报告"技能采纳率很高"。**为什么**：在没有一条 *拒绝* "跳过了某项技能的那次对话轮次" 的护栏、以及没有一条度量报告 "哪些技能实际被触发过" 的情况下，这座技能库是在靠荣誉制度运作。团队的意图与智能体的行为，只能靠自我汇报来度量。**症状**：复盘里对这些技能赞不绝口；事故复盘却揭示，相关技能本来在，只是没被调用。**解法**：为每一条承重技能，配一条 `PreToolUse` hook——当技能的前置条件（红色测试、尚未签字的设计、缺失的验收表）不满足时就失败。Superpowers 提供处方；Claude Code 的 hook 提供执行。单独哪一端，都不是挽具。'

T['HarnessCard'] = 'HarnessCard'
T['Field'] = '字段'
T['Value'] = '值'
T['HarnessCard schema version'] = 'HarnessCard schema 版本'
T['CAR-HarnessCard v0.2 {cite}`car2025decomposition`'] = 'CAR-HarnessCard v0.2 {cite}`car2025decomposition`'
T['Subject'] = '对象'
T['Superpowers, 2026-04 snapshot {cite}`vincent2025superpowersrepo`'] = \
    'Superpowers，2026-04 快照 {cite}`vincent2025superpowersrepo`'
T['License'] = '许可证'
T['MIT {cite}`vincent2025superpowers`'] = 'MIT {cite}`vincent2025superpowers`'
T['Control layer (CAR)'] = 'Control 层（CAR）'
T['Strongly opinionated via ~30 prose skills.'] = \
    '通过约 30 条散文技能，持有强烈主张。'
T['Agency layer (CAR)'] = 'Agency 层（CAR）'
T['Unchanged from the host Claude Code installation.'] = \
    '与宿主 Claude Code 安装相比没有变化。'
T['Runtime layer (CAR)'] = 'Runtime 层（CAR）'
T['Deferred to Claude Code; Superpowers does not ship a runtime.'] = \
    '交由 Claude Code 处理；Superpowers 不自带运行时。'
T['SDD (mean)'] = 'SDD（均值）'
T['3.5'] = '3.5'
T['TDD (mean)'] = 'TDD（均值）'
T['3.0'] = '3.0'
T['MDD (mean)'] = 'MDD（均值）'
T['1.5'] = '1.5'
T['Primary citation'] = '主要引用'
T['{cite}`vincent2025superpowers`'] = '{cite}`vincent2025superpowers`'

T['Research Foundations'] = '研究脉络'

T['**TDD** {cite}`beck2002tdd` — academic lineage of the TDD skill.'] = \
    '**TDD** {cite}`beck2002tdd` —— TDD 技能的学术谱系。'
T['**Debugging** {cite}`zeller2009whyprogramsfail` — lineage behind the systematic-debugging and receiving-code-review skills.'] = \
    '**调试** {cite}`zeller2009whyprogramsfail` —— systematic-debugging 和 receiving-code-review 两条技能背后的谱系。'
T['**Code review** {cite}`bacchelli2013codereview` — the modern-code-review research that motivates the request / receive review skills.'] = \
    '**代码评审** {cite}`bacchelli2013codereview` —— 现代代码评审的研究，正是 request / receive review 两条技能的动机所在。'
T['**Socratic design essays** {cite}`mills2015socratic` — philosophical backing for skills that ask the agent questions before letting it act.'] = \
    '**Socratic design 论文** {cite}`mills2015socratic` —— 给"先向智能体提问、再允许它行动"这类技能提供哲学支撑。'
T['**Anthropic skills documentation** {cite}`anthropic2024skills` — the official format specification for `SKILL.md` files.'] = \
    '**Anthropic 的 skills 文档** {cite}`anthropic2024skills` —— `SKILL.md` 文件的官方格式规范。'

T['Hands-On'] = '动手环节'

T['Two copyable artefacts live under `book/source/_handson/08-superpowers/`:'] = \
    '在 `book/source/_handson/08-superpowers/` 下，住着两份可直接拷走的制品：'
T['`SKILL.md` — a drop-in skill readers can copy to `~/.claude/skills/spec-first-feature/SKILL.md`.'] = \
    '`SKILL.md` —— 一份可直接扔进去就能用的技能，读者可以把它拷到 `~/.claude/skills/spec-first-feature/SKILL.md`。'
T['`walkthrough.md` — an *install → invoke → observe* walkthrough verifying the skill fires end-to-end.'] = \
    '`walkthrough.md` —— 一段 *安装 → 调用 → 观察* 的走查，用来端到端验证这份技能确实被触发。'


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
