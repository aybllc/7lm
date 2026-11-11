# verify:K08

Agent result, as returned. Workflow: The model, read deep. Run `wf_9a60cf50-a5f`. Phase: Verify. Checked in 2026-11-11 19:51 UTC.

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
