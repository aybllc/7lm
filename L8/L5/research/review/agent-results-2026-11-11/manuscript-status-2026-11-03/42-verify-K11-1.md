# verify:K11:1

Agent result, as returned. Workflow: Manuscript status of 3 November 2026. Run `wf_1cf4205c-c72`. Phase: Verify. Checked in 2026-11-11 19:56 UTC.

- **refuted**: no
- **confidence**: high
- **reason**: Every quoted phrase, number, date and path in K11 re-checked against origin/claude/book-structure-roadmap-k8ap82 (head 9259c18, 2026-09-14 02:04:14 +0000) at L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md (686 lines); all hold.

  BRANCH ONLY: `git ls-tree -r origin/main --name-only | grep -ic BOOK_STRUCTURE_AND_ROADMAP` = 0; `git log origin/main -- <path>` empty; merge-base(main, branch) = 2165144 = origin/main head (2026-09-11 23:26:02 -0700); 5 commits on branch not in main (30a40f1, 62d2e3f, b1ec302, 4e2c4e4, 9259c18), 0 the other way. `gh api repos/aybllc/auditonomous/pulls/27`: state "closed", merged false, merged_at null, head claude/book-structure-roadmap-k8ap82 @ 9259c18, base main, created 2026-09-13T20:39:22Z, closed_at 2026-10-17T08:41:45Z.

  PROPOSAL / NOTHING ADOPTED: line 3 verbatim "**[source text withheld from the public copy] … Nothing here is adopted." Also line 608 "Nothing below is adopted.", line 639 "Nothing reserved for the author is adopted.", line 685 "[source text withheld from the public copy]." Line 3 identical in 30a40f1.

  27 CHAPTERS / TALLY: line 454 verbatim "[source text withheld from the public copy]". Independent recount of the §4 table (lines 426–452): exactly 27 rows "| 1 |"…"| 27 |"; first token of the "Label today" column tallies [source text withheld from the public copy] (several carry compound labels, e.g. line 440 "VERIFIED (literature) · INTERNALLY DERIVED (use)", line 445 "SPECULATION → CONJECTURE"). Same tally line in 30a40f1 at its line 452.

  22 DECISIONS, NO D17: `grep -c '^| D[0-9]+ |'` on head = 22; ids at lines 612–633 in file order D1…D16 (612–627), D18 (628), D19 (629), D20 (630), D22 (631), D23 (632), D21 (633) — i.e. set D1–D16, D18–D23 as claimed (D21 is out of numeric order, after D23). `grep -n 'D17'` exit 1 on head and on 30a40f1; `git grep -n 'D17' origin/claude/book-structure-roadmap-k8ap82` exit 1 (absent from the whole branch tree). Unique D-ids anywhere in the file: D1–D16, D18–D23 (no D17). First version 30a40f1 (2026-09-13 20:37:08 +0000) had 20 rows (D1–D16, D18–D21 at lines 609–628); D22/D23 were added by the 2026-09-14 revision (line 7 "D22 and D23 are added").

  ONLY D15 RULED: line 626 D15 recommendation column verbatim "[source text withheld from the public copy])"; line 7 "[source text withheld from the public copy]"; line 585 S2 gate "D15, taken as ruled by the instruction". All other case-insensitive "ruled" hits (196, 356, 500, 505, 514, 589, 598 "Once D22 is ruled", 629 "editorial once ruled", 637 "until D12 is ruled", 680) are future conditions or chapter 'done-when' prose, none records another D as ruled. In 30a40f1 the D15 row (its line 623) still read "restore; [source text withheld from the public copy]" — recommendation, not ruled.

  WRITING NOT BEGUN: line 645 verbatim "…the writing not begun (S6)."; line 587 S4 "twenty-seven chapter files … no chapter has text".

  SESSIONS: line 589 "27 chapters at 1–2 sessions each"; line 591 "[source text withheld from the public copy]" (30a40f1 equivalents at its lines 583 and 588).

  NOTED TENSION IN SOURCE (not a refutation; the claim's "treats only D15 as ruled" already accommodates it): the record declares "Nothing here is adopted" while recording D15 as TAKEN AS RULED and §9 (line 645) recording S0–S5 executed the same day (papers drafted, 116 files restored, 27 chapter files opened). Status labels seen in the file: PROPOSAL, INTERNAL ONLY, INTERNALLY DERIVED, OWNER DECISION, RECOMMENDED, RESEARCHING, CONJECTURE, SPECULATION, VERIFIED, EMPTY (line 418), "LEAD — NOT VERIFIED" (637), TAKEN AS RULED (626), NOT-CHEC[KED] (444), and S-table statuses "done 2026-09-14" / "checked 2026-09-14" / "opened 2026-09-14" / "declared 2026-09-14" (585–588, 583–584).
- **correction**: Not refuted. Two precision addenda only: (1) the claim's cited line numbers (3/454/589/591/612–633/626/645) are those of the branch head 9259c18; in the first version 30a40f1 the tally sits at line 452 and the D-table at 609–628 with 20 rows (D1–D16, D18–D21), D15 not yet ruled. (2) In the head table the rows run D1–D16, D18, D19, D20, D22, D23, D21 (D21 at line 633, after D23) — the set D1–D16, D18–D23 is correct, the numeric order is not. PR #27 was created 2026-09-13T20:39:22Z and closed unmerged on 2026-10-17T08:41:45Z (gh api repos/aybllc/auditonomous/pulls/27: merged=false).
