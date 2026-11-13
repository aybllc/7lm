# resolve:D23

Agent result, as returned. Workflow: Resolutions for the 23 owner decisions. Run `wf_3293f65c-a92`. Phase: Resolve.

- **decision**: 23. Whether the live references to uso/l6/LEDGER.md and other paths from before 5 September 2026 are corrected, three of them in binder files that "are not rewritten".
- **resolution**: Change no file now. Put the references to the owner as a proposal in two classes: (a) the three binder gate files and the dated or staging records stay byte for byte, read through the forward pointer that already stands at L8/L6/0.md:79; (b) the four working files that are not dated records (FORMULAS_LEDGER.md:23 and datasets-LEDGER.md:21 in both exemplars, and MANUSCRIPT.tex:50 and :79 in autonomous) have `uso/l6/LEDGER.md` replaced by `L7/provenance/sources/LEDGER.md`, in one commit per repository with a record line, only once the owner says so. If the owner also wants the binder files corrected, binder/0.md:8 must be reworded in the same commit, because it currently says they are not rewritten.
- **reasoning**
  - item 1
    - **quote**: Don't change the system unless you ask or are unsure
    - **speaker**: owner
    - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:482
    - **bears**: The owner's standing word is that a correction not asked for is proposed, not applied, so nothing is edited before the owner answers.
  - item 2
    - **quote**: thank you please pull out historicallyu referndes to the docuejtnation leaving just the historical docuemtnatio that is cirrent and relevant for the purpose of using the thing
    - **speaker**: owner
    - **locator**: auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:158
    - **bears**: The owner wants documentation in use to be current, which favours correcting a dead path in a working file, but the word was given about the sheets and does not name binder files, ledgers or the manuscript.
  - item 3
    - **quote**: we need to uipdate the autonomous and auditonomous repos phsyciall; to match first .
    - **speaker**: owner
    - **locator**: owner's instruction of 11 November 2026, as typed
    - **bears**: The instruction of the day is to match the exemplars to the changed model physically; it does not ask for references to the layout before 5 September 2026 to be repaired, so the correction is outside what was asked.
  - item 4
    - **quote**: The three files are the tree's own gates from the earlier layout and are not rewritten.
    - **speaker**: sheet
    - **locator**: auditonomous@origin/main:L7/publications/binder/0.md:8
    - **bears**: The binder's own sheet states that binder/README.md, internal/README.md and press-kit/README.md are kept as written, so editing README.md:11 or press-kit/README.md:18 would make a live sheet untrue unless it is reworded too (autonomous has the same sentence at the same path and line, beginning "The files are").
  - item 5
    - **quote**: The lowercase `uso/` of the layouts before 2026-09-05 stays what it was, a path of that layout.
    - **speaker**: record
    - **locator**: auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:172
    - **bears**: The record's reading rule already treats lowercase uso/ as a path of the old layout to be read as such, not swept (autonomous carries the same sentence at :179).
  - item 6
    - **quote**: The pointer register formerly at `uso/l6/LEDGER.md` is now `L7/provenance/sources/LEDGER.md`.
    - **speaker**: sheet
    - **locator**: auditonomous@origin/main:L8/L6/0.md:79
    - **bears**: A reader who meets the old path is already told in a live sheet where the register stands, so leaving the references loses no one (same line in autonomous@origin/main:L8/L6/0.md:79).
  - item 7
    - **quote**: No research object, no definition, no ledger row and no manuscript file is touched.
    - **speaker**: record
    - **locator**: auditonomous@origin/ccr-9391bd81-f2enmj:L8/L6/history/harmonization-2026-09-05.md:200
    - **bears**: The mirror of 11 November 2026 declared it touched no manuscript or ledger file, so correcting MANUSCRIPT.tex or the two ledgers inside that pull request would break what its own record says; it must be a separate, owner-approved commit.
  - item 8
    - **quote**: - [ ] [source text withheld from the public copy]`.
    - **speaker**: other
    - **locator**: autonomous@origin/main:L7/publications/binder/press-kit/README.md:18
    - **bears**: This is the reference at issue: a release-checklist item, not yet exercised (nothing released), naming a path that no longer exists; the same line stands at auditonomous@origin/main:L7/publications/binder/press-kit/README.md:18 and the third binder instance at auditonomous@origin/main:L7/publications/binder/README.md:11.
- **against**: "thank you please pull out historicallyu referndes to the docuejtnation leaving just the historical docuemtnatio that is cirrent and relevant for the purpose of using the thing" (owner, 2026-09-07; auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:158). A release checklist and a manuscript preamble that send the reader to a path that does not exist are not "cirrent and relevant for the purpose of using the thing"; on that reading the references should be corrected, the binder's included. The owner's own candidate did so in one place: autonomous@origin/beta/7lm-exemplar-autonomous:L7/allications/publications/binder/press-kit/README.md:17 reads "- [ ] [source text withheld from the public copy]`."
- **confidence**: the quotations do not reach it: the owner must say
- **alternatives**: Facts first. Outside L8/L6/history/ and L8/L6/retired/, and leaving out sheets that correctly say "relocated from", `uso/l6/LEDGER.md` stands on main in autonomous on 9 lines of 5 files (press-kit/README.md:18; datasets-LEDGER.md:21; __STAGING_README.md:7,22,28,45; FORMULAS_LEDGER.md:23; MANUSCRIPT.tex:50,79) and in auditonomous on 10 lines of 6 files (binder/README.md:11; press-kit/README.md:18; datasets-LEDGER.md:21; STAGING_README.md:7,26,34,49; FORMULAS_LEDGER.md:23; RECONCILIATION_FROM_L6_2026-08-16.md:4,84). The draft pull requests #30 and #28 carry all of them unchanged at the moved binder path. The register itself stands at L7/provenance/sources/LEDGER.md in both.

  Alternatives: (1) Correct everything, binder included, and reword binder/0.md:8 — the reading the owner's word of 2026-09-07 supports and the autonomous beta already made for one line; it rewrites files the sheets call gates of the earlier layout. (2) Correct nothing and add nothing — fully consistent with the record, but leaves the autonomous manuscript and two ledgers pointing at a dead path. (3) Leave every file and add one reading line to each binder sheet ("`uso/l6/LEDGER.md` in these files stands at `L7/provenance/sources/LEDGER.md` now") — touches only sheets, yet is still a change the owner has not asked for. (4) Take the autonomous beta's press-kit/README.md — not recommended as a path fix, because the same diff also rewrites that file's opening statements about clearance, which is a separate decision. The beta is also inconsistent: it left the auditonomous binder files and both ledgers and the manuscript uncorrected.
- **what_it_costs**: Nothing is changed, so nothing needs reversing. The cost of waiting is that 19 lines in 11 working files keep naming a path that does not exist, two of them in the autonomous manuscript preamble and three in binder release gates; a reader must know to look at L8/L6/0.md:79. If the owner approves class (b), it is six one-line substitutions across the two repositories (four files in autonomous counting two lines in MANUSCRIPT.tex, two in auditonomous), reversible by a single revert each. The staging READMEs and the reconciliation record stay as dated records under either answer.
- **who_acts**: The owner says one of: "leave them all", "fix the working files, leave the binder", or "fix them all, binder too". Whoever holds the exemplar branches then makes the edit by hand as a separate commit from the mirror pull requests (#30 autonomous, #28 auditonomous), with a line in each record at L8/L6/history/harmonization-2026-09-05.md.
