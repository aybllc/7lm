# verify:K02

Agent result, as returned. Workflow: The model, read deep. Run `wf_9a60cf50-a5f`. Phase: Verify. Checked in 2026-11-11 19:51 UTC.

- **id**: K02
- **verdict**: stands
- **reasoning**: Every part of the claim was confirmed from git objects on 7lm@origin/main (c9dc0617983e18fb6327d79bd1be8d8b1255aab3); no counter-evidence found.

  1. 71 canonical positions, 35 + 36. 7lm@origin/main:.github/workflows/integrity.yml:47-59 is the `canon=` list (cited locator is exact). Expanded with top=L8, lower=L it yields 71 entries, 71 unique: 35 matching ^L7(/|$) (lines 47-51) and 36 matching ^L8(/|$) (lines 52-59). The specification's tree at 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:206-276 independently has 71 "/0" entries: 35 on lines 206-240 (L7) and 36 on lines 241-276 (L8). Reading note, not an error: the 35 and 36 each include the layer root itself (L7 plus 34 beneath it; L8 plus 35 beneath it). The literal number 71 is not written in the workflow or the specification; it is obtained by counting.

  2. Four direct L7 branches and their children. Spec line 46 verbatim: "Canonical direct L7 branches are L7/provenance/, L7/governance/, L7/peering/, and L7/allications/." Spec lines 207-240 and workflow lines 47-51 agree: provenance (prior-art, sources, lineage, authority); governance (copyright, licensing, patents, permissions, access, controlled); peering (private, public; each ingress, egress; each peer-1/object-1 = 15 positions); allications (publications, applications, communications, specifications, notifications, participations). The tree IS the same: `ls-tree origin/main L7/` gives exactly 0.md, allications, governance, peering, provenance; `ls-tree -r -d origin/main L7` gives exactly 35 directories (L7 included), identical to the canon list, with no extra directory. Corroborating sheets: 7lm@origin/main:L7/0.md:16 quotes the same sentence; L7/peering/0.md:8 and L7/allications/0.md:8 say "one of the four canonical direct L7 branches". No stale L7/publications or governance/restrictions position exists in the tree (only a historical mention at L7/allications/0.md:38: "`publications/` moved here from `L7/publications/` in the pass of 2026-09-20").

  3. Sheets. Simulating G-003 (workflow lines 31-61) from objects: root of origin/main is .github, L7, L8, README.md, so top=L8. Of 94 files named 0.md under L7/ and L8/, 19 lie below L8/L6/retired/scaffold-2026-08-20/ and are skipped by the line-40 case pattern; 75 are checked; 0 have a first line other than "# <path>/"; all 71 canonical positions have a 0.md (0 missing). The 75 = 71 canonical + 4 non-canonical checked sheets: L8/L6/in, L8/L6/retired/scaffold-2026-08-20, L8/L6/retired/specification-2026-09-04, L8/L6/retired/specification-draft-2026-09-03. No 0.md path contains spaces or non-ASCII characters and first lines end in LF only, so the object-based simulation matches what the CI shell loop would do on a checkout.

  Caveat on method: the 75/0/0 result is my simulation from git objects, not an observed CI run log (no network used).
- **evidence_checked**
  - 7lm@origin/main (rev-parse = c9dc0617983e18fb6327d79bd1be8d8b1255aab3)
  - 7lm@origin/main:.github/workflows/integrity.yml:31-61 (G-003 step) and :47-59 (canon list: 71 entries, 35 L7 + 36 L8, all unique)
  - 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:46 ('Canonical direct L7 branches are L7/provenance/, L7/governance/, L7/peering/, and L7/allications/.')
  - 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:206-276 (tree: 71 '/0' entries; 35 on 206-240, 36 on 241-276)
  - git -C /home/user/7lm ls-tree --name-only origin/main (root: .github, L7, L8, README.md)
  - git -C /home/user/7lm ls-tree --name-only origin/main L7/ (0.md, allications, governance, peering, provenance)
  - git -C /home/user/7lm ls-tree -r -d --name-only origin/main L7 (35 directories incl. L7, identical to canon list)
  - git -C /home/user/7lm ls-tree -r --name-only origin/main filtered to ^(L7|L8)(/.*)?/0\.md$ : 94 sheets, 19 skipped under L8/L6/retired/scaffold-2026-08-20/, 75 checked, 0 wrong first lines (each read with git show origin/main:<path> | head -1), 0 canonical positions missing
  - Non-canonical checked sheets: L8/L6/in/0.md, L8/L6/retired/scaffold-2026-08-20/0.md, L8/L6/retired/specification-2026-09-04/0.md, L8/L6/retired/specification-draft-2026-09-03/0.md
  - 7lm@origin/main:L7/0.md:16; L7/peering/0.md:8; L7/allications/0.md:8 and :38 (corroboration of four direct branches; only a historical mention of L7/publications/)
  - git grep on origin/main for 'L7/publications|governance/restrictions' in spec, README.md, L7/ (no live stale position) and for literal 71/75 in spec, README.md, L7/0.md, L8/0.md, .github (not found)
