# L1 / state-space - Admissible State Declarations

This directory holds state-space declarations. A declaration says which state variables
exist, what values they may take, over what domains, under what structural constraints and
invariants, with what exclusions and boundary cases - all under one named L0
interpretation. One file per declaration. Nothing here decides what a term means; that was
decided at L0 and is named, not restated.

## What a declaration must contain

| Field | Required content |
| --- | --- |
| Declaration name | A stable name that does not encode the interpretation's outcome. |
| Selected L0 interpretation | The named L0 artifact, its definition status, and the scope it is controlling for. |
| State variables | Each variable with its domain, its type, and whether a value is required. |
| Structural constraints | Conditions relating two or more variables inside a single admissible state. |
| Invariants | Conditions that must hold of every state the declaration admits. |
| Exclusions | Values or states removed from admissibility, each with its recorded reason. |
| Boundary cases | Behaviour at the edge of each domain, including empty, minimal, and maximal cases. |
| Non-value markers | How missing, undefined, and inapplicable are represented, separately from each other. |
| Status | Provisional or adjudicated, with the candidate owner or the adjudicated layer owner. |
| Live alternatives | Named sibling declarations that select a different live L0 interpretation. |

## Manual work

1. Name the L0 interpretation this declaration selects before writing anything else; a declaration with no named interpretation does not belong in this directory.
2. List the admissible state variables, giving each a domain and a type, and say for each whether a value is required.
3. State the structural constraints and invariants as conditions over whole states, not as commentary on individual variables.
4. State the exclusions and the boundary cases explicitly; an unstated edge is an unresolved edge, not an admissible one.
5. Declare missing, undefined, and inapplicable as three separate markers, and check that none of them is encoded as an ordinary value of any domain.
6. If a second live L0 interpretation supports a different declaration, write that declaration as its own file and list each as a live alternative of the other.
7. Record any contradiction, tension, or inconsistency between the named L0 interpretations as an L0 matter, and keep every affected declaration current until L0 adjudication happens.
8. Re-check each declaration whenever a named L0 interpretation changes; a changed interpretation makes the declaration stale, not wrong.
9. When a declaration is replaced, write a successor declaration, preserve the earlier one, and record the successor relation between them.

## Terms used here

| Term | Working definition | Basis |
| --- | --- | --- |
| state variable | A named place in a declaration that may hold one value drawn from a stated domain. | Project working use |
| structural constraint | A condition relating two or more state variables inside a single admissible state. | Project rule |
| invariant | A condition that must hold of every state the declaration admits. | Project rule |
| exclusion | A value or state the declaration removes from admissibility, with a recorded reason. | Project rule |
| boundary case | An admissible state at the edge of a declared domain, stated explicitly rather than left implied. | Project working use |
| missing | The value exists in principle but is not present in this state. | Project rule |
| undefined | The variable has no value here because this state lies outside the declared domain. | Project rule |
| inapplicable | The variable does not apply to this state at all. | Project rule |

`domain`, `identity`, `type`, and `live alternative` are owned at /uso/l0/definitions/0.md and are
named, not restated, here; this table holds only terms controlling inside L1.

## Source anchors

Quoted to anchor terminology only. No source below evaluates, endorses, or validates this
layer architecture, this directory, or any declaration written in it. The PROV-DM quotations
below are reproduced verbatim (the source's section-permalink glyph removed).

- ISO/IEC/IEEE 31320-2:2012(E), 3.1.52, page 13: "domain: Syn: value class."
- ISO/IEC/IEEE 31320-2:2012(E), 3.1.202, page 23: "value class: A kind of class that represents instances that are pure values. The constituent instances of a value class do not come and go and cannot change state."
- ISO/IEC/IEEE 31320-2:2012(E), 3.1.80, page 15: "identity: The inherent property of an instance that distinguishes it from all other instances. Identity is intrinsic to the instance and independent of the instance's property values or the classes to which the instance belongs."
- ISO/IEC/IEEE 24765:2017(E), 3.4404 'type', definition 2, printed page 487: "2. of an <X>, a predicate characterizing a collection of <X>s"
- ISO/IEC 2382:2015 (corrected version), entry "scope / scope of a declaration": "that portion of a program within which a declaration is valid"
- PROV-DM (W3C Recommendation 30 April 2013), Section 5.5.2 Alternate: "Two alternate entities present aspects of the same thing. These aspects may be the same or different, and the alternate entities may or may not overlap in time."
- PROV-DM (W3C Recommendation 30 April 2013), Section 5.2.2 Revision: "A revision is a derivation for which the resulting entity is a revised version of some original."

## Boundary

- Do not merge two declarations that depend on different live L0 interpretations, and do not silently pick one of them. Non-selection is not rejection, failure, recall, or supersession, and a non-selected live alternative stays current here rather than going to L6 history.
- Do not repair an unresolved L0 meaning by declaring around it. A declaration may say the meaning is unresolved; it may not settle it.
- Never encode missing, undefined, or inapplicable as an ordinary value of a domain, and never collapse any of the three into another.
- No operators, axioms, derivations, proofs, or counterexamples here; those are L2. No finite representation, resolution, or uncertainty; those are L3. No application-specific selection; that is L4 or an L7 composition. A declaration may name the quantity kind and unit that fix a domain, by naming the L0 interpretation that carries them; what is excluded is the finite side of a unit.
- Similarity between two declarations establishes neither identity nor equivalence, and a semantic mapping drawn between them is not semantic authority over either.
- A declaration's internal consistency, its custody in this repository, or its provenance does not make it scientifically valid.

Record reusable process problems found while writing state-space declarations in /L7/process-lessons.md.
