# verify:K01

Agent result, as returned. Workflow: The model, read deep. Run `wf_9a60cf50-a5f`. Phase: Verify.

- **id**: K01
- **verdict**: stands
- **reasoning**: Every part of the claim is confirmed from the git objects, and I found no evidence against it.

  1. One path differs. `git -C /home/user/7lm diff --name-status 2e5a6d6 origin/main` (origin/main = c9dc0617983e18fb6327d79bd1be8d8b1255aab3) returns one row, `A L8/L6/in/7lm-layer-lists.md`. `--stat` gives 1 file changed, 415 insertions, no deletions. `--raw` and `--no-renames` give the same single add (blob ab91236, mode 100644).

  2. Merged 11 November 2026 as pull request #21. 2e5a6d6 is an ancestor of origin/main, and `git log 2e5a6d6..origin/main` holds two commits:
     - c6d598a, 2026-10-31 04:16:20 +0000, "The layer lists: one complete bullet list per position, filed at the L6 inbox as a proposal". This is also the tip of origin/ccr-9a67809a-iwii3n, which has nothing beyond main.
     - c9dc061, 2026-11-11 10:08:11 -0800, parents 2e5a6d6 and c6d598a, "Merge pull request #21: the layer lists, one complete bullet list per position, filed at the L6 inbox".

  3. 5 October 2026. 2e5a6d6 is "Update 0.md", dated 2026-10-05 20:33:36 -0700, touching L7/0.md only (2 insertions). In UTC that is 2026-10-06 03:33; the claim's date matches the commit's own timezone.

  4. No sheet, position, specification line or check line differs. Object ids are identical at 2e5a6d6 and origin/main for:
     - the specification blob (86fe2415)
     - .github/workflows/integrity.yml (f43dd045) and the whole .github tree (d78cb8e4)
     - the L7 tree (8974b3a8) and the L8/L4 tree (69797317)
     - README.md (b62c31ec)
     Both refs have 97 directories and 94 0.md files. L8/L6/in/0.md is unchanged (lines 1-3: "# L8/L6/in/", "The inbox for L6.").

  5. Cited quotes.
     - 7lm@origin/main:L8/L6/in/7lm-layer-lists.md:5 reads "Nothing in the tree, any sheet, the guide, the templates, the specification, or the CI changes with it", and the same line says it is filed "as a proposal".
     - 7lm@origin/main:L8/L6/in/7lm-layer-lists.md:3 adds "Where this document and the specification differ, the specification controls."
     - 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:18 reads "Version of 20 September 2026." Line 12 also reads "20 September 2026", and the phrase "Version of" occurs only at line 18.

  Three observations that do not alter the verdict:
     - The new file's line 5 cites record section 36 of L8/L6/history/harmonization-2026-09-04.md. That section (line 480, "standing: the system is not changed without asking...") is the standing rule, not an entry about the layer lists.
     - Nothing else on main mentions the new file: grep for '7lm-layer-lists' and 'layer lists' outside the file returns nothing. The addition is unrecorded in the history file and unlisted in the inbox sheet.
     - The claim covers main only. It says nothing about the unmerged branches (beta/common-contracts-r1-r6, the two open draft PR branches, the audit branch), which may carry model changes.
- **evidence_checked**
  - git -C /home/user/7lm rev-parse origin/main -> c9dc0617983e18fb6327d79bd1be8d8b1255aab3; 2e5a6d6 -> 2e5a6d67b6c590a06ea9761dfd8a98c3ed8ff270; merge-base --is-ancestor 2e5a6d6 origin/main -> true
  - git -C /home/user/7lm diff --name-status / --stat / --raw / --summary / --no-renames 2e5a6d6 origin/main -> single row 'A L8/L6/in/7lm-layer-lists.md', 415 insertions, create mode 100644, blob ab91236
  - git -C /home/user/7lm log 2e5a6d6..origin/main -> c6d598a (2026-10-31 04:16:20 +0000, Claude, 'The layer lists: ... filed at the L6 inbox as a proposal') and c9dc061 (2026-11-11 10:08:11 -0800, EDM, 'Merge pull request #21: ...', parents 2e5a6d6 c6d598a)
  - git -C /home/user/7lm rev-parse origin/ccr-9a67809a-iwii3n -> c6d598a; log origin/main..origin/ccr-9a67809a-iwii3n -> empty
  - git -C /home/user/7lm show --stat 2e5a6d6 -> 'Update 0.md', 2026-10-05 20:33:36 -0700, L7/0.md 2 insertions
  - 7lm@origin/main:L8/L6/in/7lm-layer-lists.md:5 -> 'Nothing in the tree, any sheet, the guide, the templates, the specification, or the CI changes with it'; same line: 'as a proposal'
  - 7lm@origin/main:L8/L6/in/7lm-layer-lists.md:3 -> 'Where this document and the specification differ, the specification controls.'
  - 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:18 -> 'Version of 20 September 2026.'; line 12 -> '7LM Harmonized Authoritative Architecture Specification • 20 September 2026'; grep 'Version of' hits line 18 only
  - git rev-parse at 2e5a6d6 and at origin/main, identical ids: specification blob 86fe2415; .github/workflows/integrity.yml f43dd045; .github tree d78cb8e4; L7 tree 8974b3a8; L8/L4 tree 69797317; README.md b62c31ec
  - git ls-tree -r at 2e5a6d6 and origin/main: 94 files named 0.md and 97 directories at both refs; directories without a sheet on main: .github, .github/workflows, L8/L6/retired/scaffold-2026-08-20/USO
  - git ls-tree -r --name-only L8/L6/in at both refs: origin/main adds only 7lm-layer-lists.md to 0.md, the slim .docx, optimistic-thompson-branch-text.md and specification-removed-2026-09-07.docx
  - 7lm@origin/main:L8/L6/in/0.md:1-3 -> '# L8/L6/in/' / 'The inbox for L6.' (unchanged)
  - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:480 -> '## 36. 2026-09-20 — standing: the system is not changed without asking; ...'; line 492 -> '## 37. ...' (last section)
  - git -C /home/user/7lm grep -F '7lm-layer-lists' origin/main and grep -i -F 'layer lists' origin/main excluding the file itself -> no hits
