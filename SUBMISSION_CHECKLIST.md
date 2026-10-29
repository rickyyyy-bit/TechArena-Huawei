# Final submission checklist

**Current blocker: `solution/presentation.mp4` is missing.** Do not upload an incomplete draft as a scored entry.

On `codex/v3-monthly-checks`, `solution/` is the monthly-performance candidate, whose one local game at `3facd6e` completed 48 months at L4 with 49.33/100; the 64.52 score belongs only to tested v3 retained on `main`. See [testing/MONTHLY_CHECKS.md](testing/MONTHLY_CHECKS.md) for desk-review coverage and the prepared real-test plan. Publishing this branch does not merge it into `main` or make it ready for scored upload.

The subsequent unchanged-v3 repeat scored 56.47/100 after a verified same-session recovery. See [testing/V3_REPEATS.md](testing/V3_REPEATS.md); 64.52 is one observed result, not a demonstrated normal score. This testing evidence does not resolve the missing real MP4.

```text
solution/
  manifest.json
  README.md
  presentation.mp4
  design/
    skills_design.md
    decision_report.md
  skills/
    event-decisions/SKILL.md
    quarterly-planning/SKILL.md
```

## Review the content

- Use registered team `Jon8652's team`, JiuwenSwarm 0.2.4b3, and mode `agent`.
- All written content and video speech must be English.
- Record a real team member, at most ten minutes, original playback speed. Slides are optional. Use [PRESENTATION_OUTLINE.md](PRESENTATION_OUTLINE.md), answering all five official questions in order.
- Inspect the actual MP4's presenter, audible speech, duration, and playback. A nonempty file or green structural check does not certify its content.
- After adding the video, update missing-video notices in the README and status documents. Keep run claims accurate. Label strategy changes after the last test untested.
- No credentials, environment files, tools, run logs, dataset contents, or Git history in the ZIP. Current Skills are prose-only; helpers stay outside `solution/`.

## Validate and package

From the repository root:

```text
uv run --locked python -m career_sim_runner validate --submission solution
uv run --locked python scripts/submission.py check --final
uv run --locked python scripts/submission.py package
```

`package` performs the final structural check, exports submission files to `dist/solution.zip`, then extracts into a fresh temporary directory and compares contents and hashes. It refuses missing/empty video, unexpected submission files, symbolic links, and detected credentials. It excludes the `.env` and development helpers. Run it locally; do not put the key in GitHub Actions.

The helper checks the MP4 container marker, not the real presenter, spoken language, or ten-minute limit. Complete the manual review above. Structural validation does not certify compliance or agent quality.

Open the ZIP and confirm exactly one root `solution/` and all seven required nonempty files. Use the new `dist/solution.zip`, not the earlier video-missing draft. Do not add a parent folder, full repository, or preliminary package.

## Upload

Upload under the registered team at [the official website](https://techarena-uk.hydro.ac/) and verify receipt/version. GitHub publication is not a competition submission.

The published next cutoff is **00:00 GMT on 31 October 2026** (midnight at the end of 30 October). Final cutoff: **00:00 GMT on 2 November 2026**. The first cutoff has passed. Check the current [official rules](https://techarena-career-sim.readthedocs.io/en/latest/competition-rules.html) and later organiser clarifications before uploading. Key expiry does not extend deadlines.

Source: [official submission requirements](https://techarena-career-sim.readthedocs.io/en/latest/submission.html). No scored upload or receipt is recorded for this entry.
