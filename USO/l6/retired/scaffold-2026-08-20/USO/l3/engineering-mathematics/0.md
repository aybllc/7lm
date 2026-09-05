# L3 / engineering-mathematics - Finite Results and Their Conditions

This directory holds finite work: approximation, measurement, calibration, numerical
method, finite representation, units, resolution, uncertainty, error, tolerance,
rounding, and the reproducibility conditions that travel with each result. Every record
here names the exact L2 object it approximates and states the conditions under which
the approximation is claimed to hold.

## What a result record must carry

| Field | Required content |
| --- | --- |
| Result name | A stable name that does not assert more than the result establishes. |
| Approximated L2 object | The named exact L2 artifact, with the L0 interpretation and L1 declaration that artifact names. |
| Conditions of validity | The stated conditions under which the approximation is asserted to hold, and where it is known to fail. |
| Method | The numerical method or measurement procedure, including its own stated assumptions. |
| Finite representation | Number format, representable range, rounding rule, and behaviour on overflow or underflow. |
| Units and resolution | The unit of every reported quantity and the resolution at which it is reported. |
| Calibration | The calibration as /uso/l0/definitions/0.md defines it, recorded with its date, conditions, and the authority the assignment is referred to |
| Error | Deviation from the approximated L2 object, where that deviation can be bounded or estimated. |
| Uncertainty | The measured or estimated dispersion, with how it was obtained. |
| Tolerance | The separately stated allowance the result is required to fall within, if any. |
| Reproducibility conditions | Inputs, environment, method version, and what a failure of this result would look like. |

## Manual work

1. Name the exact L2 object first; if no L2 object exists yet, the work belongs in L2 before it belongs here.
2. State the conditions of validity as conditions, including the regime where the approximation is known to break down.
3. Record the method with enough detail that someone else can run it, including the assumptions the method itself makes.
4. Record the finite representation explicitly: format, range, rounding rule, and what happens at the edges of that range.
5. Give every reported quantity a unit and a resolution, and keep the resolution honest to the method rather than to the display.
6. A numeral received with trailing zeros carries a resolution claim in its written form: record the received form exactly, record separately whether the source's stated method supports that resolution, and where it does not, record the discrepancy rather than re-rounding or re-formatting the value.
7. Record how the method or instrument encodes absence — sentinel value, blank field, or status flag — and check it against the non-value markers of the named L1 declaration; a sentinel that is also a representable value of the domain is reported to L1 as a defect, never silently converted here.
8. Enter error, uncertainty, and tolerance as three separate fields, and leave a field empty rather than filling it from one of the others.
9. Record the reproducibility conditions with the result, including a written description of what a failure of this result would look like.
10. Compare the finite result against the L2 object only under the stated conditions, and report a mismatch to L2 rather than adjusting the result to fit.
11. Route anything whose owner or layer is not yet adjudicated back through L7 ingress instead of treating placement here as settled.

## Three statements that must not be blurred

- A finite result is not the exact L2 object. It is a separate artifact with its own conditions and its own failure modes, and it inherits none of the L2 object's guarantees.
- A similarity measure is not semantic authority. Two results that agree closely are two results that agree closely; agreement does not make either one controlling over the other's meaning, and it does not establish identity or equivalence.
- A stated tolerance is not a measured uncertainty. A tolerance is a requirement someone set; an uncertainty is something obtained from the measurement or the method. Reporting one in place of the other misstates what is known.

## Terms used here

| Term | Working definition | Basis |
| --- | --- | --- |
| approximation | A finite artifact standing in for a named exact L2 object under stated conditions. | Project rule |
| numerical method | A finite procedure that produces an approximation, carrying its own assumptions. | Project working use |
| finite representation | The format, range, and rounding rule under which a value is actually held. | Project working use |
| resolution | The smallest distinction the method or instrument actually supports. | Project working use |
| error | Deviation of the finite result from the approximated L2 object. | Project working use |
| uncertainty | Measured or estimated dispersion of a result, with its method of estimation stated. | Project working use |
| tolerance | A separately stated allowance the result is required to fall within. | Project rule |
| definitional uncertainty | Uncertainty arising from the finite amount of detail in the definition of what is measured. | Adapted from JCGM 200:2012 (VIM) |
| reproducibility conditions | Inputs, environment, method, and stated failure appearance, recorded with the result. | Project rule |

`validation` and `failure` are owned at /uso/l0/definitions/0.md and are named, not restated,
here; this table holds only terms controlling inside L3.

## Source anchors

Quoted to anchor terminology only. No source below evaluates, endorses, or validates this
layer architecture, this directory, or any result recorded in it.

- JCGM 200:2012 (VIM), Entry 2.45 validation, printed page 31: "verification, where the specified requirements are adequate for an intended use"
- JCGM 200:2012 (VIM), Entry 2.44 verification, NOTE 5, printed page 31: "Verification should not be confused with calibration. Not every verification is a validation."
- JCGM 200:2012 (VIM), 2.27 'definitional uncertainty': "component of measurement uncertainty resulting from the finite amount of detail in the definition of a measurand"; NOTE 2: "Any change in the descriptive detail leads to another definitional uncertainty."
- JCGM 200:2012 (VIM), Entry 1.2 kind of quantity, NOTE 2: "Quantities of the same kind within a given system of quantities have the same quantity dimension. However, quantities of the same dimension are not necessarily of the same kind."
- ISO/IEC/IEEE 24765:2017(E), 3.4500 'validation', definition 1, printed page 499: "1. confirmation, through the provision of objective evidence, that the requirements for a specific intended use or application have been fulfilled"
- ISO/IEC/IEEE 24765:2017(E), 3.1560 'failure', definition 1, printed page 178: "1. termination of the ability of a system to perform a required function or its inability to perform within previously specified limits; an externally visible deviation from the system's specification"

## Boundary

- No exact mathematics is created here. New objects, operators, axioms, and proofs belong to L2; this directory approximates them and reports back to them.
- L3 may not repair a defective L2 object, an unresolved L1 declaration, or an unresolved L0 meaning. Exit to the owning layer and correct it there.
- Matching units does not mean matching quantities, and matching numbers does not mean matching meaning.
- An unrun result is not a result. If the method has not been executed under the recorded conditions, say so in the record.
- Reproducing a result under its recorded conditions establishes reproducibility, not scientific validity; custody, an exact hash, and clean provenance establish neither.
- A choice of method made for one composition or application is not universal supersession of another live method.

Record reusable process problems found while writing engineering-mathematics records in /L7/process-lessons.md.
