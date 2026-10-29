# Submission working checklist

This file retains the original maintainer's local audit history. For commands that work on a teammate's fresh clone, use [TEAM_GUIDE.md](TEAM_GUIDE.md); for sanitised evidence and final release steps, use [testing/RESULTS.md](testing/RESULTS.md) and [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md). Local `.tools/` files and raw run outputs mentioned below are intentionally not published.

Current branch note: `codex/v3-monthly-checks` completes the existing untested monthly-performance routine from `29515b1`; the historical v3 completion below remains evidence for `main` only. The eight-case instruction desk review and prepared repeated-baseline/candidate test plan are in [testing/MONTHLY_CHECKS.md](testing/MONTHLY_CHECKS.md). No paid game was started for this revision. The real MP4 remains missing.

29 October update: the actual `solution/` on `main` is restored to v3 from `545f06b`, with the original manifest and Skill hashes verified. V4 scored 42.12 and failed in Month 39; its source remains on `codex/phase3-skills`. [testing/PHASE3.md](testing/PHASE3.md) retains that experiment's audit; the earlier audit below is historical.

Verified on 28 October 2026 against the public docs in official repository commit `00b084a88732d81e595db88b26dde90d44e72d87`. The website fetch failed; the official repository documentation was used instead. Source checkout: `official/`; working runner files were copied unchanged to the workspace root, apart from local ignore additions.

- First cutoff: 24:00 GMT on 27 October = 00:00 GMT on 28 October (already passed on today's date). Next: 24:00 GMT on 30 October = 00:00 GMT on 31 October. Final: 24:00 GMT on 1 November = 00:00 GMT on 2 November. Later key expiry in the organiser email does not extend submission cutoffs.
- Organiser email supplies API_BASE `https://openrouter.ai/api/v1`, MODEL_NAME `deepseek-v4-flash`, USD 50 limit, competition-only use, and a key-use period through 2 November. Use only the three supplied environment values; no hosting-route preferences. User saved the key locally; presence and the other values were checked without displaying the key.
- Exact JiuwenSwarm version 0.2.4b3; `agent` mode in both manifests. Official dependency spelling `0.2.4.beta3` normalises to that version; dependency files are unchanged.
- ZIP must contain exactly one root `solution/` with manifest, README, real English presentation MP4, both design documents, and at least one Skill with valid name/description YAML front matter. All deliverables and spoken video English; video at most ten minutes, original speed.
- Stage 1: 80% mean quantitative score of three official runs, 10% Skill document quality, 10% token efficiency. Only top ten advance to expert review; their final score is 70% Stage 1 plus 30% expert review. Local scores are development evidence only.
- Simulation access only through the five official MCP tools. No private package/dataset/database inspection, fixed named-event answers, unpublished thresholds, prompt injection, harmful scripts, or secret inclusion.
- Team name carried forward from verified preliminary manifest: `Jon8652's team`; current manifest matches that entry.
- Preliminary was verified per user; it is not scored and is preserved unchanged.
- Setup update: portable uv installed locally under `.tools/uv/`; Python 3.12 installed under `.python/`; official `uv sync --locked --python 3.12` succeeded. Installed JiuwenSwarm version verified through package metadata as exactly `0.2.4b3`. Official setup succeeded and copied the three credential settings to the named instance. Instance language set to English and startup invoked. Dependency files remain unchanged. Local tool/cache directories are ignored by Git.
- Official submission validation ran: exit 1, reporting missing `solution/presentation.mp4`. No real recording exists yet.
- Initial data loading failed with Windows error 1314. User then successfully ran the official loader in administrator PowerShell. No package or dataset workaround was applied.

## Test record

Only actual observations are recorded below. A partial run's last observed month is not a completed survival length. Missing scores and unreliable metering remain unavailable.

| Version | Run | Months | quantitative_score | Tokens | Observed failure | Change |
| --- | --- | --- | --- | --- | --- | --- |
| Baseline v1: preliminary Skills | 20261028T172641Z | Reached Month 36, incomplete | Unavailable: empty ending score | Unavailable: report contains zero-filled counters | Model connection/DNS error; warning follow-through and effect claims weak | Explicit warning comparison and observed-effect checks in v2 |
| Baseline v1: official resume attempt | 20261028T202117Z | New game into Month 2, stopped | Unavailable | Unavailable | Runner sent unknown session ID; agent incorrectly started replacement game | v2 manifest reports recovery failure instead of replacing game |
| Revised v2 | 20261028T202638Z | 3, eliminated | 21.77/100 | 1,059,570 total; reported cost USD 0.029506 | Health reached zero before first quarterly recovery | v3 prioritises preserving ability to reach recovery, rather than assuming future recovery |
| Revised v3 | 20261028T203013Z | 48, completed at L5 | 64.52/100 | 48,614,866 total; reported cost USD 0.936443 | Completed; unsupported numerical claims and omitted mitigation comparisons persisted | Immediate Health protection retained; no strategy changes after completed test |

## Hypothetical desk checks (not simulator tests)

| Case | Instruction review result |
| --- | --- |
| Health deteriorating before review | Both Skills compare repair against growth; quarterly procedure rechecks after each spend. |
| Dignity low, Output strong | Procedures examine neglected dimensions rather than continue maximising Output. |
| Weak Network or negative Wealth | Risk checks include relationships and finances; exact failure counters are not assumed. |
| Two-Energy option with one remaining | Quarterly Skill restricts comparison to affordable legal actions. |
| Repeated weak reviews | Review feedback changes next quarter's priority; no promotion threshold inferred. |
| Warning with no visible direct effect for risk action | Consider legitimate warning and uncertainty; no assumed risk counter. |
| Unfamiliar story wording and conflicting gains | Read current offered choices; compare likely directions and tolerable downside. |

These checks show intended coverage, not that a model follows it reliably.

## Remaining workflow

1. Credential presence and three allowed settings checked; no key printed.
2. Dependency installation, exact version verification, official setup and data loading completed.
3. Completed: three strategy-version tests plus the stopped resume attempt, using the official play/score/replay commands behind Makefile targets. The current v3 completed 48 months; its score and replay were inspected. No database or simulation package internals were inspected. Local service was stopped after testing.
4. Record real English video using `PRESENTATION_OUTLINE.md`; update claims to reflect actual evidence, copy to `solution/presentation.mp4`.
5. Run `uv run python -m career_sim_runner validate --submission solution`; inspect all content and video, confirm team name, package one `solution/`, extract into a fresh directory, inspect exact structure and absence of secrets. Do not upload an incomplete draft.
6. User uploads the final ZIP at https://techarena-uk.hydro.ac/ before the applicable cutoff and verifies receipt. No upload has occurred.

## Baseline evidence — 28 October 2026

The user successfully loaded development data through the official loader in an administrator PowerShell. A real single-agent test started at 17:26:41 GMT using the unchanged preliminary Skills and JiuwenSwarm 0.2.4b3. Official output directory: `.career_sim_runner/career_emu/outputs/Jon8652's team/20261028T172641Z`. Simulation session: `f016de801ce94a00a26d4e604c9fdff2`. It stopped after 155 recorded decision steps, during Month 36 at L4. No terminal game state or quantitative score was returned. A model API connection/DNS error appears in service logs. The original report, transcript and event logs are preserved. `make score`'s underlying command was attempted but did not return before cancellation; the original report already showed the empty ending score. The official replay command generated `.tools/baseline-v1-replay.md` successfully.

Baseline observations: numerical action effects were asserted although the public handbook supplies directions only; expected gains were sometimes described as achieved without visible confirmation; persistent risk warnings did not reliably lead to mitigation comparison. An organisational incident occurred in Month 11. This does not establish a hidden causal formula or prove another action would prevent it. Revision v2 addresses the general decision weaknesses without named-event answers or inferred thresholds. Baseline files and hashes are saved under `.tools/baseline-v1/` and `.tools/baseline-v1-hashes.json`. The original submission was unchanged throughout that test.

The official `--continue` path builds its initial continuation prompt with no known game state and supplies `unknown`; this was verified in the public participation runner, not in simulation package internals. The agent started a new game, which was stopped. No fix to the official runner or dependency versions was applied. Fresh v2 and v3 tests followed, as recorded above.

## Current tested version

v3 session `bf32999e444d4b74b81ce98afe88fd83` completed with exit code 0. Score was reconfirmed through the official score command. Replay: `.tools/revision-v3-replay.md`; original outputs: `.career_sim_runner/career_emu/outputs/Jon8652's team/20261028T203013Z/`. Installed Skill hashes matched source after the test. The agent loaded both Skills. Manifest mode and Skill YAML parsing, nonempty text files, and exclusion of the actual locally saved key were checked. No hosting-route settings were added. No upload occurred. Final validation still requires the team's real MP4.
