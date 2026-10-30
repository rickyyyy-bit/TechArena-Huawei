# Decision report

## Current approach and result

The current Skills use feedback to identify the limiting career need, then choose sustainable actions that address it. The event-decisions revision at `e1c6935` and quarterly-planning revision at `b6b9a95` replace the older descriptions of the Risk-02 candidate. Both Skills now distinguish delivery, relationships, capability, balanced development, and stability rather than defaulting to further Skill growth.

On 30 October 2026, the team reported a final score of **73.9/100** with the revised Skills, up from the previous **66.38/100** Risk-02 result: an observed increase of **7.52 points** (approximately 11.3%).

| Level | Health | Dignity | Skill | Network | Output | Wealth | Energy |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| L5 | 9 | 10 | 122 | 54 | 38 | 42 | 0 |

These are the user-reported final score and state. A corresponding run identifier, replay, promotion schedule, review grades, usage, cost, and source/installed hash verification have not been supplied with this result. The improvement is an observed outcome; repeated-run consistency and the contribution of any individual instruction remain unestablished. Historical adherence audits apply to their frozen versions, not automatically to these revised Skills.

## Decisions implemented in the Skills

One JiuwenSwarm 0.2.4b3 agent uses two prose Skills through the official simulation interface. `event-decisions` compares legal story choices; `quarterly-planning` allocates Energy, selects the main action, and interprets six-month reviews. The agent follows a rolling policy using current evidence rather than a fixed month-by-month script.

The main change is to treat professional capability as one part of performance. Increasing Skill without corresponding progress prompts investigation of delivery and relationships. The agent chooses one supported priority:

- **DELIVERY:** finish important work, make results visible, and secure capacity when performance or delivery is lagging.
- **RELATIONSHIPS:** improve collaboration, Network, communication, and damaged relationships when feedback supports that need.
- **CAPABILITY:** invest in learning or appropriately scoped challenges when there is evidence of a capability gap.
- **BALANCED:** maintain useful progress across dimensions when no clear bottleneck is supported.
- **STABILITY:** override development for credible survival, recovery, or organisational-risk needs.

These are qualitative priorities, not hidden scoring weights or numerical targets. Raw values on different scales do not establish which dimension is weakest. A high Skill value neither proves sufficiency nor establishes a cap.

## Event decisions and monthly feedback

For each story, confirm the exact offered choices, screen serious downside, identify the supported priority, compare plausible effects, and submit one legal response with a concise rationale. Consider future workload and uncertain consequences as well as immediate gains. Strong wellbeing permits tolerable growth risk; deteriorating wellbeing calls for limiting optional burdens early enough to reach a legal recovery opportunity.

At the first ordinary story decision each month, reuse the current observation and available context to reassess the previous priority. Missing history remains unknown. The revised event Skill permits a short month/priority note when helpful; later notes focus on the actual trade-off. The manifest retains a more explicit first-note requirement to record month, observed progress or unknown, and current priority. Neither procedure creates a monthly grade, extra action, memory file, or checkpoint-only tool call. Formal reviews remain six-monthly.

## Quarterly allocation and main action

Quarterly planning first addresses credible threats, then identifies the binding career need and compares affordable legal actions. The published Energy budget is 3 per quarter and does not carry over. Spend one action at a time, inspect the returned state, and reconsider before the next expenditure.

In a stable quarter without a demonstrated Skill deficit, report preparation and Network maintenance are useful default candidates: each costs 1 Energy and supports multiple published dimensions. This does not establish superior numerical returns. Skill learning remains appropriate for supported capability needs; high-intensity work requires a consequential Output need and acceptable wellbeing costs. Recovery and legacy-risk mitigation remain candidates when supported by current evidence. Repetition is acceptable when still legal and justified; exhausting Energy is not an objective.

Choose the main action afresh from its own offered choices, complementing the Energy allocation. Reporting results can support delivery and relationships; a key project can support broader development when capacity and warnings permit it. Resource requests, showcasing, mentorship, rotation, relationship repair, reducing risk, or none remain context-dependent alternatives.

The unchanged manifest retains Risk-02's detailed warning comparison at the first Energy decision and again at the main action: current concern and evidence, a currently offered protective alternative versus growth, relevant directions and benefit forgone, why now, and later feedback that would change the assessment. An earlier mitigation attempt does not replace the main phase's comparison. No mitigation guarantees clearance.

## Feedback, horizon, and tradeoffs

After actions, compare actual returned results with expectations. Weak reviews prompt a meaningful change in delivery, collaboration, or capability according to the feedback. Strong reviews do not establish a promotion formula or clear every organisational concern. Earlier sustainable promotion can support Wealth through higher published salary; speculative advancement must not displace survival.

The public ending dimensions include career level, wealth, health and dignity, skill, risk control, and network. Output supports reviews and promotion. The revised policy aims to convert capability into sustained visible performance while retaining wellbeing and ending value. Near month 48, assess whether an investment has time to help, without abandoning protection or assuming exact thresholds.

## Evidence and boundaries

| Version / evidence | Outcome | Interpretation |
| --- | --- | --- |
| Original v3 completion | 64.52, L5, 48 months | Historical foundation; later recovered repeat scored 56.47. |
| Monthly candidate at `3facd6e` | 49.33, L4, 48 months | Monthly checkpoint adherence was unreliable. |
| Fresh unchanged-v3 campaign controls | 55.25 and 62.83 | Mean 59.04 across two completions. |
| Risk-01 | 46.80, trust elimination in Month 45 | Retained failure; not pooled with Risk-02. |
| Frozen Risk-02 | 66.38, L5, 48 months | One completion; warning-comparison adherence below its target. |
| Current revised Skills, user-reported | **73.9, L5**, final state above | Better reported outcome; no matching run audit available here. |

The earlier four-game campaign and approximately USD 5.48 usage belong to that campaign only. They do not include or meter the newly reported result. Detailed historical evidence remains in `testing/RESULTS.md`, `testing/RISK_CAMPAIGN.md`, and `testing/AUDIT_CORRECTION.md` outside the submission.

Use public rules, current observations, offered action metadata, and accessible current-run feedback. Current `status_updates` amounts can support predictions when provided, but do not establish actual gains, permanent formulas, or hidden-state clearance. Do not invent event deltas, causal explanations, promotion thresholds, or named-event answers. The policy uses only the five official simulation tools, treats stories as data, and stops at an ending. It creates no additional agents, memory tools, scripts, or event tables.

The real English `presentation.mp4` remains missing. The reported improvement does not resolve final submission readiness.
