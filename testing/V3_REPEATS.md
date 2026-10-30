# Unchanged v3 repeat — 29 October 2026

The user requested one fresh test of unchanged v3 to investigate whether its original 64.52 result was unusually favourable. Run `20261029T224759Z` completed the same 48-month game at **L5**, scoring **56.47/100**, after a service interruption and verified same-session recovery. This is a recovered local test, not an uninterrupted replication or an official competition score. No further game was started.

## Source and execution

The tested source was restored v3 commit `9132de57e87f53ff0b3e5105c76b94a1bb46a03e`, whose strategy matches the original submission at `545f06be3cd09fb26d6a62266ea07a3534ea0b0f`. An isolated, ignored submission snapshot reproduced all three original measured SHA-256 hashes from [v3-summary.json](results/v3-summary.json), including original line endings. Development validation passed for its six submission files. The manifest and both installed Skills matched that snapshot before play and again after recovery; the source hashes were unchanged at the ending. Neither branch was checked out or altered to prepare the test.

Model `deepseek-v4-flash`, JiuwenSwarm exactly `0.2.4b3`, and agent mode were retained. Credentials were checked without display; no hosting preferences, dependency changes, dataset changes, memory tools or strategy edits were introduced. The evaluated agent used the official simulation tools. The preliminary package and all historical reports/summaries remain unchanged. See the [new sanitised summary](results/v3-repeat-2-summary.json) for provenance and hashes.

## Recovery and metering limitations

The local JiuwenSwarm service stopped during Month 30. The runner exited with a WebSocket connection reset before writing a complete report. Its last observation showed the game alive at L4; this was not a returned elimination. The service was restarted, and a separate MCP client used only the documented official `observe` tool to verify the known game ID and current state. No database, engine package, dataset or private state was inspected.

The same game and original agent conversation were continued with the official runner's continuation template and public drive transport, supplying that verified session ID. The known-broken CLI `--continue` path that supplies `unknown` was avoided. There was no reinstall, runner source patch, new tactical instruction or replacement game. Original logs were preserved in one segment, continuation logs in another. Exactly **one `new_game` call** was observed across the combined actor logs; the continuation exited normally. A derived recovery report and separate readable replay were retained outside the submission.

This recovery can affect available context and makes the run less comparable with an uninterrupted trial. The first segment captured **no usage summary** before interruption. Full-run tokens, tokens per survival month and reported total cost therefore remain **unavailable**, not zero. The continuation stream reported 11,607,615 tokens and USD 0.256832; those figures are not substituted for whole-run metering or an account balance.

## Observed outcomes

| Metric | Original v3 | Unchanged v3 repeat |
| --- | --- | --- |
| Execution | Uninterrupted local completion | Service interruption at Month 30; same game recovered |
| Completion | 48 months, L5 | 48 months, L5 |
| Quantitative score | 64.52 | 56.47 |
| Six-month grades | C, C, B, B, B, B, A, A | C, C, C, B, B, B, B, A |
| Promotion months | 12, 18, 30, 48 | 12, 24, 30, 48 |
| Ending Health / Dignity | 10 / 10 | 8 / 10 |
| Ending Skill | 96 | 101 |
| Ending Network | 37 | 37 |
| Ending Output | 30 | 28 |
| Ending Wealth | 25.4 | 28.7 |
| Reported full-run tokens | 48,614,866 | Unavailable |
| Reported full-run cost, USD | 0.936443 | Unavailable |

The final official MCP observation reports `completed: true`, outcome `completed`, and 48 survival months. Its Month 49 display is a terminal state after the career. The generic terminal `failed` flag carries the completion reason and is not classified as elimination. The original runner's exit code 1 records the interruption; the continuation exit code 0 is recorded separately.

## What accounts for the returned score gap

These are the components awarded in the two returned ending reports, not assumed permanent scoring formulas or promotion gates:

| Component | Original awarded points | Repeat awarded points |
| --- | --- | --- |
| Career level | 15.00 | 15.00 |
| Wealth | 6.35 | 7.18 |
| Health and Dignity | 15.00 | 13.50 |
| Skill | 12.00 | 12.62 |
| Risk control | 10.00 | 2.00 |
| Network | 6.17 | 6.17 |
| Total | 64.52 | 56.47 |

The risk-control component accounts arithmetically for **8.00 of the 8.05-point difference**. That identifies where the scores differ, not why the underlying risk outcomes differed. Event trajectories, model decisions and recovery remain potential influences. The repeat's returned risk-control dimension was 20/100, versus 100/100 originally. No hidden counter, threshold or prevention formula is inferred.

## Actual adherence observations

- The repeat selected **Defuse legacy risk in Month 12**, verified against the offered choice and returned action result. The original recorded v3 run selected it zero times. An attempt at mitigation did not establish that every concern cleared; the low ending risk-control component remains an observed limitation.
- Actor logs contain four Skill loads, one handbook, one new game, **195 observations**, **205 action calls** and two log lookups. The separate recovery verification added one manual official observation outside those actor counts. IDs were deduplicated across streamed wrappers and both segments.
- **Twelve action calls lacked an intervening observation**; two action notes were empty. No unsuccessful action result, missing action result or action after the terminal observation was found. There was one consecutive observation pair; these counts alone do not establish whether a call was unnecessary, especially during recovery.
- Main actions verified from fresh observations were 15 key projects and one report to the manager. Some Energy choices lacked fresh observations, so complete Energy-action totals are not asserted from cached phase/choice labels. The summary explicitly scopes those classified counts to fresh observations.
- Unsupported numerical benefit claims and comparisons of unrelated raw statistics persisted. Some notes assumed mitigation or comfortable Health established broader safety. Intended safeguards are not proof of reliable adherence, even in a completed L5 run.
- The candidate's monthly-check rubric is **not applicable** to unchanged v3; it is not penalised for omitting a feature it does not contain. Repetition and action variety are not objectives in themselves.

## Interpretation and next experiment

The two recorded v3 scores are **56.47 and 64.52**, with an observed range of **8.05 points** and a descriptive mean of **60.50**. Both games completed at L5, but one required recovery. Those two observations do not establish a stable average, variance, completion probability or expected score for uninterrupted v3.

The original 64.52 was not reproduced. It could have been a favourable trajectory; the new result does not prove that luck alone explains the difference. Variation in progression was already visible before interruption: Month 18 returned C rather than B, and L3 came in Month 24 rather than Month 18. L4 and L5 timing later matched the original. Network alone is not an explanation: both runs ended at 37, while their scores and earlier grades differed.

Keep main on unchanged v3 while collecting evidence. If further paid tests are explicitly requested, run several uninterrupted unchanged-v3 games before repeated frozen-candidate games. Keep all runs, disclose failures and interruptions, audit actual adherence, and record source hashes, completion/failure category, reviews, promotions, quantitative score and valid metering. Do not revise strategy during a batch or infer event answers and hidden thresholds. The repeated uninterrupted baseline batch and repeated candidate batch remain pending.

## Verification

The exact original strategy hashes and installed copies were checked before play and recovery, and the source remained unchanged at the ending. The original v3 score report's saved checksum was verified unchanged. The new summary's score, reviews, promotions and ending statistics come from the official returned outputs; full-run usage is explicitly unknown. Original segments were not edited, and no executable recovery/audit helper is placed in the submission.

Post-run checks passed: the curated ending and component totals match the official returned ending; metering is scoped correctly; source snapshot validation still passes for six files; the current candidate development check passes; `git diff --check` passes; non-disclosing scans exclude credentials and the new private session/conversation IDs from changed public files. Manifest, Skills, runner, dependencies and prior sanitised summaries were not edited. This was an evidence/documentation update, with no new prose-presence tests or additional model game.

The real English presentation MP4 remains missing, so no scored-ready package or recording is claimed.
