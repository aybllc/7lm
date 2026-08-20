# L7 — Scientific Desktop

L7 is the Scientific Desktop. It sits OUTSIDE the USO: no file in L7 is layer content, and
no file in L7 is a layer owner. L7 is where anything entering the system arrives, where
fixed authority bindings are held, where compositions are assembled, where a composition names
the live alternatives it did not select, and where process learning is recorded. L7 composes
results; it never acquires ownership of its dependencies. The layer that owns an artifact still
owns it after a composition uses it, and a composition-specific choice made here is never
universal supersession.

Direction of travel is asymmetric and deliberate. Intake is top-down through L7: every
incoming object enters at `intake/` before any layer sees it. The dependency audit runs the
other way, bottom-up from L0: a composition is only as sound as the lowest layer it names,
and L7 cannot repair a lower-layer meaning from above.

## Children

- `intake/` — provisional admission: the preserved source object, its origin and version,
  its candidate local artifacts, and their candidate layer owners.
- `PINNED/` — fixed bindings to authority artifacts, and nothing else; authority content
  stays in the owning repository.
- `compositions/` — assembled results that name every layer artifact and every pin they
  depend on.
- `process-lessons.md` — reusable process problems and what was changed in response.

## Manual work

1. Send every incoming object to `intake/` first. Nothing enters a layer directly, and
   nothing is routed out of intake before its meaning, scope, and owner are clear enough.
2. Prepare one local artifact at a time for adjudication. Its meaning, scope, and owner are
   settled by the layer owner that will own it and recorded in that owner's file; what L7
   does is make the artifact ready for that decision and record the candidates and
   contradictions it found.
3. Route each adjudicated artifact to the lowest layer that can state it without importing
   an unresolved assumption from a higher layer, and update that layer's `0.md` if the
   arrival changes what the directory means.
4. When a change alters a controlling technical use, update `uso/l0/definitions/0.md` in the
   same pass.
5. Admit a pin in `PINNED/` when a composition depends on an outside authority artifact:
   record the fixed referent, the immutable binding, the version, and the scope pinned for.
6. Build each composition in `compositions/` by naming its dependencies explicitly — layer
   artifacts by their owning layer, authorities by their pin. Never restate a dependency's
   content in the composition.
7. Keep unresolved alternatives visible where they arose. A live alternative that a
   composition did not select stays current and does not move to `uso/l6/history/`.
8. When an owner's artifact is defective, stop, correct it in the owning repository, then
   admit a new exact binding and preserve the earlier binding plus the successor relation.
9. Record the disposition by its own name — contradiction, tension, inconsistency,
   rejection, recall, failure, supersession — and never substitute one for another.

## Boundary

- L7 owns no layer artifact. Composing, pinning, or holding something here confers no
  ownership and no semantic authority.
- L7 never redefines, repairs, or silently selects among unresolved lower-layer meanings. A
  meaning is fixed by its layer owner or it stays open.
- Authority content is never copied, paraphrased, or routed down into `uso/`. Only the
  binding lives here.
- Multiple pins may be active at once. Pinning one authority does not rank, merge,
  invalidate, harmonize, or supersede another, and disagreement between independently
  scoped authorities is not by itself an owner defect.
- Custody, an exact hash, authority, internal consistency, or provenance establishes no
  scientific validity. Verification and validation are distinct, and neither is conferred
  by storage.
- No automation of any kind belongs in L7: no scripts, workflows, hooks, or generators.
  Everything here is done by hand.

When a problem you hit here is reusable rather than local to one artifact, record it in
/L7/process-lessons.md.
