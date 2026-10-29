# Phase 3 candidate v4 — development record

Date: 29 October 2026. Branch: `codex/phase3-skills`. The tested v3 remains on `main`; its 64.52 local score does not apply to this candidate. No full candidate model run has been performed. The real presentation MP4 is still missing.

## Changes

- Participant-chosen protect/grow bands and explicit near-limit behaviour, retaining the v2 lesson that recovery may arrive too late. Comfortable wellbeing can fund bounded growth; a 10/10 ending prompts review of earlier opportunities, never deliberate damage to final wellbeing.
- Network priority within our two-month planning horizon when reviews or trends suggest a relationship gap. No hidden promotion cutoff or comparison of unrelated raw-stat scales.
- A compact warning ledger in official `take_action(notes=...)`, recovered with one four-entry `check_latest_logs` call per quarter. The user chose this fallback because workspace memory lacks written organiser confirmation. No memory files, memory tools or embeddings are requested.
- Ledger content changes at quarter entry or new/worsening warnings; its latest snapshot is carried in ordinary action notes so bounded recovery has a chance to find it. Roughly 16–20 semantic revisions is an estimate, not a total-write cap. First-seen warning months remain; attempted mitigation is not clearance.
- Numbered decision criteria, one observation per decision, one startup handbook, bounded logs, rationale <=18 words, ledger <=30 and complete notes <=50. These are our budgets, not engine limits.
- An optional public-only reference card; export checks now include it and still reject secrets. Design reports, presentation outline and teammate instructions describe the changed candidate separately from v3.

## Checks actually performed

- Full key-free test suite: **121 passed**. This checks runner, installation isolation, validation and export plumbing, not agent behaviour. Two added checks cover reference-card ZIP inclusion and credential rejection.
- Ruff lint passed for the changed Python helper and its tests. Repository-wide Ruff reports an existing unused import in the unchanged official `career_sim_runner/ws_client.py`; that runner file was not edited. Development submission validation passed with seven files, including the reference card. Final validation still fails because the real MP4 is missing; no final ZIP was produced for this candidate.
- Key-free manual check through the official MCP interface: an ordinary action's ledger was recovered after `Notes:` within a returned entry's `message`. The request was `count=4`, returning three entries. No model API calls were made. The initialization action's note was not returned, so missing history must remain unknown. Manual setup sessions were not completed careers or strategy tests. No engine, dataset or database contents were inspected.
- Source-size comparison against v3: manifest instruction 191 -> 79 whitespace-separated words (1,376 -> 512 characters); two Skills combined 1,311 -> 904 words. A shorter source is not a measured token saving: carried ledger notes add text, and actual model call patterns are untested.

## Hypothetical desk review

These are instruction-coverage checks, not simulated outcomes or model tests. No event names or answer mappings are used.

| Generic situation | Required decision procedure |
| --- | --- |
| Health 3 and optional work offered before recovery | Protect now; do not assume future Energy use prevents failure |
| Health 8, Dignity 7, stable, no overriding warning | Consider useful bounded growth instead of automatic recovery |
| Comfortable stats but persistent warning | Compare offered mitigation; retain earliest warning month; comfort is not clearance |
| Review window near, relationship feedback weak, other dimensions progressing | Consider a fitting Network action; infer no numerical gate |
| Mitigation attempted, result ambiguous | Retain warning as attempted; do not invent hidden clearance |
| Quarter entry after compression | Single observation and four-entry log recovery; recompute dated window distance |
| Ledger absent from returned logs | Keep available context, label unknown history, do not expand the search |
| Final month with comfortable wellbeing | Prefer benefits realised before ending while preserving scored dimensions |

## Next real test

Coordinate shared-credit use, record the strategy commit and preserve original runner outputs. Use the exact designated model, pinned JiuwenSwarm and official routing. Follow [TEAM_GUIDE.md](../TEAM_GUIDE.md).

Check completion and `quantitative_score`, tokens per survival month, actual handbook/observe/log counts, note sizes, ledger recovery and first-seen warning retention. Inspect whether warnings affect the next plan, Network receives appropriate attention, and numerical claims remain grounded in observations. Compare repeated runs before replacing v3. A single successful round trip cannot establish long-run retention, instruction adherence or score improvement.
