# L0 - Semantic Formulas

A formula admitted here exists to state a meaning, not to compute a result. Symbols are shorthand
for words that were written first, and a formula is admitted only after its natural-language
reading, its symbol glosses, and its falsification condition are on the page. Every formula here
names the /uso/l0/semantics interpretation it depends on, by source, version, and scope: the same
symbols under a different interpretation are a different formula, not the same one reused.

## Required before any symbol is written

| Required field | What it must state | Basis | Source or locator |
| --- | --- | --- | --- |
| Reading | The whole statement as one prose sentence containing no symbols. | Project rule | - |
| Symbol gloss | For each symbol, the word or phrase it abbreviates, written out. | Project rule | - |
| Range | What the symbol ranges over: the class or value class its admitted values are drawn from. | Adapted from [source] | ISO/IEC/IEEE 31320-2:2012, 3.1.202 "value class": "A kind of class that represents instances that are pure values. The constituent instances of a value class do not come and go and cannot change state." |
| Kind | The kind the quantity belongs to, stated explicitly, since sameness of dimension is not sameness of kind. | Adapted from [source] | JCGM 200:2012 (VIM), 1.2 Note 2: "Quantities of the same kind within a given system of quantities have the same quantity dimension. However, quantities of the same dimension are not necessarily of the same kind." |
| Units | The unit, or the explicit word "dimensionless". A bare number with no unit statement is not admitted. | Project rule | - |
| Falsification condition | What state of affairs, or what value, would make the statement false, and under what stated conditions the statement is meant to hold. | Adapted from [source] | ISO/IEC/IEEE 24765:2017, 3.575 def. 2 "claim": "true‐false statement about the limitations on the values of an unambiguously defined property — called the claim’s property — and limitations on the uncertainty of the property’s values falling within these limitations during the claim’s duration of applicability under stated conditions" |
| Definitional detail | The finite detail the definition carries, and what a change in that detail would change. | Adapted from [source] | JCGM 200:2012 (VIM), 2.27 'definitional uncertainty': "component of measurement uncertainty resulting from the finite amount of detail in the definition of a measurand"; NOTE 2: "Any change in the descriptive detail leads to another definitional uncertainty." |
| Named interpretation | The exact /uso/l0/semantics record relied on: source, version, scope. | Project rule | - |
| Status | Definition status of the formula statement, its scope, its layer owner, and its live alternatives. | Project rule | - |

A formula that satisfies every field is a well-stated meaning, not a verified one. ISO/IEC/IEEE
24765:2017, 3.575 Note 1, is explicit that stating a claim is not asserting its truth: "Claims
usually relate to specified versions of a product. The statement of a claim does not mean that the
only possible intent or desire is to show it is true."

## Manual work

1. Write the prose reading first, with no symbols in it. If the prose reading is unclear, the
   formula will not fix it; return to /uso/l0/semantics and settle the interpretation.
2. Gloss every symbol, including indices, subscripts, and any symbol you consider obvious. An
   unglossed symbol is an unresolved meaning wearing a letter.
3. State the range, kind, and units of each symbol, or state "dimensionless" in words. Do not leave
   units to be inferred from context or from a downstream calculation.
4. State the falsification condition and the conditions of applicability in the same paragraph, so
   a reader can see what the statement forbids as well as what it allows.
5. Name the interpretation each symbol depends on, by source, version, and scope. Where a symbol
   depends on two interpretations that differ materially, record both and mark the formula
   provisional rather than choosing one here.
6. Check the formula for symbol collisions against the other records in this directory: one letter
   used for two concepts is a defect, and renaming one is a lexical change to be recorded as such.
7. Record definition status, scope, owner, and live alternatives, then route the formula to the
   lowest layer able to state it without importing an unresolved assumption from above.
8. When an interpretation the formula names is superseded, revisit the formula, record the
   successor relation, and keep the earlier statement with its scope intact.

## Keep out

- No derivations. Deriving one statement from another is L2 work.
- No proofs, no theorems, no consistency arguments. L2 formal-mathematics owns those, and a proof
  under one interpretation never selects that interpretation.
- No executable code, no scripts, no numerical evaluation.
- No approximations, series truncations, limits taken for convenience, error budgets, or fitted
  constants. L3 engineering-mathematics owns those, together with their stated tolerances.
- No formula without a named L0 interpretation, and no formula whose symbols are glossed only by
  the surrounding equations.
- No borrowing a formula from a source that used it in a different scope. That is a new claim about
  the formula, not a citation of it, and it belongs in /uso/l0/prior-art with its limits recorded.
- No treating formal expression as validation. ISO/IEC/IEEE 31320-2:2012, 3.1.63, calls
  formalization "The precise description of the semantics of a language in terms of a formal
  language such as first order logic"; precision of description is not evidence of truth.

Reusable process problems discovered while doing this work belong in /L7/process-lessons.md, not in
this directory.
