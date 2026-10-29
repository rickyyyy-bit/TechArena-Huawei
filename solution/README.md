# Adaptive Career Agent

**Candidate: v3 plus monthly performance checks; not model-playtested.** At the first story decision each month, the agent checks prior progress and chooses one feedback-led priority, subject to v3's existing survival and warning rules. It carries that priority into offered story choices and quarterly planning. This adds no monthly grade, game action, memory file or extra observation. The 64.52 result below belongs to unchanged v3 on `main`; higher reviews and earlier promotions are not yet demonstrated.

Team: Jon8652's team (carried forward from the verified preliminary entry).

One JiuwenSwarm 0.2.4b3 agent, with manifest mode `agent`, aims to complete a balanced 48-month career. Two prose Skills provide distinct decision procedures:

- `event-decisions`: compare the current story's legal options against wellbeing, development needs, warnings, and uncertain longer-term consequences.
- `quarterly-planning`: allocate the observed Energy budget, choose a main action, and adapt priorities from performance feedback.

Both use current observations, the public handbook, and feedback from the current run. There are no executable Skills, event answer tables, private formulas, or assumed failure thresholds. See the design documents for reasoning and limitations.

Development evidence: the baseline reached Month 36 at L4 before a connection error interrupted it without an ending score. Revision v2 ended through Health failure in Month 3, scoring 21.77/100 locally. The baseline revision v3 completed all 48 months, ending at L5 with Health 10, Dignity 10, and a local quantitative score of 64.52/100. The runner reported 48,614,866 total tokens and USD 0.936443 for that run. This is one local completion, not an official score or evidence of consistent superiority across runs. Numerical effect claims and warning follow-through remained unreliable despite the revised instructions.

The team presentation is not yet recorded. This directory is incomplete for scored submission until a real English `presentation.mp4` is added and final validation succeeds.
