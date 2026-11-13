# resolve:D18

Agent result, as returned. Workflow: Resolutions for the 23 owner decisions. Run `wf_3293f65c-a92`. Phase: Resolve.

- **decision**: 18. Whether the "not yet mirrored" sentences (SPEC:950, SPEC:958), the restrictions/ wording (SPEC:938), SPEC:934 and GUIDE:474 are corrected in the scaffold, the .docx with them, once the exemplars land.
- **resolution**: Split it. Prepare now, as a proposal with the exact fix and without applying it, the correction of SPEC:938, the last sentence of SPEC:950 and the last sentence of SPEC:958, with the .docx patched by hand in the same commit and an entry in specification-history.md. Apply it only after both exemplar mirrors (autonomous PR #30, auditonomous PR #28) are on their mains and the owner says so. Leave SPEC:934 and GUIDE:474 as they are and put both to the owner: the mirror does not make them true, and the guide is retired verbatim on PR #20.
- **reasoning**
  - item 1
    - **speaker**: owner
    - **quote**: Don't change the system unless you ask or are unsure
    - **locator**: /home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:482
    - **bears**: A change to the scaffold's specification is asked first, so nothing here is applied on my recommendation alone.
  - item 2
    - **speaker**: owner
    - **quote**: we need to uipdate the autonomous and auditonomous repos phsyciall; to match first .
    - **locator**: owner's instructions of 11 November 2026
    - **bears**: The owner's word of 11 November covers the two exemplars and puts them first; it does not name any edit to the scaffold's specification.
  - item 3
    - **speaker**: owner
    - **quote**: All repos should mirror the 7lm. Manually. We update 7lm and focus on it only. No outside updates until we are sure I'm close.
    - **locator**: /home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:336
    - **bears**: The scaffold is the thing the exemplars follow, so its statement about them should be corrected by hand after they match, and not before.
  - item 4
    - **speaker**: specification
    - **quote**: What follows documents the two exemplars as they stand, including what is not yet as this specification states.
    - **locator**: /home/user/7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:930
    - **bears**: The exemplar section is a statement of present fact, so once the mirror is on the exemplars' mains, "the L7 restructure is not yet mirrored" (SPEC:950, SPEC:958) and the restrictions/ wording (SPEC:938) are false and due for correction.
  - item 5
    - **speaker**: record
    - **quote**: Its exemplar bullet that said the exemplars carry `controlled/` now says `restrictions/`, the position this specification names `controlled/`, the exemplars not being mirrored (§25); both "Not yet as stated" paragraphs record that their desks carry the former branch names.
    - **locator**: /home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:500
    - **bears**: These three passages were written on 20 September only to record the unmirrored state, so undoing them is the same kind of correction and changes no position or rule.
  - item 6
    - **speaker**: specification
    - **quote**: This Markdown is the source; the .docx filed beside it is generated from the text
    - **locator**: /home/user/7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:2
    - **bears**: Any correction to the Markdown carries the .docx with it in the same commit; the two are not corrected separately.
  - item 7
    - **speaker**: record
    - **quote**: Findings and design verdicts come to the owner as proposals — file, what is wrong, the exact fix — and nothing is applied until the owner says which.
    - **locator**: /home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:484
    - **bears**: The form of the action is fixed: a proposal with the exact replacement text, applied on the owner's word.
  - item 8
    - **speaker**: record
    - **quote**: The check reports them and does not fail on them.
    - **locator**: /home/user/autonomous@a719cec:L8/L6/history/harmonization-2026-09-05.md:217
    - **bears**: This sentence closes the mirror record's list of six folders that carry no sheet, so SPEC:934 ("Every directory has its 0.md") and GUIDE:474 ("Both exemplar repositories do exactly this.") stay untrue after the mirror lands; I confirmed unsheeted folders outside the retired sets at a719cec and 294c843.
  - item 9
    - **speaker**: owner
    - **quote**: Put the field guide into l6 as provenance stale. Deprecated and to be used as an example.
    - **locator**: /home/user/7lm@origin/ccr-9391bd81-f2enmj:L8/L6/history/harmonization-2026-09-04.md:518
    - **bears**: The guide is retired verbatim on the PR #20 branch, so GUIDE:474 is not corrected; its text is kept as it stood.
- **against**: "Read. "Please take the qwheel", the same evening as "Don't change the system unless you ask or are unsure" (§36): read as leave to make the words say what the folders already say and to act on findings verified three ways, and as no leave to change what any position is, holds, or is named." (/home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:510). On that reading the three sentences could be corrected without asking, as words made to match folders. I do not rely on it: that leave was given for the pass of 20 September, and the owner's word of 11 November names the exemplars only.
- **confidence**: the quotations favour it
- **alternatives**: 1. Correct all five passages in one pass once the exemplars land. This fails on two counts: SPEC:934 and GUIDE:474 are still untrue after the mirror, and the guide is retired verbatim on PR #20.
  2. Correct nothing and leave the specification as it is. Once the mirror merges, the specification would say "not yet mirrored" of repositories that are mirrored.
  3. Make SPEC:934 true from the exemplar side, by sheeting the unsheeted folders in both exemplars. That is a change to the exemplars the owner has not asked for; the mirror record leaves those folders "as found, for the owner".
  4. Narrow SPEC:934 to the canonical positions, or add the unsheeted folders to the two "Not yet as stated" paragraphs. Either is a new statement in the specification and is the owner's to word.
- **what_it_costs**: The proposal costs nothing in the tree and is reversible: it is a text diff held outside the repository until the owner approves it. Applied, it is one scaffold commit touching three sentences of the Markdown, the same three in the .docx (patched by hand, as on 20 September), and one row in specification-history.md. Until then the specification on main keeps saying "not yet mirrored", which stays true while PRs #30 and #28 are unmerged drafts. SPEC:934 and GUIDE:474 remain inaccurate about the exemplars until the owner rules.
- **who_acts**: The owner must say three things:
  1. Whether the three sentences are corrected once PRs #30 and #28 are merged, and whether that correction carries a new version date. The version of 20 September 2026 is now on main, so the 20 September precedent of "without a new version string" no longer applies by itself.
  2. What SPEC:934 should say, given that folders in both exemplars carry no sheet.
  3. That GUIDE:474 stands uncorrected, as the retired guide's text.

  The agent drafts the exact replacement text and the .docx patch and applies nothing. The owner merges.
