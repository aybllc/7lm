# The Seven-Layer Model: A Field Guide

A research program accumulates claims of different kinds, and without a discipline separating them, a definition, a measurement, a derivation, and a conjecture come to look alike on the page. The Seven-Layer Model is a dependency and fault-containment architecture that keeps them apart and makes the difference inspectable.

This guide states what each layer owns, where a given piece of work belongs, and the procedures for the operations you will perform most often. Section 12 is a glossary of the terms used throughout.

Everything here is drawn from the specification, from the sheets, the `0.md` files that describe every folder in the `aybllc/7lm` repository, and, where the exemplar repositories are described, from those repositories as they stood. Where this guide and the specification differ, the specification controls.

This guide is filed at `L8/L6/` in `aybllc/7lm`, as a source document. It is not the L0 pedagogy of a repository that uses the model: a repository's `L8/L0/pedagogy/` explains how that one object is traversed and attached, in its own terms, and a guide to the model as a whole is not that. A person who adopts the model takes this guide from L6, applies its updates or leaves them, publishes their own version at their L7 or keeps it at their L6, and secures their L7 surface as part of the same decision. This is the guide before the last one; the last is the one each adopter publishes. The step is taken by a person and by nothing else. The owner marks such steps HOA, human-only actions. Where an adopter's version sits is a design choice of theirs, not a rule of the model. What is never a design choice: the guides share no history. This guide carries the model; what `aybllc/7lm` was and how it changed is in its own L6, and an adopter's past is in theirs.

The diagrams live on their own sheet. The 7LM Plate Sheet is the only place the model is drawn, so there is one sheet to change when the model changes. It carries one plate for now, the eight positions with L8 as the envelope around all of them, and it is filed at `L8/L0/pedagogy/7lm-plate-sheet.html`.

---

## 1. What the Seven-Layer Model is

7LM is a directory layout with one rule per position. Every folder has exactly one job. Every folder also carries a file named `0.md`, called a sheet, which states the space of that folder and what it does. Section 10 says what a sheet is and is not.

Nothing runs on its own. There is no engine and no validator that files material for you. The filing is manual, by design. The whole model is written down in a single document, the Harmonized Authoritative Architecture Specification, which lives at `L8/L4/work/writing/7lm-harmonized-architecture-specification.md`.

### The one idea

A single subject carries several distinct kinds of claim, and each kind belongs to a different layer. The `aybllc/autonomous` repository studies one word, *autonomous*. Its claims distribute as follows.

- **What the word means here.** Somebody had to sit down and write the definition this project actually uses. That is `L8/L0/semantics/definitions/AUTONOMOUS.md`, and it lives at the bottom layer, L0.
- **Which states are admissible.** Before you can say a system moved from one condition to another, you have to declare which conditions the definition admits at all. In the sister repository, `aybllc/auditonomous`, that work sits in `L8/L1/state-space/AUDITON_ENVELOPE.md`.
- **What follows exactly, by derivation.** Axioms, operators, exact relations, theorems. In both exemplar repositories this layer holds a formulas ledger that currently declares itself empty.
- **What survives engineering tolerance.** This is where an exact relation meets units, error budgets, convergence, and the question of whether the thing is feasible at all.
- **What was genuinely made or measured.** A manuscript, a computation that ran, an experiment with a result. Autonomous keeps its manuscript placeholder and a deep research run here.
- **What you may responsibly conclude.** Autonomous states one of its conclusions plainly in a file called `FINDING_autonomy_is_an_edge_property.md`. That is a judgment about evidence, not the evidence itself.
- **What this thing used to be.** Old versions, corrections, retired layouts, the record of what changed and why.
- **What the outside world gets to see.** Sources, copyright, the standards bodies you depend on, anything you actually published.

Eight kinds of claim, one subject. 7LM gives each kind its own position. The first seven take the seven layers, L0 through L6. The eighth, the object's relation to the outside world, takes the desk, L7, which is not a layer. Section 3 states the count rule that makes this consistent.

The operating principle: a claim is only as strong as what its layer has earned.

### The debugging rule

When something fails, locate the first layer at which a promise breaks, and correct it at that layer. Do not compensate for it from a layer above. This rule governs every correction procedure in the guide.

---

## 2. The positions, in one table

Read this table bottom to top when you are building something. Read it top to bottom when you are inspecting something. Both directions are real, and section 4 covers them properly.

| Position | Name | The question it answers |
|---|---|---|
| L7 | Surface / Forward Face (the desk) | What does the outside world need to see? Sources, rights, peers, publications. |
| L6 | Library / Memory | Can we rebuild what this object used to be and how it changed? |
| L5 | Research / Discourse | What can we responsibly conclude, question, teach, or decide? |
| L4 | Conversion / Realization | What was actually made, written, run, measured, or recorded? |
| L3 | Engineering Mathematics | How do we make the exact math workable, with real units, tolerances, and error bounds? |
| L2 | Formal Mathematics | What follows exactly when lawful operations act on the allowed states? |
| L1 | State Space | Which states are admissible at all, under the contract L0 established? |
| L0 | Semantic / Foundational | What does this object mean, before anything else is said? |

Two further names appear throughout.

**L8** is the folder that holds the seven interior layers. The specification calls it the research packet on the desk. It is a count rather than a layer; section 3 explains the distinction.

**USO** is the name for what L8 holds: the inside of one bounded object. A bounded object is a single research thing with a clear edge, like one definition or one project. So `L8/` is the folder, and the USO is what sits in it.

Two facts about the layout on disk. L7 is outside the packet: `L7/` and `L8/` are siblings, and moving from the desk into L6 crosses a boundary rather than opening a subfolder. And nothing follows the desk. Past it the count restarts at zero inside another object's tree, where this entire object is one bound object at a peer position.

**The packet reading.** The specification states one more thing about these positions, and it is the owner's. Read the object as one packet. L0 is the origin: the meaning that exists in the head first and is written down second, and it is not payload. L1 is the floor of the payload and L6 its end. L7 is the glue, the face at which the object binds to what is outside it. L8 envelopes them all, and its trailing edge is the connector to the next object's L0. That connector is why nothing follows the desk: past the face the object hands off, and the count starts again at zero in the next object's tree. The reading changes no position and no path. It is drawn on the plate sheet.

---

## 3. The count rule: "First is always 0"

The owner's rule is four words: first is always 0. It is stated with this table:

| semantic | > | magnitude |
|---|---|---|
| FIRST | is | 0 |
| SECOND | is | 1 |
| THIRD | is | 2 |
| FOURTH | is | 3 |

Ordinals such as *first* and *second* are semantics. Numbers such as 0 and 1 are magnitudes. The relation between them is *is*. First is 0, second is 1, and so on.

The seven layers are L0 through L6, so the seventh layer is L6. In the owner's words, "layer 7 will always be layer 6 :)". L7 carries the number 7 but is not a layer. It is the desk, and counting up from L0 it is the eighth position you reach. L8 is not a position at all. It counts the eight positions L0 through L7, and it also names the folder holding the interior.

A second count runs in parallel, and the two must not be confused. Peers at the desk are numbered from 1: `peer-1`, `object-1`. Layers are numbered from 0. The owner's reasoning: peers are physical, and physical things are counted from one. Zero is the semantic origin, where the Semantic and Epistemic rails define the layers above. It is what exists before anything physical does.

### The names are descriptive

The specification records that the names were chosen to depict what they name. Three readings are given.

**L7 depicts the desk.** Pronounced El-Seven. The L forms the left side and bottom edge of a desk seen from above; the 7 forms the top edge and right side. Set side by side in the right font, the two characters close into a rectangle, which is the surface the layer is.

**L8 depicts the enclosure.** Because the count starts at L0, every layer carries a zero, its `0.md`, and the interior carries one as well, `L8/0.md`. The interior's zero over the layers' zeros gives 0 over 0, which forms an 8. An 8 is a closed figure: L8 encloses the seven layers.

**The byte reading.** L0 through L7 are the eight bits of a byte. L8 is the extra bit, which, like a check bit, carries the semantic and catches an error.

---

## 4. The two directions

There are exactly two legitimate ways to move through this structure.

**Construction goes outward.** Scientific construction, in the specification's phrasing. Start at L0 and proceed upward through L1, L2, L3, L4, L5, L6, to L7. Move up only when the layer beneath has settled its promise. Sometimes there is no settled way to carry your work up to the next layer, and when that happens you stop where you are. The specification calls the missing link a bridge, and it calls stopping at one *honest placement*. You leave the work at the last layer that earned it. That is a result, not a failure.

**Inspection goes inward.** Authorized external inspection, formally. Start at L7 and descend through L6, L5, L4, L3, L2, L1, to L0. An external reader meets the desk first, with the sources and rights; then the memory, and what the object used to be; then the research, the realized work, the engineering, the exact relations, the admissible states; and last, the meaning the object authored for its own terms.

One warning, straight from the specification: "Description does not become prescription merely because the structure can be traversed." Traversal is not prescription. Being able to walk a path does not turn that path into a rule.

---

## 5. The rules that hold everywhere

These apply at every layer. Most filing questions are answered by them directly.

**Higher layers do not silently repair lower layers.** Suppose your research at L5 needs a word at L0 to mean something slightly different than it does. L0 is not reinterpreted in place. It is revised explicitly, with a new version, so that everything depending on the old meaning is affected visibly.

**Each representation lives at the lowest layer that can state it correctly.** A representation is one distinct way of stating the thing. The same topic can have a representation at several layers, and that is expected. Each representation belongs to exactly one of them.

**Change one layer at a time.** A fix in one place never quietly rewrites another.

**Empty folders are fine.** Every repository carries the full layout, including the parts it has never used. An unused folder is an available capability, not a gap in your work. The specification's own example is a classroom experiment that leaves governance and publications empty. If that experiment later goes to a science fair, gets published, or produces a patent, those folders are already waiting.

**The sheet carries meaning; metadata carries machine instructions.** The `0.md` file is written for humans. Machine metadata, if it ever exists, attaches to the folder itself rather than sitting in the tree as a file, so none is created. Right now no machine metadata is switched on anywhere in the scaffold or either exemplar. Everything is manual, and the specification does not pretend otherwise.

**Build whatever the math permits. Claim only what the layer has earned.** The owner's rule. Valid math at L2 does not become an engineering claim at L3 on its own, and it does not become a claim about measured results at L4 either. Publishing something at L7 never strengthens it.

The rule does not prohibit speculation. A hypothesis may be stated and explored mathematically as far as it goes. The specification's example is faster-than-light travel: peer-reviewed FTL mathematics may be legitimate mathematics and still stop at L2, with no promotion to realizable propulsion. Stopping there is honest placement, not rejection.

The same applies to any assumed capability: unlimited power, perfect information, zero latency, infinite endurance. Each may be studied conditionally. None may serve as free evidence. A claim that depends on one requires that capability to carry its own engineering and evidentiary burden first, and nothing unobserved or unbuilt is promoted downward into the foundational claim space.

**L6 history is local to the bounded object it reconstructs.** A shared guide can describe the model, and external archives or tools can support reconstruction, but another object's history does not become this object's L6 merely because it is accessible. What matters architecturally is that the internal history claimed by this object can be reconstructed and correctly oriented.

---

## 6. Each layer, up close

### Analytic groups are not folders

The specification discusses layers in groups for certain questions. None of those groups is a folder. Under `L8/`, the seven layer folders sit flat, side by side.

L6 and L5 together are the upper interior, memory and research, and they remain separate owners. L4 alone is the realization bay, which can contain an entire realized system with its own internal layers. L3, L2, and L1 together are the technical-possibility bundle, used when a question requires engineering, exact formalization, and admissibility at once. L3 and L2 form a tighter pair when the relevant L1 state space is already established and not itself under question. L0 is separated from L1 deliberately: L0 establishes the semantic contract, and L1 establishes the states admissible under it.

A question may traverse some layers and skip others. Each part of the answer still belongs to exactly one. Do not create a folder for a group.

### L0: Semantic / Foundational

This is where the foundational meaning used by the bounded object lives. The specification calls what L0 produces the semantic/foundational contract on which the state-space representation above it depends.

Four rails divide the work, each with its own folder: ontology, semantics, epistemic, and universality. A fifth folder, pedagogy, holds explanation of traversal and attachment. Pedagogy is a folder and a function, not a fifth rail.

Definitions that function in this object's semantic contract go in `semantics/definitions/`. They may be locally authored, adopted from an external source, adapted, or explicitly provisional. Filing a definition at L0 does not erase its source authorship.

If a definition came from outside, its source relation is represented at L7/provenance where relevant. Peering is used only when an identifiable external counterpart relationship is itself part of what the object represents. A definition found in a book, article, database, archive, standard, or web search does not become a peer merely because it came from outside.

The owner left a research note at this layer worth repeating. Semantic drift, the divergence that sets in when the L0 meaning contract changes or is misapplied, is retained as an open hypothesis, not a settled rule.

### L1: State Space

The specification's phrase for the job is to freeze the board: which states are admissible, which are excluded, and which invariants hold, meaning the properties that stay fixed no matter what else varies. The layer also owns dimensions, domains and ranges, equivalence classes, and identity conditions, which together decide when two states count as the same state. One folder, `state-space/`, holds all of it.

Nothing moves at this layer. No calculation, no transformation, no transition. That machinery starts at L2.

Auditonomous fills this layer with three files, including the auditon envelope and a partition of requirements ownership. Autonomous, by contrast, leaves L1 empty, with its dimensions fixed inside findings at L5 instead. The same architecture, two different states of completion.

Sometimes a result lands outside the declared state space. When that happens, exactly one of two things is true. Either the construction is invalid under the current model, or the state space is incomplete for the phenomenon and needs an explicit, justified extension. Nothing steps outside its admissibility conditions quietly and still claims continuity with the same system.

### L2: Formal Mathematics

Exact objects only: notation and types, relations, operators, constructors, carriers, transition systems, and the axioms, lemmas, theorems, and derivations that bind them together. One folder, `formal-mathematics/`, holds three more: `relations/`, `operators/`, and `proofs/`.

Every symbol here resolves to the L0 meaning and L1 admissibility on which it depends. Functions and operators state domain and codomain; a partial operation additionally states the subset on which it is defined. General relations are not forced into function terminology: a relation may instead be stated as a subset of an appropriate Cartesian product or other formal carrier. Conjectural and unproved claims remain explicitly unproved.

Both exemplar repositories keep a formulas ledger at this layer, and both ledgers currently say the same thing: empty, no formulas held. The ledger's own preamble explains why it exists at all. A formula's existence and a formula's application get checked in separate columns, because collapsing those two is precisely the failure the file was built to prevent.

Engineering tolerances, numerical approximation, and numerical uncertainty do not belong to L2 exact formal ownership. Exact relations may nevertheless include dimensioned quantities or units; units alone do not move an exact relation to L3.

### L3: Engineering Mathematics

Here the exact relation meets realizable conditions: numerical representation and precision, approximation and discretization, tolerance, error and uncertainty budgets, sensitivity, stability, convergence, computational complexity, measurement/engineering treatment of units, and the operating region in which any of it holds. One folder, `engineering-mathematics/`, holds three more: `approximation/`, `uncertainty/`, and `tolerances/`.

A formula can have several layer-specific representations. Its semantic meaning belongs to L0; its exact formal statement belongs to L2; its numerically represented, approximate, tolerant, uncertainty-bearing, or otherwise engineering-constrained form belongs to L3.

Autonomous files two notes at this layer that show the range. One sits under tolerances and works through a defect in a shared referent. The other sits under uncertainty and examines dependence and a gate. Neither is a proof, and neither is a measurement. Each states the conditions, bounds, and failure modes under which the thing could be built or trusted.

The specification retains a working life-boundary hypothesis here, but it does not define the L2/L3 boundary. Exact feedback, dynamical, control, or adaptive relations can be represented at L2 when stated exactly. Their numerical realization, tolerances, uncertainty, finite precision, stability under implementation, or other engineering constraints are L3 questions. The broader claim that L2 'does not support life' remains an untested research hypothesis.

What leaves this layer is an engineering specification telling L4 what can be built or run, within which bounds, and with what declared error. L3 produces no empirical evidence of its own.

### L4: Conversion / Realization

This is the layer at which resources are committed and an identifiable output or recorded failure is produced.

The specification's phrase is any conversion between intellectual property and energy, in either direction. Note the sense of the term: *intellectual property* here means ideas and intellectual objects, such as a piece of writing or a model. It does not mean copyright and patents, which are legal conditions owned at L7.

Ideas to energy looks like writing, computing, running an experiment, building, deploying, or teaching. Energy to ideas looks like measurements, observations, datasets, and recorded failures. One folder, `work/`, holds three more: `writing/`, `experiments/`, and `computation/`.

Autonomous shows the layer at work. Its manuscript placeholder sits under writing. So does its autonomy scale, which the owner ruled explicitly is an L4 object as a written thing even though what it means is L5 discourse. Under computation sits a deep research run, filed as a thing that ran rather than a thing that was concluded. Auditonomous goes further and files its chat transcripts and a session record here too, because those are also events that happened.

A whole system with its own internal layers sits inside L4 as a single object. The classic case is a complete OSI network stack, which carries seven layers of its own. Its internal "layer 7" is not 7LM's L7, and the two must not be confused.

Two different questions can be asked about that stack, and they file differently.

Ask *how does it operate*, and the whole stack is one L4 object with its own internal layers intact. Ask *where did it come from, and why is it built this way*, and the inquiry expands across the architecture. External standards sources and their provenance go to L7/provenance; relationships with standards bodies go to L7/peering only when those relationships themselves are represented. Development history goes to L6. Debate and interpretation go to L5. Engineering trade-offs go to L3. Exact relations go to L2 where genuinely warranted. Admissible states go to L1 when part of the question. Foundational meanings used by the bounded object go to L0.

The stack does not move when the question expands. It remains an L4 object. The specification names this distinction operational containment versus analytic expansion, and it means a network fault inside the stack is an L4 fault unless somebody separately shows it touches another layer's object.

The owner calls this layer the cut. Below L4, things are specified. At L4, things are made.

Failures are first-class L4 work products. A run that died, a build that broke, or a measurement that failed is still an event that occurred; it is not quietly converted into a conclusion. The relevant inputs, conditions, transformations, results, and lower-layer dependencies remain identifiable to the degree needed to understand or reproduce the realized work.

L4 does not interpret its own results. That belongs to L5.

### L5: Research / Discourse

Interpretation, review, judgment, argument, teaching.

`research/lanes/` holds distinct lines of inquiry, one lane per question. Autonomous runs six of them, lettered A through F, covering the IEEE definition, auditability, levels, peer-reviewed literature, the smallest unit in a network, and verbatim capture. The lanes keep separate questions from collapsing into one undifferentiated stream.

`research/review/` holds review, criticism, and audit, and it doubles as the catch-all, which section 9 explains.

`research/findings/` holds what may responsibly be stated from the evidence. Autonomous keeps seven, among them that autonomy is an edge property, that IEEE 1872.2 does not define autonomy, and that NASA will not buy autonomy. Every finding carries its cited dependencies, its stated limitations and uncertainty, its review status, and its reproducibility information. A finding is never broader than its evidence or its maturity.

A review compares the claim to its evidence and may accept, reject, qualify, or supersede it. It may request revision from a lower-layer owner without silently mutating that owner's object.

`institution/peers/` and `institution/undergraduates/` record who takes part. They say nothing about what the research concluded.

The hard boundary at L5: consensus, prose, authority, and usefulness never substitute for proof or measurement. A well-argued paragraph is not a result.

One further ruling applies here. A scale, a ladder, or a set of status labels is an L4 object as a written thing, and what it means is L5 discourse. It is never an L1 state space and never L2 mathematics.

### L6: Library / Memory

What this object used to be, and how it changed. The specification's word for the standard is reconstructable: prior internal states, branch and decision history, failed paths, corrections, supersession, and retirement all have to be recoverable from the record itself. Two folders carry it: `history/` for the records of change, and `retired/` for prior states kept exactly as they were.

Git history supports reconstruction, but it is not the same object as scientific memory. Git records repository change events. The L6 record preserves the scientific relations, decisions, failures, corrections, versions, and retirements that make the change reconstructable. A commit identifier is an orientation pointer into the memory, not the memory itself.

Correcting something never requires deleting what it corrected.

A repository's history is its own and stays here. The guides share none of it: the source guide at the scaffold's L6 and the version an adopter publishes each carry the model, and neither carries the other's past. That is what this layer is for.

### L7: Surface / Forward Face

The desk. Where your object meets people, institutions, other repositories, legal conditions, and publications. Four folders: `provenance/`, `governance/`, `peering/`, and `allications/`.

Being on the desk proves nothing by itself. Provenance, custody, copyright, and publication each answer a different question, and not one of them makes a claim true.

---

## 7. Where things go: the filing cases

One thing can appear across several layers, each layer owning a different aspect of it. This table uses the four desk folders, which section 8 explains.

| Thing | Where its parts go |
|---|---|
| A written document | Making the file is L4. Its argument is L5. Its version history is L6. Its released publication is L7. |
| An experiment | Running it and the raw results are L4. Method and tolerance are L3. Exact relations are L2. Which states are possible is L1. The conclusion is L5. |
| Code | Algorithm and engineering choices are L3. A formal proof or model is L2. Execution, deployed bytes, and results are L4. |
| Data | Collected and stored instances are L4. Precision is L3. Formal encoding is L2. State categories are L1. External source and lineage are L7. Its own development history is L6. Interpretation is L5. |
| A definition from an external source | If the definition functions in this object's semantic contract, that semantic role is L0 regardless of source authorship. Source/version/authority relations are L7 provenance where relevant. Legal/access conditions are L7 governance where relevant. A peer relation is L7 peering only when an identifiable external counterpart relationship exists. Interpretation is L5; internal history may be L6. |
| A publication | Producing it is L4. Its scholarly meaning is L5. Its internal history is L6. Provenance, rights, and the released object are L7. |
| A system with its own layers, like an OSI stack | Running it is L4, whole. Questions about its origin, history, or design each go to the layer that owns the answer. The system itself is never re-mapped onto 7LM layers. |
| A forum, chat, or discussion tool | The tool as built and run is L4. Its outside face is L7. The roles, discussion, review, and judgments carried through it are L5. |
| Research as a whole | The work events are L4. Interpretation and review are L5. Internal memory is L6. External provenance and what is shown outside are L7. Each lower layer owns its own piece. |

---

## 8. The desk in detail

The desk carries the object's external relations. Each branch is covered separately below.

### Provenance

`L7/provenance/` represents external source relations: prior art, source identity/version, lineage, and represented authority. A source can be a paper, book, database, archive, standard, website, dataset, repository object, or other external material.

7LM does not require source files to live in one designated archive. One implementation may use a curated archive and point to exact versions there; another may use DOI records, publisher copies, library holdings, URLs, local files, or other stable references. What matters to provenance is the source relation being represented, not the storage mechanism.

A source does not become a peer merely because it is external. If the relationship with an identifiable external counterpart itself matters, that relationship can additionally be represented at `L7/peering/`.

### Governance

`L7/governance/` represents external conditions that bear on use, disclosure, access, or legal/custodial status. Its child positions answer different questions:

- `copyright/` — copyright status, claim, holder, notice, or uncertainty;
- `licensing/` — licence terms or status;
- `patents/` — patent-related external facts where relevant;
- `permissions/` — a specific grant or permission;
- `access/` — conditions under which an object can be reached;
- `controlled/` — restrictions on disclosure, use, transfer, or handling.

One object can have several of these relations at once. None substitutes for the others, and peering does not manufacture a permission or restriction.

### Peering

`L7/peering/` represents an identifiable relationship between the bounded object and an external counterpart.

A peer may be a person, institution, repository, archive, laboratory, publisher, standards body, service, model, instrument, organization, or another bounded object. The relationship need not itself be scientific.

Two independent coordinates describe the relation:

- `public/` or `private/` describes **exposure**. Both are auditable surface channels; a private channel has a restricted audit audience rather than no auditability.
- `ingress/` or `egress/` describes **direction relative to the bounded object**.

Beneath those coordinates, `peer-N/` distinguishes one external counterpart and `object-M/` distinguishes one object or interaction in that relation. The numbers are local identifiers, not ranks, authority levels, global identities, or lifecycle states.

Peering does not by itself establish authorship, ownership, provenance, permission, acceptance, truth, immutability, scientific validity, or what should happen next.

#### Instructional examples

A student sends a draft to a teacher through a restricted course system: private egress. The teacher returns comments: private ingress. Whether the student adopts the comments is an L5 research/discourse question, not a peering fact.

A laboratory receives a dataset directly from a collaborator through a restricted exchange: private ingress. The source provenance of the dataset may also be represented under provenance.

An external researcher opens a public issue: public ingress. A public response directed to that researcher is public egress. Neither interaction becomes a publication merely because it is visible.

A researcher finds a definition in a standards document through a web search: provenance may apply, but peering need not. The definition's semantic role can still be L0 if the bounded object actually uses that definition.

#### Originating implementation example

The Autonomous/Auditonomous work historically motivated one use of peering: one bounded research object relating explicitly to another while keeping their source identities distinct. Those repositories may choose version pinning, reference-only handling, or local-delta conventions. Those are implementation properties of that exemplar, not the general definition of peering.

### Allications

`L7/allications/` holds what the object does outward. Six positions, each a nominalized outward act that leaves a record someone can point at afterwards:

- `publications/` — released objects, each with a release identity.
- `applications/` — outward applications or submissions that request an external decision, such as funding, review, admission, approval, participation, or registration.
- `communications/` — statements, correspondence, announcements, answers issued outward.
- `specifications/` — a contract handed outward for others to build or check against.
- `notifications/` — notices given, usually discharging an obligation, where the fact of having given notice on a date is the point.
- `participations/` — bodies, panels, working groups the object took part in, with the role and the period.

The name is the owner's, and it is a mnemonic for the family rather than the test for membership: an outward act belongs here whether or not its name ends in *-ication*. The writing stays at L4, the meaning stays at L5, and the history stays at L6.

---

## 9. Two working habits

Two procedures govern day-to-day filing.

### The catch-all

Everything awaiting the owner's review lands at `L8/L5/research/review/`, whatever its kind and however much of it there is.

When the owner picks something up, it moves to `L8/L5/research/lanes/`, the working position. If they set it down again, it moves back. Position is state here: the moves are the record, and nothing gets deleted along the way. Anything the owner sets aside stays in review with the label PARKED. Finished work gets filed at its proper layer.

You need no other position and no new folder for any of this. The topology already has the two moves and the exits.

### Nothing is deleted before it is enumerated

To enumerate a file means listing every part of it and where each part now stands.

The rule that actually gets enforced is integrity: the repository has to stay whole and reconstructable. "Nothing is deleted" is not a separate rule sitting beside it. It falls out of integrity as a consequence.

Some things have to stay readable so the past can be rebuilt, and those get retired to `L8/L6/retired/` rather than deleted. The owner's authored documents, the rule texts of a prior layout, error records.

Everything else follows the ordinary act. A superseded file is deleted once every part of it is enumerated in a record at `L8/L6/history/` stating where each part now stands. Deleted, not retired. Git keeps the change event and the record keeps the enumeration. Retiring such a file would make L6 a second copy of git.

The one automated check on the repository, which section 10 describes, checks integrity. It does not check for the absence of deletion, and the owner was explicit that it must not.

---

## 10. The layout every 7LM repository shares

The root, meaning the top folder of the repository, holds `README.md`, `L7/`, and `L8/`. It may also hold two pieces of repository infrastructure that are not layers: the one CI workflow under `.github/`, and a `.gitignore` if there is anything to ignore. Nothing else belongs at the root, and every 7LM repository has the same one.

The README is where a reader starts. It states the reading order. The layout is stated folder by folder in the sheets, and the model in the specification.

In the tree below, `/0` after a folder name means that folder carries its `0.md`.

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

### The sheet rule

Every folder has a `0.md`. Two things about it are not design choices. The sheet exists, in every folder of the tree the scaffold pushes. And its first line is the folder's own path from the root, written like `# L8/L3/engineering-mathematics/`. Keep the tree and keep the sheets so, and the repository is a 7LM repository. Drop either and it has branched outside the system: the work may be good research, but it is not how this system works, and it is not supported or developed as part of it.

After the first line the sheet states the space of the folder and what it does. How much it says is a design choice. For a layer's own sheet, `L8/L0/0.md` through `L8/L6/0.md`, the recommendation is at least one sentence more than the layer's number: one sentence at L0, two at L1, three at L2, and so on up. A folder beneath a layer keeps its sheet, since the tree and the first line are not design choices; what its sheet says is a design choice through and through, and the sheet may be blank: the first line and nothing else. A blank sheet is skipped, and it is tagged at the end of the document that collects the sheets — the republishing meant one day, which section 14 describes — as an audit exception for HOA review — a person's review, as every step is for now. The sheets in `aybllc/7lm` say a great deal more than that: they are complete, detailed, and rigorous — the full degree, every one of them — and they bind no one else's. A new repository's sheets start at the degree its owner chooses; three templates, one at each degree, are beside this guide at `L8/L6/7lm-sheet-templates.md`.

A sheet is a working document. It is read while filing, and it belongs to its folder: when the folder moves, the sheet moves with it. It is not a support document. Support is help for things that break, and it is a service to users; 7LM does not provide one. Its users are researchers working self-service, and a researcher whose work warrants technical support has an institution that provides it.

### The one CI check

There is exactly one automated check, identical in every 7LM repository, living at `.github/workflows/integrity.yml`. It fails on four things:

- an unresolved merge-conflict marker;
- a root that does not match the standard root above, which the specification calls canonical;
- a sheet whose first line is not its own path;
- a folder from the standard tree above with no sheet.

Any other folder missing a sheet only gets reported. The check never moves anything.

### Adding folders of your own

You can add folders under a canonical position for your own material, something like `L8/L5/research/review/some-work/`. Give each one a `0.md`; every folder carries one. The check reports a missing one rather than failing on it, and a folder without a sheet is outside the system. Both exemplar repositories do exactly this.

One of these has a standard name and meaning. `in/` is a position's inbox: what belongs to that position but has not been worked into it yet. `L8/L6/in/` holds what is L6's to keep and is not yet part of any record; `L8/L4/work/writing/in/` would hold a draft that belongs to that writing position and has not been taken up. Read it as the to-be and the to-do of the folder it sits in. Any position may have one, it is never required, and it carries a `0.md` like every other folder.

What you cannot do is add anything at the root, or remove or rename a canonical folder.

A retired set under `L8/L6/retired/<name>/` keeps its old sheets exactly as they were, headings and all. The check reads the set's own `0.md` and nothing beneath it, which is what lets retired material stay frozen.

---

## 11. Procedures

### Read a 7LM repository for the first time

1. Read `README.md`. It tells you what the repository is, the order to read things in, the root, and where the prior README is, and nothing more.
2. Read `L7/0.md`, the desk: sources, rights, peers, outward acts.
3. Read `L8/0.md`, the interior, which also carries the count rule.
4. Read the `0.md` of any folder you walk into. It tells you what belongs there.
5. Work inward as far as your question needs. L6, then L5, then L4, and onward.

### Start a new bounded object

1. Establish the bounded object and use the canonical topology as the coordinate system.
2. Give each current canonical directory a local `0.md` that states what occurs there. An unused branch may remain otherwise empty; its sheet is still the semantic statement of that coordinate.
3. State the foundational L0 meanings the object actually uses. They may be locally authored, externally adopted, adapted, or provisional. Preserve source provenance separately where relevant.
4. Populate additional layers only when the work genuinely has a representation of that type. Do not manufacture an L2 formula, L3 engineering object, L4 work event, or L7 relation merely to fill the sequence.

### Use a definition from an external source

1. Identify the definition that actually functions in the bounded object's semantic contract; its semantic representation belongs at L0.
2. Represent the external source relation at `L7/provenance/` when source identity, version, authority, lineage, or prior-art relation matters.
3. Represent governance conditions at `L7/governance/` only when such conditions actually apply.
4. Use `L7/peering/` only when the relationship with an identifiable external counterpart is itself being represented.
5. Preserve authorship/source attribution without treating source origin as a reason to move semantic meaning out of L0.

### Cite a source

1. Identify the source precisely enough for the research use at hand: citation, version/date, locator, archive identity, DOI, commit, or other distinguishing reference as appropriate.
2. Represent that source relation under `L7/provenance/sources/`.
3. Represent any relevant copyright, licence, permission, access, or controlled condition in its own governance position.
4. Store or access the source using an implementation suitable to the project. A curated archive is one option, not a 7LM requirement.
5. A source relationship is not automatically a peer relationship.

### File a piece of writing

1. The file itself goes to `L8/L4/work/writing/`.
2. What it argues goes to `L8/L5/`.
3. Its drafts and corrections get recorded at `L8/L6/history/`.
4. If it is released, its release identity goes to `L7/allications/publications/`.

### Handle something when you cannot tell where it goes

Put it in `L8/L5/research/review/`. That is what the catch-all exists for, and the owner decides from there. A wrong placement that looks orderly is worse than material left visibly unfiled.

If you know which position owns it but not where it goes inside that position, put it in that position's `in/` instead. The catch-all is for not knowing the layer; an inbox is for knowing the layer and not yet having filed the thing.

### Retire a prior state

1. Make a dated set under `L8/L6/retired/`, something like `L8/L6/retired/layout-2026-09-06/`.
2. Put the prior files inside it at their old relative paths, unchanged. Do not correct their headings.
3. Give the set its own `0.md` at its root, saying what the set is and where the current state now lives.
4. Record the retirement in `L8/L6/history/`.

Retire only what integrity needs in order to rebuild the past: the owner's authored documents, the rule texts of a prior layout, error records. Everything else superseded gets enumerated in the record and then deleted.

### Trace a fault

Find the first layer where a promise breaks, and fix it there. The specification does not dictate where you start. If you are coming from outside the object, use the inspection direction.

1. Start at L7. Is the external record right? Check the source, the version, the rights.
2. Drop to L6. What did this object used to be, and what changed?
3. Keep going inward until a layer's promise fails.
4. Fix it at that layer and version the change. Do not patch it from above.

---

## 12. Vocabulary

- **Bounded object.** One research thing with a clear edge: a definition, a theory, a project. Each 7LM repository is about exactly one, and when this guide says "the object," that is what it means.
- **Owner.** The local person or role responsible for a bounded 7LM object or repository. Source authorship, issuing authority, copyright ownership, and local repository responsibility are separate relations unless they happen to coincide.
- **HOA.** Human-only actions: the owner's marker for a step a person takes and nothing else does. Filing is one. Taking this guide from L6 and publishing a version of it is another.
- **Design choice.** What the model leaves to the owner of a repository. What a sheet says after its first line, the version of this guide an adopter publishes and where, and whether a position is used at all are design choices. The tree, the sheets' first lines, and the rule that the guides share no history are not.
- **Audit exception.** A blank sheet beneath a layer — the first line and nothing else — listed at the end of the document that collects the sheets, for HOA review.
- **USO.** The interior of a bounded object, living in `L8/`.
- **Sheet.** A `0.md` file, one per folder, stating the space of that folder and what it does. A working document, not a support document.
- **Rail.** One of the four L0 tracks: ontology, semantics, epistemic, universality.
- **Contract.** What a layer guarantees to the layer above it. This guide often just calls it a promise.
- **Admissible.** Permitted under the contract in force. L1's whole job is declaring which states are admissible and which are excluded.
- **Invariant.** A property that holds across every admissible state and does not change when other things do.
- **Representation.** One distinct way of stating a thing. The same topic can have a representation at several layers, each owned by exactly one of them.
- **Partial.** Said of an operation that is undefined across part of its domain. L2 requires an operation to declare this rather than imply totality.
- **Reconstructable.** Recoverable from the record itself. L6's standard: prior states, corrections, failures, and retirements can all be rebuilt from what is written down.
- **Supersede.** To replace a claim or a state with a later one while the earlier one stays on the record.
- **Local delta.** An exemplar term for an explicitly represented difference over a stated baseline. Useful in some implementations; not a universal peering requirement.
- **Pinned.** An implementation term meaning fixed to an exact version or revision. Pinning may be useful for reproducibility but is not the definition of peering.
- **Binding.** An implementation term for a recorded relation or reference between objects. A peering relation does not require every implementation to use a reference-only binding object.
- **Peer.** The word carries two senses and the specification uses one word for both. At `L7/peering/.../peer-N/`, a peer is an outside counterpart handing you something or receiving something from you. At `L8/L5/institution/peers/`, a peer is a participant position inside the research setting. File by whichever one you actually mean.
- **Catch-all.** `L8/L5/research/review/`, where anything waiting on the owner lands.
- **PARKED.** The label on catch-all material the owner has set aside.
- **Inbox.** An `in/` folder at any position, holding what belongs to that position and has not been worked into it yet.
- **Retire.** To mark or represent a prior state as no longer current while preserving enough information for reconstruction. Physical retention strategy is an implementation choice.
- **Enumerate.** A repository-specific reconstruction technique: list the parts of a superseded file and where they now stand. It is one possible implementation of L6 reconstructability, not a universal prerequisite to deletion.
- **The cut.** The boundary at L4 where a specification becomes something actually made.
- **The desk.** L7.

---

## 13. Common errors

**Treating L7 as the seventh layer.** It is not. The seventh layer is L6, and the count rule in section 3 explains why.

**Confusing semantic role with source provenance.** If an externally sourced definition actually functions as this object's L0 meaning, L0 is the correct semantic position. Preserve the source authorship/provenance separately; do not claim local authorship merely because the definition is used locally.

**Letting a well-argued L5 paragraph stand in for a missing L2 proof or L4 measurement.** Prose is not evidence. The hard boundary at L5 states this directly.

**Mapping a contained system's layers onto the 7LM layers.** An OSI stack sits whole inside L4. Questions about it may expand across the architecture; the stack does not.

**Confusing an L5 peer participant with an L7 external counterpart.** `L8/L5/institution/peers/` represents participant roles in research/discourse. `L7/peering/` represents an external counterpart relationship when that relationship itself matters. A standards body used only as a source may instead appear through provenance without peering.

**Deleting a file to tidy up.** Enumerate its parts first. Anything the repository needs in order to reconstruct its past is retired instead.

**Fixing a lower-layer problem by rewording a higher-layer document.** That is patching from above, and it is the exact move the debugging rule forbids.

**Reading the README for the layout.** The sheets state the layout. The README states what the repository is, the reading order, the root, and where the prior README is, and nothing more.

**Reading a sheet as a support document.** A sheet states the space of its folder and what it does. Help for something that has broken is not what it is for.

**Leaving a current canonical directory without a semantic sheet.** The local `0.md` is the directory's semantic statement: it says what occurs there and its boundary. The branch may otherwise remain empty when unused. A header-only sheet does not state the coordinate's meaning.

**Reading the archive's name, `l6`, as a layer name.** `aybllc/l6` is a separate repository. `L8/L6/` is the layer. The names collide; the things are unrelated.

---

## 14. Implementation examples (non-controlling)

The examples below record implementation history and are not part of the agnostic definition of 7LM. They have not been re-audited in this architectural pass and do not control the layer meanings above.

**`aybllc/7lm`** is the current scaffold holding the specification, canonical position sheets, and this field guide.

How a push from the scaffold is meant to reach an adopter, once the mechanism exists. The scaffold's update arrives, pinned to its hashes, as an item for HOA review at the adopter's `L7/peering/private/`: the scaffold is a peer, and its push is ingress. A person decides, item by item, to follow or to edit. The pushed tree is required; taking up everything in it is not, and what the person declines is listed in their HOA record rather than dropped without a trace. The push carries the tree and the sheets, never the scaffold's L6; no repository's history moves in either direction. Automating that review instead of doing it runs the risk the review exists to catch: a directory created outside the canon, which is an easy fix and a bad pull request. The path is meant to run the other way as well: an action from the scaffold collects the adopter's working guide, the version they actually work from, through their HOA, so that the source at L6 can learn from it. Meant one day: at the HOA step, one action republishes every sheet of the repository into a document in a default format, a `.docx`, whose format the team swaps for its own or chooses from several the scaffold issues; and, later, an option to put that out to a GitHub project or, perhaps, a docs site. None of this is built; for now every step is HOA. Today the mirroring is by hand, and what each adopter does with their guide is, as before, their design choice.

**`aybllc/autonomous`** defines the word *autonomous* out of codified standards, meaning standards written down by standards bodies. The nine bodies whose clauses feed that definition are bound as peers at public ingress, and the definition itself is exposed at public egress.

**`aybllc/auditonomous`** defines the coined word *auditonomous*. It binds the Autonomous definition at public ingress, reference-only, then writes only how its own word differs. The specification calls that difference a local delta.

**`aybllc/l6`** is the curated-source archive. It is not laid out as a 7LM repository at all. The others point at its files rather than copying them.

The specification calls `autonomous` and `auditonomous` its two exemplars, meaning its worked examples, and its section "Exemplars as instantiated" lists exactly what in them does not yet match the architecture, under the heading "Not yet as stated." Read that before you copy anything from either one. As of the version of 20 September 2026 it says this:

In Autonomous, the catch-all holds work belonging to other objects, and the provenance rows for the nine bound issuing bodies are not yet ledgered. In Auditonomous, the binding names the path the peer used before its own 7LM layout, three files still take a definition of *autonomous* from somewhere other than the binding, and the L0 epistemic rail is empty with its vocabulary standing at L5 as review status.

Keep the two claims separate. The design is one claim. How far each repository has been built is another.

---

## 15. Open calls

The specification records these as decisions the owner has not yet made.

A held-off rules file about what a session or a model may touch. The tree itself states no such rule, deliberately.

A set of inherited terms with no adjudicated position: *corpus* in its broad sense, *regress*, *found*, *caught*, *naught*, *origidity*, *certainty*, and *intolerance*. The specification preserves them as reserved vocabulary while their topology remains unadjudicated.

---

## 16. Where to read more

- The diagrams: the 7LM Plate Sheet, `L8/L0/pedagogy/7lm-plate-sheet.html`. One plate for now: the eight positions, with L8 drawn as the envelope around all of them, as the owner has described it.
- The specification: `L8/L4/work/writing/7lm-harmonized-architecture-specification.md` in `aybllc/7lm`.
- The interior sheet and the count rule: `L8/0.md`.
- The desk sheet: `L7/0.md`.
- The owner's definition "First is always 0": `L8/L0/semantics/definitions/FIRST_IS_ALWAYS_0.md`.
- How the layout came to be: `L8/L6/history/harmonization-2026-09-04.md`.
- The specification's own history, with the owner's words behind each rule: `L8/L6/history/specification-history.md`.

A note on older records. Anything dated before 12 September 2026 may write the interior as `USO/` and the layers as `l0` through `l6`. Read `USO/lN/` as `L8/LN/`, and `USO/` as `L8/`. Some older records go further back still and write lowercase `uso/`, which was an earlier layout's own path from before 24 August 2026. Leave those as they are.
