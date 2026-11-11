# verify:K06

Agent result, as returned. Workflow: The model, read deep. Run `wf_9a60cf50-a5f`. Phase: Verify. Checked in 2026-11-11 19:56 UTC.

- **id**: K06
- **verdict**: corrected
- **reasoning**: Every count and name in the claim is confirmed from git objects. The one correction is scope: "nothing under L8 is missing or misnamed" holds only for the 36 canonical L8 positions, not for the whole L8 tree.

  **Confirmed**
  - **Canon list:** the scaffold's check lists 71 positions, 35 under L7 and 36 under L8 (7lm@origin/main:.github/workflows/integrity.yml:47-59).
  - **Autonomous (origin/main = c9076c3):** my re-run of the G-003 logic gives 97 sheets checked, 0 wrong headings, 63 canonical positions present, 8 missing.
  - **Auditonomous (origin/main = 2165144):** 78 sheets checked, 0 wrong headings, 63 present, 8 missing.
  - **The eight missing positions** are identical in both: L7/governance/controlled, L7/allications, and L7/allications/{publications, applications, communications, specifications, notifications, participations}.
  - **Former folders still present:** L7/publications/ holds 9 files in Autonomous and 5 in Auditonomous; L7/governance/restrictions/ holds 1 file (0.md) in each. Their sheets are headed "# L7/publications/" and "# L7/governance/restrictions/".
  - **The other 63 positions** each have a 0.md whose first line is exactly "# <path>/"; all 36 L8 positions are among them, and L8 holds L0 to L6 with the right case.
  - **Control:** the same simulation on 7lm@origin/main gives 75 sheets checked, 0 wrong, 71 of 71 present.

  **Evidence against the unscoped L8 sentence**
  - **L8/L6/in/ exists on the scaffold and in neither exemplar.** It is a sheeted directory (7lm@origin/main:L8/L6/in/0.md:1 "# L8/L6/in/", line 3 "The inbox for L6."), described at 7lm@origin/main:L8/L6/0.md:79 as "`L8/L6/in/` — the inbox". It is not in the 71-position list, and the specification file has no "L6/in" hit, so it is not a canonical position.
  - **Autonomous holds a directory spelled "autonomouos"** at L8/L5/research/review/autonomous-theory/autonomouos/. It is unsheeted filed material beneath a canonical position, not a canonical position.
  - **The scaffold's three retired sets** (L8/L6/retired/scaffold-2026-08-20, specification-2026-09-04, specification-draft-2026-09-03) are absent from the exemplars, which hold their own retired sets instead. This is expected.

  **Context the claim omits**
  The eight positions are missing only against the scaffold's check. Each exemplar's own integrity.yml on origin/main still carries the older list: it names L7/governance/restrictions and L7/publications, and has no allications line and no peer-1/object-1 line. That is 57 positions, so each exemplar's own check does not flag these. The eight peer-1 and object-1 positions nonetheless exist in both exemplar trees.
- **corrected_statement**: Measured against the 71 canonical positions listed in the scaffold's check (7lm@origin/main:.github/workflows/integrity.yml:47-59), each exemplar's origin/main (autonomous c9076c3, auditonomous 2165144) lacks exactly the same eight: L7/governance/controlled, L7/allications, and L7/allications/{publications, applications, communications, specifications, notifications, participations}. Each still holds the two former folders, L7/publications/ (9 files in Autonomous, 5 in Auditonomous) and L7/governance/restrictions/ (1 file, 0.md). The other 63 canonical positions (27 under L7, all 36 under L8) exist with correct first lines, and no sheet in either exemplar has a wrong heading (97 sheets in Autonomous, 78 in Auditonomous). No CANONICAL position under L8 is missing or misnamed. Outside the canon list, the scaffold's sheeted L6 inbox L8/L6/in/ (7lm@origin/main:L8/L6/0.md:79) exists in neither exemplar, and Autonomous carries an unsheeted filed directory spelled L8/L5/research/review/autonomous-theory/autonomouos/. Each exemplar's own integrity.yml still lists the former names (L7/governance/restrictions, L7/publications; 57 positions), so the eight are missing only against the scaffold's check, not the exemplar's own.
- **evidence_checked**
  - 7lm@origin/main:.github/workflows/integrity.yml:31-61 (G-003 step; canon list lines 47-59 counted = 71: 35 L7 + 36 L8)
  - Simulation of G-003 from git objects (ls-tree -r + show | head -n 1): 7lm@origin/main control = 75 sheets checked, 19 retired skipped, 0 wrong, 71/71 present
  - autonomous@origin/main (c9076c3): 97 sheets checked, 0 skipped, 0 wrong headings, 63 present, 8 missing (L7/governance/controlled, L7/allications and its six children)
  - auditonomous@origin/main (2165144): 78 sheets checked, 0 skipped, 0 wrong headings, 63 present, 8 missing (same eight)
  - git ls-tree -d --name-only origin/main L7/ L7/governance/ in both exemplars: L7/governance/restrictions present, no controlled, no L7/allications; L7/publications/binder present
  - autonomous@origin/main ls-tree -r L7/publications = 9 files (0.md, binder/0.md, binder/README.md, binder/internal/FETCH_LIST.md, binder/internal/README.md, binder/internal/tools/verify_fragments.py, binder/internal/tools/verify_fragments_v2.py, binder/press-kit/GLOSSARY_AUTONOMOUS.md, binder/press-kit/README.md); L7/governance/restrictions = 1 file (0.md)
  - auditonomous@origin/main ls-tree -r L7/publications = 5 files (0.md, binder/0.md, binder/README.md, binder/internal/README.md, binder/press-kit/README.md); L7/governance/restrictions = 1 file (0.md)
  - First lines: autonomous and auditonomous @origin/main:L7/publications/0.md:1 '# L7/publications/'; L7/governance/restrictions/0.md:1 '# L7/governance/restrictions/'
  - git ls-tree -d --name-only origin/main L8/ in both exemplars: L8/L0 through L8/L6, correct case; root = .github .gitignore L7 L8 README.md
  - Directory-tree comparison (ls-tree -r -d) scaffold vs exemplars: scaffold dirs absent from both = the 8 L7 positions, L8/L6/in, and three scaffold retired sets
  - 7lm@origin/main:L8/L6/in/0.md:1,3 ('# L8/L6/in/', 'The inbox for L6.'); 7lm@origin/main:L8/L6/0.md:79; git grep -F 'L6/in' in the specification file: no hit
  - autonomous@origin/main ls-tree -d: L8/L5/research/review/autonomous-theory/autonomouos (no 0.md)
  - diff of 7lm@origin/main:.github/workflows/integrity.yml against autonomous@origin/main and auditonomous@origin/main copies: exemplar canon lists L7/governance/restrictions and L7/publications, with no allications line and no peer-1/object-1 line
  - No paths with whitespace in any of the three trees (word-splitting in the check's for-loop does not affect the result)
