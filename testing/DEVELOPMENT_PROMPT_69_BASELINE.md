# Development prompt: improve the 69.03 baseline while preserving its strengths

Act as a careful development and evaluation lead for our TechArena Career Survival Agent. Improve our verified 69.03/100 strategy through controlled, evidence-based changes while preserving its existing advantages.

Do not merely provide generic advice. Inspect the actual files, establish the current version, produce a concrete development plan, and implement the first narrowly scoped improvement if you have repository access. Do not launch paid games without explicit authorization.

## 1. Objective

Improve repeatable career outcomes over the full 48-month simulation, especially sustainable promotion, Wealth, and Network, while preserving:

- Survival and protection against repeated Health depletion.
- Effective organisational-risk responses.
- Strong Skill development.
- Financial resilience.
- Balanced delivery and relationships.
- Flexible quarterly Energy allocation.
- Concise, executable instructions.

A higher single-run maximum is insufficient. Aim for better average and lower-end performance without sacrificing completion reliability.

## 2. Read the rules and inspect the evidence first

Official documentation:

- https://techarena-career-sim.readthedocs.io/en/latest/rules.html
- https://techarena-career-sim.readthedocs.io/en/latest/handbook.html
- https://techarena-career-sim.readthedocs.io/en/latest/failure-and-ending.html
- https://techarena-career-sim.readthedocs.io/en/latest/competition-rules.html

If those pages are inaccessible, inspect the corresponding official source files:
https://raw.githubusercontent.com/RAI-Internal/techarena-career-sim/main/docs/

Inspect applicable repository instructions, then these project files:

- `solution/manifest.json`
- `solution/skills/event-decisions/SKILL.md`
- `solution/skills/quarterly-planning/SKILL.md`
- `solution/design/skills_design.md`
- `solution/design/decision_report.md`
- `testing/RESULTS.md`
- `testing/UPDATE_PLAN_2026_10_31.md`
- `testing/results/survival-delivery-04-completion-summary.json`
- `testing/results/restore-survival-delivery-04-comparison.json`
- `testing/results/risk-02-base69-quarterly-07-preflight.json`
- Relevant earlier failure summaries and adherence audits.

Important provenance records:

- Original backup: `release-check/solution-backup-20261031-215741/solution/`
- Later restoration verification: `release-check/restore-original-backup-20261101-003855/restore-verification.json`
- Original 69.03 run log: `.career_sim_runner/career_emu/emulator_logs/55aa1b418f5f482a945ed4f508d98868.log`

The last verified state was that the current solution had been restored to the original 69.03 backup on 1 November. An older document incorrectly remained labelled as though revision 07 were active. Verify the current files and hashes yourself; do not assume either description is still current.

Use only permitted public documentation and our own official run outputs. Do not inspect hidden engine state, internal evaluation data, or simulation databases.

If necessary evidence is unavailable, identify the gap and continue with supported conclusions. Never imply that you inspected a log or tested a change when you did not.

## 3. Starting evidence

The verified survival-delivery-04 run:

- Run: `20261031T212328Z`
- Score: 69.03/100.
- Outcome: completed all 48 months.
- Ending level: L5.
- Wealth: 39.1.
- Health and Dignity: 10 each.
- Skill: 110.
- Network: 33.

Returned ending contributions:

| Component | Earned | Maximum component contribution |
|---|---:|---:|
| Level | 15.00 | 30 |
| Wealth | 9.78 | 20 |
| Health/Dignity | 15.00 | 15 |
| Skill | 13.75 | 15 |
| Risk control | 10.00 | 10 |
| Network | 5.50 | 10 |

These contributions describe this ending. They do not establish action returns, hidden promotion thresholds, or a permitted strategy formula.

Its quarterly Energy actions were:

- 14 report preparations.
- 13 Network maintenance actions.
- 17 Health recoveries.
- 2 risk defusals.
- Total Energy spent: 48.

Seven recoveries occurred at Health 10 with no visible Health gain: months 12, 15, 18, 30, 39, 42, and 48. Their rationale included “maintaining buffer.” These consumed 14.6% of the total Energy budget without the claimed visible benefit.

Main actions:

- 13 key projects.
- 1 report to the manager.
- 2 protective “lay low” actions.

Promotion/review evidence:

- Reached L4 around month 24.
- Remained L4 at the month-30, month-36, and month-42 windows.
- Those reviews were B, A, and A.
- Reached L5 at the final window.
- Some notes treated A reviews as proof that the strategy was working.
- Some projects developed Skill without the anticipated Output/Network improvements.

Other problems visible in the successful run:

- Some notes acknowledged an active HR warning and then said “no concerns.”
- Some asserted organisational-risk reduction without sufficient evidence.
- The final main-action rationale treated Output as a direct ending-score target.
- Some notes prematurely called the game complete before an ending was returned.

The later revision-05 run completed with 51.27/100. Its contributions were:

- Level: 12.
- Wealth: 7.03.
- Health/Dignity: 14.25.
- Skill: 11.
- Risk control: 1.
- Network: 6.

Do not mislabel that result as an elimination or attribute it to revision 06. The largest component deterioration was risk control. Different trajectories mean this comparison does not prove which policy change caused the decline.

Earlier history also includes Health failures, trust-related failures, capability dismissals, financial failure, and unsuccessful attempts to improve behaviour by adding longer checkpoints. Use these as regression concerns, not as justification for fixed event answers.

## 4. Preserve these advantages explicitly

Before proposing edits, create a preservation checklist.

1. **Health sustainability**
   Preserve checks on recent depletion, existing commitments, and the decisions before recovery is actually available. Never justify optional strain by assuming the agent will survive until a later recovery phase.

2. **Risk follow-through**
   Preserve comparison of protection against growth in both the Energy and main-action phases. Mitigation is an attempt, not proof that a warning has cleared.

3. **Capability development**
   Preserve useful Skill gains from projects and story choices. A large raw Skill number does not prove readiness for the current or next level.

4. **Financial resilience**
   Preserve affordability checks and responses to deteriorating Wealth. Do not assume future salary, promotion, or bonuses will rescue imminent distress.

5. **Balanced development**
   Preserve constructive delivery, visibility, relationships, and professional standing. Do not broadly remove Dignity protection because it finished high in one run.

6. **Sequential allocation**
   Preserve the three-point quarterly budget, affordability checks, and reassessment after each action. Unused Energy does not carry over.

7. **Simple execution**
   Keep the existing two-Skill structure unless evidence demonstrates a need to change it. Prefer ordinary decision notes over extra planning calls or external memory.

Preserve decision principles, not exact action counts or a memorised trajectory.

## 5. Prioritised improvements

### Priority 1: Stop ineffective recovery at the published cap

Before Health recovery, check whether its intended benefit is available.

At Health 10:

- Do not claim ordinary recovery adds a visible buffer.
- Compare another useful, affordable, legal action.
- Do not automatically redirect the point to Output.
- Preserve an action with a separately supported protective purpose.
- If no worthwhile option exists, explain unused Energy rather than force ineffective spending.

Below the cap:

- Keep recovery available when recent depletion or upcoming demands justify it.
- Do not create a fixed “safe Health” threshold or universal recovery quota.

### Priority 2: Make quarterly allocation adaptive in practice

Prevent the provisional “report + network + recovery” plan from becoming mandatory.

- Compare useful allocations before the first purchase.
- Keep an urgent two-point action affordable.
- Reassess after each returned result.
- Compare repeated one-point actions only when still legal and useful.
- Stop repeating an action for a gain that repeatedly fails to appear unless changed evidence or another supported purpose justifies it.
- Distinguish unavailable evidence from an observed absent benefit.
- Do not treat absent visible gains as proof that supported risk mitigation is worthless.

### Priority 3: Reassess after missed promotion windows

Separate:

- Review grade.
- Actual promotion outcome.
- Evidence of development.
- Remaining opportunities.

After a missed window, compare completed work, visibility, collaboration, capability, and current responsibilities. Change emphasis when supported.

Do not assume A or S guarantees promotion. Do not invent exact readiness targets, hidden thresholds, or promised promotion dates. Do not compensate for uncertainty by forcing unsafe workload.

### Priority 4: Evaluate the actual value of projects and alternatives

For each relevant main action:

- Identify the intended benefit.
- Check what actually changed.
- Retain useful Skill development even when Output/Network did not improve.
- Compare offered alternatives against the current need.
- Reassess ineffective repetition.

Do not automatically replace projects with reporting. Reporting does not create completed work, and a visibility problem is only one possible explanation for weak performance.

### Priority 5: Maintain warning continuity across phases

Use a compact concern summary in ordinary notes:

- Latest relevant evidence.
- Response taken.
- Observed result or unknown.
- Current tradeoff.
- Feedback that would change the assessment.

An active serious warning must not disappear because a new month begins, Health is high, or a previous mitigation was attempted.

Compare avoidable exposure in monthly story choices as well as quarterly protection. Do not claim a choice reduces organisational risk merely because it sounds responsible.

Allow reassessment when relevant evidence improves; avoid indefinite mitigation without review.

### Priority 6: Correct remaining-horizon reasoning

Check which reviews and promotion opportunities have actually settled.

When none remain:

- Do not pursue Output solely for another review.
- Do not call Output a separate ending component.
- Compare benefits that can still affect the ending.
- Preserve useful project Skill/Network gains where relevant.
- Continue protection against remaining threats.
- Stop only when an ending is returned.

Apply this to story choices, Energy, and main actions.

### Priority 7: Improve sustained Network and Wealth

For Network:

- Examine both acquisition and avoidable losses.
- Reassess relationships after promotion or organisational changes.
- Compare constructive collaboration and repair with other needs.
- Do not accept every social demand regardless of Health cost.

For Wealth:

- Address financial strain promptly.
- Compare discretionary costs with concrete benefits.
- Pursue earlier sustainable promotion without assuming it will occur.
- Avoid harmful blanket cost avoidance.

Do not optimise either dimension at the expense of risk control or capability.

### Priority 8: Keep capability assessment proactive

Check responsibilities, task feedback, and actual Skill development after promotion or increasing task difficulty.

- Count capability gained through stories and projects.
- Compare learning when supported.
- Do not wait for dismissal warnings.
- Do not buy learning automatically after every promotion.
- Do not use fixed Skill caps or raw-stat comparisons to declare sufficiency.

### Priority 9: Improve diagnosis and monthly priorities

Replace generic slogans with concise, evidence-based choice criteria.

A weak review may reflect delivery, visibility, collaboration, capability, or several factors. Preserve uncertainty where feedback is broad.

Use one brief checkpoint in the first ordinary monthly note. It should influence subsequent choices, carry into quarterly planning, and change when results contradict expectations.

### Priority 10: Improve efficiency and evidence quality

After behavioural improvements are validated:

- Remove duplicated instructions and repeated unchanged histories.
- Avoid observation/log calls whose only purpose is restating a checkpoint.
- Preserve decisive evidence and important exceptions.
- Measure tokens per survived month, not just cost or elapsed time.
- Test compression separately from strategic changes.

For every run, record version identity, source and installed hashes, loaded Skills, model/configuration, outcome, score, survived months, grades, promotions, component contributions, and complete usage where available.

Keep historical claims attached to their actual versions.

## 6. Development sequence

Do not implement all improvements at once.

### Stage 0 — Baseline and evidence

- Verify the active source against the original backup.
- Preserve the backup and original outputs unchanged.
- Identify uncommitted user changes.
- Reconcile stale version descriptions.
- Separate verified findings, hypotheses, and missing evidence.
- Establish a baseline metrics table.

### Stage 1 — First narrow candidate

Implement only:

- Explicit capped-Health recovery handling.
- Reconsideration of the remaining Energy plan after each action.

Keep the monthly event Skill, default development priorities, warning controls, and broader main-action strategy unchanged unless a minimal consistency edit is necessary.

Review the existing revision-07 material for reusable wording, but do not restore the entire revision automatically.

Run appropriate local checks. Prepare the candidate for evaluation, but do not launch paid games.

### Stage 2 — Promotion, project, and horizon candidate

After Stage 1 is evaluated, separately introduce:

- Missed-window reassessment.
- Actual project-benefit comparison.
- Correct final-phase reasoning.

Preserve the successful protection and capability criteria.

### Stage 3 — Warning-execution candidate

Tighten warning continuity and unsupported safety claims in monthly decisions. Keep the comparison between competing survival threats explicit.

### Stage 4 — Targeted growth experiment

Only change Network, Wealth, capability, or project emphasis when repeated evidence identifies a specific bottleneck. Change one coherent policy dimension at a time.

### Stage 5 — Efficiency and release

Compress duplication, verify behaviour remains intact, align the design documents, and validate the submission package and required presentation.

## 7. Validation plan

First perform manual policy checks for:

- Health at 10 with a useful alternative.
- Health at 10 with no worthwhile alternative.
- Health below 10 after recurrent depletion.
- A serious warning persisting after defusal.
- A competing urgent Health and organisational threat.
- An action with no observed intended gain.
- Risk mitigation without a visible-stat gain.
- A project producing Skill but no intended Output/Network.
- A strong review without promotion.
- Broad weak-review feedback without a clear diagnosis.
- Financial distress.
- Useful capability development without an explicit warning.
- Final decisions after the last review has settled.
- A returned terminal outcome.

These checks are not gameplay evidence. Existing software tests do not prove instruction adherence.

When paid evaluation is explicitly authorized:

1. Freeze and verify the candidate.
2. Run one pilot.
3. Audit consequential decisions semantically.
4. Revise or reject candidates with critical execution failures.
5. For promising candidates, compare at least three unchanged candidate runs with three comparable unchanged baseline runs.
6. Reuse historical baselines only when provenance and configuration match.
7. Count every scored elimination.
8. Separate technical interruptions and label recoveries.
9. Do not change policy midway through a run.

Track:

- Completion rate.
- Mean and minimum score.
- Ending component contributions.
- Promotion timing.
- Review trajectory.
- Failure categories.
- Ineffective Energy spending.
- Warning-response failures.
- Capability and financial deterioration.
- Tokens per survived month.

Predeclare an adoption rule before testing. A reasonable initial target is at least +5 mean score points, no worse observed completion rate or minimum score, and meaningful adherence to survival controls. Explain that a small batch provides provisional evidence, not proof of reliability.

If results are inconclusive, preserve the baseline and report uncertainty.

## 8. Explicitly avoid

- A broad rewrite motivated by one high or low score.
- Assigning a historical score to an untested revision.
- Treating passing packaging tests as evidence of better gameplay.
- Inferring causation from different run trajectories.
- Fixed answers for named events or memorised event sequences.
- Hidden formulas, invented caps, failure counters, or promotion thresholds.
- Converting ending contributions into a supposedly exact action-value formula.
- Ranking unrelated raw statistics as though their units are comparable.
- Treating an A/S review as proof of promotion readiness.
- Treating strong visible statistics as proof of organisational safety.
- Treating attempted mitigation as clearance.
- Blanket suppression of Skill, Dignity, recovery, or protection.
- Fixed quarterly recipes or compulsory mitigation quotas.
- Repeating ineffective actions merely to spend all Energy.
- Promising future recovery, bonuses, or promotions.
- Extra Skills, agents, memory systems, or planning calls without a demonstrated need and rule compliance.
- Altering the official runner or environment to improve measured outcomes.
- Editing original logs, scores, backups, or historical evidence.
- Launching paid games without explicit authorization.
- Claiming that the resulting candidate is improved before evaluation.

## 9. Required response and deliverables

Provide:

1. **Verified current state:** what version is active and what evidence supports it.
2. **Evidence assessment:** confirmed problems, plausible hypotheses, and unresolved questions.
3. **Preservation checklist:** old advantages and how each proposed edit protects them.
4. **Prioritised improvement table:** evidence, proposed change, expected benefit, regression risk, and success criterion.
5. **Detailed staged development plan:** exact files affected and the boundary between candidates.
6. **First candidate implementation, if repository access is available:** only the Stage 1 scope, preserving unrelated work.
7. **Validation report:** checks actually performed, results, exclusions, and limitations.
8. **Evaluation-ready handoff:** frozen version identity, metrics, audit criteria, and the proposed run protocol.

Do not ask me to reconfirm reversible repository inspection or the explicitly authorized Stage 1 edits. Ask only for genuinely missing information or authorization required for paid evaluation.

If repository access is unavailable, provide the same evidence-based plan and clearly labelled proposed edits without pretending implementation occurred.

Focus on the central objective: reclaim wasted opportunities and improve sustained career growth while preserving the survival, risk control, and capability strengths of the 69.03 baseline.
