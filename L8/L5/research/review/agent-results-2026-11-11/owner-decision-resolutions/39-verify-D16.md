# verify:D16

Agent result, as returned. Workflow: Resolutions for the 23 owner decisions. Run `wf_3293f65c-a92`. Phase: Verify.

- **quotes**
  - item 1
    - **locator**: auditonomous@origin/claude/book-structure-roadmap-k8ap82:L8/L6/history/restore-2026-09-14.md:7
    - **verbatim**: yes
    - **correction**: Verbatim at that line. The same sentence stands at autonomous@origin/claude/scholarly-pair-baseline-k8ap82:L8/L6/history/exemplar-2026-09-14.md:7. Both branches are closed pull requests that were never merged (neither is an ancestor of its origin/main), so the owner's sentence is on no model-of-record branch.
  - item 2
    - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:482
    - **verbatim**: yes
  - item 3
    - **locator**: 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:958
    - **verbatim**: yes
    - **correction**: Verbatim. Note the specification writes the peer's path as L0/semantics/definitions/AUTONOMOUS.md; the path L8/L0/semantics/definitions/AUTONOMOUS.md used in the resolution comes from the exemplar's record and the peer's egress sheet, not from this line.
  - item 4
    - **locator**: auditonomous@origin/main:L7/peering/public/ingress/peer-1/object-1/0.md:30
    - **verbatim**: yes
  - item 5
    - **locator**: auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:170
    - **verbatim**: yes
  - item 6
    - **locator**: auditonomous@origin/claude/book-structure-roadmap-k8ap82:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:586
    - **verbatim**: yes
    - **correction**: Verbatim, but it is a session's judgement of 14 September 2026 on a closed, unmerged branch, and the same table cell continues with the 'Not yet' items the resolver quotes under 'against'.
  - item 7
    - **locator**: auditonomous@origin/claude/book-structure-roadmap-k8ap82:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:631
    - **verbatim**: yes
    - **correction**: Verbatim. The 'peer's declaration' it names was carried by autonomous PR #29 (origin/claude/scholarly-pair-baseline-k8ap82), closed unmerged; the tag does not exist (the autonomous clone has no tags).
  - item 8
    - **locator**: owner's instructions of 11 November 2026, as typed (also auditonomous@origin/ccr-9391bd81-f2enmj:L8/L6/history/harmonization-2026-09-05.md:178)
    - **verbatim**: yes
  - item 9
    - **locator**: auditonomous@origin/claude/book-structure-roadmap-k8ap82:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:586 (the 'against' quotation, 'Not yet: ...')
    - **verbatim**: yes
  - item 10
    - **locator**: 7lm@origin/main:L8/L6/7lm-field-guide.md:634 (the 'against' quotation)
    - **verbatim**: yes
- **inference_holds**: no
- **objection**: Every quotation is verbatim at its locator, and the checked facts hold: blob ffbdc28 is identical at 0504961 and at the current path on autonomous main, PR #30, the beta and the scholarly-pair branch; 0504961 is an ancestor of autonomous main; the clone has no tags; PR #28 changes only the boundary sentence of the binding sheet. (The PR #28 branch now stands at 428bbaf, three check-in commits past 294c843; the pin is still untouched.)

  The resolution has three limbs and the quotations carry only one of them.

  1. Not rebinding before or inside the mirror: this holds. The owner's order of 11 November names the physical match and no rebinding; the specification and the exemplar record both reserve the rebinding to the owner; the sheet makes it a new record beside the old. The peer's own sheet agrees: "a later binding on the receiving side names the new path beside its old record; nothing here mutates the bound version" (autonomous@origin/main:L7/peering/public/egress/peer-1/object-1/0.md:13).

  2. "Treat peering as stable enough to start": this claims more than the quotations say.
  - The only stability finding is a session's, of 14 September, on a closed unmerged branch, and its own cell lists three things as "Not yet".
  - It predates the owner's own audit branch on peering (7lm origin/audit/peering-descriptive-reframe-2026-09-20, 158 commits authored by the owner on 20 September, including "Remove residual binding and local-authorship wording from L7 root" and "Teach peering as one relationship pattern, not universal attachment"). The scaffold's record says of that branch: "its disposition is still the owner's call (§36)" (7lm@origin/ccr-9391bd81-f2enmj:L8/L6/history/harmonization-2026-09-04.md:537).
  - It also predates the owner's beta of 2-3 November, which edits L7/peering/0.md in the scaffold.
  - The steps the owner put before the stability step are not on any main: the read-only exemplar declaration was on autonomous PR #29, closed unmerged, and the definition bytes are unchanged, so the review's fixes are not applied.
  - The owner's later word of 11 November already orders the QA handle after the model research and the physical match and asks for no stability finding. So the QA can follow the mirror on that word alone. A session need not, and should not, pronounce peering stable; the 14 September gate ("then start Auditonomous") still stands for the writing and is the owner's to lift.

  3. The commit: "the Autonomous main commit that results from merging its mirror" is in no quotation. D22 as quoted prefers a tag [source text withheld from the public copy], and that declaration was never merged. Because the bytes are identical, a post-mirror pin corrects only the path. It would be superseded by the first corrected version of the definition, which the owner's order of 14 September asks for (see the missed quotation).

  One statement in the alternatives is wrong. Alternative (d) says the beta "leaves object-1 alone". The owner's candidate edits object-1's sheet in place:
  - the Version line becomes the full hash (auditonomous@origin/beta/7lm-exemplar-auditonomous:L7/peering/public/ingress/peer-1/object-1/0.md:13);
  - it adds a provenance row AUT-SOURCE-001 and the blob and SHA-256;
  - it adds "| Convenience location | `L8/L0/semantics/definitions/AUTONOMOUS.md`, byte-identical; historical object/path remain the binding |" (same file, line 19);
  - its object-2 sheet says "Object-1 remains the unchanged historical definition binding." (same branch, L7/peering/public/ingress/peer-1/object-2/0.md:8);
  - it rewrites the paragraph on the three files.

  So the most recent owner-side candidate (unmerged, made by Codex, committed under the owner's name on 2 November) answers this decision as "keep 0504961, pin the bytes, note the current path", which is D22's third option and not a rebinding. It does so by mutating the record that says it "does not mutate this one". It is not the owner's typed word and does not override the specification, but it is a live option the resolution dismissed on a wrong description. The scaffold beta says the same in general terms: "The receiving project can review and adopt a new binding, retain the old one or mark the dependency unresolved" (7lm@origin/beta/common-contracts-r1-r6:L7/peering/0.md:20).
- **missed_quotation**: "[source text withheld from the public copy]." — owner, 2026-09-14, auditonomous@origin/claude/book-structure-roadmap-k8ap82:L8/L6/history/restore-2026-09-14.md:7 (same line as the stability sentence, immediately before it; also autonomous@origin/claude/scholarly-pair-baseline-k8ap82:L8/L6/history/exemplar-2026-09-14.md:7). It cuts against naming the post-mirror commit: the owner put a correct definition and a read-only exemplar ahead of the stability step, neither is on autonomous main, and a pin to the post-mirror commit binds the same uncorrected bytes.

  Second, also unused: "Auditonomous gets the definitions of autonomous from Autonomous and nowhere else." — owner, 2026-09-05, auditonomous@origin/main:L7/peering/public/ingress/peer-1/object-1/0.md:24 (also 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:73). It is the owner's own test of this peering; the four files that take the word from elsewhere fail it, and the resolution sets them aside as a separate edit while calling peering stable.
- **corrected_resolution**: Do not rebind before or inside the mirror. PR #28 and PR #30 leave the pin at 0504961 and stay that way. This part stands.

  Do not pronounce peering stable on a session's authority. Report its state to the owner instead:
  - In force: the binding at 0504961, reference-only, with bytes identical at the peer's current path L8/L0/semantics/definitions/AUTONOMOUS.md (blob ffbdc28).
  - Open: the record names the [source text withheld from the public copy], against the owner's rule of 5 September; the peer-3 hashes are unpinned; the read-only exemplar declaration and the definition fixes are on no main; two unmerged owner candidates touch peering (the audit branch of 20 September and the beta of 2-3 November).

  The QA handle on the research and manuscript goes ahead after the mirror on the owner's word of 11 November. It is read-only and that word asks for no stability finding. Starting the writing stays behind the owner's 14 September gate until the owner says peering is stable.

  The rebinding is the owner's act, after the mirror merges, as a new record beside the old one. A session does not pick the commit. Put three targets to the owner:
  (a) The Autonomous main commit after its mirror merges. This corrects the path only, pins the same bytes, and is superseded when a corrected definition version is merged.
  (b) The commit or tag at which the owner merges the read-only exemplar declaration or the first corrected definition version. This follows the owner's order of 14 September and D22's preference, and resolves the four files in the same sitting.
  (c) Keep 0504961 as the binding and add the blob hash and the current path as a note, as the owner's beta candidate does on object-1. This needs the owner's word, because it edits a record that says it is not mutated.

  Until the owner chooses, nothing is changed.
- **corrected_confidence**: Split. The quotations favour the timing: no rebinding before or inside the mirror, the owner's act, a new record beside the old. They do not settle the stability verdict or the commit; the owner must say both.
