# verify:K07

Agent result, as returned. Workflow: The model, read deep. Run `wf_9a60cf50-a5f`. Phase: Verify. Checked in 2026-11-11 19:51 UTC.

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
