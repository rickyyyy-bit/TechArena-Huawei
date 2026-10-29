# Decision report

## Implemented approach

One agent follows a rolling policy rather than a month-by-month script. It reads the current phase and legal choices, checks fragility and warnings, identifies the most useful current repair or development need, compares plausible options, and submits one legal action with a brief rationale. After observing the result it revises its assumptions. `event-decisions` handles story options; `quarterly-planning` handles the quarterly budget, main action, and review-driven adjustment.

The agent balances Health, Dignity, Skill, Network, Output, Wealth, and career level. Serious or persistent threats receive priority when fragile; stable states permit more growth. Avoiding every risk could produce a weak ending, so the policy allows tolerable uncertainty when development is worthwhile. It does not assign unpublished numerical weights or assume that any one statistic guarantees promotion.

## Public information and feedback

Sources are the official competition rules, handbook, public rules, failure-and-ending guide, MCP interface documentation, and current-run observations and logs when available. Public information establishes the 48-month horizon, quarterly Energy budget and action directions, six-month reviews and promotion windows, and general failure directions. These sources do not publish exact promotion, performance, hidden-risk, or failure formulas.

Review grades, warnings, and attribute changes should update the plan during a run. A weak review calls for corrective attention to the observed development gaps; a strong review supports sustained progress rather than reckless escalation. The revised quarterly procedure explicitly compares mitigation against growth when warnings persist or worsen. It checks whether expected gains actually appear and avoids treating an absence of visible cost as proof of zero risk. Promotion preparation occurs across quarters through Skill, Output, and Network, while retaining wellbeing and financial resilience. Approaching the final months changes the time available to benefit from an investment, but does not justify ignoring ending dimensions or risk.

## Principal risks and tradeoffs

- Deteriorating Health or Dignity can undermine future opportunities. Compare recovery against costly growth actions before spending Energy.
- Weak Network, persistent negative Wealth, repeated weak reviews, or lagging Skill need correction even if current Output is strong.
- Organisational risks can accumulate without visible counters. Respond to legitimate warnings without inventing hidden state or assuming a risk action guarantees safety.
- Uncertain story outcomes can make plausible reasoning wrong. Distinguish published effects from predictions and adapt after feedback.
- Exhausting Energy is not itself an objective. Consider useful affordable actions because it does not carry forward, while allowing an early end when spending would be harmful.
- Repeated observation or log calls can waste tokens. Use returned state and recent context when adequate; query again when needed to resolve a consequential ambiguity.

## Generalisation

The procedures depend on the current observation and legal options, not event names, identifiers, ordering, or memorised outcomes. They compare directions, opportunity costs, and observed trends rather than fitting hidden development formulas. The current handbook and offered actions govern play if settings change. Conflicting or missing information calls for a targeted observation, handbook, or recent-log query, not a guessed action identifier. Warnings change priorities without implying an exact failure countdown.

## Evidence status

A real baseline run began on 28 October 2026 with the designated model, JiuwenSwarm 0.2.4b3, and the preliminary Skills in agent mode. Its official simulation session was `f016de801ce94a00a26d4e604c9fdff2`. It reached Month 36 at L4 with Health 10 and Dignity 10 before a model connection error interrupted execution. This is progress into Month 36, not a completed 36-month survival result or a completed 48-month game. The report returned exit code 1 and an empty ending score. Its zero-filled usage fields do not establish zero usage or free play; valid complete metering is unavailable.

The baseline recovered from low Health, responded to review feedback, and progressed from L1 to L4. It also acknowledged repeated organisational risk warnings without choosing explicit mitigation at the following quarterly opportunities; an organisational incident followed in Month 11. This sequence does not establish the hidden causal formula or prove that a different choice would have prevented the incident. It does show that the instructions' warning check did not reliably lead to a mitigation comparison.

Action notes repeatedly asserted numerical benefits that the returned handbook did not supply. Some subsequent observations did not show the predicted gain, yet the agent continued describing it as achieved. It also sometimes attributed a period's whole Health decline to one decision. The revision therefore requires actual state comparison, cautious attribution, explicit mitigation comparison, and a distinction between predicted and observed effects. It includes no event-specific answer or inferred internal threshold.

The official resume attempt supplied an unknown session ID; the agent started another game instead of recovering the original, and that attempt was stopped. No ending score was obtained from those attempts. The revised manifest reports recovery failure rather than inventing state or starting a replacement.

Revision v2 then ran in a fresh real game, session `e8877f1033c641a9b3a5318814191f7b`. It ended through Health failure in Month 3 with a local quantitative score of 21.77/100. The report recorded 1,059,570 tokens and USD 0.029506 of model cost; these are runner-reported development figures, not a full account credit balance. Its log shows acceptance of optional demands while Health was declining, justified by recovery in a future quarter. That future opportunity did not arrive before Health reached zero. Revision v3 therefore gives preserving the ability to reach recovery explicit priority and distinguishes a visible Energy value from actions actually legal in the current phase. It uses no fixed event answer or unpublished health cutoff.

Revision v3 completed a fresh game, session `bf32999e444d4b74b81ce98afe88fd83`. The official local score command confirmed `completed: true`, 48 survival months, and quantitative score 64.52/100. The ending was L5, Health 10, Dignity 10, Skill 96, Network 37, and Wealth 25.4. The runner reported 48,614,866 total tokens and USD 0.936443. The readable replay contains 208 decisions and the ending observation; its Month 49 display is the terminal state after the 48-month career, not a claim of 49 survival months.

The v3 log shows recovery when Health fell, promotion to L5, and responses to review and relationship feedback. It also shows repeated omissions of the intended mitigation comparison and numerical benefit claims stronger than the available evidence. Both Skills were loaded and their installed hashes matched the submission files after the run, so installation success does not imply reliable instruction following. These remain limitations of the submitted design. No additional untested strategy change was made after this completed run.

Original logs, replays, and reports are preserved outside the submission. One v3 completion is evidence that this version can finish under the local configuration, not a demonstration of consistent performance or guaranteed improvement. These runs have different event trajectories and are not a controlled comparison. Token savings are not established. Hypothetical desk checks remain development reasoning rather than gameplay evidence. All local evidence is development feedback, not an official score.
