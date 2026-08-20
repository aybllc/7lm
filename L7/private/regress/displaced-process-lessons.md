# Process lessons

This file is the running record of process decisions and process problems recorded as this
scaffold is drafted and worked by hand. It exists so a decision made once does not have to be
rediscovered, and so anyone who later proposes tooling can see which behaviours the scaffold
depends on. It is a log, not a gate: nothing here approves work, nothing here has to be filled
in before work proceeds, and nothing here is a second ledger of the corpus.

## Format

One lesson per line, four fields, in this order:

```
YYYY-MM-DD - path or layer - what happened - what a future tool must preserve
```

Append lessons; do not rewrite earlier ones. Do not use " - " inside a field, because it is the
field separator. If a lesson needs more than one line, it is not a process lesson yet, and belongs
in the artifact it concerns.

## Lessons

```
2026-08-20 - /L7/intake - intake was placed at L7 while uso/l6 was reserved for history and provenance, so new material enters through L7 and never through L6 - a future tool must send every incoming object to /L7/intake first and must never accept uso/l6 as an entry point
2026-08-20 - /L7/intake - early intake classification was defined as provisional, letting one source bear on several artifacts and one artifact carry several candidate owners - a future tool must keep intake classification provisional and must allow overlapping candidate owners instead of forcing a single label
2026-08-20 - uso/l0 to uso/l4 - routing was separated from copying, so a source object is stated and named where it is used rather than pushed unchanged through every layer - a future tool must not propagate a source object layer by layer as if each layer needed its own copy
2026-08-20 - repository root - internal directory guides were standardized on 0.md while the repository root keeps README.md - a future tool must preserve that split and must not rename 0.md files or add a second guide per directory
2026-08-20 - repository root - the scaffold object list was fixed, and anything not on it was made conditional on prior naming, justification, and approval - a future tool must require prior naming, justification, and approval before creating any unlisted object
2026-08-20 - uso/l0/definitions - term, label, concept, definition, terminology, vocabulary, controlled vocabulary, taxonomy, thesaurus, ontology, type, syntax, semantics, semantic mapping, and epistemic status were kept as separate entries - a future tool must not treat these as interchangeable or collapse them into one field
2026-08-20 - uso/l0/epistemic - epistemic status was attached to claims and definition status was attached to definitions, on two separate axes - a future tool must keep the two axes separate and must never write an epistemic status onto a definition or a definition status onto a claim
2026-08-20 - /L7/PINNED - canonical was defined as owner designation for a stated scope and version, not as proven or universally true - a future tool must require a named owner and a declared scope before recording canonical, and must not infer canonical from use, age, or frequency
2026-08-20 - uso/l0/semantics - semantic mapping and similarity were kept separate from identity and semantic authority - a future tool must not promote a mapping, a similarity measure, or an early merge to identity, equivalence, or authority
2026-08-20 - uso/l0 to uso/l3 - contradiction, tension, and inconsistency were recorded as visible open items with distinct dispositions rather than reconciled in place - a future tool must keep contradictions visible until adjudication and must not silently harmonize, repair, or drop them
2026-08-20 - uso/l2/formal-mathematics - formal consistency under one interpretation was held not to select that interpretation - a future tool must not treat a consistency check, a type check, or a proof of non-contradiction as adjudication of semantics
2026-08-20 - /L7/PINNED - only the fixed binding was placed in PINNED while the authority content stayed in its owning repository - a future tool must store bindings only and must never copy, paraphrase, or route authority content into uso/
2026-08-20 - /L7/PINNED - defective owner artifacts were made correctable only in the owning repository, followed by admission of a new exact binding - a future tool must send owner defects out of the consumer USO and must preserve the earlier binding and the successor relation
2026-08-20 - /L7/PINNED - several pins were allowed to be active at once without ranking, merging, harmonizing, or superseding one another - a future tool must not derive a combined authority from coexisting pins and must not read disagreement between independently scoped authorities as an owner defect
2026-08-20 - uso/l6/provenance - provenance records and integrity identifiers were kept separate from scientific validity - a future tool must not infer validity from custody, hash match, authority, internal consistency, or provenance
2026-08-20 - uso/l0 to uso/l3 - layers L0 through L3 were kept declarative and manual, with no generation, derivation, or automation - a future tool must not write, derive, or rewrite L0-L3 artifacts on its own
2026-08-20 - uso/l4 - L4 selections were bounded to the present application and implementation boundary - a future tool must treat an L4 selection as application-scoped and must never read it as universal supersession
2026-08-20 - /L7/compositions - live alternatives that a composition did not select were left current in their owning layers - a future tool must not move an unselected live alternative into uso/l6/history, because non-selection is not rejection, recall, failure, or supersession
2026-08-20 - uso/l0/definitions - every change to a controlling technical use was tied to an update of the definitions list in the same pass - a future tool must update the definitions list whenever a controlling term, label, or sense changes, and must not leave the list trailing the corpus
2026-08-20 - repository root - adjudication of meaning, equivalence, contradiction, ownership, and supersession was left entirely to a human - a future tool must not silently adjudicate any of these and must surface the open question instead of resolving it
```

## Status of this file

Every entry above records a design decision taken while this scaffold was drafted on 2026-08-20,
not an observation of the scaffold in operation. No artifact has been worked through the cycle
yet. This file is evidence only. It is NOT authorization to automate, and no entry here approves
a script, hook, workflow, schema, or generated artifact. Automation remains an unlisted object:
it requires prior naming, justification, and approval before anything is built.
