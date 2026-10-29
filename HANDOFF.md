# TechArena entry handoff — 28 October 2026

This is the maintainer's historical test/release record. Machine-specific paths and ignored `.tools/` outputs below are local evidence locations, not files provided by a fresh clone. Teammates should start with [TEAM_GUIDE.md](TEAM_GUIDE.md), [testing/RESULTS.md](testing/RESULTS.md), and [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md).

The current v3 agent completed a real 48-month local game with quantitative score **64.52/100**, ending at **L5**, Health **10**, Dignity **10**, Skill **96**, Network **37**, and Wealth **25.4**. This is local development evidence, not an official competition score. One full completion does not establish consistency.

The entry is **not yet valid for scored submission** because the team has not supplied a real English `solution/presentation.mp4`. The draft ZIP is deliberately named `solution-draft-video-missing.zip`; do not upload it as a final entry.

## Prepared files

- `solution/manifest.json`: team `Jon8652's team`, taken from the verified preliminary entry; mode `agent`.
- `solution/README.md`: entry summary and honest testing status.
- `solution/design/skills_design.md` and `decision_report.md`: implemented responsibilities, public sources, actual development evidence, tradeoffs and unresolved limitations.
- `solution/skills/event-decisions/SKILL.md` and `quarterly-planning/SKILL.md`: English prose Skills with valid YAML front matter. No executable Skill files or event answer tables.
- `PRESENTATION_OUTLINE.md`: English speaking outline covering the five official questions in order, updated with actual earlier/later run evidence.
- `WORKING_CHECKLIST.md`: verified requirements and test history.

## Evidence

| Version | Result | Local quantitative score | Reported total tokens | Reported model cost |
| --- | --- | --- | --- | --- |
| Baseline v1 | Reached Month 36 at L4; connection failure; incomplete | Unavailable | Unreliable zero-filled report | Unavailable |
| Official resume attempt | Runner supplied unknown session ID; started replacement game; stopped | Unavailable | Unavailable | Unavailable |
| Revision v2 | Eliminated in Month 3 when Health reached zero | 21.77/100 | 1,059,570 | USD 0.029506 |
| Current v3 | Completed 48 months at L5 | 64.52/100 | 48,614,866 | USD 0.936443 |

The reported costs are not a complete account balance or a reliable total for all attempts. No remaining-credit claim is made.

Current v3 original report: `.career_sim_runner/career_emu/outputs/Jon8652's team/20261028T203013Z/score_report.json`. Its transcript and event log are beside it. Readable replay: `.tools/revision-v3-replay.md`. Original reports and logs were not manually edited. The official score command reconfirmed completion and score; the official replay command generated the readable replay.

The baseline motivated explicit mitigation comparisons and observed-effect checks. The v2 failure motivated protecting the ability to reach recovery rather than assuming a future quarter would arrive first. V3 finished, but numerical effect claims and mitigation comparisons remained unreliable. Different event trajectories prevent a controlled causal claim. The submitted strategy was not changed after its completed v3 test.

## Checks completed

- Official docs read from repository commit `00b084a88732d81e595db88b26dde90d44e72d87`; website fetching failed, so the official repository docs were used.
- Official dependency lock retained; JiuwenSwarm metadata verified as exactly `0.2.4b3`. Python and uv installed locally. Make is unavailable, so the exact underlying official commands were used.
- Official setup completed; only the organiser's three environment values were supplied. No hosting-route preferences added. The key was not printed and is ignored by Git.
- User resolved Windows symbolic-link permission through the official loader in administrator PowerShell. No engine/dataset/package workaround or private simulation inspection was used.
- Both Skills were loaded by the agent. Installed Skill hashes matched source after v3 testing.
- Text files are nonempty; manifest mode and team match checked; real YAML parsing checked Skill names/descriptions. English prose manually reviewed. Actual locally saved key excluded from all packaged content.
- Draft archive contains exactly one root `solution/`, six text files, and no credentials, logs, tools, or runtime directories. Extracted files matched source hashes. The required video is absent; no empty placeholder or fabricated recording was created.
- Official final validator fails for missing `presentation.mp4`. Structural validation cannot certify full compliance or agent quality.
- Local service stopped after testing. No upload or receipt verification occurred.

## Next step: the real recording

Record a team member speaking English using `PRESENTATION_OUTLINE.md`, at original speed, for at most ten minutes. A webcam recording is sufficient; slides are optional. Place the playable MP4 at:

`C:\Users\ricky\Documents\GitHub\TechArena-Huawei\solution\presentation.mp4`

After the video is added, inspect its speech, playback and duration; update the README to remove its missing-video notice. Run the official validator again:

```text
uv run --locked python -m career_sim_runner validate --submission solution
uv run --locked python scripts/submission.py package
```

Only after validation succeeds, package a new ZIP with `solution/` at its root, extract it into a new clean folder, and inspect all seven required files, including the real video. Recheck that no key or runtime output is included. The current draft must not be mistaken for that final ZIP.

Upload the valid final ZIP on the registered team's entry at https://techarena-uk.hydro.ac/ and verify the website's receipt/version. The first cutoff, 00:00 GMT on 28 October, has passed. The next cutoff is **00:00 GMT on 31 October 2026**; the final cutoff is **00:00 GMT on 2 November 2026**. Key expiry does not extend submission cutoffs. Official scoring averages three runs and also considers Skill quality and token efficiency; the top ten proceed to expert review.

Sources: [competition rules](https://github.com/RAI-Internal/techarena-career-sim/blob/main/docs/competition-rules.rst), [submission requirements](https://github.com/RAI-Internal/techarena-career-sim/blob/main/docs/submission.rst), [quickstart](https://github.com/RAI-Internal/techarena-career-sim/blob/main/docs/quickstart.rst).
