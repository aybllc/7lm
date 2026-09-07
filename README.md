# 7lm — Seven-Layer Model (7LM)

This repository is the scaffold of the Seven-Layer Model research architecture: one canonical agnostic directory topology and one uniform information sheet for each layer. It is the only current README in the repository; the pre-harmonization README is preserved, not as a gate, at `USO/l6/retired/scaffold-2026-08-20/README.md`. Every directory below describes itself in a local `0.md`. Nothing here is automated. The controlling text is the Harmonized Authoritative Architecture Specification filed at `USO/l4/work/writing/7lm-harmonized-architecture-specification.md` (Markdown conversion of the `.docx` beside it); where this README and that specification differ, the specification controls.

## What 7LM is

The Seven-Layer Model (7LM) is a dependency and fault-containment architecture for separating local meaning, admissibility, exact formalization, engineering approximation, realized work, research interpretation, reconstructable memory, and external presentation. Its practical debugging rule is to find the first layer at which the required invariant, evidence relation, or handoff fails, then return the correction to that owner.

7LM exists to:

- separate ontology/semantics from state space, formal mathematics, engineering mathematics, realized work, research judgment, memory/history, and external provenance/governance/peering/publication;
- pin lower-layer contracts so multiple research corpora can rely on them;
- prevent semantic drift;
- localize errors to the layer that owns them;
- allow repair, promotion, pinning, supersession, and shedding without collapsing the whole research program;
- keep implementation details from silently redefining lower-layer science.

The operational debugging principle is:

> Find the first layer where the invariant or contract fails.

## Two valid directions

Authorized external inspection inward:

L7→L6→L5→L4→L3→L2→L1→L0

Scientific construction outward:

L0→L1→L2→L3→L4→L5→L6→L7

Direction rule. Scientific construction proceeds from L0 outward only as dependencies are established. External inspection begins at L7 and proceeds inward. Description does not become prescription merely because the structure can be traversed.

## Canonical research directory topology

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
└── USO/0
    ├── l6/0
    │   ├── history/0
    │   └── retired/0
    ├── l5/0
    │   ├── research/0
    │   │   ├── lanes/0
    │   │   ├── review/0
    │   │   └── findings/0
    │   └── institution/0
    │       ├── peers/0
    │       └── undergraduates/0
    ├── l4/0
    │   └── work/0
    │       ├── writing/0
    │       ├── experiments/0
    │       └── computation/0
    ├── l3/0
    │   └── engineering-mathematics/0
    │       ├── approximation/0
    │       ├── uncertainty/0
    │       └── tolerances/0
    ├── l2/0
    │   └── formal-mathematics/0
    │       ├── relations/0
    │       ├── operators/0
    │       └── proofs/0
    ├── l1/0
    │   └── state-space/0
    └── l0/0
        ├── universality/0
        ├── pedagogy/0
        ├── epistemic/0
        ├── ontology/0
        └── semantics/0
            └── definitions/0
```

Canonical-tree rule. Unused now does not mean removed. The same complete topology is available to Autonomous, Auditonomous, OMMP, classroom research, institutional research, and future research repositories. A canonical branch may remain empty when unused. Presence in the agnostic topology establishes admissible capability, not mandatory population.

L7 is outside the USO and is physically a sibling boundary to USO/. L6 through L0 are the scientific interior. Physical siblinghood and semantic sequence are different relations: crossing L7 <-> L6 is a boundary/peering event, not filesystem nesting. `USO/0.md` describes the interior; `L7/0.md` describes the forward face.

## Layers

| Layer | Name | Core question | Path |
|---|---|---|---|
| L0 | LAYER 0 — Local semantic/rail version of the bounded thing; origin contract, not a warehouse for external definitions. | What local ontological, semantic, epistemic, and universality distinctions does THIS object establish before an admissible state is declared? | `USO/l0/` |
| L1 | STATE SPACE — Admissible states and static possibility bounds. | What states and distinctions are possible or admissible under the established L0 contract? | `USO/l1/` |
| L2 | FORMAL MATHEMATICS — Exact formal objects and lawful operation over L1. | What follows exactly when lawful operations are defined over L1? | `USO/l2/` |
| L3 | ENGINEERING MATHEMATICS — Approximation, numerical representation, tolerance, uncertainty, and feasibility. | How can the exact L2 relation be made feasible under declared constraints? | `USO/l3/` |
| L4 | LAYER 4 — Conversion / realized work / identifiable output. | What conversion between intellectual property and energy, in either direction, was actually made, written, run, measured, instantiated, operated, manufactured, or recorded? | `USO/l4/` |
| L5 | RESEARCH / DISCOURSE — Interpretation, review, judgment, argument, and teaching. | What may responsibly be concluded, questioned, taught, compared, or decided from the available work? | `USO/l5/` |
| L6 | LIBRARY — Memory, history, reconstruction, retirement, and query orientation. | Can the object's internal history, prior states, failures, corrections, and retirement be reconstructed and correctly oriented for inspection? | `USO/l6/` |
| L7 | SURFACE / FORWARD FACE — External provenance, public/legal governance, peering, publications, exposure, and exchange. | What provenance, governance, peer relation, publication, or other external representation must exist at the object's forward face? | `L7/` |

The Name column carries each layer's heading and subtitle as the specification prints them. The specification's topology diagram bands the same layers as L0 SEMANTIC / FOUNDATIONAL, L1 STATE SPACE, L2 FORMAL MATHEMATICS, L3 ENGINEERING MATHEMATICS, L4 CONVERSION / REALIZATION BAY, L5 RESEARCH / DISCOURSE, L6 LIBRARY / MEMORY, and L7 SURFACE / FORWARD FACE. L0 through L6 are the seven interior dependency layers. L7 is the numbered external Surface / Forward Face; it participates in traversal but is not an eighth interior dependency layer.

## Architecture-wide dependency rules

Higher layers do not silently repair lower layers. If a higher-layer object requires different lower-layer meaning, the lower-layer dependency is revised explicitly rather than reinterpreted in place.

Layer ownership is local. A topic may appear at several layers, but each representation belongs at the lowest layer where that representation can be stated correctly.

Change one layer at a time. A correction at one layer does not silently rewrite another layer.

A canonical branch may remain empty when unused. Presence in the agnostic topology establishes admissible capability, not mandatory population.

Directory metadata may enforce a machine rule, but it does not create the human semantic meaning carried by /0. Conversely, /0 does not substitute for machine instructions.

Operational containment and analytic expansion are different relations. A complete architecture may remain owned at one 7LM layer while questions about its origin, justification, development, or effects generate representations at other 7LM layers. The contained architecture is not remapped merely because the inquiry expands.

## The 0.md convention

Every directory carries a local Layer 0 semantic description. Standing. Each local 0.md first identifies the directory/object and its path, then supplies that directory's semantic description. Machine instructions belong to the directory metadata, not to the semantic prose. In each sheet the first heading is the directory's canonical path and the first body line names the object, path, layer, and owner.

/0 carries human-readable meaning; metadata carries machine-actionable instruction. Neither replaces the other. This separation keeps semantic description distinct from machine operation. The layer sheets describe the machine metadata each layer would carry; none of it is instantiated. By the owner's rule this repository holds no automation — no scripts, workflows, actions, hooks, generators, schemas, templates, or metadata files. Everything is done by a person, by hand, and reviewed by reading. The specification states the same allowance. Machine-readable metadata may support automation, but the architecture does not assume that automation has been enabled or validated. Current research practice may remain manual until the metadata contract is tested.

## Exemplars

Three exemplar programs fill in the layers by reference. Each layer root sheet cites, by repository path, the artifacts in these repositories that play that layer's role.

- **EXEMPLAR AUTO — aybllc/autonomous @ 0504961** — https://github.com/aybllc/autonomous
  In its own words: "Research repository of Eric D. Martin. Subject: what 'autonomous' means in codified authority, what it requires, and at what unit it attaches."
  Its position is a plural entry of codified definitions carried in verbatim with ownership tags, plus a locally derived, explicitly internally derived rule-set for using the word; the definition it holds is the term the sibling auditonomous repository references rather than redefines.
- **EXEMPLAR AUDIT — aybllc/auditonomous @ 280226a** — https://github.com/aybllc/auditonomous
  In its own words, the "research home for auditonomous (adj.) — a word coined by Eric D. Martin — and for the theory, engineering doctrine, and record format built around it": bounded autonomy under mandatory auditability.
  Everything there is declared INTERNAL ONLY; contradictions are reported, never harmonized, and the Autonomous definition is consumed as a peer object.
- **EXEMPLAR OMMP — aybllc/ommp @ 609e4de, with aybllc/uha-stack @ 49ab41f as the UHA it attaches to** — https://github.com/aybllc/ommp and https://github.com/aybllc/uha-stack
  In its own words, ommp is "the research repository of Eric D. Martin. Subject: oMMP (Observer MetaModal Platform) — an observer-anchored grammar for recording an observation as typed mathematical fields rather than as a narrative story."
  uha-stack is the configuration-controlled home of the UHA, "an observer-rooted, state-space-first, openly decodable binary addressing and record system", whose address is the first, opaque, anchored field of the oMMP record; ommp is declared INTERNAL ONLY; uha-stack keeps every claim labelled at or below INTERNALLY VALIDATED, with no outside-verified claim.
- All three point into the same curated-source archive, `aybllc/l6`, by path and pinned commit; none holds a source file.

The owner's rule, stated plainly: the exemplars fill in the layers by reference; they are not merged into this scaffold as research projects. In the specification's words, the Autonomous and Auditonomous repositories are implementation work in progress; their current layouts do not control the architecture. Architecture and implementation status are separate claims. The Autonomous/Auditonomous root issue supplies the concrete origin of the agnostic peering rule: one bounded research object must be able to depend on another without owning, copying, redefining, or maintaining both objects' foundational semantics. Reference implementations: https://github.com/aybllc/autonomous and https://github.com/aybllc/auditonomous.

## Where things live

- Controlling specification: `USO/l4/work/writing/7lm-harmonized-architecture-specification.md`, the canonical Markdown form and, for the version of 6 September 2026, the source; `USO/l4/work/writing/7lm-harmonized-architecture-specification.docx` is generated from it and reads back to it unchanged, and is the draft of the next controlling document awaiting the owner's hand. Its Harmonization Record lists every change from the prior version under "Changes of 6 September 2026".
- Superseded draft (its own footer dates it "3 September 2026"): `USO/l6/retired/specification-draft-2026-09-03/`.
- Prior version (the owner's authored document of 4 September 2026, which controlled the wording of that version): `USO/l6/retired/specification-2026-09-04/`.
- Retired pre-harmonization scaffold (2026-08-20), every gate file at its original relative path, including the owner's README sketch: `USO/l6/retired/scaffold-2026-08-20/`.
- Harmonization record of this displacement event (2026-09-04): `USO/l6/history/harmonization-2026-09-04.md`.
- Source ledger (header-only, no rows): `L7/provenance/sources/source-ledger.md`.
- Curated sources: served by pointer from the archive `aybllc/l6` (INTERNAL; read-only from every consuming repository; each row pins the `l6` commit it was read at) — see `L7/provenance/sources/0.md`.
- Layer root sheets: `USO/l0/0.md` … `USO/l6/0.md`, `L7/0.md`; interior root: `USO/0.md`.
- Copyright: one place, `L7/governance/copyright/`. Nothing else in a 7LM repository restates a copyright rule; the sheet there says what to do next (owner's rule, 2026-09-04; applied in `aybllc/autonomous` and `aybllc/auditonomous`).

## Harmonization dispositions

Normative authority and non-erasure rule. The principal L0-L7 sheets and the explicit rules in this record control. Harmonization removes stale duplicate contracts but preserves unique research notes, author notes, examples, cases, rationales, hypotheses, and inherited terms. A reserved term remains available for research without manufacturing a directory or layer owner.

Questionable inherited semantics are preserved in their stated or recoverable meaning. Unless a row above expressly ratifies an owner and path, topology remains unadjudicated. No convenience placement in this document settles an open scientific question.

| Inherited term or issue | Disposition | Controlling harmonization |
|---|---|---|
| prior-art | Relocated | External antecedents belong at L7/provenance/prior-art/. |
| definitions | Ratified | Locally authored definitions belong at USO/l0/semantics/definitions/; peer definitions arrive as immutable external bindings. |
| semantic-formulas | Split and reserved | Semantic reading remains L0; an exact formula is L2; an applied, tolerant, adaptive, or engineering formula is L3. The inherited compound term remains searchable. |
| thesis-statements | Relocated | Research claims and thesis statements belong at USO/l5/research/lanes/ or the corresponding L5 research artifact. |
| origidity; certainty; intolerance | Reserved | Candidate L1 semantics preserved; topology remains unadjudicated. |
| found; caught; naught | Reserved | caught remains the zero state; found remains the observer role; naught remains the empty or settled state. Their topology remains unadjudicated. |
| regress | Reserved | Preserved as a prior unadjudicated holding concept; active path and owner remain unadjudicated. |
| corpus | Split and reserved | Released corpus/publication identity belongs at L7/publications/; the broader inherited term remains reserved where its exact role is not yet adjudicated. |
| INFRASTRUCTURE | Superseded as L4 name | L4 is Conversion. Infrastructure belongs at L4 only when it is the bounded work or conversion being made; generic repository support is not automatically a layer. |
| DEVOID; IMMUTABLE; FINITE; INFINITE; IDENTITY BY PROSE; RESEARCH MEMORY; SCIENTIFIC DESKTOP | Descriptive | Preserved as historical mnemonics or working language; the principal layer sheets control ownership. |
| L6 provenance | Split | Internal reconstructable memory remains L6; external source, authority, prior art, and public provenance belong at L7/provenance/. |

## Owner's working sketch (retained)

The block below is the owner's working sketch (written 2026-08-24, commit 3bde809; retired 2026-09-04, commit e810f61), retained verbatim from the retired README at `USO/l6/retired/scaffold-2026-08-20/README.md`. Three of its bands match rows of the specification's analytic-view table (the L6 / L5 upper interior, the L4 realization bay, and the L3 / L2 nested sub-bundle); its L1 and L0 lines match the L1 STATE SPACE band and the L0 local semantic boundary. The specification states that such bundles are semantic and dependency views, not filesystem nesting. The sketch's own separators and terms are the owner's and are not adjudicated here.

```text
 | L7 | desktop, publications, peering, governance, collaboration, endpoints, provenance (authority and custody - provenance/ - records recoverable source identity, issuer, exact version, locator, declared scope, and local use; the local table is provenance/source-ledger.md.
 
 thesis declaration

    |---broken zero---|

| L6 | historical, negative research, curated library,  logs
| L5 | research, writing, peer-review, discourse, conference ... inspection

    |---broken zero---|

| L4 | modeling, processing, manufacturing, computing ... input:energy/work --> output:work/energy = conversion. Layer 4 is the conversion of layer 0-3 by processing, transforming and converting the corpus, matter and energy into a physical object or projected into the physical universe through a physical medium

    |---broken zero---|

| L3 | engineering mathematics, certainty ... tolerance, ranges, statistics, Pi, infinite 
| L2 | formal mathematics, notation, uncertainty ... intolerant, exactness, tightness, enclosure, finite

    |---broken zero---|

| L1 | state spaces, admissibility conditions, base logic, binary ... discrete boundary

    |---broken zero---|

| L0 | ontology, semantics, pedagogic, epistemic ... semantic explanations
```

Paths named inside the sketch are the sketch's own; the ledger it names is now at `L7/provenance/sources/source-ledger.md`.
