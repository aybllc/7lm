# Seven‑Layer Methodology v1.3 — Immutable Math, Contracts, and Operational Lexicon

> Purpose. A domain‑agnostic, OSI‑style stack for creating and storing scientific theory and experimentation. Layers 0–3 are pure mathematics; Layers 3–4 introduce variables (IV/DV) and technical infrastructure (encoding, storage, transport). Every layer is immutable in place; evolution occurs via pinned, versioned conservative extensions or refinements. No examples appear in this document; all symbols are abstract.

> Notation. MUST/SHALL are normative; MAY is permissive. UN denotes the "broken‑0" unknown value. USS denotes the Unified State Space. "Pinned" means an exact, immutable reference to a specific version.

---

## 0. Stack‑Wide System Invariants (S‑invariants)

S1 — Monotone Knowledge Flow. Claims at layer k are derivable solely from artifacts at or below k. No upward layer introduces unproven assumptions about lower layers.

S2 — Conservative Evolution (0–2). Layers 0–2 SHALL only change via conservative extensions: previously valid theorems over the old vocabulary remain valid. No in‑place mutation.

S3 — Refinement (2–4). Layers 3–4 evolve by precision‑increasing refinements that do not alter prior denotations relative to Layer 2 precision.

S4 — Determinate Interfaces. Every inter‑layer interface is specified as total functions or set‑valued maps with explicit codomain and error/uncertainty structure.

S5 — Version Pinning. All cross‑layer references pin exact semantic versions. No "moving floor."

S6 — Append‑Only Evidence. Once committed at Layer 4, evidence is never edited — only superseded by addition at 5–6.

S7 — Provenance Preserved. Identity, authorship, parameters, and transformations are cryptographically or logically bound and transitively carried forward.

---

## 1. Layer Contracts (L0–L6)

### 1A. Unified State Space (USS) — Formal Core

Goal. Provide a single, layer‑compatible state‑space backbone that each layer maps to or quotients from, preserving immutability and agnosticism.

Pinned objects (L1).

- State space S with chosen structure (e.g., topology, sigma‑algebra, algebraic operations as required). Once chosen, this structure is pinned.
- Index set E (time or ordering) with a monoid structure (E, op, zero). Deterministic or stochastic evolution is indexed by E.
- Action monoid U (abstract controls or inputs). No domain semantics are attached to elements of U.

Dynamics (L1 to L3).

- Transition map F: S x U x E -> S (deterministic) or a stochastic kernel K from S x U x E to S. Composition respects E's monoid law.

Observation (ties to L2).

- Quantization at L2 induces a quotient q_Pi: S -> S_Pi for each precision profile Pi. Define a pseudometric d_Pi where d_Pi(x, y) = 0 iff q_Pi(x) = q_Pi(y).
- Observation map O_Pi: S -> Y_Pi factors through q_Pi: there exists Otilde_Pi: S_Pi -> Y_Pi with O_Pi = Otilde_Pi after q_Pi. Observability at precision Pi requires: if O_Pi(x) = O_Pi(y) for all admissible indices or trajectories, then x and y are equivalent at Pi.

UN / Broken‑0 (L0 coupling).

- Provide a Galois‑style abstraction: alpha: S -> R and gamma: R -> P(S) with alpha(x) <= r iff x is in gamma(r). UN is the bottom of R. Refinements in R are monotone lifts to subsets of S.

Variables and design (L3).

- A variable is a typed map v: S -> Val with a role tag in {IV, DV, Control, …}.
- Design operators are endomaps on product spaces built from S, U, E (e.g., assignment, blocking, conditioning) that transform admissible experiment tuples without adding semantics.

Encoding and transport (L4).

- Encode/Decode satisfy decode(encode(q_Pi(x))) = q_Pi(x). Commitments bind code to Otilde_Pi, q_Pi, and the USS version.

Provenance and discourse (L5–L6).

- A trajectory is a finite or countable sequence (x_t, u_t) indexed by E, with images under O_Pi. L6 stores trajectories and morphisms between them as edges in the provenance DAG; L5 reasons over pinned USS components.

System‑level properties.

- Controllability (abstract). For states x, y in S, there exists a finite control word and indices such that F (or K) reaches a state equivalent at Pi to y from x.
- Identifiability (abstract). Parameters theta in a chosen USS‑compatible family are identifiable at Pi if equality of induced observation laws implies theta equality up to Pi‑equivalence.

Compliance hooks.

- L0: alpha and gamma proven; UN typed per sort.
- L1: S, Sigma, topology, E, U pinned; conservative extensions only.
- L2: each Pi defines equivalence ~_Pi and d_Pi; refinement partial order over Pi.
- L3: variables and operators typed over S_Pi; role tags enumerated.
- L4: encode/decode proofs up to Pi; commitments bind to USS version.
- L5–L6: trajectories and inference artifacts append‑only with typed edges.

---

### L0 — Resolution Basis and UN (Epistemic Axiom Layer)

Intent. Formalize the presence of missing values without domain semantics.

Structures.

- A resolution lattice R with partial order <= and bottom element UN.
- Refinement maps rho: R -> R that are monotone: x <= rho(x).
- Closure invariants at L0 are algebraic properties over R (e.g., defined meets/joins when applicable), not narrative claims.

Obligations upward. L1 logic and type systems MUST preserve <= and treat UN as a well‑typed bottom. L2–L4 MUST never coerce UN to determinate values.

---

### L1 — Immutable Mathematics

Intent. Fix base logic, type theory, and abstract state spaces independent of measurement.

Structures.

- Base logic (pinned), type system, and state spaces S.
- Admissible transformations on S and proof obligations.

Evolution. Only conservative extensions (S2). Prior theorems remain true in prior vocabulary.

Obligations upward. L2 MUST present finite‑precision objects as quotients or refinements of S and supply proof terms tying back to L1.

---

### L2 — Finite Precision Mathematics

Intent. Introduce quantization, thresholds, and uncertainty as pure math.

Structures.

- Precision profiles Pi and quantizers q_Pi: S -> S_Pi.
- Uncertainty semantics as first‑class types (intervals, sets, or abstract elements), with comparison laws.

Evolution. Refinements that strictly increase resolution without invalidating prior denotations (S3).

Obligations upward. L3 variables and operators MUST be typed over S_Pi; all error handling is type‑level, not prose.

---

### L3 — Abstract Experiment Schema (Variables and Design)

Intent. Define variables, roles, relations, and design operators purely over L2 objects; IV/DV appear as tags, not domain narratives.

Structures.

- Variable set V with role tags: {IV, DV, Control, Nuisance, …}.
- Design operators (assignment, blocking, conditioning, constraint) as typed maps transforming tuples of L2‑typed variables.
- Constraints are formal (e.g., admissible sets, partial orders), not descriptive text.

Evolution. Refinements that restrict admissible operations without altering prior denotations.

Obligations upward. L4 MUST encode/decode L3 artifacts losslessly within L2 fidelity and bind them to identity and provenance.

---

### L4 — Technical Infrastructure (Encoding, Storage, Transport)

Intent. Realize machine representations, persistence, and movement while preserving L2/L3 semantics.

Invariants.

- Fidelity. decode(encode(x)) = x up to L2 equivalence.
- Verifiability. Each datum binds to its L3 schema and L2 precision profile via commitments or attestations.
- Transport Integrity. Transformations preserve type, provenance, and do not silently coerce.
- Identity. Agents and instruments are uniquely identified and bound to artifacts.

Evolution. New encodings or transports MUST prove fidelity and verifiability relative to existing artifacts.

---

### L5 — Discourse and Governance

Intent. Human or agent reasoning, peer challenge, and decision records without mutating L0–L4.

Rules.

- Claims reference pinned artifacts and provide machine‑checkable arguments or mappings to L1 theorems.
- Governance accepts, rejects, or supersedes by addition. No edits to committed L4 records (S6).

---

### L6 — Research Memory (Provenance Graph)

Intent. Persistent, branch‑preserving archive of artifacts and their relations.

Structures.

- An immutable provenance DAG with typed edges (derivesFrom, contradicts, refines, supersedes, uses, configOf, …).
- Branch‑preserving updates; no history erasure.

---

## 2. Inter‑Layer Interface Specification

For each adjacent pair k -> k+1:

- Define function signatures, codomains, and error/uncertainty propagation.
- Provide totality or explicit partiality conditions.
- State preservation lemmas (what is guaranteed to hold across the boundary).

A conformance matrix SHALL list the required properties and proofs per boundary.

---

## 3. Formal Semantics of UN (Broken‑0)

- For every type T, introduce UN_T in T_bottom with UN_T <= t for all t in T.
- Distinguish unknown (unobserved), undefined (outside domain), inapplicable (type mismatch); each is separately typed.
- Refinement robustness. Any statement involving UN SHALL declare whether it persists under all admissible refinements.

---

## 4. Evolution and Versioning

- Semantic Versioning. Major = vocabulary or logic change; Minor = conservative extension or refinement; Patch = proof or metadata additions.
- Pinning. All references include exact version IDs.
- Supersession. Newer artifacts MAY supersede older by explicit typed edges in L6; older remain valid and citable.

---

## 5. Compliance Checklists (per layer)

L0. Lattice defined; UN typed; refinement monotone; closure conditions stated.
L1. Base logic and types pinned; theorem obligations listed; conservative‑extension policy formalized.
L2. Precision profiles and quantizers typed; uncertainty algebra laws stated; refinement order defined.
L3. Variable roles enumerated; operator algebra specified; typing over S_Pi; no prose semantics.
L4. Encode/decode proofs; commitment formats; identity/provenance bindings; transport invariants.
L5. Machine‑checkable citation discipline; non‑destructive governance workflow.
L6. DAG schema; edge set; branch‑preserving update rules; query and closure properties.

---

## 6. Parameters to Instantiate (to be pinned once chosen)

1) Base logic at L1.
2) Uncertainty algebra at L2.
3) Variable‑role vocabulary and operator set at L3.
4) Proof or attestation artifact format at L4.
5) Governance rules at L5.
6) Identity and provenance model across 4–6.

---

## 7. Operational Lexicon — Pin/Unpin and Related Primitives

Definitions.

- Artifact: a typed, versioned object produced within layers 0–6. Write as (type, id, version).
- Reference: a pointer to an artifact. A pinned reference is (id, exact version). An unpinned reference carries a constraint (e.g., latest or >= v) and is only allowed in L5–L6 proposals, never in 0–4 artifacts.
- Snapshot: a signed set of pinned references forming a closed dependency set.

Operators (first‑class, recorded in L6 with typed edges).

- PIN(ref, v) -> pinned_ref. Pre: v exists. Effect: ref.version := v. Edge: pins(ref, v).
- UNPIN(ref) -> floating_ref. Pre: only permitted at L5–L6 or in drafts; never in 0–4 committed artifacts. Effect: remove exact version, replace with declared constraint. Edge: unpins(ref).
- REPIN(ref, v2) -> pinned_ref2. Pre: v2 is a conservative extension or permitted refinement of v according to the layer’s rules. Effect: update to v2. Edge: repins(ref, v -> v2) and supersedes(v2, v) where applicable.
- SNAPSHOT(set_of_refs) -> signed_snapshot. Effect: produce an immutable, signed closure of exact versions for reproducibility. Edge: snapshots(snapshot_id, refs).

Policies.

- 0–4 MUST use pinned references only.
- 5 MAY use unpinned references in proposals, but MUST pin before approval or execution.
- 6 stores all operator applications as append‑only events (who, when, why), with links to governance decisions.

Pin Sheet (planning artifact at L5).

- A minimal table that lists each to‑be‑pinned parameter or dependency, its candidate version(s), decision rationale, and approval signature. Output is a SNAPSHOT.

Pin Cursor (ephemeral helper).

- A temporary pointer to a candidate version used during REPIN evaluation. Not storable as a committed artifact; only exists in decision workflows.

Conflict Resolution.

- If REPIN would violate S2 or S3, it is rejected and recorded as a failed event with justification.

---

## 8. Second‑Pass Refinements (v1.3 articulation)

- Added an Operational Lexicon with formal PIN/UNPIN/REPIN/SNAPSHOT definitions and constraints per layer.
- Clarified pinning discipline: layers 0–4 require only pinned references; unpinned allowed exclusively in L5 proposals and L6 queries.
- Kept USS as the pinned backbone and tied encode/decode fidelity explicitly to S_Pi equivalence.
- Harmonized interface determinacy language and preserved append‑only provenance guarantees.

---

## 9. Glossary (formal)

Conservative Extension: An extension that proves no new theorems in the old vocabulary.
Refinement: Information‑increasing map preserving order in R or resolution in S_Pi.
Denotation Preservation: New definitions do not change meanings of previously defined terms at the same precision.
Provenance DAG: Immutable graph whose nodes are pinned artifacts and edges are typed relations.
Pinned Reference: A reference that fixes an artifact’s exact version; mandatory for layers 0–4.
Unpinned Reference: A reference with a version constraint; allowed only at L5–L6 and never in committed 0–4 artifacts.

---

## 10. U‑CV/AV — Uniform “Current” vs “All Versions” (Norms)

**Goal.** Provide a single, cross‑discipline rule that distinguishes the *current* version from *all versions* while preserving pins, provenance, and reproducibility.

### 10.1 Reserved symbols

- **@…@CURRENT** — the *only* sanctioned symbolic alias for the current version of an artifact family.
- **@…@v** — a **pinned** immutable version (semver or content hash).
- **@…@*** — **all‑versions selector** (read‑only; never used for state‑changing commands).

### 10.2 Resolution rule

- Any command that changes state (**PUT, BLOCK, SNAPSHOT, SHED, UNSHED, HOLD‑protect**) **MUST** resolve symbols to a pinned **@…@v** *before* execution and **MUST** log the resolved pin.
- **GET** **MAY** accept symbols but returns the resolved **@…@v** deterministically.

### 10.3 Alias management (L5)

- **ALIAS set @ns/name@CURRENT -> @ns/name@v [--prev p]**
  - **CAS (compare‑and‑swap):** the update **MUST** carry the previous pointer hash `p`; if it doesn’t match the current pointer, the operation **MUST** fail.
  - The new mapping **MUST** be recorded as an **append‑only** pointer record in L6 with actor, time, reason, and signature.
- **ALIAS show @ns/name** — returns the target pin and pointer hash.
- **ALIAS history @ns/name@CURRENT** — returns the append‑only chain of pointer records.
- **ALIAS lock/unlock @ns/name@CURRENT [--ttl T]** — when locked, `CURRENT` **MUST NOT** advance; lock/unlock events are append‑only in L6.

### 10.4 Scope of CURRENT

- Default scope is global per artifact family. A scope **MAY** be refined via labels (e.g., `#env=prod`).
- In any scope, there **MUST** exist **at most one** `CURRENT` for a given artifact family.

### 10.5 Selector & listing safety

- `@…@*` is **read‑only** and **paginated**. Any state‑changing command **MUST** first reduce selectors to explicit pins (or fail).

### 10.6 Snapshot & reproducibility

- **SNAPSHOT** **MUST** eagerly resolve all symbols to pins and embed the alias map used at capture time.
- Citations in discourse **SHALL** use **pinned** versions; `CURRENT` may be shown for convenience alongside the resolved pin.

### 10.7 Normalization & hygiene

- References **MUST** be canonicalized (Unicode NFC, whitespace/case rules) to avoid aliasing collisions.
- Tags (`#…`) are metadata only; adding/removing them **MUST NOT** change the content hash or pin.

### 10.8 Interplay with shedding

- Shedding to L6 **MUST NOT** change pins. Resolution of `@…@v` **MAY** traverse anchors/capsules. Moving `CURRENT` does not mutate prior pins or snapshots.

---

### End of v1.3