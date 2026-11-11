# verify:D20

Agent result, as returned. Workflow: Resolutions for the 23 owner decisions. Run `wf_3293f65c-a92`. Phase: Verify.

- **quotes**
  - item 1
    - **locator**: owner's instructions of 11 November 2026, as typed ("Get qa hanfle on the research and manuscruipt for Auditonomous but firwst re0ull7lm ... to match first .")
    - **verbatim**: yes
    - **correction**: Verbatim against the task's text of the instruction, and also against the git object auditonomous@origin/ccr-9391bd81-f2enmj:L8/L6/history/harmonization-2026-09-05.md:178, which is the better locator. No change to the wording.
  - item 2
    - **locator**: auditonomous@origin/claude/book-structure-roadmap-k8ap82:L8/L6/history/restore-2026-09-14.md:7
    - **verbatim**: yes
    - **correction**: Verbatim at line 7. Caveat on standing, not wording: this is the owner's message as transcribed by a session in a record on a branch the owner never merged; the same text stands at autonomous@origin/claude/scholarly-pair-baseline-k8ap82:L8/L6/history/exemplar-2026-09-14.md:7, also unmerged. It is on no main.
  - item 3
    - **locator**: auditonomous@origin/claude/book-structure-roadmap-k8ap82:L8/L6/history/restore-2026-09-14.md:13
    - **verbatim**: yes
    - **correction**: Verbatim at line 13. The counts in the bearing were checked and hold: 328 files at 9259c18 against 169 on main; the branch is 0 behind and 5 ahead of main 2165144 (159 added, 17 modified).
  - item 4
    - **locator**: auditonomous@origin/claude/book-structure-roadmap-k8ap82:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:626
    - **verbatim**: yes
    - **correction**: Verbatim at line 626 (row D15). The same cell opens "[source text withheld from the public copy]", i.e. the sentence quoted is the session's own earlier recommendation, not the owner's. The bearing's fact holds: main's L8/L1/state-space/AUDITON_ENVELOPE.md:76 names `definitions/AUDITONOMY.md` and no AUDITONOMY.md is in main's tree.
  - item 5
    - **locator**: auditonomous@origin/claude/book-structure-roadmap-k8ap82:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:587
    - **verbatim**: yes
    - **correction**: Verbatim at line 587, but cut short where it matters. The same cell ends: "[source text withheld from the public copy]". The chapter files are headers only (ch07 is 26 lines). The three drafts with text are on main and are byte-identical on the book branch (they are not among its 17 modified files).
  - item 6
    - **locator**: auditonomous@origin/ccr-9391bd81-f2enmj:L8/L6/history/harmonization-2026-09-05.md:207
    - **verbatim**: yes
    - **correction**: Verbatim at line 207. Seven files are changed on both the book branch and the mirror branch relative to main (L7/0.md, L7/peering/private/ingress/peer-3/object-1/0.md, L7/provenance/sources/0.md, L8/L4/work/computation/0.md, L8/L4/work/writing/0.md, L8/L5/research/findings/0.md, L8/L6/history/0.md), so the later reconciliation is wider than L7/0.md alone.
  - item 7
    - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:482
    - **verbatim**: yes
    - **correction**: Verbatim at line 482 (owner, 2026-09-20). Said of the scaffold ("the system"); its use for an exemplar's closed branch is by analogy.
  - item 8
    - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:303
    - **verbatim**: yes
    - **correction**: Verbatim at line 303. The bearing over-reads it: section 24 (lines 301-303) records a branch that was closed unmerged AND deleted, whose text was extracted into one file under L8/L6/in/ and not revived. Nobody proposes deleting the book branch, and the precedent's actual treatment (enumerate and file, do not merge) cuts against "bring the five commits forward" as much as for reading the branch.
  - item 9
    - **locator**: auditonomous@origin/claude/book-structure-roadmap-k8ap82:L8/L6/history/restore-2026-09-14.md:9 (the 'against' quotation)
    - **verbatim**: yes
    - **correction**: Verbatim at line 9.
  - item 10
    - **locator**: auditonomous@origin/claude/book-structure-roadmap-k8ap82:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:3 ("Nothing here is adopted.")
    - **verbatim**: yes
    - **correction**: Verbatim at line 3.
- **inference_holds**: no
- **objection**: All ten quotations are character for character at their locators, so the resolution does not fail on evidence. It fails on what it leaves out and on one claim overtaken by the repository.

  1. A third base exists and is ignored. auditonomous@origin/beta/7lm-exemplar-auditonomous (714480d, 2 November 2026, author EDM, one commit directly on main 2165144, 0 behind) is the owner's own later candidate. It already makes both L7 moves (L7/publications -> L7/allications/publications, restrictions -> controlled), adds AUDITONOMOUS_BETA_* objects at L0-L6, modifies 33 files, and holds none of the book material (no book/, no manuscript/, no AUDITONOMY.md, no STANDARDS_REGISTER.md, no restore record). The owner's most recent act on this repository took main as base and left the restore out. "Main or the closed book branch" is therefore a false pair, and "revive after the mirror" is under-specified: the mirror record itself says "whichever of the two lands second will need them reconciled" (auditonomous@origin/ccr-9391bd81-f2enmj:L8/L6/history/harmonization-2026-09-05.md:206).

  2. "Run the QA now against 9259c18" is already overtaken. The handle ran on 11 November and is checked in on the mirror branch (tip 428bbaf): auditonomous@origin/ccr-9391bd81-f2enmj:L8/L5/research/review/agent-results-2026-11-11/auditonomous-research-handle/0.md:8 reads "What research exists, layer by layer, on main, on the closed roadmap branch and on the beta candidate". It read three refs, not one, and its own open question is whether the owner accepted the restore (12-read-records.md:951). The live decision is which base findings stand on, not whether to read the book branch.

  3. The restore reversed the owner's own hand. The files it returned were removed by commit 8c98573, whose message reads "Eric's manual prune and promotion (2026-08-14/15), committed on his instruction after session review" and lists "the older manuscripts set" among the removals. The instruction of 14 September does not mention restoring; the session inferred it (restore:9), and PR #27 then closed unmerged. That makes "the closure was the reversal" more than a remote possibility, and the resolution treats the book branch as the default base anyway.

  4. Internal inconsistency in the use of "to match first". The same sentence is used to push the revival after the mirror but not the QA, which is to run "now" while the mirror is an unaccepted draft. The gap is small in practice (the mirror pass says "No research object, no definition, no ledger row and no manuscript file is touched", ccr harmonization-2026-09-05.md:200), but the resolution should say so and not lean on the ordering selectively.

  5. The manuscript claim is overstated. The quoted cell at roadmap:587 ends "no chapter has text"; the book branch's book/ is 27 header files. The drafts that have text are on main already. What the book branch adds for the manuscript is the pruned Blocks set and the plan, not a manuscript.

  6. "What it costs: nothing on disk" contradicts the owner's own word, "have them check in their results periodically so we dont lose them." and "put them in auditonomous too and the public one": results are being committed at the catch-all on the mirror branch.

  7. The section 24 precedent is read one way only (see quotation 8).

  What survives: reading the closed branch as git objects is harmless and useful; nothing should be revived without the owner's word; any revival follows the mirror.
- **missed_quotation**: "All repos should mirror the 7lm. Manually. We update 7lm and focus on it only. No outside updates until we are sure I'm close." (owner, 2026-09-20; 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:336). Also the same day: "We are only from now on updating the 7LM. Lets finish the updates." (7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:329). Both are later than the 14 September order the resolution rests on ("then start Auditonomous") and suspend it. They cut both ways: they give a reason other than rejection for PR #27 never merging, and they mean the only outside work the owner has since reopened is what he named on 11 November, the physical match and a QA handle, not the return of 116 pruned files and a chapter tree to main.
- **corrected_resolution**: Treat the base as three refs, with main as the base of record. The reading is already done: the handle of 11 November read main 2165144, the closed book branch 9259c18 and the owner's beta candidate 714480d as git objects and is checked in at the catch-all on the mirror branch. Keep it that way: every finding tagged "on main", "book branch only" or "beta only"; findings that rest only on book-branch files (the 116 restored files, the header-only chapter tree, the vocabulary paper, roadmap decisions D1-D23) stay PARKED and are not treated as standing until the owner says whether the restore of 14 September is accepted. Do not revive, rebase or reopen the book branch. Put three questions to the owner, in this order: (1) was closing PR #27 a rejection of the restore, which returned files his own prune of 15 August (8c98573) removed, or a pause under "No outside updates until we are sure I'm close"; (2) which reaches main first, the hand mirror (draft PR #28) or his beta candidate 714480d, since both make the same L7 moves with different wording and the second to land must be reconciled; (3) only after both answers, whether the five book commits come forward as a new draft pull request on whatever main then is (seven files overlap the mirror, thirty name former paths), or whether the scaffold's section 24 treatment is followed instead: the branch's text enumerated into L6 in/ and the branch left closed. Results continue to be checked in as the owner said; the cost is not "nothing on disk".
- **corrected_confidence**: The quotations support reading the closed branch and support doing nothing to it without the owner's word. They do not settle the base: no owner word accepts the restore, and his latest act (the beta candidate on main, without the book material) leans toward main. Owner's word needed on all three questions.
