# Real development tests

Model: `deepseek-v4-flash`; JiuwenSwarm: `0.2.4b3`; mode: `agent`. These runs occurred on 28–29 October 2026 through the official runner. They are development evidence, not official scores.

| Version | Run identifier | Result | quantitative_score | Reported tokens | Reported model cost |
| --- | --- | --- | --- | --- | --- |
| Baseline v1 | 20261028T172641Z | Reached Month 36 at L4; interrupted by connection/DNS error | Unavailable | Zero-filled report unreliable | Unavailable |
| Resume attempt | 20261028T202117Z | Unknown session ID; replacement started and stopped | Unavailable | Unavailable | Unavailable |
| Revision v2 | 20261028T202638Z | Eliminated in Month 3 through Health failure | 21.77/100 | 1,059,570 | USD 0.029506 |
| Restored v3 on main | 20261028T203013Z | Completed 48 months at L5 | 64.52/100 | 48,614,866 | USD 0.936443 |
| Phase 3 v4 candidate | 20261029T170511Z | Trust-related elimination in Month 39 at L4 | 42.12/100 | 39,636,793 | USD 1.184291 |
| Monthly-check candidate | 20261029T194156Z | Completed 48 months at L4 | 49.33/100 | 63,191,426 | USD 0.742856 |
| Unchanged v3 repeat, recovered | 20261029T224759Z | Completed 48 months at L5 after service interruption and same-session recovery | 56.47/100 | Full run unavailable | Full run unavailable |

V3 ended with Health 10, Dignity 10, Skill 96, Network 37, Output 30 and Wealth 25.4. See [the sanitised summary](results/v3-summary.json). Original logs/reports remain on the originating machine under ignored `.career_sim_runner/`; they are not in a fresh clone. The curated summary omits private paths, credentials, event text/sequences, and internal formulas. It is not the original full score report.

V4 scored 22.40 points below v3. Tokens per survival month were approximately 0.35% higher, despite lower total tokens over a shorter career. V3 remains the better measured baseline on `main`; the candidate is not an upgrade. See the [v4 summary](results/v4-summary.json) and [PHASE3.md](PHASE3.md) for source hashes, the actual adherence audit and limitations. No strategy was changed during the run.

After the v4 merge, the actual `solution/` on `main` was restored from v3 commit `545f06b`. Its manifest and both Skill files were checked against the original v3 hashes. This restoration does not represent another model run or a new score.

## Changes and limitations

The user-requested unchanged-v3 repeat reproduced all three original strategy hashes at source `9132de5`. It completed the same 48-month game at L5 with **56.47/100** after a local service interruption in Month 30. The game ID was verified through official `observe`, and the original conversation continued with the official continuation template; no replacement game, strategy edit or runner patch was made. Full-run usage is unavailable because the first segment captured no usage summary. Continuation-only metering is not a whole-run total.

V3 now has two observed scores, **64.52 and 56.47**, with a descriptive mean of **60.50** and two L5 completions, one recovered. That small, mixed-execution sample does not establish a stable average or variance. The repeat's grades were C, C, C, B, B, B, B, A; promotions occurred in Months 12, 24, 30 and 48. The returned risk-control contribution fell from 10 points to 2, accounting arithmetically for 8 of the 8.05-point gap; the cause of different risk outcomes is uncertain. See [V3_REPEATS.md](V3_REPEATS.md) and the [new sanitised summary](results/v3-repeat-2-summary.json). Historical summaries and reports were preserved. No further game was started.

The separate `codex/v3-monthly-checks` strategy at `3facd6e` completed one user-requested game: **49.33/100**, 48 months, L4. It did not demonstrate an upgrade over v3. Grades were C, C, B, B, B, B, B, B; promotion months were 12, 18 and 36. A conservative manual audit found 0/48 unambiguous full monthly checkpoints, although all 48 first notes named the month and some notes used returned feedback. Reported tokens per survival month were 1,316,488, about 29.98% above the single v3 run; lower reported USD cost is not proof of token efficiency. The [full audit and pending repeated-test plan](MONTHLY_CHECKS.md) and [sanitised summary](results/monthly-check-summary.json) keep source hashes, adherence and outcomes separate from the original v3/v4 evidence. Further paid games require an explicit request; no repeated baseline batch has been run.

- Baseline warnings often did not lead to mitigation comparison; notes claimed effects unsupported by the next observation. V2 made the intended checks explicit.
- V2 accepted optional demands while Health fell, relying on future recovery. It died first. V3 explicitly prioritised preserving the ability to reach recovery.
- V3 completed, but numerical predictions and omitted mitigation comparisons persisted. Both Skills were loaded, and installed hashes matched source. These remain instruction-following limitations.

One full completion is not proof of consistency or causation: event trajectories differ. Costs are not an account balance. Do not describe the interrupted baseline as a completed 36-month survival result or the replacement as a resumed game.

## Teammate test procedure

1. Make one coherent strategy change on a branch. Keep the pinned dependencies, designated model, official server, and agent mode. No named-event answers or inferred hidden formulas.
2. Run the key-free check, then coordinate paid runs within the shared credit budget.
3. Play a fresh game and preserve original outputs. Record strategy commit/version, `completed`, survival months, `quantitative_score`, tokens, reported cost, observed failures, and changes. Label interruptions incomplete.
4. Inspect the transcript, events, and replay for Skill loading and actual adherence. Distinguish prediction, observed change, and uncertain causal explanation.
5. Compare multiple runs by completion rate, average/worst score, and tokens per survival month. Keep the previous tested solution available until a candidate is assessed. Do not optimise against a memorised event sequence.
6. Add only a sanitised summary here. Keep raw logs private and outside Git. Align design documents and video claims with the submitted version.

The generic cases in `WORKING_CHECKLIST.md` are hypothetical desk checks, not extra real runs.
