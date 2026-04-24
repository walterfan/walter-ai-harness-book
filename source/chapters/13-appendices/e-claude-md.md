---
status: draft
chapter-type: appendix
---

# 附录 E —— `CLAUDE.md` 兼容模板

本附录把第 03、04、05、06 章（含 Tauri-Todo 那条弧线）中的 hands-on 片段，合并成一份 `CLAUDE.md`，供仍以 Claude Code 为主的仓库直接使用。若仓库有多个智能体客户端，优先把这些内容放进 `AGENTS.md`；`CLAUDE.md` 应作为 symlink 或薄镜像存在。每一块都带一条 `<!-- origin: ..., zone: ..., guardian: ... -->` 头注，这样生成出来的文件，仍然可以对照十二格矩阵审计。

**许可证。** 下面这份模板以 MIT 协议发布；拷贝、修改、再分发皆不需要额外致谢。引用记录住在 `_bib/*.bib` 里，不会随模板一起旅行；CAR HarnessCard schema {cite}`car2025decomposition` 是它被设计去对接的上游披露格式。

## 合并后的兼容模板

````text
## CLAUDE.md

<!-- origin: chapters/03-what-is-harness-engineering.md, zone: Bridle, guardian: SDD -->
### Role and scope
You are a coding agent for <project-name>. You may edit <allowed paths>.
You must not touch <forbidden paths>. Every new public function gets a
docstring and a test; no exceptions.

<!-- origin: chapters/04-three-guardians.md, zone: Bridle, guardian: SDD -->
### Spec discipline
Before editing any source file, read the matching spec under `specs/`
(or, if absent, `docs/adr/`). If the spec is older than the code by
more than 30 days, surface this as a risk and pause.

<!-- origin: chapters/04-three-guardians.md, zone: Bridle, guardian: TDD -->
### Test discipline
Before writing implementation code, locate or author the failing test
that captures the requirement. A commit that does not green one test
does not advance the project.

<!-- origin: chapters/04-three-guardians.md, zone: Bridle, guardian: MDD -->
### Metric discipline
Before merging any change that touches a user-facing path, confirm the
metrics north-star (`mean agent turns to green` on the fixed benchmark)
has not regressed.

<!-- origin: chapters/05-harness-anatomy.md · SDD × Paddock -->
### Acceptance Gate (Verification Table)

| ## | Requirement                          | Checked by        |
|---|--------------------------------------|-------------------|
| 1 | Acceptance tests green               | Test Engineer     |
| 2 | `AGENTS.md` rules unchanged or versioned | Architect     |
| 3 | `CHANGELOG.md` entry under Unreleased | PO               |

<!-- origin: chapters/05-harness-anatomy.md · TDD × Fence -->
### Pre-edit hooks (Claude Code)

Install `.claude/hooks.json` as follows:

```json
{
  "hooks": {
    "PreToolUse": [
      {"matcher": "Write|Edit|MultiEdit",
       "command": "pytest -q -m 'not slow'",
       "stopOnFailure": true}
    ]
  }
}
```

<!-- origin: chapters/05-harness-anatomy.md · MDD × Fence -->
### Cost cap

A per-session cap of $2.00 and a monthly cap of $800.00 apply; breaches
refuse new tool calls until manual reset. The per-repo configuration
file lives at `.harness/cost-cap.yaml`.

<!-- origin: chapters/06-operating-a-harness.md · SDD × Groom -->
### Weekly groom schedule

Monday: run the entropy audit workflow; file issues for any new CVE,
stale `verified:` header, or broken link.
Friday: verify spec surface has no drift > 3 items; otherwise trigger a
mid-sprint re-spec.

<!-- origin: _handson/06-operating-a-harness/tauri-todo/, Bridle, SDD -->
### Tauri-Todo 家规（当这份仓库是一个 Tauri 2 应用时）

- Rust crate `src-tauri/` 持有 IPC、存储、操作系统集成。
- `src/` 下的 TypeScript 应用只持有 UI 与输入校验。
- 绝不要从 TS 直接调用操作系统 API；一律经由 `invoke()` 转接。
- 绝不要在同一笔 commit 中引入依赖却不跑 `cargo audit`。

<!-- origin: chapters/06-operating-a-harness.md · TDD × Fence + SDD × Fence -->
### Committed gates

A commit is only valid if, in order:
1. `pytest -q` passes.
2. `ruff check .`（或相应语言的等价 linter）通过。
3. `gitleaks` finds no secrets.
4. `make prompts-lint`（或等价的规约校验器）通过。
5. 不允许新增 `TODO` 标记而没有与之对应的 issue 链接。

<!-- origin: chapters/13-appendices/d-harnesscard.md · meta -->
### HarnessCard self-disclosure

When you finish a non-trivial change, update `HarnessCard.md` at the
repo root and append a one-line entry to `HARNESSCARD-CHANGELOG.md`
naming which cell's score moved and by how much.
````

## 粘贴使用说明

上面这段以 MIT 协议发布，且刻意全为文本——没有图片、没有外部抓取、
没有密钥。若你只用 Claude Code，可以把它命名为 `CLAUDE.md`；若你有
多个智能体客户端，应先把它并入 `AGENTS.md`，再把 `CLAUDE.md` 做成
symlink 或薄镜像。除了把 `<project-name>` 与 `<allowed paths>` 替换掉
之外，不需要任何额外修改。
