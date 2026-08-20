# L6 - Research History and Provenance

L6 holds the scientific record of the corpus: where material came from, what displaced what, and
why. It is not the file history. Git records which bytes changed in which files, when, and by whom;
L6 records the origin of material, the disposition of states that are no longer current, and the
reasoning behind each displacement. A clean file history can accompany an empty scientific record,
and the two must never be treated as the same thing.

Children:

- history/ - preserves superseded, rejected, failed, and recalled states, plus states kept because
  later material cannot be read without them; the four dispositions — rejected, recalled, failed,
  superseded — are kept distinct, and historical significance is a retention reason rather than a
  disposition.
- provenance/ - records recoverable source identity, issuer, exact version, locator, declared scope,
  and local use; the local table is provenance/source-ledger.md.

## Manual work

1. Write the L6 record at the moment of displacement, while the reason is still known. A record
   reconstructed later is marked as reconstructed.
2. Record why, not only what: the reason a state stopped being current is the part git cannot hold.
3. Name the disposition exactly. Contradiction, tension, inconsistency, rejection, recall, failure,
   and supersession are different and are never collapsed into one word.
4. Record the successor relation where one exists, and state plainly when none does.
5. Record every source in provenance/source-ledger.md at the time it is first used, not at
   publication time.
6. Leave live alternatives alone. Non-selection by one application or composition is not a
   disposition and produces no L6 entry.
7. When a git operation and an L6 record disagree, treat git as evidence about files and L6 as the
   claim about material, and reconcile the two explicitly rather than silently.

## Boundary

- L6 is not an intake point. New material - sources, authority artifacts, objects, candidate
  artifacts - enters at L7 ingress and is routed from there.
- L6 does not adjudicate meaning, own definitions, or assign layer ownership. It records what was
  decided elsewhere and by whom.
- Provenance and history establish audit and retrieval. Neither establishes scientific validity.
- Do not delete a displaced state to tidy the record; displacement is recorded, not erased.
- Do not rewrite an existing L6 entry to agree with a later decision; add the later entry and the
  successor relation.

When a difficulty here is about the process rather than about a particular record, record it in
/L7/process-lessons.md.
