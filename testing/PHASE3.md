# Phase 3 candidate v4 — development record

**Archived experiment:** `main` now restores the actual v3 submission from `545f06b`, including its original manifest, Skills and design documents. The v4 source remains on `codex/phase3-skills`; this file and the result summary are retained as historical evidence. The changes and checks below describe v4, not the current v3 submission.

Date: 29 October 2026. Branch: `codex/phase3-skills`. V4 scored **42.12/100** and was eliminated in Month 39 through a trust-related failure. The tested v3 remains on `main`, with 64.52 over 48 months, and is the better measured baseline. The real presentation MP4 is still missing.

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

## Actual v4 model run

Run `20261029T170511Z`, using source commit `07d821426267987ae8cf5a3c11c5fd344777851f`, the designated model and pinned environment. Strategy hashes matched the installed files and remained unchanged during play. The official runner finished normally, but the game was eliminated: exit code zero does not mean a completed career. Original outputs were preserved; the [sanitised result](results/v4-summary.json) contains the selected report fields and audit counts.

| Metric | V3 baseline | V4 candidate |
| --- | --- | --- |
| Quantitative score | 64.52 | 42.12 |
| Survival months | 48, completed | 39, eliminated |
| Ending level | L5 | L4 |
| Reported total tokens | 48,614,866 | 39,636,793 |
| Tokens per survival month, rounded | 1,012,810 | 1,016,328 |
| Reported model cost, USD | 0.936443 | 1.184291 |

V4's score was 22.40 points lower; tokens per survival month were about 0.35% higher and reported total spend about 26.5% higher. Lower total tokens reflect fewer months and are not an efficiency gain. An extended response pause occurred; elapsed time is not a controlled speed comparison. These are single, different trajectories, not official scores or causal evidence about any individual policy change.

V4 ended with Health 10, Dignity 8, Skill 59, Network 34, Output 19 and ending-score Wealth 14.3. Visible comfort did not prevent the returned trust-related elimination. No hidden numerical gate or risk formula is inferred from that result.

Actual unique calls, deduplicated by tool-call ID: two Skill loads, one handbook, one new game, 142 observations, 160 actions and twelve log lookups. All log requests used `count=4`; all twelve responses contained a ledger snapshot. Nevertheless, thirteen action notes omitted the ledger; twenty actions lacked an intervening observation. One consecutive observation pair was also recorded. All notes met the budgets (maximum 12 whitespace-separated words, 153 characters). The audit counted forty consecutive ledger versions, including initialization and field/format edits, not forty proven semantic warning revisions. A saved-month field became stale across a review update. Successful transport is not proof of reliable warning tracking or mitigation.

## Next iteration

Keep v3 on `main`. The next candidate should make fresh-observation and ledger requirements more durable, verify warning first-seen dates and clearance evidence, and test whether warnings change the actual plan. Those fixes have not been made or tested here. No second paid candidate run was started automatically.

Coordinate shared-credit use, record the strategy commit and preserve original runner outputs. Use the exact designated model, pinned JiuwenSwarm and official routing. Follow [TEAM_GUIDE.md](../TEAM_GUIDE.md).

Check completion and `quantitative_score`, tokens per survival month, actual handbook/observe/log counts, note sizes, ledger recovery and first-seen warning retention. Inspect whether warnings affect the next plan, Network receives appropriate attention, and numerical claims remain grounded in observations. Compare repeated runs before replacing v3. A single successful round trip cannot establish long-run retention, instruction adherence or score improvement.
