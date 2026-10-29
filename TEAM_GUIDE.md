# Teammate setup and testing

Run commands from the repository root. Install [Git](https://git-scm.com/downloads) and [uv](https://docs.astral.sh/uv/getting-started/installation/) first. Python 3.12 is the tested development version; uv can install it. The maintainer's ignored `.tools/` and `.venv/` are not part of a fresh clone and are not needed.

Use `main` for the restored v3 solution: its original run scored 64.52/100 over 48 months; the later recovered repeat scored 56.47/100. After updating an existing clone, confirm `git branch --show-current` reports `main`. The separate `codex/phase3-skills` branch retains the v4 experiment, which scored 42.12 and failed in Month 39. Read [testing/PHASE3.md](testing/PHASE3.md) for that archived test. Coordinate version and shared credit before another paid run.

The separate `codex/v3-monthly-checks` candidate completes the monthly self-check routine first published at `29515b1`. Read [testing/MONTHLY_CHECKS.md](testing/MONTHLY_CHECKS.md) for the eight-case desk review and real-test record fields. Its one user-requested game at `3facd6e` completed 48 months at L4 with **49.33/100**, with unreliable checkpoint adherence. This did not demonstrate an upgrade. Formal game reviews stay six-monthly. The first ordinary story-action note each month should give month, observed prior progress or unknown, and one current priority. Audit whether offered story choices and quarterly Energy/main-action comparisons actually use it, explain survival/warning overrides, and reconsider contrary results. No checkpoint-only observation/log calls, repeated plan recital or extra workload are required. Stop at the ending.

The repeated uninterrupted batches are still pending: the user authorised one monthly-candidate game and one unchanged-v3 repeat. The v3 repeat completed after a service recovery; no additional games were started. Do not start further paid games until explicitly requested. Then repeat unchanged v3 runs first to estimate baseline variability, followed by repeated frozen-candidate runs, coordinating shared credit. Record full source commit and manifest/Skill SHA-256 hashes before each run, actual monthly adherence, completion and failure category, six-month grades, promotion months, quantitative score, tokens per survival month and reported cost. Keep unknown results unknown and retain original outputs unchanged. One run cannot establish causation or consistent improvement. New risk systems, operating bands, Network targets and token redesign remain separate experiments; no workspace-memory files/tools or embeddings are introduced.

The unchanged-v3 repeat scored **56.47/100**, completed 48 months at L5 and recovered the same game after a Month 30 service outage. Its full-run usage is unavailable. Read [testing/V3_REPEATS.md](testing/V3_REPEATS.md) before interpreting the original 64.52 or planning more tests; two results, one recovered, do not establish the normal score range.

## 1. Clone and install

```text
git clone https://github.com/rickyyyy-bit/TechArena-Huawei.git
cd TechArena-Huawei
uv sync --locked --python 3.12
uv run --locked python scripts/submission.py check
```

Do not copy the example submission over `solution/`: our actual solution is already included. Keep `pyproject.toml` and `uv.lock` unchanged. JiuwenSwarm must be exactly **0.2.4b3**, in `agent` mode.

The development check needs no key, running service, or dataset. Missing video is a final-submission blocker, not a gameplay blocker. The check reads the public submission structure and package metadata only; it does not inspect simulator contents or play a game.

## 2. Save credentials locally and run setup

In PowerShell, copy the template only if you do not already have `.env`:

```powershell
if (-not (Test-Path .env)) { Copy-Item .env.example .env }
notepad .env
```

On macOS/Linux: `test -f .env || cp .env.example .env`, then edit `.env`.

Keep exactly these three assignments, entering the key supplied privately by the organisers:

```dotenv
API_BASE="https://openrouter.ai/api/v1"
API_KEY=""
MODEL_NAME="deepseek-v4-flash"
```

Never paste the key in chat or commit it. No provider, order, only, allow_fallbacks, or other hosting-route preference. No substitute model. The competition key is for registered-team use only, with a USD 50 limit and the organiser's authorised period. Coordinate paid tests to avoid overlapping shared-credit use. Reported costs are not the account balance.

Check the values without printing them, then run official setup:

```text
uv run --locked python scripts/submission.py check --credentials
uv run --locked python -m career_sim_runner setup
```

Use a normal interactive terminal and select **English** if initialization asks. Setup creates the named instance `career_emu` and copies the three values into its local configuration outside this repository. Do not share complete configuration files or screenshots containing secrets.

## 3. Load data through the official command

```text
uv run --locked career-emulator-engine update --source distribution --split dev
```

**Windows error 1314:** the loader needs permission to create a directory symbolic link. Open a new PowerShell using **Run as administrator**, change to your own clone folder, and run the same command. If uv is not on that terminal's PATH, use the installed executable from your clone root:

```powershell
.\.venv\Scripts\career-emulator-engine.exe update --source distribution --split dev
```

Do not copy or inspect the packaged dataset, create a substitute dataset, patch the engine, or access the database. Return to a normal terminal for subsequent steps.

## 4. Start and play

Terminal A, kept open:

```text
uv run --locked jiuwenswarm-start --name career_emu all
```

Terminal B, also at the repository root:

```text
uv run --locked jiuwenswarm-start --name career_emu --list
uv run --locked python -m career_sim_runner play --submission solution
```

Use the web-interface port reported by `--list`. On the maintainer's setup it is [http://localhost:6173](http://localhost:6173). `localhost` is your own computer, not a shared online server. The presentation video is not required for play. These are the commands behind the official Makefile targets; make is optional.

This test uses the key and can take tens of minutes. Keep the computer awake and connected. The evaluated agent uses only `new_game`, `observe`, `take_action`, `check_latest_logs`, and `show_employee_handbook` to interact with the simulation. Stop your service with Ctrl+C in Terminal A when finished.

## 5. Read results and retain evidence

```text
uv run --locked python -m career_sim_runner score
uv run --locked python -m career_sim_runner replay
```

Use `quantitative_score`, not `competition_partial_score`. Check `completed`, `survival_months`, exit code, and failure reason. A successful process exit can still mean elimination. An interrupted game with an empty ending score is not a completed career.

Your original outputs are in `.career_sim_runner/career_emu/outputs/<team>/<timestamp>/`: transcript, event log, score report, and replay. Read these outputs only; do not open the simulation database or package/dataset internals. Preserve original outputs without hand editing. Review/redact logs before sharing privately. Do not publish full event sequences or turn them into future answer tables.

**Known continuation issue:** the provided `--continue` path supplied `session_id=unknown` in our interrupted attempt and started a replacement game. Do not treat that as a resumed result. The current manifest requests recovery failure for an unknown ID. We did not patch the runner. Prefer a fresh labelled test after resolving connectivity; retain the interrupted attempt as incomplete.

Follow [testing/RESULTS.md](testing/RESULTS.md) to record tests. Note the strategy commit and uncommitted changes. Change one major behaviour at a time and compare multiple runs, completion rate, average/worst score, and tokens per month. One better result with different events does not establish causation. Do not infer hidden thresholds or memorise event answers.

## 6. Key-free checks and submission

```text
uv run --locked python scripts/submission.py check
uv run --locked pytest
```

These checks make no model calls and need no competition secrets. GitHub Actions runs them too. Green development checks do not mean the scored ZIP is complete or compliant. For video, final validation, packaging, and upload, follow [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md). The scripts and workflow never go in the submission ZIP.
