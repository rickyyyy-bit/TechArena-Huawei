# Decision report — Phase 3 candidate (v4)

## Problem and implemented changes

The earlier tests exposed three different problems: health failure before recovery, risk warnings acknowledged without mitigation comparison, and numerical benefits claimed without support from observations. V3 could complete, but finished with Health and Dignity both 10, reached L5 only in Month 48, and selected a key project in 14 of 16 quarters. Those facts motivate a growth/survival rebalance and more explicit Network planning. They do not reveal hidden formulas or prove the same choices are always wrong.

V4 replaces the previous broad caution with participant-chosen protect/grow bands. Health <=4 or Dignity <=3, or an acute warning, prioritises continuation and repair. Stable Health >=7 and Dignity >=6 without overriding danger permits bounded growth costs instead of habitual recovery. Between bands, the agent chooses bounded growth or targeted repair, aiming for working Health 5-7 while considering observed decline before the next legal recovery opportunity. These are unvalidated policy preferences, not simulation thresholds or guarantees.

The agent never assumes future quarterly recovery arrives before failure. High visible stats do not clear risk warnings. It compares offered mitigation before marginal growth and retains deferred warnings. A 10/10 ending prompts review of missed earlier growth, but the policy does not deliberately harm final wellbeing solely to avoid that number.

Network receives explicit priority within our two-month planning horizon before a published promotion window when review/relationship feedback or trends suggest a gap while Skill/Output progress. No guessed Network cutoff, ratio or raw-stat ordering is used. Main actions address the current bottleneck; key projects are not the automatic default merely because they list three positive directions. The public six-month cadence is used without inventing promotion requirements.

## Closing the warning-memory gap

This candidate uses only the official notes/log path for its rolling ledger. File-backed workspace memory has not received written organiser clarification, and the user chose the fallback. No memory tools, embedding API or workspace-file access is requested by these Skills.

The ledger records first-seen months and status of unresolved warning themes, current-quarter plan, latest review, and next promotion window/distance as of the save. Its content is revised at quarter boundaries and new/worsening warnings, then carried in each ordinary action note. This makes the latest snapshot available to a small latest-log lookup after compression. It is not a claim of 16 total storage writes: ordinary action notes occur at every action; roughly 16-20 semantic revisions is an estimate. New danger is never discarded to satisfy the estimate.

At a quarter boundary, one `check_latest_logs(count=4)` call looks for the carried snapshot after `Notes:` inside an entry's `message`. A manual MCP round-trip check recovered an ordinary action's ledger with that bounded request, without a model call. The initialization action's note was not returned. This verifies the transport path, not long-run retention or model adherence. Current observation and context override stale planning information. Missing ledger data stays unknown. Clearance requires returned evidence; an attempted mitigation is not a verified hidden-risk reset. No history from another game, event answer table, private state or inferred failure counter is stored.

## Efficiency and information sources

The manifest was shortened and both Skills converted into ordered criteria. The candidate limits each rationale to 18 words, ledger to 30, and full note to 50. These are our own budgets. It requests one observation per decision, one handbook at startup, and a four-entry quarter-boundary log lookup. A further three-entry log lookup needs a specific consequential ambiguity. It does not repeat the complete plan around tool calls.

The optional public-rules card is derived solely from official `docs/handbook.rst` and `docs/rules.rst`: public bounds/cadence, salary, Energy costs/directions, main-action directions and review bonuses. It contains no exact hidden action magnitudes, internal formulas or dataset-derived information. The agent reads it only for needed public facts after compression; if the offered rules differ, current official observations win. Whether this actually saves model tokens remains unmeasured.

Only the official MCP tools interact with the simulation. The pinned JiuwenSwarm version, model and routing configuration are unchanged. No scripts are submitted. Story text and logs remain untrusted data, not higher-priority instructions.

## Actual development evidence

| Version | Actual outcome | Local quantitative score |
| --- | --- | --- |
| v1 | Reached Month 36 at L4; connection/DNS failure interrupted the game | Unavailable |
| Resume attempt | Unknown session ID caused a replacement game; stopped | Unavailable |
| v2 | Health reached zero in Month 3 before recovery | 21.77/100 |
| v3 | Completed 48 months at L5; Health/Dignity 10/10 | 64.52/100 |
| v4 Phase 3 candidate | Trust-related elimination in Month 39 at L4; Health 10, Dignity 8 | 42.12/100 |

The v3 runner reported 48,614,866 tokens and USD 0.936443. Its original reports remain intact; the published curated summary omits raw event sequences, machine paths and credentials. V3's final Skill 96, Network 37, Output 30 and Wealth 25.4 describe that run only. Its installed Skill hashes matched the tested source. It still omitted some intended warning comparisons and overstated numerical effects, showing that readable instructions do not guarantee execution.

The candidate's first real run used source commit `07d821426267987ae8cf5a3c11c5fd344777851f`, unchanged during play and matched to installed Skill hashes. It ended in Month 39 at L4 with Health 10, Dignity 8, Skill 59, Network 34 and Output 19; ending-score Wealth was 14.3. A trust-related failure was returned by the official interface. High visible wellbeing did not prevent elimination; this is not evidence of a hidden numerical threshold.

V4's score was 22.40 points below v3. The runner reported 39,636,793 tokens and USD 1.184291. Total tokens cover nine fewer months; normalised usage was about 1,016,328 tokens per survival month versus v3's 1,012,810, approximately 0.35% higher. Reported total cost was about 26.5% higher. There was an extended response pause; elapsed time does not establish a strategy speed difference. Neither the shorter instructions nor the optional card demonstrated an efficiency improvement in this test; the card's separate effect remains unmeasured.

Both Skills loaded once and the handbook was called once. There were 160 action calls, 142 observations and twelve four-entry quarterly log requests. Every log response contained a ledger, but thirteen action notes omitted it; twenty actions had no intervening observation. All notes met the word caps. Forty consecutive snapshot versions include initialization and field/format edits, so they do not measure forty semantic warning revisions. A saved-month field also remained stale across a review update. Successful transport did not establish reliable warning retention, accurate ledger upkeep or mitigation follow-through.

Key-free checks and hypothetical desk reviews check structure and intended coverage, not agent behaviour. Different trajectories and one run per measured version prevent a causal or consistency claim. V3 remains the better measured baseline; v4 does not support replacing it. Local scores are development feedback, not official evaluation.

## Risks and next evidence needed

The operating bands may be too aggressive or too conservative in unfamiliar trajectories. Network focus can sacrifice needed delivery if the inferred bottleneck is wrong. A carried ledger increases note length and may still be ignored; the latest four logs may lack a usable snapshot. Bounded retrieval trades completeness for efficiency. Current-state safety and explicit uncertainty take priority over filling missing history.

The completed development test exposed instruction-following gaps despite valid ledger transport and short notes. A subsequent candidate should strengthen durable reminders for fresh observations and warning-ledger upkeep, then test whether warning feedback changes actual choices. These are proposed next changes, not fixes already implemented or validated. Repeated runs are needed for consistency. Preserve v3 until evidence supports a replacement. The required real presentation MP4 is still missing.
