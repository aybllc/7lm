# 7lm — Seven-Layer Model (7LM)

The scaffold of the Seven-Layer Model research architecture: one canonical agnostic directory topology, one information sheet per directory.

This file is the start, not the documentation. The documentation is the sheets: every directory describes itself in its own `0.md`, and the controlling text is the Harmonized Authoritative Architecture Specification at `USO/l4/work/writing/7lm-harmonized-architecture-specification.md`. Where anything else in this repository differs from the specification, the specification controls.

Read in this order:

1. `L7/0.md` — the desk, the forward face: provenance, governance, peering, publications.
2. `USO/0.md` — the interior: the seven layers `l6/` down to `l0/`, the count rule, the dependency rules, the tree.
3. The `0.md` of every directory beneath them.

The root holds `README.md`, `L7/`, `USO/`, and `.github/` (one CI check, repository infrastructure and not a layer), and nothing else.

Every prior README is retired, not deleted, at `USO/l6/retired/`: `scaffold-2026-08-20/README.md`, the owner's working sketch; `readme-2026-09-07/README.md`, the README that carried the documentation until 7 September 2026. The record of this repository's layout is `USO/l6/history/harmonization-2026-09-04.md`.
