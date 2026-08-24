# L2 / formal-mathematics - Exact Objects and Open Obligations

This directory holds the exact mathematics: objects, notation, domains, codomains,
operators, axioms, derivations, proofs, counterexamples, and the register of open
obligations. Every artifact here is written under one named L0 interpretation and one named
L1 declaration, and is exact - no finite precision anywhere in it.

## What an artifact record must carry

| Field | Required content |
| --- | --- |
| Artifact name | A stable name that does not assert the result it is trying to establish. |
| Selected L0 interpretation | The named L0 artifact, its definition status, and the scope it is controlling for. |
| Named L1 declaration | The declaration this artifact works over, plus the variables, domains, and invariants used. |
| Notation | Every symbol introduced, with its reading; no symbol reused across incompatible senses. |
| Domains and codomains | Stated for every operator and every map, including where the operator is partial. |
| Axioms and primitives | What is assumed without proof here, marked as assumed. |
| Derivation or proof | The argument itself, with each step's dependence on an axiom or a prior artifact named. |
| Counterexamples | Cases that defeat a stated claim, kept with the claim they defeat. |
| Open obligations | Everything needed but not established, listed as open. |
| Composite parts | For a composed object, the pieces used and the state of the compatibility argument. |

## Manual work

1. Name the selected L0 interpretation and the L1 declaration in the artifact header; an unnamed artifact is not exact about anything in particular.
2. Introduce notation once, and check it against the notation already in use in this directory before reusing a symbol.
3. Give every operator an explicit domain and codomain, and say where it is partial rather than letting the partiality be discovered later. Where an L1 declaration's domain is a quantity on an interval or ratio scale, name the scale type in the artifact header and state which operations that scale admits; excluding units here does not license treating a scale-bearing quantity as a bare real.
4. Mark axioms and primitives as assumed at the point of use, so that a reader can separate what is proved here from what is taken.
5. Write the derivation so each step names the axiom, operator, or prior artifact it depends on.
6. Write down every open obligation the moment it appears, in the artifact and in the register; an obligation that is merely postponed in your head has been deferred silently.
7. For any composed object, write the compatibility argument explicitly and mark the object unverified until that argument exists.
8. Record counterexamples against the claim they defeat, and mark that claim as defeated rather than quietly narrowing it.
9. Route an artifact whose owner or layer is not yet adjudicated back through L7 ingress rather than treating placement here as settled.

## Open obligations

- An open obligation is recorded as open. It is never dropped, never softened into a remark, and never closed by the artifact that needs it.
- Each obligation names what would close it: a proof, a counterexample, an L1 declaration, or an L0 adjudication.
- An obligation that belongs to a lower layer is recorded here by name and raised in the owning layer. L2 does not close L1 or L0 obligations on its own authority.
- An artifact with open obligations may be used, cited, and extended; it may not be presented as established.

## Terms used here

| Term | Working definition | Basis |
| --- | --- | --- |
| operator | A named map with a stated domain and codomain, total or explicitly partial. | Project working use |
| axiom | A statement assumed without proof inside this artifact and marked as assumed. | Project rule |
| derivation | A stepwise argument in which each step names what it depends on. | Project working use |
| proof | A derivation that establishes its claim under the named interpretation and declaration. | Project working use |
| counterexample | A case that defeats a stated claim under its own named interpretation and declaration. | Project rule |
| open obligation | Something the artifact needs and has not established, recorded as open. | Project rule |
| composite object | A new object assembled from existing objects, unverified until compatibility is shown. | Project rule |

`syntax`, `semantics`, and `claim` are owned at /uso/l0/definitions/0.md and are named, not
restated, here; this table holds only terms controlling inside L2.

## Source anchors

Quoted to anchor terminology only. No source below evaluates, endorses, or validates this
layer architecture, this directory, or any artifact written in it.

- ISO/IEC/IEEE 31320-2:2012(E), 3.1.195, page 23: "syntax: The structural components or features of a language and rules that define the ways in which the language constructs may be assembled together to form sentences."
- ISO/IEC/IEEE 31320-2:2012(E), 3.1.175, page 21: "semantics: The meaning of the syntactic components of a language."
- ISO/IEC/IEEE 31320-2:2012(E), 3.1.63, page 14: "formalization: The precise description of the semantics of a language in terms of a formal language such as first order logic."
- ISO/IEC/IEEE 24765:2017(E), 3.575 'claim', definition 2, printed page 69: "2. true‐false statement about the limitations on the values of an unambiguously defined property — called the claim's property — and limitations on the uncertainty of the property's values falling within these limitations during the claim's duration of applicability under stated conditions"
- ISO/IEC/IEEE 24765:2017(E), 3.4538 'verification', Note 1 to entry, printed page 503: "A system could be verified to meet the stated requirements, yet be unsuitable for operation by the actual users."
- JCGM 200:2012 (VIM), Conventions - "Terminology rules", printed page xii: "In some definitions, the use of non-defined concepts (also called “primitives”) is unavoidable."

## Boundary

- No finite-precision results, no measurement, no units-with-uncertainty. Those are L3. A number that came from a computation with a rounding rule does not belong in an L2 artifact.
- Component validity does not imply composite validity: an object built from valid pieces is unverified until its compatibility is shown, and inheritance of validity is never automatic.
- Formal consistency under one interpretation does not choose that interpretation, and does not make a live alternative interpretation obsolete.
- L2 may not repair, silently select, or redefine an unresolved L0 meaning or an unresolved L1 declaration.
- A semantic mapping between two artifacts is not semantic authority over either, and similarity between two derivations does not establish identity or equivalence.
- Custody here, an exact hash, or a clean provenance chain does not establish scientific validity.

Record reusable process problems found while writing formal-mathematics artifacts in /L7/process-lessons.md.
