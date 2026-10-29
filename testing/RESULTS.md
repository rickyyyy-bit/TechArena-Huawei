# Real development tests

Model: `deepseek-v4-flash`; JiuwenSwarm: `0.2.4b3`; mode: `agent`. These runs occurred on 28–29 October 2026 through the official runner. They are development evidence, not official scores.

| Version | Run identifier | Result | quantitative_score | Reported tokens | Reported model cost |
| --- | --- | --- | --- | --- | --- |
| Baseline v1 | 20261028T172641Z | Reached Month 36 at L4; interrupted by connection/DNS error | Unavailable | Zero-filled report unreliable | Unavailable |
| Resume attempt | 20261028T202117Z | Unknown session ID; replacement started and stopped | Unavailable | Unavailable | Unavailable |
| Revision v2 | 20261028T202638Z | Eliminated in Month 3 through Health failure | 21.77/100 | 1,059,570 | USD 0.029506 |
| Restored v3 on main | 20261028T203013Z | Completed 48 months at L5 | 64.52/100 | 48,614,866 | USD 0.936443 |
| Phase 3 v4 candidate | 20261029T170511Z | Trust-related elimination in Month 39 at L4 | 42.12/100 | 39,636,793 | USD 1.184291 |

V3 ended with Health 10, Dignity 10, Skill 96, Network 37, Output 30 and Wealth 25.4. See [the sanitised summary](results/v3-summary.json). Original logs/reports remain on the originating machine under ignored `.career_sim_runner/`; they are not in a fresh clone. The curated summary omits private paths, credentials, event text/sequences, and internal formulas. It is not the original full score report.

V4 scored 22.40 points below v3. Tokens per survival month were approximately 0.35% higher, despite lower total tokens over a shorter career. V3 remains the better measured baseline on `main`; the candidate is not an upgrade. See the [v4 summary](results/v4-summary.json) and [PHASE3.md](PHASE3.md) for source hashes, the actual adherence audit and limitations. No strategy was changed during the run.

After the v4 merge, the actual `solution/` on `main` was restored from v3 commit `545f06b`. Its manifest and both Skill files were checked against the original v3 hashes. This restoration does not represent another model run or a new score.

## Changes and limitations

The separate `codex/v3-monthly-checks` branch is an untested monthly-performance candidate, first published at `29515b1` and subsequently reviewed. It has no model score and must not inherit v3's result. Its [desk review and real-test plan](MONTHLY_CHECKS.md) call for repeated unchanged-v3 baselines followed by repeated frozen-candidate games only after explicit paid-test authorisation, recording source commit/hashes and actual monthly adherence alongside outcomes, grades, promotions, score and efficiency. No new model run is added to the historical table above.

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
