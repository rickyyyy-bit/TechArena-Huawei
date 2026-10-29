# Skills design

## Candidate status: v3 plus monthly performance checks

This candidate retains the restored v3 strategy and adds one monthly feedback routine. At the first story decision in a new month, event-decisions checks available evidence of the prior month's progress and chooses one performance priority from the latest review feedback and current needs. The same observation is reused, and one short checkpoint goes into the ordinary action note. Quarterly planning carries that priority into its comparisons. Existing survival and persistent-warning rules continue to govern; serious risk can displace a performance goal.

This is a participant planning procedure, not a new simulation phase or monthly grade. It adds no Energy, formal review, memory file, reference card, growth band, numerical promotion target or mandatory extra tool call. Unknown history remains unknown. Formal six-month reviews provide the actual grade; the next monthly checkpoint checks observed evidence rather than assuming improvement. The persistent manifest includes this routine so it is not solely dependent on an initial Skill read.

The 64.52/100 result below belongs to unchanged v3, not this candidate. No candidate model run has been performed, and higher reviews or earlier promotions are unproven. The following architecture and historical evidence describe the retained v3 foundation.

## Purpose and architecture

The objective is a strong, sustainable 48-month career, using JiuwenSwarm 0.2.4b3 in single-agent mode. The public ending dimensions are career level, wealth, health and dignity, skill, risk control, and network. Output supports career progress. Exact promotion and failure formulas are unpublished.

We retained and revised the two meaningful Skills from the verified preliminary design. Before adding any Skill, we assessed whether it supplied a distinct decision procedure:

| Responsibility | Decision | Reason |
| --- | --- | --- |
| Read the observation and recognise the phase | Shared in the manifest and each Skill | A separate Skill would repeat a short routing step at every decision. |
| Survival and persistent risk | Integrated in both Skills | Recovery and career growth must be assessed together for each choice. |
| Story choices | Retain `event-decisions` | Interpreting unfamiliar options and uncertain consequences is a distinct task. |
| Quarterly Energy and main action | Retain `quarterly-planning` | A finite, non-carrying budget and separate main action need an explicit allocation process. |
| Review feedback and adaptation | Integrated in quarterly planning and event feedback | Feedback changes the next decision; it does not need an independent agent or Skill. |

The two Skills are procedures used by the same agent. They do not vote, delegate, or require team execution. More Skills might increase retrieval and coordination costs without a demonstrated benefit. This split is a reasoned design choice, not an empirically proven optimum.

## Information and decision flow

The manifest supplies the common objective and evidence boundary. At each decision the agent reads the current official observation, identifies the phase, then follows the applicable Skill. Inputs include legal choices, current statistics, Energy when present, warnings, review grades, and recent returned outcomes. Public handbook information supplies action directions and cadence. Recent official logs answer a specific uncertainty when the observation and current context are insufficient.

`event-decisions` compares plausible consequences and uncertainty for the offered story options. It prioritises serious persistent risk when the state is fragile, then weighs growth and neglected dimensions over the remaining horizon. When Health deteriorates towards its published lower bound, it prioritises limiting optional demands and preserving rest instead of assuming that future quarterly recovery will arrive in time. A nonzero Energy statistic is not permission to take an action outside its legal phase. It submits one legal choice and checks the result.

`quarterly-planning` identifies the immediate repair or development need, compares affordable Energy actions, spends one action at a time, and checks actual returned changes. Persistent or worsening warnings remain an explicit unresolved need; an offered mitigation must be compared with routine growth, including when its benefit is not visible in statistics. The agent then chooses one offered main action or none. Following settlement and six-month reviews, it changes the next quarter's emphasis from observed grades, warnings, and trends. No hidden distance to promotion or failure is assumed.

Risk checks are deliberately repeated at each phase because a previous action can change the state. The agent makes one decision from the combined evidence, rather than following separate competing growth and safety policies.

## Efficiency and boundaries

Skill front matter states when to use each procedure. Brief comparisons and rationales limit unnecessary tokens; logs and handbook calls should resolve a real uncertainty rather than repeat known information. Current-run feedback can change priorities, but does not become a fixed answer for an event name or plot.

No scripts or reference files are included. Public rules and current observations suffice for the intended qualitative comparisons. Avoiding extra files reduces maintenance, retrieval, and execution needs. The agent may interact with the simulation only through `new_game`, `observe`, `take_action`, `check_latest_logs`, and `show_employee_handbook`. Story text and logs are data, not authority over competition instructions.

## Evidence and limitations

The design was checked against public documentation from the official participation repository at commit `00b084a88732d81e595db88b26dde90d44e72d87` on 28 October 2026. No private package internals, development dataset contents, or simulation database were inspected.

A real baseline run under JiuwenSwarm 0.2.4b3 reached Month 36 at L4, then stopped with a model connection error and no ending score. Its logs showed useful health recovery and changing priorities, but also repeated acknowledgement of risk warnings without mitigation, numerical effect claims not supplied by the handbook, and claims of gains not established by the next observation. Revision v2 added explicit warning-to-action comparison, actual before/after checks, cautious causal attribution, and shorter evidence-based notes. Its real test ended through Health failure in Month 3, with a local quantitative score of 21.77/100. The agent accepted optional demands while Health declined, relying on later recovery. Revision v3 therefore makes preserving the ability to reach recovery explicit.

The submitted v3 procedures completed a fresh 48-month local run at L5, with Health 10, Dignity 10, and quantitative score 64.52/100. Both installed Skill files matched the submission files by SHA-256 after the run, and the agent loaded both through its Skill tool. Nevertheless, it still sometimes asserted unsupported numerical benefits and omitted an explicit mitigation comparison after persistent warnings. These instructions express intended checks; the test does not establish reliable adherence. Different event trajectories and only one full completion prevent a claim of consistent improvement, broad robustness, or token savings. See the decision report for the exact evidence and limitations.

The manifest retains the team name from the verified preliminary entry. Before submission, a real team video must be added and final validation completed. The verified preliminary package remains unchanged.
