# Adaptive Career Agent — TechArena UK 2026

Team: **Jon8652's team**. This repository includes our actual `solution/`, the official participation runner, pinned dependencies, and teammate setup/testing instructions.

**Branch status: v3 plus monthly performance checks, untested candidate.** `main` keeps the restored v3 submission, which scored **64.52/100** over 48 months at L5. This branch adds only a monthly feedback routine; it has no model score and is not a demonstrated upgrade. See [testing/MONTHLY_CHECKS.md](testing/MONTHLY_CHECKS.md). V4's archived result is in [testing/PHASE3.md](testing/PHASE3.md). The required real English video is still missing, so the scored submission is **not ready**.

## Start here

1. Read [TEAM_GUIDE.md](TEAM_GUIDE.md) for installation, credentials, Windows setup, local play, scores, and replays.
2. Run the key-free check: `uv run --locked python scripts/submission.py check`.
3. Read [testing/RESULTS.md](testing/RESULTS.md) for real results and known weaknesses.
4. Record the team video using [PRESENTATION_OUTLINE.md](PRESENTATION_OUTLINE.md), then follow [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md).

## Included files

| Path | Purpose |
| --- | --- |
| `solution/` | Actual submission: manifest, README, two design reports, and two prose Skills |
| `preliminary/` | Previously verified, unscored preliminary design |
| `career_sim_runner/`, `Makefile`, `pyproject.toml`, `uv.lock` | Official runner and pinned environment |
| `docs/` | Official documentation snapshot from upstream commit `00b084a88732d81e595db88b26dde90d44e72d87` |
| `scripts/submission.py` | Development-only check and final ZIP packaging; never included in the submission |
| `testing/` | Sanitised evidence and teammate test procedure |
| `.github/workflows/checks.yml` | Key-free checks with no model calls or competition credentials |

One JiuwenSwarm **0.2.4b3** agent uses `event-decisions` for story choices and `quarterly-planning` for Energy/main actions. Both manifests use mode `agent`. The MCP server is the official `career-emulator-engine[mcp]` server; we did not build or modify it.

## Credentials

Obtain the organiser key privately within the registered team. Each teammate creates their own ignored `.env` from `.env.example`; only `API_BASE`, `API_KEY`, and `MODEL_NAME` are allowed. Use `deepseek-v4-flash` exactly. No hosting-route preferences or substitute model. Never put the key in GitHub, issues, screenshots, ZIPs, or shared logs.

Local environments, raw runs, datasets, service state, release checks, and ZIPs stay out of Git. Public evidence is a curated summary; original logs remain on the originating machine. Development helper scripts stay outside `solution/`.

## Authoritative references

Read the current [competition rules](https://techarena-career-sim.readthedocs.io/en/latest/competition-rules.html), [submission requirements](https://techarena-career-sim.readthedocs.io/en/latest/submission.html), [API-key guidance](https://techarena-career-sim.readthedocs.io/en/latest/api-key.html), and [official repository](https://github.com/RAI-Internal/techarena-career-sim). Later written organiser clarification takes precedence over this guide. The documentation snapshot is retained in `docs/` for reference.
