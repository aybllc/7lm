# verify:KC-06

Agent result, as returned. Workflow: Handle on the Auditonomous research and manuscript. Run `wf_9c2917a7-7f0`. Phase: Verify.

- **id**: KC-06
- **verdict**: corrected
- **reasoning**: Checked every cited locator against git objects on MAIN, ROADMAP and BETA. The core of the claim holds, but three parts are imprecise or overstated.

  1. "60 rows, not 62" — CONFIRMED for the ledger; state qualifier needed.
  - MAIN:L7/provenance/sources/LEDGER.md:20-79 has 60 register [source text withheld from the public copy] (my own count). The ROADMAP ledger is the same blob (4ad8ea2).
  - The figure 62 is not in the ledger. It is in the sheets around it: MAIN:L7/provenance/sources/0.md:10 "62 pointer rows into the `aybllc/l6` archive", :41, MAIN:L7/0.md:220, MAIN:L7/peering/private/ingress/peer-1/object-1/0.md:10, and MAIN:L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:30 "62 rows (PR-001..020, STD-001..034, INST-001..004, EXC-001/002)", whose own enumeration sums to 60.
  - The same MAIN sheet also says, at 0.md:55, "The ledger has no rows; that is admissible." So MAIN carries three figures: 62, none, and the actual 60.
  - ROADMAP repeats 62, including BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:413 "the 62-row source ledger".
  - BETA:LEDGER.md:147-149 confirms: "[source text withheld from the public copy]." It also corrects the close-out log's "22 new rows" (MAIN:LEDGER.md:113) to 21.
  - On BETA only, the ledger has a 61st record in a separate table: AUT-SOURCE-001 (BETA:LEDGER.md:153), "[source text withheld from the public copy]".

  2. "all pointers into a private archive no reader could open" — IMPRECISE.
  - 58 rows carry an `l6` path and Access FULL. The 2 EXC rows are not pointers: MAIN:LEDGER.md:78-79 "— (HELD OUT of l6)", Access NOT OBTAINED and BLOCKED.
  - The repository labels the archive private: MAIN:LEDGER.md:3-4 "(`https://github.com/aybllc/l6`, INTERNAL)" and :144 "l6 is private/INTERNAL". I could not open l6 (it is not among the clones), so the privacy is the repository's label, not something I confirmed. "No reader" should read "no outside reader".
  - Each row also carries a bibliographic citation (column rule, :84 "[source text withheld from the public copy]"), though some are incomplete (PR-013 and PR-020 have no year).

  3. "VERIFIED records that a file matches the archive copy, not that a claim was checked" — CONFIRMED.
  - 37 of 60 rows carry VERIFIED, always qualified as byte-identical, same standard net of watermark, content-identical, or same work (e.g. :20 "[source text withheld from the public copy])").
  - Row PR-002 (:21) settles it: "[source text withheld from the public copy]".
  - 19 further rows read "ACCESSIONED; sha256 … verified"; PR-006 is labelled PREPRINT; STD-025 has only "Acquired lawfully"; 2 are EXC.
  - The comparison is staged copy against l6 copy (:111-113, :124-131).
  - This use conflicts with the repository's own ladder, MAIN:STATUS_LADDER.md: VERIFIED = "(checked against an OUTSIDE source, which is cited)", while the ledger's column rule (:88) calls the [source text withheld from the public copy]".

  4. "A record of reading exists for 14 of the 58 held sources" — CONFIRMED, with qualifiers.
  - 11 reading-protocol records: ieee/reading/ IEEE-3152, 7001, 7007, 7009, 7014 (STD-017, 004, 006, 007, 008); library/reading/ ARIES, Ferreira, Haber-Stornetta, FIPS 180-4, RFC 6962, RFC 9162 (PR-018, PR-020, PR-019, STD-002, STD-033, STD-034).
  - 3 capture records: standards/extracted/IEEE-1872.2-2021_captures.md (STD-010); ISO-IEC-22989-2022_captures.md (STD-025); interval/DECORATIONS_2026-08-04.md (STD-023).
  - The ISO/IEC 22989 captures were taken from the withdrawn third-party copy, not the held STD-025 copy (captures.md:7 "[source text withheld from the public copy]").
  - The IEEE 1788-2015 record is partial: DECORATIONS:111 "[source text withheld from the public copy].**"
  - Recorded as not read: Stevens PR-002, Ewen 1951 PR-011, Bennett PR-012 (SOURCE_LEDGER.md:381-386 "held but not read"); IEEE 1788.1-2017 STD-024 (DECORATIONS:97 "NOT READ this session"); Tan and Vandewalle PR-017 (DECORATIONS:106 "NOT-CHECKED"); PR-014, 015, 016 (ieee/papers/README.md:43 "[source text withheld from the public copy]").
  - About 11 others have only first-page identification quotes (SOURCE_LEDGER.md:316-346; method at :391-394).
  - A 15th capture record, SP800-53r5_AC-AU_verbatim.md, is for a source with no ledger row.
  - No reading record exists outside staging-records in any of the three states (grep for READING RECORD, VERBATIM CAPTURES, "pages read").
  - staging-records holds 26 blobs: 25 records plus the 0.md sheet, matching 0.md:8 "(25 files)". MAIN:LEDGER.md:134 says "27 markdown working records", but the move commit 4a1c1db placed 25.

  5. "The definition's own external citations have no rows" — OVERSTATED.
  - MAIN:AUDITONOMOUS_DEFINITION.md:281-336 cites the American Heritage Dictionary (five entries), Perseus/Liddell-Scott, Lewis and Short, the NIST CSRC Glossary (CNSSI 4009-2015, SP 800-37, SP 800-53), IETF RFC 4949, NIST AI 100-1 and IEEE 7001-2021. Lines 338-347 are failure records, not citations.
  - None of the dictionary, NIST or RFC citations has a row in LEDGER.md in any state (zero grep hits each).
  - IEEE 7001-2021 as a work does have a row: STD-004 (MAIN:LEDGER.md:33), plus a reading record. The definition (:329-330) cites the IEEE catalogue page, "[source text withheld from the public copy]", not the ledgered file, and never names STD-004. staging-records/ieee/README.md:35 says "[source text withheld from the public copy]."
  - On BETA the definition differs (blob 8127041; Appendix C shifts to about 283-352) and adds a binding to AUT-SOURCE-001, which has a row at BETA:LEDGER.md:153.
  - On ROADMAP only, a separate restored STANDARDS_REGISTER.md lists NIST AI 100-1 (:169 "OBTAINED"), RFC 4949 (:205 "LEAD") and IEEE 7001-2021 (:121). These are not LEDGER rows.
  - By the repository's own rule these are unledgered citations: MAIN:L7/peering/private/ingress/peer-1/object-1/0.md:21 "A source cited anywhere in this repository without a row in `L7/provenance/sources/LEDGER.md` is an unledgered citation."

  Evidence states: row count 60 = INTERNALLY CHECKED (recorded on BETA; unmerged); "62" and "no rows" in the MAIN and ROADMAP sheets = CONTRADICTED; ledger label VERIFIED = fixity only; the definition's Appendix C citations = unledgered.
- **corrected_statement**: KC-06 (corrected): The source ledger (MAIN and ROADMAP, identical blob: L7/provenance/sources/LEDGER.md:20-79) has 60 register [source text withheld from the public copy]), not the 62 stated in the sheets around it on MAIN and ROADMAP (L7/provenance/sources/0.md:10 and :41, L7/0.md:220, peer-1/object-1/0.md:10, L8/L6/history/LEDGER_2026-08-16…:30); the same MAIN sheet also says at 0.md:55 "The ledger has no rows". BETA corrects the figure to "60 archive rows" (BETA:LEDGER.md:149), corrects the close-out log's "22 new rows" to 21, and adds a 61st record, AUT-SOURCE-001 (BETA:LEDGER.md:153), which is not an archive pointer. Of the 60 rows, 58 are pointers (path plus commit, Access FULL) into aybllc/l6, which the repository labels "private/INTERNAL" and which no outside reader can open (the privacy is the repository's label; l6 was not available to confirm). The other 2 (EXC-001, EXC-002) are exclusion rows, "HELD OUT of l6", with no pointer. The label VERIFIED, on 37 rows, records only that the staged file matched the l6 copy (byte-identical, same standard net of watermark, or same work); 19 more rows read "ACCESSIONED; sha256 … verified". It does not record that any claim was checked, and one such row says "NOT READ" (PR-002); this is a different sense from the status ladder's VERIFIED ("checked against an OUTSIDE source"). A record of reading exists in staging-records (25 records plus a sheet) for 14 of the 58 held sources: 11 reading-protocol records (STD-002, 004, 006, 007, 008, 017, 033, 034; PR-018, 019, 020) and 3 capture records (STD-010; STD-023, decoration clauses only; STD-025, captured from the withdrawn third-party copy rather than the held one). Four are recorded as not read (PR-002, PR-011, PR-012, STD-024), three as shelved unread (PR-014 to 016), one as NOT-CHECKED (PR-017), and the rest have at most a first-page identification quote. One further capture record (NIST SP 800-53 Rev. 5) is for a source with no ledger row. The definition's external citations (MAIN:AUDITONOMOUS_DEFINITION.md:281-336: American Heritage Dictionary, Perseus/Liddell-Scott, Lewis and Short, NIST CSRC Glossary, RFC 4949, NIST AI 100-1) have no ledger rows in any state. The one exception is IEEE 7001-2021, which has row STD-004 and a reading record, but the definition cites the IEEE catalogue page rather than that row. On BETA only, the definition's added binding AUT-SOURCE-001 has a ledger row; on ROADMAP only, a separate restored STANDARDS_REGISTER.md lists NIST AI 100-1, RFC 4949 and IEEE 7001-2021, which are not ledger rows.
- **evidence_checked**
  - MAIN:L7/provenance/sources/LEDGER.md:20-79 — 60 rows counted ([source text withheld from the public copy]); Access column: 58 FULL, 1 NOT OBTAINED, 1 BLOCKED; 58 rows with a library/ path; label first word: 37 VERIFIED, 19 ACCESSIONED, 1 PREPRINT, 1 Acquired, 1 EXCLUDED, 1 PROHIBITED
  - MAIN:L7/provenance/sources/LEDGER.md:3-4, :21, :78-79, :84-89, :111-113, :117-145 — archive labelled INTERNAL/private; PR-002 'NOT READ'; EXC rows 'HELD OUT of l6'; column rules; search log ('22 new rows'); transfer accounting ('27 markdown working records')
  - ROADMAP:L7/provenance/sources/LEDGER.md — same blob as MAIN (4ad8ea2)
  - BETA:L7/provenance/sources/LEDGER.md:147-153 — '60 archive rows', 21-not-22 correction, AUT-SOURCE-001 row; diff against MAIN is 8 insertions and no deletions
  - MAIN:L7/provenance/sources/0.md:10, :41, :55 — '62 pointer rows', '62 rows', 'The ledger has no rows'; BETA:L7/provenance/sources/0.md:10, :41, :55 corrected to 60
  - MAIN:L7/0.md:220; MAIN:L7/peering/private/ingress/peer-1/0.md:16; MAIN:L7/peering/private/ingress/peer-1/object-1/0.md:10 and :21; MAIN:L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:30; MAIN:L8/L6/history/7LM_ROUTING_PLAN_2026-09-05.md:80 and :206 — origin of '62'; unledgered-citation rule
  - ROADMAP:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:413 — 'the 62-row source ledger'
  - MAIN:L8/L5/research/review/STATUS_LADDER.md and STATUS_AND_LABEL_DISCIPLINE.md — the ladder's definition of VERIFIED
  - MAIN:L7/provenance/sources/staging-records/ — 26 blobs (25 records plus 0.md); read 0.md, README.md, STAGING_README.md, ieee/README.md, ieee/papers/README.md, library/README.md, standards/SOURCE_LEDGER.md in full; heads of ieee/FINDINGS, library/FINDINGS, all 11 reading records, the 3 extracted capture files and terms.json; interval/DECORATIONS_2026-08-04.md lines 1-115
  - MAIN:L7/provenance/sources/staging-records/standards/SOURCE_LEDGER.md:316-346, :381-394 — INTAKE 8526 identification quotes, 'held but not read' list, method
  - MAIN:L7/provenance/sources/staging-records/interval/DECORATIONS_2026-08-04.md:96-111 — 1788.1 'NOT READ', Tan and Vandewalle 'NOT-CHECKED', 1788-2015 read for decorations only
  - MAIN:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:263-347 — Appendix C external citations at 281-336, failures at 338-347; same blob on ROADMAP (8b934b4); BETA blob 8127041 with 16 insertions, including the AUT-SOURCE-001 binding
  - grep of LEDGER.md in all three states for American Heritage, ahdictionary, Perseus, Liddell, Lewis, CSRC, CNSSI, 4949, AI 100-1, AI RMF, 800-53, 800-37, Merriam, Winfield: 0 hits each; '7001': 1 hit (STD-004)
  - grep of all three states for 'READING RECORD', 'VERBATIM CAPTURES', 'pages read' outside staging-records: no files
  - ROADMAP:L7/provenance/sources/STANDARDS_REGISTER.md:121, :169, :205 and lists-2026-08-08/0.md:8 — a separate register listing IEEE 7001-2021, NIST AI 100-1 (OBTAINED), RFC 4949 (LEAD); lists described as 'leads, not sources'
  - git commit 4a1c1db (2026-08-16) — research/ledgers/staging-records held 25 files at the move; RECONCILIATION_FROM_L6_2026-08-16.md now at L7/peering/private/egress/peer-1/object-1/ in all three states
