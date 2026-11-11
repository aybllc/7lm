# verify:K04

Agent result, as returned. Workflow: The model, read deep. Run `wf_9a60cf50-a5f`. Phase: Verify. Checked in 2026-11-11 19:51 UTC.

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
