# USO/l6/history/harmonization-2026-09-04.md

**Object:** L6 record of the harmonization displacement event of 2026-09-04 — what was superseded, relocated, reserved, split, or retired, by prior path → current path (or "reserved, no path"), with the deletions already made on `main` before this pass.
**Path:** `USO/l6/history/harmonization-2026-09-04.md` · **Layer:** L6 — LIBRARY · **Owner:** USO/l6/

This record records; it does not adjudicate. Its dispositions are the Harmonization Record's dispositions, copied by name. Its paths are the repository's actual paths. Where the Harmonization Record reserves a term, this record says "reserved, no path" and names where the prior text can be read; it gives no term a home. Commit identifiers are orientation pointers to repository change events; the facts they attach to were supplied to this record and checked against Git history in the verification of this record. Git history and scientific memory are not the same object; this file is the memory.

## 1. Inherited terms — disposition, current path, prior text

| Inherited term / prior path | Disposition | Where it is now | Where the prior text is preserved |
|---|---|---|---|
| prior-art / `uso/l0/prior-art/` (renamed `USO/l0/prior-art/` at c0f46e1) | Relocated | `L7/provenance/prior-art/` — "External antecedents belong at L7/provenance/prior-art/." | `USO/l6/retired/scaffold-2026-08-20/USO/l0/prior-art/0.md` |
| definitions / `uso/l0/definitions/` (renamed `USO/l0/definitions/`) | Ratified | `USO/l0/semantics/definitions/` — "Locally authored definitions belong at USO/l0/semantics/definitions/; peer definitions arrive as immutable external bindings." | `USO/l6/retired/scaffold-2026-08-20/USO/l0/definitions/0.md`. The pass instruction directs that the file's two controlled-definition tables be carried forward verbatim into the current sheet under an inherited heading; that carriage is not a re-adjudication. |
| semantic-formulas / `uso/l0/semantic-formulas/` (renamed `USO/l0/semantic-formulas/`) | Split and reserved | No current path for the compound term. "Semantic reading remains L0; an exact formula is L2; an applied, tolerant, adaptive, or engineering formula is L3. The inherited compound term remains searchable." The three destinations exist as `USO/l0/semantics/`, `USO/l2/formal-mathematics/`, `USO/l3/engineering-mathematics/`; no file was moved to any of them. | `USO/l6/retired/scaffold-2026-08-20/USO/l0/semantic-formulas/0.md` |
| thesis-statements / `uso/l0/thesis-statements/` (renamed `USO/l0/thesis-statements/`) | Relocated | `USO/l5/research/lanes/` — "Research claims and thesis statements belong at USO/l5/research/lanes/ or the corresponding L5 research artifact." | `USO/l6/retired/scaffold-2026-08-20/USO/l0/thesis-statements/0.md` |
| origidity; certainty; intolerance | Reserved | Reserved, no path. "Candidate L1 semantics preserved; topology remains unadjudicated." | Stated meaning: the Harmonization Record row. In the retained prior text: the retired README sketch's layer map lists "certainty" on its L3 line and "intolerant" on its L2 line (`USO/l6/retired/scaffold-2026-08-20/README.md`, lines 20–21). "origidity" is not located in any committed state of this repository; its stated meaning is preserved only in the Harmonization Record row. |
| found; caught; naught / `L7/private/durable/found/`, `L7/private/durable/caught/`, `L7/private/durable/naught/` | Reserved | Reserved, no path. "caught remains the zero state; found remains the observer role; naught remains the empty or settled state. Their topology remains unadjudicated." | Stated meaning: the Harmonization Record row. Prior gate files `L7/private/durable/0.md`, `L7/private/durable/found/0.md`, `L7/private/durable/caught/0.md`, `L7/private/durable/naught/0.md` were deleted by the owner in c0f46e1 (2026-08-24); they are not in the retired scaffold and are recoverable from Git history only (the tree before c0f46e1). |
| regress / `L7/private/regress/` | Reserved | Reserved, no path. "Preserved as a prior unadjudicated holding concept; active path and owner remain unadjudicated." | Stated meaning: the Harmonization Record row. Prior files were deleted by the owner before this pass — see §2 (1edf4c7, f154f9f, ee12569, 84ca4f4, c0f46e1); none is in the retired scaffold; all are recoverable from Git history only. |
| corpus / `L7/corpus/` | Split and reserved | Released corpus/publication identity: `L7/publications/`; the broader inherited term: reserved, no path. "Released corpus/publication identity belongs at L7/publications/; the broader inherited term remains reserved where its exact role is not yet adjudicated." | `L7/corpus/0.md` was deleted by the owner in c0f46e1 and is recoverable from Git history only. The word in its broader sense is used throughout the retired scaffold sheets, e.g. `USO/l6/retired/scaffold-2026-08-20/USO/l6/0.md` line 3 ("the scientific record of the corpus"), `.../USO/l0/0.md`, `.../USO/l5/0.md`, and the retired definitions table's row "USO" (`.../USO/l0/definitions/0.md` line 73). |
| INFRASTRUCTURE (as L4 name) | Superseded as L4 name | `USO/l4/` — "L4 is Conversion. Infrastructure belongs at L4 only when it is the bounded work or conversion being made; generic repository support is not automatically a layer." | The word is not located as a layer name in the current working tree. The retired scaffold's L4 sheet is headed "L4 - Application and Implementation" (`USO/l6/retired/scaffold-2026-08-20/USO/l4/0.md`); the retired README sketch's L4 line reads "modeling, processing, manufacturing, computing … = conversion" (`.../README.md` line 16). The v1.3 origin document deleted at c0f46e1 (recoverable at 3bdbe4b) carries the older name at its heading "L4 — Technical Infrastructure (Encoding, Storage, Transport)" (line 141). |
| DEVOID; IMMUTABLE; FINITE; INFINITE; IDENTITY BY PROSE; RESEARCH MEMORY; SCIENTIFIC DESKTOP | Descriptive | No path. "Preserved as historical mnemonics or working language; the principal layer sheets control ownership." | FINITE and INFINITE: the superseded draft's retained compact sheets headed "L2 — FINITE / FORMAL MATHEMATICS" and "L3 — INFINITE / ENGINEERING MATHEMATICS" (`USO/l6/retired/specification-draft-2026-09-03/7lm-architecture-specification-draft.txt`, lines 1256 and 1273), and the retired README sketch's L2/L3 lines ("finite", "infinite"). IMMUTABLE and INFINITE: the harmonized specification's own author notes at L1 ("STATE and IMMUTABLE remain useful descriptive/mnemonic language") and L3 ("INFINITE is retained as a working term"). SCIENTIFIC DESKTOP: the retired definitions table row "Scientific Desktop" (`.../USO/l0/definitions/0.md` line 75), the retired README sketch's L7 line ("desktop"), and the specification's own line "L7 = Desktop". RESEARCH MEMORY: the v1.3 origin document deleted at c0f46e1 (recoverable at 3bdbe4b), heading "L6 — Research Memory (Provenance Graph)", line 167. DEVOID and IDENTITY BY PROSE: not located in any committed state of this repository; their stated meaning is preserved only in the Harmonization Record row. |
| L6 provenance / `uso/l6/provenance/` (renamed `USO/l6/provenance/`) | Split | Internal reconstructable memory stays here at `USO/l6/` (`history/`, `retired/`). External provenance moved to `L7/provenance/`; the ledger `USO/l6/provenance/source-ledger.md` (header-only, no rows) is relocated to `L7/provenance/sources/source-ledger.md`. "Internal reconstructable memory remains L6; external source, authority, prior art, and public provenance belong at L7/provenance/." | `USO/l6/retired/scaffold-2026-08-20/USO/l6/provenance/0.md` (the gate); the ledger itself is not retired but relocated, with its eight column headings unchanged. |
| blank 0.md / status markers (`L7/0.md`, `L7/governance/0.md`, `L7/peering/0.md`, `L7/publications/0.md`, empty at e295a5d: `L7/governance/0.md` and `L7/peering/0.md` created empty at c0f46e1; `L7/publications/0.md` emptied at 3bde809; `L7/0.md` emptied at 9523400) | historical implementation evidence at L6, not architecture | Overwritten by the harmonized sheets at the same paths in this pass. | Not preserved as files (they were empty). Recorded here: four empty stubs existed at those paths before this pass; the earlier non-empty content of `L7/publications/0.md` and `L7/0.md` is recoverable from Git history only. |

### 1a. Files of the 2026-08-20 scaffold retired at e810f61 (prior relative path → retired path)

Each of the nineteen gate files was moved verbatim on 2026-09-04, in commit e810f61, from `USO/<path>` to `USO/l6/retired/scaffold-2026-08-20/USO/<path>`:

| Prior path (after the c0f46e1 rename) | Retired path |
|---|---|
| `USO/l0/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l0/0.md` |
| `USO/l0/definitions/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l0/definitions/0.md` |
| `USO/l0/epistemic/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l0/epistemic/0.md` |
| `USO/l0/ontology/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l0/ontology/0.md` |
| `USO/l0/prior-art/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l0/prior-art/0.md` |
| `USO/l0/semantic-formulas/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l0/semantic-formulas/0.md` |
| `USO/l0/semantics/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l0/semantics/0.md` |
| `USO/l0/thesis-statements/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l0/thesis-statements/0.md` |
| `USO/l1/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l1/0.md` |
| `USO/l1/state-space/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l1/state-space/0.md` |
| `USO/l2/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l2/0.md` |
| `USO/l2/formal-mathematics/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l2/formal-mathematics/0.md` |
| `USO/l3/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l3/0.md` |
| `USO/l3/engineering-mathematics/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l3/engineering-mathematics/0.md` |
| `USO/l4/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l4/0.md` |
| `USO/l5/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l5/0.md` |
| `USO/l6/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l6/0.md` |
| `USO/l6/history/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l6/history/0.md` |
| `USO/l6/provenance/0.md` | `USO/l6/retired/scaffold-2026-08-20/USO/l6/provenance/0.md` |

The owner's README working sketch, titled "Unified Science Object", is retired verbatim at `USO/l6/retired/scaffold-2026-08-20/README.md`. Directories of the old scaffold that the canonical topology also names (`USO/l0/epistemic/`, `USO/l0/ontology/`, `USO/l0/semantics/`, `USO/l1/state-space/`, `USO/l2/formal-mathematics/`, `USO/l3/engineering-mathematics/`, `USO/l6/history/`) keep their paths; their sheets are rewritten under the harmonized specification, and the old sheet is at the retired path above. Directories the canonical topology does not name (`USO/l0/definitions/`, `USO/l0/prior-art/`, `USO/l0/semantic-formulas/`, `USO/l0/thesis-statements/`, `USO/l6/provenance/`) have no current counterpart at that path; their dispositions are in §1.

## 2. Chronology (repository change events, with commit identifiers)

| Date | Event | Commit |
|---|---|---|
| 2026-08-20 | Pre-harmonization scaffold drafted, with lowercase `uso/` as the interior root and an L7 desk (`L7/corpus/`, `L7/private/durable/…`, `L7/private/regress/`, `L7/public/ingress/`, `L7/public/egress/`). | 9532e6f; 82ce669 |
| 2026-08-20 | Sanitize/quarantine cycle: root README archived, methodology and source ledger moved into `L7/private/regress/`, `pre-sanitize-*.md` snapshots created. | f9fde14 … 7bb015e (f9fde14, 81aa684, daf77b6, 618e0de, bfb9b1b, e101939, df838fc, 7bb015e) |
| 2026-08-24 | The v1.3 "Seven-Layer Methodology" origin document moved from the repository root to `uso/l6/history/origin/seven_layer_methodology.md`. It remains recoverable at this commit. | 3bdbe4b |
| 2026-08-23 | "Restore repository tree to 82ce669": a set of `pre-sanitize-*.md` snapshots removed from `L7/private/regress/`. | 1edf4c7 |
| 2026-08-24 | Owner deleted `L7/private/regress/l7-structure-inconsistencies-2026-08-20.md`. | f154f9f |
| 2026-08-24 | Owner deleted `L7/private/regress/displaced-compositions-0.md`. | ee12569 |
| 2026-08-24 | Owner deleted `L7/private/regress/displaced-process-lessons.md`. | 84ca4f4 |
| 2026-08-24 | "Restructure: USO/ corpus and L7 governance/peering/publications": `uso/` renamed `USO/`; the old L7 desk cut. Deleted: `L7/corpus/0.md`; `L7/private/0.md`; `L7/private/durable/0.md`, `L7/private/durable/found/0.md`, `L7/private/durable/caught/0.md`, `L7/private/durable/naught/0.md`; `L7/private/regress/0.md`, `L7/private/regress/displaced-L7-0.md`, `L7/private/regress/displaced-PINNED-0.md`, `L7/private/regress/oasis-niem-ndr-v6-0-naming-and-design-rules-2025.pdf`; `L7/public/ingress/0.md`, `L7/public/egress/0.md`, `L7/public/egress/ACQUIRE.md`; `uso/0.md`; `uso/l6/history/origin/seven_layer_methodology.md`. | c0f46e1 |
| 2026-08-24 | `USO/0.md` deleted. | e295a5d |
| 2026-08-24 | The USO layer map moved from `L7/publications/0.md` into `README.md`, leaving `L7/publications/0.md` empty. That README working sketch is now retired verbatim at `USO/l6/retired/scaffold-2026-08-20/README.md`. | 3bde809 |
| 2026-08-24 | `L7/0.md` emptied. | 9523400 |
| 2026-09-03 | Draft "SEVEN-LAYER MODEL (7LM) Authoritative Architecture Specification" — the date its own footer carries. Superseded the next day. | — |
| 2026-09-04 | Retirement and filing: the nineteen `0.md` files and README.md moved verbatim to `USO/l6/retired/scaffold-2026-08-20/…` at their old relative paths (§1a); `USO/l6/provenance/source-ledger.md` (header-only, no rows) relocated to `L7/provenance/sources/source-ledger.md` unchanged; the harmonized specification filed at `USO/l4/work/writing/7lm-harmonized-architecture-specification.docx` and `.md`; the superseded draft filed at `USO/l6/retired/specification-draft-2026-09-03/7lm-architecture-specification-draft.pdf` (386,578 bytes; 19 pages) and `.txt`. | e810f61 |
| 2026-09-04 | Uniform `0.md` sheets written for every directory of the canonical topology, by hand, without automation; the stubs `L7/0.md`, `L7/governance/0.md`, `L7/peering/0.md`, `L7/publications/0.md` (empty at e295a5d) overwritten by harmonized sheets. | (uncommitted at time of writing) |
| 2026-09-04 | The sheets of the previous row were committed. | fb22e25 |
| 2026-09-05 | Owner designated `aybllc/l6` (INTERNAL) as the archive that serves curated sources to this program, read-only from every consuming repository ("don't edit l6; use it to serve curated sources"). Recorded at `L7/provenance/sources/0.md` and `L7/peering/private/ingress/0.md`; the archive pinned at `53b28f6`. | (the commit that added this row) |
| 2026-09-05 | Owner rule for the originating boundary test: "Auditonomous gets the definitions of autonomous from Autonomous and nowhere else." Recorded at `L7/peering/public/ingress/0.md`; applied in the auditonomous routing proposal. | (the commit that added this row) |

## 3. Reserved — no current path

The following are reserved by the Harmonization Record and therefore have no current path, owner, or directory in this repository. Their stated meanings are preserved in the Harmonization Record; their prior text is preserved where §1 says. "A reserved term remains available for research without manufacturing a directory or layer owner."

- **found; caught; naught.** "caught remains the zero state; found remains the observer role; naught remains the empty or settled state. Their topology remains unadjudicated." Prior gate files deleted at c0f46e1; Git history only.
- **regress.** "Preserved as a prior unadjudicated holding concept; active path and owner remain unadjudicated." Prior files deleted at 1edf4c7, f154f9f, ee12569, 84ca4f4, c0f46e1; Git history only.
- **origidity; certainty; intolerance.** "Candidate L1 semantics preserved; topology remains unadjudicated." Words "certainty" and "intolerant" in the retired README sketch; "origidity" not located in any committed state of this repository.
- **corpus, in its broader sense.** "the broader inherited term remains reserved where its exact role is not yet adjudicated." Only the released corpus/publication identity has a path (`L7/publications/`). `L7/corpus/0.md` deleted at c0f46e1; Git history only.
- **semantic-formulas, as a compound term.** "The inherited compound term remains searchable." Its three readings have layer owners (L0, L2, L3); the compound has no path. Prior text at `USO/l6/retired/scaffold-2026-08-20/USO/l0/semantic-formulas/0.md`.

## 4. The "L6 provenance" split, named

The Harmonization Record's row "L6 provenance — Split": "Internal reconstructable memory remains L6; external source, authority, prior art, and public provenance belong at L7/provenance/." Applied in this repository: internal reconstructable memory stays here at `USO/l6/` (`USO/l6/history/`, `USO/l6/retired/`); external provenance moved to `L7/provenance/`; the ledger moved from `USO/l6/provenance/source-ledger.md` to `L7/provenance/sources/source-ledger.md`. The prior L6 provenance gate is retired at `USO/l6/retired/scaffold-2026-08-20/USO/l6/provenance/0.md`. No `USO/l6/provenance/` directory exists after this pass.

## 5. Not recorded here

- Whether any retired text was right. That is an L5 judgment.
- The provenance of external sources any retired sheet cited (ISO/IEC/IEEE 24765:2017, JCGM 200:2012, IEEE Std 2755-2017, W3C PROV). Those references resolve to `L7/provenance/`; they are not re-owned by this record.
- Any placement for a reserved term.
