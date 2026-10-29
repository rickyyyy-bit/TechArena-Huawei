# Adaptive Career Agent

**Current branch: Phase 3 candidate v4.** Its first real run scored **42.12/100**, eliminated in Month 39 through a trust-related failure. Preserved v3 on `main` scored 64.52 over 48 months and remains the better measured baseline. V4 adds participant-chosen operating bands, Network planning, a rolling ledger in official notes, bounded calls, and an optional published-rules card. It uses no workspace-memory files or embedding service.

Team: Jon8652's team (carried forward from the verified preliminary entry).

One JiuwenSwarm 0.2.4b3 agent, with manifest mode `agent`, aims to complete a balanced 48-month career. Two prose Skills provide distinct decision procedures:

- `event-decisions`: compare the current story's legal options against wellbeing, development needs, warnings, and uncertain longer-term consequences.
- `quarterly-planning`: allocate the observed Energy budget, choose a main action, and adapt priorities from performance feedback.

Both use current observations, the public handbook, and feedback from the current run. The reference card contains published facts only. Numerical operating bands are explicitly our unvalidated policy preferences, not engine thresholds. There are no executable Skills, event answer tables or private formulas. See the design documents for reasoning and limitations.

Development evidence: the baseline reached Month 36 at L4 before a connection error interrupted it without an ending score. Revision v2 ended through Health failure in Month 3, scoring 21.77/100 locally. V3 completed 48 months at L5, scoring 64.52/100, with 48,614,866 reported tokens and USD 0.936443. V4 ended in Month 39 at L4 with Health 10, Dignity 8, Skill 59, Network 34 and Output 19, scoring 42.12/100. It used 39,636,793 reported tokens and USD 1.184291. Tokens per survival month were about 0.35% higher than v3; fewer total tokens reflect a shorter career. These are individual local trajectories, not official scores or controlled causal comparisons. Ledger omissions and skipped observations persisted; no v4 improvement is established.

The team presentation is not yet recorded. This directory is incomplete for scored submission until a real English `presentation.mp4` is added and final validation succeeds.
