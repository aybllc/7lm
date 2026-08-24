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

## Boundary

- L7 owns no layer artifact. Composing, pinning, or holding something here confers no
  ownership and no semantic authority.
- L7 never redefines, repairs, or silently selects among unresolved lower-layer meanings. A
  meaning is fixed by its layer owner or it stays open.
- Authority content is never copied, paraphrased, or routed down into `uso/`. Only the
  binding lives here.
- Custody, an exact hash, authority, internal consistency, or provenance establishes no
  scientific validity. Verification and validation are distinct, and neither is conferred
  by storage.
- No automation of any kind belongs in L7: no scripts, workflows, hooks, or generators.
  Everything here is done by hand.
