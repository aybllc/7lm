# The USO corpus (L0-L6)

This directory holds the seven-layer corpus: one layer per directory, L0 through L6. The Scientific
Desktop at /L7 is NOT part of this corpus. It sits outside as the working surface where every
incoming object first arrives (intake), where fixed authority bindings are held (PINNED), where
compositions are assembled, and where process learning is written down. "USO" is used here only as
the operational name of this local L0-L6 corpus; the acronym expansion is not asserted anywhere in
this scaffold and remains author-controlled.

## The layers

| Layer | The question it answers | What lives here |
| --- | --- | --- |
| L0 | What does it mean, and what is being claimed? | ontology, semantics, definitions, semantic formulas, prior art, thesis statements, epistemic status |
| L1 | What states are admissible? | state spaces, admissibility conditions, the objects a claim is allowed to range over |
| L2 | What exact mathematics holds? | formal mathematics: exact statements, derivations, proofs, and the assumptions each one names |
| L3 | What happens under finite precision and measurement? | engineering mathematics: rounding, tolerance, measurement, error budgets, numerical behaviour |
| L4 | What is actually applied and implemented? | the present application and implementation boundary: what has been built or used, and against which named lower-layer meanings |
| L5 | How is it interpreted, reviewed, governed? | interpretation, review, governance; adjudication and ratification records |
| L6 | What is the record of origin and displacement? | provenance and history: where an artifact came from, and what was rejected, recalled, failed, or superseded |

## Two directions of travel, never merged

TOP-DOWN intake runs L7 -> corpus. Every incoming object enters at /L7/public/ingress first. Early intake is
provisional: one source may bear on several artifacts, and one artifact may have several candidate
owners. Candidate classification is not adjudicated routing and is not ownership. Route a local
artifact into a layer only after its current meaning, scope, and owner are sufficiently clear.

BOTTOM-UP dependency audit runs L0 -> upward. It starts at L0 and walks up, checking that each layer
names the lower-layer definitions, interpretations, state spaces, and assumptions it uses, and that
no higher layer has repaired, silently selected among, or redefined an unresolved lower-layer
meaning. Do not run intake and audit as one pass; they answer different questions.

## Ownership and naming

- Lowest competent layer owns. After adjudication, the lowest layer able to state a local artifact
  without importing unresolved assumptions from a higher layer is its layer owner.
- Higher layers must NAME what they use. An unnamed lower-layer dependency is an audit finding
  against the higher layer, not against the lower one.
- A higher layer cannot repair, silently select, or redefine an unresolved lower-layer meaning. It
  may record that the ambiguity blocks it, and an L4 application record or a composition at
  /L7/corpus may make an application-scoped or composition-scoped choice - which is not
  universal supersession.
- Live alternatives stay live. Non-selection in one composition does not send an artifact to L6
  history.

## Where the work is

Work is concentrated in L0-L3. L4 is the present application and implementation boundary: it is
where this corpus meets something actually built or used, and it is as far as the present scaffold
reaches in that direction. L5 and L6 are deliberately minimal but correctly bounded, so that
interpretation and governance material, and origin and displacement material, have a correct home
instead of silently accumulating in L0-L4.

## Manual work

1. Confirm the object is recorded in /L7/public/ingress with its source. If it is not, stop and enter it
   there first.
2. Read the object for its current meaning and scope, not for where it would be convenient to file.
3. List every candidate layer owner you can defend and say why each is a candidate; more than one is
   a normal result, not a problem to be closed early.
4. Adjudicate only when meaning, scope, and owner are sufficiently clear. If they are not, leave the
   object provisional in intake and write down what would settle it.
5. Route the artifact to the lowest competent layer, then open that layer's 0.md and follow its
   local checklist.
6. In the receiving layer, name every lower-layer definition, interpretation, state space, and
   assumption the artifact relies on.
7. If the artifact depends on an external authority, admit the fixed binding at /L7/public/ingress and
   reference that binding; never copy authority content into uso/.
8. Before calling a layer settled, run the dependency audit bottom-up from L0 and record every
   unnamed dependency as an open item at the higher layer.

## Boundary

- /L7 is not an eighth member of the L0-L6 sequence. Nothing in uso/ may treat it as one.
- Authority CONTENT never enters uso/. Only a fixed binding lives at /L7/public/ingress; the content stays in
  its owning repository and is never copied, paraphrased, or routed down.
- Multiple pins may be active at once. Pinning one authority does not rank, merge, invalidate,
  harmonize, or supersede another, and disagreement between independently scoped authorities is not
  by itself an owner defect.
- If an owner's artifact is defective, leave this consumer corpus, correct it in the owning
  repository, admit a new exact binding, and preserve the earlier binding plus the successor
  relation.
- Do not collapse dispositions. Contradiction, tension, inconsistency, rejection, recall, failure,
  and supersession are different and are recorded differently.
- Repository custody, an exact hash, authority, internal consistency, or provenance does not by
  itself establish scientific validity.
- Do not expand the USO acronym in any file of this corpus.

Reusable process problems - anything that will recur across objects rather than belong to one
artifact - go to /L7/process-lessons.md.
