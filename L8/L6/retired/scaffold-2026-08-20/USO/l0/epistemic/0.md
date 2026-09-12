# L0/epistemic - what kind of support each claim has

This directory records the standing of L0 material: what each item is, what supports it, what would
contradict it, and what is still open. It is a register, not an argument. Nothing here is written to
persuade; it is written so that a reader can tell, without reading the rest of the corpus, whether an
item is a definition, a guess, a derivation, a measurement, or a live disagreement.

## Nine registers, kept separate

| Register | What it holds | What it must never hold |
| --- | --- | --- |
| definitions | a pointer to the definition's row in ../definitions/, naming its owner and the scope it is stated for | the truth of any claim that uses the term, and the definition status itself, which the row in ../definitions/ carries |
| conjectures | proposed statements with no established support yet, stated so they could fail | statements already carried as results elsewhere |
| derived results | statements obtained from stated premises, with the premises named | the premises' own justification |
| empirical claims | statements answerable to measurement or observation, with the conditions named | derivations dressed as observations |
| contested claims | claims a named party disputes, with the dispute and the disputer recorded | the adjudication outcome, which belongs to the owner |
| contradictions | two statements that cannot both hold under one interpretation at one scope | apparent clashes across different scopes |
| inconsistencies | a set of statements that cannot be jointly satisfied under a stated interpretation, with the set and the interpretation named | a verdict on any single member of the set |
| tensions | statements that pull against each other without a demonstrated impossibility | anything already shown to be a contradiction |
| open questions | what is not settled, and what would settle it | speculation presented as a pending result |

Do not merge these registers to tidy the layer. A conjecture that is filed as a derived result, or a
tension filed as a contradiction, is a semantic loss that later layers cannot detect.

An instrument indication and the quantity it is taken to indicate are two claims, not one: record
what the device output as one empirical claim, record what the world is taken to have been as
another, and record the inference between them as a named dependency with its own support.

## Three different things, on purpose

| Axis | What it establishes | What it does NOT establish |
| --- | --- | --- |
| semantic authority | who gets to say what a term means, for which scope and version | that any statement using the term is true |
| internal support | that an item follows from, or is consistent with, this corpus and its stated premises | that the premises hold outside this corpus |
| independent external validation | that an outside party, on outside evidence, confirmed the item for a stated use | that the item holds outside the use that was validated |

The separation matters because the three are routinely collapsed, and collapsing them manufactures
confidence that no one earned. An owner may hold semantic authority over a term and still be wrong
about every claim made with it. An item may be perfectly supported internally and never have been
checked against anything outside. Two standing distinctions make the same point from the outside:
"A system could be verified to meet the stated requirements, yet be unsuitable for operation by the
actual users." (ISO/IEC/IEEE 24765:2017(E), Clause 3.4538 'verification', Note 1 to entry, printed
page 503), and "Verification should not be confused with calibration. Not every verification is a
validation." (JCGM 200:2012, VIM 3rd edition, Entry 2.44 verification, NOTE 5, printed page 31).
Neither source speaks to this corpus or its layer arrangement; they are cited for the distinction
only.

## Two axes, not one

A claim carries an EPISTEMIC STATUS: what kind of support it has and what would defeat it. A
definition carries a DEFINITION STATUS: how settled the definition is, for which scope and version,
and by whose designation. These are different axes and are never substituted for one another. A
canonical definition does not make a claim verified. A well-supported claim does not settle the
definition status of the terms it uses. Record both, separately, and never infer one from the other.

## What does not establish validity

Repository custody, an exact hash, authority, internal consistency, and provenance do not by
themselves establish scientific validity. Each answers a real but different question - where the
object is, that it is unaltered, who is entitled to speak for it, that it does not conflict with
itself, and where it came from. None of them is evidence that the claim is true of the world. Record
them where they belong and do not let them appear in the support column of a claim.

## Manual work

1. For each L0 item, write the register it belongs to before writing anything about its content.
2. State the claim in one sentence, then state separately what would have to be observed or shown for
   it to fail.
3. Record semantic authority, internal support, and independent external validation in three distinct
   fields; leave a field empty rather than filling it from a neighbour.
4. Give every claim an epistemic status and every definition a definition status, and check that
   neither was copied from the other.
5. When two items clash, decide first whether it is a contradiction, a tension, or an inconsistency,
   and record the scope and interpretation under which you decided.
6. Name the owner who can adjudicate each contested claim, and leave the outcome blank until that
   owner rules.
7. Re-check the support fields for custody, hash, authority, internal consistency, or provenance
   masquerading as evidence, and move them out.
8. Log every open question with the specific check, source, or measurement that would close it.

## Boundary

- Contradiction, tension, and inconsistency are different dispositions and are recorded differently:
  a contradiction is a demonstrated impossibility under one interpretation at one scope; a tension is
  an unresolved pull between items with no impossibility shown; an inconsistency is a set of
  statements that cannot be jointly satisfied under a stated interpretation — a property of the
  set, not a verdict on any single member (see /uso/l0/definitions/0.md).
- Do not silently repair, reinterpret, or harmonize a clash to make the register look clean.
- Absence of contradiction is not support, similarity is not validation, and compatibility is not
  proof.
- This corpus cannot validate itself; internal support is recorded as internal support and never
  reported as external validation.
- Do not adjudicate here. This directory records standing; ratification and governance belong to the
  owner and to L5.

Reusable process problems - anything that will recur across claims rather than belong to one entry -
go to /L7/process-lessons.md.
