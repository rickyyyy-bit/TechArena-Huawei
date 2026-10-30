# Adaptive Career Agent — TechArena UK 2026

**Current status — 30 October 2026:** The revised event and quarterly Skills use explicit delivery, relationships, capability, balanced, and stability priorities. The user reports **73.9/100**, up **7.52 points** from Risk-02's 66.38, with final state **L5; Health 9; Dignity 10; Skill 122; Network 54; Output 38; Wealth 42; Energy 0**. No matching run log or metering was provided; the older campaign costs and adherence audits apply only to their frozen versions. See [the current design](solution/design/skills_design.md) and [decision report](solution/design/decision_report.md). The real English MP4 remains missing.

## Historical context

The dated branch, campaign, and evidence statements below describe earlier versions; use the current reports above for the revised Skills and latest reported result.

**Current uncommitted candidate: risk-follow-through-02; paid campaign closed.** Risk-02 completed 48 months at L5 with **66.38/100**. Two fresh unchanged-v3 controls scored 55.25 and 62.83 (mean **59.04**); Risk-01 scored 46.80 with Month 45 trust elimination at L4. Warning handling and once-monthly checkpoint placement remain unreliable, so no upgrade is demonstrated. About **USD 5.48** was used; no more paid games are queued. Main remains tested v3. See [the complete comparison](testing/RISK_CAMPAIGN.md) and [audit correction](testing/AUDIT_CORRECTION.md). All work is uncommitted; the real English MP4 remains missing.

Team: **Jon8652's team**. This repository includes our actual `solution/`, the official participation runner, pinned dependencies, and teammate setup/testing instructions.

**Historical branch status before the 30 October campaign: monthly performance checks, one local test.** `main` keeps the restored v3 submission, whose original run scored **64.52/100** over 48 months at L5. The candidate at `3facd6e` completed 48 months at L4 with **49.33/100**, with unreliable monthly-check adherence. It is not a demonstrated upgrade; main remains on tested v3. See [testing/MONTHLY_CHECKS.md](testing/MONTHLY_CHECKS.md). V4's archived result is in [testing/PHASE3.md](testing/PHASE3.md). The required real English video is still missing, so the scored submission is **not ready**.

The later unchanged-v3 repeat completed at L5 with **56.47/100**, after a service interruption and same-session recovery. V3's two observed scores are 64.52 and 56.47; neither the 60.50 descriptive mean nor two L5 completions establishes reliable expected performance. Full-run metering for the repeat is unavailable. See [the v3 repeat record](testing/V3_REPEATS.md).

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
