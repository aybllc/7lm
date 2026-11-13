# verify:KC-12

Agent result, as returned. Workflow: Handle on the Auditonomous research and manuscript. Run `wf_9c2917a7-7f0`. Phase: Verify.

- **id**: KC-12
- **verdict**: corrected
- **reasoning**: Every ref, hash, date and ancestry fact in the claim checks out. Four parts are imprecise or overstated.

  **Confirmed as written**
  - 7lm `origin/main` is c9dc061 (2026-11-11 10:08 -0800) and has `L7/allications/` and `L7/governance/controlled/`.
  - 7lm `origin/beta/common-contracts-r1-r6` is 97314c5 (2026-11-03 08:58 -0800); it is not an ancestor of main; the merge-base is 2e5a6d6.
  - 4ca3edb is the beta's first commit and is in no branch but the beta.
  - Both exemplar betas pin 4ca3edb at `binding.json:7` (`"architecture_commit": "4ca3edb9172c34e6b0033bd09e2379ed3da76d9d"`).
  - `## Manuscript work` appears only at 7LM-BETA:`L8/L4/work/writing/0.md:12`; no such heading exists in any state of auditonomous or autonomous.
  - The mirror commits f2d5b37 (auditonomous) and 8257118 (autonomous), both 11 Nov 2026 UTC, sit directly on `origin/main`; neither BETA nor ROADMAP is an ancestor of the session branch.

  **Corrections**
  1. **"Three candidate states" undercounts.** 7lm has three more unmerged heads, none in main or the beta:
     - `origin/audit/peering-descriptive-reframe-2026-09-20` (3555866): 122 commits, 79 files, mostly the owner's descriptive reframe of 20 Sep.
     - `origin/ccr-00099fac-hjosbo` (b5c3984): 8 commits.
     - `ccr-9391bd81-f2enmj` (4cbd74b).

     All three retire the field guide to `L8/L6/retired/field-guide-2026-09-20/`, while the beta edits it at its live path. Main and beta have also diverged: the beta lacks main's `L8/L6/in/7lm-layer-lists.md`.
  2. **The date on main is the layer-lists merge, not the restructure.** The L7 restructure reached main on 20 Sep 2026 (606d4b3, PR #17 merge 0d1ec40). The 11 Nov merge added one file.
  3. **4ca3edb is not the beta tip.** The manuscript guidance arrived in 97314c5, one commit after the pinned 4ca3edb, so the exemplars pin a state without it. The repository calls R1–R6 "corrections", not contracts (7LM-BETA:`L8/L6/history/specification-history.md:104-106`: "after the owner's approval of R1–R6").
  4. **"Match none in full" is overstated on the model's own check.** Against the 71-position canonical list in `integrity.yml`:
     - MAIN, ROADMAP, autonomous main and scholarly-pair each lack 8 positions.
     - Both exemplar betas and both session branches have all 71.
     - Auditonomous BETA's `integrity.yml` is byte-identical to 7lm 4ca3edb's; the auditonomous session branch's is byte-identical to 7lm main's.

     What no repository state has is the beta tip's guidance.

  **Smaller points**
  - BETA already contains the L7 restructure (the same six renames in auditonomous), so two unmerged auditonomous branches each carry it independently.
  - "Six renames" is true of auditonomous only; autonomous 8257118 has ten. The mirror commits also add six new `allications` sheets and edit about 45 others.
  - The session branch is not local-only: `origin/ccr-9391bd81-f2enmj` exists at the same tips, now 74b270e (auditonomous) and a719cec (autonomous), not the cited commits.
- **corrected_statement**: The model (aybllc/7lm) has one merged state and several unmerged ones, and three of them matter to the repositories. (1) 7lm main (c9dc061, merge of PR #21 on 11 November 2026) carries the L7 restructure, which has been on main since PR #17 of 20 September 2026; the 11 November merge added only the layer lists at the L6 inbox. (2) The 7lm beta is two commits on merge-base 2e5a6d6 and has diverged from main (not merged into main, and it lacks main's layer lists). Its first commit, 4ca3edb (2 November 2026 PST), applies the owner-approved R1 to R6 corrections and adds bounded research objects. (3) Its tip, 97314c5 (3 November 2026), adds guidance to 18 sheets, including the "Manuscript work" section. Both exemplar betas pin 4ca3edb, not the tip, so they pin a state without the manuscript guidance. Three further unmerged 7lm heads exist (audit/peering-descriptive-reframe-2026-09-20 at 3555866, ccr-00099fac-hjosbo at b5c3984, and the session branch ccr-9391bd81-f2enmj at 4cbd74b); all three retire the field guide that the beta edits in place.

  No repository state carries the beta tip's guidance. MAIN and ROADMAP (and autonomous main and the scholarly-pair branch) lack 8 of the model's 71 canonical positions (L7/allications with its six children, and L7/governance/controlled). BETA already contains the L7 restructure and has all 71 positions, with an integrity workflow in auditonomous identical to 7lm 4ca3edb's. The session branch ccr-9391bd81-f2enmj (pushed; mirror commits f2d5b37 in auditonomous and 8257118 in autonomous, 11 November 2026; tips now 74b270e and a719cec) mirrors the L7 restructure directly on MAIN (six renames in auditonomous, ten in autonomous, plus six new allications sheets). It has all 71 positions and, in auditonomous, a workflow identical to 7lm main's, but contains nothing of BETA, ROADMAP, R1 to R6 or the manuscript guidance.
- **evidence_checked**
  - 7lm refs: origin/main c9dc061 (2026-11-11 10:08:11 -0800, 'Merge pull request #21: the layer lists...'); origin/beta/common-contracts-r1-r6 97314c5 (2026-11-03 08:58:01 -0800); merge-base 2e5a6d6; beta is not an ancestor of main; 4ca3edb (2026-11-02 20:53:22 -0800) is contained only in the beta branch
  - 7lm `git diff --stat 2e5a6d6 origin/main`: one file, L8/L6/in/7lm-layer-lists.md (415 insertions)
  - 7lm `git log --diff-filter=A origin/main -- L7/allications/0.md L7/governance/controlled/0.md`: 606d4b3 2026-09-20 'The L7 restructure: allications, and controlled'; merged by 0d1ec40 (PR #17, 2026-09-20)
  - 7LM-BETA:L8/L4/work/writing/0.md:12 '## Manuscript work'; heading absent at 7lm origin/main, 2e5a6d6 and 4ca3edb (git grep)
  - 7lm `git diff --stat 4ca3edb 97314c5`: 18 sheets changed, including L8/L4/work/writing/0.md (+6); 97314c5 message: 'Update 18 existing 0.md documents for shared project structure, project-owned design choices, manuscript placement'
  - 7LM-BETA:L8/L6/history/specification-history.md:104-106 '### Owner-approved common architecture corrections of 2 November 2026' / 'Implemented by Codex, task T1, on 2 November 2026 ... after the owner's approval of R1–R6'
  - 7LM-BETA:L8/L6/history/specification-history.md:101 'The exemplar repositories `aybllc/autonomous` and `aybllc/auditonomous` still carry the former branch names and are not brought into step by this pass.'
  - BETA:L7/peering/public/ingress/peer-1/object-2/binding.json:7 '"architecture_commit": "4ca3edb9172c34e6b0033bd09e2379ed3da76d9d"' (auditonomous)
  - autonomous origin/beta/7lm-exemplar-autonomous:L7/peering/public/egress/peer-1/object-2/binding.json:7, same architecture_commit; autonomous BETA:L8/L5/research/findings/BETA_FINDINGS.md:13 '[source text withheld from the public copy] `4ca3edb...`'
  - 7lm other unmerged heads (`git log origin/main..<ref>`): origin/audit/peering-descriptive-reframe-2026-09-20 3555866 (122 commits, 79 files vs 2e5a6d6); origin/ccr-00099fac-hjosbo b5c3984 (8 commits); ccr-9391bd81-f2enmj 4cbd74b (8 commits); each includes 574500d 'The field guide retired: stale, deprecated, kept as an example'; none is an ancestor of main or the beta
  - 7lm `git diff --stat 2e5a6d6 4ca3edb`: L8/L6/7lm-field-guide.md edited at its live path (6 lines), while the 17 October lines rename it to L8/L6/retired/field-guide-2026-09-20/
  - auditonomous ccr-9391bd81-f2enmj: merge-base with origin/main is 2165144; six commits beyond main, f2d5b37 (2026-11-11 18:34:37 UTC, mirror) through tip 74b270e; BETA and ROADMAP are not ancestors; origin/ccr-9391bd81-f2enmj is at the same tip
  - autonomous ccr-9391bd81-f2enmj: merge-base with origin/main is c9076c3; 8257118 (2026-11-11 18:33:28 UTC, mirror) and tip a719cec; BETA and scholarly-pair are not ancestors
  - auditonomous `git show -M --name-status f2d5b37`: 5 renames to L7/allications/publications/ and 1 to L7/governance/controlled/0.md (six), 6 added allications sheets, about 45 modified files
  - autonomous `git show -M --name-status 8257118`: 9 renames to L7/allications/publications/ and 1 to L7/governance/controlled/0.md (ten)
  - auditonomous `git diff --name-status -M origin/main origin/beta/7lm-exemplar-auditonomous`: the same six renames are already in BETA; autonomous BETA has ten
  - Canonical 71-position list from 7lm 4ca3edb:.github/workflows/integrity.yml:45-57, checked against ls-tree of each state: auditonomous MAIN and ROADMAP, autonomous main and scholarly-pair each lack 8 (L7/governance/controlled, L7/allications and its six children); both exemplar betas and both session branches lack none
  - integrity.yml compared by diff: auditonomous BETA vs 7lm 4ca3edb 0 differing lines; auditonomous session branch vs 7lm origin/main 0 differing lines; autonomous copies differ by a retained local comment block
  - Heading grep '^#+ .*manuscript' on *0.md: none on auditonomous MAIN, BETA, f2d5b37 or session tip (other than a results-folder sheet), none on autonomous main, BETA, 8257118 or session tip; auditonomous BETA and session L8/L4/work/writing/0.md headings are identical and lack 'Manuscript work'
  - MAIN:L8/L5/research/review/STATUS_LADDER.md and MAIN:L8/L5/research/review/STATUS_AND_LABEL_DISCIPLINE.md read first, per rule 7
