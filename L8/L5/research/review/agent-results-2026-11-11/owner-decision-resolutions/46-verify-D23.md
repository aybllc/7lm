# verify:D23

Agent result, as returned. Workflow: Resolutions for the 23 owner decisions. Run `wf_3293f65c-a92`. Phase: Verify.

- **quotes**
  - item 1
    - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:482
    - **verbatim**: yes
    - **correction**: Verbatim. Context: it opens §36, "standing: the system is not changed without asking", given in the scaffold's own session; it is applied to the exemplars by reading, not by its own words.
  - item 2
    - **locator**: auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:158
    - **verbatim**: yes
    - **correction**: Verbatim. Section 11 is headed "the sheets say what is; the record says what happened", so the resolver is right that it was given about the sheets.
  - item 3
    - **locator**: owner's instruction of 11 November 2026, as typed
    - **verbatim**: yes
    - **correction**: Verbatim against the instruction as typed: "we need to uipdate the autonomous and auditonomous repos phsyciall; to match first ."
  - item 4
    - **locator**: auditonomous@origin/main:L7/publications/binder/0.md:8
    - **verbatim**: yes
    - **correction**: Verbatim. It is the last sentence of line 8. Autonomous's line 8 at the same path ends "The files are the tree's own gates from the earlier layout and are not rewritten.", as the resolver says.
  - item 5
    - **locator**: auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:172
    - **verbatim**: yes
    - **correction**: Verbatim. It is the second sentence of line 172. Autonomous carries the same sentence at :179.
  - item 6
    - **locator**: auditonomous@origin/main:L8/L6/0.md:79
    - **verbatim**: yes
    - **correction**: Verbatim. The same line stands at autonomous@origin/main:L8/L6/0.md:79.
  - item 7
    - **locator**: auditonomous@origin/ccr-9391bd81-f2enmj:L8/L6/history/harmonization-2026-09-05.md:200
    - **verbatim**: yes
    - **correction**: Verbatim. It is the final sentence of line 200.
  - item 8
    - **locator**: autonomous@origin/main:L7/publications/binder/press-kit/README.md:18
    - **verbatim**: yes
    - **correction**: Verbatim. The same line stands at auditonomous@origin/main:L7/publications/binder/press-kit/README.md:18, and auditonomous@origin/main:L7/publications/binder/README.md:11 reads "   [source text withheld from the public copy] beta line given in "against" (autonomous@origin/beta/7lm-exemplar-autonomous:L7/allications/publications/binder/press-kit/README.md:17) is also verbatim.
- **inference_holds**: yes
- **objection**: All eight quotations are verbatim at their locators, and the core inference holds. The decision is not settled by any word of the owner, the standing of 2026-09-20 says to propose rather than apply, and the instruction of 11 November asks for the exemplars to be matched to the changed model (the L7 restructure), not for a sweep of paths from before 5 September. The resolution has three defects.

  (1) The fact base misses a live sheet that states something false in the present tense. auditonomous@origin/main:L7/provenance/sources/0.md:18 reads "as do its siblings: `uso/l6/LEDGER.md` in aybllc/autonomous (rows pinned to `7540a9d6951c`)". On main, autonomous's register stands at L7/provenance/sources/LEDGER.md (autonomous@origin/main:L7/provenance/sources/0.md:10). This is not a stale pointer in a dated or gate file. It is a current sheet misreporting the sibling, the kind the owner's word of 2026-09-07 ("cirrent and relevant for the purpose of using the thing") was given about. It stands unchanged on the PR #28 branch and on the auditonomous beta. The resolver's filter ("leaving out sheets that correctly say 'relocated from'") let it through, because the line is not a "relocated from" line and it is not correct. So the auditonomous count is 11 lines in 7 files, not 10 in 6, and class (b) must include this sheet sentence. The `aybllc/ommp` clause on the same line may still be true and is not this decision's to change.

  (2) The resolver's "bears" for the 11 November word understates what the model of record does. The scaffold's §25 (7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:325, "Twenty-eight live files named the former paths and now name the current ones", corrected to twenty-six at :506) shows the model's practice: a path change is propagated into live files, while records keep their paths. On that reading, "match" can fairly be taken to cover live working files. This favours class (b) once the owner approves; it does not license applying it unasked.

  (3) A word of the owner on Autonomous's status is not weighed. It bears on editing autonomous's MANUSCRIPT.tex and ledgers. It stands only on a closed, unmerged branch, and whether it still governs is decision 2, so class (b) in autonomous should be made conditional on that answer.
- **missed_quotation**: "[source text withheld from the public copy]." (owner, 2026-09-14; autonomous@origin/claude/scholarly-pair-baseline-k8ap82:L8/L6/history/exemplar-2026-09-14.md:7. This is on a closed, unmerged branch; whether it still governs is decision 2.)
- **corrected_resolution**: Change no file now. Put the references to the owner as a proposal in classes (a) and (b). In (a), the three binder gate files (binder/README.md, internal/README.md, press-kit/README.md), the staging READMEs and RECONCILIATION_FROM_L6_2026-08-16.md stay byte for byte, read through L8/L6/0.md:79. Class (b) covers the working files that are not dated records. In both exemplars, FORMULAS_LEDGER.md:23 and datasets-LEDGER.md:21 have `uso/l6/LEDGER.md` replaced by `L7/provenance/sources/LEDGER.md`. In autonomous, so does MANUSCRIPT.tex:50 and :79. In auditonomous, L7/provenance/sources/0.md:18 has "`uso/l6/LEDGER.md` in aybllc/autonomous" corrected to "`L7/provenance/sources/LEDGER.md` in aybllc/autonomous". This last one is a false statement in a live sheet, not a stale pointer, and it is the strongest case in the set. Each change goes in one commit per repository, separate from PR #30 and PR #28, with a line in L8/L6/history/harmonization-2026-09-05.md, and is made only on the owner's word. The autonomous part of (b) is subject to the owner's answer on decision 2, because the order of 14 September 2026 would make Autonomous a read-only exemplar. If the owner wants the binder files corrected too, binder/0.md:8 in each repository is reworded in the same commit.
- **corrected_confidence**: The quotations do not reach it, so the owner must say. The one exception is the false sibling claim at auditonomous L7/provenance/sources/0.md:18: the owner's word of 2026-09-07 on current, usable sheets supports correcting it fairly strongly. It is still to be proposed, not applied, under the standing of 2026-09-20.
