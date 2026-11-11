# check:fips180-4

Agent result, as returned. Workflow: Public sources against their originals. Run `wf_73fbd9d4-516`. Phase: Check.

- **check**: FIPS 180-4 Secure Hash Standard: reading record and LEDGER row STD-002 in aybllc/auditonomous (origin/main 2165144) versus the official NIST PDF and CSRC page
- **sources**
  - item 1
    - **name**: [source text withheld from the public copy]), August 2015 (PDF)
    - **official_url**: https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf
    - **final_url**: https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf
    - **http_status**: 200
    - **bytes**: 833315
    - **sha256**: 0455b406d89648d20cbde375561e19c245b9815e894164c2670772e3d54deb82
    - **saved_at**: /tmp/claude-0/-home-user/bfcfd013-a2da-5019-961e-7f46116f08be/scratchpad/wf-sources/fips180-4/dl-1/NIST.FIPS.180-4.pdf
    - **repo_recorded**: SHA-256 0455b406d89648d20cbde375561e19c245b9815e894164c2670772e3d54deb82 (reading record line 3); 36 PDF pages (line 10). LEDGER.md line 31 (STD-002) records only an l6 archive commit `b328334`, no file hash or size.
    - **same_as_recorded**: yes - sha256 identical; page count 36 identical (pdfinfo)
  - item 2
    - **name**: CSRC publication page for FIPS 180-4
    - **official_url**: https://csrc.nist.gov/pubs/fips/180-4/upd1/final
    - **final_url**: https://csrc.nist.gov/pubs/fips/180-4/upd1/final
    - **http_status**: 200
    - **bytes**: 40642
    - **sha256**: 7a7e3f8247e0c04b6c22109bc1031527a1928e384da5a878269e7be4b5cf8fc5
    - **saved_at**: /tmp/claude-0/-home-user/bfcfd013-a2da-5019-961e-7f46116f08be/scratchpad/wf-sources/fips180-4/dl-2/csrc.html
    - **repo_recorded**: not recorded
    - **same_as_recorded**: n/a - page shows: FIPS 180-4, Secure Hash Standard (SHS); Date Published August 2015; Supersedes FIPS 180-4 (03/06/2012); Document History 08/04/15: FIPS 180-4 (Final); Planning Note (03/07/2023): NIST has decided to revise FIPS 180-4. Status is Final, not withdrawn. Consistent with the record and with ledger citation '[source text withheld from the public copy].'
- **items_total**: 224
- **confirmed**: 221
- **problems**
  - item 1
    - **id**: fips180-4-1
    - **kind**: COUNT-WRONG
    - **repo_locator**: auditonomous origin/main:L7/provenance/sources/staging-records/library/reading/NIST_FIPS-180-4_Secure-Hash-Standard.md lines 17, 21, 29
    - **repo_text**: [source text withheld from the public copy]
    - **source_locator**: Official PDF, 36 pages (pdfinfo)
    - **source_text**: Pages the record itself enumerates as read: 1-5, 6-7, 8, 9-11, 12, 18-19, 21-22, 23-25, 32-36 = 24 pages. Pages it enumerates as not read: 13-17, 20, 26-31 = 12 pages. 24 + 12 = 36.
    - **note**: The record gives two different read counts (25 and 24) and an unread count (eleven) that does not match its own page list or the 36-page source. 24 read / 12 unread is the figure consistent with the source. The absence claims are unaffected: I re-ran every keyword over all 36 pages.
  - item 2
    - **id**: fips180-4-2
    - **kind**: MISATTRIBUTED
    - **repo_locator**: same reading record, line 21
    - **repo_text**: "[source text withheld from the public copy])"
    - **source_locator**: Official PDF pp. 13-20 (printed 8-15)
    - **source_text**: PDF pp13-14: end of Sec. 3.1 (item 4) and Sec. 3.2; pp15-17: Sec. 4.1 and 4.2 (through 4.2.3). "5. PREPROCESSING" and "5.1 Padding the Message" begin on PDF p18. "5.3.3 SHA-256", "5.3.4 SHA-384" and "5.3.5 SHA-512" are all on PDF p20.
    - **note**: Section 5.1 and Sections 5.3.3-5.3.5 are not on pp13-17. Section 5.1 is on p18, which the record elsewhere says it read and quotes from (C16); 5.3.3-5.3.5 are on p20, which holds the SHA-256, SHA-384 and SHA-512 initial values, not only SHA-512's. Page-content description error only; no quotation is affected.
  - item 3
    - **id**: fips180-4-3
    - **kind**: MISMATCH
    - **repo_locator**: same reading record, line 216 (C14 'Bears on')
    - **repo_text**: Two DIFFERENT computation paths ... 'yield the same message digest'.
    - **source_locator**: Official PDF p25 (printed p20), Sec. 6.1.3
    - **source_text**: "The alternate method that is described in this section [yields] the same message digest as the SHA-1 computation method described in Sec. 6.1.2."
    - **note**: Differing word: record 'yield', source 'yields'. A grammatical adaptation placed inside quotation marks in commentary; the C14 block quotation itself reproduces 'yields' correctly. Trivial.
- **could_not_check**
  - item 1
    - **what**: LEDGER.md row STD-002: l6 path `library/standards/nist/nist-fips-180-4-secure-hash-standard-2015.pdf` at l6 commit `b328334`, and the label '[source text withheld from the public copy]'
    - **why**: The ledger points to the internal aybllc/l6 archive, which is not among the repositories given to me; no PDF of this standard exists in auditonomous at origin/main or at origin/claude/book-structure-roadmap-k8ap82. The ledger row carries no sha256 or size to compare. Only the citation ([source text withheld from the public copy]) could be confirmed. For reference, the git blob id of the official PDF is 5462a6a01d7aa1124d853c5c0f8eade62ffa2603.
  - item 2
    - **what**: The record's reading of the Erratum as a change to 't ≤ 79', and its statement that equations such as a ← H0^(i-1) sit behind the garbled text on p24
    - **why**: The text layer carries these glyphs only as Symbol-font private-use code points (U+F0A3 on p36, U+F03D/U+F02D on p24). I confirmed those code points are present exactly where the record says, but the glyph identity cannot be established from pdftotext output alone.
  - item 3
    - **what**: Verifier's measured elision lengths of 148 characters (C13, p24) and 733 characters (C17, p19)
    - **why**: On my whitespace-collapsed extraction the gaps measure 177 and 730 characters. The measure depends on how whitespace and private-use glyphs are counted, so the difference is not reportable as a mismatch. The other two measures (236 on p4, 246 on p12) reproduce exactly.
- **summary**: I tested the FIPS 180-4 reading record and its ledger row against the official PDF from nvlpubs.nist.gov (HTTP 200, 833,315 bytes). Its sha256 is identical to the one the record gives, so the record was made from the same file NIST serves today. The csrc.nist.gov page confirms the title, the number, publication in August 2015 and Final status, with a 2023 note that NIST has decided to revise it.

  Of 224 items tested, 221 were confirmed. All 25 block quotations (29 contiguous segments) are verbatim on the PDF page, printed page and section the record names. All 55 table-of-contents entries match. The title-page and other citation details match, as do the short quotations embedded in the commentary. All 22 keyword counts reproduce over the full 36 pages, including zero for collision, preimage, deprecat, tamper and chain, and "security strength" twice on p8. The structural claims hold: seven glossary entries, three references, "five hash algorithms" followed by seven names, and "FIPS 140-4" as printed.

  Three minor problems, none affecting a block quotation:
  - **Page counts:** the record says both 25 and 24 pages read and "eleven" unread; its own page list gives 24 and 12.
  - **Page contents:** it places Sec. 5.1 and 5.3.3-5.3.5 on pp13-17; they are on p18 and p20.
  - **One word:** commentary quotes "yield" where the source says "yields".

  The ledger's l6 archive commit could not be checked.
