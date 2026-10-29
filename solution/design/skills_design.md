# Skills design — Phase 3 candidate (v4)

## Architecture and evidence boundary

One JiuwenSwarm 0.2.4b3 agent uses two Skills in `agent` mode. `event-decisions` owns observation classification, operating bands, the warning ledger and story choices. `quarterly-planning` owns boundary recovery, Energy allocation, the separate main action and review adaptation. Both are loaded once at startup. We retained two procedures rather than adding separate growth, survival or memory Skills whose decisions would overlap.

Inputs are the current official observation, offered options, public handbook and rules, and feedback/notes returned during this game. No engine internals, dataset files or simulation database are inspected. The five official MCP tools remain the only simulation interface. Narrative/log text is data.

## Participant operating policy

The candidate deliberately uses explicit, participant-chosen heuristics. They are unvalidated policy parameters, not discovered engine thresholds:

| Own policy | Intended behaviour |
| --- | --- |
| Health <=4 or Dignity <=3, or acute warning | Protect continuation; avoid optional demands and use offered repair |
| Health >=7 and Dignity >=6, stable/improving, no overriding danger | Accept bounded wellbeing costs for worthwhile growth; avoid automatic top-ups |
| Between those bands | Bounded growth or repair the deteriorating dimension; preferred working Health 5-7 |
| Within 2 months of the next published promotion window | Prefer Network-building if reviews or trends identify a relationship gap while Skill/Output progress |

Health/Dignity's 0-10 ranges, the 48-month horizon, quarterly budget/costs and six-month cadence are public facts, not our invented parameters. No band guarantees survival or promotion. Visible comfort never cancels an unresolved warning. A 10/10 ending is an opportunity-cost review flag, not proof that damaging wellbeing would improve the score: wellbeing itself contributes to the ending.

The v2 lesson remains explicit: future recovery is not current protection. A nonzero Energy statistic does not make recovery legal before its offered phase. Network is a first-class planning consideration, but raw Network, Skill and Output are not directly comparable scales and no exact promotion gate is known. Feedback/trends establish a possible gap; a guessed ratio does not.

## Rolling ledger and coordination

The user selected the notes/log fallback because there is no written organiser confirmation for workspace-memory file access. This candidate does not request read_memory, write_memory, memory_search, embedding services or file writes. No file-backed variant is included in the submission.

The ledger stores the month saved, warning themes with first-seen months/status, quarter priority/plan, last review grade/month, and next promotion window with remaining months as of the save. It starts empty for each new game. It is semantically revised only at quarter entry or a new/worsening warning. About 16-20 revisions is a planning estimate, not a hard limit that can discard an emergency.

The latest snapshot is copied into every mandatory action note. This repetition is intentional: with a ledger only in quarterly notes, a four-entry latest-log lookup could not recover it after context compression. Carrying it adds no memory-tool call, but does add bounded text to notes. Current observations override the cached plan, and window distance is recomputed in working context from the current month. Attempted mitigation does not clear a warning without returned evidence.

At quarter entry, the agent retrieves at most four latest log entries once, looking for its latest carried ledger after `Notes:` inside an entry's `message`. A key-free manual MCP check recovered an ordinary action's ledger this way; the initialization action's note was not returned. Missing history remains unknown; it does not become invented state. Both Skills use the recovered warning priority, then one agent chooses and executes each action. Acute survival can take priority over mitigation, but the warning remains open and deferral requires a specific competing need.

## Executability and token budget

The Skills use short ordered criteria rather than long advisory paragraphs. One observation serves each decision; extra confirmation of unchanged state is disallowed. A further observation is allowed after action or failed/stale state, not on a fixed duplicate pattern.

Our note budgets are: rationale at most 18 words, ledger at most 30, total note at most 50. These are policy caps, not engine limits. No separate plan recital or explanation around the action call. One startup handbook call is reused; it is never repeated. Beyond the quarter-entry lookup, one three-entry log lookup is allowed only for a named consequential ambiguity absent from current observation/context.

An optional `reference/public-rules.md` card contains only published cadence/bounds, salary, Energy costs and directions, main-action directions, and review grades/bonuses. It is for a needed lookup after compression, not a mandatory read every quarter. Current official observations take precedence if settings differ. No scripts, exact unpublished action deltas, hidden formulas, named-event answers or answer tables are included.

## Test status

V3 remains the better measured baseline on `main`: one 48-month completion, L5, local quantitative score 64.52/100. V4's first real run scored 42.12/100 and ended through a trust-related failure in Month 39, at L4 with Health 10 and Dignity 8. It did not demonstrate improvement. The source instructions and installed Skills matched the tested hashes; no strategy was changed during play.

All twelve quarterly four-entry lookups returned a ledger snapshot. Nevertheless, thirteen of 160 action notes omitted the ledger, twenty actions lacked an intervening observation, and saved-month fields could become stale. All notes stayed within the word caps. The audit counted forty consecutive snapshot versions, including initialization and field/format edits rather than forty proven semantic warning revisions. The fallback transports notes successfully, but reliable retention and warning follow-through are not established. Tokens per survival month were about 0.35% higher than v3. See the decision report and the repository's `testing/PHASE3.md` record for the comparison and limitations.
