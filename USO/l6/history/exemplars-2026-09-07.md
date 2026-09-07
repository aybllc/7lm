# The exemplars as they stood on 7 September 2026

**Object:** A dated state of the two exemplar repositories, pulled out of the specification so that the specification states the architecture and not the current condition of any repository.
**Path:** `USO/l6/history/exemplars-2026-09-07.md` · **Layer:** L6 — LIBRARY · **Owner:** `USO/l6/history/`

This is the section "Exemplars as instantiated" as it stood in the specification's version of 7 September 2026, carried here word for word when that version was reduced to the layer contracts. It describes `aybllc/autonomous` and `aybllc/auditonomous` on 7 September 2026, including what was not yet as the specification stated. It is a record of a state, not a rule: what those repositories hold now is documented in their own sheets and in their own records at `l6/history/`.

The specification keeps the claim that outlived the snapshot: architecture and implementation status are separate claims, and an exemplar's layout does not control the architecture.

---

Reference implementations: https://github.com/aybllc/autonomous and https://github.com/aybllc/auditonomous, with the scaffold at https://github.com/aybllc/7lm and the curated-source archive at https://github.com/aybllc/l6.

**[Clarification]** Architecture and implementation status are separate claims. What follows documents the two exemplars as they stand, including what is not yet as this specification states. Their layouts do not control the architecture.

**What both exemplars carry**

- The canonical tree under README.md, L7/, and the interior container, which both still name USO/ pending the rename pass. Every directory has its 0.md, headed by its path. No directory metadata, no automation in the layout; the one CI check at .github/workflows/integrity.yml, and the same root in both.
- One locally authored L0 definition each. Autonomous owns l0/semantics/definitions/AUTONOMOUS.md, a plural entry of eleven codified definitions A1–A11 carried in verbatim with their issuing bodies' ownership tags. Auditonomous owns l0/semantics/definitions/AUDITONOMOUS_DEFINITION.md, the local delta over the bound Autonomous root.
- The binding of the Autonomous definition at Auditonomous's L7/peering/public/ingress/peer-1/object-1/, reference-only, NO EDIT and NO DELETE, under the owner's rule that Auditonomous gets the definitions of autonomous from Autonomous and nowhere else. Autonomous exposes the definition at its L7/peering/public/egress/peer-1/.
- Curated sources served by pointer from aybllc/l6, bound at each repository's L7/peering/private/ingress/peer-1/; one ledger row per source at L7/provenance/sources/LEDGER.md; no source file in either repository.
- Copyright in one place, L7/governance/copyright/, with licensing/ and restrictions/ pointing to it.
- l5/research/review/ as the catch-all and l5/research/lanes/ as the working position. The queue that preceded them at the repository roots, orphan, foster, results, delete, with its access rules for sessions, is retired at l6/retired/layout-2026-09-06/ in each repository.
- The records at l6/history/ in each repository, carrying the owner's words verbatim and every move, retirement, deletion, and binding.
- No rule in either tree about what a session or any other intelligence may touch. The repository file that would carry such rules is held off.
- A README that is a start page: the subject, the reading order, the root, and where the prior README is. The evidence rules of Autonomous and the status and label discipline of Auditonomous stand verbatim at l5/research/review/.

**Autonomous** (aybllc/autonomous)

Face. Public ingress peer-1 to peer-9: the issuing bodies whose clauses are bound into the definition, ISO/TC 299, ISO/IEC JTC 1/SC 42, ISO/IEC JTC 1/SC 7, IEEE, NIST, the European Union, US DoD, EASA, and ETSI, one object per bound clause. Public egress peer-1: aybllc/auditonomous, the definition as exposed. Private ingress peer-1 aybllc/l6; peer-2 aybllc/eb-stack with abba-01/ebios; peer-3 aybllc/auditonomous, the coinage, referenced and not adopted; peer-4 the principal's intake corpus. Private egress: none. Provenance: the pointer ledger into l6 and a 450-entry capture register. Publications: a binder; nothing released.

Interior. l6: the master ledger, five forensic reconstructions, the two records, two retired layouts, and four definition error records. l5: six lanes; the reviews, audits, and adjudications; seven findings. l4: the manuscript placeholder, the autonomy scale (an L4 object by the owner's ruling), and one deep-research run. l3: two engineering-mathematics notes. l2: an empty formulas ledger. l1: empty, its dimensions fixed by content inside four L5 findings. l0: the definition with its companions and a universality scope statement.

Not yet as stated. The interior is named USO/, not L8/. The catch-all holds material that belongs to other objects: Autonomous Theory, one work and not the definition of autonomous, whose home the owner has not named; a template of the Auditonomous definition; and the owner's notes on memory consolidation with conserved uncertainty. Each leaves on the owner's word. The provenance rows for the bound issuing bodies are not yet ledgered.

**Auditonomous** (aybllc/auditonomous)

Face. Public ingress peer-1: aybllc/autonomous, the definition of autonomous, bound at commit 0504961. Private ingress peer-1 aybllc/l6; peer-2 aybllc/eb-audit; peer-3 abba-01/ebios with the Martin 2026 manuscript. Private egress peer-1: the closed transfer of the source corpus to l6; peer-2: the pending transfer of the Third Power Corpus to aybllc/ncf-research, whose files wait at object-1. Public egress: nothing released. Provenance: 62 pointer rows into l6, the staging records about those sources, and one session-provenance record at lineage/. Publications: presentation rules and an empty press-kit checklist.

Interior. l6: the master index, three session ledgers, the two records, two retired layouts. l5: two lanes; two reviews and the status ladder carried verbatim; three findings. l4: drafts, chat transcripts, a session record, three requirements extractions, and one deep-research run with its exports. l3: a proposal and an external-priors note. l2: an empty formulas ledger. l1: the auditon envelope, the substitutability states, and the requirements partition. l0: the one locally authored definition; the other rails empty.

Not yet as stated. The interior is named USO/, not L8/. The binding of the Autonomous definition names the path the peer used before its own 7LM layout, research/definitions/AUTONOMOUS.md at 0504961; the same object now stands at the peer's l0/semantics/definitions/AUTONOMOUS.md, and rebinding to a current version is the owner's act. The binding record says three files still take a definition of autonomous from somewhere other than the binding. The catch-all holds two Autonomous Theory files that leave once that work's home is named. The l0 epistemic rail is empty; its vocabulary stands at L5 as review status.

**What the exemplars show**

- A second work inside a repository is not the object. Autonomous Theory appeared in both exemplars and is neither's definition; the catch-all holds it until the owner names its home, and the architecture's place for a second work is a repository of its own, met here by peering. Whether it takes that route is the owner's call.
- Position is state. Three motions and no metadata carried the two repositories from a root queue to the catch-all: rename, retire, file. Nothing was deleted.
- The desk is not a layer. Reaching for layer seven hands the reader l6, exactly as the count rule says.
- The tree's silence on access is deliberate. Both repositories ran for one day with the sessions' rules stated in the tree and then removed; nothing in the tree depended on them.

---
