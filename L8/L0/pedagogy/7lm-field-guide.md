<!-- The 7LM field guide. Filed at L8/L0/pedagogy/ on 12 September 2026 as system-level traversal and attachment pedagogy,
     drawn from the specification (version of 12 September 2026) and the sheets. Where this guide and the specification
     differ, the specification controls. Record: L8/L6/history/harmonization-2026-09-04.md §15. -->

# The Seven-Layer Model: A Field Guide

Welcome aboard. This is the Seven-Layer Model, or 7LM for short. I am going to walk you through it the way I would walk a friend through it. Plain talk. One idea at a time. If you hit a word you do not know, jump to the word list in section 12 and come right back.

One rule before we start. Everything in this guide comes from the model's own rulebook, the specification, and from the little description files that live in every folder of the `aybllc/7lm` repository. If this guide and the specification ever disagree, the specification wins. Every time.

---

## 1. What the Seven-Layer Model is

Here is the big picture.

- 7LM is a way to organize research so that mistakes stay small and easy to find.
- At its heart, it is a folder layout. Every folder has one fixed job.
- Every folder also has one description file, named `0.md`. We call that file a sheet. The sheet tells you what the folder means and what belongs in it.
- 7LM is not software. Nothing runs by itself. People do the filing by hand, and that is on purpose.
- The whole model is written down in one document, the Harmonized Authoritative Architecture Specification. You will find it at `L8/L4/work/writing/7lm-harmonized-architecture-specification.md`.

### The one idea

Here is the whole thing in one breath. Different kinds of claims live in different places.

- Saying what a word means is one kind of claim.
- Saying which states are even possible is another.
- Saying what follows exactly, by math, is another.
- Saying what can be built within real tolerances is another.
- Saying what was actually built or measured is another.
- Saying what we conclude from all that is another.
- Saying what happened before, and what changed, is another.
- And saying how the work meets the outside world is the last one.

7LM gives each of those kinds its own position. The first seven kinds get the seven layers, L0 through L6. The last kind, meeting the outside world, gets the desk, L7. The desk is not a layer. Section 3 explains why, and it is worth the trip.

The payoff is this. A claim is only as strong as what its layer has actually earned.

### The debugging rule

When something goes wrong, find the first layer where a promise breaks. Fix it right there. Do not patch over it from higher up. That is the whole debugging philosophy, and you will see it again and again.

---

## 2. The positions, in one table

Read this table from the bottom up when you are building something. Read it from the top down when you are inspecting something. Both directions are real, and we will get to them.

| Position | Name | The question it answers |
|---|---|---|
| L7 | Surface / Forward Face (the desk) | What does the outside world need to see? Sources, rights, peers, publications. |
| L6 | Library / Memory | Can we rebuild what this object used to be and how it changed? |
| L5 | Research / Discourse | What can we responsibly conclude, question, teach, or decide? |
| L4 | Conversion / Realization | What was actually made, written, run, measured, or recorded? |
| L3 | Engineering Mathematics | How do we make the exact math workable, with real units, tolerances, and error bounds? |
| L2 | Formal Mathematics | What follows exactly when lawful operations act on the allowed states? |
| L1 | State Space | Which states are allowed at all, given the meaning we set? |
| L0 | Semantic / Foundational | What does this object mean, before anything else is said? |

Two more names you will see everywhere.

- **L8** is the folder that holds the seven interior layers. The specification calls it "the research packet on the desk." It is a count, not a layer. Section 3 explains what that means.
- **USO** is the name for what L8 holds. It is the inside of the bounded object. A bounded object is one research thing with a clear edge, like a single definition or a single project. So the folder is named `L8/`, and the thing inside it is called the USO.

And two facts about how these sit on disk.

- L7 is outside the packet. On disk, `L7/` and `L8/` sit side by side. When you step from the desk into L6, you are crossing a boundary. You are not opening a subfolder.
- Nothing comes after the desk. Past it, the count starts over at zero in some other object's tree. Out there, this whole object is just one bound object at somebody else's peer position.

---

## 3. The count rule: "First is always 0"

Okay. This is the part that trips everybody up, so let's slow down and get it right.

The owner's rule is short. First is always 0. It comes with this table:

| semantic | > | magnitude |
|---|---|---|
| FIRST | is | 0 |
| SECOND | is | 1 |
| THIRD | is | 2 |
| FOURTH | is | 3 |

Here is how to read that. Words like "first" and "second" are meanings. Numbers like 0 and 1 are magnitudes. The relationship between them is the word "is." First is 0. Second is 1. And so on.

Now apply it to the layers.

- The seven layers are L0, L1, L2, L3, L4, L5, and L6.
- So the seventh layer is L6. In the owner's own words: "layer 7 will always be layer 6."
- L7 carries the number 7, but it is not a layer. It is the desk. If you count up from L0, it is the eighth position you reach.
- L8 is not a position at all. It is the count of the eight positions, L0 through L7. It is also the name of the folder that holds the interior.

The names are design, not decoration. The owner was clear about that.

- L7 is pronounced "El-Seven," and the name is a picture. Look at the two characters. The L is the left side and the bottom edge of a desk, seen from above. The 7 is the top edge and the right side. Put them side by side, in the right font, and L7 draws a rectangle. That rectangle is the desktop. That is the joke, and the owner made it on purpose.
- L8 is two zeros stacked on top of each other. Because the count starts at L0, every layer has a zero, its `0.md`. The interior has its own zero too, `L8/0.md`. Put the interior's zero over the layers' zeros and you get 0 over 0, which is an 8. And an 8 is a closed shape. L8 encloses the seven layers inside it. That is the second joke, and it is the same kind as the first.
- L0 through L7 are the eight bits of a byte. L8 is the extra bit. Like a check bit in computing, it carries the meaning and catches an error.

---

## 4. The two directions

There are exactly two legitimate ways to move through this structure. Not three. Two.

**Building goes outward.** The specification calls this construction.

- You start at L0 and move up: L1, then L2, then L3, then L4, then L5, then L6, and finally L7.
- You only move up when the layer below you has settled its promise.
- Sometimes there is no settled way to carry your work into the next layer yet. When that happens, you stop. The specification calls the missing link a "bridge." Stopping at a missing bridge is not a failure. The specification calls it "honest placement." You put the work where it has actually earned a place, and you leave it there.

**Inspecting goes inward.**

- You start at L7 and move down: L6, then L5, then L4, then L3, then L2, then L1, and finally L0.
- Think of it as an outsider arriving. They meet the desk first (L7). Then the memory (L6). Then the research (L5). Then the actual work (L4). Then the math and the allowed states (L3, L2, L1). Last of all, the meaning (L0).

One caution, straight from the specification: "Description does not become prescription merely because the structure can be traversed." In plain English, just because you can walk a path does not make that path a rule.

---

## 5. The rules that hold everywhere

These rules apply at every layer, all the time. Learn them and most filing questions answer themselves.

- **Higher layers do not silently repair lower layers.** Say the research at L5 needs a word at L0 to mean something slightly different. You do not quietly reinterpret L0. You change L0 out in the open, with a new version.
- **Each way of stating a thing lives at the lowest layer that can state it correctly.** One topic can show up at several layers. That is fine. But each appearance belongs to exactly one layer.
- **Change one layer at a time.** A fix at one layer never quietly rewrites another.
- **Empty folders are fine.** Every repository carries the whole layout, even the parts it does not use yet. An unused folder is an available capability, not a failure. The specification's own example is a classroom experiment. It can leave the governance and publications folders empty. Later, a science fair, a public release, or a patent can fill them without changing the layout at all.
- **The sheet carries meaning. Metadata carries machine instructions.** The `0.md` file is written for people. Machine metadata, if there ever is any, is attached to the folder itself. It is not a file in the tree, and it is not drawn as a branch. So do not go creating one. Right now, no machine metadata is switched on in the scaffold or in either exemplar. Everything is manual. The specification does not assume automation has been turned on or tested.
- **Build whatever the math permits. Claim only what the layer has earned.** This one is the owner's, and it does a lot of work. Valid math at L2 does not, by itself, become an engineering claim at L3. It does not, by itself, become a claim about measured results at L4. And publishing something at L7 never makes the claim any stronger.
  - The model is not against speculation. You are free to state a hypothesis and explore it in math.
  - The specification's example is faster-than-light travel. Peer-reviewed faster-than-light math can be perfectly good math. It stays at L2. It gets no free ride to "buildable propulsion" at L3 or L4. Stopping at L2 is not rejection. It is honest placement.
  - Assumed powers like faster-than-light travel, unlimited power, perfect information, zero latency, or infinite endurance can be studied on condition. What they cannot do is serve as free evidence. If a claim leans on one of them, that power has to carry its own engineering and evidence burden first.
  - Nothing unobserved or unbuilt gets pushed down into the foundational or physical claims.

---

## 6. Each layer, a little closer

### Groups that are not folders

Before we go layer by layer, a quick warning. The specification sometimes talks about layers in groups. None of those groups is a folder. Under `L8/`, the seven layer folders sit side by side, flat.

- L6 and L5 together are called the "upper interior." That is memory and research. They are still two separate owners.
- L4 by itself is called the "realization bay." A whole built system can sit inside it, with its own internal layers.
- L3, L2, and L1 together are the "technical-possibility bundle." You look at all three when a question needs engineering, exact math, and allowed states at the same time.
- L3 and L2 by themselves are a tighter pair. You use that pair when L1 is already settled and nobody is questioning it.
- L0 stands apart from L1 on purpose. L0 says what things mean. L1 says which states are allowed under that meaning.

A question can pass through some layers and skip others. Each piece of the answer still belongs to exactly one layer. Whatever you do, do not make a folder for a group.

### L0: Semantic / Foundational

- This is where the object's own meaning lives. The meaning this object itself authored.
- There are four "rails" here: ontology, semantics, epistemic, and universality. Each rail has its own folder.
- There is a fifth folder, pedagogy. It explains how to walk the layers and how to connect this object to other objects. It is a folder, not a rail.
- `semantics/definitions/` holds the definitions this object actually wrote.
- Somebody else's definition never gets copied in here to fill space. It gets bound at the desk instead. Section 8 covers that.
- One open research note from the owner. "Semantic drift," meaning slipping away from what L0 set down, is suspected to start right here. That is a hypothesis, not a settled rule.

### L1: State Space

- The job here is to "freeze the board." Which states are allowed? Which are excluded? What never changes? Those last ones are the invariants.
- There is one folder: `state-space/`.
- There is no motion here. No calculation, no transformation. All of that starts at L2.
- Sometimes a result falls outside the declared state space. When that happens, one of two things is true. Either the construction is invalid, or the state space needs an explicit, justified extension. Nothing steps outside quietly.

### L2: Formal Mathematics

- Exact objects only. Symbols, types, relations, operators, proofs, derivations.
- There is one folder, `formal-mathematics/`, and it holds three more: `relations/`, `operators/`, and `proofs/`.
- Every symbol has to trace back to an L0 meaning and an L1 allowed state.
- Every operation says what it takes in and what it gives out. Mathematicians call that its domain and codomain. If it does not work on every input, it says so. That is called being partial.
- Unproved claims get marked unproved. Writing something down does not promote it.
- There are no tolerances or approximations here. Those belong to L3.

### L3: Engineering Mathematics

- This is where the exact math gets made workable. L3 handles units, precision, approximation, tolerance, uncertainty, complexity, and operating regions.
- There is one folder, `engineering-mathematics/`, and it holds three more: `approximation/`, `uncertainty/`, and `tolerances/`.
- Here is where a formula goes. Its meaning, in words, goes to L0. The exact formula goes to L2. The formula as you actually apply it, with approximations, tolerances, adaptation, or open ends, goes to L3.
- The specification carries a working hypothesis here. Math that depends on continuation, feedback, adaptation, tolerance, uncertainty, or exchange with an environment begins at L3. L2 can state exact relations about a living or adaptive thing, but L2 does not "support" that thing. The specification marks this as a hypothesis until it is tested.
- L3 tells L4 what can be built or run, and under what conditions.
- L3 does not produce evidence itself. That is L4's job.

### L4: Conversion / Realization

- This is where resources get spent and something identifiable comes out the other side.
- The specification's phrase for it is any conversion between intellectual property and energy, in either direction. Careful with that phrase. Here, "intellectual property" means ideas and intellectual objects, like a piece of writing or a model. It does not mean legal rights like copyright or patents. Those live at L7, and section 8 covers them.
  - Ideas to energy looks like writing, computing, running an experiment, building, deploying, or teaching.
  - Energy to ideas looks like measurements, observations, datasets, and recorded failures.
- There is one folder, `work/`, and it holds three more: `writing/`, `experiments/`, and `computation/`.
- A whole system with its own internal layers sits inside L4 as one object. The classic example is a complete OSI network stack, which has seven layers of its own. Its internal "layer 7" is not 7LM's L7. Do not mix them up.
- Now, you can ask two very different questions about that same system, and they file differently.
  - "How does it run?" The whole stack is one L4 object. Its own layers stay its own.
  - "Where did it come from, and why is it built this way?" That question spreads out. Each answer goes to the layer that owns it. The standards bodies and source bindings go to L7. Its development history goes to L6. The debate about why it took its shape goes to L5. The engineering trade-offs that shaped it go to L3. Exact relations go to L2, but only where they are truly warranted. Allowed states go to L1 when they are part of the question. The words this object itself coins to describe it go to L0.
  - The stack does not move when the question spreads. It stays at L4. The specification calls this the difference between "operational containment" and "analytic expansion."
  - A network fault inside the stack is an L4 fault, unless somebody separately shows it touches another layer's object.
- The owner calls this layer "the cut." Below L4, things are specified. At L4, things are made.
- Failures get filed too. A failed run, a broken build, a measurement that went sideways. Each one is an L4 object, recorded as a failure. It does not get turned into a conclusion.
- Every L4 filing stays traceable. Inputs, conditions, what was done, results, tests, rework. The lower-layer contracts it depends on are pinned, and you can find them.
- L4 does not get to interpret its own results. That is L5's job.

### L5: Research / Discourse

- This is interpretation, review, judgment, argument, and teaching.
- `research/lanes/` holds distinct lines of inquiry, one lane per question. It is also what the model calls the "working position." Section 9 explains that.
- `research/review/` holds review, criticism, and audit. It is also the catch-all. Section 9 explains that too.
- `research/findings/` holds what you can responsibly state from the evidence. A finding carries what it rests on, with citations. It carries its limits and its uncertainty. It carries its review status. And it carries whatever someone would need to reproduce it. A finding is never broader than its evidence.
- A review names the claim it is reviewing and says one of four things: accept, reject, qualify, or supersede. A review can ask a lower layer to revise. It does not reach down and fix the lower layer itself.
- `institution/peers/` and `institution/undergraduates/` record who takes part. They do not record what the research says.
- The hard boundary at L5 is this. Consensus, prose, authority, or usefulness never substitutes for proof or measurement. Never.
- One more. A scale, a ladder, or a set of status labels is an L4 object as a written thing. What it means is L5 discourse. It is never an L1 state space and never L2 math.

### L6: Library / Memory

- This is what the object used to be, and how it changed.
- There are two folders. `history/` holds the records of change. `retired/` holds prior states, kept exactly as they were.
- Git history helps, but it is not the same thing as scientific memory. The record in L6 is the memory. A Git commit identifier is only a pointer to it.
- Correcting something never requires deleting the prior state.

### L7: Surface / Forward Face

- This is the desk. It is where the object meets people, institutions, other repositories, legal conditions, and publications.
- There are four folders: `provenance/`, `governance/`, `peering/`, and `publications/`.
- Being on the desk proves nothing by itself. Provenance, custody, copyright, and publication each answer a different question. None of them makes a claim true.

---

## 7. Where things go: the filing cases

One thing can show up in several layers, with each layer owning a different aspect of it. This table uses the four desk folders, provenance, governance, peering, and publications. Section 8 explains each one, so peek ahead if you need to.

| Thing | Where its parts go |
|---|---|
| A written document | Making the file is L4. Its argument is L5. Its version history is L6. Its released publication is L7. |
| An experiment | Running it and the raw results are L4. Method and tolerance are L3. Exact relations are L2. Which states are possible is L1. The conclusion is L5. |
| Code | Algorithm and engineering choices are L3. A formal proof or model is L2. Execution, deployed bytes, and results are L4. |
| Data | Collected and stored instances are L4. Precision is L3. Formal encoding is L2. State categories are L1. External source and lineage are L7. Its own development history is L6. Interpretation is L5. |
| A definition someone else owns | The owner stays external, at L7 peering. Source and version are L7 provenance. Legal conditions are L7 governance. Use history is L6. Interpretation is L5. L0 holds a definition only if this object writes its own. The external one is never copied in. |
| A publication | Producing it is L4. Its scholarly meaning is L5. Its internal history is L6. Provenance, rights, and the released object are L7. |
| A system with its own layers, like an OSI stack | Running it is L4, whole. Questions about its origin, history, or design each go to the layer that owns the answer. The system itself is never re-mapped onto 7LM layers. |
| A forum, chat, or discussion tool | The tool as built and run is L4. Its outside face is L7. The roles, discussion, review, and judgments carried through it are L5. |
| Research as a whole | The work events are L4. Interpretation and review are L5. Internal memory is L6. External provenance and what is shown outside are L7. Each lower layer owns its own piece. |

---

## 8. The desk in detail: provenance, governance, peering, publications

Let's spend some time at the desk. This is where most newcomers get tangled up, and it is also where the model does some of its smartest work.

### Provenance (`L7/provenance/`)

- Provenance answers four questions. Where did a thing come from? What came before it? Which version is in use? And who speaks for it?
- There are four folders: prior-art, sources, lineage, and authority.
- Source files are not stored here. They are pointed to. A designated archive repository holds them. That archive is bound once at private ingress, and it is read-only from every repository that uses it. A repository that uses a source keeps one row for it in a list, called a ledger. The row gives the file's path in the archive and the exact archive version it is pinned to. No source file ever gets copied in.
- In the repositories described in section 14, the archive is `aybllc/l6`. That is a fact about those repositories, not a rule of the model. Another 7LM object could name a different archive, or none at all.

### Governance (`L7/governance/`)

- Governance holds the legal and access conditions: copyright, licensing, patents, permissions, access, and restrictions.
- Copyright has exactly one place: `governance/copyright/`. You state every copyright or licence condition there, once. The licensing and restrictions folders point to it instead of repeating it.

### Peering (`L7/peering/`)

- A peer is any party this object exchanges things with. It could be a person, an institution, a standards body, another repository, an archive, or a model session. Any number of peers can meet the object at the same time. Each one gets its own numbered position.
- Two independent distinctions organize this folder.
  - Exposure is either `public/` or `private/`.
  - Direction is either `ingress/` (coming in) or `egress/` (going out).
- Under each direction, `peer-N/` names one peer, where N is its number. Under a peer, `object-M/` names one thing exchanged with it, where M is its number.
- A peer's `0.md` sits one level above that peer's objects. It is the owner's list of those objects and where each one stands. A person writes it.
- A bound object never moves and never changes. When a decision gets made about it, the decision goes in that list. The choices are authorized, denied, quarantined, or retired. The record of the decision goes to `L8/L6/history/`. A binding that is no longer active gets retired to `L8/L6/retired/`. It is never erased.
- Whatever a peer brings in takes one path. It gets compared and judged at `L8/L5/`. Only what survives that gets carried inward, and it is written as this object's own work, citing the bound object. A person's manuscript, a standards clause, and a model's draft all take exactly the same route.
- The path tells you who brought a thing before anyone reads it. The specification calls this provenance by position.
- To change a peer's object, you go to its owner. You can update or retire your binding. You do not edit theirs.
- Egress is not publication. Handing an object to a named peer is egress. A public release with a release identity goes in `publications/`.

### Where the desk rules came from

- These peering rules grew out of one real problem. Two research objects, Autonomous and Auditonomous, had to share one definition without both of them owning it.
- The answer was this. One object can depend on another without owning, copying, redefining, or maintaining the other's meaning. The `peer-1/object-1/` structure is the general form of that answer.
- Autonomous has one job. It freezes the narrowest agreement its bound standards actually share. Where the sources disagree, it does not invent agreement. Each disagreement stays tagged with its source and stays visible.
- Auditonomous takes that frozen baseline and writes only its own difference. The specification calls that difference a local delta. The baseline and the delta stay separately owned. They are laid over each other, never blended.
- An argument about one object never silently counts as an argument about the other. A claim that crosses objects has to name the relation or the hand-off.
- The specification is emphatic about this case. It calls it "not an optional exemplar" but the originating boundary test of the whole architecture.

### The peering rule for definitions

- A definition lives once, at its owner.
- When this object uses another object's definition, the definition travels a fixed route. It starts at the owner's L0. It leaves through the owner's L7 egress. It enters through this object's L7 ingress. It arrives at this object's L0.
- The bound object is reference-only. The receiving repository may not edit it and may not delete it. The specification writes this as NO EDIT and NO DELETE.
- Wherever it is used inside, it carries a tag that never changes: object identity, owner, source layer, version, and ingress binding.
- If the owner changes the definition, that creates a new binding. The pinned one does not change.
- The receiver takes the owner's exact definition as authoritative for what the owner means. That is declared trust. It is not a claim that the definition is true.

### Publications (`L7/publications/`)

- This holds released objects, each with a release identity. The writing stays at L4. The meaning stays at L5. The history stays at L6.

---

## 9. Two working habits the model requires

Two habits keep the whole thing honest. Get these into your hands and the rest follows.

### The catch-all

- Everything waiting for the owner's review lands at `L8/L5/research/review/`. All of it, however much there is.
- When the owner takes something up, it moves to `L8/L5/research/lanes/`. That is the working position. If the owner sets it down again, it moves back to review. Position is state. The moves are the record, and nothing gets deleted.
- What the owner sets aside stays in review, labelled PARKED.
- Finished work gets filed at its layer.
- You do not need any other position or any new folder for this.

### Nothing is deleted before it is enumerated

- To enumerate a file means to list every part of it and where each part now stands. The word list in section 12 has it too.
- The rule that actually gets enforced is integrity. The repository has to stay whole and reconstructable. "Nothing is deleted" is not a separate rule. It follows from integrity.
- Some things have to stay readable in the repository so its past can be rebuilt. Those get retired to `L8/L6/retired/`, not deleted. Think of the owner's authored documents, the rule texts of a prior layout, and error records.
- A superseded file, meaning one that has been replaced, gets deleted once every part of it is listed in a record at `L8/L6/history/`. The record says where each part now stands. It is deleted, not retired. That is the ordinary act. Git keeps the change event. The record keeps the list.
- The one automated check on the repository, the CI check in section 10, checks integrity. It does not check for the absence of deletion.

---

## 10. The layout every 7LM repository shares

The root is the top folder of the repository. It holds `README.md`, `L7/`, and `L8/`. It may also hold two things that are repository infrastructure, not layers: the one CI workflow under `.github/`, and a `.gitignore` if there is anything to ignore. Nothing else goes at the root. Every 7LM repository has the same root.

The README is where you start. It is not the documentation. The documentation is the sheets and the specification.

In the tree below, `/0` after a folder name means the folder carries its `0.md`.

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

### The sheet rule

- Every folder has a `0.md`.
- The first line of that file is the folder's own path. For example, `# L8/L3/engineering-mathematics/`.
- After that, the sheet says what the folder is, why it exists, what it holds, and what it does not hold.

### The one CI check

There is exactly one automated check, and it is the same in every 7LM repository. It lives at `.github/workflows/integrity.yml`. It fails when it finds any of these four things:

- an unresolved merge-conflict marker;
- a root that does not match the standard root shown above. The specification calls that root "canonical";
- a sheet whose first line is not its own path;
- a folder from the standard tree above that has no sheet.

For any other folder without a sheet, it only reports the gap. It never moves anything.

### Adding folders

- You can add folders under a canonical position for your own material. For example, `L8/L5/research/review/some-work/`. Give each one a `0.md` when you can. The CI check will report a missing one, but it will not fail on it.
- You cannot add anything at the root. You cannot remove or rename a canonical folder.
- A retired set under `L8/L6/retired/<name>/` keeps its old sheets exactly as they were. The CI check reads the set's own `0.md` and nothing below it.

---

## 11. How to do common things

Enough theory. Here is how you actually do things.

### Read a 7LM repository for the first time

1. Read `README.md`. It tells you what the repository is and the order to read things in. It is not the documentation.
2. Read `L7/0.md`. That is the desk: sources, rights, peers, and publications.
3. Read `L8/0.md`. That is the interior, and it carries the count rule.
4. Read the `0.md` of any folder you walk into. It tells you what belongs there.
5. Go inward from there. L6, then L5, then L4, and so on, as far as your question needs.

### Start a new bounded object

1. Copy the full layout. Leave the unused folders empty.
2. Write the object's own definition under `L8/L0/semantics/definitions/`. If you have not written one yet, leave the folder empty. Do not paste in somebody else's.
3. Move outward only as each layer settles its promise.

### Use a definition owned by someone else

1. Bind it at `L7/peering/public/ingress/peer-N/object-M/`. Use private instead of public if the exchange is controlled. The folder holds a binding record, not the definition. The record carries the object identity, the owner, the source layer, the exact version, this ingress position, and the standing. No file of the peer's is held.
2. Add one row at `L7/provenance/sources/`.
3. State any rights conditions once, at `L7/governance/copyright/`.
4. Refer to it inside with its tag, at L0 or at any layer that needs it. Never write it into `L8/L0/semantics/definitions/`.
5. Record the binding event at `L8/L6/history/`. If the owner later changes the definition, add a new binding beside the old one and retire the old one to `L8/L6/retired/`.

### Cite a source, like a paper, a standard, or a document

1. The source file stays in the designated archive. The archive is bound once at `L7/peering/private/ingress/peer-N/` and is read-only from this repository. For the repositories in section 14, that archive is `aybllc/l6`.
2. Add one row at `L7/provenance/sources/`. The row carries an ID, the citation, the archive path, and the archive commit you read it at.
3. If the source carries a copyright or licence condition, state it once at `L7/governance/copyright/`.
4. Quote and cite in your work, and point to the row. Never copy the source file into this repository.
5. If the archive does not hold the source, ask the archive's owner to add it. Do not put the file here.

### File a piece of writing

1. The file itself goes to `L8/L4/work/writing/`.
2. What it argues goes to `L8/L5/`.
3. Its drafts and corrections get recorded at `L8/L6/history/`.
4. If it gets released, its release identity goes to `L7/publications/`.

### Handle something you are not sure where to put

Put it in `L8/L5/research/review/`. That is exactly what the catch-all is for. The owner decides from there.

### Retire a prior state

1. Make a dated set under `L8/L6/retired/`. For example, `L8/L6/retired/layout-2026-09-06/`.
2. Put the prior files inside it at their old relative paths, unchanged. Do not fix their headings.
3. Give the set its own `0.md` at its root. Say what the set is and where the current state now stands.
4. Record the retirement in `L8/L6/history/`.

Retire only what integrity needs in order to rebuild the past. That means the owner's authored documents, the rule texts of a prior layout, and error records. Anything else that has been superseded gets enumerated in the record and then deleted.

### Trace a fault

The rule is simple. Find the first layer where a promise breaks, and fix it there. The specification does not tell you where to start. If you are coming from outside the object, use the inspection direction.

1. Start at L7. Is the external record right? Check the source, the version, and the rights.
2. Go to L6. What did this object used to be? What changed?
3. Keep going inward until a layer's promise fails.
4. Fix it at that layer. Version the change. Do not patch it from above.

---

## 12. Vocabulary

- **Bounded object.** One research thing with a clear edge, like a definition, a theory, or a project. Each 7LM repository is about one bounded object. When this guide says "the object" or "this object," that is what it means.
- **Owner.** The person who runs a 7LM repository and decides what gets filed where. Sections 9 and 11 lean on this sense. A definition's owner is the object that wrote it. Section 8 uses that sense.
- **USO.** The interior of a bounded object. It lives in `L8/`.
- **Sheet.** A `0.md` file. There is one per folder.
- **Rail.** One of the four L0 tracks: ontology, semantics, epistemic, and universality.
- **Contract.** What a layer promises to the layer above it. This guide usually just says "promise."
- **Pinned.** Fixed to an exact version, usually a commit.
- **Binding.** The reference-only link to a peer's object at L7.
- **Peer.** This word has two senses, and the specification uses one word for both. At `L7/peering/.../peer-N/`, a peer is an outside counterpart: a person, an institution, a standards body, a repository, an archive, or a model session that hands this object something or receives something from it. At `L8/L5/institution/peers/`, a peer is a participant position inside the research setting. File by whichever one you actually mean.
- **Catch-all.** `L8/L5/research/review/`. Anything waiting on the owner lands there.
- **PARKED.** The label on catch-all material the owner has set aside.
- **Retire.** To move a prior state to `L8/L6/retired/` unchanged, instead of deleting it.
- **Enumerate.** To list every part of a file and where each part now stands, in a record, before the file gets deleted.
- **The cut.** The boundary at L4 where a specification becomes something actually made.
- **The desk.** L7.

---

## 13. Common mistakes

I have watched smart people make every one of these. Save yourself the trouble.

- Treating L7 as the seventh layer. It is not. The seventh layer is L6.
- Copying an external definition into L0 to "complete" it. Bind it at the desk instead.
- Letting a well-written L5 argument stand in for a missing L2 proof or a missing L4 measurement. Good prose is not evidence.
- Mapping the layers of a contained system, like OSI, onto the 7LM layers. A contained system sits whole inside L4. Questions about that system can still spread to other layers. The system itself does not.
- Filing an outside repository, archive, or standards body at `L8/L5/institution/peers/`. Outside counterparts belong at `L7/peering/`. The institution folder holds participant positions only.
- Deleting a file to clean up. List its parts first. That is enumeration. Anything the repository needs to rebuild its past gets retired, not deleted.
- Fixing a lower-layer problem by rewording a higher-layer document. That is patching from above, and it is exactly what the debugging rule forbids.
- Using the README as documentation. The sheets are the documentation.
- Reading the archive's name, `l6`, as a layer name. `aybllc/l6` is a separate repository. `L8/L6/` is the layer.

---

## 14. Where it is used today

- **`aybllc/7lm`** is the scaffold. It holds the specification and one sheet for every canonical position.
- **`aybllc/autonomous`** defines the word "autonomous" from codified standards, meaning standards written down by standards bodies. The nine bodies that issued those standards are bound as peers at public ingress. Its own definition is exposed at public egress.
- **`aybllc/auditonomous`** defines the coined word "auditonomous." It binds the Autonomous definition at public ingress, reference-only. Then it writes only how "auditonomous" differs from that definition. The specification calls this difference a "local delta."
- **`aybllc/l6`** is the curated-source archive. It is not laid out as a 7LM repository. The other repositories point to its files instead of copying them.

The specification calls `autonomous` and `auditonomous` its two exemplars, which is to say its worked examples. Its section "Exemplars as instantiated" lists what in them does not yet match the architecture, under the heading "Not yet as stated." Read that before you copy anything from them. As of 12 September 2026, here is what it says.

- In Autonomous, the catch-all holds work that belongs to other objects, and the provenance rows for the nine bound issuing bodies are not yet ledgered.
- In Auditonomous, the binding names the path the peer used before its own 7LM layout. Three files still take a definition of autonomous from somewhere other than the binding. And the L0 epistemic rail is empty, with its vocabulary standing at L5 as review status.

Keep these two claims apart in your head. The design is one claim. How far each repository has actually been built is a separate claim.

---

## 15. Still being decided

The specification records a few decisions the owner has not made yet.

- Peers are numbered from 1, while layers count from 0. Whether to change that is the owner's call.
- There is a held-off rules file about what a session or a model may touch. The tree itself states no such rule.
- Some older words in the records have no home yet: corpus in its broad sense, regress, found, caught, naught, origidity, certainty, and intolerance. The specification keeps them "reserved." Do not make a folder for any of them.

---

## 16. Where to read more

- The specification: `L8/L4/work/writing/7lm-harmonized-architecture-specification.md` in `aybllc/7lm`.
- The interior sheet and the count rule: `L8/0.md`.
- The desk sheet: `L7/0.md`.
- The owner's definition "First is always 0": `L8/L0/semantics/definitions/FIRST_IS_ALWAYS_0.md`.
- The record of how the layout came to be: `L8/L6/history/harmonization-2026-09-04.md`.
- The specification's own history, with the owner's words behind each rule: `L8/L6/history/specification-history.md`.

One last note, about older records. A record dated before 12 September 2026 may write the interior as `USO/` and the layers as `l0` through `l6`. Read `USO/lN/` as `L8/LN/`, and `USO/` as `L8/`. Some older records also write lowercase `uso/`. That was an earlier layout's own path, from before 24 August 2026. Leave it exactly as it is.

That is the tour. Go find the first layer where the promise breaks.
