# critic

Agent result, as returned. Workflow: The model, read deep. Run `wf_9a60cf50-a5f`. Phase: Verify.

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
