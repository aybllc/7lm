# 7lm — Agnostic USO Scaffold

This repository is a manual, documentation-only scaffold. It holds a seven-layer corpus at
`uso/l0` through `uso/l6`, plus an L7 "Scientific Desktop" that sits outside the USO. Every
directory carries a `0.md` stating what that directory means and what to do there by hand.
There is no code here, no build, and no automation. A newcomer's first job is to read the
`0.md` of the directory they intend to touch.

"Agnostic" means the scaffold commits to no domain, no subject matter, and no result in
advance. It is a structure for admitting material from any source, deciding what that
material locally means, and placing it where it can be stated without importing unresolved
assumptions from somewhere else. "USO" is used operationally here as the name of the local
L0-L6 corpus; its acronym expansion is author-controlled and is not inferred anywhere in
this scaffold.

## Directory map

```
7lm/
  README.md                      this file; no README.md exists under L7/ or uso/
  seven_layer_methodology.md     author-controlled; not maintained by scaffold work
  L7/                            Scientific Desktop; sits OUTSIDE the USO
    public/                      ingress/ (in, and where immutables rest)
                                 egress/  (out)
    private/                     durable/ (found/ caught/ naught/)
                                 regress/
    corpus/                      what is released
  uso/
    l0/
      definitions/
      epistemic/
      ontology/
      prior-art/
      semantic-formulas/
      semantics/
      thesis-statements/
    l1/
      state-space/
    l2/
      formal-mathematics/
    l3/
      engineering-mathematics/
    l4/
    l5/
    l6/
      history/
      provenance/
        source-ledger.md
```

Every directory under `L7/` and `uso/` carries a `0.md`. Internal directories never use
`README.md`, so the root file you are reading is the scaffold's only one.

## The layer map (L0-L6)

- **L0 — meaning and standing.** The base of the corpus. `definitions/` holds the
  controlled vocabulary and each term's definition status; `semantics/` holds
  source-scoped meaning and controlling use; `ontology/` holds the type, identity, and
  equivalence structure; `epistemic/` holds epistemic status and what would count as
  validation; `semantic-formulas/` holds the syntax and semantics of any formal notation
  the corpus relies on; `thesis-statements/` holds the claims the corpus makes as claims;
  `prior-art/` records what already exists outside, as a consumer record, not as authority
  content.
- **L1 — state-space.** The state space over which L0 meanings range: what varies, what is
  held fixed, what an admissible state is.
- **L2 — formal-mathematics.** Formal statements and results that name their L0 and L1
  dependencies explicitly.
- **L3 — engineering-mathematics.** Working mathematics with stated tolerances,
  approximations, and units — still general, not yet an application.
- **L4 — present application and implementation boundary.** Where the corpus meets a
  particular application. L4 is the current outer edge of practical work.
- **L5 — interpretation, review, and governance.** Deliberately minimal. It holds talk
  *about* the lower layers — interpretation, review, records of adjudications their layer
  owners made, ratification, and publication discourse — and never a substitute for what the
  lower layers state.
- **L6 — history and provenance.** `history/` holds what is no longer current — rejected,
  recalled, failed, or superseded artifacts, each with its disposition named, plus states retained
  because later material cannot be read without them — historical significance is a retention
  reason, not a disposition. `provenance/`
  holds the record of where artifacts came from and what succeeded what.

Ownership rule: after adjudication, the **lowest** layer able to state a local artifact
without importing unresolved assumptions from a higher layer owns it. A higher layer must
**name** the lower-layer definitions, interpretations, state spaces, and assumptions it
uses. A higher layer may not repair, silently select among, or redefine an unresolved
lower-layer meaning; it must exit and get the lower layer fixed by its owner.

## L7 — the Scientific Desktop, outside the USO

L7 is where anything entering the system arrives, where fixed authority bindings are held,
where compositions are assembled, and where process learning is recorded. It sits outside
the USO on purpose. Intake, bindings, compositions, and process lessons are not layer
content: if they lived inside a layer, that layer would silently own artifacts it never
adjudicated, and a composition-specific choice would leak into the corpus as though it were
universal. L7 composes results; it never acquires ownership of what it composes.

Direction matters. Intake is top-down through L7 — every incoming object enters at
`L7/public/ingress/` first. The dependency audit runs the other way, bottom-up from L0.

## The manual cycle: intake -> adjudication -> routing -> composition

1. **Intake.** The source object is preserved unchanged in `L7/public/ingress/` with its origin and
   version. It is decomposed provisionally into candidate local artifacts, each with one or
   more candidate layer owners. Early intake is provisional; overlap and contradiction are
   expected and are written down, not resolved on the spot.
2. **Adjudication.** The layer owner that will own the artifact settles its meaning, scope, and
   ownership, one local artifact at a time, and records the decision in that owner's file; L7
   only prepares the artifact for that decision.
   Candidate classification is not adjudicated routing or ownership.
3. **Routing.** Only an adjudicated artifact is routed, and only to the lowest layer that
   can state it cleanly. Unrouted material stays in intake with its open questions visible.
4. **Composition.** Compositions are assembled in `L7/corpus/`, naming every layer
   artifact and every pinned authority they depend on.

Two rules govern the cycle throughout. Contradiction, tension, inconsistency, rejection,
recall, failure, and supersession are different dispositions and are never collapsed into
one another. And a live alternative stays current: not being selected in one composition
does not send it to `uso/l6/history/`.

## PINNED

`L7/public/ingress/` holds fixed bindings to authority artifacts, and nothing else. Only the
binding — the fixed referent, its immutable identification, and the scope it is pinned for
— lives here. Authority content stays in its owning repository and is never copied,
paraphrased, or routed down into `uso/`.

Multiple pins may be active at once. Pinning one authority does not rank, merge,
invalidate, harmonize, or supersede another; disagreement between two independently scoped
authorities is not by itself a defect in either owner. `canonical` means owner-designated
as controlling for a stated scope and version — not proven, not validated, not universally
true. If an owner's artifact is defective, leave this consumer scaffold, correct it in the
owning repository, then admit a new exact binding and preserve both the earlier binding and
the successor relation.

## The 0.md gate convention

`0.md` is the local gate for its directory. It states what the directory means, what belongs
there, what does not, and the manual steps for working there. Read it before adding
anything to that directory, and update it in the same pass if what you add changes what the
directory means. `0.md` files are not duplicate ledgers and carry no approval chains.

## The definitions-list rule

Every change to a controlling technical use updates `uso/l0/definitions/0.md` in the same
pass. If you introduce a controlling term, narrow one, split one, retire one, or change which
use of a term is the controlling use, the definitions list changes with that work — never in a
later cleanup. A term controlling across more than one layer but absent from this list is a
defect to fix. Keep the two axes apart: a definition carries a definition status, a claim
carries an epistemic status, and neither implies the other.

## Where work happens

Work is concentrated in L0-L3. L4 is the present application and implementation boundary and
moves only as the lower layers can support it. L5 and L6 stay minimal by design — correctly
bounded, not filled out for symmetry.

## Boundary

- This repository holds no automation. No scripts, workflows, actions, hooks, generators,
  schemas, or templates. Everything here is done by a person, by hand, and reviewed by
  reading.
- Custody establishes nothing scientific. Holding an artifact here, hashing it, pinning it,
  or tracing its provenance does not make it valid. Integrity, authority, internal
  consistency, and provenance are separate from scientific validity, and none of them
  substitutes for it.
- Mapping and similarity never establish identity or semantic authority, and formal
  consistency under one interpretation does not choose that interpretation.
- `seven_layer_methodology.md` is outside this scaffold's documentation surface and is
  not maintained by scaffold work.

When a problem you hit here is reusable rather than local to one artifact, record it in
/L7/process-lessons.md.