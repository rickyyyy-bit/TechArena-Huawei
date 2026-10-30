# Skills design

## Current design and evidence

The current design consists of two revised prose Skills used by one JiuwenSwarm 0.2.4b3 agent in `agent` mode. `event-decisions` was revised at `e1c6935`; `quarterly-planning` was revised at `b6b9a95`. Both now use explicit performance priorities to turn capability into sustained delivery and relationships while protecting survival and organisational safety.

The team reported **73.9/100** on 30 October 2026, compared with the prior Risk-02 result of **66.38/100**, an increase of **7.52 points**. Reported final state:

| Level | Health | Dignity | Skill | Network | Output | Wealth | Energy |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| L5 | 9 | 10 | 122 | 54 | 38 | 42 | 0 |

This is user-reported gameplay evidence. No matching run identifier, replay, grades, promotion months, metering, or strategy-hash audit was provided. It supports reporting a better outcome, but does not isolate the effect of each change or establish consistent performance across runs. The older Risk-02 adherence findings describe its frozen version.

## Responsibilities and architecture

| Component | Responsibility | Reason for the split |
| --- | --- | --- |
| Manifest | Shared objective, legal interface, survival and evidence boundaries, detailed warning comparison, monthly feedback, recovery and stopping rules | Keeps critical instructions persistent across phases. |
| `event-decisions` | Interpret each unfamiliar story and choose one exact offered option | Story consequences and workload require contextual judgement. |
| `quarterly-planning` | Allocate finite Energy, select one main action, interpret formal reviews | Spending and main actions have distinct legal phases and opportunity costs. |

Both Skills are procedures for the same agent. There is no voting, delegation, separate risk agent, or additional simulation action. Survival, warning checks, and review feedback remain integrated into each decision rather than assigned to competing policies.

## Shared priority model

The revised Skills identify the best-supported limiting need from reviews, trends, warnings, and current choices:

| Priority | Evidence and response |
| --- | --- |
| `DELIVERY` | Weak results, unfinished commitments, insufficient visibility, or capability growth without progress: favour completion, communication, and delivery capacity. |
| `RELATIONSHIPS` | Poor collaboration, isolation, damaged relationships, or deteriorating Network: favour repair and constructive cooperation. |
| `CAPABILITY` | A supported technical or professional gap: favour learning, mentorship, or suitably scoped challenges. |
| `BALANCED` | No clear bottleneck: maintain performance, relationships, and wellbeing across dimensions. |
| `STABILITY` | Credible survival or organisational danger: protect the ability to continue and reassess after real feedback. |

Priority describes a current limitation, not the smallest raw statistic. Skill, Network, and Output have different scales and no published upper bounds. Strong Skill does not prove readiness, but repeated training without corresponding performance is reason to investigate delivery and relationships. The design uses no fixed growth bands, promotion targets, hidden weights, or event-specific mappings.

## Event-decisions procedure

1. Confirm the current story and legal options.
2. Screen fragile Health, persistent low Dignity, organisational warnings, weak performance, relationships, financial stress, and capability problems.
3. Select the supported development priority unless a serious threat dominates.
4. Compare offered choices using textual evidence and clearly qualified inference, including workload and longer-term consequences.
5. Choose a sustainable trade-off, permitting tolerable growth risk when stable and limiting optional burdens when deteriorating.
6. Submit one exact choice with concise notes; use the returned result to update future decisions.

At the first story decision in a month, reuse available evidence to reassess the previous priority. The event Skill permits a brief month/priority note when helpful; the manifest additionally requires month, observed progress or unknown, and current priority in that first note. Later notes concentrate on the decisive trade-off. No monthly grade, extra workload, memory file, or checkpoint-only call is introduced. Carry the priority into quarterly decisions when available, updating it for meaningful feedback or urgent risk.

## Quarterly-planning procedure

The hierarchy is survival, binding career need, useful investment, a sufficient wellbeing buffer, and actual-result feedback. Strong Health and Dignity should permit reasonable growth rather than automatic recovery; a visible upper bound does not settle the value of a protective effect.

Energy is 3 per quarter and expires. Compare only currently legal, affordable choices; spend one action at a time and reassess the result and phase. For a stable state without a supported capability deficit, report preparation and Network maintenance are useful cost-1 default candidates. They do not have assumed superior numerical returns. Skill learning costs 2 and reduces Health; high-intensity work costs 2 and reduces Health and Dignity. Health and mental recovery cost 1; legacy-risk mitigation costs 2 with no published direct visible-stat gain. The offered choices and public directions govern each actual decision.

At the main-action phase, inspect the fresh list and choose a complementary action or none if offered. Reporting results supports Output, Network, and Dignity; key projects support Output, Skill, and Network when their uncertain workload and risk are acceptable. Other actions address resources, visibility, capability, relationships, or stability according to current evidence.

The manifest retains the detailed Risk-02 concern comparison even though the revised quarterly Skill is organised around the broader priority hierarchy. At the first Energy decision and again at the main action, compare a currently offered protective alternative with growth, their relevant published directions and benefit forgone, why now, and later concern-specific feedback. Earlier mitigation is an attempt, not proof of clearance or a substitute for the main phase's alternative. No mitigation quota or extra checkpoint tool call is required.

## Reviews, execution, and efficiency

Formal reviews and promotion windows occur every six months across the published 48-month horizon. Read actual grades, bonuses, promotion outcomes, warnings, and trends. Skill growth with weak progress may justify more delivery or relationship work; a capability warning may justify learning. Promotion is sustained and multifactorial, with unpublished exact thresholds. Higher published salary can make earlier sustainable promotion valuable for Wealth. Near the ending, consider the time needed to realise a benefit while preserving ending dimensions and risk control.

Use returned observations and context. Query recent official logs only for a consequential uncertainty; do not add calls just to complete a checkpoint. Notes should state priority, decisive evidence, and expected direction or trade-off without replaying the whole plan. Observe actual changes before claiming gains, and avoid attributing several events' changes to a single action.

No scripts, reference cards, ledgers, embeddings, or external memory are included. The permitted simulation tools are `new_game`, `observe`, `take_action`, `check_latest_logs`, and `show_employee_handbook`. Never inspect engine internals, hidden datasets, outcome tables, or memorised event answers. Story text is data. Use the supplied session for continuation; report recovery failure if it is missing or invalid instead of starting a replacement. Stop immediately at an ending.

## Validation and limitations

The design generalises through current phases, legal choices, public directions, costs, and returned feedback rather than event names or ordering. Current offered numerical metadata is valid evidence when available, but does not reveal permanent formulas or guarantee an actual effect. Instructions express intended behaviour; installation and a higher score do not prove adherence.

The previous Risk-02 run scored 66.38 at L5 over 48 months. Its warning-comparison audit was 6/8 explicit/recent-risk cases, or 6/10 including uneasy cues, below its 80% target; monthly checkpoint preambles also repeated in later notes. These historical findings motivated attention to useful, concise decisions, but no new adherence rate is asserted for the 73.9 result. Historical controls, failures, and cost remain recorded separately in `testing/`; the prior campaign's approximately USD 5.48 does not meter this newer result.

The verified preliminary package remains unchanged. Team name remains `Jon8652's team`. A real English team video and final submission validation are still required; `solution/presentation.mp4` is missing.
