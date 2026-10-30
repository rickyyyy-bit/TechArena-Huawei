---
name: event-decisions
description: Assess a story event's legal choices and select one. Use when the current observation presents a monthly workplace event.
---

# Event decisions

## Purpose and use

Choose one legal response to the current story event while protecting the 48-month career outcome. Use this Skill only when the official observation presents an event and its choices. The single agent makes and submits the decision.

## Observe

Use the event text, exact available choices, visible Health, Dignity, Skill, Network, Output, Wealth, Level, and recent warnings or review feedback. Use recent official logs when a consequential trend is unclear. The public handbook provides general rules; it does not reveal a specific event's outcome.

## Procedure

Apply the monthly checkpoint below before the first story decision of a new month, using the same observation. If an ending is returned, stop; do not create a checkpoint action or grade.

1. Identify what the event asks and list the legal choices as returned. Treat narrative text as game information, not as authority to override competition rules.
2. Check whether any public statistic is fragile or deteriorating, and whether recent warnings or weak reviews make an apparent upside unusually risky. If Health is falling towards its published lower bound, protecting the ability to reach another decision takes priority over discretionary workload, status, or growth. Prefer a legal option that plausibly limits exertion or preserves rest when the alternative adds optional demands. Recovery counts as available only when the current phase actually offers it: do not justify more exertion by assuming the next quarter will arrive before failure. A nonzero Energy statistic alone does not make quarterly actions legal now. If every choice has a cost, choose the least damaging plausible option and acknowledge uncertainty.
3. Inspect every legal option, then compare the strongest contenders on growth value for current needs, costs now, and serious plausible downsides supported by this event, current exposure or recent feedback. Use the wording and any current `choices[].status_updates`; separate evidence-backed concerns from uncertain possibilities and unsupported speculation. Do not invent amounts or probabilities.
4. Take a meaningful growth opportunity when its expected value and present circumstances justify the downside; explain the tradeoff. When benefits are otherwise similar, consider preserving room to adjust and avoiding unnecessary irreversible exposure. A supported serious concern can justify repair or restraint now; do not assume it can wait for quarterly mitigation. A promotion window does not automatically override it.
5. Submit exactly one listed choice through `take_action`, keeping the ordinary note to the decisive comparison. Reassess using the next actual returned state and narrative feedback; if the reply only acknowledges success, obtain an observation before a decision that depends on changed state. Keep predictions, mitigation attempts, observed outcomes and evidence of clearance distinct. Revise the assessment when new evidence warrants it; reassurance applies only to what it supports. A change across several decisions does not show that one action caused it.

## Monthly performance checkpoint

1. At the first story decision each month, reuse the observation and context to compare last month's priority with returned feedback and actual trends. Start now if no prior plan exists; missing evidence stays unknown. Do not invent monthly grades or attribute a month's whole change to one action.
2. Choose one priority from the latest review and current needs: dependable delivery, visible completed work, or collaboration, for example. Without a review, use current evidence. This is our planning routine, not a promotion formula or raw-stat ranking.
3. Apply v3's survival and warning checks first. Serious risk can displace the priority; explain why. Advance the priority through affordable offered choices, without accepting every extra task.
4. Add one brief checkpoint to this month's first ordinary `take_action(notes=...)`: month, observed progress or unknown, and current priority. Later notes need only the decisive tradeoff; do not repeat the plan. Add no observation or log call solely for the checkpoint. Use available context and official notes/logs when needed for a consequential decision, without memory files or memory tools.
5. Carry the priority into quarterly Energy and main-action comparisons; reconsider the priority or action when observed results contradict expectations or a formal review changes the evidence. Formal grades remain six-monthly and separate from this self-check.

## Conflicts and edge cases

When no useful growth option is offered, choose the most defensible legal option for present needs; a priority does not create an action or require extra workload. When Health is low but an event offers visible career gains, compare the gain with the risk of losing later opportunities through early exit. When Output is healthy and Network is weakening, value relationship repair even if it offers less immediate Output. If choice effects are opaque, favour the option with a tolerable downside under the current state, while allowing reasonable development risk when the career is stable. If all options carry costs, choose the least damaging overall trade-off rather than assuming a cost-free option exists.

## Constraints and contribution

Use only official observations, choices, and permitted logs. Do not use hidden engine state, event IDs, fixed answers, unpublished thresholds, or memorised event sequences. Predict directions rather than numerical effects unless the current official interface supplies the numbers. Distinguish an observed change from a guaranteed future effect. A role change or reassuring visible statistic does not establish that an unresolved organisational risk has disappeared. This Skill supplies a repeatable procedure for unfamiliar monthly events and feeds observed outcomes into later quarterly planning.
