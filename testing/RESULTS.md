# Real development tests

Current 30 October status: the four-game risk campaign is closed at approximately USD 5.48. Fresh v3 scores 55.25 and 62.83 average 59.04; Risk-01 scored 46.80 with Month 45 elimination; Risk-02 scored 66.38 over 48 months at L5. Adherence and confirmation requirements remain unmet, so improvement is not demonstrated. See [the complete campaign comparison](RISK_CAMPAIGN.md). The dated records below describe their state at the time; original historical evidence is preserved.

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

## 30 October: separate risk follow-through experiment

Uncommitted iteration risk-follow-through-01 continues from the latest monthly candidate evidence commit cc0b210 on codex/risk-follow-through. It replaces the existing quarterly warning reminder with a decision-note procedure; the monthly routine stays unchanged. No new model outcome is available yet. The user allocated USD 10 now; the campaign is bounded by nine games or six hours, with no overlapping games and earlier stops for cost/readiness/metering. See [the predeclared protocol](RISK_FOLLOW_THROUGH.md). All historical reports, logs and curated summaries above remain unchanged. Main remains on tested v3.

Fresh unchanged-v3 pilot on 30 October: run `20261030T021528Z-v3` completed 48 months uninterrupted at L4 with **55.25/100**, grades C, C, C, C, B, B, B, B and promotions 6, 30, 42. Full-stream reported usage: **56,390,812 tokens**, 1,174,808.58 per survival month, **USD 1.443714**. Eight mitigation attempts and 10 returned risk-control points do not establish a causal prevention rule. Frozen/installed checks passed; no post-terminal action or fresh-state omission was found. This one fresh score is not a baseline batch or an expectation. See [the new summary](results/v3-repeat-3-summary.json) and [campaign record](RISK_FOLLOW_THROUGH.md). The cost-conscious frozen candidate pilot is in progress; no upgrade is claimed.

Frozen risk-follow-through-01 pilot `20261030T025849Z-risk-01`: **46.80/100**, trust-related elimination in Month 45 at L4, uninterrupted. Grades C, C, C, B, B, B, B; promotions 12,24,30. Full-stream usage **60,339,333 tokens**, 1,340,874.07 per survival month, **USD 1.554331**. The elimination is retained; it is not a service failure or completion despite exit0. In ten current-HR-warning primary notes, five Energy comparisons were full and all five main comparisons partial. It fails the predeclared completion/adherence screens. No causal prevention claim follows. See [the separate outcome](results/risk-follow-through-01-summary.json). The next uncommitted [risk-02 revision](RISK_FOLLOW_THROUGH_02.md) clarifies current-phase protective versus growth alternatives and relevant published directions, using the same USD10 total campaign allocation and preserving monthly/survival rules. No upgrade is demonstrated.

Audit correction: official returned choices expose `status_updates` amounts, including in preserved original-v3 and monthly records. Handbook-only absence does not make matching numerical predictions invented. Keep original records unchanged and read their blanket numerical-claim findings with [this correction](AUDIT_CORRECTION.md). Actual-result mismatches, unjustified clearance, raw-stat rankings and outcome differences remain separate questions. No score or raw run was changed.

Risk-02 pilot `20261030T040427Z-risk-02` completed48 months atL5 with **66.38/100**, grades C,B,B,B,B,A,A,B and promotions6,12,24,42. Full usage50,055,512 tokens,1,042,823.17 per survival month, USD1.223468. Source/installed/config checks passed; no post-terminal action or fresh-state omission. It exceeds the first fresh v3 control by11.13 but is one trajectory, with lower returned risk-control contribution(5 versus10). The core risk-comparison audit is6/8 explicit/recent-risk cases, or6/10 including uneasy cues; target80% not met. See [the separate summary](results/risk-follow-through-02-summary.json) and [corrected numerical-metadata interpretation](AUDIT_CORRECTION.md). A further unchanged-v3 control is in progress; no upgrade is declared or published.


## Closed risk campaign — final update, 30 October

The second unchanged-v3 control, `20261030T045759Z-v3`, completed 48 months at L5 with **62.83/100**. Grades were C, B, B, B, A, A, B, B; promotions 6, 12, 18, 36. Full-stream usage: 52,391,577 tokens, 1,091,491.19 per survival month, USD 1.258105. All frozen source/installed/config checks passed; two Energy-spending decisions lacked a fresh state after success-only responses. No missing result or post-terminal action occurred. See [its separate summary](results/v3-repeat-4-summary.json).

Fresh v3 mean: **59.04** across two completions. Risk-02's single 66.38 is 7.34 higher, but its explicit/recent-risk comparison is 6/8 (75%), or 6/10 (60%) including uneasy cues, below the 80% target. Monthly component review found 32 complete and 16 partial first story notes, with repeated checkpoint preambles in all 96 later notes. No confirmation game was bought. Risk-01's 46.80 trust elimination remains included and separate from Risk-02.

All four new games were uninterrupted with complete stream metering. Reported cost sum USD 5.479618; fixed-start shared-key usage increase approximately USD 5.481222, a distinct scope. Testing stopped to minimise spend while meaningful execution gaps remain; about USD 4.52 of the USD 10 allocation was unused. No more paid game is queued. Improvement is not demonstrated. Risk-02 remains an uncommitted experiment; main stays v3. All 121 tests passed, historical evidence is preserved, and the real English MP4 remains missing. See [decision, limits and next experiment](RISK_CAMPAIGN.md) and [machine-readable comparison](results/risk-campaign-comparison.json).
