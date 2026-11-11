# resolve:D16

Agent result, as returned. Workflow: Resolutions for the 23 owner decisions. Run `wf_3293f65c-a92`. Phase: Resolve.

- **decision**: 16. Whether peering is stable enough to start, and whether the Autonomous definition is rebound before or after the mirror and to which commit.
- **resolution**: Treat peering as stable enough to start on the binding in force (0504961, reference-only), and do not rebind before or inside the mirror: PR #28 leaves the binding record's pin untouched and should stay that way. After the two mirror PRs are merged, the owner rebinds in one sitting by writing a new binding record beside the old one that names the peer's current path L8/L0/semantics/definitions/AUTONOMOUS.md at a commit the owner names: the Autonomous main commit that results from merging its mirror (or a tag the owner creates there); until then nothing is changed.
- **reasoning**
  - item 1
    - **speaker**: owner
    - **quote**: [source text withheld from the public copy].
    - **locator**: auditonomous@origin/claude/book-structure-roadmap-k8ap82:L8/L6/history/restore-2026-09-14.md:7
    - **bears**: The owner made peering stability a precondition of starting Auditonomous, so the question must be answered before the research and manuscript work, but the words do not themselves say that stability requires a rebinding.
  - item 2
    - **speaker**: owner
    - **quote**: Don't change the system unless you ask or are unsure
    - **locator**: 7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:482
    - **bears**: A session may not rebind on its own motion; the rebinding is put to the owner as a proposal and nothing is applied until the owner says which.
  - item 3
    - **speaker**: specification
    - **quote**: the same object now stands at the peer's L0/semantics/definitions/AUTONOMOUS.md, and rebinding to a current version is the owner's act.
    - **locator**: 7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:958
    - **bears**: The specification reserves the rebinding to the owner and says the object is the same one at a new path, so the stale path is a recorded shortfall and not a broken binding.
  - item 4
    - **speaker**: sheet
    - **quote**: An upstream change creates a new binding record beside this one; it does not mutate this one.
    - **locator**: auditonomous@origin/main:L7/peering/public/ingress/peer-1/object-1/0.md:30
    - **bears**: The rebinding is additive and reversible: a new record is written beside the old, the 0504961 record stays, so the mirror need not and should not edit the pin.
  - item 5
    - **speaker**: record
    - **quote**: the binding pinned by the record at `L7/peering/public/ingress/peer-1/object-1/`, the peer's path `research/definitions/AUTONOMOUS.md` at commit `0504961`, as it was, rebinding to a current version being the owner's act
    - **locator**: auditonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:170
    - **bears**: The exemplar's own record sets the precedent that a structural pass (the rename pass) leaves the pin as it was; the mirror of 11 November is a pass of the same kind, so rebinding is kept out of it.
  - item 6
    - **speaker**: record
    - **quote**: [source text withheld from the public copy].
    - **locator**: auditonomous@origin/claude/book-structure-roadmap-k8ap82:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:586
    - **bears**: The only recorded stability judgement (a session's, on a closed unmerged branch) found peering stable with the binding still at 0504961, treating the rebinding as an owner follow-up and not as a blocker; the L7 restructure since then moved no peering position.
  - item 7
    - **speaker**: record
    - **quote**: [source text withheld from the public copy]
    - **locator**: auditonomous@origin/claude/book-structure-roadmap-k8ap82:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:631
    - **bears**: Decision D22 as put to the owner already preferred binding after the peer's own change is merged, to a point the owner creates, over binding at once to c9076c3; the same logic puts the rebinding after the Autonomous mirror merges.
  - item 8
    - **speaker**: owner
    - **quote**: we need to uipdate the autonomous and auditonomous repos phsyciall; to match first .
    - **locator**: owner's instructions of 11 November 2026, as typed
    - **bears**: The owner's present order puts the physical match first and names no rebinding, so the mirror goes ahead of the rebinding and is not widened to include it.
- **against**: "[source text withheld from the public copy]" (auditonomous@origin/claude/book-structure-roadmap-k8ap82:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:586). Read with the owner's "[source text withheld from the public copy].", this supports the opposite view: that peering is not stable until the binding is current, so the rebinding should come before any Auditonomous research or manuscript work starts. The field guide also still lists "Rebinding the Autonomous definition in Auditonomous to its current path." as an open call (7lm@origin/main:L8/L6/7lm-field-guide.md:634).
- **alternatives**: (a) Bind now to c9076c3, Autonomous main today, the first option in D22: it can be done at once and the content is the same, but it pins a commit whose L7 still has the former layout and would be stale on the day the mirror merges. (b) Bind to a719cec, the head of draft PR #30: rejected, because it is an unmerged branch commit and may not survive the merge. (c) Keep 0504961 indefinitely, the third option in D22: nothing changes, but the specification's "Not yet as stated" entry stays open. (d) Take the beta's route, which leaves object-1 alone and adds peer-1/object-2 with a binding.json: this binds a different object (a synthetic result), pins unmerged commits and does not rebind the definition.
- **confidence**: the quotations favour it
- **who_acts**: The owner. The specification and both records call the rebinding "the owner's act", and the stability judgement is the owner's under the order of 14 September 2026. A session may only draft the new binding record as a proposal once the owner names the commit or tag. The owner needs to say two things: (1) "peering is stable, start" or "rebind first"; (2) the commit or tag of aybllc/autonomous to bind to.
- **what_it_costs**: Nothing now: no file changes, and the mirror PRs stay as they are. Auditonomous keeps a binding that names the pre-7LM path research/definitions/AUTONOMOUS.md until the owner's sitting, so the specification's "Not yet as stated" line (SPEC:958) and the guide's open call (GUIDE:634) stay true a little longer.

  Facts checked in git objects:
  - The definition is byte-identical (blob ffbdc28) at 0504961:research/definitions/AUTONOMOUS.md and at L8/L0/semantics/definitions/AUTONOMOUS.md on autonomous origin/main (c9076c3), on PR #30 (a719cec), on the beta and on the scholarly-pair branch. Waiting therefore changes no meaning, only the path and commit named.
  - 0504961 is an ancestor of autonomous main.
  - The autonomous clone has no tags, so the tag D22 names (exemplar-2026-09-14) does not exist.
  - PR #28 changes one line of the binding sheet (the boundary sentence) and leaves the pin alone.

  The later rebinding costs one new sheet beside object-1 and is reversible, because the old record is never overwritten. The four files that [source text withheld from the public copy] are a separate owner edit and are not resolved by this.
