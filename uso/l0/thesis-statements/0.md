# L0/thesis-statements - the end claims, in plain language

This directory holds the end claims of the corpus: what is actually being asserted, written so that a
reader outside the project can understand it without reading anything else. Claims here may be
proposed, contested, or owner-designated canonical. The text is plain language only - the support,
the mathematics, and the application live in other layers and are reached by naming this claim, not
by restating it.

## What one entry records

| Field | What to record | Rule |
| --- | --- | --- |
| claim | the assertion in one or two plain sentences, with no hedging and no argument | if it cannot be stated plainly, it is not ready to be an entry |
| owner | the party entitled to designate the claim's standing | one named owner; "the project" is not an owner |
| scope | the conditions, domain, and version under which the claim is asserted | a claim without a stated scope is provisional, whatever else is recorded |
| epistemic status | the status carried in ../epistemic/, referenced not duplicated | never inferred from the owner's authority or from the claim's age |
| controlling terms | every term whose L0 meaning the claim depends on, each pointing to its entry | an unnamed controlling term is an unfinished entry |
| inclusions | the cases the claim is meant to cover | state cases, not examples of how well it works |
| exclusions | the cases the claim is explicitly not about | silence is not an exclusion; write them out |
| minimum support | the least that would have to hold for the claim to stand | stated before support is sought, not after |
| contradiction conditions | what observation, result, or counter-case would defeat the claim | if nothing could defeat it, say so and mark the entry as not yet a claim |

Keep one file per claim, and keep the fields in this order so entries can be compared by reading down
the same column.

## Canonical is a designation, not a compliment

Do not call a claim canonical unless its OWNER has designated it as controlling for a STATED scope.
canonical means owner-designated as controlling for that scope and version. It does not mean proven,
validated, or universally true, and it does not raise the claim's epistemic status by one step. Until
an owner designates it, the entry is proposed or contested, and it is recorded that way. Two external
distinctions are worth keeping in view while writing entries: "Claims usually relate to specified
versions of a product. The statement of a claim does not mean that the only possible intent or desire
is to show it is true." (ISO/IEC/IEEE 24765:2017(E), Clause 3.575 'claim', Note 1 to entry, printed
page 69); and on scope, "The scope of each concept defined has been chosen to provide a definition
that is suitable for general application. In those circumstances where a restricted application is
concerned, a more specific definition might be needed." (ISO/IEC/IEEE 24765:2017(E), Clause 1.1
General, printed page 1). Both are cited for the distinction only; neither speaks to this corpus.

## Manual work

1. Write the claim in plain language first, before consulting any support, so the wording is not bent
   to fit what happens to be available.
2. Fill in owner and scope next; if either is unknown, stop and leave the entry provisional rather
   than guessing.
3. List every controlling term and link each to its entry under ../definitions/ or ../semantics/; add
   any term that is missing there before continuing.
4. Write inclusions and exclusions as separate lists, and make the exclusions specific enough that
   someone could misapply the claim only by ignoring them.
5. State the minimum support and the contradiction conditions in the same sitting, and check that
   they are not two phrasings of the same thing.
6. Reference the epistemic status held in ../epistemic/ rather than copying it, so the two cannot
   drift apart.
7. Mark the entry canonical only on the owner's designation, and record the scope and version that
   designation covers.
8. When a claim changes, keep the earlier entry and record the successor relation; do not overwrite,
   and do not move the earlier entry to L6 history unless it was actually displaced.

## Keep out

- No proofs and no derivations. The reasoning belongs to L2, which names this claim.
- No equations, no notation, and no symbol definitions; if the claim cannot survive in words, it is
  not an end claim yet.
- No literature arguments, no source comparison, and no positioning against other work; sources
  bearing on meaning go to ../prior-art/, and standing goes to ../epistemic/.
- No implementation, no code, no results, and no performance figures; those belong to L4.
- No rhetoric - no significance, novelty, promise, or importance language, and no framing intended to
  make the claim harder to refuse.
- No status inflation. A contested claim stays contested until its owner rules, and a live
  alternative stays live even when a composition did not select it.
- No adjudication here. This directory states claims; ratification is the owner's act and is recorded
  where governance is recorded.

Reusable process problems - anything that will recur across claims rather than belong to one entry -
go to /L7/process-lessons.md.
