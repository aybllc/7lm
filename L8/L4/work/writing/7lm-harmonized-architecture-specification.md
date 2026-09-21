<!-- Canonical Markdown form of the Seven-Layer Model (7LM) Harmonized Authoritative Architecture Specification,
     version of 20 September 2026. This Markdown is the source; the .docx filed beside it is generated from the text
     below this comment and reads back to it unchanged. The history of versions and changes, with the owner's words
     behind each rule, is at L8/L6/history/specification-history.md. -->

# SEVEN-LAYER MODEL (7LM)

Harmonized Authoritative Architecture Specification

Canonical research directory topology and uniform layer information sheets

*7LM Harmonized Authoritative Architecture Specification • 20 September 2026*

> Authority\
> This specification states the controlling 7LM research architecture: one canonical agnostic directory topology and one uniform information sheet for each layer. The structure, layer boundaries, directory prose, machine-metadata distinction, and stated rationales are authoritative for this research program. Capability branches may remain empty when unused; they remain part of the agnostic topology so a project can instantiate them without changing the architecture.

Version\
Version of 20 September 2026. The history of versions and changes, with the owner's words behind each rule, is at L8/L6/history/specification-history.md in the scaffold repository.

Self-description and machine-instruction rule\
Every directory carries a local Layer 0 semantic description. In tree notation, /0 denotes that directory's local 0.md without drawing the file as a separate branch. The same directory separately carries machine-readable metadata for machine instructions, constraints, permissions, routing, validation, and lifecycle behavior. /0 carries human-readable meaning; metadata carries machine-actionable instruction. Neither replaces the other. This separation keeps semantic description distinct from machine operation.

Direction rule\
Scientific construction proceeds from L0 outward only as dependencies are established. External inspection begins at L7 and proceeds inward. Description does not become prescription merely because the structure can be traversed.

### Originating peering exemplar

The Autonomous/Auditonomous root issue historically exposed a useful boundary case: one bounded research object may maintain an explicit relationship with another bounded object while keeping the two objects distinguishable. That case helped reveal the `peer-N/object-M` form, but it does **not** define the full meaning of peering.

Peering is more general: it represents an identifiable relationship across the bounded object's external surface. A peer can be a person, institution, repository, archive, laboratory, publisher, computational system, model, service, instrument, organization, or another bounded object. The relation may be scientific, administrative, educational, editorial, legal, computational, logistical, or otherwise external.

**[Clarification]** The Autonomous and Auditonomous repositories are implementation work in progress. Their current layouts and handling rules do not control the agnostic architecture.

#### Example semantic route

One use of peering is an explicit semantic exchange between two bounded research objects:

Source L0 definition → source L7 egress → receiving L7 ingress → receiving L0 use.

In the originating Autonomous/Auditonomous exemplar, the receiving object chose to bind an exact external version, preserve its source identity, and treat it as reference-only. Those are properties of that exemplar's handling contract. They are not universal requirements of peering.

A definition may also be adopted from a book, article, archive, database, standards source, web search, or another external source without a peering relation being represented at all. In that case the semantic use belongs where the meaning functions, while provenance describes the source relation where relevant.

[
	ext{external source}\not\Rightarrow	ext{peer}
]

The architectural distinction is:

- L0 states the semantic representation used by the bounded object;
- L7/provenance states the external source relation where relevant;
- L7/peering states an identifiable external counterpart relationship only when that relationship itself is part of the represented object.

Canonical direct L7 branches are L7/provenance/, L7/governance/, L7/peering/, and L7/allications/.

#### Seven-layer count and harmonization rule

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

**[Clarification]** Peers are physical and are counted from 1 at L7/peering/: peer-1, object-1. The layers are counted from 0: 0 is the semantic origin, where the Semantic and Epistemic rails define the layers above; it is what exists first, before anything physical. The two counts do not conflict.

**[Note]** Author note. L7, pronounced El-Seven, is the desk: the L is the lower left hand corner of the desk and the 7 is the upper right; the name draws the rectangle that this layer is, its Surface. L8 is the research packet on the desk: two zeros stacked, the interior's zero over the zeros of the seven layers. The interior directories carry uppercase too: L0 through L7 are the eight bits of a byte, 0 being a bit, and L8 is the extra bit that carries the semantic, as information needs an extra bit to catch any error. The names are design, not decoration, and were not chosen by accident.

**[Clarification]** The packet reading. The owner, 12 September 2026, quoted as written: "L8 has to envelope them all to simulate a packet where gteh floor is l1 the end is l6, ythe glue is l7 adn l8 is gthe connectror the the next l0". Read the bounded object as one packet. L0 is the origin: the meaning that exists in the head first and is written down second; it is not payload. L1 is the floor of the payload and L6 its end. L7 is the glue, the face at which the object binds to what is outside it. L8 envelopes them all, and its trailing edge is the connector to the next object's L0. The connector is why nothing follows the desk in traversal: past the face the object hands off, and the count begins again at zero in another object's tree. This states as a structure what the byte reading above states as a count, and the two agree.

**[Clarification]** The packet reading changes no position, no count, and no path. The eight positions remain L0 through L7; first is always 0; L8 remains a count and not a ninth position; L0 remains the first position, excluded from the payload but not from the count. On disk L7/ and L8/ remain siblings at the repository root, with L8/ holding the interior L0 through L6, as the canonical topology states. The owner ruled the directory structure unchanged, 12 September 2026, quoted as written: "I like to waive that l seven and l eight are set up right now in the current directory structure." The envelope is a reading of that layout, not a change to it.

### 7LM is a dependency and fault-containment architecture

7LM exists to:

1. separate ontology/semantics from state space, formal mathematics, engineering mathematics, realized work, research judgment, memory/history, and external provenance/governance/peering/publication;
2. pin lower-layer contracts so multiple research corpora can rely on them;
3. prevent semantic drift;
4. localize errors to the layer that owns them;
5. allow repair, promotion, explicit version/source distinction, supersession, and shedding without collapsing the whole research program;
6. keep implementation details from silently redefining lower-layer science.

The operational debugging principle is:

> Find the first layer where the invariant or contract fails.

### Two valid directions

External inspection inward:

L7→L6→L5→L4→L3→L2→L1→L0

Scientific construction outward:

L0→L1→L2→L3→L4→L5→L6→L7

### Architecture-wide dependency rules

Higher layers do not silently repair lower layers. If a higher-layer object requires different lower-layer meaning, the lower-layer dependency is revised explicitly rather than reinterpreted in place.

Layer ownership is local. A topic may appear at several layers, but each representation belongs at the lowest layer where that representation can be stated correctly.

Change one layer at a time. A correction at one layer does not silently rewrite another layer.

A canonical branch may remain empty when unused. Presence in the agnostic topology establishes admissible capability, not mandatory population.

Directory metadata may enforce a machine rule, but it does not create the human semantic meaning carried by /0. Conversely, /0 does not substitute for machine instructions.

Operational containment and analytic expansion are different relations. A complete architecture may remain owned at one 7LM layer while questions about its origin, justification, development, or effects generate representations at other 7LM layers. The contained architecture is not remapped merely because the inquiry expands.

---

## Structured Architecture Outline

*APA-like hierarchy with author notes • current working architecture*

### 1. Purpose and controlling method

The Seven-Layer Model (7LM) is a dependency and fault-containment architecture for separating local meaning, admissibility, exact formalization, engineering approximation, realized work, research interpretation, reconstructable memory, and external presentation. Its practical debugging rule is to find the first layer at which the required invariant, evidence relation, or handoff fails, then return the correction to that owner.

Scientific construction/prescription proceeds outward: L0 → L1 → L2 → L3 → L4 → L5 → L6 → L7, but only as far as established dependencies justify. Interpretive inspection of an externally owned object proceeds inward: L7 → L6 → L5 → L4 → L3 → L2 → L1 → L0.

**[Clarification]** *Author note.* Description does not prescribe. A path can be observed or interpreted without becoming a normative requirement. Prescription requires an established dependency that has actually been tested or ratified to the degree the next layer needs.

### 2. Topology and traversal

L7 is outside the USO and is physically a sibling boundary to L8/. L6 through L0 are the scientific interior. Physical siblinghood and semantic sequence are different relations: crossing L7 <-> L6 is a boundary traversal, not filesystem nesting; peering applies only where an external counterpart relationship is represented.

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

### 3. Contained architectures and analytic expansion

An architecture may be contained at one 7LM layer operationally while questions about that architecture expand across 7LM epistemically. Operational ownership answers where the architecture is realized; analytic expansion answers which 7LM owner is needed to state the particular question or representation correctly.

#### 3.1 OSI as an operating architecture

When the question is how the OSI architecture operates, the complete OSI model remains inside 7LM L4. OSI L1 through OSI L7 are internal layers of a contained realized architecture; OSI L7 is not 7LM L7, and the OSI layer numbers do not map onto the 7LM layer numbers.

#### 3.2 OSI as an object of inquiry

When the question changes to the origins, development, justification, standardization, institutional history, or design constraints of OSI, the inquiry may rail the OSI object across the 7LM architecture. The operating OSI stack remains an L4 object; the inquiry generates layer-owned representations of that object according to what is being asked.

| **7LM layer** | **OSI-origin inquiry may ask / represent** |
|---|---|
| L7 - Surface / Forward Face | External source provenance, standards-publication state, governance conditions, outward acts, and relationships to standards bodies or other external counterparts. |
| L6 - Library / Memory | Reconstructable development history, versions, superseded or retired material, internal chronology, and the record needed to recover how the local inquiry developed. |
| L5 - Research / Discourse | Institutional debate, research interpretation, committee or scholarly discourse, pedagogical framing, competing explanations, and judgments about why the architecture took its form. |
| L4 - Conversion / Realization | The realized OSI architecture itself as specified, implemented, taught, tested, transmitted, or otherwise made operational. |
| L3 - Engineering Mathematics | Engineering constraints, tradeoffs, approximation, tolerances, uncertainty, feasibility, or other engineering conditions that shaped or test the architecture. |
| L2 - Formal Mathematics | Exact formal relations, operators, proofs, or formal constraints used to state the architecture where such formalization is actually warranted. |
| L1 - State Space | Admissible structural states, possibilities, exclusions, or coordinate/state-space descriptions when these are part of the question. |
| L0 - Semantic / Foundational | The semantic and foundational distinctions required to describe what is being investigated. A distinction may be locally formulated or adopted from an external source; provenance records source relations where relevant, while peering applies only when an external counterpart relationship itself is represented. |

**[Clarification]** *Author note.* The OSI model does not become 7LM L0-L7. The question about the OSI object expands. Operational containment remains L4, while representations produced by the inquiry are owned by the 7LM layer that can state them correctly.

#### 3.3 Nested analytic views

Some questions require only the L3-L2 engineering/formal sub-bundle. Others require the broader L3-L2-L1 technical-possibility bundle because admissibility itself is under examination. L0 is crossed only when the local semantic or foundational contract is itself part of the question. These are selectable analytic rails, not new containers and not a requirement that every inquiry traverse every layer.

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
│   │   └── controlled/0
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
│   └── allications/0
│       ├── publications/0
│       ├── applications/0
│       ├── communications/0
│       ├── specifications/0
│       ├── notifications/0
│       └── participations/0
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

**[Clarification]** README.md is where a reader starts; it is not the documentation. The documentation is the sheets, one 0.md per directory, and this specification. The README states what the repository is, the reading order (the desk L7/0, the interior L8/0, then every sheet), the root, and where the prior README is, and nothing else. The root holds README.md, L7/, and L8/, and may hold repository infrastructure that is not a layer: the one CI check at .github/workflows/integrity.yml, which refuses unresolved conflict markers, a root that is not canonical, a sheet whose heading is not its path, and a canonical position without a sheet, reports any other directory without a sheet, and moves nothing; and .gitignore. Every 7LM repository has the same root.

**[Research Note]** Each /0 begins with the object directory and path: /data/location/object

**[Clarification]** Standing. Each local 0.md first identifies the directory/object and its path, then supplies that directory's semantic description. Machine instructions belong to the directory metadata, not to the semantic prose.

**[Clarification]** The topology states positions and meaning. It states no rule about what any intelligence, a person, a session, a model, or an orchestrator, may or may not touch. Where such rules exist they belong to repository infrastructure outside the layers, and general repository infrastructure is not automatically a layer.

L7 = Desktop

L8 = USO, the bounded scientific object's interior: the research packet on the desk

The USO is the compartmentalized scientific interior that allows the components/representations of a bounded thing to occupy their correct layer without forcing the entire repository or corpus to share one maturity status. General repository infrastructure is not automatically a layer.

A bounded exemplar can be written or made at L4 while its semantic, state-space, formal, engineering, research, memory/history, provenance/governance, and surface representations remain separately addressable. The layer tree is the discourse structure of a thing, not a command to refile unrelated repository infrastructure.

---

## L0 — LAYER 0

Foundational semantic/rail contract used by the bounded object before admissible state is declared.

| **Core question** | What ontological, semantic, epistemic, and universality distinctions does THIS bounded object use before an admissible state is declared? |
|---|---|
| **Function** | Hold the bounded object's foundational representation, regardless of whether a particular distinction was formulated locally or explicitly adopted from an external source. |
| **Directional inputs** | Construction begins with the meanings and foundational distinctions the bounded object is actually using. External sources may contribute to those meanings; their provenance remains separately representable at L7. |
| **Output** | A rail-grounded L0 contract sufficient for L1. A rail may remain sparse when no representation of that type is needed. |
| **Hard boundary** | L0 owns foundational meaning and distinctions, not prior art, provenance, public/legal governance, state transition, operator, proof, numerical method, experiment, or research conclusion. Source origin does not change the layer role of a meaning used at L0. |
| **Machine metadata** | Machine-readable metadata may identify rail, source reference, scope, version, gate status, or implementation-specific handling conditions. Metadata may describe the representation but must not replace its semantic meaning. |

| **Owns / represents** | **Permitted actions** | **Acceptance / boundary check** |
|---|---|---|
| • Ontological, Semantic, Epistemic, and Universality rail boundaries for this object.<br>• System-level traversal/attachment pedagogy as a directory/function, without making Pedagogy a fifth rail.<br>• Vocabulary and semantic representations used by this bounded object, whether locally formulated or explicitly adopted for a stated scope. | • place each foundational distinction in the rail that states its role<br>• state ambiguity or unresolved meaning without filling it by guess<br>• distinguish semantic use from external provenance when a source relation matters<br>• record changed meaning as a changed semantic state rather than silently conflating it with the prior state | • Every L1 distinction resolves to an L0 meaning actually used by the bounded object.<br>• Source origin and semantic role are not conflated: provenance may describe where a meaning came from, while L0 describes what meaning functions here.<br>• Peering is not required merely because a source is external.<br>• No neighboring rail silently supplies another rail's local meaning. |

**Directory structure**

```text
L8/L0/0
├── universality/0
├── pedagogy/0
├── epistemic/0
├── ontology/0
└── semantics/0
    └── definitions/0
```

**[Boundary Rule]** **Boundary / traversal rule.** L0/semantics contains the semantic representation used by the bounded thing. External origin does not force a meaning out of L0; provenance and peering describe different external relations where those relations are relevant.

**Directory prose and rationale**

| **Directory / thing** | **Prose** | **Why** |
|---|---|---|
| **L8/L0/** | Layer 0 container for the bounded object's foundational and rail representation. | Keeps foundational meaning distinct from state, formalization, engineering, realized work, research judgment, provenance, and surface exchange. |
| **universality/** | Directory for the Universality rail content owned by L0. | Preserves Universality as its own rail instead of letting another rail silently supply it. |
| **pedagogy/** | Directory for system-level traversal and attachment pedagogy. | Keeps pedagogy explicit without turning it into a fifth philosophical rail. |
| **epistemic/** | Directory for the Epistemic rail content owned by L0. | Keeps epistemic distinctions inside the rail that owns them. |
| **ontology/** | Directory for the Ontological rail content owned by L0. | Keeps ontological distinctions inside the rail that owns them. |
| **semantics/** | Directory for the Semantic rail content used by this bounded object. | States what meaning functions here while leaving source history to provenance when relevant. |
| **semantics/definitions/** | Directory for definitions that function in this bounded object's Semantic rail. | Keeps definition as a semantic role independent from whether the wording was locally authored or externally sourced. |

**[Note]** Author note. L0/semantics is the semantic representation under which this bounded object operates. It may be locally formulated, externally adopted, or mixed. The architecture distinguishes semantic function from source provenance rather than requiring local authorship.

**[Research Note]** MOST IMPORTANT: I THINK DRIFT LIVES HERE! NOT ANYWHERE ELSE...(NEEDS A LOT OF STUDY)

**[Clarification]** Standing. This statement is retained as a research hypothesis: semantic drift is expected to originate when the local L0 meaning contract changes or is misapplied. The hypothesis remains open to testing rather than being promoted to a settled rule.

#### In the case of:

In the Autonomous exemplar, IEEE/IEC have already been adjudicating relevant definitions through standards. The locally authored semantic definition used by this bounded object still lives at Layer 0, while the discourse, research, and state-space objects are distilled to their own layers. AUTONOMOUS and AUDITONOMOUS are retained as pedagogical exemplars: EXEMPLAR AUTO and EXEMPLAR AUDIT.

**[Clarification]** Standing. In this exemplar, the L0 object is the semantic definition used for Autonomous. IEEE/IEC source definitions and standards retain their external source provenance at L7/provenance. A direct peer relation is represented at L7/peering only where this exemplar actually maintains one. Historical internal use remains reconstructable through L6.

---

## L1 — STATE SPACE

Admissible states and static possibility bounds.

| **Core question** | What states and distinctions are possible or admissible under the established L0 contract? |
|---|---|
| **Function** | Freeze the board: dimensions, admissible states, invariants, exclusions, equivalence/identity conditions, and static compatibility. |
| **Directional inputs** | Construction: the current L0 contract. Inspection: higher-layer evidence may trigger a question or proposed revision, but cannot silently change admitted states. |
| **Output** | An L1 state-space contract defining what L2 may represent and operate upon. |
| **Hard boundary** | No carrying, transition, selection, learning, calculation, propagation, or transformation. Formal operation begins at L2. |
| **Machine metadata** | Machine-readable metadata may identify the state-space version, pinning/immutability status, admission checks, and compatibility validation. It may enforce the frozen board, but it does not create the states or their meaning. |

| **Owns / represents** | **Permitted actions** | **Acceptance / boundary check** |
|---|---|---|
| • admissible and excluded states<br>• dimensions, domains, ranges, equivalence classes, identity conditions<br>• static invariants and compatibility constraints | • admit, exclude, distinguish, bound, freeze<br>• test state membership and compatibility<br>• issue a new version when the possibility landscape changes | • Every admitted state is grounded in L0.<br>• Invariants are mutually compatible or the collision is explicit.<br>• Changes return to L1 and create a new version. |

**Directory structure**

```text
L8/L1/0
└── state-space/0
```

**[Boundary Rule]** **Boundary / traversal rule.** L1 establishes the admissible state space. Formal operation begins at L2.

**Directory prose and rationale**

| **Directory / thing** | **Prose** | **Why** |
|---|---|---|
| **L8/L1/** | Layer 1 container for the admissible state-space representation grounded in L0. | Keeps static possibility separate from the formal operations that begin at L2. |
| **state-space/** | Directory for admissible and excluded states, dimensions, invariants, identity conditions, and static compatibility. | Establishes what may exist or be represented before lawful operation is introduced. |

In the case of: State-space containment and scientific claim boundaries

### State-space boundary — leaving the declared state space

A valid object or transition must remain inside the declared state space and its admissibility rules.

If a result falls outside the declared state space, then either:

1. the construction is invalid under the current model; or
2. the current state space is incomplete for the phenomenon, and a new explicitly justified extension must be proposed.

The model may not silently step outside its state space and still claim continuity with the same system.

### Mathematical permission is not automatic scientific or engineering permission

A mathematical construction is allowed to remain mathematically valid even when no engineering realization exists.

The construction stops at the first unresolved required bridge.

That is not rejection. It is honest placement.

Example used in session: peer-reviewed FTL/warp-drive mathematics may be legitimate mathematics while still lacking an engineering bridge. The math can stay where it is. It does not receive a free promotion into realizable propulsion.

### No exotic capability gets a free explanatory advantage

FTL, unlimited power, perfect information, zero latency, infinite endurance, and similar assumptions may be studied conditionally.

They may not be used as free empirical resources unless the capability itself carries its own evidentiary and engineering burden.

The session rule became:

> Build whatever the math permits. Claim only what the layer has earned.

### Observable science is bounded without forbidding speculation

The architecture is not anti-speculation.

Hypotheses may be created and mathematically explored.

The discipline is that unobserved or unengineered capability cannot be silently promoted downward into the foundational or physical claim space.

State-space and claim boundaries

An object or formal operation may not silently leave the declared state space and still claim continuity with the same L1 contract. An out-of-space result either fails under the current model or motivates an explicit proposal for a revised state space.

Mathematical permission is not automatic engineering or empirical permission. A mathematically valid object may stop at L2. Engineering feasibility must be earned at L3, realized work at L4, and scientific interpretation at L5. Packaging or publicity at L7 never promotes maturity by itself.

The architecture therefore permits speculation while making maturity explicit: build whatever the mathematics legitimately permits; claim only what the completed handoffs have earned.

**[Note]** Author note. STATE and IMMUTABLE remain useful descriptive/mnemonic language, but the controlling layer name is State Space.

---

## L2 — FORMAL MATHEMATICS

Exact formal objects and lawful operation over L1.

| **Core question** | What follows exactly when lawful operations are defined over L1? |
|---|---|
| **Function** | Define notation, types, relations, operators, constructors, carriers, exact models, derivations, and proof obligations. |
| **Directional inputs** | Construction: the L1 state-space contract. Inspection: higher-layer work may expose a formal obligation, but the L2 object must still be stated over L1. |
| **Output** | An exact L2 formal contract supplying L3 with behavior, invariants, formulas, and unresolved proof obligations. |
| **Hard boundary** | No engineering tolerance, approximation quality, physical realization, measurement, or empirical truth is claimed here. |
| **Machine metadata** | Machine-readable metadata may identify formal artifact type, dependencies, proof/test status, domain/codomain pointers, and execution restrictions. It assists machines without replacing the formal or semantic statement. |

| **Owns / represents** | **Permitted actions** | **Acceptance / boundary check** |
|---|---|---|
| • formal symbols and types<br>• relations, functions, operators, gates, constructors, carriers, transition systems<br>• axioms, definitions, lemmas, theorems, derivations, exact formulas | • formalize, derive, prove, type-check, construct, test closure<br>• declare domain/codomain/partiality<br>• mark conjectural or unproved claims explicitly | • Every symbol binds to L0 meaning and L1 admissibility.<br>• Every operation has declared domain/codomain or partiality.<br>• Exact results are supported by proof/derivation or marked as unproved. |

**Directory structure**

```text
L8/L2/0
└── formal-mathematics/0
    ├── relations/0
    ├── operators/0
    └── proofs/0
```

**[Boundary Rule]** **Boundary / traversal rule.** Engineering tolerance, numerical approximation, and numerical uncertainty belong to L3, not to L2 exact formal ownership.

**Directory prose and rationale**

| **Directory / thing** | **Prose** | **Why** |
|---|---|---|
| **L8/L2/** | Layer 2 container for exact formal representation and lawful operation over L1. | Separates exact mathematical structure from engineering approximation and empirical realization. |
| **formal-mathematics/** | Directory for the exact formal system: symbols, types, models, derivations, and obligations. | Keeps formal mathematics grouped under one exact owner before engineering choices are introduced. |
| **relations/** | Directory for exact relations among admitted formal objects. | Keeps relational structure distinguishable from the operators that act and the proofs that warrant claims. |
| **operators/** | Directory for exact operators, functions, gates, constructors, and other lawful formal actions. | Keeps operation explicit rather than burying it inside prose or engineering implementation. |
| **proofs/** | Directory for proofs, lemmas, derivations, and explicit unproved obligations. | Keeps warrant for exact claims inspectable and separate from the claim’s notation or later numerical realization. |

**[Note]** Author note. Current correction: “finite tolerance” is not an L2 ownership rule. Engineering tolerance and numerical uncertainty belong at L3.

---

## L3 — ENGINEERING MATHEMATICS

Approximation, numerical representation, tolerance, uncertainty, and feasibility.

| **Core question** | How can the exact L2 relation be made feasible under declared constraints? |
|---|---|
| **Function** | Translate formal behavior into implementable numerical/engineering methods with explicit units, precision, approximation, tolerance, uncertainty, complexity, and operating regions. |
| **Directional inputs** | Construction: the L2 formal contract plus declared environmental, resource, and performance constraints. Inspection: L4 evidence may force re-evaluation without silently changing L2. |
| **Output** | An L3 engineering specification telling L4 what can be built/run and within what conditions. |
| **Hard boundary** | L3 is not the realized L4 output and does not itself create empirical evidence. |
| **Machine metadata** | Machine-readable metadata may identify units, precision, approximation profile, tolerance/uncertainty bounds, implementation target, and validation conditions. It carries machine constraints while /0 carries the human semantic description. |

| **Owns / represents** | **Permitted actions** | **Acceptance / boundary check** |
|---|---|---|
| • algorithms and abstract data-structure choices<br>• units, numerical representation, precision, approximation, discretization, tolerance<br>• error/uncertainty budgets, sensitivity, stability, convergence, complexity<br>• simulation, optimization, feasibility arguments | • approximate, discretize, optimize, estimate, bound error, choose representation<br>• compare candidate methods to L2 invariants<br>• state operating assumptions and valid region | • Error/uncertainty, units, precision, and tolerance are explicit.<br>• Required L2 invariants are preserved within declared bounds.<br>• Resource/complexity claims are analyzed or labeled estimates. |

**Directory structure**

```text
L8/L3/0
└── engineering-mathematics/0
    ├── approximation/0
    ├── uncertainty/0
    └── tolerances/0
```

**[Boundary Rule]** **Boundary / traversal rule.** L3 owns engineering approximation and feasibility; it does not own the realized L4 output.

**Directory prose and rationale**

| **Directory / thing** | **Prose** | **Why** |
|---|---|---|
| **L8/L3/** | Layer 3 container for numerical and engineering feasibility applied to the L2 formal contract. | Separates implementable approximation and constraint handling from exact L2 mathematics and realized L4 work. |
| **engineering-mathematics/** | Directory for algorithms, numerical representation, units, precision, feasibility, stability, and complexity. | Keeps the engineering translation of exact formal behavior explicit and inspectable. |
| **approximation/** | Directory for approximations and discretizations used to make exact relations workable. | Makes loss or approximation visible instead of letting it appear as exact mathematics. |
| **uncertainty/** | Directory for uncertainty and error characterization associated with an engineering representation. | Keeps uncertainty explicit rather than silently absorbing it into a result. |
| **tolerances/** | Directory for declared tolerances and admissible engineering bounds. | Keeps acceptance bounds separate from the exact L2 relation they approximate or implement. |

### Working life boundary hypothesis

L2 may formalize exact relations about life, but L2 does not mathematically support life.

Mathematics that depends on continuation, tolerance, uncertainty, adaptation, feedback, or environmental exchange begins at L3. L4 realizes or records the resulting conversion.

**[Clarification]** This boundary remains a research hypothesis until tested.

**[Note]** Author note. INFINITE is retained as a working term for open-ended tolerance/refinement across implementations and time, not as permission to move exact L2 objects here.

---

## L4 — LAYER 4

Conversion / realized work / identifiable output.

| **Core question** | What conversion between intellectual property and energy, in either direction, was actually made, written, run, measured, instantiated, operated, manufactured, or recorded? |
|---|---|
| **Function** | Own Conversion: any intellectual property to energy, or energy to intellectual property. Commit resources to realize an intellectual object, or capture an energetic event, work, or failure as an identifiable intellectual object. |
| **Directional inputs** | Construction: pinned L3-L0 contracts plus resources required for conversion. Inspection: realized output or failure returns evidence upward; L7 authority or release status is not a scientific construction dependency. |
| **Output** | An audit-ready conversion product or recorded failure with traceable inputs, transformations, conditions, tests, results, and rework. |
| **Hard boundary** | L4 does not authorize its own L5 interpretation and cannot flatten lower contracts into a convenience summary. |
| **Machine metadata** | Machine-readable metadata may identify build/run instructions, environment, resource requirements, inputs/outputs, integrity checks, permissions, and fault routing for realized work. It does not supply the L5 interpretation of the result. |

| **Owns / represents** | **Permitted actions** | **Acceptance / boundary check** |
|---|---|---|
| • IP-to-energy realization: writing, models, toys, computation, code execution, experiments, integration, transport, deployment, operation, and manufacturing.<br>• Energy-to-IP capture: observations, measurements, records, datasets, failures, and other identifiable intellectual objects.<br>• A contained architecture, including an OSI stack, as actually specified, made, taught, tested, or operated. | • make, write, code, run, measure, test, collect, integrate, convert, store, transport, deploy, manufacture<br>• verify conformance and rework against the governing input contract<br>• record result or failure without converting it into a conclusion | • Governing lower dependencies are pinned and resolvable.<br>• A distinguishable IP/energy conversion output or recorded failure exists.<br>• Inputs, conditions, transformations, results, and evidence remain traceable.<br>• L4 existence does not authorize its own L5 interpretation. |

**Directory structure**

```text
L8/L4/0
└── work/0
    ├── writing/0
    ├── experiments/0
    └── computation/0
```

**[Boundary Rule]** **Boundary / traversal rule. Writing belongs to L4 as performed work. Its research meaning belongs to L5; a released publication belongs to L7. Contained architectures may expand internally without changing their 7LM owner. When the question is how the OSI architecture operates, the complete OSI L1-L7 stack remains inside 7LM L4, and OSI L7 is not 7LM L7. When the question instead concerns OSI origins, development, justification, standardization, or design constraints, the inquiry may expand across the appropriate 7LM layers without remapping the OSI stack itself. An OSI network fault is therefore an L4 operational fault unless separately shown to affect another layer's owned object.**

**Directory prose and rationale**

| **Directory / thing** | **Prose** | **Why** |
|---|---|---|
| **L8/L4/** | Layer 4 container for performed and realized work that returns an identifiable output or recorded failure. | Keeps the event of making or doing distinct from the later L5 interpretation of what the result means. |
| **work/** | Directory for traceable realized work governed by pinned lower-layer dependencies. | Provides one place for the performed event without flattening the L3-L0 package that governs it. A complete internal architecture, including OSI, remains an L4 object even when it has its own internal layers. |
| **writing/** | Directory for writing and document production as performed work. | Distinguishes making the document from its L5 research meaning and its L7 released publication. |
| **experiments/** | Directory for experiments as actually executed, including observations, measurements, tests, and failures. | Distinguishes performed experiment from L3 measurement design and L5 interpretation. |
| **computation/** | Directory for computation as actually run, including executable processing and recorded outputs or failures. | Separates executed computation from the formal L2 relation and engineering L3 method that specify it. OSI application and network layers remain execution detail inside L4; OSI L7 is not the 7LM Surface / Peering layer. |

### L4 conversion rule

Any intellectual property to energy, or energy to intellectual property.

IP to energy: an intellectual object is made operative through writing, computation, experiment, integration, transport, deployment, teaching, operation, or manufacturing.

Energy to IP: an energetic event, operation, measurement, observation, success, or failure is captured as an identifiable intellectual object.

A toy, model, OSI stack, writing event, computation, manufactured thing, or full system can be L4. Role remains decisive: an exact model may be L2, its engineering realization may be L3, the model as made or operated is L4, and its research meaning is L5.

**[Research Note]** MOST IMPORTANT: THE CUT LIVES HERE

**[Clarification]** Standing. The cut is the realization boundary: L3 and below specify what is admissible, exact, or engineerable; L4 is where resources are committed and an identifiable work product, measurement, execution, or failure is produced.

#### In the case of:

Cross-layer activity cases

| **Case** | **Placement rule** |
|---|---|
| **Research** | L5 owns interpretation/review; L6 preserves internal memory/history; L7 owns external provenance and exposes permitted presentations; L4 performs research work events; lower layers own their specific representations. |
| **Writing** | The act/file production is L4. The research argument is L5. Internal version and correction history are L6. Public provenance, governance, and the released publication are L7. |
| **Experiment** | Executed experiment, observation, measurement, and raw work product are L4; engineering method/tolerance L3; exact relations L2; possibilities L1; interpretation/conclusion L5. |
| Contained architecture (OSI) | Operationally, the full OSI L1-L7 architecture remains an L4 object. Questions about its origins, development, justification, standards history, or design constraints may be railed through other 7LM layers; this analytic expansion does not remap OSI layers to 7LM layers. |
| **Code** | Algorithmic/engineering representation can be L3; formal proof/model L2; execution, deployed bytes, storage, interfaces, and operational result L4. |
| **Data** | Collected/stored instances and transformations are L4; engineering representation/precision L3; formal encoding may be L2; state categories L1; external source/lineage is L7 provenance; internal development history is L6; interpretation is L5. |
| **External-source definition** | When the bounded object uses the definition as part of its semantic contract, that semantic role is L0 regardless of who authored the source. Source/version/authority/prior-art relations are L7 provenance where relevant; applicable legal/access conditions are L7 governance; a peer relationship is L7 peering only when such a relationship actually exists; internal use history may be L6; interpretation is L5. |
| **Publication** | Production is L4; scholarly/research meaning is L5; internal history is L6; provenance, public/legal governance, and the released publication object are L7. |

**[Note]** Author note. Writing is L4 as work. An exemplar/model/thesis/file is made here; its research meaning may be L5 and its released publication may be L7.

### Auditonomous academic-book traversal

L0 owns the locally authored Auditonomous definition.

L1 owns the Auditonomous state space.

L2 may own exact formal relations or proofs about the project when actually established, but it does not support life or own the project's formulas for life.

L3 owns the project's formulas for life when they are applied, open-ended, constrained, approximate, or engineering formulas.

L4 owns the Auditonomous model as made, written, instantiated, or operated, including production of the book artifact.

L5 owns the book's research argument, interpretation, and teaching.

L6 owns the reconstructable development, correction, failure, and supersession history.

L7 owns release and publication of the academic book and the peer binding to the separately owned Autonomous definition.

Separate layer-owned representations overlay the same bounded subject.

The L4 Auditonomous model does not contain the L1 state space or L3 formulas as its own layer contents; it is governed by and related to those separately owned representations.

Overlay does not collapse ownership or duplicate the whole book at every layer. A peer definition may reach the receiving L0 through the two L7 faces while remaining an immutable, externally authored binding.

---

## L5 — RESEARCH / DISCOURSE

Interpretation, review, judgment, argument, and teaching.

| **Core question** | What may responsibly be concluded, questioned, taught, compared, or decided from the available work? |
|---|---|
| **Function** | Frame questions, interpret evidence, evaluate claims, conduct review, govern research decisions, and communicate scientific meaning. |
| **Directional inputs** | Construction: L4 work/evidence plus relevant L3-L0 contracts. Inspection/query: questions may enter from L7; they frame inquiry but do not create lower-layer facts. |
| **Output** | A bounded claim/decision with cited dependencies, limitations, review status, and reproducibility information for L6 retention and L7 presentation. |
| **Hard boundary** | Consensus, prose, authority, or usefulness cannot substitute for proof, measurement, or a lower-layer fact. |
| **Machine metadata** | Machine-readable metadata may identify workflow state, ACL/role constraints, review status, routing, institutional access, and release readiness. These instructions govern machine handling; they do not create the research meaning. |

| **Owns / represents** | **Permitted actions** | **Acceptance / boundary check** |
|---|---|---|
| • research questions, hypotheses, rationale, analyses, interpretations, findings<br>• literature search and relevance judgment<br>• claim scope, limitations, uncertainty, explanation, conclusion<br>• review, audit, research governance, teaching, manuscript meaning | • compare claim to evidence; interpret; criticize; accept/reject/qualify/supersede<br>• request revision from a lower owner without silently mutating it<br>• prepare a claim for preservation and presentation | • Claim is no broader than evidence/maturity.<br>• Methods, exclusions, uncertainty, and inferential limits are disclosed.<br>• Research meaning is distinguished from L4 writing and L7 release. |

**Directory structure**

```text
L8/L5/0
├── research/0
│   ├── lanes/0
│   ├── review/0
│   └── findings/0
└── institution/0
    ├── peers/0
    └── undergraduates/0
```

**[Boundary Rule]** **Boundary / traversal rule.** L5 may interpret externally owned definitions, but interpretation does not transfer ownership of the peer definition into L0.

**Directory prose and rationale**

| **Directory / thing** | **Prose** | **Why** |
|---|---|---|
| **L8/L5/** | Layer 5 container for research interpretation, review, judgment, argument, research governance, and teaching. | Keeps scientific meaning and decision distinct from the L4 work product and the L7 presentation surface. |
| **research/** | Directory for the active research record and discourse owned at L5. | Keeps inquiry and interpretation separate from institutional participant structure. |
| **research/lanes/** | Directory for distinct lines of inquiry within the research record. | Prevents separate questions or investigative paths from being collapsed into one undifferentiated research stream. |
| **research/review/** | Directory for review, criticism, audit, and qualification of research claims. | Keeps review activity distinguishable from the findings being reviewed. |
| **research/findings/** | Directory for findings that may responsibly be stated from the available work and evidence. | Keeps stated findings tied to L5 judgment rather than treating raw L4 output as a conclusion. |
| **institution/** | Directory for the institutional research setting and participant positions. | Keeps the social/institutional setting distinct from the research record itself. |
| **institution/peers/** | Directory for peer participant positions within the institutional setting. | Keeps peer participation distinct from other institutional roles. |
| **institution/undergraduates/** | Directory for undergraduate participant positions within the institutional setting. | Keeps undergraduate participation distinct from peer and research-owner roles. |

#### In the case of:

**[Research Note]** Forward-facing discourse forums, chat, and institutional documentation may allow fellows or participants to operate under a shared institutional identity while access controls separate participant roles and lower-layer discourse backends.

**[Clarification]** Standing. A forum or chat interface may be realized operationally at L4 and exposed at L7, while institutional roles, discourse, interpretation, review, and research meaning carried through it remain L5-owned. L7 governance concerns the external/public legal and access relation, not scientific judgment.

**[Note]** Author note. External definitions can be interpreted here. Interpretation does not transfer ownership of the peer definition into L0.

**[Clarification]** The catch-all. research/review/ is also where everything awaiting the owner's review lands, however much of it there is. What the owner sets aside stays there labelled PARKED. What the owner takes up moves to research/lanes/, the working position, and back if set down again. Finished work is filed at its layer. Nothing is deleted. No other position and no new directory is needed for this.

**[Clarification]** A scale, a ladder, or a vocabulary of levels or statuses is semantics of layer 4 and up: as written it is an L4 object, and what it means is L5 discourse. It is not an L1 state space and not L2 mathematics. A ladder of review statuses is research governance and stands at L5, not at the L0 epistemic rail.

---

## L6 — LIBRARY

Memory, history, reconstruction, retirement, and query orientation.

| **Core question** | Can the object's internal history, prior states, failures, corrections, and retirement be reconstructed and correctly oriented for inspection? |
|---|---|
| **Function** | Preserve internal memory, prior versions, branch history, corrections, failures, supersession, retirement, ledgers, and reconstructable relations without re-owning external provenance. |
| **Directional inputs** | Construction: versioned artifacts and relations from L5 through L0. Inspection/query: L7 boundary events orient reconstruction; external provenance remains owned at L7. |
| **Output** | A reconstructable Library record identifying the relevant prior state, branch, correction, failure, supersession, retirement, and internal relation needed for inspection or reproduction. |
| **Hard boundary** | L6 records, preserves, and orients; it does not make the L5 research judgment or establish truth. |
| **Machine metadata** | Machine-readable metadata may identify retention, archival, retirement, supersession, reconstruction, and integrity instructions for memory/history. References to external provenance resolve to L7 rather than being re-owned by L6. |

| **Owns / represents** | **Permitted actions** | **Acceptance / boundary check** |
|---|---|---|
| - prior internal states and versions<br>- branch history and decision history<br>- failed paths and unresolved obligations<br>- corrections, supersession, retirement, and retained memory | - record, preserve, compare, branch, supersede, retire, reconstruct<br>- retain prior classifications and corrections without erasure<br>- orient inspection before entering the active payload | - Prior internal states and changes are reconstructable.<br>- Correction does not require deletion of prior state.<br>- External source/provenance references resolve back to L7.<br>- Retirement preserves the record rather than erasing it. |

**Directory structure**

```text
L8/L6/0
├── history/0
└── retired/0
```

**[Boundary Rule]** Boundary / traversal rule. For an externally encountered object, L7 is the boundary and owns its external provenance/governance relation. L6 is the first interior layer used to reconstruct prior internal states, changes, failures, supersession, and retirement before deeper inspection.

**Directory prose and rationale**

| **Directory / thing** | **Prose** | **Why** |
|---|---|---|
| **L8/L6/** | Layer 6 Library container for internal memory, history, prior states, failures, corrections, supersession, retirement, and reconstruction. | Keeps reconstructable scientific memory inside the USO while external provenance and public/legal relations remain on the L7 forward face. |
| **history/** | Directory for prior states, branch history, corrections, failures, unresolved paths, and reconstructable development over time. | Preserves how the object changed instead of presenting only the latest state. |
| **retired/** | Directory for retired or superseded internal states or relations that are no longer current. | Keeps prior states separately reconstructable when they no longer represent the current object. |

### Git and scientific memory

Git history can support L6 reconstruction, but Git history and scientific memory/provenance are not the same object. Git records repository change events; L6 must preserve the scientific relations, decisions, failures, corrections, versions, and retirement needed for reconstruction. External source, authority, and prior-art provenance remain L7-owned.

**[Clarification]** L6 requires reconstructability of the internal history it claims to preserve; it does not prescribe one storage or deletion policy. A repository may preserve prior states through retained files, version-control history, explicit retirement records, archival storage, or another method adequate to reconstruction. In this repository, Git history and L6 records are used together as an implementation choice. Reconstructability is the architectural function; the retention mechanism is not.

**[Note]** Author note. When full interpretation begins outside the object, L7 is encountered first and L6 is the first interior layer. Interior-only inspection can therefore be described as beginning at L6.

---

## L7 — SURFACE / FORWARD FACE

External provenance, public/legal governance, peering, publications, exposure, and exchange.

| **Core question** | What provenance, governance, peer relation, publication, or other external representation must exist at the object's forward face? |
|---|---|
| **Function** | Provide the external Surface on which provenance, governance, peering, and outward acts can be represented without changing the scientific meaning owned by the interior. |
| **Directional inputs** | Relations may be directed toward the bounded object, away from it, or describe an external condition without directional exchange. Peering direction is stated relative to the bounded object; direction alone does not imply acceptance, release, or internal scientific use. |
| **Output** | An addressable external relation: provenance, governance condition, peer relation, or outward act, stated only to the extent required by that representation. |
| **Hard boundary** | L7 owns external relations, not lower-layer scientific meaning. Presence, publication, copyright, patent status, exposure, custody, provenance, or peering does not make an object valid, complete, true, adopted, or internally authored. |
| **Machine metadata** | Machine-readable metadata may identify provenance, governance, visibility, ingress/egress direction, peer/object identity, release state, permissions, and implementation-specific handling conditions. Metadata describes or enforces an implementation contract; it does not define scientific meaning. |

| **Owns / represents** | **Permitted actions** | **Acceptance / boundary check** |
|---|---|---|
| - provenance: prior art, sources, lineage, authority<br>- public/legal governance: copyright, licensing, patents, permissions, access, controlled<br>- peering: public/private exposure, ingress/egress direction, peer/object relation<br>- allications: outward acts, of which publication is one | - represent and distinguish external relations<br>- identify source and provenance relations<br>- state governance conditions where relevant<br>- identify peer counterpart, exposure, and direction<br>- represent outward acts and releases | - Each L7 record states only the external relation it owns.<br>- Peering does not silently determine authorship, acceptance, truth, or interior layer ownership.<br>- Public/private and ingress/egress remain independent peering coordinates.<br>- Publication or legal status does not strengthen scientific evidence.<br>- Unused canonical branches may remain empty without implying failure. |

**Directory structure**

```text
L7/0
├── provenance/0
│   ├── prior-art/0
│   ├── sources/0
│   ├── lineage/0
│   └── authority/0
├── governance/0
│   ├── copyright/0
│   ├── licensing/0
│   ├── patents/0
│   ├── permissions/0
│   ├── access/0
│   └── controlled/0
├── peering/0
│   ├── private/0
│   │   ├── ingress/0
│   │   │   └── peer-1/0
│   │   │       └── object-1/0
│   │   └── egress/0
│   │       └── peer-1/0
│   │           └── object-1/0
│   └── public/0
│       ├── ingress/0
│       │   └── peer-1/0
│       │       └── object-1/0
│       └── egress/0
│           └── peer-1/0
│               └── object-1/0
└── allications/0
    ├── publications/0
    ├── applications/0
    ├── communications/0
    ├── specifications/0
    ├── notifications/0
    └── participations/0
```

**[Boundary Rule]** Boundary / traversal rule. L7 is the forward face outside the USO. It owns the external relations of the bounded object: provenance, governance, peering, and allications — the outward acts, of which publication is one. Public/private exposure and ingress/egress direction remain independent peering distinctions. L7 does not thereby acquire or change the lower-layer scientific meaning.

#### Peering as an agnostic external relationship

Peering answers one question: **with what identifiable external counterpart is the bounded object relating, through what exposure and direction, and what object or interaction is distinguished in that relation?**

```text
L7/peering/
├── private/
│   ├── ingress/peer-1/object-1/
│   └── egress/peer-1/object-1/
└── public/
    ├── ingress/peer-1/object-1/
    └── egress/peer-1/object-1/
```

Public/private and ingress/egress are independent coordinates.

- **Public** means the relationship is exposed through a public-facing channel.
- **Private** means the relationship is exposed through a restricted channel. Private remains an auditable L7 relation; the audience of inspection is restricted rather than public.
- **Ingress** means the relationship is directed from the external counterpart toward the bounded object.
- **Egress** means the relationship is directed from the bounded object toward the external counterpart.

Here **auditable** means that the represented relationship can be identified and inspected by the audience to which the channel is exposed. 7LM does not prescribe an audit procedure, legal regime, or access-control implementation.

`peer-N/` identifies one external counterpart within the local peering channel. `object-M/` identifies one object or interaction within that peer relation. The numbers distinguish local instances; they do not by themselves establish rank, authority, chronology, ownership, version, status, or cross-channel identity.

Peering does not, merely by representing a relationship, establish authorship, ownership, acceptance, rejection, adoption, provenance, permission, truth, scientific validity, or internal layer ownership.

[
	ext{peering}=	ext{represented relationship across the boundary}
]

[
	ext{external relation}\neq	ext{scientific meaning}
]

[
	ext{external source}\not\Rightarrow	ext{peer}
]

A source encountered through a book, archive, database, article, search engine, or standards collection may be represented through provenance without peering when no counterpart relationship itself is being represented.

**[Note]** Author note. The agnostic L7 topology carries admissible external-facing capabilities even when a project does not use them.

#### Instructional peering exemplars

These examples teach the coordinates; they do not create additional requirements.

**High-school research.** A student sends a draft to a teacher through a restricted course channel: private egress. The teacher returns comments: private ingress. Whether the student adopts the comments is not decided by peering.

**College laboratory.** A collaborating laboratory privately returns a calibration dataset: private ingress. A later public repository discussion with that laboratory can be represented separately through public peering.

**Peer-review preparation.** A manuscript sent through a restricted journal submission system is private egress. Reviewer comments returned through that system are private ingress. Later publication, if it occurs, is represented separately as a publication act.

**Public external interaction.** An external researcher opens a public repository issue: public ingress. A public response directed to that researcher is public egress. Neither interaction becomes a publication merely because it is visible.

**External source without peering.** A researcher adopts a definition discovered in a published source through a web search. The semantic use may belong at L0 and the source relation at provenance. Peering is not required unless the relationship to an identifiable external counterpart is itself being represented.

#### Originating Autonomous/Auditonomous exemplar

The Autonomous/Auditonomous case historically motivated the need to represent one bounded research object in explicit relation to another. In that exemplar, the source exposes an exact definition through public egress and the receiver represents it through public ingress. The exemplar also chooses version pinning, external-source tagging, and reference-only handling.

Those handling choices remain valid **for that exemplar**. They do not define peering generally, and another 7LM use may represent a completely different kind of peer relation.

**[Clarification]** The originating exemplar demonstrates one use of the architecture. It does not control the architecture.

**Directory prose and rationale**

| **Directory / thing** | **Prose** | **Why** |
|---|---|---|
| **L7/** | External Surface / forward-face container outside the USO where the bounded object meets external people, institutions, systems, repositories, legal/public conditions, publications, and data sources. | Keeps external relations separate from the scientific interior while giving those relations an explicit owner. |
| **provenance/** | Directory for the external provenance of the bounded object: where it came from, what preceded it, what source/version is being used, and what authority is being represented. | Places externally meaningful source and lineage information at the forward face rather than burying it inside internal memory. |
| **provenance/prior-art/** | Directory for identified prior art and antecedent work relevant to the bounded object. | Makes the antecedent landscape explicit without confusing prior art with the object's L0 meaning. |
| **provenance/sources/** | Directory for source identity and exact source/version references. | Keeps source identification inspectable at the external face. |
| **provenance/lineage/** | Directory for externally relevant lineage and derivation relationships. | Makes origin and relation traceable without turning lineage into scientific validity. |
| **provenance/authority/** | Directory for represented source or issuing authority associated with an external object or record. | Distinguishes who issued or speaks for an external object from what the local research concludes about it. |
| **governance/** | Directory for public/legal/custodial conditions attached to externally exposed or received objects. | Separates legal and access conditions from provenance, peering direction, publication, and scientific judgment. |
| **governance/copyright/** | Directory for copyright-related representation when applicable. | Copyright governs external use of an artifact; it does not change the artifact's scientific meaning. |
| **governance/licensing/** | Directory for licensing terms or status when applicable. | Keeps conditions of use explicit at the external face. |
| **governance/patents/** | Directory for patent-related representation when applicable. | Provides an agnostic forward-face position for patent status or materials without requiring every project to use it. |
| **governance/permissions/** | Directory for explicit permissions attached to external use, disclosure, or exchange. | Keeps permission separate from ownership and scientific validity. |
| **governance/access/** | Directory for access conditions applicable to externally facing objects. | Makes who may access an object a boundary condition rather than an internal scientific claim. |
| **governance/controlled/** | Directory for restrictions and other conditions that constrain external disclosure, use, transfer, or handling. | Keeps what is controlled explicit without redefining the underlying research. |
| **peering/** | Directory for identifiable relationships between the bounded object and external counterparts. | Makes the relationship itself addressable without turning it into scientific meaning or a universal intake protocol. |
| **private/** | Restricted-exposure peering channel. | Keeps restricted exposure distinct from direction while remaining auditable to its exposed audience. |
| **private/ingress/** | Restricted-exposure inbound peering position. | Describes an external relation directed toward the bounded object without implying acceptance or adoption. |
| **private/egress/** | Restricted-exposure outbound peering position. | Describes an external relation directed outward without implying publication. |
| **public/** | Public-exposure peering channel. | Keeps public exposure distinct from direction and publication. |
| **public/ingress/** | Public-exposure inbound peering position. | Describes a publicly exposed relation directed toward the bounded object. |
| **public/egress/** | Public-exposure outbound peering position. | Describes a publicly exposed relation directed toward an external counterpart; publication remains separately representable. |
| ***/peer-1/** | One external counterpart distinguished within a peering channel. | Keeps counterpart identity distinct from each object or interaction; numbering is local and carries no rank or authority. |
| ***/peer-1/object-1/** | One object or interaction distinguished within a peer relation. | Allows multiple interactions with one counterpart without using the object number as ownership, status, or acceptance. |
| **allications/** | Directory for the bounded object's outward acts: publications, applications, communications, specifications, notifications, participations. | Keeps outward acts addressable as acts rather than collapsing them into peering. |
| **allications/publications/** | Directory for released publication objects at the forward face. | Keeps publication release at L7 while writing remains L4, research meaning remains L5, and internal history remains L6. |
| **allications/applications/** | Directory for applications the object makes outward. | Distinguishes an application act from a peer relation or publication. |
| **allications/communications/** | Directory for communications the object issues outward. | Distinguishes communication as an outward act. |
| **allications/specifications/** | Directory for specifications issued outward. | Distinguishes an issued specification from the relationship through which it may travel. |
| **allications/notifications/** | Directory for notices the object issues outward. | Distinguishes notification as an outward act. |
| **allications/participations/** | Directory for the object's participation in external settings. | Distinguishes participation from a particular peer exchange. |

### Forward-face model

L7 is the desk: the current external surface where finished work, external relations, provenance, governance, peering, and allications become addressable without moving their scientific meaning out of the USO.

Conceptual distinctions include consumer <-> product; customer <-> service; request <-> response; need <-> offer; incoming interaction <-> outgoing interaction; and restricted exposure <-> public exposure.

Presence on the desk establishes nothing by itself. Provenance, custody, authority, copyright, patent status, permissions, internal consistency, and publication each answer different questions; none of them alone establishes scientific truth.

#### Standing rules

L7 describes external relations; it does not acquire the scientific authority of the interior merely because an object is present at the surface.

Peering describes a relationship. It does not itself prescribe ownership, authorship, immutability, acceptance, review status, handling, or lifecycle. Those properties may be represented elsewhere when they matter or may belong to a specific exemplar or implementation contract.

Public/private describe exposure. Ingress/egress describe direction. Neither pair establishes scientific validity.

An external source is not automatically a peer. Peering is used when an identifiable external counterpart relationship is itself part of the represented object.

Material crossing outward may lose fidelity and may never gain scientific maturity merely by being exposed.

An external counterpart does not acquire interior-layer authority merely by being represented at L7.

Machine-readable metadata may support automation, but the architecture does not assume that automation has been enabled or validated.


---

## Exemplars as instantiated

Reference implementations: https://github.com/aybllc/autonomous and https://github.com/aybllc/auditonomous, with the scaffold at https://github.com/aybllc/7lm and the curated-source archive at https://github.com/aybllc/l6.

**[Clarification]** Architecture and implementation status are separate claims. What follows documents the two exemplars as they stand, including what is not yet as this specification states. Their layouts do not control the architecture.

**What both exemplars carry**

- The canonical tree under README.md, L7/, and L8/. Every directory has its 0.md, headed by its path. No directory metadata, no automation in the layout; the one CI check at .github/workflows/integrity.yml, and the same root in both.
- One locally authored L0 definition each. Autonomous owns L0/semantics/definitions/AUTONOMOUS.md, a plural entry of eleven codified definitions A1–A11 carried in verbatim with their issuing bodies' ownership tags. Auditonomous owns L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md, the local delta over the bound Autonomous root.
- The binding of the Autonomous definition at Auditonomous's L7/peering/public/ingress/peer-1/object-1/, reference-only, NO EDIT and NO DELETE, under the owner's rule that Auditonomous gets the definitions of autonomous from Autonomous and nowhere else. Autonomous exposes the definition at its L7/peering/public/egress/peer-1/.
- Curated sources served by pointer from aybllc/l6, bound at each repository's L7/peering/private/ingress/peer-1/; one ledger row per source at L7/provenance/sources/LEDGER.md; no source file in either repository.
- Copyright in one place, L7/governance/copyright/, with licensing/ and restrictions/ (the position this specification now names controlled/) pointing to it.
- L5/research/review/ as the catch-all and L5/research/lanes/ as the working position. The queue that preceded them at the repository roots, orphan, foster, results, delete, with its access rules for sessions, is retired at L6/retired/layout-2026-09-06/ in each repository.
- The records at L6/history/ in each repository, carrying the owner's words verbatim and every move, retirement, deletion, and binding.
- No rule in either tree about what a session or any other intelligence may touch. The repository file that would carry such rules is held off.
- A README that is a start page: the subject, the reading order, the root, and where the prior README is. The evidence rules of Autonomous and the status and label discipline of Auditonomous stand verbatim at L5/research/review/.

**Autonomous** (aybllc/autonomous)

Face. Public ingress peer-1 to peer-9: the issuing bodies whose clauses are bound into the definition, ISO/TC 299, ISO/IEC JTC 1/SC 42, ISO/IEC JTC 1/SC 7, IEEE, NIST, the European Union, US DoD, EASA, and ETSI, one object per bound clause. Public egress peer-1: aybllc/auditonomous, the definition as exposed. Private ingress peer-1 aybllc/l6; peer-2 aybllc/eb-stack with abba-01/ebios; peer-3 aybllc/auditonomous, the coinage, referenced and not adopted; peer-4 the principal's intake corpus. Private egress: none. Provenance: the pointer ledger into l6 and a 450-entry capture register. Publications: a binder; nothing released.

Interior. L6: the master ledger, five forensic reconstructions, the two records, two retired layouts, and four definition error records. L5: six lanes; the reviews, audits, and adjudications; seven findings. L4: the manuscript placeholder, the autonomy scale (an L4 object by the owner's ruling), and one deep-research run. L3: two engineering-mathematics notes. L2: an empty formulas ledger. L1: empty, its dimensions fixed by content inside four L5 findings. L0: the definition with its companions and a universality scope statement.

Not yet as stated. The catch-all holds material that belongs to other objects: Autonomous Theory, one work and not the definition of autonomous, whose home the owner has not named; a template of the Auditonomous definition; and the owner's notes on memory consolidation with conserved uncertainty. Each leaves on the owner's word. The provenance rows for the bound issuing bodies are not yet ledgered. The desk carries the L7 branch names of the version before 20 September 2026, publications/ as a direct branch and governance/restrictions/; the L7 restructure is not yet mirrored.

**Auditonomous** (aybllc/auditonomous)

Face. Public ingress peer-1: aybllc/autonomous, the definition of autonomous, bound at commit 0504961. Private ingress peer-1 aybllc/l6; peer-2 aybllc/eb-audit; peer-3 abba-01/ebios with the Martin 2026 manuscript. Private egress peer-1: the closed transfer of the source corpus to l6; peer-2: the pending transfer of the Third Power Corpus to aybllc/ncf-research, whose files wait at object-1. Public egress: nothing released. Provenance: 62 pointer rows into l6, the staging records about those sources, and one session-provenance record at lineage/. Publications: presentation rules and an empty press-kit checklist.

Interior. L6: the master index, three session ledgers, the two records, two retired layouts. L5: two lanes; two reviews and the status ladder carried verbatim; three findings. L4: drafts, chat transcripts, a session record, three requirements extractions, and one deep-research run with its exports. L3: a proposal and an external-priors note. L2: an empty formulas ledger. L1: the auditon envelope, the substitutability states, and the requirements partition. L0: the one locally authored definition; the other rails empty.

Not yet as stated. The binding of the Autonomous definition names the path the peer used before its own 7LM layout, research/definitions/AUTONOMOUS.md at 0504961; the same object now stands at the peer's L0/semantics/definitions/AUTONOMOUS.md, and rebinding to a current version is the owner's act. The binding record says three files still take a definition of autonomous from somewhere other than the binding. The catch-all holds two Autonomous Theory files that leave once that work's home is named. The L0 epistemic rail is empty; its vocabulary stands at L5 as review status. The desk carries the L7 branch names of the version before 20 September 2026, publications/ as a direct branch and governance/restrictions/; the L7 restructure is not yet mirrored.

**What the exemplars show**

- A second work inside a repository is not the object. Autonomous Theory appeared in both exemplars and is neither's definition; the catch-all holds it until the owner names its home, and the architecture's place for a second work is a repository of its own, met here by peering. Whether it takes that route is the owner's call.
- Position is state. Three motions and no metadata carried the two repositories from a root queue to the catch-all: rename, retire, file. Nothing was deleted.
- The desk is not a layer. Reaching for layer seven hands the reader L6, exactly as the count rule says.
- The tree's silence on access is deliberate. Both repositories ran for one day with the sessions' rules stated in the tree and then removed; nothing in the tree depended on them.

---

## Harmonization Record

Normative authority and non-erasure rule. The principal L0-L7 sheets and the explicit rules in this record control. Harmonization removes stale duplicate contracts but preserves unique research notes, author notes, examples, cases, rationales, hypotheses, and inherited terms. A reserved term remains available for research without manufacturing a directory or layer owner.

Architecture and implementation status are separate claims. The canonical topology declares admissible and owned positions even when a present repository has not instantiated them. Current Autonomous, Auditonomous, and agnostic-method layouts are implementation work in progress and do not rewrite the architecture. Disposition: blank 0.md / status markers remain historical implementation evidence at L6, not architecture.

Supporting-evidence disposition: Git history can support L6 reconstruction, but Git history and scientific memory/provenance are not the same object. External provenance remains L7-owned; internal reconstructable scientific memory remains L6-owned.

### Controlling reserved-state rule

**[Clarification]** Questionable inherited semantics are preserved in their stated or recoverable meaning. Unless a row above expressly ratifies an owner and path, topology remains unadjudicated. No convenience placement in this document settles an open scientific question.

### Inherited terms and their dispositions

| **Inherited term or issue** | **Disposition** | **Controlling harmonization** |
|---|---|---|
| prior-art | Relocated | External antecedents belong at L7/provenance/prior-art/. |
| definitions | Revised | Definitions that function in the bounded object's semantic contract belong at L8/L0/semantics/definitions/ regardless of source authorship. External source relations belong to provenance where relevant; peering applies only when an identifiable counterpart relationship is represented. |
| semantic-formulas | Split and reserved | Semantic reading remains L0; an exact formula is L2; an applied, tolerant, adaptive, or engineering formula is L3. The inherited compound term remains searchable. |
| thesis-statements | Relocated | Research claims and thesis statements belong at L8/L5/research/lanes/ or the corresponding L5 research artifact. |
| origidity; certainty; intolerance | Reserved | Candidate L1 semantics preserved; topology remains unadjudicated. |
| found; caught; naught | Reserved | caught remains the zero state; found remains the observer role; naught remains the empty or settled state. Their topology remains unadjudicated. |
| regress | Reserved | Preserved as a prior unadjudicated holding concept; active path and owner remain unadjudicated. |
| corpus | Split and reserved | Released corpus/publication identity belongs at L7/allications/publications/; the broader inherited term remains reserved where its exact role is not yet adjudicated. |
| INFRASTRUCTURE | Superseded as L4 name | L4 is Conversion. Infrastructure belongs at L4 only when it is the bounded work or conversion being made; generic repository support is not automatically a layer. |
| DEVOID; IMMUTABLE; FINITE; INFINITE; IDENTITY BY PROSE; RESEARCH MEMORY; SCIENTIFIC DESKTOP | Descriptive | Preserved as historical mnemonics or working language; the principal layer sheets control ownership. |
| L6 provenance | Split | Internal reconstructable memory remains L6; external source, authority, prior art, and public provenance belong at L7/provenance/. |
| USO/ as the directory name of the interior | Renamed L8/ | The term USO remains the name of the bounded scientific object's interior; the directory is L8, the research packet on the desk, a count and not a rank. |
| README.md as documentation | Superseded | README.md is where a reader starts; the sheets and this specification are the documentation. The READMEs that carried documentation were deleted after enumeration, records kept at L8/L6/history/. |
| no deletion as a rule | Superseded | Integrity is enforced; no deletion is implied. Retirement is for what integrity needs reconstructable; deletion after enumeration is the ordinary act, recorded at L8/L6/history/. |
| l0 … l6 as the interior directory names | Superseded | L0 through L6 under L8: the eight bits L0 through L7 and the extra bit L8. |
| orphan; foster; results; delete | Retired | The exemplars' queue vocabulary and the access rules that came with it were retired on the owner's word; L8/L5/research/review/ is the catch-all and L8/L5/research/lanes/ the working position; nothing is deleted. |
| peer-1 / object-1 numbering | Resolved | Peers are physical and are counted from 1; the layers are counted from 0, the semantic origin, where the Semantic and Epistemic rails define the layers above. The owner's ruling of 12 September 2026; the words are at L8/L6/history/specification-history.md. |

The dated lists of what changed in each version stand at L8/L6/history/specification-history.md in the scaffold repository.
