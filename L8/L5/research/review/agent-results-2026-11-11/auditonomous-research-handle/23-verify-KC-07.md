# verify:KC-07

Agent result, as returned. Workflow: Handle on the Auditonomous research and manuscript. Run `wf_9c2917a7-7f0`. Phase: Verify.

- **id**: KC-07
- **verdict**: corrected
- **reasoning**: Most of the claim is confirmed from the git objects; four parts are imprecise or rest on a locator that does not say what it is cited for.

  CONFIRMED
  - Binding. MAIN:L7/peering/public/ingress/peer-1/0.md:10 carries the owner's sentence "Auditonomous gets the definitions of autonomous from Autonomous and nowhere else. — owner, 2026-09-05". MAIN:.../object-1/0.md:13 reads "[source text withheld from the public copy]". Line 10 names the object `aybllc/autonomous:research/definitions/AUTONOMOUS.md`.
  - Date. Commit 050496161a848ea26492b8468e59afc7e0c07282 is dated 2026-08-14 18:56:51 -0700, which is 2026-08-15 01:56:51 UTC. "14 August" holds in the author's timezone only.
  - Bytes. I recomputed [source text withheld from the public copy], 315 lines. It is identical at 0504961:research/definitions/AUTONOMOUS.md and at Autonomous origin/main (c9076c3):L8/L0/semantics/definitions/AUTONOMOUS.md. It is also identical on Autonomous beta e64b382 and on 9b49910. The path differs between the pin and main; the bytes do not.
  - Plural entry. Lines 24-25 of the [source text withheld from the public copy]." Lines 70-80 hold eleven rows, A1 to A11.
  - Review. Autonomous origin/main:L8/L5/research/review/REVIEW_4_AUTONOMOUS_ADJUDICATION.md:451: "[source text withheld from the public copy]." Lines 458-466 list seven fixes (i) to (vii). The same blob is already present at commit 5a32fea (2026-08-08), so none of the seven fixes has been applied. I found no delta re-review and no CLEARS record on Autonomous main.

  IMPRECISE OR OVERSTATED
  1. "Takes 'autonomous' from one object" is the owner's rule and the binding, not confirmed practice on MAIN. MAIN:object-1/0.md:34 records: "Three files at HEAD still take a definition of *autonomous* from somewhere other than this [source text withheld from the public copy]). MAIN:L8/L6/history/harmonization-2026-09-05.md:93 leaves them open, and 7lm origin/main specification:958 repeats this under "Not yet as stated". I confirmed all three exist on MAIN (AUDITONOMOUS_DEFINITION.md:263, REQUIREMENTS_OWNERSHIP.md:268, CONTRADICTIONS.md:36-37). Only BETA (unmerged) says they "now carry explicit receiving-use dispositions" (BETA:object-1/0.md:36). BETA also adds a second ingress object from the same peer, object-2, which is a result handoff and not a definition.
  2. "Nine bodies" is a count no document makes. The entry's own headline says "[source text withheld from the public copy]" (line 39). REVIEW_4 F10 (lines 51, 299-306) calls that count [source text withheld from the public copy] Body column has ten distinct strings; the Auditonomous binding (MAIN:object-1/0.md:28) names eight organisations. Nine is reached only by merging the two IEEE rows while keeping the three ISO committees apart.
  3. "Eleven definitions" needs a caveat. A10 defines "autonomic", which the entry calls "a different word" (line 79). The entry's own §6 says "the ten above" and "A1…A10" (lines 244, 246), which is REVIEW_4 F4.
  4. "Blocks its gate" misnames the gate. It is the C-001 gate of RULINGS.md (opening "[source text withheld from the public copy]", REVIEW_4:9-10), not a gate belonging to the entry. The review blocks the prerequisite only: "[source text withheld from the public copy]" (line 469). The review is a single internal reviewer with "External Sources Checked: NONE" (line 503).
  5. "No consensus baseline exists" is not what the cited locator says. MAIN:L8/L0/0.md:79 only quotes the specification's requirement ("state and freeze the narrowest reasonable agreement…"; "Auditonomous consumes the pinned Autonomous consensus baseline"). On merged states the absence is confirmed by search only: a grep for "consensus baseline" and "narrowest reasonable agreement" across every ref of the three repositories returns only the requirement text. The explicit statement exists only on unmerged branches:
     - Autonomous beta e64b382:L8/L0/0.md:105: "a plural A1–A11 entry, not a demonstrated common consensus baseline".
     - Autonomous beta:L8/L5/research/review/BETA_SOURCE_OVERLAY.md:11: "[source text withheld from the public copy]."
     - Auditonomous BETA:L8/L0/0.md:81: "a complete consensus-plus-local-delta result is not claimed".
     - 7lm beta 97314c5:L7/0.md:190: "a research obligation, not an assertion that agreement has been established".
     The "baseline paper" on the closed-PR branch 9b49910 is a draft composition over the plural entry and states no narrowest-agreement baseline.

  ADDITIONAL CONTRADICTION NOT CITED
  Autonomous origin/main:L8/L0/semantics/definitions/REGISTER.md:19 [source text withheld from the public copy]", while the entry at line 24 says ADOPTED. Only the unmerged Autonomous beta corrects the register.

  EVIDENCE STATE (mine)
  - Byte identity: INTERNALLY CHECKED.
  - Single-source rule: ASSERTED by the owner, and CONTRADICTED in practice on MAIN by the three recorded files.
  - Gate: UNRESOLVED (blocked, seven fixes unapplied).
  - Consensus baseline: EMPTY (required by the specification, not produced).
- **corrected_statement**: By [source text withheld from the public copy] and the binding at MAIN:L7/peering/public/ingress/peer-1/object-1/, Auditonomous is to take "autonomous" from one object: aybllc/autonomous:research/definitions/AUTONOMOUS.md at commit 0504961 (2026-08-14 18:56 -0700, which is 2026-08-15 UTC). MAIN's own binding record says three files still take a definition of autonomous from elsewhere ([source text withheld from the public copy]); only the unmerged BETA claims dispositions for them. The pinned bytes (blob ffbdc28, SHA-256 2756661749c3…a12b, 22,735 bytes) are unchanged on Autonomous main today at the new path L8/L0/semantics/definitions/AUTONOMOUS.md, and also on the Autonomous beta and closed PR #29 branches. The object is a plural entry of eleven rows, A1 to A11, that declines to state a single definition. Its headline says "Six Tier-1 bodies"; its own review counts 8 to 10 depending on grouping; no document says nine. Row A10 defines "autonomic", which the entry calls a different word, and the entry's own §6 still says "the ten above". Autonomous's internal adversarial review of 2026-08-08 (REVIEW_4) "[source text withheld from the public copy] a seven-item fix set. None of the seven is applied, since the blob predates the review, and the gate declaration is reserved to the owner. The Seven-Layer Model specification requires an Autonomous "consensus baseline", and none is found in any ref of the three repositories. On merged states this is confirmed by absence only: MAIN:L8/L0/0.md:79 states the requirement, not the absence. The explicit statement "[source text withheld from the public copy]" exists only on the unmerged Autonomous beta (e64b382), echoed by Auditonomous BETA and the 7lm beta. Autonomous main's REGISTER.md still lists "autonomy / autonomous" as not yet entered, contradicting the entry's ADOPTED status.
- **evidence_checked**
  - MAIN:L8/L5/research/review/STATUS_LADDER.md and STATUS_AND_LABEL_DISCIPLINE.md (read for labels)
  - MAIN:L7/peering/public/ingress/peer-1/0.md:10,12,20,22 (owner's rule; only-source statement; holdings)
  - MAIN:L7/peering/public/ingress/peer-1/object-1/0.md:10,13,28,34 (object identity research/definitions/AUTONOMOUS.md; version 0504961; eight named bodies; three files still departing from the binding)
  - MAIN:L8/L0/0.md:79,98 (spec requirement of a consensus baseline quoted; rule restated; no statement that a baseline is absent)
  - MAIN:L8/L6/history/harmonization-2026-09-05.md:11,93 (three departures left as open owner decisions)
  - MAIN:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:263; MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:268; MAIN:L8/L5/research/review/CONTRADICTIONS.md:36-37 (the three departures exist)
  - ROADMAP (9259c18): L7/peering/public/ingress/peer-1/ unchanged from MAIN (git diff --stat shows no change there)
  - BETA (714480d):L7/peering/public/ingress/peer-1/object-1/0.md:13-19,36; object-2/0.md and binding.json; L8/L0/0.md:81; L7/provenance/sources/LEDGER.md:153 (AUT-SOURCE-001, same blob and SHA-256); L8/L0/semantics/AUDITONOMOUS_BETA_SCOPE.md
  - autonomous 0504961: git log -1 (050496161a848ea26492b8468e59afc7e0c07282, 2026-08-14 18:56:51 -0700, 'Update RULINGS.md'); ancestor of origin/main c9076c3
  - autonomous blob ffbdc28be7b47a83c9354526ac034596ba7b6e9a: sha256sum recomputed = 2756661749c3e322d3c13abc5104cb8d7b4d07203905611c4ec5196b9aa1a12b, 22,735 bytes, 315 lines, at 0504961:research/definitions/AUTONOMOUS.md, origin/main:L8/L0/semantics/definitions/AUTONOMOUS.md, e64b382 and 9b49910 (same path); same blob at 5a32fea/b0ef129/c866842:definitions/AUTONOMOUS.md
  - autonomous origin/main:L8/L0/semantics/definitions/AUTONOMOUS.md:24-25, 38-39, 70-80, 79, 244-247 (plural entry; 'Six Tier-1 bodies'; eleven rows; A10 'a different word'; 'the ten above', 'A1…A10')
  - autonomous origin/main:L8/L5/research/review/REVIEW_4_AUTONOMOUS_ADJUDICATION.md:1-34, 42-56, 299-306, 433-471, 503, 517-520 (15 findings; F10 8-10 bodies; [source text withheld from the public copy]; seven fixes; declaration is Eric's; no external sources checked)
  - autonomous origin/main:L8/L0/semantics/definitions/REGISTER.md:10-19 ('autonomy / autonomous' under 'Not yet entered')
  - autonomous origin/main:L7/peering/public/egress/peer-1/object-1/0.md:10-15; L7/peering/public/egress/0.md:37
  - autonomous origin/main: grep for CLEARS / delta re-review / REVIEW_4 (no later clearing record; L8/L6/history/LEDGER.md:813 and HUB_SURVEY_2026-08-14.md:793 repeat the block)
  - autonomous origin/beta/7lm-exemplar-autonomous (e64b382):L8/L0/0.md:105; L8/L5/research/review/BETA_SOURCE_OVERLAY.md:3,11; L8/L0/semantics/definitions/BETA_SCOPE.md; REGISTER.md diff; L7/peering/public/egress/peer-1/object-2/
  - autonomous origin/claude/scholarly-pair-baseline-k8ap82 (9b49910):L8/L4/work/writing/papers/AUTONOMOUS_BASELINE_PAPER_2026-09-14.md:1-120 and grep for baseline/consensus; L8/L6/history/exemplar-2026-09-14.md
  - git grep -i 'consensus baseline|narrowest reasonable agreement' over auditonomous MAIN/ROADMAP/BETA, autonomous main/beta/scholarly branch, 7lm main/beta (only requirement text, plus the beta negatives)
  - 7lm origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:42,44,958; 7lm origin/beta/common-contracts-r1-r6:L7/0.md:190
