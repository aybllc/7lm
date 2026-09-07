<!-- Canonical Markdown form of the Seven-Layer Model (7LM) Harmonized Authoritative Architecture Specification,
     version of 7 September 2026. This Markdown is the source; the .docx filed beside it is generated from the text
     below this comment and reads back to it unchanged. This document states the model. Each directory of the tree
     states its own position in its own 0.md; the versions of this document, what changed in each, and the owner's
     words behind each rule are at USO/l6/history/specification-history.md. -->

# SEVEN-LAYER MODEL (7LM)

Harmonized Authoritative Architecture Specification

The model, its layers, and its canonical directory topology

*7LM Harmonized Authoritative Architecture Specification • 7 September 2026*

> Authority\
> This specification states the controlling 7LM research architecture: the seven interior layers, the numbered face, their boundaries, and one canonical agnostic directory topology. It is authoritative for this research program. Capability branches may remain empty when unused; they remain part of the agnostic topology so a project can instantiate them without changing the architecture.

Version\
Version of 7 September 2026. The history of versions and changes, with the owner's words behind each rule, is at L8/L6/history/specification-history.md in the scaffold repository.

### How to use this document

This document states the model and nothing else: what the layers are, where each one stops, the tree, the rules that hold across layers, and how a definition you do not own is carried in. It is short on purpose.

Each directory of the canonical tree states itself in its own 0.md: the full contract of its layer, what it owns, what may be done there, what it does not hold, its worked cases, and its inherited terms. Those sheets are the documentation. This document does not repeat them. Where a sheet and this document differ, this document controls.

To place a thing, ask which layer can state it correctly: each representation belongs at the lowest layer where it can be stated correctly. The recurring cases — research, writing, experiment, contained architecture, code, data, an external definition, publication — are settled at L8/L4/0.md.

To debug, find the first layer where the invariant or contract fails, and return the correction to that owner.

To find what changed, when, and on whose word, read the records at L6/history/. This document states the architecture as it is, not how it got here.

---

## What 7LM is

7LM exists to:

1. separate ontology/semantics from state space, formal mathematics, engineering mathematics, realized work, research judgment, memory/history, and external provenance/governance/peering/publication;
2. pin lower-layer contracts so multiple research corpora can rely on them;
3. prevent semantic drift;
4. localize errors to the layer that owns them;
5. allow repair, promotion, pinning, supersession, and shedding without collapsing the whole research program;
6. keep implementation details from silently redefining lower-layer science.

The operational debugging principle is:

> Find the first layer where the invariant or contract fails, and return the correction to that owner.

---

## Two valid directions

Authorized external inspection inward:

L7→L6→L5→L4→L3→L2→L1→L0

Scientific construction outward:

L0→L1→L2→L3→L4→L5→L6→L7

---

## First is always 0

L0 through L6 are the seven interior dependency layers. L7 is the numbered external Surface / Forward Face; it participates in traversal but is not an eighth interior dependency layer.

The coherent principal L0-L7 information sheets control. Repeated contracts and contradictory anchors are superseded; unique notes, cases, rationales, and boundary research are preserved. Questionable inherited concepts are reserved with topology unadjudicated unless this specification expressly places them.

First is always 0.\
The owner's definition, given with its table:

| **semantic** | **>** | **magnitude** |
|---|---|---|
| FIRST | is | 0 |
| SECOND | is | 1 |
| THIRD | is | 2 |
| FOURTH | is | 3 |

**[Clarification]** Ordinals are semantics; numbers are magnitudes; the relation between them is "is". The seven interior layers are the seven semantics FIRST through SEVENTH and the seven magnitudes L0 through L6, so the seventh layer is L6: layer 7 will always be layer 6. L7 is a magnitude, the position numbered 7, the eighth reached in traversal: numbered, not a layer. L8 is a count, not a position: the interior's own zero over the seven layer zeros. Nothing follows the desk in traversal; past the face the count begins again at zero, in another object's tree, where this whole object is one bound object at a peer position.

**[Note]** Author note. L7, pronounced El-Seven, is the desk: the L is the lower left hand corner of the desk and the 7 is the upper right; the name draws the rectangle that this layer is, its Surface. L8 is the research packet on the desk: two zeros stacked, the interior's zero over the zeros of the seven layers. The interior directories carry uppercase too: L0 through L7 are the eight bits of a byte, 0 being a bit, and L8 is the extra bit that carries the semantic, as information needs an extra bit to catch any error. The names are design, not decoration, and were not chosen by accident.

---

## The layers

| **Layer** | **Owns** | **Stops at** |
|---|---|---|
| **L0 — Semantic / Foundational** | Local semantic/rail version of the bounded thing; origin contract, not a warehouse for external definitions. | A source L0 definition may travel through source L7 egress and receiving L7 ingress to receiving L0. At receiving L0 it remains exact, externally authored, immutable, version-pinned, and explicitly tagged; it is not locally redefined or counted as local authorship. L0 does not own prior art, provenance, public/legal governance, state transition, operator, proof, numerical method, experiment, or research conclusion. |
| **L1 — State Space** | Admissible states and static possibility bounds. | No carrying, transition, selection, learning, calculation, propagation, or transformation. Formal operation begins at L2. |
| **L2 — Formal Mathematics** | Exact formal objects and lawful operation over L1. | No engineering tolerance, approximation quality, physical realization, measurement, or empirical truth is claimed here. |
| **L3 — Engineering Mathematics** | Approximation, numerical representation, tolerance, uncertainty, and feasibility. | L3 is not the realized L4 output and does not itself create empirical evidence. |
| **L4 — Conversion** | Conversion / realized work / identifiable output. | L4 does not authorize its own L5 interpretation and cannot flatten lower contracts into a convenience summary. |
| **L5 — Research / Discourse** | Interpretation, review, judgment, argument, and teaching. | Consensus, prose, authority, or usefulness cannot substitute for proof, measurement, or a lower-layer fact. |
| **L6 — Library** | Memory, history, reconstruction, retirement, and query orientation. | L6 records, preserves, and orients; it does not make the L5 research judgment or establish truth. |
| **L7 — Surface / Forward Face** | External provenance, public/legal governance, peering, publications, exposure, and exchange. | L7 owns the external relation, not the lower-layer scientific meaning. Presence, publication, copyright, patent status, custody, or provenance at L7 does not make an object valid, complete, true, or internally authored. |

Each layer's full contract — its core question, function, directional inputs, output, what it owns, what may be done there, the acceptance check, its machine-metadata rule, and its worked cases — stands at that layer's own sheet: L8/L0/0.md through L8/L6/0.md for the interior, and L7/0.md for the face.

Higher layers do not silently repair lower layers. If a higher-layer object requires different lower-layer meaning, the lower-layer dependency is revised explicitly rather than reinterpreted in place.

Layer ownership is local. A topic may appear at several layers, but each representation belongs at the lowest layer where that representation can be stated correctly.

Change one layer at a time. A correction at one layer does not silently rewrite another layer.

A canonical branch may remain empty when unused. Presence in the agnostic topology establishes admissible capability, not mandatory population.

Directory metadata may enforce a machine rule, but it does not create the human semantic meaning carried by /0. Conversely, /0 does not substitute for machine instructions.

Operational containment and analytic expansion are different relations. A complete architecture may remain owned at one 7LM layer while questions about its origin, justification, development, or effects generate representations at other 7LM layers. The contained architecture is not remapped merely because the inquiry expands.

---

## Topology and traversal

L7 is outside the USO and is physically a sibling boundary to L8/. L6 through L0 are the scientific interior. Physical siblinghood and semantic sequence are different relations: crossing L7 <-> L6 is a boundary/peering event, not filesystem nesting.

```text
external peer / citizen / practitioner
                 |
                 v
      [ L7 SURFACE / FORWARD FACE ]
======== boundary / peering separator ========
                    USO

        [ L6 LIBRARY / MEMORY ]
      [ L5 RESEARCH / DISCOURSE ]

   [ L4 CONVERSION / REALIZATION BAY ]
       contained operational architecture
       may expand internally here
       example: complete OSI L1-L7 stack

[ L3 ENGINEERING MATHEMATICS ]
        [ L2 FORMAL MATHEMATICS ]
              [ L1 STATE SPACE ]
---------- local L0 boundary ----------
     [ L0 SEMANTIC / FOUNDATIONAL ]
```

The canonical research tree keeps the interior physically flat: L6/, L5/, L4/, L3/, L2/, L1/, and L0/ are siblings under L8/. The arrows, groupings, and visual bands in this outline indicate traversal, dependency, or analytic view; they do not create child-directory containment.

| **Analytic view** | **Meaning** |
|---|---|
| L6 / L5 upper interior | Memory/history and research/discourse are the upper scientific interior. They remain separate layer owners even when shown as one research-facing band. |
| L4 realization bay | A whole realized architecture may be contained here and may expand internally according to its own native structure without commandeering 7LM layer numbers. |
| L3 / L2 / L1 technical-possibility bundle | Engineering mathematics, exact formalization, and admissible state space can be examined together when the question requires all three dependencies. |
| L3 / L2 nested sub-bundle | Within the broader L3-L2-L1 view, L3-L2 is a tighter engineering/formal sub-bundle when L1 is already pinned and not itself under question. |
| L0 local semantic boundary | L0 is deliberately separated from L1. L0 establishes the local semantic/foundational contract; L1 establishes admissible states under that contract. |

**[Clarification]** *Author note.* These bundles are semantic and dependency views, not filesystem nesting and not mandatory traversal paths. The same scientific object may be railed through different subsets of the architecture according to the question being asked, while each representation remains owned by the layer that can state it correctly.

---

## Canonical Research Directory Topology

One complete agnostic directory structure is available to all research repositories. A branch may remain empty when unused; the canonical tree is not reduced merely because one project does not need a capability.

Notation: /0 means the directory carries its local 0.md human-readable semantic description. Directory metadata is attached to the directory itself and is therefore not drawn as another branch in the tree.

```text
<repo>/
├── README.md
├── L7/0
│   ├── provenance/0
│   │   ├── prior-art/0
│   │   ├── sources/0
│   │   ├── lineage/0
│   │   └── authority/0
│   ├── governance/0
│   │   ├── copyright/0
│   │   ├── licensing/0
│   │   ├── patents/0
│   │   ├── permissions/0
│   │   ├── access/0
│   │   └── restrictions/0
│   ├── peering/0
│   │   ├── private/0
│   │   │   ├── ingress/0
│   │   │   │   └── peer-1/0
│   │   │   │       └── object-1/0
│   │   │   └── egress/0
│   │   │       └── peer-1/0
│   │   │           └── object-1/0
│   │   └── public/0
│   │       ├── ingress/0
│   │       │   └── peer-1/0
│   │       │       └── object-1/0
│   │       └── egress/0
│   │           └── peer-1/0
│   │               └── object-1/0
│   └── publications/0
└── L8/0
    ├── L6/0
    │   ├── history/0
    │   └── retired/0
    ├── L5/0
    │   ├── research/0
    │   │   ├── lanes/0
    │   │   ├── review/0
    │   │   └── findings/0
    │   └── institution/0
    │       ├── peers/0
    │       └── undergraduates/0
    ├── L4/0
    │   └── work/0
    │       ├── writing/0
    │       ├── experiments/0
    │       └── computation/0
    ├── L3/0
    │   └── engineering-mathematics/0
    │       ├── approximation/0
    │       ├── uncertainty/0
    │       └── tolerances/0
    ├── L2/0
    │   └── formal-mathematics/0
    │       ├── relations/0
    │       ├── operators/0
    │       └── proofs/0
    ├── L1/0
    │   └── state-space/0
    └── L0/0
        ├── universality/0
        ├── pedagogy/0
        ├── epistemic/0
        ├── ontology/0
        └── semantics/0
            └── definitions/0
```

Canonical-tree rule. Unused now does not mean removed. The same complete topology is available to Autonomous, Auditonomous, OMMP, classroom research, institutional research, and future research repositories.

**[Clarification]** README.md is where a reader starts; it is not the documentation. The documentation is the sheets, one 0.md per directory, and this specification. The README states what the repository is, the reading order (the desk L7/0, the interior L8/0, then every sheet), the root, and where the prior README is, and nothing else. The root holds README.md, L7/, and L8/, and may hold repository infrastructure that is not a layer: the one CI check at .github/workflows/integrity.yml, which refuses unresolved conflict markers, a root that is not canonical, and a sheet whose heading is not its path, reports directories without a sheet, and moves nothing; and .gitignore. Every 7LM repository has the same root.

**[Research Note]** Each /0 begins with the object directory and path: /data/location/object

**[Clarification]** Standing. Each local 0.md first identifies the directory/object and its path, then supplies that directory's semantic description. Machine instructions belong to the directory metadata, not to the semantic prose.

**[Clarification]** The topology states positions and meaning. It states no rule about what any intelligence, a person, a session, a model, or an orchestrator, may or may not touch. Where such rules exist they belong to repository infrastructure outside the layers, and general repository infrastructure is not automatically a layer.

L7 = Desktop

L8 = USO, the bounded scientific object's interior: the research packet on the desk

The USO is the compartmentalized scientific interior that allows the components/representations of a bounded thing to occupy their correct layer without forcing the entire repository or corpus to share one maturity status. General repository infrastructure is not automatically a layer.

A bounded exemplar can be written or made at L4 while its semantic, state-space, formal, engineering, research, memory/history, provenance/governance, and surface representations remain separately addressable. The layer tree is the discourse structure of a thing, not a command to refile unrelated repository infrastructure.

---

## A definition you do not own

The Autonomous/Auditonomous root issue supplies the concrete origin of the agnostic peering rule: one bounded research object must be able to depend on another without owning, copying, redefining, or maintaining both objects' foundational semantics. Auditonomous can use the exact Autonomous definition without becoming a second semantic authority for Autonomous. peer-1/object-1 is the agnostic form of this concrete ownership problem.

**[Clarification]** The Autonomous and Auditonomous repositories are implementation work in progress; their current layouts do not control the architecture. Architecture and implementation status are separate claims.

### Contextual semantic route

Source L0 definition → source L7 egress → receiving L7 ingress → receiving L0. A source object's L0 definition is an L7 egress object at its boundary; to us it is L7 ingress directed to our L0. Its semantic identity remains source-owned L0 throughout the exchange.

The receiver does not have to redefine the peer definition. Every internal representation that uses it carries the exact bound version with an immutable external-ownership tag: object identity, owner, source layer, version, and ingress binding. An upstream change creates a new binding; it does not mutate the pinned object.

Declared semantic-deference rule. For the bounded purpose of interpreting the peer, the receiver intentionally takes the owner's exact bound definition as authoritative for what the owner means and does not re-prove or locally redefine that meaning. This declared trust is not a claim that the definition is objectively true, not an endorsement of downstream claims, and not a transfer of authorship.

An argument about Autonomous cannot silently stand in for an argument about Auditonomous. A cross-object claim requires an explicit named relation or handoff. The same identity-tagging rule applies to agnostic methods as they are made and carried through the architecture.

Autonomous has one bounded semantic job: state and freeze the narrowest reasonable agreement shared across exact, independently bound standards definitions. It must not manufacture consensus where sources materially disagree; every disagreement remains source-tagged and visible.

Auditonomous consumes the pinned Autonomous consensus baseline and authors the Auditonomous difference as an explicit local delta. The baseline and delta remain separately owned and overlaid rather than blended into a dual-owned definition.

Canonical direct L7 branches are L7/provenance/, L7/governance/, L7/peering/, and L7/publications/.

### Standing rules

A definition lives once, at its owner. L7 holds the boundary binding and provenance relation. The exact bound version may be carried inward with its immutable ownership tag, but it never becomes a copied substitute or locally authored definition.

To change an immutable external object, return to its owner. The repository using the object does not edit the peer-owned source.

Material crossing outward may lose fidelity and may never gain scientific maturity merely by being exposed.

No outsider traverses the USO by default. What an outside reader or system needs is represented at the forward face.

Machine-readable metadata may support automation, but the architecture does not assume that automation has been enabled or validated. Current research practice may remain manual until the metadata contract is tested.

---

## Contained architectures

An architecture may be contained at one 7LM layer operationally while questions about that architecture expand across 7LM epistemically. When the question is how the OSI architecture operates, the complete OSI model remains inside 7LM L4: OSI L1 through OSI L7 are internal layers of a contained realized architecture, OSI L7 is not 7LM L7, and the OSI layer numbers do not map onto the 7LM layer numbers. When the question changes to the origins, development, justification, standardization, institutional history, or design constraints of OSI, the inquiry may rail the OSI object across the architecture; the operating stack remains an L4 object and the inquiry generates layer-owned representations of it. Which layer answers which question is tabulated at L8/L4/0.md, and the analytic views that select a subset of layers are stated at L8/L3/0.md.

---

## The rest of the documentation

The sheets. Every directory carries its own 0.md, headed by its path, stating that position in full. Read L7/0.md for the face and L8/0.md for the interior, then the sheet of whatever position you are working at.

The record. What changed, when, on whose word, and what each prior version carried is at L8/L6/history/. The prior texts that integrity needs reconstructable are retired at L8/L6/retired/. Integrity is enforced; no deletion is implied.

---

## Exemplars

The architecture is instantiated in four repositories: the scaffold at https://github.com/aybllc/7lm, the exemplars at https://github.com/aybllc/autonomous and https://github.com/aybllc/auditonomous, and the curated-source archive at https://github.com/aybllc/l6.

Architecture and implementation status are separate claims. What each repository holds, and where it is not yet as this specification states, is documented in that repository's own sheets and in its records at L6/history/. Their layouts do not control the architecture.

---

## Harmonization Record

Normative authority and non-erasure rule. This document and the layer sheets control. Harmonization removes stale duplicate contracts but preserves unique research notes, author notes, examples, cases, rationales, hypotheses, and inherited terms. A reserved term remains available for research without manufacturing a directory or layer owner.

Architecture and implementation status are separate claims. The canonical topology declares admissible and owned positions even when a present repository has not instantiated them. Current exemplar layouts are implementation work in progress and do not rewrite the architecture.

**[Clarification]** Questionable inherited semantics are preserved in their stated or recoverable meaning. Unless the disposition at the receiving sheet expressly ratifies an owner and path, topology remains unadjudicated. No convenience placement settles an open scientific question.

Each inherited term is disposed of at the sheet of the layer that received it, under that sheet's "Inherited terms and dispositions". The full table of inherited terms with their dispositions, and the dated record of each disposition, stands at L8/L6/history/specification-history.md.
