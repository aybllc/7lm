# L7/regress — loose files awaiting a second opinion

**Owner's definition (2026-08-20, his words, typos normalized):**

> regress is a loose file area for things needing a second opinion, AND which can't go into
> the USO until it is adjudicated.

Two conditions, both live at once: something here is held because a second opinion is wanted
on it, and it is barred from `uso/` until that adjudication happens. Neither condition is
satisfied by storage. A file sitting here is not admitted, not owned, not pinned, and not
evidence of anything.

`regress` is not `egress`. Egress is departure; regress is a file sent back — returned from a
place that declined it, or held short of a place that has not yet accepted it.

## Boundary

- Nothing here may be cited, quoted as authority, or named as a dependency by any composition
  or any layer artifact.
- Presence here confers no ownership, no provenance, and no validity. Custody is not evidence.
- A file leaves only by adjudication — routed onward when its meaning, scope, and owner are
  clear enough, or discarded. It does not age into acceptance.
- **This directory has no fixity coverage.** `7lm/` is untracked in the `ayb` git repository
  and no manifest covers this path. Hashes are recorded by hand below or they are not recorded
  at all.

## Contents

### `oasis-niem-ndr-v6-0-naming-and-design-rules-2025.pdf`

- **sha256** `241dee6e9cbc353fdcf5ffecd300d04cf343889a63770c19d0eb84b1508de439`
- **size** 4,654,798 bytes · **129 pages** · not encrypted
- **arrived** 2026-08-20, withdrawn from `aybllc/l6` at `library/standards/oasis/`
- **byte-identical** to the l6 copy at withdrawal, verified at the moment of transfer; the
  bytes also remain recoverable from l6's git history, and the owner's staged download remains
  at `~/Downloads/layers/standards/niem-ndr-v6.0.pdf`.

**Why it is here.** Its acquisition route could not be established. The owner downloaded it
2026-08-19 23:59 local, in the same session as 22 IEEE Xplore retrievals, and initially
recalled it as an Xplore download; asked again, he did not recall. The artifact rules Xplore
out on its own metadata: all 20 Xplore deliveries in that batch carry IEEE's stamper
(`Producer: … modified using iText® 7.1.1`) plus a Washington State University access stamp,
and this file carries neither. It reads `Creator: Mozilla/5.0 (Macintosh; Intel Mac OS X
10_15_7) … HeadlessChrome/142.0.0.0`, `Producer: Skia/PDF m142`, `CreationDate: Fri Dec 5
19:57:30 2025 PST` — a browser-generated PDF made on a macOS machine nine months before the
download, on neither the owner's platform nor his date. IEEE Xplore does not publish OASIS
standards.

l6's charter admits only material whose provenance is established. Its owner declined to hold
a file that does not meet that bar. That decision is recorded in l6's `VERIFICATION_LOG.md`.

**What is NOT in doubt.** The document is complete and internally consistent: 129 pages
matching its own printed "Page 129 of 129", cover printing "OASIS Standard" and "Standards
Track Work Product" dated 28 November 2025, editors named, full body through Appendix I. It
prints its own authoritative location,
`https://docs.oasis-open.org/niemopen/ndr/v6.0/os/niem-ndr-v6.0-os.html`, and its own licence,
"Copyright © OASIS Open 2025. All Rights Reserved. Distributed under the terms of the OASIS
IPR Policy." **No paywall binds it and no hold-private rule applies.** The problem is
provenance, not licence and not integrity.

**What would adjudicate it.** Retrieve OASIS's published PDF from the authoritative URL above
and compare sha256. Identical means these are the issuer's own bytes and the route question
closes. Different, or unavailable, and it stays here. Until one of those is done by hand,
byte-fidelity to anything OASIS publishes is **UNVERIFIED**.

### `l7-structure-inconsistencies-2026-08-20.md`

Seven disagreements observed inside `7lm/` on 2026-08-20 while placing the PDF above: `L7/`'s
children versus the map in `7lm/README.md`; two `0.md` files whose titles name directories they do
not sit in; the documented intake route pointing at an `L7/intake/` that does not exist; "manual,
documentation-only scaffold" versus `intake/` holding "the preserved source object"; three
`L7/` directories carrying no `0.md` against the stated convention; `7lm/uso/l6/` and the separate
`aybllc/l6` repository both holding the L6 provenance role while naming each other nowhere; and one
0-byte editor backup file.

It is here rather than in `process-lessons.md` because it is **observation awaiting adjudication**,
not a settled process lesson — which side of each disagreement is current is the owner's to say.
Nothing in it was repaired. **It is explicitly a dated snapshot**: the owner reported the same day
that he is reworking the directory structure, so items may already be stale. Verify against the
tree before acting.
