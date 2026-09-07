<!-- Canonical Markdown form of the Seven-Layer Model (7LM) Harmonized Authoritative Architecture Specification,
     version of 7 September 2026. This Markdown is the source; the .docx filed beside it is generated from the text
     below this comment and reads back to it unchanged. The history of versions and changes, with the owner's words
     behind each rule, is at USO/l6/history/specification-history.md. -->

# SEVEN-LAYER MODEL (7LM)

Harmonized Authoritative Architecture Specification

Canonical research directory topology and uniform layer information sheets

*7LM Harmonized Authoritative Architecture Specification • 7 September 2026*

> Authority\
> This specification states the controlling 7LM research architecture: one canonical agnostic directory topology and one uniform information sheet for each layer. The structure, layer boundaries, directory prose, machine-metadata distinction, and stated rationales are authoritative for this research program. Capability branches may remain empty when unused; they remain part of the agnostic topology so a project can instantiate them without changing the architecture.

Version\
Version of 7 September 2026. The history of versions and changes, with the owner's words behind each rule, is at L8/L6/history/specification-history.md in the scaffold repository.

Self-description and machine-instruction rule\
Every directory carries a local Layer 0 semantic description. In tree notation, /0 denotes that directory's local 0.md without drawing the file as a separate branch. The same directory separately carries machine-readable metadata for machine instructions, constraints, permissions, routing, validation, and lifecycle behavior. /0 carries human-readable meaning; metadata carries machine-actionable instruction. Neither replaces the other. This separation keeps semantic description distinct from machine operation.

Direction rule\
Scientific construction proceeds from L0 outward only as dependencies are established. External inspection begins at L7 and proceeds inward. Description does not become prescription merely because the structure can be traversed.

### Originating architectural constraint

The Autonomous/Auditonomous root issue supplies the concrete origin of the agnostic peering rule: one bounded research object must be able to depend on another without owning, copying, redefining, or maintaining both objects' foundational semantics. Auditonomous can use the exact Autonomous definition without becoming a second semantic authority for Autonomous. peer-1/object-1 is the agnostic form of this concrete ownership problem.

**[Clarification]** The Autonomous and Auditonomous repositories are implementation work in progress; their current layouts do not control the architecture. Architecture and implementation status are separate claims.

#### Contextual semantic route

Source L0 definition → source L7 egress → receiving L7 ingress → receiving L0. A source object's L0 definition is an L7 egress object at its boundary; to us it is L7 ingress directed to our L0. Its semantic identity remains source-owned L0 throughout the exchange.

The receiver does not have to redefine the peer definition. Every internal representation that uses it carries the exact bound version with an immutable external-ownership tag: object identity, owner, source layer, version, and ingress binding. An upstream change creates a new binding; it does not mutate the pinned object.

Declared semantic-deference rule. For the bounded purpose of interpreting the peer, the receiver intentionally takes the owner's exact bound definition as authoritative for what the owner means and does not re-prove or locally redefine that meaning. This declared trust is not a claim that the definition is objectively true, not an endorsement of downstream claims, and not a transfer of authorship.

An argument about Autonomous cannot silently stand in for an argument about Auditonomous. A cross-object claim requires an explicit named relation or handoff. The same identity-tagging rule applies to agnostic methods as they are made and carried through the architecture.

Autonomous has one bounded semantic job: state and freeze the narrowest reasonable agreement shared across exact, independently bound standards definitions. It must not manufacture consensus where sources materially disagree; every disagreement remains source-tagged and visible.

Auditonomous consumes the pinned Autonomous consensus baseline and authors the Auditonomous difference as an explicit local delta. The baseline and delta remain separately owned and overlaid rather than blended into a dual-owned definition.

Canonical direct L7 branches are L7/provenance/, L7/governance/, L7/peering/, and L7/publications/.

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

**[Note]** Author note. L7, pronounced El-Seven, is the desk: the L is the lower left hand corner of the desk and the 7 is the upper right; the name draws the rectangle that this layer is, its Surface. L8 is the research packet on the desk: two zeros stacked, the interior's zero over the zeros of the seven layers. The interior directories carry uppercase too: L0 through L7 are the eight bits of a byte, 0 being a bit, and L8 is the extra bit that carries the semantic, as information needs an extra bit to catch any error. The names are design, not decoration, and were not chosen by accident.

### 7LM is a dependency and fault-containment architecture

7LM exists to:

1. separate ontology/semantics from state space, formal mathematics, engineering mathematics, realized work, research judgment, memory/history, and external provenance/governance/peering/publication;
2. pin lower-layer contracts so multiple research corpora can rely on them;
3. prevent semantic drift;
4. localize errors to the layer that owns them;
5. allow repair, promotion, pinning, supersession, and shedding without collapsing the whole research program;
6. keep implementation details from silently redefining lower-layer science.

The operational debugging principle is:

> Find the first layer where the invariant or contract fails.

### Two valid directions

Authorized external inspection inward:

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

### 3. Contained architectures and analytic expansion

An architecture may be contained at one 7LM layer operationally while questions about that architecture expand across 7LM epistemically. Operational ownership answers where the architecture is realized; analytic expansion answers which 7LM owner is needed to state the particular question or representation correctly.

#### 3.1 OSI as an operating architecture

When the question is how the OSI architecture operates, the complete OSI model remains inside 7LM L4. OSI L1 through OSI L7 are internal layers of a contained realized architecture; OSI L7 is not 7LM L7, and the OSI layer numbers do not map onto the 7LM layer numbers.

#### 3.2 OSI as an object of inquiry

When the question changes to the origins, development, justification, standardization, institutional history, or design constraints of OSI, the inquiry may rail the OSI object across the 7LM architecture. The operating OSI stack remains an L4 object; the inquiry generates layer-owned representations of that object according to what is being asked.

| **7LM layer** | **OSI-origin inquiry may ask / represent** |
|---|---|
| L7 - Surface / Forward Face | Externally owned standards and source bindings, provenance, standards-publication state, public/legal governance, and relationships to standards bodies or other peers. |
| L6 - Library / Memory | Reconstructable development history, versions, superseded or retired material, internal chronology, and the record needed to recover how the local inquiry developed. |
| L5 - Research / Discourse | Institutional debate, research interpretation, committee or scholarly discourse, pedagogical framing, competing explanations, and judgments about why the architecture took its form. |
| L4 - Conversion / Realization | The realized OSI architecture itself as specified, implemented, taught, tested, transmitted, or otherwise made operational. |
| L3 - Engineering Mathematics | Engineering constraints, tradeoffs, approximation, tolerances, uncertainty, feasibility, or other engineering conditions that shaped or test the architecture. |
| L2 - Formal Mathematics | Exact formal relations, operators, proofs, or formal constraints used to state the architecture where such formalization is actually warranted. |
| L1 - State Space | Admissible structural states, possibilities, exclusions, or coordinate/state-space descriptions when these are part of the question. |
| L0 - Semantic / Foundational | The locally authored semantic distinctions required to describe what is being investigated. Externally owned standards definitions remain owned by their source and are bound through L7 rather than copied into L0. |

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

## L0 — LAYER 0

Local semantic/rail version of the bounded thing; origin contract, not a warehouse for external definitions.

| **Core question** | What local ontological, semantic, epistemic, and universality distinctions does THIS object establish before an admissible state is declared? |
|---|---|
| **Function** | Hold the object's locally authored foundational representation and its exact, immutable bindings to externally authored semantic inputs, without confusing the two authorities. |
| **Directional inputs** | Construction: the bounded object's locally authored distinctions; no higher-layer scientific dependency. Inspection: an external definition first bound at L7 may be traced inward as an exact, immutable, externally owned semantic input to the receiving L0. |
| **Output** | A local rail-grounded L0 contract sufficient for L1. A rail may remain sparse or gate-only when no local representation has been authored. |
| **Hard boundary** | A source L0 definition may travel through source L7 egress and receiving L7 ingress to receiving L0. At receiving L0 it remains exact, externally authored, immutable, version-pinned, and explicitly tagged; it is not locally redefined or counted as local authorship. L0 does not own prior art, provenance, public/legal governance, state transition, operator, proof, numerical method, experiment, or research conclusion. |
| **Machine metadata** | Machine-readable metadata may identify the local rail or an external semantic binding, including object identity, owner, source layer, version, ingress binding, immutability, gate status, and allowed actions. It may enforce handling constraints, but it must not define or replace semantic meaning. |

| **Owns / represents** | **Permitted actions** | **Acceptance / boundary check** |
|---|---|---|
| • Ontological, Semantic, Epistemic, and Universality rail boundaries for this object.<br>• System-level traversal/attachment pedagogy as a directory/function, without making Pedagogy a fifth rail.<br>• Local vocabulary or semantic representation actually authored by this object. | • bind local distinctions to their owning rail<br>• state ambiguity or unresolved meaning without filling it by guess<br>• version a changed local distinction rather than silently rewriting prior use | • Every L1 distinction resolves to locally authored L0 meaning or an exact named external semantic binding.<br>• Every external binding retains object identity, owner, source layer, version, ingress binding, and immutable status.<br>• No peer definition is locally redefined merely to make L0 look complete.<br>• No neighboring rail silently supplies another rail's local meaning. |

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

**[Boundary Rule]** **Boundary / traversal rule.** L0/semantics contains the semantic representation authored by the bounded thing. An externally owned definition is not copied into L0 merely to populate the directory.

**Directory prose and rationale**

| **Directory / thing** | **Prose** | **Why** |
|---|---|---|
| **L8/L0/** | Layer 0 container for the bounded object’s locally authored foundational and rail representation. | Keeps foundational meaning distinct from state, formalization, engineering, realized work, research judgment, provenance, and surface exchange. |
| **universality/** | Directory for the Universality rail content owned by L0. | Preserves Universality as its own rail instead of letting another rail silently supply it. |
| **pedagogy/** | Directory for system-level traversal and attachment pedagogy. | Keeps pedagogy explicit without turning it into a fifth philosophical rail. |
| **epistemic/** | Directory for the Epistemic rail content owned by L0. | Keeps epistemic distinctions inside the rail that owns them. |
| **ontology/** | Directory for the Ontological rail content owned by L0. | Keeps ontological distinctions inside the rail that owns them. |
| **semantics/** | Directory for the Semantic rail content authored by this bounded object. | Keeps local semantic meaning separate from externally owned definitions and later formal representation. |
| **semantics/definitions/** | Directory for definitions actually authored by this object under its Semantic rail. | Prevents an external definition from being copied inward and mistaken for locally owned meaning. |

**[Note]** Author note. Current correction: L0/semantics is the semantic version we make of the thing. If we do not make one, the directory is not populated with someone else’s definition.

**[Research Note]** MOST IMPORTANT: I THINK DRIFT LIVES HERE! NOT ANYWHERE ELSE...(NEEDS A LOT OF STUDY)

**[Clarification]** Standing. This statement is retained as a research hypothesis: semantic drift is expected to originate when the local L0 meaning contract changes or is misapplied. The hypothesis remains open to testing rather than being promoted to a settled rule.

#### In the case of:

In the Autonomous exemplar, IEEE/IEC have already been adjudicating relevant definitions through standards. The locally authored semantic definition used by this bounded object still lives at Layer 0, while the discourse, research, and state-space objects are distilled to their own layers. AUTONOMOUS and AUDITONOMOUS are retained as pedagogical exemplars: EXEMPLAR AUTO and EXEMPLAR AUDIT.

**[Clarification]** Standing. In this exemplar, the L0 object is the locally authored semantic definition of Autonomous. IEEE/IEC source definitions and standards remain externally owned inputs bound through L7 peering; their source identity, version, authority, and prior-art relation are represented through L7 provenance. Historical internal use remains reconstructable through L6.

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
| **External definition** | Owner remains external at L7 peering; source/version/authority/prior-art relation is L7 provenance; applicable legal/access conditions are L7 governance; internal use history is L6; interpretation is L5; no local L0 object exists unless this bounded thing authors a semantic version. |
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
| **retired/** | Directory for retired or superseded internal states and bindings that are no longer current. | Implements retirement as preservation rather than deletion, including the history of peer bindings that are no longer active. |

### Git and scientific memory

Git history can support L6 reconstruction, but Git history and scientific memory/provenance are not the same object. Git records repository change events; L6 must preserve the scientific relations, decisions, failures, corrections, versions, and retirement needed for reconstruction. External source, authority, and prior-art provenance remain L7-owned.

**[Clarification]** Integrity is enforced; no deletion is implied. What integrity needs reconstructable from the repository itself is retired, not deleted: the owner's authored documents, the rule texts of a prior layout, the error records. A superseded file whose every part is enumerated, in the record at L8/L6/history/, as standing elsewhere is deleted after that enumeration; git keeps the change event, the record keeps the enumeration. Nothing is deleted before it is enumerated, and no rule of no deletion is enforced anywhere: the one CI check checks integrity, not the absence of deletion.

**[Note]** Author note. When full interpretation begins outside the object, L7 is encountered first and L6 is the first interior layer. Interior-only inspection can therefore be described as beginning at L6.

---

## L7 — SURFACE / FORWARD FACE

External provenance, public/legal governance, peering, publications, exposure, and exchange.

| **Core question** | What provenance, governance, peer relation, publication, or other external representation must exist at the object's forward face? |
|---|---|
| **Function** | Provide the external Surface for provenance, prior art, public/legal governance, peering, publications, and release without absorbing external authority or granting lower-layer validity. |
| **Directional inputs** | Outward release: approved L6-backed packages. Ingress: peer objects, source/authority information, and governance conditions initiate inward inspection and may carry an exact source-owned L0 definition to the receiving L0 without transferring authorship. |
| **Output** | A bounded provenance record, governance record, ingress/egress binding, or publication/presentation with explicit source, authority, permissions, status, and direction where applicable. |
| **Hard boundary** | L7 owns the external relation, not the lower-layer scientific meaning. Presence, publication, copyright, patent status, custody, or provenance at L7 does not make an object valid, complete, true, or internally authored. |
| **Machine metadata** | Machine-readable metadata may identify provenance bindings, public/legal governance, visibility, ingress/egress direction, peer/object identity, release state, permissions, and NO EDIT/NO DELETE constraints for peer-owned ingress. Metadata does not transfer semantic authority. |

| **Owns / represents** | **Permitted actions** | **Acceptance / boundary check** |
|---|---|---|
| - provenance: prior art, sources, lineage, authority<br>- public/legal governance: copyright, licensing, patents, permissions, access, restrictions<br>- peering: exposure/custody, ingress/egress, peer/object bindings<br>- publications and release identity | - receive, bind, attribute, disclose, present, publish, release, route<br>- record provenance and prior art<br>- apply public/legal permissions and restrictions<br>- authorize, deny, quarantine, retire a binding without deleting its history | - Source, version, authority, and provenance are explicit where required.<br>- Applicable public/legal governance is explicit where required.<br>- External ingress is not silently admitted to L6-L0.<br>- Publication or legal status does not strengthen scientific evidence.<br>- Unused canonical branches may remain empty without implying failure. |

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
│   └── restrictions/0
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
└── publications/0
```

**[Boundary Rule]** Boundary / traversal rule. L7 is the forward face outside the USO. It owns the external relations of the bounded object: provenance, governance, peering, and publication state. Public/private exposure and ingress/egress direction remain independent peering distinctions. L7 does not thereby acquire or change the lower-layer scientific meaning.

#### In the case of:

L7 scientific desktop and forward-face semantics

The Surface is organized around four owned external relations: provenance, governance, peering, and publications. Within peering, exposure/custody (public versus private) and direction (ingress versus egress) remain independent semantic distinctions.

```text
L7/peering/
├── private/
│   ├── ingress/peer-1/object-1/
│   └── egress/peer-1/object-1/
└── public/
    ├── ingress/peer-1/object-1/
    └── egress/peer-1/object-1/
```

Public ingress is the natural peering position for externally owned, publicly available definitions or peer objects. Private ingress is available for controlled inbound material. Public egress handles outward public exchange toward peers; private egress supports restricted outbound exchange. Released publications are represented by the L7 publications branch, while provenance and public/legal governance remain separately addressable.

**[Note]** Peer-object contract. peer-1 identifies the external peer and object-1 identifies the bounded object exposed by that peer. The object may be a document, database, foreign/federated data endpoint, or repository. A peer-owned ingress object is bound/reference-only: NO EDIT and NO DELETE by the receiving repository. Retirement or supersession of the internal binding history is preserved at L8/L6/retired/ rather than erased.

**[Note]** Author note. The agnostic L7 topology carries admissible external-facing capabilities even when a project does not use them. A classroom experiment may leave governance and publication branches empty; a science fair, public release, publication, patent, or controlled exchange can populate the relevant forward-face positions without changing the architecture.

External definitions and inward interpretation

A definition lives once at its owner. When 7LM does not author the definition, its exact version is bound at L7 peering and may be carried inward to receiving L0 and referenced at any needed layer with its immutable external-ownership tag intact. L7 provenance records source, version, authority, and prior-art relation; L7 governance records applicable public/legal/access conditions; L6 preserves binding history; L5 compares and interprets it. No receiving layer thereby becomes the definition's author.

#### Autonomous and Auditonomous: peering without semantic annexation

The Autonomous/Auditonomous root issue is the originating case for the agnostic peer-1/object-1 relation. The repositories are implementation work in progress; their current layouts do not control this architecture.

Reference implementations: https://github.com/aybllc/autonomous and https://github.com/aybllc/auditonomous

Autonomous owns the locally authored definition of Autonomous.

Autonomous L7 public egress may expose an exact version of that Autonomous L0 definition.

Auditonomous L7 public ingress binds that version as a peer-owned, reference-only object under NO EDIT and NO DELETE.

Source L0 definition → source L7 egress → receiving L7 ingress → receiving L0. Auditonomous L0 may receive and bind the Autonomous definition as externally authored semantic input while remaining responsible only for the locally authored definition of Auditonomous. Receipt at L0 does not copy authorship.

Auditonomous does not have to redefine the peer definition. Wherever it is referenced internally, the exact bound version carries an immutable external-ownership tag containing object identity, owner, source layer, version, and ingress binding.

Declared semantic-deference rule. Auditonomous intentionally takes the owner's exact bound definition as authoritative for what the owner means and does not re-prove or locally redefine that meaning. This is not a claim that the definition is objectively true, an endorsement of downstream claims, or a transfer of authorship.

Auditonomous L6 preserves the binding event, exact version, use, correction, supersession, and retirement history. Auditonomous L5 interprets the bound definition without taking semantic ownership.

An argument about Autonomous cannot silently stand in for an argument about Auditonomous. Any cross-object claim requires an explicit named relation or handoff; the same identity-tagging rule applies to agnostic methods as they are made now.

Autonomous freezes the narrowest reasonable agreement among its exact source-tagged standards inputs as the Autonomous consensus baseline. It must not manufacture consensus where sources materially disagree. Auditonomous then authors the Auditonomous difference as an explicit local delta; the baseline and delta remain separately owned and overlaid.

An upstream change creates a new binding; it does not mutate the pinned object. A change to the Autonomous definition returns to the Autonomous owner. Auditonomous updates or retires its binding; it does not edit the peer-owned definition.

**[Clarification]** This is not an optional exemplar. It is the concrete originating boundary test for the agnostic architecture.

**[Note]** Author note. Public/private and ingress/egress are explicit semantic positions in the canonical research tree. Their presence does not assert that every external implementation must use the same filesystem vocabulary.

**[Note]** Author note. Many intelligences at one face. The peering positions are not sized for one counterpart: peer-1 opens an enumeration that is the same on all four faces, so the bounded object can meet any number of intelligences at once, a person, an institution, a standards body, another repository, an archive, a model session, an orchestrator, each at its own numbered peer position and each delivery its own object. Provenance is positional: the path says who brought a thing before anyone reads it. The peer's 0 is the owner's register of that peer's objects and their standing, and it is written by a person; nothing here presumes an automated mover. The tree states positions; what any intelligence may write is not stated by the tree.

**Directory prose and rationale**

| **Directory / thing** | **Prose** | **Why** |
|---|---|---|
| **L7/** | External Surface / forward-face container outside the USO where the bounded object meets external people, institutions, systems, repositories, legal/public conditions, publications, and data sources. | Keeps external relations separate from the scientific interior while giving those relations an explicit owner. |
| **provenance/** | Directory for the external provenance of the bounded object: where it came from, what preceded it, what source/version is being used, and what authority is being represented. | Places externally meaningful source and lineage information at the forward face rather than burying it inside internal memory. |
| **provenance/prior-art/** | Directory for identified prior art and antecedent work relevant to the bounded object. | Makes the antecedent landscape explicit without confusing prior art with the object's locally authored L0 meaning. |
| **provenance/sources/** | Directory for source identity and exact source/version references. | Keeps source identification inspectable at the external face. |
| **provenance/lineage/** | Directory for externally relevant lineage and derivation relationships. | Makes origin and relation traceable without turning lineage into scientific validity. |
| **provenance/authority/** | Directory for represented source/owner authority associated with the external object or record. | Distinguishes who owns or speaks for an external object from what the local research concludes about it. |
| **governance/** | Directory for public/legal/custodial conditions attached to externally exposed or received objects. | Separates legal and access conditions from provenance, peering direction, publication, and scientific judgment. |
| **governance/copyright/** | Directory for copyright-related representation when applicable. | Copyright governs external use of an artifact; it does not change the artifact's scientific meaning. |
| **governance/licensing/** | Directory for licensing terms or status when applicable. | Keeps permissions of use explicit at the external face. |
| **governance/patents/** | Directory for patent-related representation when applicable. | Provides an agnostic forward-face position for patent status or materials without requiring every project to use it. |
| **governance/permissions/** | Directory for explicit permissions attached to external use, disclosure, or exchange. | Keeps permission separate from ownership and from scientific validity. |
| **governance/access/** | Directory for access conditions applicable to externally facing objects. | Makes who may access an object a boundary condition rather than an internal scientific claim. |
| **governance/restrictions/** | Directory for restrictions that constrain external disclosure, use, transfer, or handling. | Keeps restrictions explicit and machine-addressable without redefining the underlying research. |
| **peering/** | Directory for relationships to externally owned peers and the bounded objects exchanged with them. | Preserves external ownership and authority instead of absorbing the peer into the USO. |
| **private/** | Peering branch for non-public exposure or custody. | Keeps exposure/custody distinct from direction. |
| **private/ingress/** | Private inbound peering position. | Represents something entering from a peer without making it public or internally owned. |
| **private/egress/** | Private outbound peering position. | Represents something leaving toward a peer without making it a public release. |
| **public/** | Peering branch for public exposure or custody. | Keeps public exposure distinct from whether the object is entering or leaving. |
| **public/ingress/** | Public inbound peering position. | Represents a publicly exposed external object entering the local boundary without transferring ownership. |
| **public/egress/** | Public outbound peering position. | Represents public outward exchange toward a peer; the released publication object itself is held by the L7 publications branch. |
| ***/peer-1/** | Directory identifying the external peer within an ingress or egress position. | Keeps peer identity distinct from the particular object exchanged with that peer. |
| ***/peer-1/object-1/** | Directory identifying one bounded peer-owned or peer-directed object. | Allows one peer to expose or receive multiple objects without treating the peer itself as the object. Peer-owned ingress is reference/binding only: NO EDIT and NO DELETE by the receiving repository. |
| **publications/** | Directory for released publication objects at the forward face. | Keeps publication release at L7 while writing remains L4, research meaning remains L5, and internal history remains L6. |

**[Clarification]** Copyright has one place, governance/copyright/: every copyright or licence condition the bounded object is under is stated there once, with what to do next. governance/licensing/ and governance/restrictions/ point to it rather than restating it.

**[Note]** Author note. Curated sources are served by pointer. A designated archive repository holds the source files; it is bound at private ingress and is read-only from every consuming repository. A consuming repository keeps one ledger row per source at provenance/sources/, with the archive path and the pinned commit, and no source file lives in it.

```text
external owner L0 definition
 |
 v
source L7 public egress
 |
 v
receiving L7 public ingress — exact immutable binding
 |
 v
receiving L7 provenance/governance — source, version, authority, conditions
 |
 v
receiving L6 through L1 — only needed layer-specific references, identity tag retained
 |
 v
receiving L0 — externally authored semantic input; local definition only if WE author one
```

This direction preserves ownership and makes interpretation inspectable. It also prevents a copied external definition from masquerading as a locally authored semantic object.

### Forward-face model

L7 is the desk: the current external surface where finished work, external bindings, provenance, governance, peering, and publications become addressable without moving their scientific meaning out of the USO.

Conceptual distinctions include consumer <-> product; customer <-> service; request <-> response; need <-> offer; incoming object <-> outgoing object; and private custody <-> public exchange.

Presence on the desk establishes nothing by itself. Provenance, custody, authority, copyright, patent status, permissions, internal consistency, and publication each answer different questions; none of them alone establishes scientific truth.

#### Standing rules

A definition lives once, at its owner. L7 holds the boundary binding and provenance relation. The exact bound version may be carried inward with its immutable ownership tag, but it never becomes a copied substitute or locally authored definition.

To change an immutable external object, return to its owner. The repository using the object does not edit the peer-owned source.

Material crossing outward may lose fidelity and may never gain scientific maturity merely by being exposed.

No outsider traverses the USO by default. What an outside reader or system needs is represented at the forward face.

Machine-readable metadata may support automation, but the architecture does not assume that automation has been enabled or validated. Current research practice may remain manual until the metadata contract is tested.

---

## Exemplars as instantiated

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
| definitions | Ratified | Locally authored definitions belong at L8/L0/semantics/definitions/; peer definitions arrive as immutable external bindings. |
| semantic-formulas | Split and reserved | Semantic reading remains L0; an exact formula is L2; an applied, tolerant, adaptive, or engineering formula is L3. The inherited compound term remains searchable. |
| thesis-statements | Relocated | Research claims and thesis statements belong at L8/L5/research/lanes/ or the corresponding L5 research artifact. |
| origidity; certainty; intolerance | Reserved | Candidate L1 semantics preserved; topology remains unadjudicated. |
| found; caught; naught | Reserved | caught remains the zero state; found remains the observer role; naught remains the empty or settled state. Their topology remains unadjudicated. |
| regress | Reserved | Preserved as a prior unadjudicated holding concept; active path and owner remain unadjudicated. |
| corpus | Split and reserved | Released corpus/publication identity belongs at L7/publications/; the broader inherited term remains reserved where its exact role is not yet adjudicated. |
| INFRASTRUCTURE | Superseded as L4 name | L4 is Conversion. Infrastructure belongs at L4 only when it is the bounded work or conversion being made; generic repository support is not automatically a layer. |
| DEVOID; IMMUTABLE; FINITE; INFINITE; IDENTITY BY PROSE; RESEARCH MEMORY; SCIENTIFIC DESKTOP | Descriptive | Preserved as historical mnemonics or working language; the principal layer sheets control ownership. |
| L6 provenance | Split | Internal reconstructable memory remains L6; external source, authority, prior art, and public provenance belong at L7/provenance/. |
| USO/ as the directory name of the interior | Renamed L8/ | The term USO remains the name of the bounded scientific object's interior; the directory is L8, the research packet on the desk, a count and not a rank. The scaffold and the exemplars carry USO/ until the rename pass. |
| README.md as documentation | Superseded | README.md is where a reader starts; the sheets and this specification are the documentation. The READMEs that carried documentation were deleted after enumeration, records kept at L8/L6/history/. |
| no deletion as a rule | Superseded | Integrity is enforced; no deletion is implied. Retirement is for what integrity needs reconstructable; deletion after enumeration is the ordinary act, recorded at L8/L6/history/. |
| l0 … l6 as the interior directory names | Superseded | L0 through L6 under L8: the eight bits L0 through L7 and the extra bit L8. The repositories carry lowercase until the rename pass. |
| orphan; foster; results; delete | Retired | The exemplars' queue vocabulary and the access rules that came with it were retired on the owner's word; L8/L5/research/review/ is the catch-all and L8/L5/research/lanes/ the working position; nothing is deleted. |
| peer-1 / object-1 numbering | Reported, not resolved | The peering enumeration begins at 1 while the layers count from 0 under "First is always 0"; the owner's call. |

The dated lists of what changed in each version stand at L8/L6/history/specification-history.md in the scaffold repository.
