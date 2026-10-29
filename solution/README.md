# Adaptive Career Agent

**Current branch: Phase 3 candidate v4, not yet model-playtested.** The 64.52/100 result below belongs to preserved v3 on `main`, not these changed instructions. V4 adds participant-chosen operating bands, Network planning, a rolling ledger in official notes, bounded calls, and an optional published-rules card. It uses no workspace-memory files or embedding service.

Team: Jon8652's team (carried forward from the verified preliminary entry).

One JiuwenSwarm 0.2.4b3 agent, with manifest mode `agent`, aims to complete a balanced 48-month career. Two prose Skills provide distinct decision procedures:

- `event-decisions`: compare the current story's legal options against wellbeing, development needs, warnings, and uncertain longer-term consequences.
- `quarterly-planning`: allocate the observed Energy budget, choose a main action, and adapt priorities from performance feedback.

Both use current observations, the public handbook, and feedback from the current run. The reference card contains published facts only. Numerical operating bands are explicitly our unvalidated policy preferences, not engine thresholds. There are no executable Skills, event answer tables or private formulas. See the design documents for reasoning and limitations.

Development evidence: the baseline reached Month 36 at L4 before a connection error interrupted it without an ending score. Revision v2 ended through Health failure in Month 3, scoring 21.77/100 locally. The earlier revision v3 completed all 48 months, ending at L5 with Health 10, Dignity 10, and a local quantitative score of 64.52/100. The runner reported 48,614,866 total tokens and USD 0.936443 for that run. This is one local completion, not an official score or evidence of consistent superiority across runs. Numerical effect claims and warning follow-through remained unreliable in that tested version. No v4 improvement is established.

The team presentation is not yet recorded. This directory is incomplete for scored submission until a real English `presentation.mp4` is added and final validation succeeds.
