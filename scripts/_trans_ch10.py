"""One-shot translator for Ch.10 Claude Code."""
import polib

PATH = 'source/locale/zh_CN/LC_MESSAGES/chapters/10-claude-code.po'
T = {}

T['Case Study: Claude Code via《马书》'] = \
    '案例研究：通过《马书》看 Claude Code'

T['*The only closed-source case study in this book. Read it knowing that.*'] = \
    '*本书中唯一一份闭源案例。带着这一点去读。*'

T['Reverse-Engineering Disclaimer'] = '逆向工程免责声明'

T["The Claude Code product is closed source. This chapter's analysis relies on three evidence classes, in descending order of authority:"] = \
    'Claude Code 产品是闭源的。本章的分析依赖三类证据，按权威性递减排列：'

T["**Anthropic's official public documentation and launch post** {cite}`anthropic2024claudecode` and the MCP specification {cite}`anthropic2024mcp` — primary authority."] = \
    '**Anthropic 的官方公开文档与发布文章** {cite}`anthropic2024claudecode` 以及 MCP 规范 {cite}`anthropic2024mcp` —— 第一权威。'

T['**Observed runtime behaviour** of the Claude Code CLI across the 2026-03 through 2026-04 observation window on macOS and Linux, captured in author session logs.'] = \
    '**运行时实测行为**：作者在 2026-03 到 2026-04 的观察窗口里，在 macOS 与 Linux 上运行 Claude Code CLI，记入会话日志的观察结果。'

T["**Zhang Handong's《马书》 2026 reverse-engineering analysis** {cite}`zhangbook2026` — hereafter *Ma's book* — a publicly available Chinese-language study of Claude Code's bundled prompt, skill library, hooks contract, and tool schemas."] = \
    '**张汉东《马书》2026 年的逆向工程分析** {cite}`zhangbook2026` —— 下文称 *马书* ——一份公开发行的中文研究，系统拆解了 Claude Code 的内置提示、技能库、hooks 契约与工具 schema。'

T["**Observation window.** All claims below reflect Claude Code's behaviour between **2026-03-01 and 2026-04-15**. Behaviour outside this window is not guaranteed to match."] = \
    '**观察窗口。** 下文所有结论只反映 Claude Code 在 **2026-03-01 到 2026-04-15** 之间的行为。此窗口之外的行为不保证一致。'

T['**Retraction commitment.** If Anthropic publishes official documentation or makes a public statement that contradicts any claim below, this chapter will be updated within 30 days and the retracted claim will be struck through with a dated note explaining the change. The book treats reverse-engineered observation as *provisional*, not authoritative.'] = \
    '**撤回承诺。** 若 Anthropic 发布官方文档或公开声明与下文任一结论冲突，本章将在 30 天内更新，并把被撤回的结论划掉，附上注明日期的说明。本书把逆向观察视为 *临时性* 结论，而非权威结论。'

T["**Licensing.** Neither《马书》 nor Claude Code's internal bundle is reproduced verbatim in this chapter beyond the standard fair-use excerpt limit of ≤ 20 lines per quoted passage, with attribution to《马书》's page numbers where applicable."] = \
    '**版权。** 本章不会原样转载《马书》或 Claude Code 的内部捆绑内容，单段引用不超过合理使用上限的 20 行，在可能处标注《马书》页码。'

T['§10.1 — Reading Claude Code through the matrix'] = \
    '§10.1 —— 用三大护法 × 四区域矩阵来读 Claude Code'

T['Claude Code, as observed and as described by《马书》, distributes harness responsibility across three overlapping surfaces:'] = \
    '如实测所见、并被《马书》所记载：Claude Code 把挽具职责，分布在三个彼此重叠的表面上：'

T["**The bundled system prompt** (Bridle, primarily SDD) — a multi-kilobyte document that《马书》 reproduces and annotates across several chapters; it includes role framing, tool-use heuristics, citation formatting rules, and explicit red-flag self-questions."] = \
    '**内置系统提示**（缰绳，主要是 SDD）—— 一份数 KB 的长文档；《马书》跨多章复刻并批注过它；里面包含角色设定、工具使用的启发式规则、引用格式、以及显式的"红旗自问清单"。'

T['**The hooks contract** (Fence, spanning TDD and MDD) — `hooks.json` under `.claude/` supports `PreToolUse`, `PostToolUse`, `SessionEnd`, and `UserPromptSubmit` matchers; a non-zero exit code from a `PreToolUse` hook refuses the tool call.'] = \
    '**hooks 契约**（护栏，横跨 TDD 与 MDD）—— `.claude/hooks.json` 支持 `PreToolUse`、`PostToolUse`、`SessionEnd`、`UserPromptSubmit` 几类匹配器；`PreToolUse` 钩子以非零退出码结束，就会拒掉那次工具调用。'

T['**The skills system** (Bridle + Paddock, mostly SDD) — `SKILL.md` files under `~/.claude/skills/` the agent auto-discovers and invokes based on the `description:` front-matter.'] = \
    '**技能系统**（缰绳 ＋ 牧场，主要是 SDD）—— `~/.claude/skills/` 下的 `SKILL.md` 文件，智能体根据 front-matter 里的 `description:` 自动发现并调用。'

T["A compact excerpt from《马书》's observation of the bundled prompt (original is Chinese; translation is the author's own for exposition):"] = \
    '以下是《马书》对内置提示的一段简短摘录（原文为中文；为便于叙述，译文由作者自行翻译）：'

code_16 = '''[Excerpt, ≤ 20 lines, translated from《马书》 Chapter 4, §4.2, p. 113]

System message tail:
    - When asked a factual question, cite at least one source.
    - When writing code, prefer edits over creation.
    - Never include a generated-by-AI signature in the output.
    - If a skill applies, read and follow it before answering.
    - Treat user files as authoritative; do not overwrite without confirmation.
'''
code_16_zh = '''[摘录，≤ 20 行，译自《马书》第 4 章 §4.2，p. 113]

系统消息尾部：
    - 被问到事实性问题时，至少引用一处来源。
    - 写代码时，优先"修改"而非"新建"。
    - 输出中绝不要包含"由 AI 生成"的落款。
    - 若有 skill 适用，作答之前先读并遵循它。
    - 把用户文件视作权威；未确认之前不覆盖。
'''
T[code_16] = code_16_zh

T['《马书》 argues — and observed behaviour corroborates — that these tail-of-prompt rules are the single most load-bearing SDD × Bridle artefact in the product.'] = \
    '《马书》主张——实测行为也佐证——这些"提示尾部规则"是本产品里最承重的那一件 SDD × 缰绳 制品。'

T['§10.2 — 12-cell highlight map with confidence bands'] = \
    '§10.2 —— 十二格亮点图（含置信等级）'

T['Every cell below carries a confidence band: `observed` (directly verifiable in runtime behaviour), `inferred` (derived from《马书》 + official docs + observation triangulated), or `speculative` (best-guess that future disclosure could promote or retract).'] = \
    '下表每一格都标注一条置信等级：`observed`（直接可在运行时行为中复现）、`inferred`（由《马书》＋ 官方文档 ＋ 实测三角印证推得）、或 `speculative`（当前是最佳猜测，未来的官方披露可能把它升级或推翻）。'

T['Cell'] = '格子'
T['Score'] = '得分'
T['Confidence'] = '置信等级'
T['Evidence and what would change the band'] = '证据，以及什么会改变这个置信等级'

T['SDD × Bridle'] = 'SDD × 缰绳'
T['5'] = '5'
T['observed'] = 'observed'
T['Bundled prompt + skills system directly shape every turn; corroborated by《马书》 Ch.~4 {cite}`zhangbook2026` and Anthropic docs {cite}`anthropic2024claudecode`.'] = \
    '内置提示 ＋ 技能系统直接塑造每一回合；被《马书》第 4 章 {cite}`zhangbook2026` 与 Anthropic 官方文档 {cite}`anthropic2024claudecode` 双重印证。'

T['SDD × Fence'] = 'SDD × 护栏'
T['3'] = '3'
T['inferred'] = 'inferred'
T["Front-matter schema for `SKILL.md` is undocumented; skills with malformed YAML are silently skipped.《马书》 Ch.~5 reproduces the parser's tolerant mode."] = \
    '`SKILL.md` 的 front-matter schema 无官方文档；格式不对的 skill 会被悄悄跳过。《马书》第 5 章复现了解析器的这种"宽容模式"。'

T['SDD × Paddock'] = 'SDD × 牧场'
T['No built-in acceptance ritual; review discipline is delegated to the host team.'] = \
    '内置并无验收仪式；评审纪律交由宿主团队自己定。'

T['SDD × Groom'] = 'SDD × 梳理'
T['`/cost`, `/status`, `/clear` slash commands support grooming but cadence is operator-owned.'] = \
    '`/cost`、`/status`、`/clear` 几条斜杠命令支持梳理，但节奏由操作者自己掌控。'

T['TDD × Bridle'] = 'TDD × 缰绳'
T['Test-first framing is encouraged by default skills and《马书》 Ch.~6 but not enforced.'] = \
    '默认技能与《马书》第 6 章都在鼓励"测试先行"的表述，但并未强制。'

T['TDD × Fence'] = 'TDD × 护栏'
T['`PreToolUse` hooks with non-zero exit refuse edits; documented by Anthropic and demonstrated in hands-on `hooks.json`.'] = \
    '非零退出码的 `PreToolUse` 钩子会拒掉编辑；Anthropic 文档有记载，hands-on 的 `hooks.json` 也做了演示。'

T['TDD × Paddock'] = 'TDD × 牧场'
T['2'] = '2'
T['speculative'] = 'speculative'
T['Would be promoted to `inferred` if Anthropic published a public CI-integration spec. A shipped `claude-code ci` subcommand with a documented exit protocol would change the band.'] = \
    '若 Anthropic 公开 CI 集成规范，这一格可被升级为 `inferred`。若上线带有文档化退出协议的 `claude-code ci` 子命令，也会改变置信等级。'

T['TDD × Groom'] = 'TDD × 梳理'
T['Would be promoted if Anthropic published release-note signals for model updates that invalidate older test assumptions.'] = \
    '若 Anthropic 在模型更新的 release note 中，公开标记"会使旧测试假设失效"的信号，这一格可被升级。'

T['MDD × Bridle'] = 'MDD × 缰绳'
T['4'] = '4'
T['`/cost` endpoint + status-line token counter expose a usable north-star candidate.'] = \
    '`/cost` 端点 ＋ 状态栏 token 计数器，合起来暴露了一个能用的"北极星候选项"。'

T['MDD × Fence'] = 'MDD × 护栏'
T['Rate limits exist at the API layer but a *local* cost cap requires operator-authored hooks.《马书》 Ch.~7 documents the default limits.'] = \
    'API 层有速率限制，但 *本地* 成本上限需要操作者自己写钩子。《马书》第 7 章记录了这些默认限制。'

T['MDD × Paddock'] = 'MDD × 牧场'
T['Release SLI concept absent; Claude Code is a client tool, not a server.'] = \
    '没有"发布 SLI"这个概念；Claude Code 是客户端工具，不是服务端产品。'

T['MDD × Groom'] = 'MDD × 梳理'
T['Anthropic pushes weekly prompt-library updates that act as an upstream groom signal.'] = \
    'Anthropic 每周推送 prompt 库更新，这相当于一路上游的"梳理信号"。'

T['At least one cell — **TDD × Paddock** — is explicitly flagged `speculative`. What would promote it: either a shipped Anthropic `claude-code ci` subcommand with a documented machine-readable exit protocol, or an官方 release note that declares the existing behaviour stable and publicly versioned.'] = \
    '至少有一格——**TDD × 牧场**——被显式标为 `speculative`。要把它升级，需要其中之一：要么 Anthropic 上线带文档化、机器可读退出协议的 `claude-code ci` 子命令；要么官方 release note 正式宣告现有行为稳定且公开版本化。'

T["§10.3 — The hooks contract — Claude Code's primary Fence"] = \
    '§10.3 —— hooks 契约 —— Claude Code 的主要护栏'

T["Claude Code's `.claude/hooks.json` is the most transferable piece of the product, because it is purely declarative. The observation is that any hook exiting with code 2 refuses the in-flight tool call; this is documented by Anthropic {cite}`anthropic2024claudecode` and matches observed behaviour."] = \
    'Claude Code 的 `.claude/hooks.json` 是这款产品里 *最可迁移* 的那一块，因为它是纯声明式的。实测结论是：任何钩子以退出码 2 结束，就会拒掉当前那次工具调用；这一点由 Anthropic 官方文档 {cite}`anthropic2024claudecode` 记录，且与实测一致。'

code_58 = '''{
  "$comment": "verified: 2026-04-17 · Ch.10 Claude Code hands-on · stop-on-test-failure hook. Synthesized from Anthropic's public hooks documentation; NOT a copy of any Claude Code internal file.",
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "command": "pytest -q -m 'not slow' || exit 2",
        "description": "Refuse edits while the test tree is red. Exit code 2 is the documented 'stop the tool call' signal."
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "command": "git diff --stat | tee .claude/.last-edit-diff",
        "description": "Capture a diff summary after every edit so the session log carries an audit trail."
      }
    ],
    "SessionEnd": [
      {
        "command": "python scripts/session_cost_report.py",
        "description": "Write a per-session cost report into .claude/reports/; feeds the MDD Groom audit."
      }
    ]
  }
}
'''
T[code_58] = code_58

T['The hands-on artefact is *synthesized from public documentation* — explicitly not a copy of any internal file. Any reader who adopts it into their own `.claude/` setup is using a reconstruction.'] = \
    'hands-on 制品是 *基于公开文档合成* ——明确不是任何内部文件的拷贝。读者把它搬进自己的 `.claude/` 配置，用的是一份重建版本。'

T['§10.4 — What transfers, what does not'] = '§10.4 —— 哪些可以搬走，哪些不行'

T['**Transfers.** The bundled-prompt discipline (a long, load-bearing system message), the `SKILL.md` format (simple markdown with front-matter), and the hooks contract (exit-code-driven refusals).'] = \
    '**可搬走的**：内置提示这种纪律（一份长且承重的系统消息）、`SKILL.md` 的格式（带 front-matter 的简单 markdown）、以及 hooks 契约（由退出码驱动的拒绝机制）。'

T['**Does not transfer directly.** Claude-specific model-provider coupling, the slash-command registry, the bundled skill library\'s exact wording (copyright restriction).'] = \
    '**不能直接搬**：Claude 专属的模型供应商耦合、斜杠命令注册表、内置技能库的原文措辞（受版权限制）。'

T["Readers who want the *pattern* without paying Anthropic's platform cost can reproduce (a) in their own agent (any agent that reads a long system message works), (b) trivially (it's already just markdown), and (c) by adopting Claude Code's hook grammar in any agent that supports pre-write callbacks."] = \
    '想拿到 *模式* 又不想付 Anthropic 平台成本的读者，可以：(a) 在自己的智能体里复刻第一项（任何会读取长系统消息的智能体都行）；(b) 几乎不费力地复刻第二项（它本来就是 markdown）；(c) 在任何支持 "写前回调" 的智能体里采纳 Claude Code 的钩子语法。'

T['Structural risks of a closed-source harness'] = '闭源挽具的结构性风险'

T['The asymmetry of learning from a closed-source system deserves naming explicitly — not as criticism of Claude Code, but as a warning to readers about how conclusions from this chapter should (and should not) be generalised.'] = \
    '从一套闭源系统里学习，其不对称性值得明说——这不是批评 Claude Code，而是在提醒读者：本章的结论该如何（以及不该如何）推广到别处。'

T['**Observation window bias.** Every claim in §10.2 is indexed to the 2026-03 through 2026-04 observation window. Anthropic ships prompt- library updates weekly; any claim about the *content* of the bundled prompt has a half-life measured in weeks, not quarters. This is not a defect — it is how the product evolves — but it means a reader who treats §10.2 as a static reference will progressively hold an out-of-date mental model.'] = \
    '**观察窗口偏置。** §10.2 的每一条结论都锚定在 2026-03 到 2026-04 的观察窗口。Anthropic 每周都在更新 prompt 库；任何关于"内置提示 *内容*"的结论，其半衰期是以周计的，不是以季度计。这不是缺陷——这是产品的正常演进——但它意味着：把 §10.2 当作静态参考的读者，心里那份模型会逐渐过时。'

T['**Unfalsifiable speculative bands.** Two cells in §10.2 carry the `speculative` confidence band. The honest consequence is that the scores are guesses; the subtler consequence is that *they cannot be falsified without Anthropic\'s cooperation*. Readers should treat speculative cells as placeholders, not evidence.'] = \
    '**不可证伪的 speculative 等级。** §10.2 里有两格挂着 `speculative` 置信等级。诚实地说，这些分数是猜测；更微妙的一层是——*没有 Anthropic 的配合，它们就无法被证伪*。读者应当把 speculative 格视为占位符，而非证据。'

T["**Coupling to Anthropic's release cadence.** Every transfer pattern named above assumes Anthropic continues to ship along its current trajectory (hooks stay declarative, SKILL.md stays simple markdown, the bundled prompt remains overridable). A vendor decision to consolidate, simplify, or replace any of these surfaces invalidates the corresponding transfer. The harness engineering move is to **adopt the pattern, not the surface** — a team that wrote its own `PreToolUse`-style hook grammar against a stable abstraction will survive a Claude Code 2.0 rewrite; a team that bound directly to the current `hooks.json` schema will not."] = \
    '**与 Anthropic 发布节奏的耦合。** 上面每一条"可迁移模式"，都假设 Anthropic 继续按当前轨迹发布（hooks 保持声明式、SKILL.md 保持简单 markdown、内置提示仍可被覆盖）。厂商若决定合并、简化、或替换这些表面，对应那条可迁移性就作废。挽具工程意义上正确的做法是——**采纳模式，不要采纳表面**——自己在一层稳定抽象之上写一套 `PreToolUse` 风格钩子语法的团队，能挺过 Claude Code 2.0 的重写；直接绑死当前 `hooks.json` schema 的团队则不能。'

T['Pitfall — Mistaking observation for specification'] = '陷阱——把观察当成规范'

T['A team reads Chapter 10, copies the synthesised `hooks.json` from §10.3, and builds six months of tooling on top of the observed behaviour "exit code 2 refuses the in-flight tool call". Anthropic later ships a Claude Code update that reserves exit code 2 for a different semantic and introduces a structured JSON response instead. Half the tooling silently breaks. **Why**: the observed behaviour was never an API — it was behaviour, which vendors are free to change. The chapter\'s Retraction Commitment covers the book; nothing covers the team\'s tooling. **Fix**: wrap every reverse-engineered interface in your own abstraction *before* relying on it. A function named `refuse_tool_call(reason)` that happens to exit 2 today and exits 3 next quarter is resilient to the vendor\'s internal evolution; direct calls to `sys.exit(2)` are not. This is the same discipline Feathers {cite}`feathers2004legacy` prescribes for legacy interfaces, applied to a system the team does not own.'] = \
    '一支团队读完第 10 章，把 §10.3 合成出来的 `hooks.json` 拷过去，在"退出码 2 拒掉当前工具调用"这条实测行为之上建了半年工具链。随后 Anthropic 发布一次 Claude Code 更新——把退出码 2 用于另一种语义，并改以结构化 JSON 响应代之。这套工具有一半悄悄坏了。**为什么**：实测行为从来不是 API ——那是行为，而行为是厂商可以随意修改的。本章的"撤回承诺"覆盖的是本书；没有什么来覆盖团队的工具链。**解法**：在依赖任何一份逆向得来的接口之前，*先* 用自己的抽象把它包住。一只名叫 `refuse_tool_call(reason)` 的函数——今天退出 2、下个季度退出 3——能扛过厂商的内部演进；直接 `sys.exit(2)` 的调用扛不住。这与 Feathers {cite}`feathers2004legacy` 对遗留接口开出的那剂药方是同一种纪律——只不过这次应用在"团队并不拥有"的那套系统上。'

T['HarnessCard'] = 'HarnessCard'
T['Field'] = '字段'
T['Value'] = '值'
T['HarnessCard schema version'] = 'HarnessCard schema 版本'
T['CAR-HarnessCard v0.2 {cite}`car2025decomposition`'] = 'CAR-HarnessCard v0.2 {cite}`car2025decomposition`'
T['Subject'] = '对象'
T['Claude Code, 2026-03 – 2026-04 observation window {cite}`anthropic2024claudecode`'] = \
    'Claude Code，2026-03 到 2026-04 观察窗口 {cite}`anthropic2024claudecode`'
T['License'] = '许可证'
T['Closed source (subject); synthesized examples under MIT'] = \
    '对象本身为闭源；合成示例以 MIT 协议发布'
T['Control layer (CAR)'] = 'Control 层（CAR）'
T['Very opinionated; bundled prompt is multi-kilobyte.'] = \
    '主张极强；内置提示长达数 KB。'
T['Agency layer (CAR)'] = 'Agency 层（CAR）'
T['Tool access is strongly gated by hooks and user confirmation prompts.'] = \
    '工具访问被 hooks 与用户确认提示强力把守。'
T['Runtime layer (CAR)'] = 'Runtime 层（CAR）'
T['Cloud LLM + local CLI; optional Docker sandbox via hooks.'] = \
    '云端 LLM ＋ 本地 CLI；可通过 hooks 选装 Docker 沙箱。'
T['SDD (mean)'] = 'SDD（均值）'
T['3.5 (observed=1, inferred=3, speculative=0)'] = \
    '3.5（observed=1，inferred=3，speculative=0）'
T['TDD (mean)'] = 'TDD（均值）'
T['3.0 (observed=1, inferred=1, speculative=2)'] = \
    '3.0（observed=1，inferred=1，speculative=2）'
T['MDD (mean)'] = 'MDD（均值）'
T['3.0 (observed=1, inferred=2, speculative=1)'] = \
    '3.0（observed=1，inferred=2，speculative=1）'
T['Primary citation'] = '主要引用'
T['{cite}`zhangbook2026`'] = '{cite}`zhangbook2026`'
T['Every score above carries the confidence band of its corresponding cell in §10.2.'] = \
    '上述每一项分数，都带有 §10.2 中对应格子的置信等级。'

T['Research Foundations'] = '研究脉络'

T["**Ma's book** {cite}`zhangbook2026` — primary reverse-engineering source for the bundled prompt, skill library, and hooks behaviour."] = \
    '**马书** {cite}`zhangbook2026` —— 对内置提示、技能库、hooks 行为的首要逆向工程来源。'
T['**Anthropic Claude Code launch post** {cite}`anthropic2024claudecode` — the official documentation of record.'] = \
    '**Anthropic Claude Code 发布文章** {cite}`anthropic2024claudecode` —— 作为权威记录的官方文档。'
T["**MCP specification** {cite}`anthropic2024mcp` — the public specification Claude Code's tool ecosystem targets."] = \
    '**MCP 规范** {cite}`anthropic2024mcp` —— Claude Code 工具生态所对齐的公开规范。'
T['**CAR decomposition** {cite}`car2025decomposition` — the HarnessCard schema the chapter serialises against.'] = \
    '**CAR 分解** {cite}`car2025decomposition` —— 本章把 HarnessCard 序列化到的那套 schema。'

T['Hands-On'] = '动手环节'

T['One copyable artefact lives under `book/source/_handson/10-claude-code/`:'] = \
    '在 `book/source/_handson/10-claude-code/` 下，住着一份可直接拷走的制品：'

T['`hooks.json` — a minimal `.claude/hooks.json` example with a stop-on-test-failure `PreToolUse` rule, a diff-capturing `PostToolUse` rule, and a `SessionEnd` cost-report trigger. Synthesized from public documentation; not a copy of any internal file.'] = \
    '`hooks.json` —— 一份最小的 `.claude/hooks.json` 示例，含：一条"测试失败就停"的 `PreToolUse` 规则、一条抓取 diff 的 `PostToolUse` 规则，以及一条 `SessionEnd` 成本报告触发器。基于公开文档合成；不是任何内部文件的拷贝。'


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
