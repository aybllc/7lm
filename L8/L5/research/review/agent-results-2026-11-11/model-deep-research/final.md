# Final return of the workflow: The model, read deep

As returned. Run `wf_9a60cf50-a5f`.

- **summary**: Read-only deep research of the 7LM model as it stands on 2026-11-11 and of the gap to both exemplar repositories
- **agentCount**: 26
- **logs**
  - readers returned: 11/11, facts: 740
  - claims: 12, verdicts: 12, corrected or refuted: 10, gaps: 13
- **result**
  - **report**: **Locator key.** REC = `7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md`. SPEC = `7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md`. CHK = `7lm@origin/main:.github/workflows/integrity.yml`. GUIDE = `7lm@origin/main:L8/L6/7lm-field-guide.md`. BETA = `7lm@origin/beta/common-contracts-r1-r6`. PR20 = `7lm@origin/ccr-9391bd81-f2enmj`. PR19 = `7lm@origin/ccr-00099fac-hjosbo`. BOOK = `auditonomous@origin/claude/book-structure-roadmap-k8ap82`. The number after a colon is a line.

    ## The short answer

    The model of record is the scaffold's main at c9dc061. It has 71 canonical positions, 35 on the desk (L7) and 36 in the interior (L8), each count including the root itself, a sheet in every directory, and one check (CHK:47-59). On main the model has not changed since 5 October 2026: the only difference from 2e5a6d6 is one filed proposal, `L8/L6/in/7lm-layer-lists.md`, merged on 11 November 2026. For the exemplars' main branches, "becuase its chamnged" comes to one thing, the L7 restructure of 20 September 2026: `L7/publications/` became `L7/allications/publications/` beside five new positions, `L7/governance/restrictions/` became `L7/governance/controlled/`, the prose was swept to match, and the check's list grew from 57 to 71 (REC:321, REC:498, REC:504). Every later change sits off main: the beta candidate of 2 and 3 November 2026, pull requests #19 and #20, and the owner's audit branch. None of them adds, removes or renames a canonical position, so the physical target is the same whichever is accepted. Each exemplar's main lacks exactly eight positions, `L7/governance/controlled` and the seven `L7/allications` positions, still holds the two former folders, and still words its sheets, README and check the former way; each check lists 57 positions, so it does not flag the eight. Each exemplar's beta candidate already carries the two moves, the six sheets and a 71-entry list, but swept paths and not words, and added research objects and contract edits that go beyond a physical alignment. Not in the brief: each exemplar clone holds a local commit dated 11 November 2026 (8257118, f2d5b37), in no remote-tracking ref, that makes the mirror from main and passes every test run here. Two things the mirror does not settle: the owner's order of 14 September 2026 names peering as well as the model, and the Auditonomous research and manuscript sit mostly on a closed, unmerged branch.

    ## What changed, in time order

    1. **12 September 2026** (11 September, 23:25 Pacific). The rename pass, `USO/` to `L8/` and `l0`–`l6` to `L0`–`L6`, merged in all three repositories within six seconds (7lm 67bb795, autonomous c9076c3, auditonomous 2165144). *On main; physical.* Neither exemplar's main has moved since.
    2. **12 September 2026.** Peers count from 1, layers from 0 (REC:192). *On main; rule and words.* The exemplars owed nothing.
    3. **13 September 2026**, merged 19 September. The packet reading entered the specification: "No position changes, no count changes, no path changes." (REC:283). *On main; words and filed material.*
    4. **14 September 2026.** The owner's order of work: "[source text withheld from the public copy]." and "[source text withheld from the public copy]." (`autonomous@origin/claude/scholarly-pair-baseline-k8ap82:L8/L6/history/exemplar-2026-09-14.md:7`; BOOK:`L8/L6/history/restore-2026-09-14.md:7`). *On two closed, unmerged exemplar branches only; rule.* The roadmap there turns it into steps S0 to S6 and judged the model "[source text withheld from the public copy]" (BOOK:`L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:586`). The restructure overtook that; today's request is that step again.
    5. **19 September 2026.** The owner's edit of `L7/0.md` (0738519) drew `controlled/` and `allications/` before the folders existed (REC:317). *On main; words.*
    6. **19 September 2026.** `in/`, an optional inbox; `L8/L6/in/` created in the scaffold (REC:295). The UHA/oMMP page filed at prior-art. *On main; rule and filed material; not canonical.*
    7. **20 September 2026.** The L7 restructure (REC:315-331, commit 606d4b3): two tracked renames, six new sheets, L7 from 29 sheets to 35, the specification's version of 20 September 2026, the check's list 57 to 63. *On main; physical, words and the check.* This is the change the exemplars' mains lack.
    8. **20 September 2026.** Sections 26 to 31 and 36: the standing rules listed below. The field guide moved to `L8/L6/`. *On main; rule; physical in the scaffold only.*
    9. **20 September 2026.** The prose sweep (REC:498, "a scripted pass with a count per phrase", "Forty-four files."). Commit bbb04dd changes 44 files in all, the check, the .docx and the templates among them; the check's list went 63 to 71 (REC:504). The same section withdrew the guide's "when you can": every folder carries a sheet (REC:502). *On main; words, rule and the check.*
    10. **20 September 2026.** Sections 32 to 35: `1.md`, base dirs, plates, "allics", a separate definitions directory, the picture book. *On main; recorded and not applied*, then parked (REC:494).
    11. **20 September 2026.** The owner's audit branch: 118 commits rewording the specification and about 70 sheets, with a stricter check. *Branch only; words and rule.* The same day, Copilot's 96 recommendations. *Branch only; filed material.*
    12. **5 October 2026.** One heading added at `L7/0.md` line 159 (2e5a6d6). *On main; words.*
    13. **6 October 2026.** "The public face agnostic" (pull request #19). Its record gives the instruction indirectly: "the public is to see the sheets and the source documents without authorship tags of any kind, the author's own included" (PR19:`L8/L6/history/harmonization-2026-09-04.md:514`). *Pull-request branch only; words and filed material.*
    14. **17 October 2026.** The field guide retired (pull request #20), "Deprecated and to be used as an example"; the same record carries "I didn't want anything automated yet" (PR20:`L8/L6/history/harmonization-2026-09-04.md:518`). *Pull-request branch only; physical in the scaffold only; rule.*
    15. **2 November 2026** (Pacific; 3 November UTC). Beta commit 4ca3edb, "Apply approved R1–R6 and exercise bounded research objects"; the same evening the Autonomous beta (805cd42, e64b382) and the Auditonomous beta (714480d). *Beta only; words, the check and filed material; in the exemplar betas also physical.*
    16. **3 November 2026.** Beta commit 97314c5: research-housing guidance in 18 sheets. *Beta only; words.*
    17. **11 November 2026.** Pull request #21 merged: the layer lists, filed at `L8/L6/in/` as a proposal; "the specification controls". *On main; filed material.* No other file on main mentions it.
    18. **11 November 2026.** Local commits 8257118 and f2d5b37 in the two exemplar clones, authored and committed by Claude with this session's trailer. *In no remote-tracking ref; physical, words and the check, each recorded in its own L6.*

    ## The model as it stands on main, from the bottom up

    **L0, semantic and foundational.** What this object itself establishes before any state is declared. Positions: `universality/`, `pedagogy/`, `epistemic/`, `ontology/`, `semantics/definitions/`. It holds only what the object authored: "An externally owned definition is not copied into L0 merely to populate the directory." (SPEC:327).

    **L1, state space.** What states are admissible under L0. One position, `state-space/`. No operation of any kind: "Formal operation begins at L2." (SPEC:378).

    **L2, formal mathematics.** What follows exactly. `formal-mathematics/` with `relations/`, `operators/`, `proofs/`. Nothing approximate or measured.

    **L3, engineering mathematics.** How the exact relation is made feasible. `engineering-mathematics/` with `approximation/`, `uncertainty/`, `tolerances/`. It specifies; it does not realize.

    **L4, conversion.** What was actually made, written, run or measured. `work/` with `writing/`, `experiments/`, `computation/`. "Writing belongs to L4 as performed work. Its research meaning belongs to L5; a released publication belongs to L7." (SPEC:558).

    **L5, research and discourse.** What may responsibly be concluded. `research/` with `lanes/` (the working position), `review/` (the catch-all) and `findings/`; `institution/` with `peers/` and `undergraduates/` (SPEC:679).

    **L6, library.** `history/` and `retired/`. It records and preserves; it does not judge. "Nothing is deleted before it is enumerated" (SPEC:723).

    **L7, the desk.** Numbered, not a layer; a sibling of L8 at the root. Four branches, 35 positions (SPEC:46, SPEC:206-240):

    - `provenance/`: `prior-art/`, `sources/`, `lineage/`, `authority/`.
    - `governance/`: `copyright/` (the one place), `licensing/`, `patents/`, `permissions/`, `access/`, `controlled/`.
    - `peering/`: `private/` and `public/`, each with `ingress/` and `egress/`, each of those with `peer-1/object-1/`. Peers count from 1 (SPEC:66).
    - `allications/`: `publications/`, `applications/`, `communications/`, `specifications/`, `notifications/`, `participations/`. "Each is something the object does toward the outside, once, on a date, leaving a record that can be addressed afterwards." (`7lm@origin/main:L7/allications/0.md:10`).

    **L8, the envelope.** "L8 is a count, not a position" (SPEC:64). The folder holds L0 to L6 as flat siblings: 36 positions with itself.

    **The root.** `README.md`, `L7/`, `L8/`, `.github/`. The specification and the check also admit `.gitignore` (SPEC:281, CHK:23); the scaffold's README says "and nothing else" (`7lm@origin/main:README.md:13`). The scaffold has none on any ref; both exemplars have one.

    **The sheet rule.** Every directory carries `0.md`, first line `# <path>/` (CHK:42-43). Since 20 September: "Give each one a `0.md`; every folder carries one." and "a folder without a sheet is outside the system. Both exemplar repositories do exactly this." (GUIDE:474). The check still says other folders "may carry sheets or not" (CHK:35), and the templates keep the narrower form, "in every folder of the tree the scaffold pushes" (`7lm@origin/main:L8/L6/7lm-sheet-templates.md:3`).

    **The one check.** No conflict markers (G-001); a canonical root (G-002); every sheet headed by its path and all 71 positions sheeted (G-003). On main 75 sheets are checked. Any other folder without a sheet is reported, not failed. Main's check still accepts `USO/` or `L8/` (CHK:27-28).

    **Standing rules.**

    - Mirror by hand: "All repos should mirror the 7lm. Manually. We update 7lm and focus on it only. No outside updates until we are sure I'm close." (REC:336); when the owner judges the scaffold close, and not before (REC:346).
    - Nothing changed without asking: "Don't change the system unless you ask or are unsure" (REC:482).
    - HOA, human-only actions: "for now everything is HOA" (REC:376). No push mechanism is built. The guide adds: "Today the mirroring is by hand" (GUIDE:610). On the pull-request and audit branches only, not on main or the beta: "I didn't want anything automated yet".
    - What is not a design choice: the tree the scaffold pushes, in every folder a `0.md` whose first line is the folder's path (REC:352), and the rule that the guides share no history (REC:408). Everything else a sheet says, and whether a position is used at all, is the repository's own choice (GUIDE:554, :610).
    - The hard rule: "Our 7Lm guides DO NOT share ANY HISTORY! HARD RULE. That's why you have l6." (REC:402). Each repository's history stays at its own L6. The rule bars the scaffold's `history/`, `retired/` and `in/`; the guide and the sheet templates are source documents an adopter takes by a person's act (REC:340, REC:364). Neither exemplar holds a copy of either.
    - What an adopter records: the update "pinned to its hashes", and "what the person declines is listed in their HOA record rather than dropped without a trace" (GUIDE:610).
    - `in/`: an optional inbox at any position, never required, not canonical (REC:299). The exemplars have none and owe none.
    - Blank sheets: beneath a layer a sheet may be its first line only, tagged an audit exception for HOA review; no check was added (REC:390, REC:396).
    - Recorded and not applied: sections 32 to 35, parked by "lets not do 1.md becuase we are still working 0.md and I think i will end up just nmaking it worse." (REC:494).

    ## Main against the beta candidate

    The candidate is two commits on 2e5a6d6, author and committer EDM: 4ca3edb (2 November 2026; 8 files added, 9 modified) and 97314c5 (3 November 2026; 18 sheets modified). Together 24 files modified, 8 added; nothing moved or deleted.

    **What it leaves alone.** The directory tree is identical on main and beta: 97 directories on each. The 71 positions are identical and sheeted on both. The version line still reads "Version of 20 September 2026" although six passages changed, so that string does not identify one text. The harmonization record is untouched and still ends at section 37.

    **R1 to R6.** No document on any ref of the three repositories lists these corrections one by one. The only description is one sentence (BETA:`L8/L6/history/specification-history.md`:106), which names seven items in five clauses. Read against the diff they are, by inference: (1) a bound peer object "never becomes locally authored"; (2) machine metadata exists only "When machine instructions are enabled"; (3) the four named rails are not exhaustive, and "no new directory or fixed ontology is required"; (4) the scale ruling is narrowed to the written instrument; (5) an exact tagged external reference may reach the receiving L0; (6) the byte reading is "an architectural mnemonic, not a theorem". Unrelated R-numbered series exist and are not this set: `autonomous@origin/main:L8/L5/research/review/EBIOS_RECODE_single_object.md` (R1 to R7), `AUDIT_L1_QUOTE_FIDELITY.md:189-194`, and the scaffold's `uha-ommp-exemplar.html:494`.

    **Words.** Six passages of the specification (five rewritten, one Clarification added) with its .docx regenerated; three passages of the field guide; two entries in `specification-history.md`; 18 sheets, of which 11 gain a headed guidance section and 7 are reworded in line.

    **Research-housing guidance** (97314c5). The manuscript stays at `L8/L4/work/writing/`, its argument at `L8/L5/`, its history at `L8/L6/`, a release at `L7/allications/publications/`. On taking an update from the scaffold: "compare the changed contracts, retain the project's data and local choices, record any moves, and review affected dependencies before claiming the project has migrated." (BETA:`L8/0.md`:24).

    **The check.** It drops `USO/` and lowercase layer names and requires `L8/`; `.gitignore` is still admitted. The list of 71 is the same.

    **Filed material.** Eight files: four probe documents at L0 to L3, a probe script, its test and a results file at `L8/L4/work/computation/`, one findings document at L5; and two source-ledger rows. The sheet of `L8/L4/work/computation/` still says "It is empty at present."

    **What its own record does not claim.** "This records the checked common-architecture candidate, not a full-beta or release claim". The second commit calls itself "not an executable or exemplar implementation, migration, merge, release or beta-readiness claim." The owner's approval of R1 to R6 is asserted in three places (the heading at :104, the sentence at :106, the subject of 4ca3edb) and quoted in none. "Codex" appears in one line of that record and nowhere else in any ref or commit message. Not verified: the .docx inspection it reports. The candidate merges into main without conflict today.

    ## Open pull requests and branches on the scaffold

    Open or draft state, and the mapping of pull-request numbers to branches, were not verified; no network was used.

    - **Pull request #20** (c9638a9, 17 October 2026). Retires the field guide to `L8/L6/retired/field-guide-2026-09-20/` as a tracked rename, the only directory on any unmerged branch that is not on main, and writes the hard rule into `L8/L6/0.md`. It merges into main without conflict. It also merges with the beta, but the beta's three guide edits then land in the copy pull request #20 declares unchanged. It is already merged into the pull request #19 and audit branches.
    - **Pull request #19** (b5c3984; written 6 October 2026). Takes authorship tags out of the live text ('quoted as written' 6 times on main, 0 there; 'the owner' 127 against 45), leaves the records "the words as written", sets "Version of 6 October 2026", and adds `.github/release.sh` and `release.yml`. It merges into main without conflict. It conflicts with the beta in 7 files, the specification among them.
    - **The audit branch** (3555866). 118 commits by the owner, all of 20 September 2026. It rewrites the specification and about 70 sheets toward descriptive wording, and would let L0 hold adopted external definitions, the opposite of the beta's fifth correction. Its check allows exactly four root entries, so it would refuse the `.gitignore` both exemplars carry; it also requires a body in every current sheet, against section 30, though no exemplar sheet is heading-only today. It merges into main without conflict, and conflicts with the beta in 12 files and with pull request #19 in 20, so those two cannot both go in cleanly. The record on the pull request #20 branch calls it "neither adopted nor retired".
    - **`copilot/create-error-list`** (1e2fe77). One review file of 96 recommendations. It merges cleanly. No adjudication was found.
    - **`copilot/create-academic-guide-plan`** (e22c5fc, 19 September 2026) and **`ccr-9a67809a-iwii3n`**. Ancestors of main; nothing of their own. The first still shows the state before the restructure: a 57-position list and the two former folders.
    - **The clone.** In `/home/user/7lm`, HEAD is the pull request #20 branch and local main is 2e5a6d6, two commits behind origin/main. `L7/`, `.github/` and `README.md` there equal main's.

    ## Each exemplar against the model

    Nothing under L8 moves in either repository. Pull-request numbers on the exemplars were not verified.

    **Autonomous** (main c9076c3).

    - Positions: 63 of 71; 97 sheets, none wrongly headed. Missing: `L7/governance/controlled`, `L7/allications` and its six children. Still standing: `L7/publications/` (9 files, a `binder/` subtree among them) and `L7/governance/restrictions/` (1 file).
    - Words, live text: `L7/publications` on 29 lines in 23 files; `governance/restrictions` on 16 lines in 13 files; "peering, and publication state" 56 times in 55 sheets; "the L7 publications branch" 8; "access, restrictions" 8; three more phrases at 2 each; the canonical-branches sentence twice.
    - The check lists 57 positions; its comment block on the retired Q-6 step is its own history and stays. README line 9 names the fourth branch "publications". The record ends at section 13, the rename pass.
    - Six folders outside the retired sets have no sheet, three under the binder and three at `autonomous-theory`; the check reports them only. The specification says of both exemplars "Every directory has its 0.md, headed by its path." (SPEC:934), which is not so.
    - The beta (e64b382; 65 files, 1,930 lines added) made the two moves and added 13 sheets: the six allications sheets in its own short form, one at each of the six unsheeted folders, and `peer-1/object-2`; it checks at 110 sheets with no folder unsheeted. It swept paths, not words (56, 8, 2, 2 and 2 remain; "access, restrictions" changed in 2 of 8 places), left the README, and misquotes the specification at `L7/peering/0.md:8` ("…and L7/allications/publications/."). It adds `BETA_HISTORY.md` and no section 14. Beyond alignment: 1,638 of its added lines are 13 new research objects; it edits two binder files and `DEFINITION_LIST_AUTONOMOUS.md`; in `REGISTER.md` it moves "autonomy / autonomous" from not entered to "ADOPTED **as a plural entry**"; it pins scaffold commit 4ca3edb, which is not on the scaffold's main.
    - The local commit 8257118 (78 files): no former phrase left in live text, 103 sheets, 71 positions, record section 14 quoting the request as written. Its check is the scaffold's file with the Q-6 block and a blank line inserted and the scaffold's blank line 12 absent. It conflicts with the beta in 12 files.
    - The closed branch `claude/scholarly-pair-baseline-k8ap82` (9b49910) files at `L7/governance/restrictions/0.md:34`: "this repository is declared a read-only exemplar of the Seven-Layer Model"; the L0 object and its companions "change only by a dated version merged by the owner". It merges cleanly into main; against 8257118 it conflicts in `L7/governance/0.md`, and its files keep former names in three places. The beta's edits to the two L0 companions touch what that declaration reserves.

    **Auditonomous** (main 2165144).

    - Positions: 63 of 71; 78 sheets, none wrongly headed. The same eight are missing. Still standing: `L7/publications/` (5 files) and `L7/governance/restrictions/` (1 file).
    - Words, live text: `L7/publications` on 26 lines in 20 files; `governance/restrictions` on 16 lines in 13 files; the boundary phrase 38 times in 37 sheets; "the L7 publications branch" 9; "access, restrictions" 8; three more at 2 each; the canonical-branches sentence twice.
    - The check lists 57 positions and differs from the scaffold's in five places. README line 9 names the fourth branch "publications". The record ends at section 12.
    - Twelve folders outside the retired sets have no sheet: nine under `staging-records/`, two under the binder, and `autonomous-theory`.
    - The beta (714480d; 56 files, 2,352 lines added) made the two moves, added seven sheets (the six in its own wording and `peer-1/object-2`), and swept the paths. It left all 61 occurrences of the swept phrases, the README and the 12 unsheeted folders. It adds `AUDITONOMOUS_BETA_HISTORY.md` and no section 13. Beyond alignment: it edits `AUDITONOMOUS_DEFINITION.md`, Q13 and `CONTRADICTIONS.md`, which the repository's own record leaves to the owner, and the source `LEDGER.md`; it adds eleven files (2,154 lines); its check is the scaffold beta's, not main's; it pins unmerged commits 4ca3edb and 805cd42. Only 22 of its 56 files are pure alignment.
    - The local commit f2d5b37 (55 files): no former phrase left, 84 sheets, 71 positions, the check byte-identical to the scaffold's main, record section 13. It conflicts with the beta in 13 files.
    - Peering. The binding still names `aybllc/autonomous:research/definitions/AUTONOMOUS.md` at commit `0504961`, a path from before the peer's 7LM layout (`auditonomous@origin/main:L7/peering/public/ingress/peer-1/object-1/0.md:10`), and the guide lists the rebinding as an open call (GUIDE:626-634). The mirror changes one line of that sheet and rebinds nothing; both betas add a second bound object instead.
    - For the research and manuscript. Main's `L8/L4/work/writing/` holds three draft files, two chat transcripts and a session record, and main's research files cite objects absent from its tree (`AUDITONOMY.md`, `STANDARDS_REGISTER.md`, for example `L8/L1/state-space/AUDITON_ENVELOPE.md:76`). The closed branch BOOK (9259c18) holds 328 files against 169: `manuscript/` (55), `book/` (31, headers only: "no chapter has text"), papers, prompts, a sourcebook, 24 review files and more; its record says "[source text withheld from the public copy]". It merges cleanly into main; against f2d5b37 it conflicts in `L7/0.md`, and its new files keep former names. The beta was built from main and conflicts with it in three files. A QA pass therefore has no settled base.

    In both: the binder moves whole, one level deeper, under a branch defined as outward acts, while both records leave open "`binder/internal/` at publications versus L4 writing". Live files still name `uso/l6/LEDGER.md`, a path from before 5 September 2026, the press-kit README and the Autonomous `MANUSCRIPT.tex` among them; the register stands at `L7/provenance/sources/LEDGER.md`. The copied sheet `L7/allications/0.md` carries at line 8 a dated quotation of the owner, the only one in any live exemplar sheet. Neither new record section pins the scaffold commit mirrored or lists what was declined.

    Not verified: every edited line of the two local commits, read one by one.

    ## Decisions that are the owner's

    1. Whether the scaffold is close enough for the hand mirror to land now; section 26 reserves that judgement.
    2. Whether the order of 14 September 2026 still governs, and with it the merge, tag and protection of Autonomous as a read-only exemplar, the papers' review, and roadmap decisions D1 to D23.
    3. Whether a session-made, counted pass is the mirror "Manually", or a proposal for a person to apply.
    4. Whether the exemplars mirror main alone or main with the beta's wording; the folders are the same either way.
    5. Whether the beta candidate is merged into the scaffold's main, and whether the approval of R1 to R6 covered its second commit.
    6. Which mirror lands in each exemplar: the local commit of 11 November 2026, the beta of 2 November 2026, or a fresh pass; the first two conflict in 12 and 13 files.
    7. What becomes of the beta exemplars' research objects and their edits to the definitions, Q13, `CONTRADICTIONS.md`, `LEDGER.md`, `REGISTER.md`, `DEFINITION_LIST_AUTONOMOUS.md` and two binder files.
    8. Whether pull request #20 is merged and, if the beta is too, whether the beta's three guide edits are dropped.
    9. Whether pull request #19 is merged, given its 7 conflicts with the beta and its version date of 6 October 2026.
    10. Whether the exemplars follow the agnostic wording: the owner's quotation at `L7/allications/0.md:8`, and the words of 11 November quoted in the two new record sections.
    11. Whether the audit branch is adopted, retired, or taken in part.
    12. Whether `.gitignore` belongs at a canonical root, since the specification and check admit it and the README does not.
    13. Whether each exemplar's check must be the scaffold's file byte for byte, and in which form: main's, which still accepts `USO/`, or the beta's.
    14. Whether a physical match includes a sheet, blank if need be, at the 18 unsheeted folders, nine of which hold third-party staging records.
    15. Whether `binder/internal/` stays under `L7/allications/publications/` or goes to `L8/L4/work/writing/`.
    16. Whether peering is stable enough to start, and whether the Autonomous definition is rebound before or after the mirror and to which commit.
    17. Whether each new record section pins the scaffold commit mirrored and lists what was declined, as the guide asks.
    18. Whether the "not yet mirrored" sentences (SPEC:950, SPEC:958), the `restrictions/` wording (SPEC:938), SPEC:934 and GUIDE:474 are corrected in the scaffold, the .docx with them, once the exemplars land.
    19. Where the layer lists finally sit, which their own text calls "the owner's call, HOA".
    20. Which base the Auditonomous research and manuscript QA takes, main or the closed book branch, and whether that branch is revived before or after the mirror.
    21. What becomes of the other closed branches: the two `no-deletion-fix` branches and `claude/research-move`, still on `USO/` paths, and the scholarly-pair branch.
    22. Whether the Auditonomous sheets that state 62 ledger rows, against 60 in the register, are corrected now or separately.
    23. Whether the live references to `uso/l6/LEDGER.md` and other paths from before 5 September 2026 are corrected, three of them in binder files that "are not rewritten".
  - **migration_autonomous**
    - item 1
      - **order**: 1
      - **operation**: Precondition: the owner's word, and one hand-made pass from main
      - **detail**: Base: autonomous origin/main c9076c3, unchanged since the rename pass merged on 2026-09-11 23:25:59 -0700. Target: the scaffold's main c9dc061 (the local checkout of /home/user/7lm is the pull request #20 branch, not the model of record; its L7/, .github/ and README.md equal main's). The pass is made by hand, in one commit, on the owner's word; it changes nothing in aybllc/7lm. Expected end state: 103 sheets checked (63 under L7), all 71 canonical positions sheeted, the root unchanged (.github, .gitignore, L7, L8, README.md), nothing under L8 moved. State found: a local commit 8257118 on refs/heads/ccr-9391bd81-f2enmj (author and committer Claude, 2026-11-11 18:33:28 UTC, single parent c9076c3; 78 files: 6 added, 10 renamed, 62 modified) already performs operations 2 to 23. Checked here from git objects: 0 occurrences left of every former phrase in live text, 103 sheets each headed by its path, 71 positions sheeted, the seven binder payload files moved with identical blobs, record section 14 carrying the same per-phrase counts as this list. Applying operations 2 to 22 literally to main reproduces it file for file except the Holdings sections added to the six new sheets, the label and one added sentence at L7/0.md:223, the date, and the two history files. It is in no remote-tracking ref of the clone (the network was not consulted). Whether a session-made, counted pass is the mirror 'Manually' is the owner's decision. It conflicts with the beta candidate e64b382 in 12 files, and with the closed branch claude/scholarly-pair-baseline-k8ap82 in L7/governance/0.md (that branch merges cleanly into main today). Not verified: each edited line read one by one.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:336 and :346 (section 26); 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:482 (section 36); 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:376 ('for now everything is HOA'); autonomous@refs/heads/ccr-9391bd81-f2enmj (8257118): git diff -M --name-status c9076c3 8257118; git branch -a --contains 8257118 (the local branch only); git merge-tree --write-tree 8257118 origin/beta/7lm-exemplar-autonomous (12 files) and 8257118 origin/claude/scholarly-pair-baseline-k8ap82 (L7/governance/0.md)
    - item 2
      - **order**: 2
      - **operation**: Move, as a tracked rename: L7/publications/ to L7/allications/publications/
      - **detail**: git mv L7/publications L7/allications/publications. Nine files follow: 0.md; binder/0.md; binder/README.md; binder/internal/FETCH_LIST.md; binder/internal/README.md; binder/internal/tools/verify_fragments.py; binder/internal/tools/verify_fragments_v2.py; binder/press-kit/GLOSSARY_AUTONOMOUS.md; binder/press-kit/README.md. The seven files that are not sheets move byte for byte and are not edited. The moved files hold no relative link that the extra directory level breaks. The whole binder moves with its folder; whether binder/internal/ belongs here or at L8/L4/work/writing/ is an owner decision this repository's record already leaves open, and the move does not settle it.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:321 (section 25: 'both as tracked renames so their history follows them'); autonomous@origin/main:L7/publications (git ls-tree -r: 9 files); autonomous@origin/main:L7/publications/binder/0.md:8 ('are not rewritten'); autonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:80 ('`binder/internal/` at publications versus L4 writing')
    - item 3
      - **order**: 3
      - **operation**: Move, as a tracked rename: L7/governance/restrictions/ to L7/governance/controlled/
      - **detail**: git mv L7/governance/restrictions L7/governance/controlled. One file, 0.md. It is the same position under a wider name. Note: the closed branch claude/scholarly-pair-baseline-k8ap82 files its read-only-exemplar declaration in this sheet at its former path (line 34 there); in a test merge the declaration follows the rename.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:321 and :319 (section 25); autonomous@origin/main:L7/governance/restrictions/0.md; autonomous@origin/claude/scholarly-pair-baseline-k8ap82:L7/governance/restrictions/0.md:34
    - item 4
      - **order**: 4
      - **operation**: Head the three moved sheets by their new paths
      - **detail**: Line 1 and the Path field on line 4 of each: L7/allications/publications/0.md becomes '# L7/allications/publications/'; L7/allications/publications/binder/0.md becomes '# L7/allications/publications/binder/'; L7/governance/controlled/0.md becomes '# L7/governance/controlled/'. Six lines in three files. No other existing sheet's first line changes.
      - **basis**: 7lm@origin/main:.github/workflows/integrity.yml:42-43 (the first line must equal '# <path>/'); 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:508 ('Every sheet's first line' otherwise not changed); autonomous@origin/main:L7/publications/0.md:1,4; autonomous@origin/main:L7/publications/binder/0.md:1,4; autonomous@origin/main:L7/governance/restrictions/0.md:1,4
    - item 5
      - **order**: 5
      - **operation**: Write six new sheets
      - **detail**: L7/allications/0.md and L7/allications/applications/0.md, communications/0.md, specifications/0.md, notifications/0.md, participations/0.md, each with first line '# <path>/'. Source text: the scaffold's sheets at the same paths (39, 36, 37, 36, 36 and 37 lines). Two lines of the scaffold's L7/allications/0.md are the scaffold's own history; the five child sheets carry none. (a) Line 38, the Standing bullet, names the scaffold's record section 25 and the pass of 2026-09-20; here it names this repository's record section 14 and the date of this pass (the local commit has it at line 42). (b) Line 8 begins 'The owner named this position on 2026-09-19, quoted as written:'. The local commit carries it unchanged, which makes it the only live sheet in this repository with a dated quotation of the owner; this repository's own rule of 2026-09-07 took such text out of sheets, and pull request #19 rewrites the line on the scaffold to cite a record file no exemplar has. Whether line 8 is copied, reworded or left out is the owner's decision; do not correct the quoted words in any case. Spell the folder 'notifications'; 'allications' stands as the owner wrote it. Everything after the first line is this repository's design choice (the local commit adds a Holdings section to each). Sheets go from 97 to 103, L7 sheets from 57 to 63.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:321; 7lm@origin/main:L7/allications/0.md:1-39 (lines 8 and 38); 7lm@origin/main:L7/allications/applications/0.md:1-36; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:352 (section 27: the first line is not a design choice; the rest is); autonomous@8257118:L7/allications/0.md:8,42; autonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:167 ('are pulled out of the sheets'); 7lm@origin/ccr-00099fac-hjosbo:L7/allications/0.md:8
    - item 6
      - **order**: 6
      - **operation**: Words: the canonical-branches sentence (2 occurrences)
      - **detail**: 'Canonical direct L7 branches are L7/provenance/, L7/governance/, L7/peering/, and L7/publications/.' becomes '... and L7/allications/.' at L7/0.md:14 and L7/peering/0.md:8. Do this before the path rewrite of operation 10, so that a blanket replacement cannot produce '... and L7/allications/publications/.', the misquotation that stands on the beta candidate.
      - **basis**: 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:46; 7lm@origin/main:L7/0.md:16; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:323; autonomous@origin/main:L7/0.md:14; autonomous@origin/main:L7/peering/0.md:8; autonomous@origin/beta/7lm-exemplar-autonomous:L7/peering/0.md:8
    - item 7
      - **order**: 7
      - **operation**: Words: redraw the tree in L7/0.md
      - **detail**: Line 66: 'restrictions/0' becomes 'controlled/0'. Line 82: the single last branch 'publications/0' becomes 'allications/0' with six children in this order: publications/0, applications/0, communications/0, specifications/0, notifications/0, participations/0 (seven lines where one stood).
      - **basis**: 7lm@origin/main:L7/0.md:69,85-91; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:323; autonomous@origin/main:L7/0.md:66,82
    - item 8
      - **order**: 8
      - **operation**: Words: two rows of the prose table in L7/0.md
      - **detail**: Row 105, 'governance/restrictions/', becomes the scaffold's row: governance/controlled/ | Directory for restrictions and other conditions that constrain external disclosure, use, transfer, or handling. | Keeps what is controlled explicit and machine-addressable without redefining the underlying research. Row 115, 'publications/', becomes the scaffold's seven rows, copied as they stand: allications/, allications/publications/, allications/applications/, allications/communications/, allications/specifications/, allications/notifications/, allications/participations/.
      - **basis**: 7lm@origin/main:L7/0.md:114,124-130; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:323 ('the prose-and-rationale table gains seven rows'); autonomous@origin/main:L7/0.md:105,115
    - item 9
      - **order**: 9
      - **operation**: Words: the four owned external relations (1 occurrence)
      - **detail**: 'four owned external relations: provenance, governance, peering, and publications.' becomes 'four owned external relations: provenance, governance, peering, and allications — the outward acts, of which publication is one.' at L7/0.md:123.
      - **basis**: 7lm@origin/main:L7/0.md:138; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:323 ('the sentence naming the four owned external relations changes with it'); autonomous@origin/main:L7/0.md:123
    - item 10
      - **order**: 10
      - **operation**: Words: path references to the publications position (22 lines in 20 files; 26 occurrences with the four lines of operation 4)
      - **detail**: 'L7/publications' becomes 'L7/allications/publications' at: L7/0.md:223; L7/governance/0.md:26; L7/governance/access/0.md:24; L7/governance/copyright/0.md:23; L7/governance/licensing/0.md:19; L7/governance/permissions/0.md:24; L7/governance/controlled/0.md:24; L7/peering/0.md:29; L7/peering/private/egress/0.md:25; L7/peering/private/egress/peer-1/object-1/0.md:22; L7/peering/public/0.md:23; L7/peering/public/egress/0.md:10 and 24; L7/peering/public/egress/peer-1/object-1/0.md:21; L7/provenance/0.md:29; L8/L4/0.md:124; L8/L4/work/0.md:30 and 42; L8/L4/work/computation/0.md:40; L8/L4/work/writing/0.md:27; L8/L5/research/findings/0.md:31; L8/L6/0.md:82. Reconciliation: 29 lines in 23 files on main (22 sheets plus the check) = these 22 + 4 heading and Path lines (operation 4) + 2 canonical-branches sentences (operation 6) + 1 line of the check (operation 22). The label of the Holdings bullet at L7/0.md:223 ('publications') is this repository's own wording; the scaffold has no such section; the local commit relabels it 'allications' and adds one sentence.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:325 (section 25, Propagated); autonomous@origin/main: git grep -n -F 'L7/publications' (29 lines, 23 files; counted with git grep -o -F on origin/main, pathspec excluding L8/L6/history, L8/L6/retired, L8/L6/in)
    - item 11
      - **order**: 11
      - **operation**: Words: path references to the governance position (12 lines in 10 files; 14 occurrences with the two lines of operation 4)
      - **detail**: 'L7/governance/restrictions' becomes 'L7/governance/controlled' at: L7/governance/access/0.md:27; L7/governance/licensing/0.md:27; L7/governance/patents/0.md:19 and 25; L7/governance/permissions/0.md:28; L7/peering/private/0.md:10 and 23; L7/peering/private/egress/0.md:24; L7/peering/private/egress/peer-1/0.md:21; L7/peering/private/ingress/0.md:24; L7/provenance/prior-art/0.md:34; L7/provenance/sources/0.md:16. Change the path only: the word 'restrictions' earlier on those lines names a kind of condition and stays. Reconciliation: 16 lines in 13 files on main (12 sheets plus the check) = these 12 + 2 heading and Path lines (operation 4) + the table row at L7/0.md:105 (operation 8) + 1 line of the check (operation 22).
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:325; autonomous@origin/main: git grep -n -F 'governance/restrictions' (16 lines, 13 files; counted with git grep -o -F on origin/main, pathspec excluding L8/L6/history, L8/L6/retired, L8/L6/in)
    - item 12
      - **order**: 12
      - **operation**: Words: the folder name in prose (2 occurrences)
      - **detail**: 'restrictions/' as a folder name becomes 'controlled/' in L7/governance/0.md at line 8 (the six positions) and line 32 (Holdings). The third bare occurrence, the tree line L7/0.md:66, is operation 7. This is the file where the closed scholarly-pair branch conflicts with the mirror: that branch wrote 'One restriction that is not copyright-derived is filed at `restrictions/`'.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498 ('`restrictions/` as a folder name became `controlled/` (2)'); autonomous@origin/main:L7/governance/0.md:8,32; git merge-tree --write-tree 8257118 origin/claude/scholarly-pair-baseline-k8ap82 (conflict in L7/governance/0.md)
    - item 13
      - **order**: 13
      - **operation**: Sweep pair 1: the boundary sentence (56 occurrences in 55 sheets)
      - **detail**: 'peering, and publication state' becomes 'peering, and allications — the outward acts, of which publication is one' (an em dash with a space each side). Twice in L7/0.md (lines 4 and 87) and once in each of 54 other L7 sheets: every L7 sheet on main except L7/provenance/prior-art/ct-lane/0.md and L7/provenance/prior-art/prior-art-lane/0.md, which do not carry it. The scaffold's own count was 37. Scope of every sweep pair: live text = every tracked file except L8/L6/history/ and L8/L6/retired/ (neither exemplar has L8/L6/in/), and except quotations of the owner and third-party source texts.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498 (section 37); autonomous@origin/main: 56 occurrences, 55 files (counted with git grep -o -F on origin/main, pathspec excluding L8/L6/history, L8/L6/retired, L8/L6/in)
    - item 14
      - **order**: 14
      - **operation**: Sweep pair 2: 'the L7 publications branch' (8 occurrences in 5 sheets)
      - **detail**: 'the L7 publications branch' becomes 'L7/allications/publications/' at L7/0.md:112 and 135; L7/peering/0.md:10; L7/peering/public/0.md:10 and 23; L7/peering/public/egress/0.md:14; L7/allications/publications/0.md:10 (twice on that line). The scaffold's count was 11.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498; 7lm@origin/main:L7/0.md:121; autonomous@origin/main: 8 occurrences on 7 lines in 5 files (counted with git grep -o -F on origin/main, pathspec excluding L8/L6/history, L8/L6/retired, L8/L6/in)
    - item 15
      - **order**: 15
      - **operation**: Sweep pair 3: 'peering, and publications become addressable' (2 occurrences)
      - **detail**: becomes 'peering, and allications become addressable' at L7/0.md:6 and 198. The scaffold's count was 3.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498; 7lm@origin/main:L7/0.md:6,217; autonomous@origin/main:L7/0.md:6,198
    - item 16
      - **order**: 16
      - **operation**: Sweep pair 4: 'publications and release identity' (2 occurrences)
      - **detail**: becomes 'allications: the outward acts, of which publication is one' (a colon here, not a dash) at L7/0.md:34 and L7/allications/publications/0.md:8. The scaffold's count was 3.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498; 7lm@origin/main:L7/0.md:37; autonomous@origin/main:L7/0.md:34; autonomous@origin/main:L7/publications/0.md:8
    - item 17
      - **order**: 17
      - **operation**: Sweep pair 5: 'access, restrictions' (8 occurrences in 8 sheets)
      - **detail**: becomes 'access, controlled' at L7/0.md:32 and at line 8 of L7/governance/0.md, access/0.md, copyright/0.md, licensing/0.md, patents/0.md, permissions/0.md and controlled/0.md. The beta candidate changed only two of the eight (L7/0.md:32, L7/governance/0.md:8). The scaffold's count was 10.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498; 7lm@origin/main:L7/0.md:35; autonomous@origin/main: 8 occurrences, 8 files (counted with git grep -o -F on origin/main, pathspec excluding L8/L6/history, L8/L6/retired, L8/L6/in); autonomous@origin/beta/7lm-exemplar-autonomous:L7/0.md:32 and L7/governance/0.md:8
    - item 18
      - **order**: 18
      - **operation**: Sweep pair 6: 'access, and restrictions' (2 occurrences)
      - **detail**: becomes 'access, and controlled conditions' at L7/peering/0.md:28 and L8/L6/0.md:80. The scaffold's count was 2. L8/L6/0.md:80 is the one place under L8 where words, not only a path, change.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498; 7lm@origin/main:L8/L6/0.md:87; autonomous@origin/main:L7/peering/0.md:28; autonomous@origin/main:L8/L6/0.md:80
    - item 19
      - **order**: 19
      - **operation**: Sweep pair 7: 'licensing and restrictions folders' (0 occurrences)
      - **detail**: The scaffold's pair is 'licensing and restrictions folders' to 'licensing and controlled folders' (1 in the scaffold). The phrase does not occur in this repository. Nothing to do; record the zero.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498; autonomous@origin/main: 0 occurrences (counted with git grep -o -F on origin/main, pathspec excluding L8/L6/history, L8/L6/retired, L8/L6/in)
    - item 20
      - **order**: 20
      - **operation**: Words: the two retired cells quoted in the controlled sheet
      - **detail**: In L7/governance/controlled/0.md: line 3 (Object) and the quotation on line 8, 'Directory for restrictions that constrain external disclosure, use, transfer, or handling.', become 'Directory for restrictions and other conditions that constrain external disclosure, use, transfer, or handling.'; the quotation on line 14, 'Keeps restrictions explicit and machine-addressable without redefining the underlying research.', becomes 'Keeps what is controlled explicit and machine-addressable without redefining the underlying research.' With the table row of operation 8, the prose cell changes 3 times and the Why cell 2 times. Leave 'apply public/legal permissions and restrictions' on line 8 as it is.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498 ('the two retired cells quoted in `L7/governance/controlled/0.md` became the current ones'); 7lm@origin/main:L7/governance/controlled/0.md:3,8,14; autonomous@origin/main:L7/governance/restrictions/0.md:3,8,14; autonomous@origin/main:L7/0.md:105
    - item 21
      - **order**: 21
      - **operation**: The README: the reading order (1 occurrence)
      - **detail**: Line 9: '... peering, publications.' becomes '... peering, allications.' Keep this repository's parenthesis on copyright. Nothing else in the README names the desk's branches. The beta candidate left the README unchanged.
      - **basis**: 7lm@origin/main:README.md:9; git -C /home/user/7lm show bbb04dd -- README.md (the scaffold's change, section 37 pass); autonomous@origin/main:README.md:9
    - item 22
      - **order**: 22
      - **operation**: The check: the canonical list, 57 positions to 71
      - **detail**: In .github/workflows/integrity.yml: line 76, 'L7/governance/restrictions' becomes 'L7/governance/controlled'; line 78, 'L7/publications' becomes the scaffold's two lines: the eight positions L7/peering/{private,public}/{ingress,egress}/peer-1 and peer-1/object-1, then L7/allications and its six children. Two comments take the scaffold's wording: line 5 'USO/l6/history/' becomes 'L8/L6/history/'; line 61 'under l6/retired/' becomes 'under L6/retired/ (l6/retired/ before the rename pass)'. Leave lines 16 to 43, the 28-line comment block on the retired Q-6 step, exactly as they are. Do not hard-code the layer names, as the beta candidate did; keep the form main has, which accepts USO/ or L8/. Result: the scaffold's main file with the Q-6 block. The local commit's file (blob 45ad3f7, 97 lines against the scaffold's 69) is exactly that: the scaffold's file with one blank line and the Q-6 block inserted after the G-001 step and without the scaffold's blank line 12; its non-blank content is otherwise identical. Without this operation the check fails on the moved tree. All eight peer-1 and object-1 positions are already sheeted in this repository.
      - **basis**: 7lm@origin/main:.github/workflows/integrity.yml:5,33,47-59; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:325 and :504; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:119 (section 10: 'the one CI check, the same in every 7LM repository'); autonomous@origin/main:.github/workflows/integrity.yml:5,16-43,61,76,78; autonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:140 (the Q-6 step 'kept as recorded'); diff of 7lm@origin/main:.github/workflows/integrity.yml against autonomous@8257118:.github/workflows/integrity.yml ('12d11', '15a15,43')
    - item 23
      - **order**: 23
      - **operation**: Record the pass in this repository's own L6
      - **detail**: Append '## 14. <date> — <title>' to L8/L6/history/harmonization-2026-09-05.md in the same commit: the two moves, the six sheets, each phrase pair with the count applied in this repository, what was not changed, and the check's result. Two things the model's guide asks of an adopter's record and the local commit's section 14 lacks: (a) the scaffold commit mirrored, c9dc061, by its hash, since 'version of 20 September 2026' does not identify one text (the beta changes six passages under the same string); (b) a list of what was declined or deferred, for example the lines of the scaffold's root sheets this repository's sheets do not take (7lm L7/0.md:13, :14, :18, :159, :192; L8/0.md:10, :22). Whether the owner's request of 11 November is quoted in the record as written is the owner's decision (the local commit quotes it in full at line 185; pull request #19's record declines to quote a later instruction on the author's doubt); if quoted, quote it exactly. Do not edit sections 1 to 13. Do not copy text from the scaffold's L6 history: each repository's history is its own. A separate history file is not this repository's convention (the beta candidate added BETA_HISTORY.md and no section 14). The holdings line of L8/L6/history/0.md may name the new section; that is the sheet's body and this repository's choice. The local section's note on the scholarly-pair branch (line 214) says only that the branch 'edits `L7/governance/restrictions/0.md` at its former path'; it does not mention the conflict in L7/governance/0.md.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:402 and :406 (section 31, the hard rule); 7lm@origin/main:L8/L6/7lm-field-guide.md:610 ('pinned to its hashes'; 'what the person declines is listed in their HOA record rather than dropped without a trace'); autonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:169 (section 13, the form to follow); autonomous@8257118:L8/L6/history/harmonization-2026-09-05.md:183,185,187,207,214; 7lm@origin/ccr-00099fac-hjosbo:L8/L6/history/harmonization-2026-09-04.md:514; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:172 (section 14 names the exemplar's own record section)
    - item 24
      - **order**: 24
      - **operation**: Verify
      - **detail**: In live text each of these must count 0: 'governance/restrictions'; 'peering, and publication state'; 'the L7 publications branch'; 'peering, and publications become addressable'; 'publications and release identity'; 'access, restrictions'; 'access, and restrictions'; 'and L7/allications/publications/.'. 'L7/publications' may remain only in the history note in the Standing of L7/allications/0.md. The records under L8/L6/history/ must still hold their former paths. Then the check's tests: no conflict markers; the root canonical; 103 sheets each headed by its path; all 71 positions sheeted. Six folders remain without a sheet and are reported, not failed: internal, internal/tools and press-kit under L7/allications/publications/binder/, and L8/L5/research/review/autonomous-theory with its audit-anon and autonomouos. Since 20 September the scaffold's guide says 'every folder carries one'; whether a sheet is added at these six is the owner's decision and is not part of this list (the beta candidate sheeted all six). Not counted by these tests and left as they are: live references to paths from before 5 September 2026, 'uso/l6/LEDGER.md' at L7/allications/publications/binder/press-kit/README.md:18, L8/L2/formal-mathematics/FORMULAS_LEDGER.md:23, L7/provenance/sources/datasets-LEDGER.md:21 and L8/L4/work/writing/MANUSCRIPT.tex:50 and :79; the register stands at L7/provenance/sources/LEDGER.md.
      - **basis**: 7lm@origin/main:.github/workflows/integrity.yml:13-69 (line 35: 'may carry sheets or not'); 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:331 (how the scaffold's pass was checked); 7lm@origin/main:L8/L6/7lm-field-guide.md:474; simulation of G-003 from git objects on autonomous@8257118: 103 sheets, 0 wrong headings, 0 positions missing, 6 notices; autonomous@origin/main:L8/L6/0.md:79 ('formerly at `uso/l6/LEDGER.md`')
  - **migration_auditonomous**
    - item 1
      - **order**: 1
      - **operation**: Precondition: the owner's word, and one hand-made pass from main
      - **detail**: Base: auditonomous origin/main 2165144, unchanged since the rename pass merged on 2026-09-11 23:26:02 -0700. Target: the scaffold's main c9dc061 (the local checkout of /home/user/7lm is the pull request #20 branch, not the model of record; its L7/, .github/ and README.md equal main's). The pass is made by hand, in one commit, on the owner's word; it changes nothing in aybllc/7lm and touches no research object, definition, ledger row or manuscript file. Expected end state: 84 sheets checked (43 under L7), all 71 canonical positions sheeted, the root unchanged (.github, .gitignore, L7, L8, README.md), nothing under L8 moved. State found: a local commit f2d5b37 on refs/heads/ccr-9391bd81-f2enmj (author and committer Claude, 2026-11-11 18:34:37 UTC, single parent 2165144; 55 files: 6 added, 6 renamed, 43 modified) already performs operations 2 to 23. Checked here from git objects: 0 occurrences left of every former phrase in live text, 84 sheets each headed by its path, 71 positions sheeted, the three binder READMEs moved with identical blobs, the check byte-identical to the scaffold's main (blob f43dd04), record section 13 carrying the same per-phrase counts as this list. Applying operations 2 to 22 literally to main reproduces it file for file except the Holdings sections added to the six new sheets, the label and one added sentence at L7/0.md:223, the date, and the two history files. It is in no remote-tracking ref of the clone (the network was not consulted). Whether a session-made, counted pass is the mirror 'Manually' is the owner's decision. It conflicts with the beta candidate 714480d in 13 files, and with the closed branch claude/book-structure-roadmap-k8ap82 in L7/0.md (the Holdings bullets); that branch, which holds most of the research and manuscript, merges cleanly into main today. The mirror does nothing for peering: the pinned binding at L7/peering/public/ingress/peer-1/object-1/ is unchanged apart from the boundary sentence. Not verified: each edited line read one by one.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:336 and :346 (section 26); 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:482 (section 36); 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:376 ('for now everything is HOA'); auditonomous@refs/heads/ccr-9391bd81-f2enmj (f2d5b37): git diff -M --name-status 2165144 f2d5b37; git branch -a --contains f2d5b37 (the local branch only); git merge-tree --write-tree f2d5b37 origin/beta/7lm-exemplar-auditonomous (13 files) and f2d5b37 origin/claude/book-structure-roadmap-k8ap82 (L7/0.md)
    - item 2
      - **order**: 2
      - **operation**: Move, as a tracked rename: L7/publications/ to L7/allications/publications/
      - **detail**: git mv L7/publications L7/allications/publications. Five files follow: 0.md; binder/0.md; binder/README.md; binder/internal/README.md; binder/press-kit/README.md. The three README files move byte for byte and are not edited. The whole binder moves with its folder; whether binder/internal/ belongs here or at L8/L4/work/writing/ is an owner decision this repository's record already leaves open, and the move does not settle it.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:321 (section 25: 'both as tracked renames so their history follows them'); auditonomous@origin/main:L7/publications (git ls-tree -r: 5 files); auditonomous@origin/main:L7/publications/binder/0.md:8 ('are not rewritten'); auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:94 ('`binder/internal/` at publications versus L4 writing')
    - item 3
      - **order**: 3
      - **operation**: Move, as a tracked rename: L7/governance/restrictions/ to L7/governance/controlled/
      - **detail**: git mv L7/governance/restrictions L7/governance/controlled. One file, 0.md. It is the same position under a wider name.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:321 and :319 (section 25); auditonomous@origin/main:L7/governance/restrictions/0.md
    - item 4
      - **order**: 4
      - **operation**: Head the three moved sheets by their new paths
      - **detail**: Line 1 and the Path field on line 4 of each: L7/allications/publications/0.md becomes '# L7/allications/publications/'; L7/allications/publications/binder/0.md becomes '# L7/allications/publications/binder/'; L7/governance/controlled/0.md becomes '# L7/governance/controlled/'. Six lines in three files. No other existing sheet's first line changes.
      - **basis**: 7lm@origin/main:.github/workflows/integrity.yml:42-43 (the first line must equal '# <path>/'); 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:508; auditonomous@origin/main:L7/publications/0.md:1,4; auditonomous@origin/main:L7/publications/binder/0.md:1,4; auditonomous@origin/main:L7/governance/restrictions/0.md:1,4
    - item 5
      - **order**: 5
      - **operation**: Write six new sheets
      - **detail**: L7/allications/0.md and L7/allications/applications/0.md, communications/0.md, specifications/0.md, notifications/0.md, participations/0.md, each with first line '# <path>/'. Source text: the scaffold's sheets at the same paths (39, 36, 37, 36, 36 and 37 lines). Two lines of the scaffold's L7/allications/0.md are the scaffold's own history; the five child sheets carry none. (a) Line 38, the Standing bullet, names the scaffold's record section 25 and the pass of 2026-09-20; here it names this repository's record section 13 and the date of this pass (the local commit has it at line 42). (b) Line 8 begins 'The owner named this position on 2026-09-19, quoted as written:'. The local commit carries it unchanged, which makes it the only live sheet in this repository with a dated quotation of the owner; this repository's own rule of 2026-09-07 took such text out of sheets, and pull request #19 rewrites the line on the scaffold to cite a record file no exemplar has. Whether line 8 is copied, reworded or left out is the owner's decision; do not correct the quoted words in any case. Spell the folder 'notifications'; 'allications' stands as the owner wrote it. Everything after the first line is this repository's design choice (the local commit adds a Holdings section to each). Sheets go from 78 to 84, L7 sheets from 37 to 43.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:321; 7lm@origin/main:L7/allications/0.md:1-39 (lines 8 and 38); 7lm@origin/main:L7/allications/applications/0.md:1-36; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:352 (section 27); auditonomous@f2d5b37:L7/allications/0.md:8,42; auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:160 ('are pulled out of the sheets'); 7lm@origin/ccr-00099fac-hjosbo:L7/allications/0.md:8
    - item 6
      - **order**: 6
      - **operation**: Words: the canonical-branches sentence (2 occurrences)
      - **detail**: 'Canonical direct L7 branches are L7/provenance/, L7/governance/, L7/peering/, and L7/publications/.' becomes '... and L7/allications/.' at L7/0.md:14 and L7/peering/0.md:8. Do this before the path rewrite of operation 10.
      - **basis**: 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:46; 7lm@origin/main:L7/0.md:16; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:323; auditonomous@origin/main:L7/0.md:14; auditonomous@origin/main:L7/peering/0.md:8
    - item 7
      - **order**: 7
      - **operation**: Words: redraw the tree in L7/0.md
      - **detail**: Line 66: 'restrictions/0' becomes 'controlled/0'. Line 82: the single last branch 'publications/0' becomes 'allications/0' with six children in this order: publications/0, applications/0, communications/0, specifications/0, notifications/0, participations/0 (seven lines where one stood).
      - **basis**: 7lm@origin/main:L7/0.md:69,85-91; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:323; auditonomous@origin/main:L7/0.md:66,82
    - item 8
      - **order**: 8
      - **operation**: Words: two rows of the prose table in L7/0.md
      - **detail**: Row 105, 'governance/restrictions/', becomes the scaffold's row: governance/controlled/ | Directory for restrictions and other conditions that constrain external disclosure, use, transfer, or handling. | Keeps what is controlled explicit and machine-addressable without redefining the underlying research. Row 115, 'publications/', becomes the scaffold's seven rows, copied as they stand: allications/, allications/publications/, allications/applications/, allications/communications/, allications/specifications/, allications/notifications/, allications/participations/. (The beta candidate wrote its own cells here; they are not the scaffold's.)
      - **basis**: 7lm@origin/main:L7/0.md:114,124-130; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:323; auditonomous@origin/main:L7/0.md:105,115
    - item 9
      - **order**: 9
      - **operation**: Words: the four owned external relations (1 occurrence)
      - **detail**: 'four owned external relations: provenance, governance, peering, and publications.' becomes 'four owned external relations: provenance, governance, peering, and allications — the outward acts, of which publication is one.' at L7/0.md:123.
      - **basis**: 7lm@origin/main:L7/0.md:138; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:323; auditonomous@origin/main:L7/0.md:123
    - item 10
      - **order**: 10
      - **operation**: Words: path references to the publications position (19 lines in 17 files; 23 occurrences with the four lines of operation 4)
      - **detail**: 'L7/publications' becomes 'L7/allications/publications' at: L7/0.md:223; L7/governance/0.md:26; L7/governance/access/0.md:24; L7/governance/copyright/0.md:23; L7/governance/licensing/0.md:19; L7/governance/permissions/0.md:24; L7/governance/controlled/0.md:24; L7/peering/0.md:29; L7/peering/private/egress/0.md:25; L7/peering/public/0.md:23; L7/peering/public/egress/0.md:10, 24 and 31; L7/peering/public/egress/peer-1/object-1/0.md:22; L7/provenance/0.md:29; L8/L4/work/0.md:30; L8/L4/work/writing/0.md:27; L8/L5/research/findings/0.md:31; L8/L6/0.md:82. Reconciliation: 26 lines in 20 files on main (25 lines in 19 files of sheets, plus the check) = these 19 + 4 heading and Path lines (operation 4) + 2 canonical-branches sentences (operation 6) + 1 line of the check (operation 22). The label of the Holdings bullet at L7/0.md:223 ('publications') is this repository's own wording; the scaffold has no such section; the local commit relabels it 'allications' and adds one sentence. This Holdings area is where the closed book-structure branch conflicts with the mirror.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:325 (section 25, Propagated); auditonomous@origin/main: git grep -n -F 'L7/publications' (26 lines, 20 files; counted with git grep -o -F on origin/main, pathspec excluding L8/L6/history, L8/L6/retired, L8/L6/in); git merge-tree --write-tree f2d5b37 origin/claude/book-structure-roadmap-k8ap82 (conflict in L7/0.md)
    - item 11
      - **order**: 11
      - **operation**: Words: path references to the governance position (12 lines in 10 files; 14 occurrences with the two lines of operation 4)
      - **detail**: 'L7/governance/restrictions' becomes 'L7/governance/controlled' at: L7/governance/access/0.md:27; L7/governance/licensing/0.md:27; L7/governance/patents/0.md:19 and 25; L7/governance/permissions/0.md:28; L7/peering/private/0.md:10 and 23; L7/peering/private/egress/0.md:24; L7/peering/private/ingress/0.md:24; L7/provenance/sources/0.md:16; L7/provenance/sources/staging-records/0.md:30; L8/L4/work/computation/0.md:38. Change the path only: the word 'restrictions' earlier on those lines names a kind of condition and stays. Only the sheet staging-records/0.md is live text; the staging records beneath it are source material and are not touched. Reconciliation: 16 lines in 13 files on main (15 lines in 12 files of sheets, plus the check) = these 12 + 2 heading and Path lines (operation 4) + the table row at L7/0.md:105 (operation 8) + 1 line of the check (operation 22).
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:325; auditonomous@origin/main: git grep -n -F 'governance/restrictions' (16 lines, 13 files; counted with git grep -o -F on origin/main, pathspec excluding L8/L6/history, L8/L6/retired, L8/L6/in)
    - item 12
      - **order**: 12
      - **operation**: Words: the folder name in prose (2 occurrences)
      - **detail**: 'restrictions/' as a folder name becomes 'controlled/' in L7/governance/0.md at line 8 (the six positions) and line 32 (Holdings: 'licensing/ and restrictions/ are admissible positions that point to copyright/'). The third bare occurrence, the tree line L7/0.md:66, is operation 7.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498 ('`restrictions/` as a folder name became `controlled/` (2)'); auditonomous@origin/main:L7/governance/0.md:8,32
    - item 13
      - **order**: 13
      - **operation**: Sweep pair 1: the boundary sentence (38 occurrences in 37 sheets)
      - **detail**: 'peering, and publication state' becomes 'peering, and allications — the outward acts, of which publication is one' (an em dash with a space each side). Twice in L7/0.md (lines 4 and 87) and once in each of the other 36 L7 sheets, including L7/provenance/sources/staging-records/0.md:24, the binding sheet at L7/peering/public/ingress/peer-1/object-1/0.md (the only line of it that changes) and the two moved sheets. Every L7 sheet on main carries it. The scaffold's own count was 37. Scope of every sweep pair: live text = every tracked file except L8/L6/history/ and L8/L6/retired/ (neither exemplar has L8/L6/in/), and except quotations of the owner and third-party source texts. Note: the closed book-structure branch adds a sheet, L7/provenance/sources/lists-2026-08-08/0.md, that carries the former sentence at line 24; it is outside this pass.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498 (section 37); auditonomous@origin/main: 38 occurrences, 37 files (counted with git grep -o -F on origin/main, pathspec excluding L8/L6/history, L8/L6/retired, L8/L6/in); git diff 2165144 f2d5b37 -- L7/peering/public/ingress/peer-1/object-1/0.md (one line); auditonomous@origin/claude/book-structure-roadmap-k8ap82:L7/provenance/sources/lists-2026-08-08/0.md:24
    - item 14
      - **order**: 14
      - **operation**: Sweep pair 2: 'the L7 publications branch' (9 occurrences in 6 sheets)
      - **detail**: 'the L7 publications branch' becomes 'L7/allications/publications/' at L7/0.md:112 and 135; L7/peering/0.md:10; L7/peering/public/0.md:10 and 23; L7/peering/public/egress/0.md:14; L7/peering/public/egress/peer-1/object-1/0.md:8; L7/allications/publications/0.md:10 (twice on that line). The scaffold's count was 11.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498; 7lm@origin/main:L7/0.md:121; auditonomous@origin/main: 9 occurrences on 8 lines in 6 files (counted with git grep -o -F on origin/main, pathspec excluding L8/L6/history, L8/L6/retired, L8/L6/in)
    - item 15
      - **order**: 15
      - **operation**: Sweep pair 3: 'peering, and publications become addressable' (2 occurrences)
      - **detail**: becomes 'peering, and allications become addressable' at L7/0.md:6 and 198. The scaffold's count was 3.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498; 7lm@origin/main:L7/0.md:6,217; auditonomous@origin/main:L7/0.md:6,198
    - item 16
      - **order**: 16
      - **operation**: Sweep pair 4: 'publications and release identity' (2 occurrences)
      - **detail**: becomes 'allications: the outward acts, of which publication is one' (a colon here, not a dash) at L7/0.md:34 and L7/allications/publications/0.md:8. The scaffold's count was 3.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498; 7lm@origin/main:L7/0.md:37; auditonomous@origin/main:L7/0.md:34; auditonomous@origin/main:L7/publications/0.md:8
    - item 17
      - **order**: 17
      - **operation**: Sweep pair 5: 'access, restrictions' (8 occurrences in 8 sheets)
      - **detail**: becomes 'access, controlled' at L7/0.md:32 and at line 8 of L7/governance/0.md, access/0.md, copyright/0.md, licensing/0.md, patents/0.md, permissions/0.md and controlled/0.md. The scaffold's count was 10. The beta candidate left all eight.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498; 7lm@origin/main:L7/0.md:35; auditonomous@origin/main: 8 occurrences, 8 files (counted with git grep -o -F on origin/main, pathspec excluding L8/L6/history, L8/L6/retired, L8/L6/in)
    - item 18
      - **order**: 18
      - **operation**: Sweep pair 6: 'access, and restrictions' (2 occurrences)
      - **detail**: becomes 'access, and controlled conditions' at L7/peering/0.md:28 and L8/L6/0.md:80. The scaffold's count was 2. L8/L6/0.md:80 is the one place under L8 where words, not only a path, change.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498; 7lm@origin/main:L8/L6/0.md:87; auditonomous@origin/main:L7/peering/0.md:28; auditonomous@origin/main:L8/L6/0.md:80
    - item 19
      - **order**: 19
      - **operation**: Sweep pair 7: 'licensing and restrictions folders' (0 occurrences)
      - **detail**: The scaffold's pair is 'licensing and restrictions folders' to 'licensing and controlled folders' (1 in the scaffold). The phrase does not occur in this repository. Nothing to do; record the zero.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498; auditonomous@origin/main: 0 occurrences (counted with git grep -o -F on origin/main, pathspec excluding L8/L6/history, L8/L6/retired, L8/L6/in)
    - item 20
      - **order**: 20
      - **operation**: Words: the two retired cells quoted in the controlled sheet
      - **detail**: In L7/governance/controlled/0.md: line 3 (Object) and the quotation on line 8, 'Directory for restrictions that constrain external disclosure, use, transfer, or handling.', become 'Directory for restrictions and other conditions that constrain external disclosure, use, transfer, or handling.'; the quotation on line 14, 'Keeps restrictions explicit and machine-addressable without redefining the underlying research.', becomes 'Keeps what is controlled explicit and machine-addressable without redefining the underlying research.' With the table row of operation 8, the prose cell changes 3 times and the Why cell 2 times. Leave 'apply public/legal permissions and restrictions' on line 8 as it is. (The beta candidate left these cells in their retired form.)
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498; 7lm@origin/main:L7/governance/controlled/0.md:3,8,14; auditonomous@origin/main:L7/governance/restrictions/0.md:3,8,14; auditonomous@origin/main:L7/0.md:105
    - item 21
      - **order**: 21
      - **operation**: The README: the reading order (1 occurrence)
      - **detail**: Line 9: '... peering, publications.' becomes '... peering, allications.' Keep this repository's parenthesis on copyright and its sentence on where the definition of autonomous is bound. Nothing else in the README names the desk's branches. The beta candidate left the README unchanged.
      - **basis**: 7lm@origin/main:README.md:9; git -C /home/user/7lm show bbb04dd -- README.md; auditonomous@origin/main:README.md:9
    - item 22
      - **order**: 22
      - **operation**: The check: the canonical list, 57 positions to 71
      - **detail**: Make .github/workflows/integrity.yml identical to the scaffold's main file (blob f43dd04). Five differences: the comment on line 5 ('USO/l6/history/' becomes 'L8/L6/history/'); the comment on line 33 ('under l6/retired/' becomes 'under L6/retired/ (l6/retired/ before the rename pass)'); line 48, 'L7/governance/restrictions' becomes 'L7/governance/controlled'; line 50, 'L7/publications' becomes two lines: the eight positions L7/peering/{private,public}/{ingress,egress}/peer-1 and peer-1/object-1, then L7/allications and its six children. Keep the form main has, which accepts USO/ or L8/; the L8-only form is the unmerged beta's (the beta exemplar's check is that file, blob cd39c5b). Without this operation the check fails on the moved tree. All eight peer-1 and object-1 positions are already sheeted in this repository.
      - **basis**: 7lm@origin/main:.github/workflows/integrity.yml:5,33,47-59; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:325 and :504; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:119 (section 10: 'the one CI check, the same in every 7LM repository'); auditonomous@origin/main:.github/workflows/integrity.yml:5,33,48,50; git rev-parse origin/main:.github/workflows/integrity.yml in /home/user/7lm (f43dd04) and f2d5b37:.github/workflows/integrity.yml in /home/user/auditonomous (f43dd04)
    - item 23
      - **order**: 23
      - **operation**: Record the pass in this repository's own L6
      - **detail**: Append '## 13. <date> — <title>' to L8/L6/history/harmonization-2026-09-05.md in the same commit: the two moves, the six sheets, each phrase pair with the count applied in this repository, what was not changed, and the check's result. Two things the model's guide asks of an adopter's record and the local commit's section 13 lacks: (a) the scaffold commit mirrored, c9dc061, by its hash, since 'version of 20 September 2026' does not identify one text (the beta changes six passages under the same string); (b) a list of what was declined or deferred, for example the lines of the scaffold's root sheets this repository's sheets do not take (7lm L7/0.md:13, :14, :18, :159, :192; L8/0.md:10, :22). Whether the owner's request of 11 November is quoted in the record as written is the owner's decision (the local commit quotes it in full at line 178; pull request #19's record declines to quote a later instruction on the author's doubt); if quoted, quote it exactly. Do not edit sections 1 to 12. Do not copy text from the scaffold's L6 history: each repository's history is its own. A separate history file is not this repository's convention (the beta candidate added AUDITONOMOUS_BETA_HISTORY.md and no section 13). The holdings line of L8/L6/history/0.md may name the new section; that is the sheet's body and this repository's choice. One statement in the local section needs correcting if it is kept: at line 207 it says of the book-structure branch 'thirty of its live files name the former paths as `main` did'; four of the thirty are the branch's own new files (26 on main), and neither the conflict in L7/0.md nor the swept sentence in the branch's new sheet is mentioned.
      - **basis**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:402 and :406 (section 31, the hard rule); 7lm@origin/main:L8/L6/7lm-field-guide.md:610 ('pinned to its hashes'; 'what the person declines is listed in their HOA record rather than dropped without a trace'); auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:162 (section 12, the form to follow); auditonomous@f2d5b37:L8/L6/history/harmonization-2026-09-05.md:176,178,180,200,207; 7lm@origin/ccr-00099fac-hjosbo:L8/L6/history/harmonization-2026-09-04.md:514; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:172
    - item 24
      - **order**: 24
      - **operation**: Verify
      - **detail**: In live text each of these must count 0: 'governance/restrictions'; 'peering, and publication state'; 'the L7 publications branch'; 'peering, and publications become addressable'; 'publications and release identity'; 'access, restrictions'; 'access, and restrictions'; 'and L7/allications/publications/.'. 'L7/publications' may remain only in the history note in the Standing of L7/allications/0.md. The records must still hold their former paths (7LM_ROUTING_PLAN_2026-09-05.md on 6 lines; the record on 1). Then the check's tests: no conflict markers; the root canonical; 84 sheets each headed by its path; all 71 positions sheeted. Twelve folders remain without a sheet and are reported, not failed: nine beneath L7/provenance/sources/staging-records/, internal and press-kit under L7/allications/publications/binder/, and L8/L5/research/review/autonomous-theory. Since 20 September the scaffold's guide says 'every folder carries one'; whether a sheet is added at these twelve, nine of which hold third-party staging records, is the owner's decision and is not part of this list (the beta candidate left all twelve). Not counted by these tests and left as they are: live references to paths from before 5 September 2026, 'uso/l6/LEDGER.md' at L7/allications/publications/binder/README.md:11 and binder/press-kit/README.md:18, L8/L2/formal-mathematics/FORMULAS_LEDGER.md:23 and L7/provenance/sources/datasets-LEDGER.md:21, and 'manuscripts/definitions/AUDITONOMOUS_DEFINITION.md' at binder/README.md:23; the register stands at L7/provenance/sources/LEDGER.md. Also unchanged by the pass: main's research files cite objects absent from main's tree (AUDITONOMY.md, STANDARDS_REGISTER.md), which exist only on the closed book-structure branch.
      - **basis**: 7lm@origin/main:.github/workflows/integrity.yml:13-69 (line 35: 'may carry sheets or not'); 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:331; 7lm@origin/main:L8/L6/7lm-field-guide.md:474; simulation of G-003 from git objects on auditonomous@f2d5b37: 84 sheets, 0 wrong headings, 0 positions missing, 12 notices; auditonomous@origin/main:L7/publications/binder/README.md:11,23; auditonomous@origin/main:L8/L1/state-space/AUDITON_ENVELOPE.md:76
  - **do_not_touch**
    - The records under L8/L6/history/ in each exemplar, apart from the one new section: the earlier sections of harmonization-2026-09-05.md, 7LM_ROUTING_PLAN_2026-09-05.md (it names the former paths on 1 line in Autonomous and 6 in Auditonomous), LEDGER.md, sheets-2026-09-07.md. Why: 'A record states what was so when it was written; moving a path inside it would falsify it.' (7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:327; :508).
    - Everything below the root of each retired set under L8/L6/retired/ (layout-2026-08-14, layout-2026-09-06). Why: a retired set keeps its prior files verbatim with headings uncorrected, and the check does not read below a set's root (7lm@origin/main:.github/workflows/integrity.yml:33-40; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:327; autonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:177; auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:170).
    - The owner's words, wherever they are quoted, typos included. Why: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:508 ('The owner's words, anywhere.'); 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:291 (a tidied quotation was restored as written). Whether a given quotation is carried into an exemplar at all (the scaffold's L7/allications/0.md:8; the request of 11 November in the new record sections) is the owner's decision; if carried, it is carried exactly.
    - The first line of every existing sheet other than the three that move. Why: the first line is the folder's path and is not a design choice (7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:352; :508).
    - The word 'restrictions' where it names a kind of condition and not the position: 'apply public/legal permissions and restrictions' (6 occurrences in each exemplar), 'restriction conditions' (3 in each), the prose before the path on the governance and peering lines, and 'execution restrictions' at L8/L2/0.md:17. Why: 'are not position names and stand' (7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498).
    - The words 'publications' and 'publication' where the scaffold's own sheets keep them: the L7 Object line 'External provenance, public/legal governance, peering, publications, exposure, and exchange.' (L7/0.md:3) and its quotation at L8/0.md:99, the Function row, and 'publication branches'. Why: the scaffold's sheet still reads so (7lm@origin/main:L7/0.md:3); the lines that still say 'publications' in the two local commits are carried identically by the scaffold's main.
    - Third-party and source texts. Autonomous: the source texts under L7/provenance/ (the prior-art lanes and the staging records) and the dated research records under L8/L5/research/review/. Auditonomous: everything beneath L7/provenance/sources/staging-records/ except its sheet 0.md, the register L7/provenance/sources/LEDGER.md, the peer objects, and the deep-research files under L8/L4/work/computation/. Why: 'publications' and 'restrictions' there are other people's words or parts of addresses; the scaffold's sweep excluded filed source pages and quotations (7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498). The Auditonomous beta candidate edited LEDGER.md; the mirror does not.
    - The contents of the binder files that move: seven in Autonomous (README.md, internal/FETCH_LIST.md, internal/README.md, internal/tools/verify_fragments.py, internal/tools/verify_fragments_v2.py, press-kit/GLOSSARY_AUTONOMOUS.md, press-kit/README.md) and three README files in Auditonomous. They move byte for byte, and the whole binder moves with its folder. Why: each binder sheet says they 'are not rewritten' (autonomous@origin/main:L7/publications/binder/0.md:8; auditonomous@origin/main:L7/publications/binder/0.md:8). The Autonomous beta candidate edited two of them. Do not split binder/internal/ off to L8/L4/work/writing/ in this pass: both records leave that to the owner (autonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:80; auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:94).
    - Live references to paths from before 5 September 2026: 'uso/l6/LEDGER.md' in the press-kit READMEs (line 18 in both), the Auditonomous binder README (:11, and :23 naming 'manuscripts/definitions/AUDITONOMOUS_DEFINITION.md'), L8/L2/formal-mathematics/FORMULAS_LEDGER.md:23 and L7/provenance/sources/datasets-LEDGER.md:21 in both, and autonomous L8/L4/work/writing/MANUSCRIPT.tex:50 and :79. Why: they are not names of the 20 September restructure; three are binder files that 'are not rewritten'; the rename pass rewrote path references in sheets and three named files only (autonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:175). Correcting them is a separate decision of the owner's; the register stands at L7/provenance/sources/LEDGER.md.
    - The definitions and the research objects: in Autonomous L8/L0/semantics/definitions/AUTONOMOUS.md, REGISTER.md and DEFINITION_LIST_AUTONOMOUS.md; in Auditonomous L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md, Q13 of L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md and L8/L5/research/review/CONTRADICTIONS.md; in both, every manuscript and draft file under L8/L4/work/writing/. Why: a physical mirror changes names, not content; the Auditonomous record leaves those three items to the owner (auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:89-95); the read-only-exemplar declaration on the closed scholarly-pair branch says the Autonomous L0 object and its companions 'change only by a dated version merged by the owner' (autonomous@origin/claude/scholarly-pair-baseline-k8ap82:L8/L6/history/exemplar-2026-09-14.md:11).
    - The pinned binding of the Autonomous definition in Auditonomous at L7/peering/public/ingress/peer-1/object-1/ (commit 0504961, the peer's pre-7LM path); only the boundary sentence of its sheet changes. Do not rebind it and do not add a second bound object, as both beta candidates did. Why: 'rebinding to a current version being the owner's act' (auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:170; 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:958); the scaffold's guide lists it under open calls (7lm@origin/main:L8/L6/7lm-field-guide.md:626-634).
    - The comment block on the retired Q-6 step in Autonomous's check, lines 16 to 43. Why: it is that repository's own history, 'kept as recorded' (autonomous@origin/main:.github/workflows/integrity.yml:16-43; autonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:140).
    - The root of each exemplar, .gitignore included. Why: the specification and the check admit it (7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:281; 7lm@origin/main:.github/workflows/integrity.yml:23). Only the audit branch's check would refuse it, and that branch is neither adopted nor retired.
    - Every directory under L8. Why: nothing in the interior moved in the model. Path references change in six L8 sheets in Autonomous and five in Auditonomous, and in both L8/L6/0.md:80 also takes the word sweep of operation 18; nothing else under L8 changes apart from the new record section. Do not add L8/L6/in/: it is optional and not canonical (7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:299).
    - The scaffold. No file in aybllc/7lm changes in this pass, including the statements that go out of date once the exemplars land (7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:938, :950, :958, and the same statements in the .docx rendering) and the two that are already untrue of the exemplars (specification :934, 'Every directory has its 0.md, headed by its path.'; 7lm@origin/main:L8/L6/7lm-field-guide.md:474, 'Both exemplar repositories do exactly this.'). Why: 'Don't change the system unless you ask or are unsure' (7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:482).
    - The scaffold's history and the scaffold-only files. Copy no text of the scaffold's L8/L6/history/, retired/ or in/ into an exemplar. Why: the hard rule, 'Our 7Lm guides DO NOT share ANY HISTORY! HARD RULE.' (7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:402, :406). The field guide and the sheet templates are not barred by that rule, being source documents an adopter takes by a person's act (:340, :364), but taking them is a separate design choice and no part of this pass; neither exemplar holds a copy. Likewise do not add the plate sheet, FIRST_IS_ALWAYS_0.md, the specification or the layer lists: none is a canonical position.
    - Anything from record sections 32 to 35: 1.md, base dirs, plate assignments, 'allics', a separate definitions directory, a blank lineage sheet, the picture book; and the push mechanism of section 27. Why: recorded and not applied, then parked (7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:418, :444, :459, :478, :494); of the push mechanism the record says none of it is built (:354).
    - The unmerged and closed branches: the three beta candidates, the scaffold's pull requests #19 and #20, the audit branch, and the exemplars' no-deletion-fix, scholarly-pair-baseline, book-structure-roadmap and research-move branches. Do not merge, rebase or cherry-pick from them as part of the pass, and do not edit them to follow the mirror. Why: each is an open decision of the owner's; the beta candidates bundle research objects and contract edits with the alignment; the scholarly-pair and book-structure branches merge cleanly into main today and conflict with the mirror in one file each (L7/governance/0.md; L7/0.md), which the owner should know before choosing the order.
    - The folders that have no sheet (six in Autonomous, twelve in Auditonomous) and the sheet statements that disagree with the tree for reasons unrelated to the restructure (Auditonomous: 62 ledger rows stated where the register holds 60; in both: the sentence that the harmonized specification is filed at L8/L4/work/writing/; in Auditonomous, research files on main that cite AUDITONOMY.md and STANDARDS_REGISTER.md, absent from main's tree). Why: they are not part of record sections 25 or 37; the check reports the folders and does not fail (7lm@origin/main:.github/workflows/integrity.yml:35); the scaffold's guide now says 'every folder carries one' (7lm@origin/main:L8/L6/7lm-field-guide.md:474), so whether sheets are added is an owner decision, not a step of this list.
    - Every other sentence of every sheet. The scaffold's sheets say things the exemplars' do not (the FIRST-is-0 bullet, the name as design, the packet reading, 'Many intelligences at one face', the heading about private repositories: 7lm@origin/main:L7/0.md:13, :14, :18, :192, :159) and the exemplars' say things the scaffold's do not (Holdings). Why: what a sheet says after its first line is a design choice (7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:352); the pass matches the names of positions, not the bodies of sheets. What is left out is listed in the new record section as declined or deferred.
  - **owner_decisions**
    - 1. Whether the scaffold is close enough for the hand mirror to land now; section 26 reserves that judgement.
    - 2. Whether the order of 14 September 2026 still governs, and with it the merge, tag and protection of Autonomous as a read-only exemplar, the papers' review, and roadmap decisions D1 to D23.
    - 3. Whether a session-made, counted pass is the mirror "Manually", or a proposal for a person to apply.
    - 4. Whether the exemplars mirror main alone or main with the beta's wording; the folders are the same either way.
    - 5. Whether the beta candidate is merged into the scaffold's main, and whether the approval of R1 to R6 covered its second commit.
    - 6. Which mirror lands in each exemplar: the local commit of 11 November 2026, the beta of 2 November 2026, or a fresh pass; the first two conflict in 12 and 13 files.
    - 7. What becomes of the beta exemplars' research objects and their edits to the definitions, Q13, CONTRADICTIONS.md, LEDGER.md, REGISTER.md, DEFINITION_LIST_AUTONOMOUS.md and two binder files.
    - 8. Whether pull request #20 is merged and, if the beta is too, whether the beta's three guide edits are dropped.
    - 9. Whether pull request #19 is merged, given its 7 conflicts with the beta and its version date of 6 October 2026.
    - 10. Whether the exemplars follow the agnostic wording: the owner's quotation at L7/allications/0.md:8, and the words of 11 November quoted in the two new record sections.
    - 11. Whether the audit branch is adopted, retired, or taken in part.
    - 12. Whether .gitignore belongs at a canonical root, since the specification and check admit it and the README does not.
    - 13. Whether each exemplar's check must be the scaffold's file byte for byte, and in which form: main's, which still accepts USO/, or the beta's.
    - 14. Whether a physical match includes a sheet, blank if need be, at the 18 unsheeted folders, nine of which hold third-party staging records.
    - 15. Whether binder/internal/ stays under L7/allications/publications/ or goes to L8/L4/work/writing/.
    - 16. Whether peering is stable enough to start, and whether the Autonomous definition is rebound before or after the mirror and to which commit.
    - 17. Whether each new record section pins the scaffold commit mirrored and lists what was declined, as the guide asks.
    - 18. Whether the "not yet mirrored" sentences (SPEC:950, SPEC:958), the restrictions/ wording (SPEC:938), SPEC:934 and GUIDE:474 are corrected in the scaffold, the .docx with them, once the exemplars land.
    - 19. Where the layer lists finally sit, which their own text calls "the owner's call, HOA".
    - 20. Which base the Auditonomous research and manuscript QA takes, main or the closed book branch, and whether that branch is revived before or after the mirror.
    - 21. What becomes of the other closed branches: the two no-deletion-fix branches and claude/research-move, still on USO/ paths, and the scholarly-pair branch.
    - 22. Whether the Auditonomous sheets that state 62 ledger rows, against 60 in the register, are corrected now or separately.
    - 23. Whether the live references to uso/l6/LEDGER.md and other paths from before 5 September 2026 are corrected, three of them in binder files that "are not rewritten".
  - **claims_total**: 12
  - **claims_not_standing**
    - item 1
      - **claim**: The one physical change the exemplars have not received is the L7 restructure of 20 September 2026 (record section 25): L7/publications/ moved to L7/allications/publications/ and L7/governance/restrictions/ to L7/governance/controlled/, both as tracked renames, with six new sheets. The same day the prose was swept to match (section 37, a scripted pass with a count per phrase, 44 files) and the check's list was raised to 71. The scaffold's record and specification both state that the exemplars were not brought into step.
      - **id**: K03
      - **verdict**: corrected
      - **reasoning**: Every cited locator checks out, but three parts of the claim are imprecise or true only of a particular ref.

        CONFIRMED
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:315 is the heading "## 25. 2026-09-20 — the L7 restructure: allications, and controlled". Line 321: "`L7/publications/` moved to `L7/allications/publications/` and `L7/governance/restrictions/` to `L7/governance/controlled/`, both as tracked renames so their history follows them." and "L7 goes from 29 sheets to 35."
        - Commit 606d4b3 (2026-09-20 07:01 UTC), name-status with -M: R090 L7/publications/0.md -> L7/allications/publications/0.md; R089 L7/governance/restrictions/0.md -> L7/governance/controlled/0.md; six added sheets (L7/allications/0.md and applications, communications, notifications, participations, specifications). Six new sheets is right.
        - Line 329: "They are not brought into step by this pass and now differ from the specification at those names." Specification :950 and :958 both end "the L7 restructure is not yet mirrored." (also :938 "restrictions/ (the position this specification now names controlled/)"). specification-history.md:101 says the same.
        - Line 498: "by a scripted pass with a count per phrase" ... "Forty-four files." Line 504: "its canon list gains the eight peer-1 and object-1 positions the specification's tree draws, seventy-one positions in all".
        - Commit bbb04dd (2026-09-20 20:28 UTC, same day): 44 files changed. The canon list in .github/workflows/integrity.yml counts 57 at 606d4b3^, 63 at 606d4b3, 71 at bbb04dd, and 71 on origin/main (file unchanged since bbb04dd). Both commits are ancestors of origin/main.
        - Tree check, exemplars' main: against the scaffold's 71 canonical positions, autonomous@origin/main (c9076c3) and auditonomous@origin/main (2165144) each lack exactly eight sheeted positions: L7/governance/controlled and the seven L7/allications positions. Both still have L7/publications/ and L7/governance/restrictions/. The eight peer-1/object-1 positions are already sheeted in both. So at the canonical positions the L7 restructure is the only difference.
        - No later canonical change on the scaffold: bbb04dd..origin/main adds only L8/L6/in/7lm-layer-lists.md (non-M changes), plus record text.

        IMPRECISE OR REF-DEPENDENT
        1. "have not received" is true of each exemplar's origin/main only. The unmerged candidates already carry it: autonomous@origin/beta/7lm-exemplar-autonomous (e64b382) and auditonomous@origin/beta/7lm-exemplar-auditonomous (714480d) each have L7/allications/ with all six children, L7/governance/controlled/, no missing canonical position, and a 71-entry canon list; their diffs from main show R L7/publications/0.md -> L7/allications/publications/0.md and R094 L7/governance/restrictions/0.md -> L7/governance/controlled/0.md. (auditonomous@origin/claude/book-structure-roadmap-k8ap82, 9259c18, does not carry it.)
        2. "The one physical change" holds for canonical positions but leaves out two things in the tree. (a) Each exemplar's own .github/workflows/integrity.yml on main still has a 57-entry canon list naming L7/publications and L7/governance/restrictions and not listing the eight peer-1/object-1 positions; the check is a file that must change with the move, or it will fail on the moved tree. (b) The scaffold has a sheeted non-canonical L8/L6/in/ (record section 24, 2026-09-19, after the exemplars' last sync); neither exemplar's main has L8/L6/in/. The record calls it optional (:313 "`in/` is optional everywhere"), so it is not owed, but it is a physical difference. Also, in the exemplars the publications move is not one sheet as in the scaffold: L7/publications/ holds a binder/ subtree (9 files in autonomous@origin/main, 5 in auditonomous@origin/main).
        3. "44 files" is what the record says in its sweep paragraph, and it equals the total file count of commit bbb04dd. That commit also carries non-sweep changes: integrity.yml (the canon list and a comment), the .docx, and L8/L6/7lm-sheet-templates.md add no line containing "allications" or "controlled" (41 of the 44 do). So 44 is the whole commit, not the phrase sweep alone. Section 37's own text was committed separately in e8a5a2c (same timestamp), not in bbb04dd.

        Not found: any statement in the scaffold's record or specification on origin/main that the exemplars have been brought into step; sections end at 37.
      - **corrected_statement**: On their main branches (autonomous@origin/main c9076c3, auditonomous@origin/main 2165144) the exemplars lack exactly one change to the canonical positions: the L7 restructure of 20 September 2026 (record section 25, commit 606d4b3). In the scaffold, L7/publications/ moved to L7/allications/publications/ and L7/governance/restrictions/ to L7/governance/controlled/, both as renames git follows (R090, R089), with six new sheets (L7/allications/ and five siblings of publications); L7 went from 29 sheets to 35. Each exemplar's main is missing eight sheeted canonical positions (L7/governance/controlled and the seven L7/allications positions) and still holds L7/publications/ (with a binder/ subtree: 9 files in autonomous, 5 in auditonomous) and L7/governance/restrictions/. Each exemplar's own integrity.yml on main still lists 57 canonical positions under the former names, against the scaffold's 71, so the check file must change with the move. The scaffold also has an optional, non-canonical L8/L6/in/ that neither exemplar's main has. The unmerged candidates of 2 November 2026 (autonomous@origin/beta/7lm-exemplar-autonomous e64b382, auditonomous@origin/beta/7lm-exemplar-auditonomous 714480d) already carry the restructure and a 71-entry check list; they are not merged. The same day the scaffold's prose was swept to match (section 37, "a scripted pass with a count per phrase", "Forty-four files"; commit bbb04dd changes 44 files in total, including the check file, the .docx and the templates, which are not phrase-sweep changes), and the check's list went from 57 to 63 in 606d4b3 and from 63 to 71 in bbb04dd. The scaffold's record (harmonization-2026-09-04.md:329, "They are not brought into step by this pass and now differ from the specification at those names.") and specification (:950 and :958, "the L7 restructure is not yet mirrored") both state that the exemplars were not brought into step.
      - **evidence_checked**
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:315 (heading of section 25)
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:321 ('both as tracked renames so their history follows them'; 'L7 goes from 29 sheets to 35')
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:329 ('They are not brought into step by this pass and now differ from the specification at those names.')
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:313 ('`in/` is optional everywhere')
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:492-498 (section 37; 'by a scripted pass with a count per phrase'; 'Forty-four files.')
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:504 ('seventy-one positions in all')
        - 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:938, :950, :958 ('the L7 restructure is not yet mirrored')
        - 7lm@origin/main:L8/L6/history/specification-history.md:101 ('still carry the former branch names and are not brought into step by this pass')
        - 7lm commit 606d4b3 (2026-09-20 07:01 UTC): git show -M --name-status: R090 L7/publications/0.md, R089 L7/governance/restrictions/0.md, six A sheets under L7/allications/; integrity.yml canon list 57 -> 63
        - 7lm commit bbb04dd (2026-09-20 20:28 UTC): 44 files changed, 103 insertions, 102 deletions; integrity.yml canon list 63 -> 71; 3 of 44 files add no line with 'allications' or 'controlled'
        - 7lm commit e8a5a2c (record text of section 37, separate commit)
        - 7lm@origin/main:.github/workflows/integrity.yml:47-59 (71 canonical positions; file last changed in bbb04dd)
        - 7lm: git diff -M --name-status bbb04dd origin/main (only non-M change: A L8/L6/in/7lm-layer-lists.md)
        - 7lm@origin/main ls-tree: 94 sheets; only live non-canonical sheeted directory is L8/L6/in
        - autonomous@origin/main (c9076c3) ls-tree: 8 canonical positions without a sheet; L7/publications (9 files) and L7/governance/restrictions present; no L8/L6/in; integrity.yml canon list 57
        - auditonomous@origin/main (2165144) ls-tree: 8 canonical positions without a sheet; L7/publications (5 files) and L7/governance/restrictions present; no L8/L6/in; integrity.yml canon list 57
        - autonomous@origin/beta/7lm-exemplar-autonomous (e64b382): L7/allications with six children and L7/governance/controlled present; no canonical position missing; canon list 71
        - auditonomous@origin/beta/7lm-exemplar-auditonomous (714480d): L7/allications with six children and L7/governance/controlled present; no canonical position missing; canon list 71
        - auditonomous@origin/claude/book-structure-roadmap-k8ap82 (9259c18): former L7 names, canon list 57
    - item 2
      - **claim**: Main and the beta candidate have the same directory tree (97 directories each) and the same list of 71 canonical positions. The beta is two commits by EDM on 2e5a6d6 (4ca3edb of 2 November 2026, 97314c5 of 3 November 2026): it modifies 24 files and adds 8, and moves, renames or deletes nothing. It changes words (six passages of the specification, guidance sections in 18 sheets), it changes the check (USO/ and lowercase layer names dropped, L8/ required, .gitignore still admitted), and it files eight probe files and two source-ledger rows. It merges into main without conflict.
      - **id**: K04
      - **verdict**: corrected
      - **reasoning**: Most of K04 is confirmed from the git objects; two parts are imprecise, so the verdict is "corrected".

        **Confirmed**
        - **Directory tree.** `git ls-tree -r -d --name-only` gives 97 lines for origin/main (c9dc061), 97 for origin/beta/common-contracts-r1-r6 (97314c5) and 97 for 2e5a6d6; the main-versus-beta diff is empty.
        - **71 positions.** The canon list in the beta check (7lm@origin/beta/common-contracts-r1-r6:.github/workflows/integrity.yml:45-57) has 71 unique entries. Main's check is byte-identical to 2e5a6d6 and writes the interior entries as `$top/${lower}N`; expanded for an L8 tree it gives the same 71. All 71 have a 0.md on both refs.
        - **Commits.** `git log 2e5a6d6..beta` shows exactly two commits, author and committer EDM: 4ca3edb (2026-11-02T20:53:22-08:00, parent 2e5a6d6) and 97314c5 (2026-11-03T08:58:01-08:00, parent 4ca3edb). The merge-base with main is 2e5a6d6.
        - **File counts.** `git diff --name-status 2e5a6d6 beta` shows 8 A and 24 M, the same with `-M`; there are no D or R entries and no mode changes.
        - **Specification.** The diff of 7lm-harmonized-architecture-specification.md has six hunks (at lines 18, 65, 184, 352, 595, 680): five rewritten passages and one added Clarification.
        - **Check.** Line 23 reads `README.md|L7|L8|.github|.gitignore` (USO removed, .gitignore kept) and line 27 adds `grep -qx 'L8' || { echo "missing L8/"`. The lowercase handling is removed at lines 32, 36, 39, 50-57 and 63-65.
        - **Source ledger.** Two rows are added, NU-17271561 and SM-PDF (source-ledger.md, +2/-0).
        - **History quote.** 7lm@origin/beta/common-contracts-r1-r6:L8/L6/history/specification-history.md:106 says: "The existing integrity workflow now requires L8 and uppercase L0–L6; its 71-position list is unchanged."
        - **Merge.** `git merge-tree --write-tree origin/main origin/beta/common-contracts-r1-r6` exits 0 with tree 633c343f88378e80d75bc2fe7505e743c192dbad (same in the reverse order; the merged tree has 97 directories). Main's only change since 2e5a6d6 is one added file, L8/L6/in/7lm-layer-lists.md, so no file is changed on both sides.

        **Imprecise**
        1. **"guidance sections in 18 sheets".** Eighteen 0.md sheets are modified, all by 97314c5, but only 11 gain a new headed section:
           - Six carry "## Using this position in a research project" at line 8: L8/L1, L2, L3, L4, L5 and L6/0.md.
           - Five carry other headings: L7/0.md:8 "## Projects across a research network"; L7/peering/0.md:16 "## Shared setup without shared ownership"; L8/0.md:14 "## Shared housing and local research choices"; L8/L0/0.md:10 "## Local choices at this position"; L8/L4/work/writing/0.md:12 "## Manuscript work".
           - The other seven are reworded in line with no new section: L7/governance/controlled, L7/governance/licensing, L7/peering/private/ingress, L7/provenance/sources, L8/L0/semantics/definitions, L8/L5/research/lanes, L8/L5/research/review.
           - Three of the 18 (L7/peering/0.md, L7/provenance/sources/0.md, L8/L0/0.md) were also edited in 4ca3edb, which among other things retitled the sources sheet's archive section "## Program context: the designated curated-source archive".
        2. **The list of what changed is incomplete.** It accounts for 21 of the 24 modified files. The other three are:
           - L8/L6/7lm-field-guide.md: three passages (+3/-3).
           - L8/L6/history/specification-history.md: two new entries (+10).
           - The binary 7lm-harmonized-architecture-specification.docx: blob 9659d08 becomes 8ae7af7.

        **Minor**
        - The locator integrity.yml:19-27 covers only G-002 (USO dropped, L8 required, .gitignore admitted); the dropping of lowercase layer names is at lines 32-65.
        - ".gitignore still admitted" is true of the check, but neither tree has one: the root of both refs is `.github L7 L8 README.md`.
        - The eight added files are four probe documents at L0-L3, three L4 computation files and one L5 findings document; calling them all "probe files" is loose but not wrong.
      - **corrected_statement**: 7lm origin/main (c9dc061) and origin/beta/common-contracts-r1-r6 (97314c5) have the same directory tree (97 directories each, as does 2e5a6d6) and the same list of 71 canonical positions. Main's check, byte-identical to 2e5a6d6, writes the interior entries as $top/${lower}N, which expands to the beta's literal L8/L0-L6 list on an L8 tree; all 71 are sheeted on both refs. The beta is two commits, author and committer EDM, on 2e5a6d6: 4ca3edb (2026-11-02 20:53 -08:00; 8 added, 9 modified) and 97314c5 (2026-11-03 08:58 -08:00; 18 modified). Together they modify 24 files and add 8, and move, rename or delete nothing. The beta changes words: six passages of the specification .md (five rewritten, one Clarification added) with its .docx regenerated; three passages of L8/L6/7lm-field-guide.md; two new entries in L8/L6/history/specification-history.md; and 18 sheets. Of the 18 sheets, 11 gain a new headed guidance section (six titled "## Using this position in a research project" at L8/L1-L6/0.md; five otherwise titled at L7/0.md, L7/peering/0.md, L8/0.md, L8/L0/0.md, L8/L4/work/writing/0.md), and 7 are reworded in line with no new section (L7/governance/controlled, L7/governance/licensing, L7/peering/private/ingress, L7/provenance/sources, L8/L0/semantics/definitions, L8/L5/research/lanes, L8/L5/research/review); three of the 18 were also edited in 4ca3edb. It changes the check (integrity.yml:19-27 drops USO/ from the root and requires L8/, with .gitignore still admitted although neither tree contains one; lines 32-65 drop the lowercase layer names and fix top=L8). It files eight new files (four probe documents at L0-L3, a probe script, its test and a results JSON at L8/L4/work/computation, one findings document at L5) and two source-ledger rows (NU-17271561, SM-PDF). It merges into main without conflict (merge-tree exit 0, tree 633c343); main's only change since 2e5a6d6 is the added file L8/L6/in/7lm-layer-lists.md, so no file is changed on both sides.
      - **evidence_checked**
        - git -C /home/user/7lm ls-tree -r -d --name-only for origin/main, origin/beta/common-contracts-r1-r6 and 2e5a6d6: 97 lines each; diff main vs beta empty
        - git -C /home/user/7lm log --format='%h|%an|%cn|%ad|%s' 2e5a6d6..origin/beta/common-contracts-r1-r6: 97314c5 EDM 2026-11-03T08:58:01-08:00 'Clarify 7LM research housing in the local guidance sheets'; 4ca3edb EDM 2026-11-02T20:53:22-08:00 'Apply approved R1–R6 and exercise bounded research objects'; parents 97314c5->4ca3edb->2e5a6d6
        - git -C /home/user/7lm diff --name-status 2e5a6d6 origin/beta/common-contracts-r1-r6 (also with -M): 8 A, 24 M, no D/R; --summary shows only 8 'create mode 100644'; --shortstat 32 files, 884 insertions, 47 deletions
        - Per commit: 4ca3edb = 8 A + 9 M; 97314c5 = 18 M (all 0.md sheets)
        - 7lm@origin/beta/common-contracts-r1-r6:.github/workflows/integrity.yml:19-27 (line 23 'case "$e" in README.md|L7|L8|.github|.gitignore) ;;'; line 27 'grep -qx 'L8' || { echo "missing L8/"; fail=1; }') and lines 32, 36, 39, 45-57, 63-65
        - git -C /home/user/7lm diff 2e5a6d6 origin/main -- .github/workflows/integrity.yml: empty (main's check identical to base, still admits USO|L8 and uses ${lower})
        - Canon list extracted from integrity.yml on main (expanded with top=L8, lower=L) and on beta: 71 unique entries each, identical; every entry has a 0.md in ls-tree of both refs; 94 0.md files on each ref
        - 7lm@origin/beta/common-contracts-r1-r6:L8/L6/history/specification-history.md:106 'The existing integrity workflow now requires L8 and uppercase L0–L6; its 71-position list is unchanged.'
        - git -C /home/user/7lm diff 2e5a6d6 beta -- L8/L4/work/writing/7lm-harmonized-architecture-specification.md: 6 hunks (@@ 18, 65, 184, 352, 595, 680), +7/-5
        - git -C /home/user/7lm diff 2e5a6d6 beta -- L8/L6/7lm-field-guide.md (+3/-3, three passages), L8/L6/history/specification-history.md (+10, two new '###' entries), L7/provenance/sources/source-ledger.md (+2 rows NU-17271561, SM-PDF)
        - docx blob: 2e5a6d6 and origin/main 9659d08; beta 8ae7af7
        - git -C /home/user/7lm diff 4ca3edb 97314c5: new '## ' headings added in 11 sheets only (L7/0.md:8, L7/peering/0.md:16, L8/0.md:14, L8/L0/0.md:10, L8/L1-L6/0.md:8, L8/L4/work/writing/0.md:12); 7 sheets changed by in-line rewording only (numstat 2/1, 4/4, 4/2, 2/2, 1/1, 1/1, 1/1); none of these headings exist at 2e5a6d6
        - git -C /home/user/7lm diff 4ca3edb^ 4ca3edb -- '*0.md': L7/peering/0.md 1/1, L7/provenance/sources/0.md 7/3, L8/L0/0.md 1/1
        - git -C /home/user/7lm merge-tree --write-tree origin/main origin/beta/common-contracts-r1-r6: exit 0, tree 633c343f88378e80d75bc2fe7505e743c192dbad (same reversed); merged tree has 97 directories
        - git -C /home/user/7lm diff --name-status 2e5a6d6 origin/main: single entry 'A L8/L6/in/7lm-layer-lists.md'; no overlap with the beta's 32 changed paths
        - git -C /home/user/7lm ls-tree --name-only on origin/main and beta root: '.github L7 L8 README.md' (no .gitignore in either tree)
        - Heads of the five added .md files and names of the three added computation files on beta (L8/L0/semantics/beta-research-scope.md, L8/L1/state-space/beta-research-admissibility.md, L8/L2/formal-mathematics/proofs/beta-research-boundaries.md, L8/L3/engineering-mathematics/approximation/beta-exact-reference-method.md, L8/L4/work/computation/{beta-boundary-results.json,beta_boundary_probes.py,test_beta_boundary_probes.py}, L8/L5/research/findings/beta-research-boundary-findings.md)
    - item 3
      - **claim**: The beta's own record does not claim a release, and it asserts the owner's approval of R1 to R6 without quoting the owner. No document on any branch of the three repositories lists R1 to R6 one by one; the six-way reading given in the report is inference from the record's sentence and the diff. Git names EDM as author and committer of every beta commit; 'Codex' appears in one sentence of the beta's specification-history.md.
      - **id**: K05
      - **verdict**: corrected
      - **reasoning**: Every substantive part of the claim is confirmed from git objects, but two points are imprecise as worded, so the verdict is "corrected" rather than "stands".

        **Confirmed**

        1. No release claim. 7lm@origin/beta/common-contracts-r1-r6:L8/L6/history/specification-history.md:106 says "This records the checked common-architecture candidate, not a full-beta or release claim". Line 108 adds "No N/U or NCF theory, machine metadata engine, ACL, rail directory, private peer source, release or sibling repository is changed". The 97314c5 commit message says "not an executable or exemplar implementation, migration, merge, release or beta-readiness claim".

        2. Approval asserted, owner not quoted. The heading at line 104 is "### Owner-approved common architecture corrections of 2 November 2026". Line 106 reads "Implemented by Codex, task T1, on 2 November 2026 (America/Los_Angeles), in the bounded common-architecture candidate after the owner's approval of R1–R6." Line 112 reads "Following approval of the common correction and exemplar construction package". Lines 104-112 contain no quotation of the owner. The added lines of the whole diff 2e5a6d6..beta (excluding docx/pdf) contain no owner statement of approval either. The beta does not touch harmonization-2026-09-04.md.

        3. No enumeration of the 2 November R1–R6. I grepped every ref of all three repos (10 refs in 7lm, 15 in autonomous, 15 in auditonomous) for R1–R6 ranges and bare R-tokens. The only content hit for this correction set is specification-history.md:106 on the 7lm beta. The exemplar beta diffs add no R-numbered lines; the only R-token they add is the unrelated "IL-001-R2".

        4. The six-way reading is inference. The sentence at line 106 names seven things in five semicolon clauses: peer-authorship instruction; manual metadata status; non-exhaustive L0 foundations; model-attached vertical inquiries; scale placement; external semantic examples; byte analogy. The record does not map them to six numbers.

        5. Authorship. All five beta commits have author and committer "EDM <149889949+abba-01@users.noreply.github.com>": 7lm 4ca3edb and 97314c5, autonomous 805cd42 and e64b382, auditonomous 714480d.

        6. "Codex". A case-insensitive grep of all refs of all three repos returns exactly one line, specification-history.md:106 on the 7lm beta. It is in no commit message, and not in the beta's specification .md or .docx.

        **Imprecise**

        A. "No document on any branch … lists R1 to R6 one by one" is false if read literally. Unrelated R-series are listed one by one elsewhere:
        - autonomous@origin/main:L8/L5/research/review/EBIOS_RECODE_single_object.md has headings "## R1 — FIX THE SCHEMA FIRST…" through "## R7 — SEPARATE SPECIFICATION FROM MANIFESTO" at lines 15, 70, 97, 121, 142, 161, 185. It is dated 2026-08-04 and is the same blob (3f970bd) on the autonomous beta.
        - autonomous@origin/main:L8/L5/research/review/AUDIT_L1_QUOTE_FIDELITY.md:189-194 has table rows R1 to R6.
        - 7lm, every ref: L7/provenance/prior-art/uha-ommp-exemplar.html:494 says "its own rulings R1&ndash;R6" (the file names only R1, R1a and R6).
        None of these is the 2 November correction set, so the sentence must be scoped to that set.

        B. The cited evidence misplaces the second occurrence of "R1–R6". The 97314c5 message does not contain it. It is in the subject of the other beta commit, 4ca3edb: "Apply approved R1–R6 and exercise bounded research objects". It is also in the branch name beta/common-contracts-r1-r6. The reader's grep pattern 'R1[–-]R6' also cannot match the HTML-entity form "R1&ndash;R6" in uha-ommp-exemplar.html.
      - **corrected_statement**: The 7lm beta's own record does not claim a release (7lm@origin/beta/common-contracts-r1-r6:L8/L6/history/specification-history.md:106 "not a full-beta or release claim"; :108 "No ... release or sibling repository is changed"; commit 97314c5 message "not an executable or exemplar implementation, migration, merge, release or beta-readiness claim"). It asserts the owner's approval of R1–R6 without quoting the owner, in three places: the heading at specification-history.md:104 ("Owner-approved common architecture corrections of 2 November 2026"), the sentence at :106 ("after the owner's approval of R1–R6"), and the subject of commit 4ca3edb ("Apply approved R1–R6 and exercise bounded research objects"). The label also appears in the branch name. It does not appear in the 97314c5 message. No document on any ref of the three repositories lists the 2 November 2026 corrections R1 to R6 one by one. The only description is the single sentence at :106, which names seven items in five semicolon clauses, so any six-way reading is inference from that sentence and the diff. Unrelated R-numbered series do exist and must not be mistaken for it: autonomous@origin/main (and its beta, same blob) L8/L5/research/review/EBIOS_RECODE_single_object.md:15-185 lists eBIOS recode items R1 to R7 (dated 2026-08-04); AUDIT_L1_QUOTE_FIDELITY.md:189-194 has rows R1 to R6; and 7lm L7/provenance/prior-art/uha-ommp-exemplar.html:494 on every 7lm ref says "its own rulings R1&ndash;R6". Git names EDM <149889949+abba-01@users.noreply.github.com> as both author and committer of every beta commit: 7lm 4ca3edb and 97314c5, autonomous 805cd42 and e64b382, auditonomous 714480d. "Codex" appears in exactly one line across all refs of all three repositories, specification-history.md:106 on the 7lm beta ("Implemented by Codex, task T1, on 2 November 2026"), and in no commit message.
      - **evidence_checked**
        - 7lm@origin/beta/common-contracts-r1-r6:L8/L6/history/specification-history.md:104 heading 'Owner-approved common architecture corrections of 2 November 2026'
        - 7lm@origin/beta/common-contracts-r1-r6:L8/L6/history/specification-history.md:106 'Implemented by Codex, task T1 ... after the owner's approval of R1–R6' and 'not a full-beta or release claim'
        - 7lm@origin/beta/common-contracts-r1-r6:L8/L6/history/specification-history.md:108 'No N/U or NCF theory ... release or sibling repository is changed by this correction set'
        - 7lm@origin/beta/common-contracts-r1-r6:L8/L6/history/specification-history.md:112 'Following approval of the common correction and exemplar construction package'
        - 7lm commit 97314c5 message: 'not an executable or exemplar implementation, migration, merge, release or beta-readiness claim' (contains no 'R1–R6')
        - 7lm commit 4ca3edb subject: 'Apply approved R1–R6 and exercise bounded research objects'
        - git -C /home/user/7lm log 2e5a6d6..origin/beta/common-contracts-r1-r6: two commits (4ca3edb, 97314c5), author and committer both EDM <149889949+abba-01@users.noreply.github.com>
        - git -C /home/user/autonomous log origin/main..origin/beta/7lm-exemplar-autonomous: 805cd42, e64b382, author and committer EDM
        - git -C /home/user/auditonomous log origin/main..origin/beta/7lm-exemplar-auditonomous: 714480d, author and committer EDM
        - git grep -I -i 'codex' on every ref of 7lm (10), autonomous (15), auditonomous (15): single hit, 7lm beta specification-history.md:106
        - git log --all on the three repos, messages grepped for 'codex': no hit
        - git grep -E 'R1 ?(–|-|—|&ndash;|to|through) ?R6' on every ref of the three repos: specification-history.md:106 (7lm beta only) and L7/provenance/prior-art/uha-ommp-exemplar.html:494 'its own rulings R1&ndash;R6' (every 7lm ref, blob 5f5cdbb unchanged by the beta)
        - git diff 2e5a6d6 origin/beta/common-contracts-r1-r6 (32 files, harmonization-2026-09-04.md untouched): added lines grepped for approv/owner/R[1-6]/T1; no owner quotation and no enumeration
        - git diff origin/main..beta in both exemplars: added lines contain no 'codex' and no R1–R6; only R-token added is 'IL-001-R2'
        - autonomous@origin/main:L8/L5/research/review/EBIOS_RECODE_single_object.md:15,70,97,121,142,161,185 headings '## R1' to '## R7' (unrelated series; same blob 3f970bd on the autonomous beta)
        - autonomous@origin/main:L8/L5/research/review/AUDIT_L1_QUOTE_FIDELITY.md:189-194 table rows R1 to R6 (unrelated series)
        - autonomous@origin/beta/7lm-exemplar-autonomous:L8/L6/history/BETA_HISTORY.md:10,14 pins 4ca3edb on beta/common-contracts-r1-r6; 'No merge or release occurred.'
        - auditonomous@origin/beta/7lm-exemplar-auditonomous:L8/L6/history/AUDITONOMOUS_BETA_HISTORY.md:3 'the authorized local candidate, not a new source-owner decision or release'
        - 7lm beta specification .md and .docx (docx unzipped in scratchpad): no 'Codex', no 'R1–R6'
    - item 4
      - **claim**: Each exemplar's main lacks exactly the same eight canonical positions: L7/governance/controlled, L7/allications, and L7/allications/publications, applications, communications, specifications, notifications and participations. Each still holds the two former folders, L7/publications/ (9 files in Autonomous, 5 in Auditonomous) and L7/governance/restrictions/ (1 file). The other 63 positions exist with correct first lines; nothing under L8 is missing or misnamed.
      - **id**: K06
      - **verdict**: corrected
      - **reasoning**: Every count and name in the claim is confirmed from git objects. The one correction is scope: "nothing under L8 is missing or misnamed" holds only for the 36 canonical L8 positions, not for the whole L8 tree.

        **Confirmed**
        - **Canon list:** the scaffold's check lists 71 positions, 35 under L7 and 36 under L8 (7lm@origin/main:.github/workflows/integrity.yml:47-59).
        - **Autonomous (origin/main = c9076c3):** my re-run of the G-003 logic gives 97 sheets checked, 0 wrong headings, 63 canonical positions present, 8 missing.
        - **Auditonomous (origin/main = 2165144):** 78 sheets checked, 0 wrong headings, 63 present, 8 missing.
        - **The eight missing positions** are identical in both: L7/governance/controlled, L7/allications, and L7/allications/{publications, applications, communications, specifications, notifications, participations}.
        - **Former folders still present:** L7/publications/ holds 9 files in Autonomous and 5 in Auditonomous; L7/governance/restrictions/ holds 1 file (0.md) in each. Their sheets are headed "# L7/publications/" and "# L7/governance/restrictions/".
        - **The other 63 positions** each have a 0.md whose first line is exactly "# <path>/"; all 36 L8 positions are among them, and L8 holds L0 to L6 with the right case.
        - **Control:** the same simulation on 7lm@origin/main gives 75 sheets checked, 0 wrong, 71 of 71 present.

        **Evidence against the unscoped L8 sentence**
        - **L8/L6/in/ exists on the scaffold and in neither exemplar.** It is a sheeted directory (7lm@origin/main:L8/L6/in/0.md:1 "# L8/L6/in/", line 3 "The inbox for L6."), described at 7lm@origin/main:L8/L6/0.md:79 as "`L8/L6/in/` — the inbox". It is not in the 71-position list, and the specification file has no "L6/in" hit, so it is not a canonical position.
        - **Autonomous holds a directory spelled "autonomouos"** at L8/L5/research/review/autonomous-theory/autonomouos/. It is unsheeted filed material beneath a canonical position, not a canonical position.
        - **The scaffold's three retired sets** (L8/L6/retired/scaffold-2026-08-20, specification-2026-09-04, specification-draft-2026-09-03) are absent from the exemplars, which hold their own retired sets instead. This is expected.

        **Context the claim omits**
        The eight positions are missing only against the scaffold's check. Each exemplar's own integrity.yml on origin/main still carries the older list: it names L7/governance/restrictions and L7/publications, and has no allications line and no peer-1/object-1 line. That is 57 positions, so each exemplar's own check does not flag these. The eight peer-1 and object-1 positions nonetheless exist in both exemplar trees.
      - **corrected_statement**: Measured against the 71 canonical positions listed in the scaffold's check (7lm@origin/main:.github/workflows/integrity.yml:47-59), each exemplar's origin/main (autonomous c9076c3, auditonomous 2165144) lacks exactly the same eight: L7/governance/controlled, L7/allications, and L7/allications/{publications, applications, communications, specifications, notifications, participations}. Each still holds the two former folders, L7/publications/ (9 files in Autonomous, 5 in Auditonomous) and L7/governance/restrictions/ (1 file, 0.md). The other 63 canonical positions (27 under L7, all 36 under L8) exist with correct first lines, and no sheet in either exemplar has a wrong heading (97 sheets in Autonomous, 78 in Auditonomous). No CANONICAL position under L8 is missing or misnamed. Outside the canon list, the scaffold's sheeted L6 inbox L8/L6/in/ (7lm@origin/main:L8/L6/0.md:79) exists in neither exemplar, and Autonomous carries an unsheeted filed directory spelled L8/L5/research/review/autonomous-theory/autonomouos/. Each exemplar's own integrity.yml still lists the former names (L7/governance/restrictions, L7/publications; 57 positions), so the eight are missing only against the scaffold's check, not the exemplar's own.
      - **evidence_checked**
        - 7lm@origin/main:.github/workflows/integrity.yml:31-61 (G-003 step; canon list lines 47-59 counted = 71: 35 L7 + 36 L8)
        - Simulation of G-003 from git objects (ls-tree -r + show | head -n 1): 7lm@origin/main control = 75 sheets checked, 19 retired skipped, 0 wrong, 71/71 present
        - autonomous@origin/main (c9076c3): 97 sheets checked, 0 skipped, 0 wrong headings, 63 present, 8 missing (L7/governance/controlled, L7/allications and its six children)
        - auditonomous@origin/main (2165144): 78 sheets checked, 0 skipped, 0 wrong headings, 63 present, 8 missing (same eight)
        - git ls-tree -d --name-only origin/main L7/ L7/governance/ in both exemplars: L7/governance/restrictions present, no controlled, no L7/allications; L7/publications/binder present
        - autonomous@origin/main ls-tree -r L7/publications = 9 files (0.md, binder/0.md, binder/README.md, binder/internal/FETCH_LIST.md, binder/internal/README.md, binder/internal/tools/verify_fragments.py, binder/internal/tools/verify_fragments_v2.py, binder/press-kit/GLOSSARY_AUTONOMOUS.md, binder/press-kit/README.md); L7/governance/restrictions = 1 file (0.md)
        - auditonomous@origin/main ls-tree -r L7/publications = 5 files (0.md, binder/0.md, binder/README.md, binder/internal/README.md, binder/press-kit/README.md); L7/governance/restrictions = 1 file (0.md)
        - First lines: autonomous and auditonomous @origin/main:L7/publications/0.md:1 '# L7/publications/'; L7/governance/restrictions/0.md:1 '# L7/governance/restrictions/'
        - git ls-tree -d --name-only origin/main L8/ in both exemplars: L8/L0 through L8/L6, correct case; root = .github .gitignore L7 L8 README.md
        - Directory-tree comparison (ls-tree -r -d) scaffold vs exemplars: scaffold dirs absent from both = the 8 L7 positions, L8/L6/in, and three scaffold retired sets
        - 7lm@origin/main:L8/L6/in/0.md:1,3 ('# L8/L6/in/', 'The inbox for L6.'); 7lm@origin/main:L8/L6/0.md:79; git grep -F 'L6/in' in the specification file: no hit
        - autonomous@origin/main ls-tree -d: L8/L5/research/review/autonomous-theory/autonomouos (no 0.md)
        - diff of 7lm@origin/main:.github/workflows/integrity.yml against autonomous@origin/main and auditonomous@origin/main copies: exemplar canon lists L7/governance/restrictions and L7/publications, with no allications line and no peer-1/object-1 line
        - No paths with whitespace in any of the three trees (word-splitting in the check's for-loop does not affect the result)
    - item 5
      - **claim**: Autonomous main (c9076c3), live text: 'L7/publications' on 29 lines in 23 files; 'governance/restrictions' on 16 lines in 13 files; 'peering, and publication state' 56 times in 55 sheets; 'the L7 publications branch' 8 times; 'access, restrictions' 8; 'access, and restrictions' 2; 'peering, and publications become addressable' 2; 'publications and release identity' 2; the former canonical-branches sentence 2; 'licensing and restrictions folders' 0. Its check lists 57 positions, its README line 9 names the fourth branch 'publications', six folders have no sheet, and its record ends at section 13, the rename pass of 12 September 2026.
      - **id**: K07
      - **verdict**: corrected
      - **reasoning**: Every figure in the claim reproduces from git objects at autonomous@origin/main (c9076c3). Only one clause is imprecise as written: "six folders have no sheet" is true only within the scope of the check's own report step, not of the whole tree. The verdict is "corrected" for that scope qualifier alone.

        **Phrase counts** (live text, with L8/L6/history and L8/L6/retired excluded; L8/L6/in does not exist in this repo, so that exclusion does nothing):

        | Phrase | Occurrences | Lines | Files |
        |---|---|---|---|
        | `L7/publications` | 29 | 29 | 23 (22 sheets plus `.github/workflows/integrity.yml`) |
        | `governance/restrictions` | 16 | 16 | 13 (12 sheets plus `integrity.yml`) |
        | `peering, and publication state` | 56 | 56 | 55, all `0.md`; `L7/0.md` carries it twice |
        | `the L7 publications branch` | 8 | 7 | 5 |
        | `access, restrictions` | 8 | 8 | 8 |
        | `access, and restrictions` | 2 | 2 | 2 |
        | `peering, and publications become addressable` | 2 | 2 | 1 |
        | `publications and release identity` | 2 | 2 | 2 |
        | `licensing and restrictions folders` | 0 | 0 | 0 |

        - **Former canonical-branches sentence:** 2 occurrences, at autonomous@origin/main:L7/0.md:14 and L7/peering/0.md:8: "Canonical direct L7 branches are L7/provenance/, L7/governance/, L7/peering/, and L7/publications/."
        - **Check:** the canon list at integrity.yml:75-86 holds exactly 57 positions. Line 76 ends "L7/governance/restrictions" and line 78 is "L7/publications".
        - **README:** line 9 reads "`L7/0.md` — the desk, the forward face: provenance, governance (copyright has one place, `L7/governance/copyright/`), peering, publications."
        - **Record:** the last heading of harmonization-2026-09-05.md is at line 169 of 181: "## 13. 2026-09-12 — the rename pass: `USO/` to `L8/`, `l0` … `l6` to `L0` … `L6`".
        - **Scaffold record:** 7lm@origin/main (c9dc061):L8/L6/history/harmonization-2026-09-04.md:329 says "name the former paths in 24 and 21 files respectively, with `governance/restrictions` in 12 and 13". Counting the whole autonomous tree without `.github` gives 24 files for `L7/publications` (22 live sheets plus two L8/L6/history files) and 12 for `governance/restrictions`, as the claim states.

        **The imprecision:** 21 directories in the tree have no `0.md`. Six are under L7/ and L8/ outside the retired sets, which is the scope the check's report step uses (integrity.yml:90-96). The other 15 sit beneath the two retired layout sets, and 2 are `.github` and `.github/workflows`.

        No evidence against any other part was found.
      - **corrected_statement**: Autonomous main (c9076c3), live text (L8/L6/history and L8/L6/retired excluded; L8/L6/in does not exist in this repository): 'L7/publications' on 29 lines in 23 files (22 sheets plus .github/workflows/integrity.yml); 'governance/restrictions' on 16 lines in 13 files (12 sheets plus integrity.yml); 'peering, and publication state' 56 times in 55 sheets (twice in L7/0.md); 'the L7 publications branch' 8 times (on 7 lines in 5 sheets); 'access, restrictions' 8; 'access, and restrictions' 2; 'peering, and publications become addressable' 2 (one file); 'publications and release identity' 2; the former canonical-branches sentence 2 (L7/0.md:14, L7/peering/0.md:8); 'licensing and restrictions folders' 0. Its check lists 57 canonical positions (integrity.yml:75-86, with L7/governance/restrictions on line 76 and L7/publications on line 78), and its README line 9 names the fourth branch 'publications'. Six folders under L7/ and L8/ outside the retired sets have no sheet: L7/publications/binder/internal, L7/publications/binder/internal/tools, L7/publications/binder/press-kit, L8/L5/research/review/autonomous-theory, and its subfolders audit-anon and autonomouos. In the whole tree 21 directories lack a 0.md; the other 15 lie beneath L8/L6/retired/layout-2026-08-14 and layout-2026-09-06, and 2 are .github and .github/workflows. Its record (L8/L6/history/harmonization-2026-09-05.md) ends at section 13, line 169, the rename pass of 12 September 2026. The scaffold record's figures of 24 and 12 files (7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:329) are reproduced by counting the whole autonomous tree without .github.
      - **evidence_checked**
        - autonomous@origin/main resolves to c9076c35f1fd12e10763ec840a0356dbb7e29a42 (merge of PR #28, 2026-09-11 23:25:59 -0700)
        - git -C /home/user/autonomous grep -o/-n/-l -F per phrase on origin/main with ':!L8/L6/history' ':!L8/L6/retired' ':!L8/L6/in': L7/publications 29 occurrences / 29 lines / 23 files; governance/restrictions 16/16/13; 'peering, and publication state' 56/56/55; 'the L7 publications branch' 8/7/5; 'access, restrictions' 8/8/8; 'access, and restrictions' 2/2/2; 'peering, and publications become addressable' 2/2/1; 'publications and release identity' 2/2/2; 'licensing and restrictions folders' 0
        - autonomous@origin/main: all 55 files carrying 'peering, and publication state' are 0.md sheets; only L7/0.md has it twice (git grep -c)
        - autonomous@origin/main:L7/0.md:14 and autonomous@origin/main:L7/peering/0.md:8 - "Canonical direct L7 branches are L7/provenance/, L7/governance/, L7/peering/, and L7/publications/." (2 occurrences)
        - autonomous@origin/main:.github/workflows/integrity.yml:75-86 - canon list counted programmatically = 57 positions; line 76 ends 'L7/governance/access L7/governance/restrictions'; line 78 is 'L7/publications'
        - autonomous@origin/main:.github/workflows/integrity.yml:90-96 - report step scope: directories under L7 and L8, skipping those beneath retired sets
        - autonomous@origin/main:README.md:9 - "`L7/0.md` — the desk, the forward face: provenance, governance (copyright has one place, `L7/governance/copyright/`), peering, publications."
        - autonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:169 - "## 13. 2026-09-12 — the rename pass: `USO/` to `L8/`, `l0` … `l6` to `L0` … `L6`" (last heading; file is 181 lines)
        - git ls-tree -r -d on autonomous@origin/main tested against <dir>/0.md: 21 directories without a sheet = 6 live (L7/publications/binder/internal, .../internal/tools, .../press-kit, L8/L5/research/review/autonomous-theory, .../audit-anon, .../autonomouos) + 15 beneath L8/L6/retired/layout-2026-08-14 and layout-2026-09-06 + .github and .github/workflows
        - git ls-tree -d autonomous@origin/main L8/L6/ shows only history and retired; no L8/L6/in
        - 7lm@origin/main (c9dc061):L8/L6/history/harmonization-2026-09-04.md:329 - "name the former paths in 24 and 21 files respectively, with `governance/restrictions` in 12 and 13"
        - Whole autonomous tree without .github: git grep -l 'L7/publications' = 24 files (the two non-live hits are L8/L6/history/7LM_ROUTING_PLAN_2026-09-05.md and L8/L6/history/harmonization-2026-09-05.md); 'governance/restrictions' = 12 files; including .github the counts are 25 and 13
    - item 6
      - **claim**: Auditonomous main (2165144), live text: 'L7/publications' on 26 lines in 20 files; 'governance/restrictions' on 16 lines in 13 files; 'peering, and publication state' 38 times in 37 sheets; 'the L7 publications branch' 9 times; 'access, restrictions' 8; 'access, and restrictions' 2; 'peering, and publications become addressable' 2; 'publications and release identity' 2; the former canonical-branches sentence 2; 'licensing and restrictions folders' 0. Its check lists 57 positions, its README line 9 names the fourth branch 'publications', twelve folders have no sheet, and its record ends at section 12, the rename pass of 12 September 2026.
      - **id**: K08
      - **verdict**: corrected
      - **reasoning**: Every count in the claim reproduces from git objects at auditonomous@origin/main (rev-parse = 21651446). One part is imprecise: "twelve folders have no sheet" holds only under the check's own reporting rule.

        **Phrase counts** (git grep -n/-l/-o -F on origin/main, excluding L8/L6/history, L8/L6/retired, L8/L6/in):
        - 'L7/publications': 26 lines, 20 files.
        - 'governance/restrictions': 16 lines, 13 files.
        - 'peering, and publication state': 38 occurrences in 37 files, all 0.md sheets; L7/0.md carries two.
        - 'the L7 publications branch': 9 occurrences on 8 lines in 6 files; L7/publications/0.md:10 carries two.
        - 'access, restrictions': 8, all at line 8 of L7/governance sheets except L7/0.md:32.
        - 'access, and restrictions': 2 (L7/peering/0.md:28, L8/L6/0.md:80).
        - 'peering, and publications become addressable': 2 (L7/0.md:6 and :198).
        - 'publications and release identity': 2 (L7/0.md:34, L7/publications/0.md:8).
        - Former canonical-branches sentence: 2 (L7/0.md:14, L7/peering/0.md:8), quoted "Canonical direct L7 branches are L7/provenance/, L7/governance/, L7/peering/, and L7/publications/."
        - 'licensing and restrictions folders': 0.

        **Other parts confirmed:**
        - **Check:** .github/workflows/integrity.yml lines 47-58 list 57 positions; line 48 ends "L7/governance/restrictions" and line 50 is "L7/publications".
        - **README:** line 9 reads "provenance, governance (copyright has one place, `L7/governance/copyright/`), peering, publications."
        - **Record:** the last heading of L8/L6/history/harmonization-2026-09-05.md is line 162, "## 12. 2026-09-12 — the rename pass: `USO/` to `L8/`, `l0` … `l6` to `L0` … `L6`". The file has 174 lines and no later-dated entry was found anywhere under L8/L6/history.
        - **Scaffold figures:** 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:329 says "name the former paths in 24 and 21 files respectively, with `governance/restrictions` in 12 and 13". Counting the whole auditonomous tree without .github gives 21 files for 'L7/publications' and 13 for 'governance/restrictions'.

        **The imprecision:** ls-tree shows 25 directories under L7/ and L8/ with no 0.md. Thirteen of them lie below the roots of retired sets under L8/L6/retired/, which the check skips (integrity.yml:66). The remaining 12 are what the check's report step (lines 62-68) would list.

        **Two clarifications, not errors:**
        - The 26/20 and 16/13 figures each include the one workflow line (integrity.yml:50 and :48). Sheets and README alone give 25 lines in 19 files and 15 lines in 12 files.
        - The L8/L6/in exclusion is vacuous: that path does not exist on auditonomous main. L8/L6/retired has zero hits for both path strings.
      - **corrected_statement**: Auditonomous main (2165144), live text (whole tree except L8/L6/history, L8/L6/retired and L8/L6/in; the one CI workflow is included): 'L7/publications' on 26 lines in 20 files (25 lines in 19 files of sheets and README, plus integrity.yml:50); 'governance/restrictions' on 16 lines in 13 files (15 lines in 12 files, plus integrity.yml:48); 'peering, and publication state' 38 times in 37 sheets (twice in L7/0.md); 'the L7 publications branch' 9 times (on 8 lines in 6 sheets); 'access, restrictions' 8; 'access, and restrictions' 2; 'peering, and publications become addressable' 2; 'publications and release identity' 2; the former canonical-branches sentence 2 (L7/0.md:14, L7/peering/0.md:8); 'licensing and restrictions folders' 0. Its check lists 57 positions (integrity.yml:47-58), and its README line 9 names the fourth branch 'publications'. Twelve folders outside the retired sets have no sheet, counted as the check's own report step counts them: nine under L7/provenance/sources/staging-records/, L7/publications/binder/internal, L7/publications/binder/press-kit, and L8/L5/research/review/autonomous-theory. A further 13 unsheeted directories lie below the roots of retired sets under L8/L6/retired/ and are exempt, so the raw tree total under L7/ and L8/ is 25. Its record, L8/L6/history/harmonization-2026-09-05.md, ends at section 12 (line 162), the rename pass of 12 September 2026. The scaffold record's figures of 21 files and 13 files (7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:329) are reproduced by counting the whole tree, history included, without .github.
      - **evidence_checked**
        - auditonomous@origin/main rev-parse = 21651446b1f3f4547b588e6d7122ef7f9f81e9b9
        - git -C /home/user/auditonomous grep -n/-l/-o -F per phrase on origin/main with ':!L8/L6/history' ':!L8/L6/retired' ':!L8/L6/in': L7/publications 26 lines/20 files; governance/restrictions 16/13; 'peering, and publication state' 38 occ/37 files (all 0.md, L7/0.md has 2); 'the L7 publications branch' 9 occ/8 lines/6 files; 'access, restrictions' 8; 'access, and restrictions' 2; 'peering, and publications become addressable' 2; 'publications and release identity' 2; 'licensing and restrictions folders' 0
        - auditonomous@origin/main:L7/0.md:14 and L7/peering/0.md:8: "Canonical direct L7 branches are L7/provenance/, L7/governance/, L7/peering/, and L7/publications/." (2 occurrences, none elsewhere in the whole tree)
        - auditonomous@origin/main:.github/workflows/integrity.yml:47-58: canon list counted programmatically = 57 positions; line 48 ends 'L7/governance/restrictions'; line 50 = 'L7/publications'
        - auditonomous@origin/main:.github/workflows/integrity.yml:62-68: report step skips '*/L6/retired/*/*'
        - auditonomous@origin/main:README.md:9: "the desk, the forward face: provenance, governance (copyright has one place, `L7/governance/copyright/`), peering, publications."
        - auditonomous@origin/main ls-tree -r -d L7 L8 (103 directories) against ls-tree -r file list: 25 directories without 0.md; 13 below L8/L6/retired/<set>/; 12 outside (9 under L7/provenance/sources/staging-records/, L7/publications/binder/internal, L7/publications/binder/press-kit, L8/L5/research/review/autonomous-theory)
        - auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:162: "## 12. 2026-09-12 — the rename pass: `USO/` to `L8/`, `l0` … `l6` to `L0` … `L6`" (last heading; file is 174 lines; no date after 2026-09-12 found by grep in L8/L6/history)
        - auditonomous@origin/main ls-tree L8/L6/: 0.md, history, retired (no L8/L6/in); L8/L6/retired has 0 hits for 'L7/publications' and 'governance/restrictions'; L8/L6/history has 3 lines/2 files and 4 lines/1 file respectively; .github has 1 line/1 file each
        - Whole tree: 'L7/publications' 29 lines/22 files, without .github 28 lines/21 files; 'governance/restrictions' 20 lines/14 files, without .github 19 lines/13 files
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:329: "name the former paths in 24 and 21 files respectively, with `governance/restrictions` in 12 and 13"
        - auditonomous git log origin/main -3: 2165144 2026-09-11 merge of PR #26; f7d9b57 and 5e18f0a dated 2026-09-12
    - item 7
      - **claim**: Both exemplar beta candidates (autonomous e64b382, auditonomous 714480d, both of 2 November 2026) made the two moves and wrote six sheets, but neither did the prose sweep or changed the README: the boundary sentence remains 56 and 38 times and the scaffold's replacement wording occurs 0 times in either. Both go beyond a physical alignment. Autonomous: about 1,640 of 1,930 added lines are new research objects, two binder files are edited and a REGISTER.md row is removed. Auditonomous: AUDITONOMOUS_DEFINITION.md, Q13 and CONTRADICTIONS.md are edited and eleven research files are added. Both pin scaffold commit 4ca3edb, which is on the unmerged scaffold beta and not on the scaffold's main. Neither records its pass as a numbered section of its repository's record.
      - **id**: K09
      - **verdict**: corrected
      - **reasoning**: Every cited locator checks out, and the core of the claim is confirmed from git objects. Four parts are imprecise or incomplete, so the claim is corrected rather than left standing.

        CONFIRMED
        - Refs and dates: the autonomous beta is two commits on c9076c3 (805cd42 at 2026-11-02 21:03:03 -0800, e64b382 at 21:05:23 -0800); the auditonomous beta is one commit on 2165144 (714480d at 21:08:36 -0800). These are 3 Nov in UTC, and the documents inside date themselves 2026-11-03.
        - Shortstat: `git diff -M --shortstat origin/main <beta>` gives 65 files +1930/-72 (autonomous) and 56 files +2352/-86 (auditonomous).
        - Two moves: both betas rename L7/publications/* to L7/allications/publications/* and L7/governance/restrictions/0.md to L7/governance/controlled/0.md. ls-tree of both betas shows L7/allications/{0.md, applications, communications, notifications, participations, publications, specifications} and L7/governance/controlled, with no L7/publications or governance/restrictions.
        - README unchanged: blob ids are identical between main and beta (autonomous 3b5c731, auditonomous 72da263). README.md:9 in both still reads "provenance, governance (copyright has one place, `L7/governance/copyright/`), peering, publications."
        - Counts: 'peering, and publication state' occurs 56 times (autonomous) and 38 times (auditonomous), all in 0.md sheets under L7, identical to each origin/main. The scaffold replacement 'peering, and allications — the outward acts, of which publication is one' occurs 0 times in both. 'peering, publications.' occurs once in each (README.md:9). The replacement string does exist on 7lm origin/main (40 occurrences).
        - Misquotation: autonomous@origin/beta/7lm-exemplar-autonomous:L7/peering/0.md:8 quotes "Canonical direct L7 branches are L7/provenance/, L7/governance/, L7/peering/, and L7/allications/publications/." The scaffold specification (7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:46) reads "...L7/peering/, and L7/allications/." The auditonomous beta's L7/peering/0.md:8 quotes it correctly.
        - Pins: autonomous binding.json:7 and auditonomous binding.json:7 both read "architecture_commit": "4ca3edb9172c34e6b0033bd09e2379ed3da76d9d"; auditonomous binding.json:5 reads "producer_commit": "805cd42f...". In 7lm, 4ca3edb ("Apply approved R1–R6 and exercise bounded research objects", 2026-11-02 20:53 -0800) is an ancestor of origin/beta/common-contracts-r1-r6, is not an ancestor of origin/main, and `branch -r --contains` lists only that beta. It is the first of the beta's two commits, not its tip (97314c5).
        - Records: L8/L6/history/harmonization-2026-09-05.md has the same blob on main and beta in both repositories (autonomous 47ba4e0, last section "## 13. 2026-09-12 — the rename pass"; auditonomous 9899217, last section "## 12. 2026-09-12 — the rename pass"). The betas instead add L8/L6/history/BETA_HISTORY.md and L8/L6/history/AUDITONOMOUS_BETA_HISTORY.md.
        - Autonomous line count: the 13 added non-sheet files total 1,638 lines (12 under L8 = 1,623, of which autonomous_beta_result.json is 1,002; plus the egress binding.json, 15).
        - Autonomous binder edits: press-kit/GLOSSARY_AUTONOMOUS.md (+2, line 3 "Current bounded-use correction") and press-kit/README.md (+4/-5, "Placement here is not clearance.").
        - Auditonomous: AUDITONOMOUS_DEFINITION.md is +16 (line 20 "**Receiving semantic reference (2026-11-03 correction).**" plus 15 "Current role:" lines); CONTRADICTIONS.md is +15 (line 22 "## Current receiving-use dispositions — 2026-11-03"). Eleven files are added outside L7/allications.

        IMPRECISE OR INCOMPLETE
        1. "wrote six sheets" holds only for the six new allications positions. Autonomous adds 13 new 0.md sheets (97 to 110): the six, plus binder/internal, binder/internal/tools, binder/press-kit, peering/public/egress/peer-1/object-2, and three under L8/L5/research/review/autonomous-theory/. Auditonomous adds 7 (78 to 85): the six plus peering/public/ingress/peer-1/object-2.
        2. "neither did the prose sweep" is true of the scaffold's scripted phrases. Besides the boundary sentence, 'the L7 publications branch' (8 and 9), 'publications and release identity' (2 and 2), 'peering, and publications become addressable' (2 and 2) and 'access, and restrictions' (2 and 2) are unchanged from main. What both betas did is a path sweep ('L7/publications' 31 to 4 and 29 to 3; 'governance/restrictions' 16 to 1 and 20 to 4) plus a few ad hoc rewordings. Autonomous changed 'access, restrictions' to 'access, controlled' in 2 of 8 places (L7/0.md:32, L7/governance/0.md:8). Auditonomous L7/0.md:135 has its own wording: "The Surface is organized around four direct branches: provenance, governance, peering, and allications."
        3. "a REGISTER.md row is removed" understates the change. In autonomous L8/L0/semantics/definitions/REGISTER.md the "autonomy / autonomous" row is removed from the "Not yet entered — and why" table (main line 19) and a new "autonomy / autonomous" row is added to the entered table (beta line 12: "[source text withheld from the public copy]"). Line 6 is also edited. The term is re-statused from blocked to adopted. L8/L0/semantics/definitions/DEFINITION_LIST_AUTONOMOUS.md is also edited (+2), which the claim does not mention.
        4. Auditonomous: "Q13" is an insertion in L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:268 ("**[source text withheld from the public copy]).**"). The claim omits a fourth edited research/provenance file, L7/provenance/sources/LEDGER.md (+8, line 147 "## Attributable receiving correction — 2026-11-03", adding source row AUT-SOURCE-001 and a 21-not-22 arithmetic correction). The "eleven research files" are nine under L8 plus the L7 peering object-2 sheet and binding.json; together they are 2,154 of the 2,352 added lines.

        Not checked: the "three exclusions" named in the cited grep are not specified. My whole-tree counts match 56 and 38, and excluding L8/L6/history, L8/L6/retired and L8/L6/in does not change them.
      - **corrected_statement**: Both exemplar beta candidates (autonomous origin/beta/7lm-exemplar-autonomous = e64b382, two commits 805cd42 and e64b382; auditonomous origin/beta/7lm-exemplar-auditonomous = 714480d, one commit; all committed 2026-11-02 21:03-21:08 -0800, i.e. 3 Nov UTC) made the two moves (L7/publications/ to L7/allications/publications/, L7/governance/restrictions/ to L7/governance/controlled/) and wrote the six new allications sheets (allications/0.md and the five siblings). In total autonomous adds 13 new sheets (the six, three binder sub-directory sheets, the egress object-2 sheet, and three under L8/L5/research/review/autonomous-theory/) and auditonomous adds 7 (the six plus the ingress object-2 sheet). Both swept the paths but not the words, and neither changed README.md (identical blobs; line 9 still reads "peering, publications."). The boundary sentence 'peering, and publication state' remains 56 and 38 times, exactly as on each main, and the scaffold's replacement wording occurs 0 times in either. The only prose touched is ad hoc: autonomous changed 'access, restrictions' to 'access, controlled' in 2 of 8 places (L7/0.md:32, L7/governance/0.md:8) and misquotes the specification at L7/peering/0.md:8 ("...and L7/allications/publications/." where the scaffold reads "...and L7/allications/."); auditonomous L7/0.md:135 uses its own wording ("provenance, governance, peering, and allications"). Both go beyond a physical alignment. Autonomous: 1,638 of 1,930 added lines are 13 new non-sheet research objects (12 under L8, 1,623 lines, plus the egress binding.json); two binder files are edited (press-kit/GLOSSARY_AUTONOMOUS.md, press-kit/README.md); DEFINITION_LIST_AUTONOMOUS.md is edited; and in REGISTER.md the "autonomy / autonomous" row is removed from the "Not yet entered — and why" table and a new row for the same term is added to the entered table as "ADOPTED **as a plural entry**", which is a status change and not a bare removal. Auditonomous: AUDITONOMOUS_DEFINITION.md (+16), the Q13 disposition in L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:268 (+2), CONTRADICTIONS.md (+15) and L7/provenance/sources/LEDGER.md (+8, adding source row AUT-SOURCE-001 and an arithmetic correction) are edited, and eleven files are added outside L7/allications (nine research files under L8 plus the L7 ingress object-2 sheet and binding.json; 2,154 of 2,352 added lines). Both pin scaffold commit 4ca3edb9172c34e6b0033bd09e2379ed3da76d9d (binding.json:7 in each), which is the first of the two commits on the unmerged scaffold branch origin/beta/common-contracts-r1-r6 (tip 97314c5) and is not on the scaffold's main. Neither records its pass as a numbered section of its repository's record: L8/L6/history/harmonization-2026-09-05.md is byte-identical to main in both (last sections 13 and 12, the 2026-09-12 rename pass). Each instead adds a separate file, L8/L6/history/BETA_HISTORY.md and L8/L6/history/AUDITONOMOUS_BETA_HISTORY.md.
      - **evidence_checked**
        - autonomous: git log origin/beta/7lm-exemplar-autonomous (805cd42 2026-11-02 21:03:03 -0800, e64b382 21:05:23 -0800; merge-base with origin/main = c9076c3)
        - auditonomous: git log origin/beta/7lm-exemplar-auditonomous (714480d 2026-11-02 21:08:36 -0800; merge-base with origin/main = 2165144)
        - git diff -M --shortstat origin/main <beta>: autonomous 65 files +1930/-72; auditonomous 56 files +2352/-86; full --name-status and --numstat read for both
        - git grep -o -F 'peering, and publication state': autonomous main 56 / beta 56 (55 files, all 0.md under L7); auditonomous main 38 / beta 38 (37 files); unchanged when L8/L6/history, retired and in are excluded
        - git grep -o -F 'peering, and allications — the outward acts, of which publication is one': 0 in both betas; 40 on 7lm@origin/main
        - git grep -F 'peering, publications.': autonomous@beta:README.md:9 and auditonomous@beta:README.md:9 only; README.md blob ids identical main vs beta (3b5c731; 72da263)
        - Other sweep phrases main vs beta: 'the L7 publications branch' 8/8 and 9/9; 'publications and release identity' 2/2 and 2/2; 'access, restrictions' 8 to 6 (autonomous) and 8/8 (auditonomous); 'L7/publications' 31 to 4 and 29 to 3; 'governance/restrictions' 16 to 1 and 20 to 4
        - autonomous@origin/beta/7lm-exemplar-autonomous:L7/peering/0.md:8 quotes "...L7/peering/, and L7/allications/publications/." versus 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:46 "...L7/peering/, and L7/allications/."; auditonomous@beta:L7/peering/0.md:8 quotes it correctly
        - autonomous@beta:L7/0.md:32 and L7/governance/0.md:8 ('access, controlled'); auditonomous@beta:L7/0.md:135 ("four direct branches: provenance, governance, peering, and allications")
        - autonomous@origin/beta/7lm-exemplar-autonomous:L7/peering/public/egress/peer-1/object-2/binding.json:7 "architecture_commit": "4ca3edb9172c34e6b0033bd09e2379ed3da76d9d"; line 8 producer_commit 805cd42
        - auditonomous@origin/beta/7lm-exemplar-auditonomous:L7/peering/public/ingress/peer-1/object-2/binding.json:5 (producer_commit 805cd42...) and :7 (architecture_commit 4ca3edb...)
        - 7lm: git merge-base --is-ancestor 4ca3edb origin/beta/common-contracts-r1-r6 = yes; against origin/main = no; git branch -r --contains 4ca3edb = origin/beta/common-contracts-r1-r6 only; main..beta log = 4ca3edb then 97314c5
        - autonomous: diff of L8/L0/semantics/definitions/REGISTER.md (row removed at main line 19 under '## Not yet entered — and why'; row added at beta line 12; line 6 edited) and DEFINITION_LIST_AUTONOMOUS.md:3
        - autonomous: diff of L7/allications/publications/binder/press-kit/GLOSSARY_AUTONOMOUS.md (+2, line 3) and press-kit/README.md (+4/-5, line 5 'Placement here is not clearance.')
        - autonomous numstat: 13 added non-sheet files = 1,638 lines (12 under L8 = 1,623; autonomous_beta_result.json 1,002; binding.json 15); 13 added 0.md sheets; sheet count 97 on main, 110 on beta
        - auditonomous@beta:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:20 '**Receiving semantic reference (2026-11-03 correction).**' (+16 total)
        - auditonomous@beta:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:268 '**[source text withheld from the public copy]).**' (+2)
        - auditonomous@beta:L8/L5/research/review/CONTRADICTIONS.md:22 '## Current receiving-use dispositions — 2026-11-03' (+15)
        - auditonomous@beta:L7/provenance/sources/LEDGER.md:147 '## Attributable receiving correction — 2026-11-03' (+8; not named in the claim)
        - auditonomous numstat: 17 added files = 6 allications sheets + object-2 0.md + binding.json + 9 under L8; the 11 non-allications files total 2,154 lines; sheet count 78 on main, 85 on beta
        - Records: autonomous L8/L6/history/harmonization-2026-09-05.md blob 47ba4e0 on main and beta, last heading '## 13. 2026-09-12 — the rename pass'; auditonomous blob 9899217 on main and beta, last heading '## 12. 2026-09-12 — the rename pass'
        - autonomous@beta:L8/L6/history/BETA_HISTORY.md:8,10,14 and auditonomous@beta:L8/L6/history/AUDITONOMOUS_BETA_HISTORY.md:6,7,11 (the passes are recorded there, not in the numbered record)
        - ls-tree of both betas: root = .github, .gitignore, L7, L8, README.md; L7/allications has 0.md plus six positions; L7/governance has controlled and no restrictions
    - item 8
      - **claim**: Each exemplar clone holds one local commit, on no remote, dated 11 November 2026, that performs the hand mirror from main: autonomous 8257118 and auditonomous f2d5b37, both on refs/heads/ccr-9391bd81-f2enmj, authored by Claude with this session's trailer. Checked from git objects: no former phrase remains in live text; 103 and 84 sheets are each headed by their path; all 71 positions are sheeted; the binder payload files moved unchanged; the Auditonomous check is byte-identical to the scaffold's main and the Autonomous check is that file plus its Q-6 block; each repository's record gains its own section (14 and 13) quoting the owner's request as written. Each conflicts with its repository's beta candidate, in 12 and 13 files. Not verified: every edited line read one by one.
      - **id**: K10
      - **verdict**: corrected
      - **reasoning**: Every part of K10 was re-derived from git objects and confirmed except one imprecision about the Autonomous check, plus two scope limits worth stating.

        **Confirmed**
        - **One local commit each, from main.** Autonomous `8257118` has parent `c9076c3` (origin/main) and auditonomous `f2d5b37` has parent `2165144` (origin/main); `rev-list --count origin/main..<commit>` is 1 in both. Each is only on `refs/heads/ccr-9391bd81-f2enmj`, and `git branch -a --contains` lists no remote-tracking ref. There are no tags or stash refs in either clone.
        - **Date, author, trailer.** Both are authored and committed by `Claude <noreply@anthropic.com>`, at 2026-11-11 18:33:28 +0000 and 18:34:37 +0000. Both carry `Claude-Session: https://claude.ai/code/session_0152eAiHSRyxYsXUkjd69kS7`, which is this session.
        - **Former phrases.** Twelve former phrases and paths were counted across each whole tree, among them "peering, and publication state", "the L7 publications branch", "access, restrictions", `L7/governance/restrictions` and `L7/publications`. All hits are in `L8/L6/history/` (the record and `7LM_ROUTING_PLAN_2026-09-05.md`), except the one history note at `L7/allications/0.md:42` in both. Two further scaffold phrases, the old canonical-branches line and "licensing and restrictions", have 0 hits.
        - **Remaining "publications" wording matches the scaffold.** The lines still saying "publications" in live sheets (`L7/0.md:3`, `:6`, `:23`, `:99`, `:241`; `L8/0.md`; `L8/L5/research/0.md:32`) are carried identically by 7lm origin/main.
        - **G-003 simulation.** Autonomous: 103 sheets checked, 0 wrong headings, 71 of 71 positions sheeted. Auditonomous: 84, 0, 71 of 71. Both have a canonical root, no conflict markers, and no `L7/publications` or `L7/governance/restrictions` path left in the tree.
        - **Binder payload.** The non-sheet binder files have identical blob ids before and after the move: 7 files in autonomous, 3 in auditonomous (R100 renames).
        - **Auditonomous check.** `f2d5b37:.github/workflows/integrity.yml` is blob `f43dd0459f4dafb60e0f2254c1dc2db2772cb0eb`, the same blob as 7lm origin/main.
        - **Record sections.** Autonomous has "## 14. 2026-11-11 …" at line 183 with the owner's request at line 185; auditonomous has "## 13. 2026-11-11 …" at line 176 with the request at line 178. The quote matches the request character for character, including "phsyciall; to match first ."
        - **Conflicts with beta.** `git merge-tree --write-tree` reports 12 conflicted files for autonomous and 13 for auditonomous. The lists are the same except that auditonomous adds `L8/L4/work/computation/0.md`. Six of the conflicts in each are add/add at the `L7/allications` sheets.

        **Imprecise**
        - **Autonomous check is not strictly "that file plus its Q-6 block".** `8257118:.github/workflows/integrity.yml` (blob `45ad3f7`, 97 lines) differs from the scaffold's (69 lines) in two ways. It lacks the scaffold's blank line 12, between the checkout step and the G-001 step. It inserts, after the G-001 step, one blank line and the 28-line retired Q-6 comment block (lines 15-43), which is identical to the block on autonomous origin/main. All non-blank content is otherwise identical.

        **Scope limits**
        - "On no remote" is verified only against the remote-tracking refs in each clone; the network was not consulted.
        - 103 and 84 are the sheets the check counts: `0.md` files under `L7/` and `L8/`, excluding those below the root of each retired set.
      - **corrected_statement**: Each exemplar clone holds one local commit, contained in no remote-tracking ref of the clone (the network was not consulted), dated 11 November 2026 (18:33:28 and 18:34:37 +0000), whose single parent is origin/main (c9076c3; 2165144) and which performs the hand mirror: autonomous 8257118 and auditonomous f2d5b37, both on refs/heads/ccr-9391bd81-f2enmj, authored and committed by Claude <noreply@anthropic.com> with this session's trailer (session_0152eAiHSRyxYsXUkjd69kS7). Checked from git objects: no former phrase remains in live text (all hits are in L8/L6/history/, plus the one history note at L7/allications/0.md:42 in each); 103 and 84 sheets (those the check counts, outside the interiors of retired sets) are each headed by their path; all 71 canonical positions are sheeted; the binder payload files (7 and 3) moved with identical blobs; the Auditonomous check is byte-identical to the scaffold's main (blob f43dd04). The Autonomous check (blob 45ad3f7, 97 lines against 69) is the scaffold's file with its own retired Q-6 comment block (28 lines, identical to the block on autonomous main) and a preceding blank line inserted after the G-001 step, and without the scaffold's blank line 12 between the checkout step and the G-001 step; its non-blank content is otherwise identical. Each repository's record gains its own section (autonomous section 14 at L8/L6/history/harmonization-2026-09-05.md:183; auditonomous section 13 at :176) quoting the owner's request exactly as written. Each conflicts with its repository's beta candidate, in 12 files (autonomous, against e64b382) and 13 files (auditonomous, against 714480d; the same 12 plus L8/L4/work/computation/0.md). Not verified: every edited line read one by one.
      - **evidence_checked**
        - autonomous: git for-each-ref refs/heads refs/remotes -> refs/heads/ccr-9391bd81-f2enmj 8257118 (2026-11-11 18:33:28 +0000); refs/heads/main = origin/main = c9076c3; no tags or other refs
        - auditonomous: git for-each-ref refs/heads refs/remotes -> refs/heads/ccr-9391bd81-f2enmj f2d5b37 (2026-11-11 18:34:37 +0000); refs/heads/main = origin/main = 2165144; no tags or other refs
        - git branch -a --contains 8257118 / f2d5b37 -> only the local ccr-9391bd81-f2enmj in each clone
        - git log on 8257118 and f2d5b37: author and committer Claude <noreply@anthropic.com>; single parents c9076c3 and 2165144; trailers 'Co-Authored-By: Claude Fable 5.2' and 'Claude-Session: https://claude.ai/code/session_0152eAiHSRyxYsXUkjd69kS7'; rev-list --count origin/main..commit = 1 in both
        - git diff -M --name-status origin/main 8257118 (78 files) and origin/main f2d5b37 (55 files): R100 on 7 and 3 binder payload files; ls-tree blob ids of the non-sheet binder files identical before and after
        - git grep -c -F on 8257118 and f2d5b37 for 12 former phrases and paths: hits only under L8/L6/history/ (harmonization-2026-09-05.md, 7LM_ROUTING_PLAN_2026-09-05.md), plus L7/allications/0.md:42 '`publications/` moved here from `L7/publications/` in the pass of 2026-11-11'; the old canonical-branches line and 'licensing and restrictions' have 0 hits
        - Residual 'publications' wording in live sheets (L7/0.md:3, 6, 23, 99, 241; L8/0.md; L8/L5/research/0.md:32) is carried identically by 7lm@origin/main
        - G-003 simulated from objects (ls-tree plus show, first line of each sheet): autonomous@8257118 103 sheets, 0 wrong headings, 71/71 positions; auditonomous@f2d5b37 84 sheets, 0 wrong headings, 71/71 positions; root entries .github, .gitignore, L7, L8, README.md in both; no conflict markers; no L7/publications or L7/governance/restrictions path in either tree
        - git rev-parse: 7lm origin/main:.github/workflows/integrity.yml = f43dd0459f4dafb60e0f2254c1dc2db2772cb0eb = auditonomous f2d5b37:.github/workflows/integrity.yml; autonomous 8257118 = 45ad3f7c1b27d83e7f18d75150506871a600e68d
        - diff of 7lm@origin/main:.github/workflows/integrity.yml against autonomous@8257118:.github/workflows/integrity.yml: '12d11' (the scaffold's blank line 12 absent) and '15a15,43' (one blank line plus the 28-line Q-6 comment block); the Q-6 block is identical to the one on autonomous@origin/main; 69 lines against 97
        - autonomous@8257118:L8/L6/history/harmonization-2026-09-05.md:183 '## 14. 2026-11-11 — the L7 restructure mirrored by hand: allications, and controlled; the words match the folders'; :185 owner quote 'Get qa hanfle on the research and manuscruipt for Auditonomous but firwst re0ull7lm ...'
        - auditonomous@f2d5b37:L8/L6/history/harmonization-2026-09-05.md:176 '## 13. 2026-11-11 — the L7 restructure mirrored by hand: allications, and controlled; the words match the folders'; :178 the same owner quote, matching the relayed request exactly
        - git merge-tree --write-tree --name-only 8257118 origin/beta/7lm-exemplar-autonomous: exit 1, 12 conflicted files (.github/workflows/integrity.yml, L7/0.md, six L7/allications sheets as add/add, L7/governance/0.md, L7/governance/controlled/0.md, L7/peering/0.md, L7/peering/public/0.md)
        - git merge-tree --write-tree --name-only f2d5b37 origin/beta/7lm-exemplar-auditonomous: exit 1, 13 conflicted files (the same 12 plus L8/L4/work/computation/0.md)
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498 (section 37) used as the scaffold's phrase list: 'peering, and publication state', 'the L7 publications branch', 'access, restrictions', 'licensing and restrictions folders'
    - item 9
      - **claim**: No unmerged branch of the scaffold adds, removes or renames a canonical position: every check file on every branch lists the same 71, and the only directory not on main is the dated retired set L8/L6/retired/field-guide-2026-09-20/ (pull request #20, also merged into the pull request #19 branch and the audit branch). Pull request #20, pull request #19 and the audit branch each merge into main without conflict. The beta conflicts with pull request #19 in 7 files and with the audit branch in 12; pull request #19 and the audit branch conflict in 20. The audit branch's check would refuse the .gitignore that both exemplars carry and would require a body in every sheet.
      - **id**: K11
      - **verdict**: corrected
      - **reasoning**: Every numeric and merge fact in the claim reproduces from the git objects. One phrase is too broad: "every check file on every branch lists the same 71" (and, by extension, "the only directory not on main") is false for one remote branch the claim does not mention, origin/copilot/create-academic-guide-plan. That branch is not unmerged (it is an ancestor of main, e22c5fc, dated 2026-09-19, before the L7 restructure), so the claim's headline about unmerged branches survives, but the wording must be limited to main plus the unmerged branches.

        CONFIRMED
        1. Directories. `git ls-tree -r -d --name-only` diffed against origin/main (97 directories): beta 97314c5 = identical; copilot/create-error-list 1e2fe77 = identical; ccr-9a67809a-iwii3n c6d598a = identical; ccr-9391bd81-f2enmj c9638a9, ccr-00099fac-hjosbo b5c3984 and audit 3555866 each differ by exactly one added line, L8/L6/retired/field-guide-2026-09-20 (2 files: 0.md and 7lm-field-guide.md, the latter a pure rename). No directory removed or renamed on any unmerged branch.
        2. Check files. Canonical lists parsed from .github/workflows/integrity.yml: main (blob f43dd04, lines 47-59, with $top=L8/lower=L), beta (blob cd39c5b, lines 47-57, hard-coded L8/L6..L0), PR #20 branch (same blob as main), PR #19 branch (blob d98049a, differs from main only in comment lines 3-5), audit (blob 4c123df, lines 99-169), copilot/create-error-list (same blob as main): each 71 entries, 71 unique, sets identical. All 71 `<position>/0.md` files exist on each of those six refs (0 missing).
        3. Audit locators. 7lm@origin/audit/peering-descriptive-reframe-2026-09-20:.github/workflows/integrity.yml:49 reads "canonical root must contain exactly README.md, L7/, L8/, and .github/ (found $count entries)"; :99-169 is exactly 71 lines of positions.
        4. PR #20 ancestry. c9638a9 is an ancestor of b5c3984 and of 3555866; both tips are themselves the merge commits "Merge branch 'ccr-9391bd81-f2enmj': the field guide retired; the rename reconciled". It is not in main and not in the beta.
        5. Merge tests (git merge-tree --write-tree --name-only, in /home/user/7lm): main+ccr-9391bd81-f2enmj exit 0 tree 7df0bd6; main+ccr-00099fac-hjosbo exit 0 tree ce1e27f; main+audit exit 0 tree b9c0599. beta+ccr-00099fac-hjosbo exit 1, 7 conflicted files (L7/peering/0.md, L7/peering/private/ingress/0.md, L7/provenance/sources/0.md, the specification .docx and .md, L8/L5/research/review/0.md, L8/L6/history/specification-history.md). beta+audit exit 1, 12 files (including .github/workflows/integrity.yml). ccr-00099fac-hjosbo+audit exit 1, 20 files (including .github/workflows/integrity.yml).
        6. Audit check behaviour. Root step: :40 `README.md|L7|L8|.github) ;;` and :48 `[ "$count" -eq 4 ]`, so a tracked .gitignore fails twice ("not canonical at root" and the count). Both exemplars track .gitignore at root on origin/main and on their beta refs (ls-tree: ".github .gitignore L7 L8 README.md"); the scaffold has no root .gitignore on any ref. Body step: :89-94, `if ! tail -n +2 "$s" | grep -q '[^[:space:]]'` -> "current sheet has no semantic body: $s".

        IMPRECISIONS / EVIDENCE THE CLAIM DOES NOT CITE
        a. origin/copilot/create-academic-guide-plan (e22c5fc, "Merge pull request #16: the UHA/oMMP exemplar filed at L7 prior-art", 2026-09-19; `merge-base --is-ancestor ... origin/main` true): its integrity.yml (blob 5538d89) lists 57 positions, not 71: it has L7/governance/restrictions and L7/publications, and lacks L7/governance/controlled, the seven L7/allications* positions and the eight peer-1 / peer-1/object-1 positions. Its tree has 91 directories including L7/governance/restrictions and L7/publications, which are not on main. So "every branch" is literally false; it holds for main and every branch that has commits not on main.
        b. The claim's directory evidence names "the three branches"; the other two unmerged refs (beta, and copilot/create-error-list which is 1 commit ahead of main: 1e2fe77 "Publish all 96 audit recommendations with priorities and coverage limits") were not cited but I checked them: no directory difference, same 71. The beta's check file is a different blob from main's (USO alternative removed, L8 hard-coded) though the 71 are the same.
        c. "a body in every sheet" is slightly broad: the rule applies to current sheets under L7/ and L8/; sheets nested below a retired set's root are skipped (:76-80, `*/L6/retired/*/*) continue`).
        d. Practical weight: I ran the audit body rule against the exemplars' objects. No heading-only current sheet exists on autonomous origin/main (97 sheets), autonomous beta (110), auditonomous origin/main (78) or auditonomous beta (85), so the body rule would not bite today; the .gitignore rule would. (main's and the beta's checks both allow .gitignore: main :23, beta :23.)
        e. The three clean merges into main are individually clean only. Since PR #19 and the audit branch conflict with each other in 20 files, they cannot both be merged into main without conflict resolution. Also not stated in the claim: the beta itself merges into main cleanly (exit 0, tree 633c343), beta+PR #20 is clean (1b235ad), PR #20+PR #19 and PR #20+audit are clean, and copilot/create-error-list merges into main cleanly (16c2878).
        f. The mapping of PR numbers (#19, #20) to branch names is taken from the task brief; it cannot be verified from git objects without the network.
      - **corrected_statement**: No unmerged branch of the scaffold (origin/beta/common-contracts-r1-r6, origin/ccr-9391bd81-f2enmj [PR #20], origin/ccr-00099fac-hjosbo [PR #19], origin/audit/peering-descriptive-reframe-2026-09-20, origin/copilot/create-error-list) adds, removes or renames a canonical position: the check file on main and on each of those five branches lists the same 71 positions, and all 71 sheets exist on each. The only directory on any unmerged branch that is not on main is the dated retired set L8/L6/retired/field-guide-2026-09-20/ (PR #20, c9638a9, also merged into the PR #19 branch tip b5c3984 and the audit branch tip 3555866; not in the beta). The one exception among all remote branches is origin/copilot/create-academic-guide-plan (e22c5fc, 2026-09-19), which is NOT unmerged (it is an ancestor of main) and still carries the pre-restructure state: a 57-position check list and the directories L7/publications and L7/governance/restrictions. PR #20, PR #19 and the audit branch each merge into main without conflict when tested individually (trees 7df0bd6, ce1e27f, b9c0599); PR #19 and the audit branch cannot both go in cleanly, since they conflict with each other in 20 files. The beta conflicts with PR #19 in 7 files and with the audit branch in 12 (the beta itself merges into main cleanly, tree 633c343). The audit branch's check (.github/workflows/integrity.yml:40, :48-49) allows exactly four root entries, README.md, L7, L8, .github, so it would refuse the tracked .gitignore that both exemplars carry on main and on their beta branches; and it requires non-blank content after the heading line in every current sheet under L7/ and L8/ (:89-94), sheets nested below a retired set's root excepted (:76-80). No current exemplar sheet on either main or either beta is heading-only, so of the two rules only the .gitignore one would fail the exemplars as they stand.
      - **evidence_checked**
        - 7lm: git ls-tree -r -d --name-only for origin/main, beta/common-contracts-r1-r6, ccr-9391bd81-f2enmj, ccr-00099fac-hjosbo, audit/peering-descriptive-reframe-2026-09-20, copilot/create-error-list, copilot/create-academic-guide-plan, ccr-9a67809a-iwii3n; diffed each against main (97 dirs on main; +1 L8/L6/retired/field-guide-2026-09-20 on PR20/PR19/audit; academic-guide-plan 91 dirs with L7/publications and L7/governance/restrictions)
        - 7lm@origin/main:.github/workflows/integrity.yml:23 (root case allows .gitignore) and :47-59 (71 positions, blob f43dd04)
        - 7lm@origin/beta/common-contracts-r1-r6:.github/workflows/integrity.yml:23 and :47-57 (71 positions, blob cd39c5b)
        - 7lm@origin/ccr-00099fac-hjosbo:.github/workflows/integrity.yml (blob d98049a; differs from main only at comment lines 3-5; 71 positions)
        - 7lm@origin/ccr-9391bd81-f2enmj, origin/copilot/create-error-list, origin/ccr-9a67809a-iwii3n: .github/workflows/integrity.yml is blob f43dd04, identical to main
        - 7lm@origin/audit/peering-descriptive-reframe-2026-09-20:.github/workflows/integrity.yml:40 (README.md|L7|L8|.github), :48-49 ('canonical root must contain exactly README.md, L7/, L8/, and .github/ (found $count entries)'), :76-80 (retired exemption), :89-94 ('current sheet has no semantic body: $s'), :99-169 (71 positions)
        - 7lm@origin/copilot/create-academic-guide-plan:.github/workflows/integrity.yml (blob 5538d89): 57 positions, L7/governance/restrictions and L7/publications; git merge-base --is-ancestor against origin/main true
        - 7lm: existence of <position>/0.md for all 71 positions on main, beta, PR20, PR19, audit, create-error-list (0 missing on each)
        - 7lm: git merge-base --is-ancestor origin/ccr-9391bd81-f2enmj against ccr-00099fac-hjosbo (true), audit (true), beta (false), main (false); merge commits b5c3984 and 3555866
        - 7lm: git merge-tree --write-tree --name-only: main+PR20 exit 0 7df0bd6; main+PR19 exit 0 ce1e27f; main+audit exit 0 b9c0599; main+beta exit 0 633c343; main+create-error-list exit 0 16c2878; beta+PR19 exit 1, 7 files; beta+audit exit 1, 12 files; PR19+audit exit 1, 20 files; beta+PR20 exit 0 1b235ad; PR20+PR19 exit 0; PR20+audit exit 0
        - 7lm: git ls-tree --name-only root of every scaffold ref: .github L7 L8 README.md (no .gitignore anywhere)
        - autonomous@origin/main and @origin/beta/7lm-exemplar-autonomous: root ls-tree = .github .gitignore L7 L8 README.md
        - auditonomous@origin/main and @origin/beta/7lm-exemplar-auditonomous: root ls-tree = .github .gitignore L7 L8 README.md
        - Audit body rule applied to git objects of exemplar sheets: autonomous main 97 current sheets, beta 110; auditonomous main 78, beta 85; zero heading-only sheets, zero wrong headings
        - 7lm: git log origin/main..origin/copilot/create-error-list = 1 commit (1e2fe77); git diff --stat -M origin/main...origin/ccr-9391bd81-f2enmj (field guide renamed into the retired set, 9 files)
    - item 10
      - **claim**: Four standing rules of the model of record govern the pass. The exemplars mirror the scaffold by hand, when the owner judges the scaffold close. The system is not changed without asking. Each repository's history is kept at its own L6, so the pass is recorded in each exemplar's own record and nothing of the scaffold's L6 is copied. What is not a design choice is the tree and, in every folder, a 0.md whose first line is the folder's path; everything else a sheet says is the repository's own choice.
      - **id**: K12
      - **verdict**: corrected
      - **reasoning**: Every cited locator is confirmed on 7lm@origin/main (c9dc061), and the four rules are still in force there. Two parts of the claim are imprecise against the same objects, so the verdict is "corrected", not "stands".

        **Confirmed as cited** (all in 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md)
        - :336 (section 26), owner: "All repos should mirror the 7lm. Manually. We update 7lm and focus on it only. No outside updates until we are sure I'm close."
        - :346: "they will be, manually, when the owner judges the scaffold close, and not before."
        - :482 (section 36), owner: "Don't change the system unless you ask or are unsure". The standing at :484 adds: "no change to the system without asking first; when unsure, ask instead of deciding."
        - :402 (section 31), owner: "Our 7Lm guides DO NOT share ANY HISTORY! HARD RULE. That's why you have l6."
        - :406: "Each repository's history is its own, kept at its own L6 and nowhere else."
        - :352 (section 27): "What is not a design choice is the tree the scaffold pushes and, in every folder of it, a `0.md` whose first line is the folder's path from the root."

        **Nothing later overrides them**
        - The record on main ends at section 37. Section 37 (:506) corrects section 31 only on where the rule sits in the guide ("a bold lead-in ... not under its own heading"). Its reading at :510 keeps section 36 in force ("no leave to change what any position is, holds, or is named").
        - 2e5a6d6..origin/main adds one file only, L8/L6/in/7lm-layer-lists.md (PR #21).
        - The field guide on main restates all four: L8/L6/7lm-field-guide.md:608, :132, :240, :455, :457.

        **Imprecision 1: "nothing of the scaffold's L6 is copied" is broader than the rule**
        - What the rule bars is history. :406 and guide :610: "The push carries the tree and the sheets, never the scaffold's L6; no repository's history moves in either direction."
        - But the scaffold's L6 also holds two source documents the model says an adopter takes, by a person's act:
          - the guide: :340 and guide :9 ("A person who adopts the model takes this guide from L6, applies its updates or leaves them"), guide :608 ("this guide at L6 as the source each adopter takes");
          - the sheet templates: :364 ("beside the guide at L6 as source material an adopter takes").
        - So the scaffold's history/, retired/ and in/ must not be copied; the guide and templates are not barred by the rule, and what an adopter does with them is its design choice (guide :610).
        - Tree check: neither exemplar holds a copy of 7lm-field-guide.md, 7lm-sheet-templates.md, harmonization-2026-09-04.md or specification-history.md, on origin/main or on the beta branch (ls-tree). Each has its own L8/L6/history/ with its own harmonization-2026-09-05.md, so "recorded in each exemplar's own record" is workable.

        **Imprecision 2: the list of what is not a design choice has a third member on main**
        - Section 31 (:408) added the no-shared-history rule to that list. Guide :554: "The tree, the sheets' first lines, and the rule that the guides share no history are not."
        - The same line names "whether a position is used at all" as a design choice; guide :610: "The pushed tree is required; taking up everything in it is not".
        - "Everything else a sheet says is the repository's own choice" is correct (:352, L8/L6/7lm-sheet-templates.md:3).

        **Minor: labels**
        - The record calls only two of the four "standing" (:346 "Standing.", :480 heading). Section 31 is the owner's "HARD RULE"; section 27 is an owner ruling with no label.
      - **corrected_statement**: Four rules of the model of record (7lm@origin/main c9dc061, L8/L6/history/harmonization-2026-09-04.md, sections 26, 27, 31 and 36; none altered by section 37 or by PR #21) govern the pass. (1) Standing, section 26 (:336, :346): the exemplars mirror the scaffold by hand, when the owner judges the scaffold close and not before. (2) Standing, section 36 (:482, :484): the system is not changed without asking; when unsure, ask; findings go to the owner as proposals and nothing is applied until the owner says which. (3) The owner's hard rule, section 31 (:402, :406): the guides share no history; each repository's history is its own, kept at its own L6 and nowhere else. So the pass is recorded in each exemplar's own L8/L6/history/, and none of the scaffold's history (its L8/L6/history/, retired/, in/) is copied into an exemplar. The rule does not bar the two source documents filed at the scaffold's L6, the field guide and the sheet templates, which the model says an adopter takes by a person's (HOA) act as its own design choice (:340, :364; guide :9, :608, :610); neither exemplar holds a copy of either on main or beta. (4) Section 27 (:352), as extended by section 31 (:408; guide :554): what is not a design choice is the tree the scaffold pushes, in every folder of it a 0.md whose first line is the folder's path from the root, and the rule that the guides share no history; everything a sheet says after its first line is the repository's own choice, and whether a position is used at all is also a design choice (guide :554, :610).
      - **evidence_checked**
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:336 (section 26 owner quote, verbatim match)
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:340 (guide is an L6 source document the adopter takes)
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:346 ('they will be, manually, when the owner judges the scaffold close, and not before')
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:350-352 (section 27: what is not a design choice)
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:364 (templates 'beside the guide at L6 as source material an adopter takes')
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:402-408 (section 31 hard rule; push carries 'never the scaffold's L6'; Design choice vocabulary names the rule)
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:480-484 (section 36 heading, owner quote, standing)
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:492-510 (section 37: correction to section 31 is placement only; reading keeps section 36)
        - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md headings (grep '^## '): sections 1 to 37, none later
        - 7lm: git log 2e5a6d6..origin/main and diff --stat: only L8/L6/in/7lm-layer-lists.md added (PR #21)
        - 7lm@origin/main:L8/L6/7lm-field-guide.md:9, :132, :240, :455, :457, :554, :608, :610
        - 7lm@origin/main:L8/L6/7lm-sheet-templates.md:3-9
        - 7lm@origin/main:L8/L6/0.md:1-45
        - 7lm@origin/main ls-tree L8/L6 (guide and templates sit directly at L6 beside history/, in/, retired/)
        - 7lm@origin/beta/common-contracts-r1-r6:L8/L6/history/harmonization-2026-09-04.md headings: also ends at section 37
        - autonomous@origin/main and @origin/beta/7lm-exemplar-autonomous ls-tree L8/L6: own history/ (harmonization-2026-09-05.md; BETA_HISTORY.md on beta); no copy of scaffold guide, templates or records
        - auditonomous@origin/main and @origin/beta/7lm-exemplar-auditonomous ls-tree L8/L6: own history/ (harmonization-2026-09-05.md; AUDITONOMOUS_BETA_HISTORY.md on beta); no copy of scaffold guide, templates or records
  - **gaps**
    - item 1
      - **severity**: critical
      - **gap**: The owner's instruction of 14 September 2026, which sets the order of work that today's request belongs to, is nowhere in the report. It is recorded only on two closed, unmerged branches, with a read-only exemplar declaration for Autonomous and 23 open owner decisions.
      - **finding**: The words, as written, stand at autonomous@origin/claude/scholarly-pair-baseline-k8ap82:L8/L6/history/exemplar-2026-09-14.md:7 and auditonomous@origin/claude/book-structure-roadmap-k8ap82:[source text withheld from the public copy]." and "[source text withheld from the public copy]." Neither exemplar's main nor beta carries them (git grep for 'scholarly pair', 'read only exemplar', 'read-only exemplar' on origin/main and both beta refs: 0 files).

        The roadmap record turns them into seven steps S0 to S6 (auditonomous@origin/claude/book-structure-roadmap-k8ap82:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:567, "Build first, write after."; rows :583-589). Step S3 at :586 judged the model "[source text withheld from the public copy]". The restructure of 20 September overtook that judgement; today's request is S3 again.

        The Autonomous branch (9b49910, 9 files) files a declaration at L7/governance/restrictions/0.md:34: "this repository is declared a read-only exemplar of the Seven-Layer Model". Its record says the L0 object and its companions "change only by a dated version merged by the owner" and that the tag exemplar-2026-09-14 and protection of main are the owner's acts (exemplar-2026-09-14.md:11, :25).

        Not weighed in the report:
        - The mirror renames the position where that declaration is filed.
        - The Autonomous beta e64b382 edits two L0 companions, L8/L0/semantics/definitions/DEFINITION_LIST_AUTONOMOUS.md and REGISTER.md (git diff --name-status origin/main origin/beta/7lm-exemplar-autonomous), which the declaration reserves for versions the owner merges.
        - Four unmerged scaffold lines (beta, PR #19, PR #20, audit) conflict with each other in 7, 12 and 20 files, which bears on "stable".

        Decisions missing from the report's fourteen: whether the 14 September order still governs; step S1 (merge, tag, protection of main); the papers' review; and the roadmap's decisions D1 to D23 (:606-633). Decision 13 names only the Auditonomous branch.
    - item 2
      - **severity**: high
      - **gap**: The report understates what 'the research and manuscript for Auditonomous' is and where it sits. Main is a remnant whose research files cite objects that are not in its tree; the corpus, the book tree and the vocabulary paper exist only on the closed branch.
      - **finding**: Branch against main: 328 files against 169; 159 added, 17 modified, 22,883 lines inserted (git diff --shortstat origin/main origin/claude/book-structure-roadmap-k8ap82). The report names manuscript/ (55) and book/ (31). Also only on the branch: papers/ (2), prompts/ (4), sourcebook/ (4), 24 files under L8/L5/research/review, 16 under L8/L4/work/computation, 4 findings, L8/L0/semantics/definitions/AUDITONOMY.md, two L1 objects, L7/provenance/sources/STANDARDS_REGISTER.md and lists-2026-08-08/ (6 files), the Martin 2026 manuscript at peer-3 (2 files), and the record L8/L6/history/restore-2026-09-14.md.

        On main, live research files cite files absent from main's tree (ls-tree origin/main has no AUDITONOMY.md, AUDITON_REPLICATOR.md, AUTONOMY_AT_DISTANCE.md or STANDARDS_REGISTER.md):
        - auditonomous@origin/main:L8/L1/state-space/AUDITON_ENVELOPE.md:76 ("`definitions/AUDITONOMY.md` §0") and :110
        - L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:3 ("The answer to `STANDARDS_REGISTER.md` **Q2**")
        - L8/L5/research/findings/DISTILLATION.md:21
        - L8/L5/research/review/CONTRADICTIONS.md:46 and :72
        - line 5 of the three requirement extractions at L8/L4/work/computation/

        The branch's record states it: restore-2026-09-14.md:3, files "that existed at HEAD only as history"; :13, "[source text withheld from the public copy] roadmap adds at :13 that of six prior book structures, "[source text withheld from the public copy]`".

        The book tree holds headers only: roadmap :587, "no chapter has text".

        The Auditonomous beta 714480d was built from main, not from this branch: a test merge of the two conflicts in L7/0.md, L8/L0/0.md and L8/L0/semantics/definitions/0.md.

        So a QA pass has no settled base: main, or the closed branch. Decision 13 asks only whether the branch is revived.
    - item 3
      - **severity**: high
      - **gap**: The model's sheet rule was tightened on 20 September 2026 so that every folder carries a sheet. Six folders in Autonomous and twelve in Auditonomous have none, before and after the listed operations. The report tells the migrator to leave them and lists no decision.
      - **finding**: At the rename pass the guide read (7lm@67bb795:L8/L0/pedagogy/7lm-field-guide.md:422): "Give each one a `0.md` when you can." Record section 37 withdrew that as having "made the sheet optional" (7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:502).

        Main now reads:
        - 7lm@origin/main:L8/L6/7lm-field-guide.md:474: "Give each one a `0.md`; every folder carries one." and "a folder without a sheet is outside the system. Both exemplar repositories do exactly this."
        - :600: "A missing sheet is a folder outside the system."
        - the specification, of both exemplars (SPEC:934): "Every directory has its 0.md, headed by its path."
        - each exemplar's own README.md:5: "every directory under `L7/` and `L8/` describes itself in its own `0.md`".

        Simulating the scaffold's check from git objects on both local commits: Autonomous 8257118 passes with 6 notices (binder internal/, internal/tools/, press-kit/; autonomous-theory/ and its two subfolders); Auditonomous f2d5b37 passes with 12. The check itself says such folders "may carry sheets or not" (CHK:35), so nothing fails.

        The report's beta bullet is wrong on this point. The Autonomous beta added 13 sheets, not six: the six allications sheets, one at each of the six unsheeted folders (for example autonomous@origin/beta/7lm-exemplar-autonomous:L7/allications/publications/binder/internal/0.md:1), and peer-1/object-2. It checks at 110 sheets with 0 notices. The Auditonomous beta left all 12.

        The rule is not settled: PR #20 would retire the guide (7lm@origin/ccr-9391bd81-f2enmj:L8/L6/history/harmonization-2026-09-04.md:518, "Deprecated and to be used as an example"), while the templates keep the narrower form, "in every folder of the tree the scaffold pushes" (7lm@origin/main:L8/L6/7lm-sheet-templates.md:3).

        Missing decision: whether a physical match includes a sheet, blank if need be, at these 18 folders, nine of which hold third-party staging records.
    - item 4
      - **severity**: high
      - **gap**: The mirror would break two closed branches that merge cleanly into main today, and would leave former names in their files. The report does not say so; the local commits' own record sections understate it.
      - **finding**: Tested with git merge-tree --write-tree.

        Autonomous. origin/main + claude/scholarly-pair-baseline-k8ap82 merges clean. 8257118 + that branch conflicts in L7/governance/0.md: the mirror wrote `controlled/` where the branch wrote "One restriction that is not copyright-derived is filed at `restrictions/`". In the merged tree former names stand at:
        - L7/0.md:233 (auto-merged)
        - L7/governance/0.md:35
        - L8/L4/work/writing/papers/0.md:8 ("until its release is recorded at `L7/publications/`")
        The declaration itself follows the rename into L7/governance/controlled/0.md. The branch's record exemplar-2026-09-14.md names `L7/governance/restrictions/0.md` three times and, being a record, must stay.

        Auditonomous. origin/main + claude/book-structure-roadmap-k8ap82 merges clean. f2d5b37 + that branch conflicts in L7/0.md (the Holdings bullets). In the merged tree:
        - L7/provenance/sources/lists-2026-08-08/0.md:24 carries the swept sentence "peering, and publication state"
        - L8/L4/work/writing/book/0.md:25, book/ch01-the-readers-contract.md:11 and papers/0.md:8 name `L7/publications/`
        - the roadmap names former paths at :40, :99, :376, :584, :589 and :683

        The local record says of this branch (auditonomous@f2d5b37:L8/L6/history/harmonization-2026-09-05.md:207): "thirty of its live files name the former paths as `main` did". Four of the thirty are the branch's own new files (26 on main, 30 on the branch), and neither the conflict nor the swept sentence in the new sheet is mentioned. The Autonomous record (:214) notes only that the branch "edits `L7/governance/restrictions/0.md` at its former path".

        Unchanged by the mirror: each no-deletion-fix branch conflicts with main in L8/L5/research/0.md and L8/L5/research/review/0.md before and after.
    - item 5
      - **severity**: medium
      - **gap**: Operation 5 names one line of the scaffold's L7/allications/0.md as the scaffold's own history. There are two. The other, line 8, is a dated quotation of the owner, and copying it gives each exemplar its only sheet that carries one.
      - **finding**: 7lm@origin/main:L7/allications/0.md:8 begins: "The owner named this position on 2026-09-19, quoted as written:". Line 38 is the move note the checklist does handle.

        Both local commits carry line 8 unchanged (autonomous@8257118:L7/allications/0.md:8; auditonomous@f2d5b37:L7/allications/0.md:8). On both exemplar mains no sheet contains 'quoted as written' (git grep over *0.md, history and retired excluded: 0 lines).

        Each exemplar's own rule of 2026-09-07 took such text out of sheets: autonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:167 and auditonomous@origin/main at :160, "The dates and the owner's words that stood beside the layout's rules in the sheets ... are pulled out of the sheets". The rewritten line 38, a dated move note, is the same kind of text.

        Line 8 is scaffold-specific on every scaffold branch. PR #19 rewrites it to "This position was named on 2026-09-19 (record: `L8/L6/history/harmonization-2026-09-04.md` §25)." (7lm@origin/ccr-00099fac-hjosbo:L7/allications/0.md:8). That cites a record file no exemplar has; theirs is harmonization-2026-09-05.md.

        The five child sheets carry no scaffold history (read in full, lines 1-37 each).

        Test of the checklists: applying operations 2 to 22 literally to an export of each exemplar's origin/main reproduces 8257118 and f2d5b37 file for file, except the Holdings sections added to the six new sheets, the label and one added sentence at L7/0.md:223, the date, and the two history files (diff -rq of the exports). So the checklists are complete as a description of the local commits, and this line is the one place where both follow the scaffold too closely.
    - item 6
      - **severity**: medium
      - **gap**: The report notes that PR #19 takes authorship tags out of live text, but does not connect it to the checklists, which copy one owner quotation into two more repositories and quote the owner's request of 11 November in two new record sections.
      - **finding**: PR #19's record, 7lm@origin/ccr-00099fac-hjosbo:L8/L6/history/harmonization-2026-09-04.md:514, gives the instruction of 6 October in indirect speech: "the public is to see the sheets and the source documents without authorship tags of any kind, the author's own included". It adds that the author doubted the quoted words should be public, and: "On that doubt the words of this instruction are not quoted here as written".

        Effect on the scaffold's live text, counted here: 'quoted as written' occurs 6 times on origin/main and 0 on the PR #19 branch; 'the owner' 127 against 45.

        Against that:
        - operation 5 brings a 'quoted as written' line into a live sheet of each exemplar (L7/allications/0.md:8);
        - operation 23 asks for "the owner's words as written", and both local commits quote the request of 11 November in full (autonomous@8257118:L8/L6/history/harmonization-2026-09-05.md:185; auditonomous@f2d5b37 at :178).

        Quoting in an L6 record is consistent with PR #19's own scope, which leaves the records "the words as written" (:524). The open point is the doubt at :514, and the live sheet line.

        The exemplars also name the owner in live text, for example autonomous@origin/main:README.md:3, "Research repository of Eric D. Martin."

        Missing decisions: whether the exemplars are to follow the agnostic wording at all, and whether the 11 November words go into the two records as written. Decision 7 asks only whether PR #19 is merged.
    - item 7
      - **severity**: medium
      - **gap**: A standing word of the owner from 17 October 2026 is absent from the report's standing rules, and the list of decisions does not ask whether a session-made, counted pass is the mirror 'Manually'.
      - **finding**: 7lm@origin/ccr-9391bd81-f2enmj:L8/L6/history/harmonization-2026-09-04.md:518 records, of 17 October: 'Earlier the same day, on another matter and bearing on this one: "I didn't want anything automated yet".' The sentence is on the PR #20, PR #19 and audit branches only (git grep 'automated yet': no hit on origin/main or the beta).

        On main the related rules are:
        - "All repos should mirror the 7lm. Manually." (REC:336)
        - "for now everything is HOA" (REC:376), HOA being human-only actions
        - 7lm@origin/main:L8/L6/7lm-field-guide.md:610: "Automating that review instead of doing it runs the risk the review exists to catch", and "Today the mirroring is by hand".

        The two local commits are authored and committed by Claude and describe their word sweep as made "by a pass with a count per phrase" (autonomous@8257118:L8/L6/history/harmonization-2026-09-05.md:191; auditonomous@f2d5b37 at :184) under a title that says "mirrored by hand" (:183, :176). The scaffold's own sweep was "a scripted pass with a count per phrase" (REC:498), so there is precedent.

        The same branch record shows that pushing waits on the owner's word: section 40 quotes "push them" (7lm@origin/ccr-9391bd81-f2enmj at :534).

        Missing from the report: the 17 October word among the standing rules; and a decision on whether these session-made commits count as the hand mirror or are a proposal for a person to apply. Decision 4 asks which mirror lands, not who may make it.
    - item 8
      - **severity**: medium
      - **gap**: The owner's gate names peering as well as the model. The report leaves the pinned binding under 'do not touch' and lists no decision on it, though the scaffold's guide lists rebinding as an open call and the mirror does nothing for peering.
      - **finding**: Open on main today:
        - 7lm@origin/main:L8/L6/7lm-field-guide.md:626-634, under "Open calls": "Rebinding the Autonomous definition in Auditonomous to its current path."
        - SPEC:958: "rebinding to a current version is the owner's act".
        - The binding record, auditonomous@origin/main:L7/peering/public/ingress/peer-1/object-1/0.md:10 and :13, still names `aybllc/autonomous:research/definitions/AUTONOMOUS.md` at commit `0504961`, a path from before the peer's 7LM layout.
        - The same sheet at :34: "Three files at HEAD still take a definition of *autonomous* from somewhere other than this binding".

        On the closed roadmap branch the same matter is decision D22 (BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:631), with three options: bind to c9076c3, [source text withheld from the public copy], or keep 0504961. Step S3 at :586 lists as not yet stable: "[source text withheld from the public copy]", and that the peer-3 hashes are unpinned.

        The mirror touches none of this. In the binding record the Auditonomous local commit changes only the boundary sentence (git diff 2165144 f2d5b37 on that file: one line). But it moves Autonomous's head past c9076c3, the commit one of D22's options names.

        Both exemplar betas add a second bound object instead of rebinding the first: autonomous@origin/beta/7lm-exemplar-autonomous:L7/peering/public/egress/peer-1/object-2/0.md and auditonomous@origin/beta/7lm-exemplar-auditonomous:L7/peering/public/ingress/peer-1/object-2/0.md.

        Missing decision: whether peering is stable enough to start, and whether the rebinding comes before or after the mirror and to which commit.
    - item 9
      - **severity**: medium
      - **gap**: Both exemplars' records leave open whether the binder's internal part belongs at publications or at L4 writing. The mirror moves the whole binder one level deeper, under a branch now defined as outward acts, and the report does not list the question.
      - **finding**: The open item stands in both records under owner decisions left open: autonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:80 and auditonomous@origin/main at :94, "`binder/internal/` at publications versus L4 writing".

        The publications sheet contradicts its own holdings. autonomous@origin/main:L7/publications/0.md:29 says the position does not hold "drafts stamped internal, empty release slots, and material that has not left". Line 33 lists as held the binder with its acquisition queue, its verification tools and a glossary "stamped DRAFT — INTERNAL". The binder's own sheet calls the tools "code as made (L4 by role)" (L7/publications/binder/0.md:27).

        After the mirror the container above it is the scaffold's allications sheet, which defines the family by acts: 7lm@origin/main:L7/allications/0.md:10, "Each is something the object does toward the outside, once, on a date, leaving a record that can be addressed afterwards." Nothing in either binder has left.

        The scaffold's precedent does not settle it. Its own publications/ held only its sheet when it moved (ls-tree origin/main L7/allications/publications: 0.md alone), and record section 25 says only that the folder moved as a tracked rename (REC:321).

        Moving the binder with its folder is the faithful physical mirror, and both local commits do it at 100% similarity. The decision that the move makes visible, whether internal/ goes to L8/L4/work/writing/ or stays, is the owner's and is not among the fourteen.
    - item 10
      - **severity**: medium
      - **gap**: The new record section, as specified in operation 23 and as written in both local commits, does not pin the scaffold commit that was mirrored and does not list what was declined. The model's guide asks for both.
      - **finding**: The guide describes how an update is meant to reach an adopter, 7lm@origin/main:L8/L6/7lm-field-guide.md:610: "The scaffold's update arrives, pinned to its hashes", and "what the person declines is listed in their HOA record rather than dropped without a trace". The mechanism is not built, but this is the model's statement of what an adopter records.

        No pin. The new sections name the scaffold only by "version of 20 September 2026" (autonomous@8257118:L8/L6/history/harmonization-2026-09-05.md:187; auditonomous@f2d5b37 at :180). The only commit ids in them are the exemplars' own branches (e64b382; 714480d, 9259c18). Neither c9dc061 nor 2e5a6d6 appears. That version string does not identify one text: the beta changes six passages of the specification and keeps the same string, as the report itself notes. The checklist's precondition names c9dc061; operation 23 does not ask for it in the record.

        No list of what was declined. Both sections say only that the scaffold's sheets "say things these sheets do not" (:207, :200). Lines of the scaffold's root sheets that the mirrored sheets do not take, found by comparing exports:
        - 7lm@origin/main:L7/0.md:13, the FIRST-is-0 bullet
        - :14, the name as design
        - :18, the packet reading
        - :159, the owner's heading of 5 October about private repositories
        - :192, the note "Many intelligences at one face"
        - 7lm@origin/main:L8/0.md:10 and :22

        The exemplars' L7/0.md keeps the same link line the heading at :159 was written for (autonomous@8257118:L7/0.md:161).

        Whether those are declined or deferred is the owner's design choice, and the record is where the guide says it is stated.
    - item 11
      - **severity**: low
      - **gap**: After the listed operations, live files in both exemplars still name paths of the layout before 5 September 2026. Three of them are binder files the mirror moves untouched. The verify step and the do-not-touch list are both silent on them.
      - **finding**: These are not L7 names of 20 September, so the verify counts stay at zero, but the task's test, whether any live file still names a former path, finds them. The register they name stands at L7/provenance/sources/LEDGER.md; autonomous@origin/main:L8/L6/0.md:79 says so: "The pointer register formerly at `uso/l6/LEDGER.md` is now `L7/provenance/sources/LEDGER.md`."

        Autonomous (origin/main; the same lines on 8257118 at the moved paths):
        - L7/publications/binder/press-kit/README.md:18: "[source text withheld from the public copy]:23
        - L7/provenance/sources/datasets-LEDGER.md:21
        - L8/L4/work/writing/MANUSCRIPT.tex:50 and :79, the manuscript placeholder

        Auditonomous:
        - L7/publications/binder/README.md:11, and :23 naming `manuscripts/definitions/AUDITONOMOUS_DEFINITION.md`
        - L7/publications/binder/press-kit/README.md:18
        - L8/L2/formal-mathematics/FORMULAS_LEDGER.md:23
        - L7/provenance/sources/datasets-LEDGER.md:21

        Leaving them is consistent with each repository's own rule. The binder sheets say the files "are not rewritten" (L7/publications/binder/0.md:8 in both), and the rename pass rewrote path references in sheets and three named files only (autonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:175).

        It matters for the QA that follows. The press-kit README is the release checklist, and the roadmap on the closed branch relies on it as a gate for the book (BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:28). The checklist and the manuscript placeholder both send the reader to a register path that does not exist.

        Checked and clean: the moved files hold no relative link that the extra directory level breaks. The two Python tools already anchor to pre-2026-08-14 paths and, by the binder sheet, "cannot run at HEAD".
    - item 12
      - **severity**: low
      - **gap**: Decision 11 lists three specification lines that go out of date once the exemplars land. The same statements stand in the generated rendering, and two other statements about the exemplars are already untrue.
      - **finding**: The rendering. 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.docx, text extracted from word/document.xml: "not yet mirrored" occurs twice and "restrictions/ (the position" once. Record section 37 says the rendering is patched in step with the Markdown (REC:500), so a change to SPEC:938, :950 and :958 is a change to both files.

        Already untrue, before and after the mirror:
        - SPEC:934, of both exemplars: "Every directory has its 0.md, headed by its path." Six folders in Autonomous and twelve in Auditonomous have none. The same sentence is in the rendering, once.
        - 7lm@origin/main:L8/L6/7lm-field-guide.md:474, after "every folder carries one": "Both exemplar repositories do exactly this."

        Becomes true once the exemplars land: 19 scaffold sheets say "The exemplar of this position is the sheet at the same path in `aybllc/autonomous` and `aybllc/auditonomous`" (for example 7lm@origin/main:L7/0.md:241). No allications or governance sheet carries that section, so nothing there points at a path the exemplars lack.

        Checked and clean: outside the specification and the one history note at L7/allications/0.md:38, no live scaffold file on main names a former path (git grep for 'L7/publications', 'governance/restrictions', 'restrictions/', history, retired and in/ excluded).
    - item 13
      - **severity**: low
      - **gap**: One exemplar branch with a commit of its own is not accounted for, the state of the scaffold clone is not stated, and one line of the do-not-touch list is inexact.
      - **finding**: Branch. auditonomous@origin/claude/research-move (55541d7, 2026-09-06) is one commit ahead of main and 13 behind: 39 files on `USO/` and `common/` paths. The repository's record explains it (auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:107): "built as PR #21 here and closed unmerged when the words below superseded it". A test merge with main conflicts throughout. The mirror does not change that, but the branch belongs beside the two no-deletion-fix branches in decision 13. Every other remote branch of the two exemplars not named in the report is an ancestor of main (rev-list origin/main..ref: 0).

        Clone state, read from refs only. In /home/user/7lm, HEAD is refs/heads/ccr-9391bd81-f2enmj at c9638a9, the PR #20 branch, and refs/heads/main is 2e5a6d6, two commits behind origin/main. That checkout has no L8/L6/in/7lm-layer-lists.md and has the field guide retired, so it is not the model of record. L7/, .github/ and README.md are identical between c9638a9 and origin/main (git diff --stat: empty), so sheets copied from that checkout equal main's. In both exemplar clones HEAD is the local branch that holds the mirror commit.

        Inexact line. The do-not-touch list says of L8: "Only path references change, in six L8 sheets in Autonomous and five in Auditonomous." In both, L8/L6/0.md:80 also takes a word sweep under operation 18, "access, and restrictions" to "access, and controlled conditions".

        Checked and clean: the live canonical sheets that the report's greps exclude by path (L8/L6/history/0.md, L8/L6/retired/0.md and each retired set's root sheet) carry no former name or swept phrase in either exemplar.
  - **readers**
    - item 1
      - **key**: spec-A
      - **facts**: 66
      - **checklist**
        - item 1
          - **step**: 1. Root
          - **detail**: Root holds README.md, L7/, L8/ and nothing else except non-layer infrastructure: .github/workflows/integrity.yml and optionally .gitignore. The scaffold's own main root has no .gitignore.
          - **locator**: /home/user/7lm@origin/main:SPEC:281
        - item 2
          - **step**: 2. README
          - **detail**: README.md is a start page only: what the repository is, the reading order (L7/0, L8/0, then every sheet), the root, where the prior README is.
          - **locator**: /home/user/7lm@origin/main:SPEC:281
        - item 3
          - **step**: 3. L7 direct branches
          - **detail**: Exactly four: L7/provenance/, L7/governance/, L7/peering/, L7/allications/. There is no L7/publications/ at the top of L7.
          - **locator**: /home/user/7lm@origin/main:SPEC:46,206-240
        - item 4
          - **step**: 4. L7/provenance
          - **detail**: Positions prior-art, sources, lineage, authority.
          - **locator**: /home/user/7lm@origin/main:SPEC:207-211
        - item 5
          - **step**: 5. L7/governance
          - **detail**: Positions copyright, licensing, patents, permissions, access, controlled. The sixth is named controlled, not restrictions.
          - **locator**: /home/user/7lm@origin/main:SPEC:212-218
        - item 6
          - **step**: 6. L7/peering
          - **detail**: private/ and public/, each with ingress/peer-1/object-1 and egress/peer-1/object-1. Peers and objects are counted from 1.
          - **locator**: /home/user/7lm@origin/main:SPEC:219-233,66
        - item 7
          - **step**: 7. L7/allications
          - **detail**: Positions publications, applications, communications, specifications, notifications, participations.
          - **locator**: /home/user/7lm@origin/main:SPEC:234-240
        - item 8
          - **step**: 8. L8 interior
          - **detail**: L8/ holds L6, L5, L4, L3, L2, L1, L0 as flat siblings (uppercase L). L6/{history, retired}; L5/research/{lanes, review, findings}; L5/institution/{peers, undergraduates}; L4/work/{writing, experiments, computation}; L3/engineering-mathematics/{approximation, uncertainty, tolerances}; L2/formal-mathematics/{relations, operators, proofs}; L1/state-space; L0/{universality, pedagogy, epistemic, ontology, semantics/definitions}.
          - **locator**: /home/user/7lm@origin/main:SPEC:241-276,154
        - item 9
          - **step**: 9. Sheets
          - **detail**: Every directory carries 0.md; it first identifies the directory and its path, then gives the semantic description. All 71 canonical positions must be sheeted. Sheets inside a retired set under L6/retired/<set>/ keep their prior headings and are not checked.
          - **locator**: /home/user/7lm@origin/main:SPEC:21,283,285; /home/user/7lm@origin/main:.github/workflows/integrity.yml:31-61
        - item 10
          - **step**: 10. Keep unused positions
          - **detail**: An unused canonical branch stays in place, empty of content but sheeted; the tree is not reduced.
          - **locator**: /home/user/7lm@origin/main:SPEC:107,199,279
        - item 11
          - **step**: 11. L0 content
          - **detail**: L0/semantics/definitions holds only definitions the object itself authored. An external definition is bound at L7 peering ingress and is not copied into L0 to populate it.
          - **locator**: /home/user/7lm@origin/main:SPEC:327,339,341
        - item 12
          - **step**: 12. Machine metadata
          - **detail**: Create no metadata files. Main says every directory carries metadata, but none exists in the scaffold tree; the unmerged beta makes it conditional on machine instructions being enabled.
          - **locator**: /home/user/7lm@origin/main:SPEC:21; /home/user/7lm@origin/beta/common-contracts-r1-r6:SPEC:21
        - item 13
          - **step**: 13. Integrity check
          - **detail**: The exemplar's .github/workflows/integrity.yml should carry the scaffold's canonical list (controlled, allications and its six positions), otherwise G-003 will test the former names.
          - **locator**: /home/user/7lm@origin/main:.github/workflows/integrity.yml:47-59
      - **open_questions**
        - The L7 directory prose/why table (L7 and every position beneath it) is outside lines 1-520; it sits in the L7 sheet starting at line 729. It was not read here and needs the agent covering lines 521-1003.
        - Both 'Not yet as stated' paragraphs (lines 950 and 958) and the whole 'Exemplars as instantiated' section (from line 926) are outside this range, so what the specification says the exemplars carry today is not settled here.
        - The owner says the model changed, but the specification on origin/main is identical to its 2e5a6d6 state and still dated 20 September 2026; the only main change since is the added L8/L6/in/7lm-layer-lists.md. Whether 'changed' refers to that file, to the unmerged beta (R1-R6), or to the 20 September restructure the exemplars never received is not answerable from this file.
        - Is L8/L6/in/ part of the model the exemplars must mirror? It exists on main with a sheet but is absent from the drawn tree, from the integrity check's 71 positions, and from the specification text.
        - Should the exemplars be matched to origin/main's wording or to the beta's? The beta's four in-range changes alter meaning (metadata conditional; exact tagged reference may reach receiving L0) but no path, name or count, so the physical mirror is the same either way.
        - The .gitignore named in the root rule is not present in the scaffold at origin/main; whether an exemplar should carry one is left open by 'may hold'.
        - The exact sheet heading form '# <path>/' is stated by integrity.yml, not by lines 1-520 of the specification, which say only that the sheet first identifies the directory and its path (line 283 gives the looser form '/data/location/object').
    - item 2
      - **key**: spec-B
      - **facts**: 68
      - **checklist**
        - item 1
          - **step**: 1. File the manuscript as work at L4
          - **detail**: Drafts, document files and the production of the book artifact stand at L8/L4/work/writing/ ('Directory for writing and document production as performed work'). The act and the file are L4, nothing more.
          - **locator**: 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:566, 591, 611
        - item 2
          - **step**: 2. File the research argument, claims and thesis statements at L5
          - **detail**: The research argument and 'manuscript meaning' are L5. Research claims and thesis statements belong at L8/L5/research/lanes/ or the corresponding L5 research artifact. A claim must be no broader than the evidence, and research meaning must be kept distinct from L4 writing and L7 release.
          - **locator**: 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:591, 641, 988
        - item 3
          - **step**: 3. Use review/ as the catch-all and lanes/ as the working position
          - **detail**: Everything awaiting the owner's review lands at L8/L5/research/review/; set-aside material stays there labelled PARKED; what the owner takes up moves to L8/L5/research/lanes/ and back if set down; finished work is filed at its layer; nothing is deleted; no new directory is made for this.
          - **locator**: 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:679
        - item 4
          - **step**: 4. Keep review and findings apart
          - **detail**: L8/L5/research/review/ holds review, criticism, audit and qualification of claims; L8/L5/research/findings/ holds findings that may responsibly be stated. Raw L4 output is not a finding.
          - **locator**: 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:665-666
        - item 5
          - **step**: 5. Put experiment, computation, code and data at their layers
          - **detail**: Executed experiments, raw work product, collected data, executed code and run outputs are L4 (work/experiments/, work/computation/); engineering method, precision and tolerance L3; exact relations and proofs L2; state categories L1; interpretation L5; external source/lineage L7 provenance.
          - **locator**: 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:592, 594, 595
        - item 6
          - **step**: 6. Keep internal history at L6 and never treat git as the record
          - **detail**: Internal version, correction, failure and supersession history is L8/L6/history/; retired or superseded states and bindings go to L8/L6/retired/. Git records change events; the L6 record must carry the scientific relations and decisions.
          - **locator**: 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:591, 716-717, 721
        - item 7
          - **step**: 7. Enumerate before deleting
          - **detail**: A superseded file is deleted only after every part of it is enumerated, in the record at L8/L6/history/, as standing elsewhere. What integrity needs reconstructable (the owner's authored documents, prior rule texts, error records) is retired, not deleted.
          - **locator**: 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:723, 998
        - item 8
          - **step**: 8. Release only at the desk
          - **detail**: A released publication object stands at L7/allications/publications/; provenance and public/legal governance stay separately addressable at L7/provenance/ and L7/governance/. Exposure never raises scientific maturity.
          - **locator**: 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:803, 872, 918
        - item 9
          - **step**: 9. Take the definition of autonomous only through the binding
          - **detail**: Auditonomous binds the Autonomous definition at L7/peering/public/ingress/peer-1/object-1/, reference-only, NO EDIT and NO DELETE; it authors only its own local delta at L0; an upstream change means a new binding, and rebinding is the owner's act.
          - **locator**: 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:823-837, 936, 958
        - item 10
          - **step**: 10. Mirror the L7 names the specification says the exemplars lack
          - **detail**: Per the specification, both exemplars still carry publications/ as a direct L7 branch and governance/restrictions/; the model's names are L7/allications/publications/ (with applications, communications, specifications, notifications, participations as siblings) and L7/governance/controlled/. Confirmed against both exemplar mains by ls-tree. The specification does not itself give the order of moves; it only states the target tree.
          - **locator**: 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:747-783, 950, 958
        - item 11
          - **step**: 11. Keep copyright in one place when mirroring
          - **detail**: governance/copyright/ states every copyright or licence condition once; governance/licensing/ and governance/controlled/ point to it. In the exemplars the pointer currently sits at restrictions/, which the specification says it now names controlled/.
          - **locator**: 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:879, 938
        - item 12
          - **step**: 12. Treat scales and status ladders as written L4 objects with L5 meaning
          - **detail**: On main: a scale, ladder or status vocabulary as written is L4, its meaning L5, and it is not L1 or L2; a review-status ladder is L5 governance, not the L0 epistemic rail. The unmerged beta narrows this and permits separately declared L1 values and L2 relations, so which wording governs depends on whether the beta is adopted.
          - **locator**: 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:681; 7lm@origin/beta/common-contracts-r1-r6:same path:683
      - **open_questions**
        - The specification file did not change on main between 2e5a6d6 and c9dc061. If the owner's 'its changed' refers to main, the change is in other files (PR #21 and whatever else landed), which is outside this scope; if it refers to the unmerged beta R1-R6 corrections, they are not yet the model of record. Which is meant was not settled here.
        - L8/L6/in/ exists in the scaffold tree and in the L6 layer sheet (described as optional) but is absent from the specification's L6 tree. Whether it is one of the canonical positions the exemplars must carry, or optional and to be left out, is not stated in the specification.
        - The beta leaves the Exemplars section untouched, so on every scaffold ref the specification still says the exemplars' L7 restructure 'is not yet mirrored'. Once the exemplars are brought into step those two 'Not yet as stated' sentences (lines 950, 958) and the 'restrictions/' wording at line 938 become untrue; who updates them and when is not stated.
        - The specification's counts for the exemplars (six lanes and seven findings in Autonomous; two lanes, two reviews, three findings, 62 pointer rows in Auditonomous; a 450-entry capture register) were not verified against the exemplar trees; only the existence of the cited paths and the L7 branch names was checked.
        - The specification says the Auditonomous binding names the peer path research/definitions/AUTONOMOUS.md at commit 0504961 and that three files still take a definition of autonomous from elsewhere. Neither the binding record nor those three files were read here.
        - The Harmonization Record's inherited-terms table has no row for the 20 September 2026 renames (publications -> allications/publications, restrictions -> controlled). Whether that omission is deliberate (the history file carries it) was not determined; L8/L6/history/specification-history.md was not read in this scope.
        - The specification does not describe the CI check's three rules (G-001 to G-003) or the count of 71 positions; those must come from .github/workflows/integrity.yml itself, which was not read in this scope.
    - item 3
      - **key**: record-A
      - **facts**: 57
      - **checklist**
        - item 1
          - **step**: 1. The root is canonical
          - **detail**: The root holds README.md, L7/, L8/, .github/ and .gitignore, and nothing else. .gitignore is permitted, not required. Exactly one interior container. Enforced by G-002. Standing for every 7LM repository.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:121, 123 (§10); :186 (§15); 7lm@origin/main:.github/workflows/integrity.yml:17-29
        - item 2
          - **step**: 2. The interior is L8/, the layers L8/L0/ to L8/L6/, uppercase
          - **detail**: USO/ is L8/; l0-l6 are L0-L6. The term USO stays as the name of what L8 holds. L7/ and L8/ are siblings at the root. Every repository (done in all three on 2026-09-12).
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:170-172 (§14); :156 (§12)
        - item 3
          - **step**: 3. Every directory's sheet is headed by its path; every canonical position has a sheet
          - **detail**: A sheet is 0.md with first line '# <path>/'. As of section 23 the canonical list has 57 positions, including L7/publications and L7/governance/restrictions (not the 71 of today's main). Sheets below the root of a retired set are not checked. Enforced by G-003; a directory without a sheet beneath a canonical position is reported, not failed.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:121 (§10); 7lm@68c550e:.github/workflows/integrity.yml:canon list
        - item 4
          - **step**: 4. No unresolved conflict markers
          - **detail**: G-001. Every repository.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:121 (§10)
        - item 5
          - **step**: 5. One CI check, the same in every 7LM repository
          - **detail**: .github/workflows/integrity.yml carrying G-001, G-002, G-003 and the report step. It is repository infrastructure, not a layer; it reads the tree and moves nothing; it enforces integrity and must never enforce no-deletion. The layout holds no metadata, hooks or movers.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:119-123 (§10); :152 (§11)
        - item 6
          - **step**: 6. The README is the start, not the documentation
          - **detail**: README states what the repository is, the reading order (README, then L7/0.md, then every directory's 0.md), the root, and where prior READMEs are, and nothing else. The documentation is the sheets with the specification.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:129-131 (§11)
        - item 7
          - **step**: 7. Sheets say what is; the record says what happened
          - **detail**: No dates, owner quotations or narrative of moves, retirements or deletions in a sheet; each sheet states what its directory is, holds and does not hold, with at most one pointer to the record. History lives in the record at L8/L6/history/.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:162-164 (§13)
        - item 8
          - **step**: 8. Copyright in one place
          - **detail**: The one place to look for copyright is L7/governance/copyright/0.md, named in the README; copyright is not spoken about elsewhere.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:97 (§6)
        - item 9
          - **step**: 9. research/review/ is the catch-all; research/lanes/ the working position
          - **detail**: Everything awaiting the owner's review lands at L8/L5/research/review/; set-aside items stay there labelled PARKED; what is taken up moves to lanes/; finished work is filed at its layer; nothing is deleted; no new position is added to the canonical tree.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:103 (§7)
        - item 10
          - **step**: 10. The tree is silent on access
          - **detail**: No sheet says who may write where; L7/peering/0.md describes the register's position only. No queue vocabulary (orphan, foster, results, delete) and no directory for any reserved term (found, caught, naught, regress, origidity, certainty, intolerance, corpus in the broad sense, semantic-formulas).
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:103 (§7); :75-83 (§3)
        - item 11
          - **step**: 11. No CLAUDE.md
          - **detail**: The session rules file is held off on the owner's word; still listed open at section 14.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:103 (§7); :178 (§14)
        - item 12
          - **step**: 12. First is always 0; peers from 1
          - **detail**: The seven layers are L0 to L6; L7 is numbered and not a layer; L8 is a count, not a ninth position. Peers and objects at L7/peering/ are counted from 1 (peer-1/, object-1/).
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:107 (§8); :194 (§16)
        - item 13
          - **step**: 13. Deletion only after enumeration; retirement only for scientific memory
          - **detail**: A superseded file is deleted once every section is enumerated in the record as standing elsewhere. L8/L6/retired/ holds only states that must stay reconstructable: the owner's authored documents, rule texts of a prior layout, error records. L6 is not a copy of git.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:150-152 (§11)
        - item 14
          - **step**: 14. External provenance at L7, internal memory at L6
          - **detail**: L8/L6/ holds history/ and retired/; there is no L6 provenance directory; external source, authority, prior art and lineage are at L7/provenance/. Sources are served from aybllc/l6 by pointer row, never by copy, and that archive is not edited from a consuming repository (a rule of this program).
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:87 (§4); :72 (§2); 7lm@origin/main:L8/L6/history/sheets-2026-09-07.md:121
        - item 15
          - **step**: 15. Records and retired sets are never rewritten
          - **detail**: In any rename, the bodies of the records at L8/L6/history/ and everything below the root of each retired set stay as written; former locations named in current sheets stay as written; older records are read with the rule USO/lN -> L8/LN. Owner quotations are never tidied.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:174-176 (§14); :291 (§23)
        - item 16
          - **step**: 16. The tree does not move for the packet reading
          - **detail**: L7/ and L8/ stay siblings; L8/ holds L0 to L6; the envelope is a reading, not a change. Sheets that quote the canonical position lines 'L7 = Desktop' and 'L8 = USO, the bounded scientific object's interior: the research packet on the desk' quote them verbatim.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:269 (§22); :283, 293 (§23)
        - item 17
          - **step**: 17. The specification controls
          - **detail**: Where a sheet, guide or drawing differs from the specification (version of 13 September 2026 as of section 23), the specification controls. The exemplar's own record carries a section for each pass applied to it.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:188 (§15); :285 (§23); :172 (§14)
        - item 18
          - **step**: 18. Auditonomous only: one source for the definition of autonomous
          - **detail**: Auditonomous binds the definition of autonomous from Autonomous's bound L0 object and from nowhere else.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:73 (§2); 7lm@origin/main:L8/L6/history/sheets-2026-09-07.md:97
        - item 19
          - **step**: 19. NOT required of an exemplar by sections 1-23
          - **detail**: The field guide, the plate sheet (.py and .html), FIRST_IS_ALWAYS_0.md, specification-history.md and the specification itself are scaffold files. Section 16 says the exemplars carried no statement on the peer count; section 23 names only scaffold files as carrying the packet reading.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:194 (§16); :229 (§19); :287-289 (§23)
        - item 20
          - **step**: Result of checking the exemplars against this list
          - **detail**: Both exemplars' origin/main satisfy steps 1-5 and 11 by tree check (root, L8/L0-L6, 57-position integrity.yml, no CLAUDE.md), carry L7/governance/copyright/0.md, a README that says it is the start, and the rename-pass record section. They stand in step with the scaffold as of section 23; what separates them from today's scaffold lies in sections 24-37.
          - **locator**: autonomous@origin/main:.github/workflows/integrity.yml:76-78; auditonomous@origin/main:.github/workflows/integrity.yml:48-50; autonomous@origin/main:README.md:5; auditonomous@origin/main:README.md:5
      - **open_questions**
        - Whether an exemplar's L8/0.md and L7/0.md must carry the packet reading. Section 23 propagated it to scaffold sheets only and names no exemplar file; neither exemplar main carries it (grep for envelope, glue, connector in L8/0.md and L7/0.md of both: not found in that sense). Sections 1-23 do not say it is required of exemplars; a later section may.
        - Whether FIRST_IS_ALWAYS_0.md should exist in an exemplar. Section 8 files it as 'a locally authored definition of this object' (the scaffold); it is not found in either exemplar's origin/main tree. Not settled in scope.
        - The fate of 'the two 0-byte files in Auditonomous', listed open in section 9 (line 115) and absent from section 14's open list (line 178). No section in 1-23 says they were resolved; not found.
        - The other items section 14 leaves open (the home of Autonomous Theory; rebinding the Autonomous definition to a current version; the queue's rule texts at L8/L6/retired/layout-2026-09-06/ in each exemplar; the held-off CLAUDE.md) are not closed anywhere in sections 15-23. Their later status lies outside this scope.
        - Section 22's owner message is cut off ('So redo the one plate l eight envelope with'). The ruling that the tree does not move is the record's reading of it. The same quotation, without the cut-off sentence, is entered into the specification in section 23, which supports the reading but is not a fresh owner statement.
        - sheets-2026-09-07.md lines 37, 99 and 397 are truncated fragments. I did not compare them with the sheets as they stood before commit 1f7013c, so I cannot say whether they are faithful clause-level cuts or extraction faults.
        - The section 2 chronology lists a 2026-08-24 event (3bdbe4b) before a 2026-08-23 event (1edf4c7). Whether a date is wrong or the order is deliberate is not stated.
    - item 4
      - **key**: record-B
      - **facts**: 69
      - **checklist**
        - item 1
          - **step**: 0. Before anything: the owner's word
          - **detail**: Nothing changes without asking (section 36), and the exemplars are mirrored by hand, by a person, when the owner judges the scaffold close (section 26). Each repository records its own pass at its own L8/L6/history/; do not copy the scaffold's L6 history into an exemplar (section 31).
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:482, :346, :402
        - item 2
          - **step**: A1. Move publications (tracked rename)
          - **detail**: Move L7/publications/ to L7/allications/publications/ as a tracked rename so history follows. In the moved sheet change line 1 to `# L7/allications/publications/` and the Path line to `L7/allications/publications/`.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:321; commit 606d4b3 rename L7/{ => allications}/publications/0.md
        - item 3
          - **step**: A2. Move restrictions (tracked rename)
          - **detail**: Move L7/governance/restrictions/ to L7/governance/controlled/ as a tracked rename. In the moved sheet change line 1 to `# L7/governance/controlled/`, the Path line to `L7/governance/controlled/`, and the Object line to "Directory for restrictions and other conditions that constrain external disclosure, use, transfer, or handling."
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:321; commit 606d4b3 rename L7/governance/{restrictions => controlled}/0.md
        - item 4
          - **step**: A3. Write the container sheet
          - **detail**: Create L7/allications/0.md, first line `# L7/allications/`. Scaffold Object line: "Directory for the bounded object's outward acts: publications, applications, communications, specifications, notifications, and participations."
          - **locator**: 7lm@origin/main:L7/allications/0.md:1-4
        - item 5
          - **step**: A4. Write five sibling sheets
          - **detail**: Create 0.md at L7/allications/applications/, communications/, specifications/, notifications/, participations/, each headed by its own path. Spell `notifications` (not the owner's `notificattions`); keep `allications` as written. L7 goes from 29 to 35 sheets.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:321; 7lm@origin/main:L7/allications/*/0.md
        - item 6
          - **step**: A5. Redraw L7/0.md
          - **detail**: Tree: `controlled/0` under governance; `allications/0` with six children in place of `publications/0`. Table: governance/restrictions/ row becomes governance/controlled/ ("...restrictions and other conditions..." / "Keeps what is controlled explicit..."); the publications/ row becomes seven rows (allications/ and its six children). Sentence: "four owned external relations: provenance, governance, peering, and allications — the outward acts, of which publication is one."
          - **locator**: git -C /home/user/7lm show 606d4b3 -- L7/0.md; 7lm@origin/main:L7/0.md
        - item 7
          - **step**: A6. Specification (scaffold only)
          - **detail**: Version 20 September 2026. Canonical line now: "Canonical direct L7 branches are L7/provenance/, L7/governance/, L7/peering/, and L7/allications/." Four-relations sentence changed; both trees redrawn; seven table rows in place of publications/; governance/controlled/ row; the two copyright clarifications point at controlled/. Neither exemplar main carries a specification file.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:323
        - item 8
          - **step**: A7. Path sweep in live files
          - **detail**: Replace `L7/publications/` with `L7/allications/publications/`; `L7/governance/restrictions/` with `L7/governance/controlled/`; and in any quotation of the canonical line, "and L7/publications/." with "and L7/allications/." Scaffold files touched: L7 sheets of peering, governance, provenance; L8/L6/0.md; L8/L4/work/0.md; L8/L4/work/writing/0.md; L8/L5/research/findings/0.md; the field guide. The record gives no per-string count (26 live files after correction).
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:325, :506; git show --word-diff 606d4b3
        - item 9
          - **step**: A8. CI canon list, first change
          - **detail**: In .github/workflows/integrity.yml: `L7/governance/restrictions` becomes `L7/governance/controlled`; the entry `L7/publications` becomes `L7/allications L7/allications/publications L7/allications/applications L7/allications/communications L7/allications/specifications L7/allications/notifications L7/allications/participations`.
          - **locator**: git -C /home/user/7lm show 606d4b3 -- .github/workflows/integrity.yml
        - item 10
          - **step**: A9. Leave the records alone
          - **detail**: Do not move a path inside any historical record: the repository's own L8/L6/history/ files and dated rows, reserved-terms lists, L8/L6/history/sheets-2026-09-07.md, everything under L8/L6/retired/, and the frozen extract at L8/L6/in/.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:327
        - item 11
          - **step**: A10. Check and record
          - **detail**: Run the one CI check: no conflict markers, canonical root, [source text withheld from the public copy] including the seven new ones. Record the pass in the repository's own L6 history. (Scaffold only: the .docx was patched by XML surgery.)
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:331
        - item 12
          - **step**: B0. Sweep scope
          - **detail**: Live text only, scripted, with a count per phrase. Exclude L8/L6/history/, L8/L6/retired/, L8/L6/in/, the filed exemplar page (in the scaffold, L7/provenance/prior-art/uha-ommp-exemplar.html; the sheet prior-art/0.md was swept), and every quotation of the owner's words.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498
        - item 13
          - **step**: B1. Phrase pair, 37 in the scaffold
          - **detail**: "peering, and publication state" -> "peering, and allications — the outward acts, of which publication is one"
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498
        - item 14
          - **step**: B2. Phrase pair, 11
          - **detail**: "the L7 publications branch" -> "L7/allications/publications/"
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498
        - item 15
          - **step**: B3. Phrase pair, 3
          - **detail**: "peering, and publications become addressable" -> "peering, and allications become addressable"
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498
        - item 16
          - **step**: B4. Phrase pair, 3
          - **detail**: "publications and release identity" -> "allications: the outward acts, of which publication is one"
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498
        - item 17
          - **step**: B5. Phrase pair, 10
          - **detail**: "access, restrictions" -> "access, controlled"
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498
        - item 18
          - **step**: B6. Phrase pair, 2
          - **detail**: "access, and restrictions" -> "access, and controlled conditions"
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498
        - item 19
          - **step**: B7. Phrase pair, 1
          - **detail**: "licensing and restrictions folders" -> "licensing and controlled folders"
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498
        - item 20
          - **step**: B8. Folder name, 2
          - **detail**: `restrictions/` as a folder name -> `controlled/` (scaffold: L7/governance/0.md and L7/governance/copyright/0.md, "`licensing/` and `restrictions/` stay admissible").
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498; git grep -n 'restrictions/' bbb04dd~1
        - item 21
          - **step**: B9. Two quoted cells in L7/governance/controlled/0.md
          - **detail**: "Directory for restrictions that constrain external disclosure, use, transfer, or handling." -> "Directory for restrictions and other conditions that constrain external disclosure, use, transfer, or handling."; "Keeps restrictions explicit and machine-addressable without redefining the underlying research." -> "Keeps what is controlled explicit and machine-addressable without redefining the underlying research."
          - **locator**: git -C /home/user/7lm show bbb04dd -- L7/governance/controlled/0.md
        - item 22
          - **step**: B10. Plate label (2) and Source field (scaffold only)
          - **detail**: In the generator and regenerated sheet: "provenance &#183; governance &#183; peering &#183; publications" -> "... &#183; allications"; Source "version of 13 September 2026" -> "version of 20 September 2026". Neither exemplar main carries a plate sheet.
          - **locator**: git -C /home/user/7lm show bbb04dd -- L8/L0/pedagogy/7lm-plate-sheet.py
        - item 23
          - **step**: B11. README reading order
          - **detail**: "`L7/0.md` — the desk, the forward face: provenance, governance, peering, publications." -> "... provenance, governance, peering, allications."
          - **locator**: git -C /home/user/7lm show bbb04dd -- README.md
        - item 24
          - **step**: B12. Leave these words standing
          - **detail**: "restrictions" where it names a kind of condition (for example "apply public/legal permissions and restrictions"), and "execution restrictions" in the L2 machine-metadata cell. They are not position names.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498
        - item 25
          - **step**: B13. Sheets beyond the sweep (scaffold)
          - **detail**: L7/0.md: add the author note "Many intelligences at one face"; communications Why cell verbatim from the specification; introductory sentence no longer claims all is quotation. L7/allications/notifications/0.md Object line: "Directory for notices the object issues outward." L8/L6/0.md: describe what in/ holds.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:504
        - item 26
          - **step**: B14. CI canon list, second change
          - **detail**: Add one line of eight positions: L7/peering/private/ingress/peer-1, .../peer-1/object-1, L7/peering/private/egress/peer-1, .../object-1, L7/peering/public/ingress/peer-1, .../object-1, L7/peering/public/egress/peer-1, .../object-1. Total 71. Comment: "Retired sets under L6/retired/ (l6/retired/ before the rename pass)".
          - **locator**: 7lm@origin/main:.github/workflows/integrity.yml:33, :50
        - item 27
          - **step**: B15. Do not change
          - **detail**: The tree. Every sheet's first line. The owner's words, anywhere. The historical records. No version string change in the scaffold's specification.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:500, :508
        - item 28
          - **step**: C. Do NOT apply (recorded only)
          - **detail**: Section 32: 1.md and base dirs. Section 33: plate assignments, a blank lineage sheet, the name allics, a separate definitions directory, the L6 library picture. Section 34: the L1 plate, the dependency test, any "God rules" term, the two candidate specification clarifications. Section 35: the picture book. Also not built: the push mechanism (section 27) and the one-click republishing (section 29). Section 37 parks 1.md.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:418, :444, :459, :478, :494
      - **open_questions**
        - Section 25 says 28 live files were changed and section 37 corrects this to 26. Commit 606d4b3 lists 37 paths (6 created, 2 renamed, 29 modified). The record does not say which files the 26 counts, so the number cannot be reproduced exactly.
        - Section 37 says the Boundary Rule sentence is in "thirty-six live sheets"; git shows 36 occurrences in 35 sheets. Whether the record meant occurrences is not stated.
        - The scaffold's specification on main still states (lines 938, 950, 958) that the exemplars carry publications/ and governance/restrictions/ and that the restructure "is not yet mirrored". Once the exemplars are mirrored those three statements become untrue. Changing them changes the scaffold and needs the owner's word (section 36); the record does not say who updates them or when.
        - The exemplars' sheets may not quote the specification in the same words as the scaffold's sheets. The sweep's counts (37, 11, 3, 3, 10, 2, 1, 2) are the scaffold's; the exemplars' own counts per phrase, split between live and historical text, were not established in this scope.
        - Whether every one of the eight peer-1/object-1 positions the CI list now requires has a sheet in each exemplar was not checked here (outside scope). The scaffold's CI would fail an exemplar that lacks one.
        - The beta's two 2 November sections assert "the owner's approval of R1–R6" and an approved "exemplar construction package" without quoting the owner, and the harmonization record carries no section for that work. Whether the beta is to be treated as part of the model to mirror is the owner's call; main does not contain it.
        - The second beta section names no actor; only the first names Codex. Whether the same task produced both is not stated in the file.
        - Section 27 leaves unresolved whether the sentence recommendation reaches the desk (L7) and the interior root. Section 30 leaves unresolved where a person keeps the list of blank sheets until the collecting document exists.
        - Section 33 leaves two questions for the owner: whether the scaffold's own lineage sheet is to be blank or blanked on push, and where the one home for definitions sits. Both wait; neither is to be applied.
        - Section 29: whether "Delarers choice" introduces "declarer" as a term is recorded as not settled.
    - item 5
      - **key**: sheets-L7
      - **facts**: 85
      - **checklist**
        - item 1
          - **step**: 1. L7 must contain exactly four direct branches plus its own sheet
          - **detail**: L7/0.md, L7/provenance/, L7/governance/, L7/peering/, L7/allications/. No L7/publications/ and no L7/governance/restrictions/ (both former names). Every directory under L7 carries a 0.md whose first line is '# <path>/' with trailing slash.
          - **locator**: 7lm@origin/main:L7/0.md:16,56-92
        - item 2
          - **step**: 2. provenance/: five sheets
          - **detail**: L7/provenance/0.md and children prior-art/, sources/, lineage/, authority/, each with 0.md. The scaffold also keeps sources/source-ledger.md (title, one sentence, eight-column header: Source ID | Source and locator | Issuer / owner | Exact version | Retrieved | Declared scope | Relevant artifact or layer | Status / notes). The ledger and the prior-art HTML are not among the canonical sheeted positions.
          - **locator**: 7lm@origin/main:L7/provenance/sources/source-ledger.md:1-6
        - item 3
          - **step**: 3. governance/: seven sheets
          - **detail**: L7/governance/0.md and children copyright/, licensing/, patents/, permissions/, access/, controlled/. The sixth child is named controlled/ (formerly restrictions/). copyright/ carries the extra 'One place' section: every copyright and licence condition is stated once there; licensing/ and controlled/ point to it.
          - **locator**: 7lm@origin/main:L7/governance/copyright/0.md:16-18
        - item 4
          - **step**: 4. peering/: fifteen sheets
          - **detail**: L7/peering/0.md; private/0.md and public/0.md; under each, ingress/0.md and egress/0.md; under each of those four, peer-1/0.md and peer-1/object-1/0.md. peer-1 and object-1 are canonical position names, counted from 1; further peers and objects are peer-N/ and object-M/. The peer's 0.md is the owner's register of that peer's objects and their standing.
          - **locator**: 7lm@origin/main:L7/peering/0.md:22,28,31
        - item 5
          - **step**: 5. allications/: seven sheets
          - **detail**: L7/allications/0.md and six children, each with 0.md: publications/, applications/, communications/, specifications/, notifications/, participations/. Anything formerly at L7/publications/ belongs under L7/allications/publications/. Nothing is filed directly in allications/; an act is filed at the child that names it. Total sheeted L7 positions: 35.
          - **locator**: 7lm@origin/main:L7/allications/0.md:18-19
        - item 6
          - **step**: 6. Common sheet skeleton (every allications sheet and controlled/)
          - **detail**: Line 1: '# <path>/'. Line 3: '**Object:** <one sentence>'. Line 4: '**Path:** `<path>/` · **Layer:** L7 — SURFACE / FORWARD FACE · **Owner:** L7/'. Then the headed sections in this order: '## What this directory is', '## Why it exists', '## Holds', '## Does not hold', '## Boundary / traversal rule', '## Standing'. The first four are the four questions.
          - **locator**: 7lm@origin/main:L7/allications/applications/0.md:1-36
        - item 7
          - **step**: 7. The boundary rule (identical in all eight sheets)
          - **detail**: 'L7 is the forward face outside the USO. It owns the external relations of the bounded object: provenance, governance, peering, and allications — the outward acts, of which publication is one. Public/private exposure and ingress/egress direction remain independent peering distinctions. L7 does not thereby acquire or change the lower-layer scientific meaning.' publications/ and controlled/ add a second paragraph, the quote: "Material crossing outward may lose fidelity and may never gain scientific maturity merely by being exposed."
          - **locator**: 7lm@origin/main:L7/allications/0.md:33
        - item 8
          - **step**: 8. Common Standing lines
          - **detail**: (a) 'This branch may remain empty. Presence in the agnostic topology establishes admissible capability, not mandatory population; unused now does not mean removed.' — the five non-publication children append 'Nothing is filed here at present.' (b) 'Machine metadata: described at `L7/`; not instantiated in this repository. No automation.'
          - **locator**: 7lm@origin/main:L7/allications/applications/0.md:35-36
        - item 9
          - **step**: 9. Common 'Does not hold' tail (applications, communications, specifications, notifications, participations; and allications/ itself)
          - **detail**: the writing as produced work — `L8/L4/work/writing/`; the research meaning, argument, or claim — `L8/L5/research/`; the internal history of drafts, versions, and supersessions — `L8/L6/history/`; retired states — `L8/L6/retired/`; the provenance of what went out — `L7/provenance/`; the copyright, licence, permission, access, or controlled conditions on it — `L7/governance/`; the binding to a named peer — `L7/peering/`.
          - **locator**: 7lm@origin/main:L7/allications/applications/0.md:22-27
        - item 10
          - **step**: 10. Sheet: L7/allications/0.md
          - **detail**: Object: 'Directory for the bounded object's outward acts: publications, applications, communications, specifications, notifications, and participations.' What: the owner named the position on 2026-09-19 (owner's sentence quoted as written); one of four direct L7 branches; each of the six is a nominalized outward act done once, on a date, leaving an addressable record; the name is a mnemonic, not the membership test. Why: a released publication was the only outward act with a position; this gives the family one place and keeps six senses distinct. Holds: the six positions; nothing directly. Does not hold: a standing surface rather than an act (site, account, exposed interface, repository page — no position holds them), then the common tail. Standing: may remain empty 'and so may any of its six'; a line recording where publications/ moved from and where that move is recorded in the repository's own history; the machine-metadata line.
          - **locator**: 7lm@origin/main:L7/allications/0.md:3-39
        - item 11
          - **step**: 11. Sheet: L7/allications/publications/0.md
          - **detail**: Object: 'Directory for released publication objects at the forward face.' What: a released thing with a release identity (version that left, when, form, governance); the filer records the release, not the writing or the argument; applicable actions are present, publish, release; input is 'approved L6-backed packages'; 'Publication or legal status does not strengthen scientific evidence.' Why: 'Keeps publication release at L7 while writing remains L4, research meaning remains L5, and internal history remains L6.' Holds: released publication objects with explicit release identity (source, version, authority, permissions, status, direction); released corpus/publication identity. Does not hold: writing; research meaning; internal history and retired releases; provenance; governance conditions; outward exchange to a specific peer (peering egress); drafts stamped internal, empty release slots, material that has not left. Standing: may remain empty and what, if anything, is filed at present; the 'corpus' disposition (Split and reserved); machine-metadata line noting 'release state' is not enabled.
          - **locator**: 7lm@origin/main:L7/allications/publications/0.md:3-41
        - item 12
          - **step**: 12. Sheet: L7/allications/applications/0.md
          - **detail**: Object: 'Directory for applications the bounded object makes outward.' What: the object asks something of an external body and the asking is the record (funding, review, admission to a programme or standards body, or of its method to an outside case); filed as made — to whom, when, what version, what conditions. Why: directed at a specific authority, carries an outcome, binds the object to what it claimed; not a release, and its outcome is not a research finding. Holds: applications with body, date, version submitted, outcome where known. Does not hold: the judgement whether the claim is sound (L8/L5/research/); a correspondence that asks for nothing (communications/); then the common tail. Standing: the two common lines.
          - **locator**: 7lm@origin/main:L7/allications/applications/0.md:3-36
        - item 13
          - **step**: 13. Sheet: L7/allications/communications/0.md
          - **detail**: Object: 'Directory for communications the bounded object issues outward.' What: an act whose substance is the conveying (statement, correspondence, announcement, answer); filed: what was said, to whom, when. Why: saying something is not releasing, asking, or notifying; it is 'the residual outward act of speech'. Holds: communications with recipient, date, exact content or its version. Does not hold: a notice discharging an obligation (notifications/); a request of an external body (applications/); a released object with a release identity (publications/); then the common tail. Standing: the two common lines.
          - **locator**: 7lm@origin/main:L7/allications/communications/0.md:3-37
        - item 14
          - **step**: 14. Sheet: L7/allications/specifications/0.md
          - **detail**: Object: 'Directory for specifications the bounded object issues outward for others to build or check against.' What: a contract handed to an external party to implement, interoperate with or verify (interface contract, schema, wire format, published requirement set), filed as issued at its version. Why: a self-directed specification is L4 work with L5 meaning; one handed outward is a commitment, and the version built against matters. Holds: specifications issued outward, each at an exact version, with who it was issued to or published for. Does not hold: the specification as a written artifact under development (L8/L4/work/writing/); an external specification the object consumes (L7/peering/*/ingress/peer-1/object-1/, NO EDIT, NO DELETE); then the common tail. Standing: the two common lines.
          - **locator**: 7lm@origin/main:L7/allications/specifications/0.md:3-36
        - item 15
          - **step**: 15. Sheet: L7/allications/notifications/0.md
          - **detail**: Object: 'Directory for notices the object issues outward.' What: giving notice is itself the thing required (disclosure, required report, breach or defect notice, alert); filed: the notice, party notified, date, obligation discharged. Why: a notice usually discharges an obligation; 'was notice given, and when' has one place. Holds: notices with recipient, date, and the obligation or condition under which given. Does not hold: the obligation itself, a governance fact (L7/governance/); an ordinary statement (communications/); then the common tail. Standing: the two common lines.
          - **locator**: 7lm@origin/main:L7/allications/notifications/0.md:3-36
        - item 16
          - **step**: 16. Sheet: L7/allications/participations/0.md
          - **detail**: Object: 'Directory for the bounded object's participations in external settings.' What: taking part (conference, working group, review panel, standards body, collaboration); filed: which body, role, period, what was contributed or received standing from. Why: an external relation with a date and a role; not a publication, application or peer binding. Holds: participations with body, role, period, contribution. Does not hold: participant positions inside the research setting (L8/L5/institution/peers/); a bound peer object exchanged with a body (L7/peering/); anything produced and then released (publications/); then the common tail. Standing: the two common lines.
          - **locator**: 7lm@origin/main:L7/allications/participations/0.md:3-37
        - item 17
          - **step**: 17. Sheet: L7/governance/controlled/0.md (as on main)
          - **detail**: Object: 'Directory for restrictions and other conditions that constrain external disclosure, use, transfer, or handling.' What: a record states what may not be done with an object at the boundary (not redistributed, not reproduced at length, not used on-line, not transferred, not disclosed, not opened); one of six governance positions; the filer records the restriction, its source (licence, copyright holder, patent filing, owner ruling) and the objects it binds; the restriction stays here and the decision's history at L8/L6/. Why: 'Keeps what is controlled explicit and machine-addressable without redefining the underlying research.' Holds: restrictions on disclosure, use, transfer, handling; restrictions following from a sibling condition, cross-referenced by path; owner rulings restricting what crosses outward. Does not hold: the restricted object (L7/peering/ or L7/allications/publications/); the deriving copyright/licence/patent condition; who may access (access/); what is permitted (permissions/); history (L8/L6/history/) and the retired binding (L8/L6/retired/). Boundary: common paragraph plus the 'Material crossing outward...' quote. Standing: may remain empty; no inherited term placed here; machine-metadata line plus 'here restrictions are stated in prose only'.
          - **locator**: 7lm@origin/main:L7/governance/controlled/0.md:3-40
        - item 18
          - **step**: 18. Decide main wording or beta wording before writing controlled/ and its neighbours
          - **detail**: The unmerged beta differs in controlled/ only in Holds: the second bullet becomes two — pointers to copyright or licence conditions stated once at L7/governance/copyright/ ('do not restate those conditions independently here'), and other restrictions cross-referenced to the patent, permission or access record. Beta also changes licensing/, L7/0.md, peering/0.md, private/ingress/0.md, sources/0.md and the ledger. The seven allications sheets are identical on main and beta.
          - **locator**: 7lm@origin/beta/common-contracts-r1-r6:L7/governance/controlled/0.md:19-20
        - item 19
          - **step**: 19. Replace scaffold-only sentences with the adopting repository's own facts
          - **detail**: Do not copy: the §25 record pointer in allications/0.md:38, the 'harmonized specification' sentence in publications/0.md:39, commit c0f46e1 in governance/0.md:39, and 'in this repository' statements about what is or is not filed. peer-1 sheets name the actual peer in the adopting repository. Only six scaffold sheets carry 'Exemplars (by reference)'; L7 does not say whether an exemplar repository's own sheets carry that section.
          - **locator**: 7lm@origin/main:L7/peering/public/ingress/peer-1/0.md:8
      - **open_questions**
        - Which wording do the exemplars mirror: main (the model of record) or the unmerged beta? They differ in 7 L7 files, including controlled/ Holds, licensing/, the consensus-baseline paragraph of L7/0.md and the aybllc/l6 passages. The seven allications sheets are the same on both.
        - L7/0.md's Object line, core question and Function row still say 'publications' rather than 'allications' (L7/0.md:3, 25-26). L7 does not say whether this is intended; the specification and record section 37 were outside this scope.
        - aybllc/l6: main says it 'is bound here' and 'pinned here at commit 53b28f6', but no peer or object sheet names it and the ledger is empty. Whether each exemplar must instantiate a real private-ingress binding and source row for it was not settled from L7.
        - I read 'the four questions' as the four headed sections What this directory is / Why it exists / Holds / Does not hold. No L7 sheet uses the phrase 'four questions'.
        - What an adopting repository writes in place of the scaffold-only Standing sentences (the §25 move record, the specification sentence in publications/, commit c0f46e1) is not stated in L7.
        - Where the exemplar mains' existing L7/publications/binder/ content goes under L7/allications/publications/ was not examined; only directory names were listed.
        - Other 7lm branches also change L7 and were not read: origin/ccr-00099fac-hjosbo (draft PR #19) and origin/audit/peering-descriptive-reframe-2026-09-20 (diff stat tail shows 35 files, 727 insertions, 509 deletions, including L7 files). origin/ccr-9391bd81-f2enmj (PR #20), both copilot branches and origin/ccr-9a67809a-iwii3n show no L7 change against their merge-bases.
        - Whether exemplar sheets should carry their own 'Exemplars (by reference)' section, which in the scaffold points at the exemplars themselves, is not stated in L7.
        - The heading 'THESE REPOS BELOW ARE PRIVATE THUS WILL RETURN 404 UNLESS YOU HAVE ACCESS.' sits as a level-3 heading with no blank line before it (L7/0.md:159). L7 does not say whether the exemplars' L7/0.md should carry it.
    - item 6
      - **key**: sheets-L8
      - **facts**: 102
      - **checklist**
        - item 1
          - **step**: Definition (locally authored)
          - **detail**: Main: one file per definition in L8/L0/semantics/definitions/; version a changed definition, never rewrite; an external or peer definition is never copied in, only referenced with its tag (identity, owner, source layer, version, ingress binding, immutable). Beta adds: state only meanings the project actually uses; the exemplar's semantic job is not every project's definition; inherited table rows are preserved, not adopted.
          - **locator**: 7lm@origin/main:L8/L0/semantics/definitions/0.md:8-29; beta L8/L0/0.md:10-14, definitions/0.md:41
        - item 2
          - **step**: Other foundational distinctions
          - **detail**: Main: semantic representation that is not a definition in L8/L0/semantics/; ontological, epistemic, universality distinctions in their own rail directories; traversal and attachment teaching in L8/L0/pedagogy/. Beta adds: the four named rails are not exhaustive; other justified distinctions keep their scope inside the existing topology, no new directory.
          - **locator**: 7lm@origin/main:L8/L0/0.md:55-63; beta L8/L0/0.md:69
        - item 3
          - **step**: Admissible states
          - **detail**: Main: L8/L1/state-space/ (admitted and excluded states, domains, invariants, identity conditions, versions, explicit invariant collisions). No operations. Beta adds: a corpus or source-selection inclusion rule is filed here; it need not be numerical; keep an unresolved admission question open rather than admitting to finish a manuscript.
          - **locator**: 7lm@origin/main:L8/L1/state-space/0.md:18-22; beta L8/L1/0.md:10-12
        - item 4
          - **step**: Formal relation
          - **detail**: Main: exact relations in L8/L2/formal-mathematics/relations/; operators and constructors in operators/; proofs, derivations and explicitly unproved obligations in proofs/. Beta adds: exact mathematics about uncertainty is L2; a qualitative inquiry need not invent formal machinery; an unproved relation stays unproved even if the manuscript reports it.
          - **locator**: 7lm@origin/main:L8/L2/0.md:52-54; beta L8/L2/0.md:10-12
        - item 5
          - **step**: Method
          - **detail**: Main: algorithms, units, numerical representation, feasibility and measurement design in L8/L3/engineering-mathematics/; approximations in approximation/; error budgets in uncertainty/; declared acceptance bounds in tolerances/. Beta adds: state the chosen method and its justification only when the inquiry needs one; leave L3 unused otherwise; no computational prototype is required for a manuscript.
          - **locator**: 7lm@origin/main:L8/L3/0.md:53-57; beta L8/L3/0.md:10-12
        - item 6
          - **step**: Computation
          - **detail**: Main: what was actually run, with inputs, environment, outputs or failures, in L8/L4/work/computation/; the algorithm stays L3, the proof L2, the interpretation L5. Beta adds: an executable is required only when the research calls for executed computation; beta's own example files there are a script, its tests and a results JSON.
          - **locator**: 7lm@origin/main:L8/L4/work/computation/0.md:20-24; beta L8/L4/0.md:10
        - item 7
          - **step**: Experiment
          - **detail**: Main: the experiment as executed (observations, measurements, raw work product, failures) in L8/L4/work/experiments/; design at L3; conclusion at L5. Beta adds nothing specific beyond naming 'performed observations or experiments at work/experiments/'.
          - **locator**: 7lm@origin/main:L8/L4/work/experiments/0.md:20-23; beta L8/L4/0.md:10
        - item 8
          - **step**: Manuscript draft
          - **detail**: Main: the produced document and its production record in L8/L4/work/writing/; filing asserts production only. Beta adds: also its editable source, figures and document-production materials; the project chooses tools, formats and internal organization; cite L0-L5 representations instead of copying them; manuscript text never goes into a 0.md.
          - **locator**: 7lm@origin/main:L8/L4/work/writing/0.md:20-21; beta L8/L4/work/writing/0.md:12-16
        - item 9
          - **step**: Argument
          - **detail**: Main: research claims and thesis statements in L8/L5/research/lanes/, one lane per line of inquiry, each naming the L4 work and L3-L0 contracts it depends on. Beta adds: the manuscript argument is developed at L5; lanes are not rails; do not duplicate the whole manuscript at L5.
          - **locator**: 7lm@origin/main:L8/L5/research/lanes/0.md:10,18-21; beta L8/L5/0.md:10-12
        - item 10
          - **step**: Review
          - **detail**: Main: reviews, audits and qualifications in L8/L5/research/review/, each naming the claim reviewed; the same position is the catch-all for anything awaiting the owner's review (PARKED if set aside, moved to lanes/ if taken up). Beta adds: these moves delete nothing; later deletion follows the L6 enumeration rule; reviewer agreement supplies no missing proof.
          - **locator**: 7lm@origin/main:L8/L5/research/review/0.md:18-22,36; beta review/0.md:36, L8/L5/0.md:12
        - item 11
          - **step**: Finding
          - **detail**: Main: bounded conclusions, including negative ones, in L8/L5/research/findings/, each with dependencies, limits, uncertainty, review status and reproducibility information. Beta adds only the label 'bounded conclusions' and an example file.
          - **locator**: 7lm@origin/main:L8/L5/research/findings/0.md:18-20; beta L8/L5/0.md:10
        - item 12
          - **step**: History
          - **detail**: Main: dated records of prior states, decisions, corrections and failed paths in L8/L6/history/; unfiled L6 material may wait in the optional L8/L6/in/. Beta adds: when adopting revised origin guidance, record old and new location of every move and the affected dependencies, keep local data and authorship.
          - **locator**: 7lm@origin/main:L8/L6/history/0.md:20-24, L8/L6/0.md:53; beta L8/L6/0.md:10-12
        - item 13
          - **step**: Retired state
          - **detail**: Main: superseded drafts, prior versions, prior sheets and inactive peer bindings in a named set under L8/L6/retired/<set>/ with a sheet at the set's root; a file whose every part is enumerated as standing elsewhere may be deleted instead. Beta adds nothing to the retired sheets.
          - **locator**: 7lm@origin/main:L8/L6/retired/0.md:12,22-23
        - item 14
          - **step**: Source
          - **detail**: Main (as stated by the L8 sheets): external source identity, version, authority and lineage at L7/provenance/ (source ledger at L7/provenance/sources/source-ledger.md, prior art at L7/provenance/prior-art/); never re-owned at L6 or copied into L0-L3. Beta adds: collected source instances and collection work are L4, their external identities L7, the argument drawn from them L5.
          - **locator**: 7lm@origin/main:L8/L6/0.md:86, L8/L5/research/lanes/0.md:30; beta L8/L1/0.md:10
        - item 15
          - **step**: Peer binding
          - **detail**: Main: active bindings at L7/peering/ (the Auditonomous-to-Autonomous binding is named as L7's); the bound definition is referenced, not rewritten, at receiving L0; inactive bindings retire to L8/L6/retired/. Beta adds: another project's material is related through L7/peering/ with owner and version identified; sharing the housing merges nothing; receiving L0 may reference the exact external definition.
          - **locator**: 7lm@origin/main:L8/L4/0.md:111, L8/L6/0.md:88; beta L8/0.md:24, L8/L4/0.md:91
        - item 16
          - **step**: Released publication
          - **detail**: Main: the released publication object at L7/allications/publications/, with provenance and governance at L7; the released form of a finding likewise. Beta adds: only an authorized released version is represented there; producing a draft is not a publication decision.
          - **locator**: 7lm@origin/main:L8/L4/work/writing/0.md:32, L8/L5/research/findings/0.md:31; beta L8/L4/work/writing/0.md:16
        - item 17
          - **step**: Sheet and check discipline for any repository brought into step
          - **detail**: Root holds only README.md, L7/, L8/, .github/ (and .gitignore per the check); every 0.md under L7 and L8 begins '# <path>/'; all 71 canonical positions carry a sheet, including L7/allications/* and L7/governance/controlled; retired-set interiors are exempt. Beta's check additionally refuses USO/ and lowercase layer names.
          - **locator**: 7lm@origin/main:.github/workflows/integrity.yml:17-61; beta same file:19-59
        - item 18
          - **step**: Migration of an existing project (beta only)
          - **detail**: Compare the changed contracts, retain the project's data and local choices, record any moves, review affected dependencies, and only then claim the project has migrated.
          - **locator**: 7lm@origin/beta/common-contracts-r1-r6:L8/0.md:24
      - **open_questions**
        - The beta's history entry says the R1-R6 corrections were made 'after the owner's approval of R1–R6'. The owner's approval itself (their words, and what R1 to R6 each are) was not found in the in-scope sheets; looked in all 40 L8 sheets on main and the beta diff over L8. Whether the owner means the beta to become the model of record is unsettled; it is unmerged.
        - Which model are the exemplars to match: main as it stands (identical in every sheet to 2e5a6d6) or main plus the beta guidance? On main nothing in the interior changed since 2e5a6d6 except the layer-lists proposal in the L6 inbox.
        - L8/0.md's tree omits L6/in/ while L8/L6/0.md's tree includes it. Should an exemplar carry L8/L6/in/? The sheet calls it optional and it is not one of the 71 positions.
        - L8/L6/0.md and L8/L6/in/0.md do not name 7lm-layer-lists.md, which PR #21 added to the inbox. Whether the layer lists stay, move beside the field guide, or are withdrawn is stated in the file itself to be the owner's call.
        - README says the root holds four entries and nothing else; the check also admits .gitignore; both exemplar mains have a .gitignore. Which statement controls was not settled.
        - Main sheets (L8/L0/pedagogy/0.md:29, L8/L6/0.md:74) name the field guide at L8/L6/7lm-field-guide.md. Open draft PR #20 would retire it; that branch was not read here, so the effect on these two sheets is not established.
        - Where collected data instances go inside L4 is not assigned to a child directory (L8/L4/work/computation/0.md:22).
        - The word 'peer' covers both L5 participant positions and L7 peering positions; the relation is expressly not adjudicated (L8/L5/institution/peers/0.md:26).
        - Status of the roughly 70 inherited controlled-definition rows is left to the owner row by row (definitions/0.md:127); beta adds a caution but decides nothing.
        - On beta, sheets of the positions that received demonstration files were not updated (computation/0.md still says empty). If beta is adopted, do those sheets need correcting, and do the demonstration files belong in an exemplar at all or only in the scaffold?
        - Beta's seven L7 file changes and its docx change were not read (outside this scope). The beta JSON records Python 3.14.4 and nine passing tests; the tests were not re-run (read-only workflow).
        - Each exemplar's own integrity.yml still lists the former L7 names; it was only grepped, not read. Whether bringing the exemplars into step includes replacing their check with the scaffold's main or beta version was not determined here.
    - item 7
      - **key**: layer-lists
      - **facts**: 62
      - **checklist**
        - item 1
          - **step**: 1. Order of work: scaffold first and alone; exemplars follow by hand, when the owner judges the scaffold close
          - **detail**: The other repositories mirror aybllc/7lm by hand. No automated push exists; every step is HOA (a person's).
          - **locator**: 7lm@origin/main:L8/L6/7lm-field-guide.md:608,610
        - item 2
          - **step**: 2. Root
          - **detail**: README.md, L7/, L8/; may also hold .github/ (the one CI workflow) and .gitignore; nothing else. The layer lists (line 415) and the scaffold README (line 13) omit .gitignore; the specification (line 281) and the CI admit it, and both exemplars have one.
          - **locator**: 7lm@origin/main:L8/L6/7lm-field-guide.md:371
        - item 3
          - **step**: 3. Keep the whole canonical tree
          - **detail**: Copy the full layout; folders not needed stay empty. No canonical folder may be removed or renamed; nothing may be added at the root. Current L7 names are allications/ (publications, applications, communications, specifications, notifications, participations) and governance/controlled/.
          - **locator**: 7lm@origin/main:L8/L6/7lm-field-guide.md:377-451,478,496
        - item 4
          - **step**: 4. A sheet in every folder, first line the path
          - **detail**: Every folder has a 0.md whose first line is the folder's own path from the root, e.g. '# L8/L3/engineering-mathematics/'. These two things are not design choices; dropping either puts the repository outside the system.
          - **locator**: 7lm@origin/main:L8/L6/7lm-field-guide.md:455; L8/L6/7lm-sheet-templates.md:3
        - item 5
          - **step**: 5. Sheet body is the owner's design choice
          - **detail**: Everything after the first line is a design choice. Recommendation for a layer's own sheet: at least one sentence more than the layer's number. Choose a degree (minimal, standard, full) and use the templates; keep the first line exact. The scaffold's full-degree sheets bind no one else's; keeping them is one choice.
          - **locator**: 7lm@origin/main:L8/L6/7lm-sheet-templates.md:3,5,7; L8/L6/7lm-field-guide.md:457,496
        - item 6
          - **step**: 6. Blank sheets beneath a layer are allowed
          - **detail**: A sheet beneath a layer may be the first line and nothing else. It passes the CI and is an audit exception for HOA review, listed in a collecting document that is not built yet. A missing sheet is not the same thing: that folder is outside the system.
          - **locator**: 7lm@origin/main:L8/L6/7lm-sheet-templates.md:39,45; L8/L6/7lm-field-guide.md:457,600
        - item 7
          - **step**: 7. Own folders under canonical positions
          - **detail**: Allowed for the repository's own material; give each a 0.md. The CI reports a missing one without failing.
          - **locator**: 7lm@origin/main:L8/L6/7lm-field-guide.md:474
        - item 8
          - **step**: 8. in/ is optional at any position
          - **detail**: An inbox for what belongs to a position and is not yet worked into it; never required; carries a 0.md. If the layer itself is unknown, use the catch-all L8/L5/research/review/ instead.
          - **locator**: 7lm@origin/main:L8/L6/7lm-field-guide.md:476,527
        - item 9
          - **step**: 9. Prior states: retire, do not correct
          - **detail**: Make a dated set under L8/L6/retired/, put prior files at their old relative paths unchanged (headings uncorrected), give the set its own 0.md, record the retirement in L8/L6/history/. The CI checks only the set's own sheet.
          - **locator**: 7lm@origin/main:L8/L6/7lm-field-guide.md:480,531-534
        - item 10
          - **step**: 10. Deletion only after enumeration
          - **detail**: Retire only what integrity needs to rebuild the past (the owner's authored documents, rule texts of a prior layout, error records). Anything else superseded is enumerated in the record at L8/L6/history/ and then deleted. The CI does not enforce no-deletion.
          - **locator**: 7lm@origin/main:L8/L6/7lm-field-guide.md:536,592; .github/workflows/integrity.yml:3-5
        - item 11
          - **step**: 11. No history crosses between repositories
          - **detail**: The tree and the sheets travel; the scaffold's L6 never does. Each repository's history stays in its own L6. Any guide an adopter publishes carries the model, not any repository's past.
          - **locator**: 7lm@origin/main:L8/L6/7lm-field-guide.md:9,554,610
        - item 12
          - **step**: 12. One CI check, the same everywhere
          - **detail**: .github/workflows/integrity.yml: fails on conflict markers, a non-canonical root, a sheet not headed by its path, a canonical position without a sheet; reports other folders without a sheet; moves nothing. Main's version still accepts USO/ or L8/; beta's requires L8 and uppercase L0-L6.
          - **locator**: 7lm@origin/main:L8/L6/7lm-field-guide.md:463-470; .github/workflows/integrity.yml:17-61
        - item 13
          - **step**: 13. Before copying from an exemplar, read the specification's 'Not yet as stated'
          - **detail**: The specification lists for each exemplar what does not yet match, including that both desks carry the former L7 names (publications/ direct, governance/restrictions/) and the L7 restructure is not yet mirrored. The field guide's own summary at line 620 omits that sentence.
          - **locator**: 7lm@origin/main:L8/L6/7lm-field-guide.md:618-622; L8/L4/work/writing/7lm-harmonized-architecture-specification.md:950,958
        - item 14
          - **step**: 14. Treat the layer lists as a proposal, not a source
          - **detail**: They sit in the L6 inbox, the specification controls where they differ, and 18 of 102 checked bullets are not plain restatements of the sheets or specification (lines 50, 93, 176, 177, 228, 229, 230, 231, 264, 310, 316, 320, 356, 388, 400, 404, 414, 415). Mirror from the sheets and the specification.
          - **locator**: 7lm@origin/main:L8/L6/in/7lm-layer-lists.md:3,5
      - **open_questions**
        - Which state is the model to mirror? On origin/main nothing but the layer-lists file changed since 2e5a6d6; the substantive changes (beta R1-R6 corrections and research-housing guidance, PR #20's field-guide retirement) are unmerged. Mirroring main means mirroring the 2026-09-20 scaffold; the owner has not said in anything I read whether beta or PR #20 is to be merged first.
        - The layer lists have no section headed 'open for the owner'. If the task expected such a section, it is not found in L8/L6/in/7lm-layer-lists.md on origin/main; the only explicit owner's call there is where the document sits (line 5).
        - Is .gitignore admitted at the root? The specification (line 281), the CI and the field guide (line 371) say yes; the scaffold README (line 13) and the layer lists (line 415) say the root holds README.md, L7/, L8/, .github/ 'and nothing else'. Both exemplars have a .gitignore on origin/main.
        - Is in/ a canonical position? L8/L6/0.md draws in/0 in its directory structure and the layer lists file it under 'Canonical positions beneath it'; the specification tree, L8/0.md, the field guide tree and the CI canon list do not include it. Whether the exemplars should gain L8/L6/in/ when mirrored is not settled by these texts (the guide says it is never required).
        - If PR #20 merges, should the layer lists be re-sourced? Six bullets or clauses rest only on field-guide wording (lines 176, 229, 230, 388, 400, 404), and the retired set's sheet would declare such sentences 'not current'. Nothing I read decides this.
        - If beta merges, the layer lists carry superseded wording at lines 48, 53, 225, 231, 391, 404, 412. Neither beta nor PR #20 contains or mentions the layer lists, so no branch records how they are to be reconciled.
        - The record's open item on L7/provenance/lineage/ (record line 448: either the scaffold's own lineage sheet is the one deliberate blank, or the push blanks it on the way out) is unresolved and bears on what an exemplar's lineage sheet should say; the layer lists (line 356) repeat 'HOA input only' without the open item. Auditonomous holds a session-provenance record at lineage/ per the specification (line 954).
        - The scaffold's L6 has no record entry for PR #21 and L8/L6/0.md line 79 still lists three inbox items, not four. Whether that is deliberate under record section 36 ('Don't change the system unless you ask or are unsure') or an omission to be recorded is the owner's call.
        - I did not verify beta's research-probe files, the .docx, or the JSON (excluded by the task), nor PR #19 or the audit branch; statements about them here come only from PR #20's record sections 39-40 and beta's specification-history entry.
    - item 8
      - **key**: beta-and-prs
      - **facts**: 60
      - **checklist**
        - item 1
          - **step**: 1. Treat main c9dc061 as the physical target for the exemplars
          - **detail**: Nothing off main changes the 71 canonical positions or the root, so the directory mirror the exemplars need (allications/ with six children; governance/controlled/) is the same whichever unmerged branch is later accepted. The exemplar physical update does not have to wait on the beta, PR #19, PR #20 or the audit branch.
          - **locator**: 7lm@origin/main:.github/workflows/integrity.yml:47-59; all refs: canon list identical
        - item 2
          - **step**: 2. Decide the beta before copying integrity.yml to the exemplars
          - **detail**: main's CI still accepts USO/ and lowercase l0-l6; the beta's requires L8 and uppercase. If the beta is to be merged, the exemplars should receive the beta form; if not, main's. The 71-position list is the same either way.
          - **locator**: 7lm@origin/beta/common-contracts-r1-r6:.github/workflows/integrity.yml:19-27,36,50-57
        - item 3
          - **step**: 3. Beta into main: clean today
          - **detail**: git merge-tree --write-tree origin/main origin/beta/common-contracts-r1-r6 exits 0 (tree 633c343). The merged tree keeps PR #21's layer-lists file and passes the sheet-heading test. The specification version string would stay 'Version of 20 September 2026' despite changed text.
          - **locator**: 7lm@merge-tree result 633c343f88378e80d75bc2fe7505e743c192dbad
        - item 4
          - **step**: 4. If both the beta and PR #20 are wanted, settle the field guide first
          - **detail**: Textually they merge cleanly in either order, but the beta's three field-guide edits follow the rename and land in the retired copy that PR #20 declares verbatim. Either drop the beta's guide hunks or accept that the retired copy is not the 20 September text.
          - **locator**: 7lm@1b235ad:L8/L6/retired/field-guide-2026-09-20/7lm-field-guide.md:96,150,230
        - item 5
          - **step**: 5. PR #19 and the beta cannot both merge without hand resolution
          - **detail**: Seven conflicting files, including the specification .md, the binary .docx and specification-history.md. PR #19 sets the spec to 'Version of 6 October 2026'; the beta leaves 20 September. Whichever lands second must be re-done by hand and the .docx regenerated.
          - **locator**: 7lm@merge-tree(beta, origin/ccr-00099fac-hjosbo) exit 1: 7 files
        - item 6
          - **step**: 6. The audit branch is a competing rewrite, not an increment
          - **detail**: It merges cleanly into main alone, but conflicts with the beta in 12 files and with PR #19 in 20, and it reverses the L0 authorship rule that the beta's R5 keeps. Its CI forbids a root .gitignore that both exemplars carry, while its own specification still allows it. Its disposition is recorded as the owner's call.
          - **locator**: 7lm@origin/audit/peering-descriptive-reframe-2026-09-20:.github/workflows/integrity.yml:49; L8/L4/work/writing/7lm-harmonized-architecture-specification.md:289
        - item 7
          - **step**: 7. Beta guidance for the exemplar and manuscript work, if adopted
          - **detail**: Manuscript at L8/L4/work/writing/; argument at L8/L5/; history at L8/L6/; released version at L7/allications/publications/. On taking an origin update: compare contracts, keep local data and choices, record old and new locations of each move, review dependencies before claiming migration. This guidance exists only on the unmerged beta.
          - **locator**: 7lm@origin/beta/common-contracts-r1-r6:L8/0.md:22-24; L8/L6/0.md:10-12; L8/L4/work/writing/0.md:12-16
        - item 8
          - **step**: 8. Stale branches
          - **detail**: copilot/create-academic-guide-plan and ccr-9a67809a-iwii3n are ancestors of main and hold nothing. copilot/create-error-list holds one unmerged review file (96 recommendations at baseline 6609f38) that merges cleanly anywhere and is partly answered by the beta.
          - **locator**: 7lm@origin/copilot/create-error-list:L8/L5/research/review/7lm-audit-recommendations.md
      - **open_questions**
        - Which hunk is R1, R2 ... R6: no document on any ref of 7lm or on the exemplar beta branches enumerates them. The record's sentence names seven noun phrases; my six-way grouping (B09-B14) is inference. The original R1-R6 list presumably lives in the Codex task conversation, outside the repositories.
        - The owner's approval of R1-R6 is asserted only by the beta's own commit subject and specification-history.md:106; no owner words are quoted for it and nothing on main records it. Whether the owner still stands by that approval, and whether it covered the second commit (97314c5, the 18-sheet 'research housing' guidance), is not settled by any document.
        - Where the 'actual exemplar integration and candidate branch commit identities are recorded separately' (beta specification-history.md:112): not found in the 7lm beta tree (searched for e64b382, 714480d, '7lm-exemplar').
        - The beta leaves the specification at 'Version of 20 September 2026' although six passages changed; PR #19 moves it to 6 October 2026. Which version string the model of record should carry after either merge is undecided.
        - The beta edits the field guide at its live path while PR #20 retires that guide as stale and verbatim. Whether the beta's three guide hunks should be dropped is the owner's call.
        - Root .gitignore: main's specification (line 281) and CI admit it, main's README line 13 lists four entries 'and nothing else', the scaffold has no .gitignore on any ref, both exemplars have one, and the audit branch's CI would forbid it. Which rule the exemplars should be held to is not settled.
        - Disposition of the audit branch: PR #20's record section 40 says it is 'neither adopted nor retired'. It reverses the L0 local-authorship rule and the universal peering route that the beta retains, so the two cannot both be the model.
        - Whether PRs #19 and #20 are still open drafts was not verified (no network use); taken from the task statement. PR #20's tip c9638a9 is one record-only commit ahead of what PR #19 and the audit branch merged (c4dae95).
        - Beta claims not verifiable from git objects: that the .docx's 54 rendered pages were inspected; that the nine tests first failed for a missing implementation (no failing-run artefact in the tree); that the Zenodo deposit and the supplied Semantic Magnitude PDF have the stated SHA-256 values (source bytes are not in the repository).
        - Whether copilot/create-error-list's 96 recommendations were ever adjudicated by the owner: no adjudication found on main or on any other ref.
    - item 9
      - **key**: exemplar-autonomous
      - **facts**: 57
      - **checklist**
        - item 1
          - **step**: 0. Preconditions (nothing below is done by this workflow)
          - **detail**: Work from autonomous origin/main c9076c3 in one commit, by hand, on the owner's word (scaffold §26). Decide first whether the pass starts from main or salvages the beta's class (a) hunks; the beta's contract changes and research objects are a separate matter. Expected end state: 71 canonical positions sheeted, 103 sheets checked (63 under L7), root unchanged.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:§26
        - item 2
          - **step**: 1. Move the publications branch as a tracked rename
          - **detail**: git mv L7/publications L7/allications/publications. Nine files follow: 0.md; binder/0.md; binder/README.md; binder/internal/FETCH_LIST.md; binder/internal/README.md; binder/internal/tools/verify_fragments.py; binder/internal/tools/verify_fragments_v2.py; binder/press-kit/GLOSSARY_AUTONOMOUS.md; binder/press-kit/README.md. Do not edit the seven non-sheet files.
          - **locator**: autonomous@origin/main:L7/publications/ ; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:§25
        - item 3
          - **step**: 2. Move the restrictions position as a tracked rename
          - **detail**: git mv L7/governance/restrictions L7/governance/controlled (one file, 0.md).
          - **locator**: autonomous@origin/main:L7/governance/restrictions/0.md
        - item 4
          - **step**: 3. Set the first line and Path line of the three moved sheets
          - **detail**: L7/allications/publications/0.md lines 1 and 4: 'L7/publications/' -> 'L7/allications/publications/'. L7/allications/publications/binder/0.md lines 1 and 4: 'L7/publications/binder/' -> 'L7/allications/publications/binder/'. L7/governance/controlled/0.md lines 1 and 4: 'L7/governance/restrictions/' -> 'L7/governance/controlled/'. Six lines.
          - **locator**: autonomous@origin/main:L7/publications/0.md:1,4 ; :L7/publications/binder/0.md:1,4 ; :L7/governance/restrictions/0.md:1,4
        - item 5
          - **step**: 4. Write six new sheets
          - **detail**: L7/allications/0.md and L7/allications/{applications,communications,specifications,notifications,participations}/0.md, each headed '# <path>/'. Source text: the scaffold's sheets at the same paths. One line needs this repository's own wording: the scaffold's allications Standing bullet points to the scaffold's record §25; here it should point to this repository's new §14.
          - **locator**: 7lm@origin/main:L7/allications/0.md:1-39 (Standing line 38) ; 7lm@origin/main:L7/allications/applications/0.md
        - item 6
          - **step**: 5. Update the check, keeping the Q-6 block
          - **detail**: In .github/workflows/integrity.yml: line 76 'L7/governance/restrictions' -> 'L7/governance/controlled'; line 78 'L7/publications' -> the scaffold's two lines (eight peer-1/object-1 positions, then seven allications positions); line 61 comment 'l6/retired/' -> 'L6/retired/ (l6/retired/ before the rename pass)'; line 5 comment 'USO/l6/history/' -> 'L8/L6/history/'; add the blank line after the checkout step. Leave lines 16-44 (retired Q-6 block) as they are. Do not hard-code the layer names as the beta did. Result: the scaffold's file plus the Q-6 block; 57 listed positions become 71.
          - **locator**: autonomous@origin/main:.github/workflows/integrity.yml:5,11,16-44,61,76,78 ; 7lm@origin/main:.github/workflows/integrity.yml:5,12,33,48,50-51
        - item 7
          - **step**: 6. Replace the canonical-branches sentence (2 occurrences)
          - **detail**: '...L7/peering/, and L7/publications/.' -> '...L7/peering/, and L7/allications/.' at L7/0.md:14 and L7/peering/0.md:8. Do this before step 7 so the blanket path rewrite cannot produce the beta's misquotation.
          - **locator**: autonomous@origin/main:L7/0.md:14 ; :L7/peering/0.md:8 ; 7lm@origin/main:L7/0.md:16
        - item 8
          - **step**: 7. Rewrite the plain path references to publications (22 lines, 20 files)
          - **detail**: 'L7/publications' -> 'L7/allications/publications' at: L7/0.md:223; L7/governance/0.md:26; access/0.md:24; copyright/0.md:23; licensing/0.md:19; permissions/0.md:24; controlled/0.md:24; L7/peering/0.md:29; private/egress/0.md:25; private/egress/peer-1/object-1/0.md:22; public/0.md:23; public/egress/0.md:10,24; public/egress/peer-1/object-1/0.md:21; L7/provenance/0.md:29; L8/L4/0.md:124; L8/L4/work/0.md:30,42; L8/L4/work/computation/0.md:40; L8/L4/work/writing/0.md:27; L8/L5/research/findings/0.md:31; L8/L6/0.md:82. With steps 3, 5 and 6 this accounts for all 29 lines.
          - **locator**: autonomous@origin/main: git grep -n -F 'L7/publications' (live-text excludes)
        - item 9
          - **step**: 8. Rewrite the plain path references to restrictions (12 lines, 11 files)
          - **detail**: 'L7/governance/restrictions/' -> 'L7/governance/controlled/' at: access/0.md:27; licensing/0.md:27; patents/0.md:19,25; permissions/0.md:28; L7/peering/private/0.md:10,23; private/egress/0.md:24; private/egress/peer-1/0.md:21; private/ingress/0.md:24; L7/provenance/prior-art/0.md:34; L7/provenance/sources/0.md:16. Change the path only; the word 'restrictions' before the dash on those lines names a kind of condition and stays. With steps 3, 5 and 10 this accounts for all 16 lines.
          - **locator**: autonomous@origin/main: git grep -n -F 'governance/restrictions' (live-text excludes)
        - item 10
          - **step**: 9. Bare folder names and the tree drawing
          - **detail**: `restrictions/` -> `controlled/` at L7/0.md:66 (tree: 'restrictions/0' -> 'controlled/0') and L7/governance/0.md:8 and 32 (3 occurrences). L7/0.md:82 '└── publications/0' -> the scaffold's seven lines: '└── allications/0' with children publications/0, applications/0, communications/0, specifications/0, notifications/0, participations/0.
          - **locator**: autonomous@origin/main:L7/0.md:66,82 ; :L7/governance/0.md:8,32 ; 7lm@origin/main:L7/0.md:69,85-91
        - item 11
          - **step**: 10. The prose table in L7/0.md
          - **detail**: Line 105: row 'governance/restrictions/' -> 'governance/controlled/' with the scaffold's two current cells. Line 115: the one 'publications/' row -> the scaffold's seven rows (allications/, allications/publications/, applications/, communications/, specifications/, notifications/, participations/). Line 112 is covered by step 12.
          - **locator**: autonomous@origin/main:L7/0.md:105,115 ; 7lm@origin/main:L7/0.md:114,124-130
        - item 12
          - **step**: 11. Sweep: the boundary sentence (56 occurrences, 55 files)
          - **detail**: 'peering, and publication state' -> 'peering, and allications — the outward acts, of which publication is one'. L7/0.md lines 4 and 87, and once in each of the other 54 L7 sheets that carry it (including the three moved sheets; not ct-lane/0.md or prior-art-lane/0.md, which do not carry it).
          - **locator**: autonomous@origin/main: git grep -c -F 'peering, and publication state' ; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:§37
        - item 13
          - **step**: 12. Sweep: 'the L7 publications branch' (8 occurrences, 5 files)
          - **detail**: -> 'L7/allications/publications/' at L7/0.md:112,135; L7/peering/0.md:10; L7/peering/public/0.md:10,23; L7/peering/public/egress/0.md:14; L7/allications/publications/0.md:10 (twice).
          - **locator**: autonomous@origin/main: lines as listed ; 7lm@origin/main:L7/allications/publications/0.md:10
        - item 14
          - **step**: 13. Sweep: the remaining counted phrases
          - **detail**: 'peering, and publications become addressable' -> 'peering, and allications become addressable' (2: L7/0.md:6,198). 'publications and release identity' -> 'allications: the outward acts, of which publication is one' (2: L7/0.md:34; publications/0.md:8). 'access, restrictions' -> 'access, controlled' (8: L7/0.md:32 and line 8 of the seven governance sheets). 'access, and restrictions' -> 'access, and controlled conditions' (2: L7/peering/0.md:28; L8/L6/0.md:80). 'licensing and restrictions folders': 0, nothing to do.
          - **locator**: autonomous@origin/main: lines as listed ; 7lm@origin/main:L7/0.md:6,35,37,217 ; 7lm@origin/main:L8/L6/0.md:87
        - item 15
          - **step**: 14. The retired cells quoted in the controlled sheet
          - **detail**: L7/governance/controlled/0.md line 3 (Object) and line 8 (quoted cell): 'Directory for restrictions that constrain' -> 'Directory for restrictions and other conditions that constrain'. Line 14: 'Keeps restrictions explicit' -> 'Keeps what is controlled explicit'. Leave the permitted-action quote on line 8 and the word 'restriction' in the sheet's body.
          - **locator**: autonomous@origin/main:L7/governance/restrictions/0.md:3,8,14 ; 7lm@origin/main:L7/governance/controlled/0.md:3,8,14
        - item 16
          - **step**: 15. The three uncounted desk statements
          - **detail**: README.md:9 'peering, publications.' -> 'peering, allications.' (keep this repository's copyright parenthesis). L7/0.md:123 'peering, and publications.' -> 'peering, and allications — the outward acts, of which publication is one.' L7/0.md:223: the path is fixed by step 7; whether the bullet's label stays 'publications' is this repository's own wording (the scaffold has no Holdings section).
          - **locator**: autonomous@origin/main:README.md:9 ; :L7/0.md:123,223 ; 7lm@origin/main:README.md:9 ; 7lm@origin/main:L7/0.md:138
        - item 17
          - **step**: 16. Leave alone
          - **detail**: Everything under L8/L6/history/ and L8/L6/retired/ (two history files name L7/publications and keep it); the owner's words anywhere; every first line not listed in step 3; 'apply public/legal permissions and restrictions' (5 places); 'execution restrictions' (L8/L2/0.md:17); 'publications' where the scaffold kept it (L7/0.md:3,23,93,139,229; L8/0.md:99; L8/L5/research/0.md:32; governance/0.md:44); third-party text and URLs under L7/provenance/prior-art/, staging-records/ and L8/L5/research/review/; the seven binder payload files; L8/L0/semantics/definitions/AUTONOMOUS.md; the Q-6 block; .gitignore.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:§25 (Not propagated), §37 (Not changed)
        - item 18
          - **step**: 17. Record the pass
          - **detail**: Append '## 14. <date> — <title>' to L8/L6/history/harmonization-2026-09-05.md in the same commit: the owner's words as written, what moved, the six sheets, the per-phrase counts actually applied, what was not changed, and the sheet count the check reports. No new history file, so L8/L6/history/0.md needs no new holding. The scaffold's specification line 950 ('not yet mirrored') then becomes out of date; that is a scaffold change and not part of this pass.
          - **locator**: autonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:169 (§13, the form to follow) ; 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:950
        - item 19
          - **step**: 18. Verify
          - **detail**: On the result, with the live-text excludes: zero hits for 'L7/publications', 'governance/restrictions', 'restrictions/', 'peering, and publication state', 'the L7 publications branch', 'publications become addressable', 'publications and release identity', 'access, restrictions', 'access, and restrictions', 'and L7/allications/publications/.' (the beta's misquotation). 'publications/' outside 'allications/publications' only in the 16 URL lines and the new tree and table lines. Run the check's three steps: no conflict markers, canonical root, 103 sheets checked, 71 positions sheeted. Six directories remain unsheeted notices (three binder, three autonomous-theory), as on main.
          - **locator**: 7lm@origin/main:.github/workflows/integrity.yml:13-69
      - **open_questions**
        - PR numbers and states were not verifiable offline. Only the branches were read: origin/claude/no-deletion-fix-2026-09-07 (one commit, 2026-09-07, USO/ paths) and origin/claude/scholarly-pair-baseline-k8ap82 (one commit, 2026-09-14). The scope text calls them open PR #27 and closed PR #29; the background also gives #27 as a closed draft on auditonomous.
        - Does 'physically in step' stop at the restructure and sweep (§25, §37), or does it include the scaffold's other L7/0.md content the exemplar lacks (the FIRST_IS_ALWAYS_0 and name-as-design bullets, the packet reading, the 'Many intelligences at one face' note, the private-repos heading)? Those are content, not names, and nothing in the scaffold's record says exemplars take them.
        - Must the exemplar's check be the scaffold's file byte for byte apart from the Q-6 block? The header comment at line 5 still reads 'USO/l6/history/'; the exemplar's own §13 listed the check as not changed, while the scaffold changed that line on 2026-09-20.
        - Which text do the six new allications sheets carry: the scaffold's sheets verbatim (with the Standing pointer redirected to this repository's record), or exemplar-form sheets with Holdings sections like the rest of this repository's L7?
        - The scaffold's §25 says autonomous names the former paths in 24 files, 12 with governance/restrictions. Counted now on an unchanged main: 23 files for L7/publications, 13 for governance/restrictions, 29 for either. I could not reconstruct how 24 and 12 were counted.
        - L7/publications/0.md:43 on main says the harmonized specification is filed at L8/L4/work/writing/, which is false for this repository. It moves with the sheet; whether the mirroring pass corrects it or only records it is not covered by the scaffold's procedure.
        - The label of the Holdings bullet at L7/0.md:223 ('publications') and the record's open item 'binder/internal/ at publications versus L4 writing' both sit on the branch that moves; neither is settled by the scaffold's procedure.
        - Whether the beta's class (b) and (c) content is wanted at all is the owner's decision. Its binding pins scaffold commit 4ca3edb on the unmerged beta/common-contracts-r1-r6 branch, so it follows a candidate of the model and not main c9dc061.
        - PR #27's content (the catch-all sheets stop asserting nothing is deleted) is not on main and conflicts with main in two files. The beta rewrote one of the same sentences differently (L8/L5/research/review/0.md:41). Which wording stands is undecided.
    - item 10
      - **key**: exemplar-auditonomous
      - **facts**: 63
      - **checklist**
        - item 1
          - **step**: 0. Preconditions (the owner's)
          - **detail**: The model's rule is that the exemplar is mirrored by hand when the owner judges the scaffold close. Work from auditonomous main 2165144 on a new branch. Decide first what happens to PR #25 (USO/ paths, conflicts in two files) and PR #27 (closed; adds 5 more files with former names). Decide whether anything is taken from the beta candidate; this checklist assumes main as the base and the model's main as the target.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:336,346
        - item 2
          - **step**: 1. Move the governance position (tracked rename)
          - **detail**: git mv L7/governance/restrictions L7/governance/controlled. One file: 0.md.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:321
        - item 3
          - **step**: 2. Move the publications position (tracked rename)
          - **detail**: Create L7/allications/ and git mv L7/publications L7/allications/publications. Five files: 0.md, binder/0.md, binder/README.md, binder/internal/README.md, binder/press-kit/README.md. The three binder READMEs move byte for byte and are not edited.
          - **locator**: auditonomous@origin/main:L7/publications/ (ls-tree)
        - item 4
          - **step**: 3. Head the three moved sheets by their new paths
          - **detail**: Line 1 and the Path field on line 4 of each: '# L7/governance/controlled/'; '# L7/allications/publications/'; '# L7/allications/publications/binder/'. Six lines in three files. These six are among the counts in steps 5 and 6.
          - **locator**: auditonomous@origin/main:L7/governance/restrictions/0.md:1,4; L7/publications/0.md:1,4; L7/publications/binder/0.md:1,4
        - item 5
          - **step**: 4. Write the six missing sheets
          - **detail**: L7/allications/0.md, L7/allications/applications/0.md, communications/0.md, specifications/0.md, notifications/0.md, participations/0.md, each with first line '# <path>/'. Source: the model's sheets at the same paths (39, 36, 37, 36, 36, 37 lines). One line is scaffold-specific and needs this repository's date and record: allications/0.md:38. Sheets go from 78 to 84; L7 from 37 to 43.
          - **locator**: 7lm@origin/main:L7/allications/0.md:1-39 (line 38 names harmonization-2026-09-04.md section 25)
        - item 6
          - **step**: 5. Propagate the publications path
          - **detail**: `L7/publications/` -> `L7/allications/publications/`: 23 occurrences in 19 files (W1 less the CI line and the two canonical-branches sentences), including the 4 self-lines of step 3, `L7/publications/binder/` at L7/0.md:223 and the press-kit path at L7/peering/public/egress/0.md:31.
          - **locator**: auditonomous@origin/main: lines listed in fact W1
        - item 7
          - **step**: 6. Propagate the governance path
          - **detail**: `governance/restrictions` -> `governance/controlled`: 15 occurrences in 12 files (W2 less the CI line), including the 2 self-lines of step 3, the sheet staging-records/0.md:30, L7/provenance/sources/0.md:16 and L8/L4/work/computation/0.md:38. L7/0.md:105 is handled as a whole row in step 8.
          - **locator**: auditonomous@origin/main: lines listed in fact W2
        - item 8
          - **step**: 7. Canonical-branches sentence
          - **detail**: 'and L7/publications/.' -> 'and L7/allications/.' Two occurrences: L7/0.md:14 and L7/peering/0.md:8.
          - **locator**: 7lm@origin/main:L7/0.md:16
        - item 9
          - **step**: 8. Redraw L7/0.md
          - **detail**: Tree: line 66 'restrictions/0' -> 'controlled/0'; line 82 'publications/0' -> 'allications/0' with six children (publications, applications, communications, specifications, notifications, participations). Table: row 105 becomes the model's governance/controlled/ row; row 115 becomes the model's seven rows (allications/ and its six). Line 123: 'peering, and publications.' -> 'peering, and allications — the outward acts, of which publication is one.'
          - **locator**: 7lm@origin/main:L7/0.md:69,85-91,114,124-130,138
        - item 10
          - **step**: 9. Folder name in prose
          - **detail**: `restrictions/` -> `controlled/` in L7/governance/0.md, two occurrences: line 8 (the six positions) and line 32 (Holdings: '`licensing/` and `restrictions/` are admissible positions').
          - **locator**: auditonomous@origin/main:L7/governance/0.md:8,32
        - item 11
          - **step**: 10. Sweep: the boundary sentence
          - **detail**: 'peering, and publication state' -> 'peering, and allications — the outward acts, of which publication is one': 38 occurrences in 37 files (L7/0.md lines 4 and 87; one in each other L7 sheet).
          - **locator**: auditonomous@origin/main: fact W4
        - item 12
          - **step**: 11. Sweep: the publications branch
          - **detail**: 'the L7 publications branch' -> 'L7/allications/publications/': 9 occurrences in 6 files (L7/0.md:112,135; peering/0.md:10; peering/public/0.md:10,23; public/egress/0.md:14; public/egress/peer-1/object-1/0.md:8; publications/0.md:10 twice).
          - **locator**: auditonomous@origin/main: fact W5
        - item 13
          - **step**: 12. Sweep: the smaller phrases
          - **detail**: 'peering, and publications become addressable' -> 'peering, and allications become addressable' (2: L7/0.md:6,198). 'publications and release identity' -> 'allications: the outward acts, of which publication is one' (2: L7/0.md:34; publications/0.md:8). 'access, restrictions' -> 'access, controlled' (8: L7/0.md:32 and line 8 of seven governance sheets). 'access, and restrictions' -> 'access, and controlled conditions' (2: L7/peering/0.md:28; L8/L6/0.md:80). 'licensing and restrictions folders': 0, nothing to do.
          - **locator**: auditonomous@origin/main: fact W6
        - item 14
          - **step**: 13. The controlled sheet's two retired cells
          - **detail**: In L7/governance/controlled/0.md, line 3 and the quotation on line 8: 'Directory for restrictions and other conditions that constrain external disclosure, use, transfer, or handling.' Line 14 quotation: 'Keeps what is controlled explicit and machine-addressable without redefining the underlying research.'
          - **locator**: 7lm@origin/main:L7/governance/controlled/0.md:3,8,14
        - item 15
          - **step**: 14. README
          - **detail**: Line 9: 'peering, publications.' -> 'peering, allications.' One occurrence. Nothing else in the README names the desk's branches.
          - **locator**: auditonomous@origin/main:README.md:9; 7lm@origin/main:README.md:9
        - item 16
          - **step**: 15. The one CI check
          - **detail**: Make .github/workflows/integrity.yml identical to the model's main file. Five differences: line 5 comment (L8/L6/history/); line 33 comment; line 48 controlled; line 50 replaced by the eight peer positions and the seven allications positions. 57 positions become 71. Keep the USO|L8 dual form, as the model's main does.
          - **locator**: 7lm@origin/main:.github/workflows/integrity.yml:5,33,48,50,51
        - item 17
          - **step**: 16. Leave alone
          - **detail**: Everything under L8/L6/history/ and L8/L6/retired/ (7LM_ROUTING_PLAN 6 lines and the record's line 35 keep the former paths). The owner's words. Every other sheet's first line. 'restrictions' as a kind of condition and 'execution restrictions' at L8/L2/0.md:17. The Object and Function lines of L7/0.md and L8/0.md:99. The staging records beneath staging-records/, the sources LEDGER.md, the binder READMEs, the peer objects, the definition, the pinned binding, the dated research records.
          - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:498,508; auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:170
        - item 18
          - **step**: 17. Record the pass
          - **detail**: Append '## 13. <date> — <title>' to L8/L6/history/harmonization-2026-09-05.md: the owner's words as written, the two moves, the six sheets, each phrase pair with its count, the file total, what was not changed, and how it was checked. Do not edit sections 1 to 12.
          - **locator**: auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:162-174 (the form of section 12)
        - item 19
          - **step**: 18. Verify
          - **detail**: Expected after the pass: every phrase of steps 5 to 14 greps to 0 in live text; the records still hold their former paths; 84 sheets, each headed by its path; all 71 positions sheeted; root unchanged; 12 unsheeted directories outside retired sets, the two binder ones now under L7/allications/publications/binder/. Files touched: the 44 of fact W11 (three of them renamed), 3 renamed only, 6 new, and the record.
          - **locator**: 7lm@origin/main:.github/workflows/integrity.yml:13-69
        - item 20
          - **step**: 19. Afterwards, on the model's side (the owner's)
          - **detail**: The specification's paragraph on Auditonomous still says the restructure is not mirrored. The precedent of the rename pass is that the sentence is struck in the same pass; that is an edit to aybllc/7lm, not to this repository.
          - **locator**: 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:958; auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:174
      - **open_questions**
        - Are the six new sheets to be the model's text verbatim, or adapted? The exemplar's sheets carry a Holdings section the model's lack, and the model's allications/0.md:38 points at the scaffold's own record and date.
        - In L7/0.md Holdings (lines 218-223), is the fourth bullet's label 'publications' to become 'allications'? The model has no Holdings section to copy; beta kept 'publications' and changed only the path.
        - Does this pass carry only the restructure and sweep (model record sections 25 and 37), or also the model's other changes to shared sheets since 2026-09-12? The model's L7/0.md has lines the exemplar lacks (FIRST is 0, the name as design, the packet reading, at lines 13, 14, 18) and section 37 also added an author note and changed the introductory sentence. I did not compare the L8 sheets line by line against the model's.
        - The model's record (section 25) counts 21 Auditonomous files naming former paths. I count 20 live files for L7/publications (22 with the two records) and 13 for governance/restrictions (14 with one record); the union of the two paths in live text is 26 files. The 13 agrees; I could not reproduce the 21.
        - Are the five sheet-against-tree statements on main (62 rows against 60; 'the ledger has no rows'; lineage 'empty'; computation 'empty at present'; the specification 'filed' at L8/L4/work/writing/) to be corrected in this pass or separately? They are not part of the restructure, and the model's specification also says 62.
        - What becomes of the beta candidate's research objects and its edits to the definition, Q13 and CONTRADICTIONS.md? They rest on commits 4ca3edb (7lm beta) and 805cd42 (autonomous beta), which are on neither repository's main, and they act on items the record leaves to the owner.
        - If PR #27's roadmap material is revived, the sweep extends to 49 files, and four of its new files (book/0.md, ch01, papers/0.md, the roadmap) name L7/publications/ or governance/restrictions. The roadmap file is dated 2026-09-13 and sits in the catch-all: is it live text or a dated record?
        - PR #25 is still open on USO/ paths. Its L8/L6/0.md clarification merges cleanly, but its two L5 sheets conflict with main. Whether it is rebuilt, closed or superseded is not settled by anything I read.
        - The date and title of section 13, and the owner's words to quote in it, are the owner's. The request of 2026-11-11 is the only instruction I have seen for this pass.
    - item 11
      - **key**: timeline
      - **facts**: 51
      - **checklist**
        - item 1
          - **step**: 2026-09-11 23:25:56 -0700 (09-12 06:25 UTC) | 7lm PR #11 merged, 67bb795
          - **detail**: PHYSICAL + WORDS + FILED MATERIAL. USO/ -> L8/, l0..l6 -> L0..L6; specification version 12 September; field guide filed at L8/L0/pedagogy/. Adopter: same rename (done, next two rows).
          - **locator**: 7lm@67bb795
        - item 2
          - **step**: 2026-09-11 23:25:59 -0700 | autonomous PR #28 merged, c9076c3
          - **detail**: PHYSICAL + WORDS. The rename pass in the exemplar: 126 renames, 52 modified. Last commit on autonomous main. In step with the scaffold at this moment.
          - **locator**: autonomous@c9076c3
        - item 3
          - **step**: 2026-09-11 23:26:02 -0700 | auditonomous PR #26 merged, 2165144
          - **detail**: PHYSICAL + WORDS. The rename pass in the exemplar: 92 renames, 34 modified. Last commit on auditonomous main. CI file byte-identical to scaffold@67bb795.
          - **locator**: auditonomous@2165144
        - item 4
          - **step**: 2026-09-12 10:09:55 -0700 | 7lm PR #12 merged, b85d2e0
          - **detail**: RULE + WORDS. Peers and objects count from 1, layers from 0. No path changed. Adopter: nothing; exemplars already number from peer-1 and carry no statement on the question.
          - **locator**: 7lm@b85d2e0; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:190-194
        - item 5
          - **step**: 2026-09-13 20:37 to 2026-09-14 02:04 UTC | auditonomous branch claude/book-structure-roadmap-k8ap82, 9259c18
          - **detail**: FILED MATERIAL (exemplar content, unmerged; draft PR #27 per the task). Book and manuscript source tree, vocabulary paper, roadmap; 176 files. Not a model change.
          - **locator**: auditonomous@origin/claude/book-structure-roadmap-k8ap82
        - item 6
          - **step**: 2026-09-14 01:57:47 UTC | autonomous branch claude/scholarly-pair-baseline-k8ap82, 9b49910
          - **detail**: FILED MATERIAL + WORDS (exemplar content, unmerged). Baseline paper and a read-only-exemplar declaration written at L7/governance/restrictions/0.md (former name). Not a model change.
          - **locator**: autonomous@9b49910
        - item 7
          - **step**: 2026-09-19 01:36:36 -0700 | owner's direct edit to 7lm main, 0738519
          - **detail**: WORDS (the drawn tree in L7/0.md only): restrictions/0 -> controlled/0; publications/0 -> allications/0 with six children, 'notificattions' as typed. Directories not yet moved. Adopter: nothing until PR #17.
          - **locator**: 7lm@0738519:L7/0.md:68,84-90
        - item 8
          - **step**: 2026-09-19 01:37:54 -0700 | 7lm PR #13 merged, 6600f77
          - **detail**: WORDS + FILED MATERIAL. Specification version 13 September (packet reading), field guide rewritten, plate sheet and generator added. 'No position, count or path changed'. Adopter: nothing required.
          - **locator**: 7lm@6600f77
        - item 9
          - **step**: 2026-09-19 10:25:17 -0700 | 7lm PR #14 merged, 68c550e
          - **detail**: PHYSICAL (scaffold only, non-canonical) + WORDS. L8/L6/in/ created; in/ named as an optional inbox. Adopter: nothing required.
          - **locator**: 7lm@68c550e
        - item 10
          - **step**: 2026-09-19 10:39:58 -0700 | 7lm PR #15 merged, 22327cb
          - **detail**: WORDS. Record section 24; L8/L6/0.md names in/. Adopter: nothing.
          - **locator**: 7lm@22327cb
        - item 11
          - **step**: 2026-09-19 10:53:11 -0700 | 7lm PR #16 merged, e22c5fc
          - **detail**: FILED MATERIAL. uha-ommp-exemplar.html at L7/provenance/prior-art/. Adopter: nothing.
          - **locator**: 7lm@e22c5fc
        - item 12
          - **step**: 2026-09-20 13:31:26 -0700 | 7lm PR #17 merged, 0d1ec40
          - **detail**: PHYSICAL + WORDS + CI. L7/publications/ -> L7/allications/publications/; restrictions/ -> controlled/; six new sheets; specification version 20 September; canon list updated. Adopter: the two moves, six sheets, canon list. NOT yet on either exemplar main.
          - **locator**: 7lm@0d1ec40; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:315-331
        - item 13
          - **step**: 2026-09-20 13:32:08 -0700 | 7lm PR #18 merged, 6609f38
          - **detail**: RULE + WORDS + PHYSICAL (scaffold only) + CI. Field guide moved to L8/L6/; sheet templates added; rules of sections 26-31, 36; prose sweep of 44 files (section 37); canon list to 71 (eight peer-1/object-1 positions, already sheeted in both exemplars). Adopter: prose names and canon list; mirror by hand when the owner says.
          - **locator**: 7lm@6609f38; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:334-510
        - item 14
          - **step**: 2026-09-20 17:27:46 to 17:59:53 -0700 | 7lm branch audit/peering-descriptive-reframe-2026-09-20, 118 EDM commits to 83ad204
          - **detail**: WORDS (unmerged candidate). 75 files reworded toward descriptive peering semantics; no path change. Not the model of record.
          - **locator**: 7lm@83ad204
        - item 15
          - **step**: 2026-09-20 21:24:52 UTC | 7lm branch copilot/create-error-list, 1e2fe77
          - **detail**: FILED MATERIAL (unmerged). L8/L5/research/review/7lm-audit-recommendations.md, 96 recommendations.
          - **locator**: 7lm@1e2fe77
        - item 16
          - **step**: 2026-10-05 20:33:36 -0700 | owner's direct edit to 7lm main, 2e5a6d6
          - **detail**: WORDS. One heading added to L7/0.md line 159: 'THESE REPOS BELOW ARE PRIVATE THUS WILL RETURN 404 UNLESS YOU HAVE ACCESS.' Adopter: nothing.
          - **locator**: 7lm@2e5a6d6:L7/0.md:159
        - item 17
          - **step**: 2026-10-06 07:15 to 07:50 UTC | 7lm branch ccr-00099fac-hjosbo (PR #19 per the record), c25c864..ed77d9c
          - **detail**: WORDS + FILED MATERIAL (unmerged). 'Public face agnostic' sweep of 47 files; adds .github/release.sh and release.yml; record section 38.
          - **locator**: 7lm@ed77d9c
        - item 18
          - **step**: 2026-10-17 11:13 to 13:04 UTC | 7lm branch ccr-9391bd81-f2enmj (PR #20 per the task), 574500d..c9638a9
          - **detail**: PHYSICAL (scaffold only, unmerged). Field guide retired to L8/L6/retired/field-guide-2026-09-20/; hard rule into L8/L6/0.md; record sections 38-40. Merge commits b5c3984 and 3555866 pushed onto the PR #19 and audit branches the same day.
          - **locator**: 7lm@origin/ccr-9391bd81-f2enmj
        - item 19
          - **step**: 2026-10-31 04:16:20 UTC | 7lm branch ccr-9a67809a-iwii3n, c6d598a
          - **detail**: FILED MATERIAL. The layer lists written (merged 11 Nov as PR #21).
          - **locator**: 7lm@c6d598a
        - item 20
          - **step**: 2026-11-02 20:53:22 -0800 | 7lm beta commit 4ca3edb on beta/common-contracts-r1-r6
          - **detail**: WORDS + CI + FILED MATERIAL (unmerged candidate). 'Approved R1-R6' corrections to specification, guide, sheets; CI requires L8/uppercase; eight beta research files. This is 'common architecture 4ca3edb'.
          - **locator**: 7lm@4ca3edb
        - item 21
          - **step**: 2026-11-02 21:03:03 -0800 | autonomous beta commit 805cd42
          - **detail**: PHYSICAL + WORDS + FILED MATERIAL (unmerged candidate). L7 restructure applied in the exemplar plus beta research objects; pins 4ca3edb; binding.json left 'integration-required'.
          - **locator**: autonomous@805cd42
        - item 22
          - **step**: 2026-11-02 21:05:23 -0800 | autonomous beta commit e64b382
          - **detail**: WORDS (unmerged candidate). binding.json set to 'pinned' with producer 805cd42 and code/result SHA-256 (verified against the blobs).
          - **locator**: autonomous@e64b382:L7/peering/public/egress/peer-1/object-2/binding.json
        - item 23
          - **step**: 2026-11-02 21:08:36 -0800 | auditonomous beta commit 714480d
          - **detail**: PHYSICAL + WORDS + FILED MATERIAL (unmerged candidate). L7 restructure applied plus beta research objects; ingress binding pins autonomous 805cd42 and architecture 4ca3edb; CI byte-identical to the scaffold beta's.
          - **locator**: auditonomous@714480d
        - item 24
          - **step**: 2026-11-03 08:58:01 -0800 | 7lm beta commit 97314c5
          - **detail**: WORDS (unmerged candidate). 18 sheets edited for research-housing guidance. Cited by no exemplar binding.
          - **locator**: 7lm@97314c5
        - item 25
          - **step**: 2026-11-11 10:08:11 -0800 (18:08 UTC) | 7lm PR #21 merged, c9dc061
          - **detail**: FILED MATERIAL. L8/L6/in/7lm-layer-lists.md, a proposal; tree otherwise identical to 2e5a6d6. Adopter: nothing.
          - **locator**: 7lm@c9dc061
        - item 26
          - **step**: 2026-11-11 18:33:28 UTC | autonomous LOCAL-ONLY commit 8257118 on refs/heads/ccr-9391bd81-f2enmj
          - **detail**: PHYSICAL + WORDS + CI (unpushed, on no remote). L7 restructure mirrored by hand on c9076c3: two moves, six sheets, 71-position canon list, record section 14.
          - **locator**: autonomous@8257118
        - item 27
          - **step**: 2026-11-11 18:34:37 UTC | auditonomous LOCAL-ONLY commit f2d5b37 on refs/heads/ccr-9391bd81-f2enmj
          - **detail**: PHYSICAL + WORDS + CI (unpushed, on no remote). L7 restructure mirrored by hand on 2165144: two moves, six sheets, CI replaced by the scaffold's file byte for byte, record section 13.
          - **locator**: auditonomous@f2d5b37
      - **open_questions**
        - Pull-request numbers and states for unmerged branches cannot be read from git: #19 (ccr-00099fac-hjosbo) is named in the record on the PR #20 branch; #20 and #27, and 'open'/'closed', rest on the task's statement. No PR number was found for autonomous claude/scholarly-pair-baseline-k8ap82 or for 7lm copilot/create-error-list.
        - 'Made by Codex' for the beta branches is supported only by one sentence in 7lm@origin/beta/common-contracts-r1-r6:L8/L6/history/specification-history.md:106; every beta commit's git author and committer is EDM. The 'approved R1-R6' approval itself (the owner's words) was not found quoted in that file; I did not search the rest of the beta tree for it.
        - Two competing, unmerged implementations of the exemplar mirror now exist: the beta branches of 2 Nov (which also add research objects and pin scaffold 4ca3edb, a commit not on scaffold main) and the local-only commits 8257118 / f2d5b37 of 11 Nov (which mirror only the L7 restructure against scaffold main). Which is the intended route is the owner's decision; I did not compare their sheet texts.
        - The exemplar betas pin 4ca3edb, not the scaffold beta's tip 97314c5, and the scaffold beta forks from 2e5a6d6 so lacks PR #21. Whether the owner regards the model 'changed' by the beta (R1-R6) or only by what is on main (c9dc061) is not settled by the history.
        - The scaffold record (section 25, line 329) counts former-name files as 24 and 21, with governance/restrictions in 12 and 13; my git grep -l on exemplar main gives 25/22 and 13/14. The counting method behind the record's figures was not found.
        - The scaffold's harmonization record on main has no section for the owner's edit 2e5a6d6 (5 Oct) or for PR #21 (11 Nov); it ends at section 37. Sections 38-40 exist only on unmerged branches. Not found on main: looked at headings of 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md.
        - The local-only exemplar commits carry this session's Claude-Session trailer; I read them as git objects only and did not verify their contents beyond the commit message, name-status, the 71-position sheet check and the CI blob id.
- **workflowProgress**
  - item 1
    - **type**: workflow_phase
    - **index**: 1
    - **title**: Read
  - item 2
    - **type**: workflow_phase
    - **index**: 2
    - **title**: Synthesize
  - item 3
    - **type**: workflow_phase
    - **index**: 3
    - **title**: Verify
  - item 4
    - **type**: workflow_phase
    - **index**: 4
    - **title**: Final
  - item 5
    - **type**: workflow_agent
    - **index**: 1
    - **label**: read:spec-A
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: af5d6a375fce05162
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794421359789
    - **queuedAt**: 1794421359744
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: The specification /home/user/7lm@origin/main:L8/L4/work/wri…
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794421571421
    - **tokens**: 100070
    - **toolCalls**: 12
    - **durationMs**: 211630
    - **resultPreview**: {"scope":"The specification /home/user/7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md, lines 1-520 of 1003 (front matter, outline, canonical topology, L0, L1, L2, L3 sheets), read from git objects only; plus the diff of that file origin/main -> origin/beta/common-contracts-r1-r6 (6 hunks, 4 inside lines 1-520). Cross-checks made outside the range: ls-tree of origin…
  - item 6
    - **type**: workflow_agent
    - **index**: 2
    - **label**: read:spec-B
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: affada621d57e575a
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794421359789
    - **queuedAt**: 1794421359744
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: The specification at /home/user/7lm@origin/main:L8/L4/work/…
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794421641423
    - **tokens**: 104744
    - **toolCalls**: 11
    - **durationMs**: 278385
    - **resultPreview**: {"scope":"The specification at /home/user/7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md (1003 lines), lines 500-1003 read in full, plus lines 355-499 because the L1, L2 and L3 sheets asked for under (a) start there. Also the diff of that file between origin/main and origin/beta/common-contracts-r1-r6 (all six hunks; two fall inside lines 500+). Cross-reference che…
  - item 7
    - **type**: workflow_agent
    - **index**: 3
    - **label**: read:record-A
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: a671a65e0c3c7a196
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794421571474
    - **queuedAt**: 1794421359745
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: Scaffold record /home/user/7lm@origin/main:L8/L6/history/ha…
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794421934694
    - **tokens**: 139945
    - **toolCalls**: 18
    - **durationMs**: 363220
    - **resultPreview**: {"scope":"Scaffold record /home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md lines 1-294 (preamble and sections 1-23, 2026-09-04 to 2026-09-13) and /home/user/7lm@origin/main:L8/L6/history/sheets-2026-09-07.md (423 lines). Read from git objects only. Cross-reference checks made, and only these: the root trees and integrity.yml of 7lm@origin/main, 7lm@68c550e (the last commit befo…
  - item 8
    - **type**: workflow_agent
    - **index**: 4
    - **label**: read:record-B
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: a4c498f0057910992
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794421641438
    - **queuedAt**: 1794421359745
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: Read from git objects only: /home/user/7lm@origin/main:L8/L…
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794422014898
    - **tokens**: 138883
    - **toolCalls**: 21
    - **durationMs**: 373460
    - **resultPreview**: {"scope":"Read from git objects only: /home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md lines 295-510 (sections 24-37); /home/user/7lm@origin/main:L8/L6/history/specification-history.md (all 102 lines); and the 10 lines origin/beta/common-contracts-r1-r6 adds to that file. Cross-checks made against the two commits that performed the work (7lm 606d4b3 the restructure, bbb04dd the…
  - item 9
    - **type**: workflow_agent
    - **index**: 5
    - **label**: read:sheets-L7
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: aa2428f1a5390cb0c
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794421934711
    - **queuedAt**: 1794421359745
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: Every sheet (0.md) under L7 on /home/user/7lm@origin/main (…
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794422309868
    - **tokens**: 146094
    - **toolCalls**: 17
    - **durationMs**: 375155
    - **resultPreview**: {"scope":"Every sheet (0.md) under L7 on /home/user/7lm@origin/main (c9dc061): 35 sheets, plus the two non-sheet files under L7 (L7/provenance/sources/source-ledger.md, L7/provenance/prior-art/uha-ommp-exemplar.html); then the diff origin/main..origin/beta/common-contracts-r1-r6 (97314c5) restricted to L7. Read from git objects only. Cross-reference checks made outside scope: .github/workflows/int…
  - item 10
    - **type**: workflow_agent
    - **index**: 6
    - **label**: read:sheets-L8
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: ae226e0f13127bf08
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794422014915
    - **queuedAt**: 1794421359745
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: 7lm@origin/main (c9dc061): README.md; all 40 in-scope L8 sh…
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794422415374
    - **tokens**: 206283
    - **toolCalls**: 22
    - **durationMs**: 400459
    - **resultPreview**: {"scope":"7lm@origin/main (c9dc061): README.md; all 40 in-scope L8 sheets (L8/0.md, L0-L6 layer sheets and every sub-sheet, the three retired-set root sheets, L8/L6/in/0.md); what L8/L0/pedagogy/ and L8/L6/in/ hold (tree); .github/workflows/integrity.yml on main and on origin/beta/common-contracts-r1-r6 (97314c5); the diff origin/main..origin/beta/common-contracts-r1-r6 over L8 (json/docx excluded…
  - item 11
    - **type**: workflow_agent
    - **index**: 7
    - **label**: read:layer-lists
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: a960aefa6d9fe6ebf
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794422309893
    - **queuedAt**: 1794421359745
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: 7lm@origin/main (c9dc061): L8/L6/in/7lm-layer-lists.md (415…
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794422971168
    - **tokens**: 251522
    - **toolCalls**: 45
    - **durationMs**: 661274
    - **resultPreview**: {"scope":"7lm@origin/main (c9dc061): L8/L6/in/7lm-layer-lists.md (415 lines), L8/L6/7lm-sheet-templates.md, L8/L6/7lm-field-guide.md sections 10-14 (lines 369-622), L8/L6/0.md. Checked against the nine layer sheets (L7/0.md, L8/0.md, L8/L0..L6/0.md), the specification, .github/workflows/integrity.yml and README.md on origin/main; against PR #20 (origin/ccr-9391bd81-f2enmj, c9638a9) and the beta ca…
  - item 12
    - **type**: workflow_agent
    - **index**: 8
    - **label**: read:beta-and-prs
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: aac2271b299c1944e
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794422415387
    - **queuedAt**: 1794421359746
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: Everything on the scaffold repository /home/user/7lm that i…
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794422841018
    - **tokens**: 208522
    - **toolCalls**: 29
    - **durationMs**: 425631
    - **resultPreview**: {"scope":"Everything on the scaffold repository /home/user/7lm that is NOT on origin/main (c9dc061): the beta candidate origin/beta/common-contracts-r1-r6 (97314c5, two commits on 2e5a6d6); open draft PR #20 origin/ccr-9391bd81-f2enmj (c9638a9); open draft PR #19 origin/ccr-00099fac-hjosbo (b5c3984); origin/audit/peering-descriptive-reframe-2026-09-20 (3555866); origin/copilot/create-error-list (1…
  - item 13
    - **type**: workflow_agent
    - **index**: 9
    - **label**: read:exemplar-autonomous
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: ab0231e4bd5f9f993
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794422841031
    - **queuedAt**: 1794421359746
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: /home/user/autonomous (aybllc/autonomous): origin/main (c90…
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794423400561
    - **tokens**: 215519
    - **toolCalls**: 44
    - **durationMs**: 559529
    - **resultPreview**: {"scope":"/home/user/autonomous (aybllc/autonomous): origin/main (c9076c3) measured against the model at /home/user/7lm@origin/main (c9dc061); then the unmerged candidate origin/beta/7lm-exemplar-autonomous (e64b382), and the two PR branches origin/claude/no-deletion-fix-2026-09-07 and origin/claude/scholarly-pair-baseline-k8ap82. Git objects only; nothing written in any repository (two git merge-…
  - item 14
    - **type**: workflow_agent
    - **index**: 10
    - **label**: read:exemplar-auditonomous
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: a66b1a2fd85436cdd
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794422971180
    - **queuedAt**: 1794421359746
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: /home/user/auditonomous: origin/main (2165144) against the …
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794423609950
    - **tokens**: 235333
    - **toolCalls**: 50
    - **durationMs**: 638770
    - **resultPreview**: {"scope":"/home/user/auditonomous: origin/main (2165144) against the model at /home/user/7lm@origin/main (c9dc061); then origin/beta/7lm-exemplar-auditonomous (714480d); with PR #25 (origin/claude/no-deletion-fix-2026-09-07, f89bf8a) and PR #27 (origin/claude/book-structure-roadmap-k8ap82, 9259c18). Read-only, git objects only. \"Live text\" = every tracked file except L8/L6/history/, L8/L6/retire…
  - item 15
    - **type**: workflow_agent
    - **index**: 11
    - **label**: read:timeline
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: aad4088daeb2771c3
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794423400573
    - **queuedAt**: 1794421359746
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: Commit history of /home/user/7lm, /home/user/autonomous and…
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794423893143
    - **tokens**: 199000
    - **toolCalls**: 41
    - **durationMs**: 492569
    - **resultPreview**: {"scope":"Commit history of /home/user/7lm, /home/user/autonomous and /home/user/auditonomous from 2026-09-11 to 2026-11-11, every remote branch (plus the local-only branches found in the clones), read from git objects only. Covers: scaffold first-parent history (PRs #11-#21 and the owner's two direct edits), when the exemplars were last in step, every non-main branch, and the three beta branches …
  - item 16
    - **type**: workflow_agent
    - **index**: 12
    - **label**: synthesize
    - **phaseIndex**: 2
    - **phaseTitle**: Synthesize
    - **agentId**: af90dc49500e21778
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794423893200
    - **queuedAt**: 1794423893172
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: **Locator key.** REC = `7lm@origin/main:L8/L6/history/harmo…
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794425460765
    - **tokens**: 540211
    - **toolCalls**: 42
    - **durationMs**: 1567564
    - **resultPreview**: {"report":"**Locator key.** REC = `7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md`. SPEC = `7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md`. CHK = `7lm@origin/main:.github/workflows/integrity.yml`. BETA = `7lm@origin/beta/common-contracts-r1-r6`. The number after a colon is a line.\n\n## The short answer\n\nThe model of record is the scaffold's main at c…
  - item 17
    - **type**: workflow_agent
    - **index**: 13
    - **label**: critic
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a7babd13d39e237dc
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794425460802
    - **queuedAt**: 1794425460780
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794427091892
    - **tokens**: 474903
    - **toolCalls**: 96
    - **durationMs**: 1631089
    - **resultPreview**: {"gaps":[{"severity":"critical","gap":"The owner's instruction of 14 September 2026, which sets the order of work that today's request belongs to, is nowhere in the report. It is recorded only on two closed, unmerged branches, with a read-only exemplar declaration for Autonomous and 23 open owner decisions.","finding":"The words, as written, stand at autonomous@origin/claude/scholarly-pair-baselin…
  - item 18
    - **type**: workflow_agent
    - **index**: 14
    - **label**: verify:K01
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a797d41b8d19d301e
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794425460848
    - **queuedAt**: 1794425460831
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: K01
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794425517100
    - **tokens**: 70083
    - **toolCalls**: 4
    - **durationMs**: 56252
    - **resultPreview**: {"id":"K01","verdict":"stands","reasoning":"Every part of the claim is confirmed from the git objects, and I found no evidence against it.\n\n1. One path differs. `git -C /home/user/7lm diff --name-status 2e5a6d6 origin/main` (origin/main = c9dc0617983e18fb6327d79bd1be8d8b1255aab3) returns one row, `A L8/L6/in/7lm-layer-lists.md`. `--stat` gives 1 file changed, 415 insertions, no deletions. `--raw…
  - item 19
    - **type**: workflow_agent
    - **index**: 15
    - **label**: verify:K02
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a4b2838f017d68aeb
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794425517103
    - **queuedAt**: 1794425460832
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: K02
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794425575814
    - **tokens**: 74735
    - **toolCalls**: 5
    - **durationMs**: 58711
    - **resultPreview**: {"id":"K02","verdict":"stands","reasoning":"Every part of the claim was confirmed from git objects on 7lm@origin/main (c9dc0617983e18fb6327d79bd1be8d8b1255aab3); no counter-evidence found.\n\n1. 71 canonical positions, 35 + 36. 7lm@origin/main:.github/workflows/integrity.yml:47-59 is the `canon=` list (cited locator is exact). Expanded with top=L8, lower=L it yields 71 entries, 71 unique: 35 match…
  - item 20
    - **type**: workflow_agent
    - **index**: 16
    - **label**: verify:K03
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a44f69a0bdf1d440f
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794425575818
    - **queuedAt**: 1794425460832
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: K03
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794425706350
    - **tokens**: 100450
    - **toolCalls**: 9
    - **durationMs**: 130530
    - **resultPreview**: {"id":"K03","verdict":"corrected","reasoning":"Every cited locator checks out, but three parts of the claim are imprecise or true only of a particular ref.\n\nCONFIRMED\n- 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:315 is the heading \"## 25. 2026-09-20 — the L7 restructure: allications, and controlled\". Line 321: \"`L7/publications/` moved to `L7/allications/publications/` and `L7…
  - item 21
    - **type**: workflow_agent
    - **index**: 17
    - **label**: verify:K04
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: ae93ba41d6557150f
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794425706354
    - **queuedAt**: 1794425460832
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: K04
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794425831946
    - **tokens**: 97805
    - **toolCalls**: 10
    - **durationMs**: 125592
    - **resultPreview**: {"id":"K04","verdict":"corrected","reasoning":"Most of K04 is confirmed from the git objects; two parts are imprecise, so the verdict is \"corrected\".\n\n**Confirmed**\n- **Directory tree.** `git ls-tree -r -d --name-only` gives 97 lines for origin/main (c9dc061), 97 for origin/beta/common-contracts-r1-r6 (97314c5) and 97 for 2e5a6d6; the main-versus-beta diff is empty.\n- **71 positions.** The c…
  - item 22
    - **type**: workflow_agent
    - **index**: 18
    - **label**: verify:K05
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a7470ed18d7a8e17e
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794425831952
    - **queuedAt**: 1794425460832
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: K05
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794425976169
    - **tokens**: 102888
    - **toolCalls**: 13
    - **durationMs**: 144216
    - **resultPreview**: {"id":"K05","verdict":"corrected","reasoning":"Every substantive part of the claim is confirmed from git objects, but two points are imprecise as worded, so the verdict is \"corrected\" rather than \"stands\".\n\n**Confirmed**\n\n1. No release claim. 7lm@origin/beta/common-contracts-r1-r6:L8/L6/history/specification-history.md:106 says \"This records the checked common-architecture candidate, not …
  - item 23
    - **type**: workflow_agent
    - **index**: 19
    - **label**: verify:K06
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: ae9b3c5d01e886b8d
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794425976174
    - **queuedAt**: 1794425460832
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: K06
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794426079118
    - **tokens**: 80336
    - **toolCalls**: 7
    - **durationMs**: 102944
    - **resultPreview**: {"id":"K06","verdict":"corrected","reasoning":"Every count and name in the claim is confirmed from git objects. The one correction is scope: \"nothing under L8 is missing or misnamed\" holds only for the 36 canonical L8 positions, not for the whole L8 tree.\n\n**Confirmed**\n- **Canon list:** the scaffold's check lists 71 positions, 35 under L7 and 36 under L8 (7lm@origin/main:.github/workflows/in…
  - item 24
    - **type**: workflow_agent
    - **index**: 20
    - **label**: verify:K07
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a7f37d858dff0ae79
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794426079122
    - **queuedAt**: 1794425460832
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: K07
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794426153309
    - **tokens**: 76373
    - **toolCalls**: 6
    - **durationMs**: 74185
    - **resultPreview**: {"id":"K07","verdict":"corrected","reasoning":"Every figure in the claim reproduces from git objects at autonomous@origin/main (c9076c3). Only one clause is imprecise as written: \"six folders have no sheet\" is true only within the scope of the check's own report step, not of the whole tree. The verdict is \"corrected\" for that scope qualifier alone.\n\n**Phrase counts** (live text, with L8/L6/h…
  - item 25
    - **type**: workflow_agent
    - **index**: 21
    - **label**: verify:K08
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: afd8f4962ae25c5e5
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794426153315
    - **queuedAt**: 1794425460832
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: K08
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794426240567
    - **tokens**: 78019
    - **toolCalls**: 7
    - **durationMs**: 87252
    - **resultPreview**: {"id":"K08","verdict":"corrected","reasoning":"Every count in the claim reproduces from git objects at auditonomous@origin/main (rev-parse = 21651446). One part is imprecise: \"twelve folders have no sheet\" holds only under the check's own reporting rule.\n\n**Phrase counts** (git grep -n/-l/-o -F on origin/main, excluding L8/L6/history, L8/L6/retired, L8/L6/in):\n- 'L7/publications': 26 lines, 2…
  - item 26
    - **type**: workflow_agent
    - **index**: 22
    - **label**: verify:K09
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: aa2fd8396b53955e8
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794426240570
    - **queuedAt**: 1794425460832
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: K09
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794426430613
    - **tokens**: 115083
    - **toolCalls**: 13
    - **durationMs**: 190042
    - **resultPreview**: {"id":"K09","verdict":"corrected","reasoning":"Every cited locator checks out, and the core of the claim is confirmed from git objects. Four parts are imprecise or incomplete, so the claim is corrected rather than left standing.\n\nCONFIRMED\n- Refs and dates: the autonomous beta is two commits on c9076c3 (805cd42 at 2026-11-02 21:03:03 -0800, e64b382 at 21:05:23 -0800); the auditonomous beta is o…
  - item 27
    - **type**: workflow_agent
    - **index**: 23
    - **label**: verify:K10
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: acb1ab55b135261f2
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794426430617
    - **queuedAt**: 1794425460832
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: K10
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794426595050
    - **tokens**: 109464
    - **toolCalls**: 15
    - **durationMs**: 164432
    - **resultPreview**: {"id":"K10","verdict":"corrected","reasoning":"Every part of K10 was re-derived from git objects and confirmed except one imprecision about the Autonomous check, plus two scope limits worth stating.\n\n**Confirmed**\n- **One local commit each, from main.** Autonomous `8257118` has parent `c9076c3` (origin/main) and auditonomous `f2d5b37` has parent `2165144` (origin/main); `rev-list --count origin…
  - item 28
    - **type**: workflow_agent
    - **index**: 24
    - **label**: verify:K11
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a49ec4ff94829c2e8
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794426595053
    - **queuedAt**: 1794425460832
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: K11
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794426730202
    - **tokens**: 85410
    - **toolCalls**: 10
    - **durationMs**: 135149
    - **resultPreview**: {"id":"K11","verdict":"corrected","reasoning":"Every numeric and merge fact in the claim reproduces from the git objects. One phrase is too broad: \"every check file on every branch lists the same 71\" (and, by extension, \"the only directory not on main\") is false for one remote branch the claim does not mention, origin/copilot/create-academic-guide-plan. That branch is not unmerged (it is an an…
  - item 29
    - **type**: workflow_agent
    - **index**: 25
    - **label**: verify:K12
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a05346e68c89db107
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794426730205
    - **queuedAt**: 1794425460832
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: K12
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794426815107
    - **tokens**: 92205
    - **toolCalls**: 7
    - **durationMs**: 84902
    - **resultPreview**: {"id":"K12","verdict":"corrected","reasoning":"Every cited locator is confirmed on 7lm@origin/main (c9dc061), and the four rules are still in force there. Two parts of the claim are imprecise against the same objects, so the verdict is \"corrected\", not \"stands\".\n\n**Confirmed as cited** (all in 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md)\n- :336 (section 26), owner: \"All repos…
  - item 30
    - **type**: workflow_agent
    - **index**: 26
    - **label**: final
    - **phaseIndex**: 4
    - **phaseTitle**: Final
    - **agentId**: ae431d6b28f6df8c9
    - **model**: claude-fable-5-2
    - **state**: done
    - **startedAt**: 1794427091937
    - **queuedAt**: 1794427091901
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: **Locator key.** REC = `7lm@origin/main:L8/L6/history/harmo…
    - **promptPreview**: You are one agent in a READ-ONLY research workflow over three local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network):
      - /home/user/7lm = aybllc/7lm, "the scaffold": the Seven-Layer Model (7LM) itself.
          origin/main = c9dc061 (the model of record; PR #21 merged 2026-11-11). The state last studied was main at 2e5a6d6 (2026-10-05…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794427393892
    - **tokens**: 148821
    - **toolCalls**: 2
    - **durationMs**: 301954
    - **resultPreview**: {"report":"**Locator key.** REC = `7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md`. SPEC = `7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md`. CHK = `7lm@origin/main:.github/workflows/integrity.yml`. GUIDE = `7lm@origin/main:L8/L6/7lm-field-guide.md`. BETA = `7lm@origin/beta/common-contracts-r1-r6`. PR20 = `7lm@origin/ccr-9391bd81-f2enmj`. PR19 = `7lm@orig…
- **totalTokens**: 4192701
- **totalToolCalls**: 556
