# 7lm scaffold — structural inconsistencies observed 2026-08-20

**Snapshot, not a verdict.** Every statement below was measured against the working tree at
**2026-08-20T12:28:46-07:00**. The owner said the same day that he is "actually tooling with it"
and that a directory-structure update is coming, so **items here may already be stale — check the
tree before acting on any of them.** This file records what disagreed with what at that moment. It
proposes nothing, repairs nothing, and no item is a defect until the owner says which side of the
disagreement is current.

Written by the l6 provenance session while placing
`oasis-niem-ndr-v6-0-naming-and-design-rules-2025.pdf` into `regress/`; the disagreements surfaced
because placing a file required reading the scaffold. Cross-reference: `aybllc/l6`
`VERIFICATION_LOG.md` Event 22.

---

## 1. `L7/`'s children do not match the map in `7lm/README.md`

`README.md` prints this directory map:

> ```
>   L7/                            Scientific Desktop; sits OUTSIDE the USO
>     intake/
>     PINNED/
>     compositions/
>     process-lessons.md
> ```

On disk `L7/` holds: `0.md`, `process-lessons.md`, `bak-process-lessons.md~`, `docs/`,
`progress/` (containing `ingress/` and `egress/`), `published/`, and `regress/`.

**`intake/`, `PINNED/` and `compositions/` do not exist.** Four of the seven present entries
(`docs/`, `progress/`, `published/`, `regress/`) appear in no README map.

## 2. Two `0.md` files sit in directories their own titles do not name

| File on disk | Its own first line |
|---|---|
| `L7/progress/0.md` | `# L7/compositions - application-scoped selections` |
| `L7/progress/ingress/0.md` | `# L7/PINNED - fixed authority bindings` |

Both documents are internally coherent and describe `compositions/` and `PINNED/` in detail —
they read as complete, finished files that were placed under the new names without being
retitled. Consistent with a rename in progress; **which name is intended to survive is not
inferable from the files themselves**, which is why nothing here was changed.

`L7/progress/egress/0.md` does not exist, so `egress/` has no stated meaning at all.

## 3. The documented intake route points at a directory that does not exist

This is the operationally significant one, because it breaks a rule the scaffold states three
times.

- `L7/0.md`, Children: "`intake/` — provisional admission: the preserved source object, its origin
  and version, its candidate local artifacts, and their candidate layer owners."
- `L7/0.md`, Manual work item 1: "Send every incoming object to `intake/` first. **Nothing enters a
  layer directly**, and nothing is routed out of intake before its meaning, scope, and owner are
  clear enough."
- `uso/l6/provenance/0.md`, Boundary: "Do not use this directory as an intake point. **New material
  enters at L7 intake.**"

`L7/intake/` does not exist. **As of this snapshot the scaffold has no admission point**, so the
mandatory first step for any incoming object cannot be performed as written. Whether `ingress/` is
the intended successor to `intake/` is not stated anywhere in the tree.

## 4. "Documentation-only" versus "the preserved source object"

`7lm/README.md`, opening paragraph: "This repository is a manual, **documentation-only** scaffold …
**There is no code here, no build, and no automation.**"

`L7/0.md` describes `intake/` as holding "**the preserved source object**" — i.e. binary artifacts,
not documentation about them.

The two cannot both be fully true of the same tree. The scaffold currently holds two non-`.md`
files: `L7/regress/oasis-niem-ndr-v6-0-naming-and-design-rules-2025.pdf` (4,654,798 bytes) and
`L7/bak-process-lessons.md~` (0 bytes). **The PDF was placed by owner instruction on 2026-08-20**
and is consistent with `L7/0.md`, not with the README. Flagged so the resolution is a decision
rather than an accident: if "documentation-only" is meant literally, that file does not belong
here and needs another home.

## 5. Three directories under `L7/` carry no `0.md`, against the stated convention

`README.md`: "Every directory under `L7/` and `uso/` carries a `0.md`; `durable/` is outside the
scaffold and is not covered by this convention."

Missing: **`L7/docs/`**, **`L7/published/`**, **`L7/progress/egress/`**. All three are also
**empty**. Every one of the 21 directories under `uso/` complies; the exceptions are all under
`L7/`, which is the part being reworked.

`L7/regress/0.md` was written on 2026-08-20 to satisfy this convention for the directory this file
sits in.

## 6. Two different things are both called L6, and neither names the other

- `7lm/uso/l6/` — "L6 - Research History and Provenance", holding `history/0.md`,
  `provenance/0.md`, and `provenance/source-ledger.md`. The ledger is a **header-only stub**: 353
  bytes, an eight-column table with zero rows.
- `/home/eric/ayb/l6` (`aybllc/l6`) — a separate git repository whose `README.md` opens "Archival
  copies of primary literature held for research provenance. **USO rail L6 — Provenance.**" It
  holds **1,367 tracked files**, a 1,367-entry `MANIFEST.sha256`, and a 22-event append-only
  `VERIFICATION_LOG.md`.

Both claim the L6 provenance role. `grep` across `uso/l6/` and `L7/0.md` for any reference to the
other repository returns **nothing** — the only `/l6` hit in the scaffold is `L7/0.md` line 45
referring to its own `uso/l6/history/`. So the scaffold's empty ledger and the populated archive
are **unaware of each other**.

This is stated as an observation with a real consequence: the fields `uso/l6/provenance/0.md`
requires per row — Source ID, source identity, issuer, exact version, locator, retrieval date,
declared scope, local use, transformations, gaps, contradictions — are largely already recorded, in
prose, across `aybllc/l6`'s `VERIFICATION_LOG.md`, `ACQUIRE.md` and `MANIFEST.sha256`. **Whether
these are one L6 in two places or two L6s with one name is the owner's call and is not decided
here.**

## 7. Minor

`L7/bak-process-lessons.md~` — a **0-byte** editor backup file, dated 2026-08-20 10:50. Carries no
content and matches no convention in the tree. Noted only so it is not mistaken later for a
truncated record.

---

## What was NOT done

Nothing above was repaired, renamed, moved, created, or harmonized. `L7/regress/` and its `0.md`
were created, and one PDF placed, both by explicit owner instruction on 2026-08-20; that is the
only change this session made anywhere under `7lm/`.

**Standing reason for not repairing:** where two records disagree, which one is current is a fact
about the owner's intent, and it is not recoverable from the files. Guessing would replace a
visible disagreement with an invisible one.
