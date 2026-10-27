# Adaptive Career Agent: preliminary Skills design

## Objective and evidence boundary

The agent aims to complete a 48-month engineering career with a strong quantitative ending, not merely survive. The published ending dimensions are career level, wealth, health and dignity, skill, risk control, and network. Output is a published promotion factor, although it is not listed as a separate ending dimension; its exact role in performance reviews is unpublished. The official scoring also rewards Skill quality and token efficiency. Exact promotion, performance, risk, and ending formulas are unpublished, so this design does not assign them invented weights or thresholds.

The public handbook describes monthly story events, quarterly Energy actions and one quarterly main action, and six-month performance reviews and promotion windows. This design uses those published mechanics, plus the state, choices, warnings, logs, and review feedback legitimately returned during the current run. Any predicted effect beyond a published rule or direct observation remains a hypothesis.

## Architecture choice

One JiuwenSwarm `0.2.4b3` agent in `agent` mode uses two Skills:

| Skill | Trigger | Responsibility |
| --- | --- | --- |
| `event-decisions` | A story event offers choices | Interpret the event and legal options, assess immediate and delayed trade-offs, and select one choice. |
| `quarterly-planning` | The quarterly Energy or main-action phase | Spend Energy deliberately, choose a main action when beneficial, and adjust the next quarter's priorities from reviews and trends. |

These are decision procedures at different points in the published game sequence. The single agent selects and executes the final action. The Skills do not represent separate agents or independent votes.

The suggested Risk Management and Career Development Skills overlap at nearly every decision: a high-output choice can also threaten health, while recovery can delay growth. Separate cross-cutting Skills would require repetitive coordination. Their concerns therefore become shared priorities in the manifest instruction and explicit checks in both Skills. Quarterly Planning remains a Skill because its two action stages, non-carrying Energy, and published action directions require a distinct procedure. Event decisions were missing from the initial three-Skill proposal; they merit the other Skill because up to three unfamiliar story events may occur each month. A single comprehensive Skill could be simpler, but would mix event interpretation with the quarter's resource allocation. Three or more Skills have no demonstrated decision-quality benefit at this preliminary stage.

## Shared decision procedure and coordination

1. Read the current official observation and identify the decision phase and available choices. Consult the public handbook when its rules are needed; avoid repeated calls for information already available.
2. Check for severe or worsening public risk indicators: Health, Dignity, Network, Wealth, repeated weak reviews, and warnings. Treat hidden risk only through legitimate warnings or observed consequences.
3. Identify the most important current development gap among Skill, Output, and Network, while considering level, CurrentLevelDuration, reviews, and the remaining career horizon. No single attribute has universal priority.
4. Compare legal choices by published effects, event text, recent in-run feedback, reversibility, Energy cost where applicable, and opportunity cost. Separate known effects from uncertain assumptions.
5. Choose one legal action with a brief note explaining the decisive trade-off. Reobserve or use the returned result, then revise priorities if the outcome differs from expectation.

The manifest supplies this shared policy. `event-decisions` applies it to story choices; `quarterly-planning` applies it to Energy spending and the main action. If growth and recovery conflict, the agent decides once from the current evidence. An imminent promotion window raises the value of development only when the risk of lasting damage remains acceptable. A recent warning or repeated deterioration raises the value of repair, but survival alone is not presumed to maximise the score.

## Risk, planning, and conflicting goals

The agent looks for trends and repeated warnings rather than pretending to know unpublished failure counters. Low Health before a promotion window warrants comparing the plausible benefit of a career action with the possibility of early exit; a safer action may preserve future promotion chances. Learning that costs Health is more attractive when Health is stable or recoverable, and less attractive during a decline. If Output is strong while Network weakens, maintaining relationships can support both resilience and later promotion. A quarterly short-term gain that compounds risk is assessed against its effect across subsequent reviews, not only the present quarter.

Planning is rolling rather than a fixed month-by-month script. After each quarter and six-month review, the agent can change emphasis in response to observed grades, warnings, and attribute movement. Promotion windows recur every six months, but exact requirements are not published. CurrentLevelDuration is context, not a trigger for an assumed promotion threshold. Unused quarterly Energy does not carry over, so the agent should compare available beneficial expenditures before ending the phase, while retaining the option to end when spending would be harmful or pointless. The main action is a separate choice and may be omitted if its available options are unsuitable.

## Feedback, uncertainty, and efficiency

The agent can use the current conversation context and recent official logs to remember the last action, important warnings, reviews, and direction of change. It should request recent logs only when the current observation or context does not already answer a relevant question. Persistent memory across runs is neither assumed nor required. Notes passed through `take_action` can record a short, current-run rationale; they are not a channel for hidden state or external storage.

For uncertain event outcomes, the agent reads the option's wording and estimates direction and downside without asserting numerical effects. It becomes more conservative as serious risks accumulate and adjusts if observed results contradict its expectation. It does not key decisions to event titles, IDs, remembered development sequences, or private simulator data. These general criteria remain usable if event wording, order, or evaluation parameters change.

Concise Skill descriptions indicate when each procedure applies. A single observation and a short comparison should normally suffice for a decision; extra logs or handbook calls should answer a specific uncertainty. This controls token use without removing the checks needed for long-term decisions. No scripts or reference files are needed for this preliminary design.

## Limitations and future work

The registered team name is not available and must replace the explicit manifest placeholder before submission. No competition API key is available, so gameplay, model behaviour, and comparative Skill performance remain untested. After receiving the key, the team should use the designated model and official single-agent runner, examine several complete runs and their logs, and revise only on the basis of public rules and legitimate in-run feedback. The initial two-Skill split is a reasoned design choice, not an experimentally established optimum.
