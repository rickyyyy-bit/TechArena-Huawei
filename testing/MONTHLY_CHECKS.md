# V3 plus monthly performance checks — candidate

Branch: `codex/v3-monthly-checks`. The review started from existing candidate commit `29515b1040d48a4f172b87b8fefb4e2d43426538` and completed that routine rather than adding it twice. The user then requested one fresh game of published strategy commit `3facd6ef72fe2482f14a0de93f8fcb3e93b2f784`: it completed 48 months at L4 with **49.33/100**. This is one local result, not an upgrade or official score. The real English presentation MP4 is missing; the scored package is not ready.

## Versions and evidence

| Version | Source | Actual local evidence |
| --- | --- | --- |
| Original tested v3 | Original `545f06be3cd09fb26d6a62266ea07a3534ea0b0f`; restored unchanged on `main` at `9132de57e87f53ff0b3e5105c76b94a1bb46a03e` | One completed 48-month game at L5, 64.52/100 |
| Unsuccessful v4 | `07d8214`, archived on `codex/phase3-skills` | 42.12/100; trust-related elimination in Month 39 despite Health 10 and Dignity 8 |
| Monthly-check candidate | `3facd6ef72fe2482f14a0de93f8fcb3e93b2f784`, based on restored v3 | One completed 48-month game at L4, 49.33/100; monthly adherence was unreliable |

The v3 diagnostic evidence motivating the experiment records promotions in Months 12, 18, 30 and 48, and six-month grades C, C, B, B, B, B, A and A. It selected key projects in 14 of 16 quarters and spent 25 Energy preparing reports. Some repeated report preparations showed no observed Output increase while notes continued predicting increases. Recurring organisational warnings did not lead to the explicit “Defuse legacy risk” action. These observations motivate checking feedback; they do not establish that repetition is bad or that a specific alternative would have improved the result.

Promotion considers sustained results and factors including Skill, Network and Output; exact thresholds are unpublished. V3 already had Network 36 in Months 36 and 42 without reaching L5. Network alone does not explain its late promotion, and unrelated raw statistics cannot be ranked as if they share a scale.

V4 changed several behaviours together. Its official notes/log transport worked, but omissions, stale fields and skipped observations remained. Neither its lower score nor v3's completion isolates the effect of an individual change. Original reports/logs and curated historical summaries remain unchanged; see [RESULTS.md](RESULTS.md) and [PHASE3.md](PHASE3.md).

The historical comparisons below use the original v3 run at 64.52 only. A later unchanged-v3 repeat scored 56.47 and completed at L5 after recovery; see [V3_REPEATS.md](V3_REPEATS.md). Do not interpret the original score as typical or the earlier single-run gaps as causal effects of the monthly routine.

## One change under test

At the first story decision each month, reuse the observation and available context to compare the previous priority with actual returned feedback and trends. Missing evidence remains unknown. Choose one priority from the latest formal review and present needs, such as dependable delivery, communicating completed work or collaboration. Put month, observed progress or unknown, and current priority in that first ordinary action's notes. Use it in offered story choices and quarterly Energy/main-action comparisons. Reconsider the priority or action when returned results contradict expectations.

V3's survival and persistent-warning checks still govern. A serious competing need can displace performance, with a brief explanation. A goal does not mean accepting every extra task; no useful growth offer calls for the most defensible legal choice. Repeating an action is acceptable when justified by evidence; variety is not an objective. Improved current feedback does not establish that every organisational concern has cleared. Do not invent action deltas, hidden caps or future recovery opportunities.

This is a participant planning routine, with formal reviews still six-monthly. It creates no grades, Energy, actions or simulation phase. There is no observation/log call or repeated plan recital solely for the checkpoint. Current context and official notes/logs may resolve a consequential uncertainty when needed; missing history is not grounds for a checkpoint-only lookup. No workspace memory, memory tools, embeddings, ledger format or support file is introduced. Stop at the ending.

## Explicit desk review — 29 October 2026

These are hypothetical instruction-coverage findings from reading the manifest and both Skills. No model or simulation was used; “covered” describes intended instructions, not demonstrated behaviour.

| Hypothetical case | Required handling and coverage found |
| --- | --- |
| First month, no previous plan | Event checkpoint step 1 starts now; label prior progress unknown and choose a current priority. No fabricated history. |
| Missing review feedback or history | Event steps 1–2 and quarterly step 2 use present evidence; unavailable prior goal/review stays unknown. No checkpoint-only observation/log call. |
| No useful growth option offered | Event conflicts section compares legal options for present needs. Do not invent an offer, accept unnecessary workload, or create another action. |
| Serious danger overrides monthly priority | Event step 3 and quarterly step 2 apply existing survival/warning checks, explain the competing need, and do not assume later recovery arrives first. |
| Expected progress fails to appear | Both Skills compare returned evidence and reconsider the action or priority. Do not report an unseen gain, infer a hidden cap, or require variety. |
| Quarterly spending aligned with priority | Quarterly steps 2–5 carry the current priority into affordable Energy and offered main-action comparisons, rechecking after each result and explaining risk exceptions. |
| Formal review feedback changes plan | Event checkpoint step 5 and quarterly step 6 reconsider the priority from actual review feedback. Improved feedback is not blanket risk clearance. |
| Ending without another action or grade | Manifest and both Skills stop on the returned ending. No checkpoint action, extra review or invented monthly grade. |

## Repeated-test plan — still pending

The user authorised the single preliminary candidate game recorded below, then one unchanged-v3 repeat. That later repeat completed at L5 with 56.47 after a same-session service recovery; see [V3_REPEATS.md](V3_REPEATS.md). No additional candidate game was started. Repeated uninterrupted baseline and candidate batches remain pending; further paid games require an explicit request.

Do not start paid model games until explicitly requested. After authorisation and shared-credit coordination, run repeated unchanged-v3 baselines first, then repeated frozen-candidate games. Plan three fresh runs of each if the authorised budget permits; any smaller batch must be labelled preliminary. Keep the model `deepseek-v4-flash`, JiuwenSwarm exactly `0.2.4b3`, agent mode, public runner and routing unchanged. No provider preferences. Change one major behaviour at a time and do not revise strategy during a batch.

Before each run, record the full source commit (`git rev-parse HEAD`), branch, clean/dirty status and any diff, plus SHA-256 of `solution/manifest.json` and both `SKILL.md` files. Use the baseline hashes in [v3-summary.json](results/v3-summary.json) to verify unchanged v3. Record candidate hashes from the frozen source; never label the starting commit `29515b1` as this revised candidate. Verify installed strategy hashes using the public runner's installed submission copies only, without opening simulation packages, datasets, database or private state. Preserve original outputs without editing them.

Reviewed candidate worktree SHA-256 values are below. Hashes identify exact bytes; Git newline conversion can change them between checkouts. Capture actual source and installed bytes for each real run, and distinguish newline changes from strategy edits. The published revision's full commit must be recorded when selecting the frozen test source.

| Strategy file | Reviewed SHA-256 |
| --- | --- |
| `solution/manifest.json` | `df713c418ac0dddc85b203117e5a2b79ec2eff04b9f097925c0f41a45397a76c` |
| `solution/skills/event-decisions/SKILL.md` | `c95f2e985aef3d61479cf2198fa5aa72bd1ec4236ad7f3fb5f4205fcd514db14` |
| `solution/skills/quarterly-planning/SKILL.md` | `9568dc94756579c73bd49c8e998e31580230ad38d39ea82bf185483298c35f1d` |

For each run retain a separate review record with these fields:

| Field | Required evidence |
| --- | --- |
| Provenance | Full source commit, branch, strategy hashes, installed-copy hash match, run ID, model/version/mode, any source changes |
| Monthly adherence | One row per month with a first story decision: first action reference, checkpoint present/late/missing, prior progress supported/unknown/unsupported, current priority, latest available review, and evidence for the choice or risk override |
| Carry-forward and adaptation | Quarterly Energy/main-action references and relationship to priority; contrary result, reconsideration and subsequent choice; repeated plan notes or observation/log calls solely for the checkpoint |
| Outcome | `completed`, survival months, ending level, runner exit code, failure category from returned evidence; distinguish elimination, connection interruption and unknown cause |
| Reviews and promotions | Actual grade with each six-month review month, promotion months and resulting levels; absent feedback stays unknown |
| Quantitative result | Actual `quantitative_score`, not `competition_partial_score`; unavailable ending score stays unavailable |
| Efficiency and cost | Reported input/output/total tokens and USD cost; total tokens divided by reported survival months when both are valid and months > 0; otherwise unavailable |
| Safeguards | Evidence of optional-work restraint, warning/mitigation comparison, survival override, unsupported effect claims, missed observations and any extra checkpoint-only calls |

Count checkpoint adherence over months that actually offer a first story decision, including the first month and an elimination month if eligible. A terminal display with no new story decision is excluded. Report numerator/denominator for on-time checkpoints, supported-or-unknown progress statements and priorities carried into decisions. A checkpoint appearing later that month is late. If evidence is missing, mark adherence unassessable rather than treating it as compliant. Read the actual notes and returned feedback; presence of a keyword alone does not establish adherence. Apply the same safeguard audit to v3 without expecting it to implement the new checkpoint.

Across each batch report completion rate, failure categories, average/worst quantitative score with sample counts and missing results disclosed, actual grade sequences, promotion timing with non-promotions retained, and tokens per survival month plus reported cost. Compare completed and interrupted runs explicitly. One first candidate run would establish whether the model follows the monthly routine on that trajectory and record its safety, progression and cost; it would not establish causality, consistency, higher grades or promotion beyond L5. Repeated baseline and candidate runs can help assess variability and whether a larger comparison is warranted. Different trajectories remain a limitation. Replace v3 only after evidence supports that decision.

## Actual candidate game — 29 October 2026

Run `20261029T194156Z` used the exact frozen strategy commit `3facd6ef72fe2482f14a0de93f8fcb3e93b2f784`, designated model, pinned JiuwenSwarm and agent mode. The source tree was clean before play. Installed manifest/Skill copies matched source; the three strategy hashes above remained unchanged after play. A first launcher attempt stopped before model contact because the command search path lacked the installed runner tools; correcting that process-local path started the one fresh game. There was exactly one `new_game` call. No strategy, credential or hosting-route setting changed during play.

| Metric | Tested v3, one run | Monthly candidate, one run |
| --- | --- | --- |
| Completion | 48 months, L5 | 48 months, L4 |
| Quantitative score | 64.52/100 | 49.33/100 |
| Six-month grades | C, C, B, B, B, B, A, A | C, C, B, B, B, B, B, B |
| Promotion months | 12, 18, 30, 48 | 12, 18, 36 |
| Reported total tokens | 48,614,866 | 63,191,426 |
| Tokens per survival month, rounded | 1,012,810 | 1,316,488 |
| Reported model cost, USD | 0.936443 | 0.742856 |

The official runner report says `completed: true`, outcome `completed`, survival months 48 and process exit code 0. The terminal Month 49 display is the state after the 48-month career, not 49 survival months. Its generic terminal flags include `failed: true` with the reason “Completed the 48-month simulation.”; that flag is not an elimination classification. Ending Health and Dignity were 10, Skill 76, Network 36, Output 26 and ending-score Wealth 23.3 (the rounded terminal observation showed 23). Original report and event/transcript logs were preserved; a separate replay and private audit were generated from those returned outputs. See the [sanitised summary](results/monthly-check-summary.json).

### Actual adherence audit

This is an audit of real returned notes and observations, separate from the hypothetical desk review. All 48 first ordinary story notes were manually reviewed for the prior-priority comparison, observed evidence or unknown, and one current priority. No exact phrase was required. Narrative follow-through or references to a review were not credited as a complete checkpoint when the link to the previous monthly priority was unclear. This assesses documented adherence, not hidden model reasoning; the interpretation is deliberately conservative.

- All **48/48** first story notes named the month. **0/48** unambiguously documented the complete checkpoint routine. The first two explicitly labelled a priority; this literal-label count is descriptive, not a compliance test. Several later notes used story outcomes or formal feedback, so the result does not mean all feedback-led reasoning was absent. Missing history was not consistently labelled unknown.
- Carry-forward into quarterly spending was not reliably demonstrated because a monthly priority was usually unclear. Some quarterly notes did respond to C reviews and to survival needs. Early recovery and restraint were observed, and the run completed; that does not establish that every organisational concern cleared.
- Unique calls: two Skill loads, one handbook, one new game, **209 observations**, **209 actions**, **zero log calls**. One final-quarter action lacked an intervening observation; there were no consecutive observation pairs, unsuccessful actions or actions after the terminal observation. The log count shows no checkpoint-only log calls; tool counts alone cannot prove the purpose of every observation.
- Quarterly Energy: 17 Health recovery, 15 Network maintenance and **16 report preparations**. Main actions: **13 key projects**, two reports to the manager and one mentorship. Both “Defuse legacy risk” and “Lay low and reduce risk” were offered across all 16 quarters; neither was selected. Quarterly notes did not document the intended organisational-warning/mitigation comparison.
- Of **15 isolated report-preparation comparisons**, the next returned Output was unchanged **six** times and increased nine times. One final-quarter comparison included intervening actions and was excluded. Unsupported numerical effect predictions and raw-stat rankings remained. Repetition itself is not a failure, and no hidden cap or causal explanation is inferred.

The candidate scored **15.19 points below** the original v3 completion, reached L4 six months later and did not reach L5. Reported tokens per survival month were **29.98% higher**. Lower reported USD cost does not establish lower token use or an efficiency gain caused by the strategy; cost is not an account balance. These are different single trajectories, not a controlled comparison. The monthly routine did not demonstrate reliable adherence or improvement, and **main remains on tested v3**. No additional monthly-candidate game was started.

Evidence-record checks passed: the curated outcome, score, usage, grades and promotions match the original outputs; the original score-report checksum remained unchanged after replay/audit generation; manifest/Skill hashes still match the tested source; development submission validation and the non-disclosing credential scan passed; `git diff --check` passed. This update changes evidence/documentation only. The 121 key-free tests above were run before the game; no strategy or test code changed afterward. Final packaging remains blocked by the real missing MP4.

## Separate future experiments

- Warning/risk tracking and verified clearance, including durable official-note recovery and stale-field handling. V4's ledger transport alone did not establish reliable mitigation.
- Operating bands or Network-specific targets. No new bands or targets are part of this candidate; no unpublished numerical gate is inferred.
- Token/prompt-budget or observation-cadence redesign. Measure actual use first; source brevity is not a token-saving result.
- Workspace memory only if written organiser confirmation is obtained; no memory files, `read_memory`, `write_memory` or embeddings now.

## Key-free verification

Verification completed on 29 October 2026:

- Full existing key-free suite: **121 passed**, including **36 contract/validation tests** and **8 packaging tests**. No prose-presence tests were added.
- `python scripts/submission.py check --credentials`: passed for all six submission files, exact JiuwenSwarm `0.2.4b3`, agent mode, designated model and allowed local settings. Values were not displayed; the existing credential scan passed.
- Official submission validation, helper final check and package command each refused the missing `solution/presentation.mp4`, as expected. No final archive or recording was fabricated. Packaging fixture tests check export isolation, hash retention and rejection paths; they do not validate a real video.
- `git diff --check`: passed. Manual review covers all eight cases above and preserves v3's existing survival and persistent-warning instructions. Only strategy prose and documentation changed; no runner, helper, tests, dependency, model, routing, credential, preliminary submission or historical run artifact changed.
- The original v3 manifest instruction is retained verbatim before the monthly extension. `main` and refreshed `origin/main` remain at `9132de5`, with `solution/` identical to `545f06b`. A non-disclosing check excluded the existing local credential from every changed file.

The first suite attempt hit Windows temporary-folder permissions (79 passed, 42 setup errors); an attempt with a fresh repository-local temp directory then stalled at an asynchronous test and was stopped. The full suite passed with normal local execution and a fresh repository-local temp directory, without modifying tests or making model calls. These environment retries are not gameplay evidence.

These structural/packaging checks and the desk review did not demonstrate model adherence or gameplay improvement. The later single model game is recorded separately above and showed unreliable adherence. Final submission remains blocked by the missing real MP4.
