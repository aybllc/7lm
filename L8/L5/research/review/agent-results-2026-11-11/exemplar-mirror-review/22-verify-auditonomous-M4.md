# verify:auditonomous:M4

Agent result, as returned. Workflow: Review of the two commits. Run `wf_26752832-654`. Phase: Verify.

- **real**: no
- **reasoning**: The facts in the finding are all true, but it is not a defect of commit f2d5b37 measured against the intended content, which the finding itself concedes.

  Verified from git objects only:
  - auditonomous@f2d5b37:L7/provenance/0.md:37 reads "- `lineage/`, `authority/` — empty; authority for each bound peer object is stated in that object's binding record under `L7/peering/`." The line is byte-identical at parent 2165144.
  - `git diff -M 2165144 f2d5b37 -- L7/provenance/0.md` shows exactly two hunks: line 29 (`L7/publications/` -> `L7/allications/publications/`) and line 41 ("peering, and publication state" -> "peering, and allications — the outward acts, of which publication is one"). Line 37 is untouched.
  - `ls-tree -r f2d5b37 L7/provenance/lineage` lists 0.md and 2026-08-05-observed-not-observable-session-provenance.md, so the sheet's "empty" is false for lineage/. authority/ holds only its 0.md, so that half is true.
  - auditonomous@f2d5b37:L7/provenance/lineage/0.md:32 lists that record in its Holdings.
  - `git log -L37,37:L7/provenance/0.md` shows the line last written in ccc0554 (2026-09-05). `git log -- L7/provenance/lineage` shows the record arriving in 50f43d3 (2026-09-06). The contradiction is about two months older than this commit.

  Why it is not real:
  1. It is already true of the parent, and the sentence is not about a renamed position. Intended-content item 6 forbids touching "any sentence of a sheet that is not about the renamed positions". The commit's own section 13 says the same: "Every other sentence of every sheet ... none of that is touched here." Changing line 37 in this commit would have been the defect.
  2. The commit wrote no claim that the stale line contradicts. Section 13 makes no statement about lineage/ or about the correctness of emptiness claims generally, and its only new emptiness claim ("nothing is filed at any of the five") concerns the five new allications positions. The other lineage mentions in live sheets (L7/0.md:31, 58, 100, 103) are tree and table rows, not holdings claims.
  3. Leaving it out of "Left as found, for the owner" is not a defect either. Item 5 requires only a new numbered section, and the list does not claim to enumerate every pre-existing inaccuracy on the desk. Its four entries are all things this pass touched or adjoins: unsheeted folders the CI check reports, a sentence in a sheet the pass moved, and branches affected by the moves.

  Disposition: a true pre-existing inaccuracy that belongs to the later QA pass on the research, as the finding's own suggested fix says. No change to f2d5b37 is warranted.
- **corrected_statement**: Not a defect of f2d5b37. Pre-existing and out of scope: auditonomous L7/provenance/0.md:37 (written in ccc0554 on 2026-09-05, identical at parent 2165144) says `lineage/` is empty, while L7/provenance/lineage/ has held one session-provenance record since 50f43d3 (2026-09-06), as lineage/0.md:32 states. The commit correctly left line 37 untouched. Carry it to the QA pass on the research.
- **exact_fix**: None for this commit. For the later QA pass (not the restructure commit), line 37 of L7/provenance/0.md would become: "- `lineage/` — one session-provenance record (see its sheet); `authority/` — empty; authority for each bound peer object is stated in that object's binding record under `L7/peering/`."
