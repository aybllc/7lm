# verify:KC-02

Agent result, as returned. Workflow: Handle on the Auditonomous research and manuscript. Run `wf_9c2917a7-7f0`. Phase: Verify.

- **id**: KC-02
- **verdict**: corrected
- **reasoning**: Every cited locator checks out verbatim, but three parts of the claim are imprecise or overstated.

  CONFIRMED
  - MAIN:README.md:11 reads "The L0 object, the active definition of record (AU-NORM-02): `L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md`." The entry's header (MAIN:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:3) says "Developed 2026-07-30".
  - AU-NORM-02 is recorded as an owner ruling at MAIN:L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:32 ("Active definition of the coined word: ... AU-NORM-02). Root `AUDITONOMOUS.md` is history-only by ruling.") and in the message of commit 4a1c1db ("owner rulings AU-NORM-01..04"). No standalone ruling text exists in any of the three states; a search for AU-NORM-02 returns only ledger, sheet and README references.
  - ROADMAP:L8/L0/semantics/definitions/AUDITONOMY.md:3-5 reads as quoted. The blob (79b35ee) is byte-identical to HISTORY 1d83788:manuscripts/definitions/AUDITONOMY.md; it was restored at 62d2e3f on 2026-09-14. Its internal dates are 2026-08-04 and 2026-08-05 only.
  - AUDITONOMY.md is absent from the MAIN and BETA trees and from every other remote ref at the L0 path. It is also absent from all three refs of the autonomous repository.
  - MAIN:L8/L5/research/findings/DISTILLATION.md:21 reads "(`definitions/AUDITONOMY.md`, governing text)".

  IMPRECISE OR OVERSTATED
  1. "Two texts claim to be the definition" blurs two headwords. The 30 July text is "AUDITONOMOUS — the defining entry" for the adjective (MAIN: DEF:1, :14). AUDITONOMY.md is "TERM ENTRY — AUDITONOMY" for the noun (ROADMAP: AUD:1, :17 "THE DEFINITION", :67 "Canonical definition."). They do overlap, in both directions:
     - DEF:28 glosses the noun: "auditonomy: bounded autonomy under mandatory auditability".
     - AUD:69 defines it differently: "[source text withheld from the public copy]".
     - AUD also says what an auditonomous system is (AUD:143, and AUD:197 "[source text withheld from the public copy]"), which matches none of DEF's three senses.

  2. "No document states their relation" is false of ROADMAP as worded. Three ROADMAP documents state a headword relation:
     - ROADMAP:L8/L0/semantics/definitions/0.md:32 and :34 call DEF "the locally authored definition of *auditonomous* (adj.) ... the active record" and AUD "TERM ENTRY — AUDITONOMY, the derived noun".
     - ROADMAP:L8/L0/0.md:93 lists both as "The two L0 objects this repository authors".
     - ROADMAP vocabulary paper :20, :48 and :104 treat DEF as "the entry of record" and AUD as the noun's "term entry (the L0 object)".
     What holds is narrower: no document says which text controls where they overlap, and neither text cites the other (searches of each for the other's name return nothing). Decision D20 (ROADMAP:BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:630) ranks three framings of auditonomy and does not include DEF. On MAIN and BETA no relation can be stated because AUDITONOMY.md is not there.

  3. AU-NORM-02 does not adjudicate between these two texts. It ranked the 30 July entry over the consolidated root AUDITONOMOUS.md of 2026-08-04. AUDITONOMY.md had been deleted at 8c98573 on 2026-08-15 (462 deletions) and was not in the tree at the ruling commit 4a1c1db.

  4. "Says its v2 definition governs" is accurate, but the header's scope is internal to the file: v2 (§0) over the five-condition form (§2), "retained as its anchor analysis". It does not assert precedence over the 30 July entry.

  5. State precision:
     - The 30 July entry is on all three states, not only MAIN. MAIN and ROADMAP share blob 8b934b4. BETA carries blob 8127041, which adds a "Receiving semantic reference (2026-11-03 correction)" paragraph and "Current role" lines in Appendix C.
     - DISTILLATION.md is the same blob (cc56719) on MAIN, ROADMAP and BETA, so "governing text" is said on all three.
     - On MAIN and BETA the path it cites is dangling. MAIN:L8/L1/state-space/AUDITON_ENVELOPE.md:76 and :253 cite the same absent file.

  EVIDENCE AGAINST, NOT CITED BY THE CLAIM
  The distillation compresses a state of its "governing text" that the text itself later reversed. MAIN:DISTILLATION.md:38 says "[source text withheld from the public copy]." ROADMAP:AUD:42-44 says "**[source text withheld from the public copy]".

  EVIDENCE STATE: UNRESOLVED on which text controls; CONTRADICTED on the gloss of "auditonomy" (DEF:28 against AUD:69) and on stop adjudication (DISTILLATION:38 against AUD:42-44).
- **corrected_statement**: Two L0 texts each carry a definition, for different headwords, and no document says which controls where they overlap.

  (1) AUDITONOMOUS_DEFINITION.md is the lexicographic entry for the adjective, developed 2026-07-30. It is "the active definition of record (AU-NORM-02)" (MAIN:README.md:11). It is present on MAIN and ROADMAP as the same blob, and on BETA with a 2026-11-03 addendum. AU-NORM-02 (owner ruling recorded in LEDGER_2026-08-16:32 and commit 4a1c1db) ranked this entry over the consolidated root AUDITONOMOUS.md. It did not address AUDITONOMY.md, which had been deleted the day before at 8c98573.

  (2) AUDITONOMY.md is the term entry for the derived noun, [source text withheld from the public copy]. It is labelled "CONJECTURE / INTERNAL ONLY". Its header says "[source text withheld from the public copy])", meaning v2 over its own five-condition form of §2, not over the 30 July entry. It is on ROADMAP only (restored 2026-09-14, byte-identical to 1d83788) and absent from MAIN and BETA.

  ROADMAP does state a headword relation: definitions/0.md:32,34, L8/L0/0.md:93 and the vocabulary paper §3 and §5.1 call one "the active record" for the adjective and the other the term entry for "the derived noun". No document on any state reconciles the overlaps or says which governs:
  - DEF:28 glosses auditonomy as "bounded autonomy under mandatory auditability"; AUD:69 defines it as "[source text withheld from the public copy]".
  - AUD:143 and AUD:197 say what an auditonomous system is, matching none of DEF's three senses.
  - Neither text cites the other, and decision D20 does not include the 30 July entry.

  DISTILLATION.md:21, the same blob on MAIN, ROADMAP and BETA, calls `definitions/AUDITONOMY.md` the "governing text". On MAIN and BETA that path is dangling. Its line 38 ("[source text withheld from the public copy]") summarises language that AUDITONOMY.md:42-44 itself reversed on 2026-08-05 ("stop is NOT refusable").

  Evidence state: UNRESOLVED on precedence; CONTRADICTED on the noun gloss and on stop adjudication.
- **evidence_checked**
  - MAIN:README.md:11 - "The L0 object, the active definition of record (AU-NORM-02): `L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md`."
  - MAIN:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:1-5,14,28 - "AUDITONOMOUS — the defining entry"; "Developed 2026-07-30"; "[source text withheld from the public copy]."
  - ROADMAP:L8/L0/semantics/definitions/AUDITONOMY.md:1-5 - "`[source text withheld from the public copy]."
  - ROADMAP:L8/L0/semantics/definitions/AUDITONOMY.md:42-44,67-70,143,197 - "**[source text withheld from the public copy]"
  - MAIN:L8/L5/research/findings/DISTILLATION.md:21,38 - "(`definitions/AUDITONOMY.md`, governing text)"; "[source text withheld from the public copy]." Blob cc56719 identical on MAIN, ROADMAP and BETA (git rev-parse).
  - MAIN:L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:32 - "Active definition of the coined word: ... (410 lines, restored verbatim from `1d83788`; AU-NORM-02). Root `AUDITONOMOUS.md` is history-only by ruling."
  - Commit 4a1c1db message (2026-08-16): "structural normalization under owner rulings AU-NORM-01..04"; "Active lexicographic record per AU-NORM-02; root AUDITONOMOUS.md stays history-only." Tree at 4a1c1db has AUDITONOMOUS_DEFINITION.md and no AUDITONOMY.md.
  - Commit 8c98573 (2026-08-15): manuscripts/definitions/AUDITONOMY.md deleted (462 deletions); returned at 62d2e3f (2026-09-14).
  - ROADMAP:L8/L0/semantics/definitions/0.md:32,34 - "the locally authored definition of *auditonomous* (adj.) ... restored verbatim per AU-NORM-02 as the active record"; "`AUDITONOMY.md` — TERM ENTRY — AUDITONOMY, the derived noun: the v2 [source text withheld from the public copy]"
  - ROADMAP:L8/L0/0.md:93 - "`semantics/definitions/AUDITONOMY.md` — the term entry for the derived noun, CONJECTURE / INTERNAL ONLY by its own header, restored 2026-09-14. The two L0 objects this repository authors."
  - ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:20,48,104,267,294 - "[source text withheld from the public copy])"; framings of auditonomy referred to D20
  - ROADMAP:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:420,630 - "[source text withheld from the public copy])"; D20 ranks three framings of auditonomy and does not include the 30 July entry
  - Tree listings (git ls-tree -r) of MAIN, ROADMAP, BETA under L8/L0/semantics/definitions/: AUDITONOMY.md present on ROADMAP only; no other remote ref carries it at that path; absent from autonomous origin/main, beta and scholarly-pair refs
  - Blob identity: AUDITONOMOUS_DEFINITION.md is 8b934b4 on MAIN and ROADMAP, 8127041 on BETA (git diff shows an added "Receiving semantic reference (2026-11-03 correction)" paragraph and Appendix C "Current role" lines); AUDITONOMY.md is 79b35ee on ROADMAP and at 1d83788:manuscripts/definitions/AUDITONOMY.md
  - Cross-reference search: grep of ROADMAP AUDITONOMY.md for AUDITONOMOUS_DEFINITION, lexicograph, 07-30, three senses returned nothing; grep of MAIN AUDITONOMOUS_DEFINITION.md for AUDITONOMY.md, v2, five-condition, sovereignty returned nothing relevant
  - MAIN:L8/L1/state-space/AUDITON_ENVELOPE.md:76,253 - cite `definitions/AUDITONOMY.md`, a path absent on MAIN and BETA
  - HISTORY 1d83788:manuscripts/definitions/REGISTER.md:12,16 (not restored in any current state) - listed the consolidated AUDITONOMOUS.md for "auditonomous / auditonomy" and "auditonomy (term entry) | AUDITONOMY.md ... v2 definition governs"; the 30 July entry then stood at intake/AUDITONOMOUS_DEFINITION.md
  - Search for AU-NORM-02 across MAIN, ROADMAP, BETA (git grep -F): only README.md:11, L8/L0/0.md, definitions/0.md, the 2026-08-16 ledger, the 2026-09-05 routing plan, and on ROADMAP the vocabulary paper, restore-2026-09-14.md:26 and the retired sheets; no standalone ruling text found
