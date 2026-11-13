# verify:K12

Agent result, as returned. Workflow: The model, read deep. Run `wf_9a60cf50-a5f`. Phase: Verify.

- **id**: K12
- **verdict**: corrected
- **reasoning**: Every cited locator is confirmed on 7lm@origin/main (c9dc061), and the four rules are still in force there. Two parts of the claim are imprecise against the same objects, so the verdict is "corrected", not "stands".

  **Confirmed as cited** (all in 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md)
  - :336 (section 26), owner: "All repos should mirror the 7lm. Manually. We update 7lm and focus on it only. No outside updates until we are sure I'm close."
  - :346: "they will be, manually, when the owner judges the scaffold close, and not before."
  - :482 (section 36), owner: "Don't change the system unless you ask or are unsure". The standing at :484 adds: "no change to the system without asking first; when unsure, ask instead of deciding."
  - :402 (section 31), owner: "Our 7Lm guides DO NOT share ANY HISTORY! HARD RULE. That's why you have l6."
  - :406: "Each repository's history is its own, kept at its own L6 and nowhere else."
  - :352 (section 27): "What is not a design choice is the tree the scaffold pushes and, in every folder of it, a `0.md` whose first line is the folder's path from the root."

  **Nothing later overrides them**
  - The record on main ends at section 37. Section 37 (:506) corrects section 31 only on where the rule sits in the guide ("a bold lead-in ... not under its own heading"). Its reading at :510 keeps section 36 in force ("no leave to change what any position is, holds, or is named").
  - 2e5a6d6..origin/main adds one file only, L8/L6/in/7lm-layer-lists.md (PR #21).
  - The field guide on main restates all four: L8/L6/7lm-field-guide.md:608, :132, :240, :455, :457.

  **Imprecision 1: "nothing of the scaffold's L6 is copied" is broader than the rule**
  - What the rule bars is history. :406 and guide :610: "The push carries the tree and the sheets, never the scaffold's L6; no repository's history moves in either direction."
  - But the scaffold's L6 also holds two source documents the model says an adopter takes, by a person's act:
    - the guide: :340 and guide :9 ("A person who adopts the model takes this guide from L6, applies its updates or leaves them"), guide :608 ("this guide at L6 as the source each adopter takes");
    - the sheet templates: :364 ("beside the guide at L6 as source material an adopter takes").
  - So the scaffold's history/, retired/ and in/ must not be copied; the guide and templates are not barred by the rule, and what an adopter does with them is its design choice (guide :610).
  - Tree check: neither exemplar holds a copy of 7lm-field-guide.md, 7lm-sheet-templates.md, harmonization-2026-09-04.md or specification-history.md, on origin/main or on the beta branch (ls-tree). Each has its own L8/L6/history/ with its own harmonization-2026-09-05.md, so "recorded in each exemplar's own record" is workable.

  **Imprecision 2: the list of what is not a design choice has a third member on main**
  - Section 31 (:408) added the no-shared-history rule to that list. Guide :554: "The tree, the sheets' first lines, and the rule that the guides share no history are not."
  - The same line names "whether a position is used at all" as a design choice; guide :610: "The pushed tree is required; taking up everything in it is not".
  - "Everything else a sheet says is the repository's own choice" is correct (:352, L8/L6/7lm-sheet-templates.md:3).

  **Minor: labels**
  - The record calls only two of the four "standing" (:346 "Standing.", :480 heading). Section 31 is the owner's "HARD RULE"; section 27 is an owner ruling with no label.
- **corrected_statement**: Four rules of the model of record (7lm@origin/main c9dc061, L8/L6/history/harmonization-2026-09-04.md, sections 26, 27, 31 and 36; none altered by section 37 or by PR #21) govern the pass. (1) Standing, section 26 (:336, :346): the exemplars mirror the scaffold by hand, when the owner judges the scaffold close and not before. (2) Standing, section 36 (:482, :484): the system is not changed without asking; when unsure, ask; findings go to the owner as proposals and nothing is applied until the owner says which. (3) The owner's hard rule, section 31 (:402, :406): the guides share no history; each repository's history is its own, kept at its own L6 and nowhere else. So the pass is recorded in each exemplar's own L8/L6/history/, and none of the scaffold's history (its L8/L6/history/, retired/, in/) is copied into an exemplar. The rule does not bar the two source documents filed at the scaffold's L6, the field guide and the sheet templates, which the model says an adopter takes by a person's (HOA) act as its own design choice (:340, :364; guide :9, :608, :610); neither exemplar holds a copy of either on main or beta. (4) Section 27 (:352), as extended by section 31 (:408; guide :554): what is not a design choice is the tree the scaffold pushes, in every folder of it a 0.md whose first line is the folder's path from the root, and the rule that the guides share no history; everything a sheet says after its first line is the repository's own choice, and whether a position is used at all is also a design choice (guide :554, :610).
- **evidence_checked**
  - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:336 (section 26 owner quote, verbatim match)
  - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:340 (guide is an L6 source document the adopter takes)
  - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:346 ('they will be, manually, when the owner judges the scaffold close, and not before')
  - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:350-352 (section 27: what is not a design choice)
  - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:364 (templates 'beside the guide at L6 as source material an adopter takes')
  - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:402-408 (section 31 hard rule; push carries 'never the scaffold's L6'; Design choice vocabulary names the rule)
  - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:480-484 (section 36 heading, owner quote, standing)
  - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:492-510 (section 37: correction to section 31 is placement only; reading keeps section 36)
  - 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md headings (grep '^## '): sections 1 to 37, none later
  - 7lm: git log 2e5a6d6..origin/main and diff --stat: only L8/L6/in/7lm-layer-lists.md added (PR #21)
  - 7lm@origin/main:L8/L6/7lm-field-guide.md:9, :132, :240, :455, :457, :554, :608, :610
  - 7lm@origin/main:L8/L6/7lm-sheet-templates.md:3-9
  - 7lm@origin/main:L8/L6/0.md:1-45
  - 7lm@origin/main ls-tree L8/L6 (guide and templates sit directly at L6 beside history/, in/, retired/)
  - 7lm@origin/beta/common-contracts-r1-r6:L8/L6/history/harmonization-2026-09-04.md headings: also ends at section 37
  - autonomous@origin/main and @origin/beta/7lm-exemplar-autonomous ls-tree L8/L6: own history/ (harmonization-2026-09-05.md; BETA_HISTORY.md on beta); no copy of scaffold guide, templates or records
  - auditonomous@origin/main and @origin/beta/7lm-exemplar-auditonomous ls-tree L8/L6: own history/ (harmonization-2026-09-05.md; AUDITONOMOUS_BETA_HISTORY.md on beta); no copy of scaffold guide, templates or records
