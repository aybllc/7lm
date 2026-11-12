# Final return of the workflow: Handle on the Auditonomous research and manuscript

As returned. Run `wf_9c2917a7-7f0`.

- **summary**: Read-only: a quality-assurance handle on the Auditonomous research and manuscript, position by position, with verified evidence
- **agentCount**: 29
- **logs**
  - readers returned: 14/14, items: 589, defects: 257
  - claims: 12, verdicts: 12, corrected or refuted: 12, gaps: 12
- **result**
  - **report**: # Auditonomous: where the research stands, and what the manuscript can take from it

    Read on 11 November 2026 from git objects only. Nothing was changed.

    **States.** MAIN = origin/main 2165144, unchanged since 11 September 2026. ROADMAP = the closed branch of pull request #27, 9259c18. BETA = origin/beta/7lm-exemplar-auditonomous 714480d, committed 2 November 2026 (Pacific time). HISTORY = commit 1d83788, the tree before the prune of 15 August 2026. MAIN is an ancestor of both branches. ROADMAP holds all 169 of MAIN's paths and 159 more. BETA keeps 163 of them, renames 6 and adds 17. ROADMAP and BETA are the only pair where neither contains the other.

    **Short names.** DEF = L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md. AUDY = L8/L0/semantics/definitions/AUDITONOMY.md. CONS = L8/L6/retired/consolidated-2026-08-04/AUDITONOMOUS.md (ROADMAP). RM = L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md. REV/ = L8/L5/research/review/. FIND/ = L8/L5/research/findings/. SS/ = L8/L1/state-space/. STG/ = L7/provenance/sources/staging-records/. HIST/ = L8/L6/history/. AUT = aybllc/autonomous origin/main. 7LM-MAIN = aybllc/7lm origin/main c9dc061.

    Words in capitals inside quotation marks are the repository's own labels. Evidence states in plain capitals are my assignments. Ids such as X-02 or U-01 point into the open register.

    ## The short answer

    The research is a set of dated working records written between 30 July and 14 September 2026, plus one small computation of 2 November 2026.

    - **MAIN holds** the definition entry, the state space, an empty formal layer, one engineering proposal, three standards extractions, three findings, the seven standards contradictions, the perpetuity adjudication and the source records.
    - **Only ROADMAP holds** the noun entry (AUDY), the lambda thesis and its checks, the docket, the author assertions, four findings, eight probes, the corpus, 23 internal contradictions and the roadmap.
    - **BETA adds** a 16-case synthetic run and corrections to the records.
    - **No live tree holds** the term ledger, the contamination rule or the prior-art search record.

    Outside checks are narrow. They cover the word's roots, quotations from the sources that were read, the lambda arithmetic against Rump 1999, the external audit's sample, and bounded searches for the word. No executed test of any system against the definition exists. A prior-art search was run, although the repository's labels say it was not. Searches of 2, 5 and 8 August 2026 found the word not new and the definition unrefuted, but none reached publisher-of-record or standards hosts. The search on whether "autonomous" entails auditability was queued on 16 August 2026 and never run.

    The live contradictions:
    - four defining texts, with no stated precedence;
    - "concealment impossible", against the repository's own reading that records detect and do not prevent;
    - three positions on Q13;
    - eleven definitions of "autonomous", with no baseline;
    - 23 internal contradictions, never resolved.

    The manuscript can draw today on four things: the definition as the author's statement, verbatim standards quotations within licence limits, the lambda results with their conditions, and the contradiction registers as method. It cannot draw on any claim that the concept is new, any claim of conformance or achievement, any formal statement, or any number in the first-contact chapters.

    ## The research, from the bottom up

    **L0, the definition.** MAIN holds DEF, the entry for the adjective. It has 410 lines, is dated 30 July 2026, has been byte-identical since the first commit, and gives three senses, eight criteria, a firmware clause and seven exclusions. It is the "active definition of record (AU-NORM-02)" (MAIN:README.md:11). The ruling survives only as a ledger line (MAIN:HIST/LEDGER_2026-08-16_l6-close-and-normalization.md:32) and in commit 4a1c1db. It ranked DEF over the consolidated root file. It did not rank DEF over AUDY, which had been deleted the day before.

    ROADMAP adds AUDY, the entry for the noun, labelled "CONJECTURE / INTERNAL ONLY". Its "[source text withheld from the public copy])" over its own five conditions, which it keeps as "anchor analysis" (ROADMAP:AUDY:3-5). ROADMAP's sheets state how the two headwords relate, but nothing says which text governs where they overlap. DEF:28 gives the noun as "bounded autonomy under mandatory auditability"; AUDY:69 gives it as "[source text withheld from the public copy]".

    CONS adds two more defining texts. One is the constitutional sentence, labelled "the primary definiens" (CONS:70-74). The other is a fused form: "Neither is preferred here. Both stand." (:80-96). DEF quotes the constitutional sentence without its third clause, "a runtime without parameters". MAIN's distillation calls AUDY the "governing text" (FIND/DISTILLATION.md:21), but that path does not exist on MAIN or BETA. BETA inserts 16 lines into DEF. The other four L0 positions are EMPTY.

    Evidence:
    - The roots are EXTERNALLY CHECKED: 13 "VERIFIED" and 1 "PARTIALLY VERIFIED", on 30 July 2026.
    - The senses and criteria are ASSERTED.
    - Sense 3, the firmware clause, line 52 and the noun's gloss are CONTRADICTED.
    - AUDY is CONJECTURE.
    - Which text takes precedence is UNRESOLVED.

    Verdict: four defining texts, and no precedence among them.

    **L1, state space.** MAIN holds three documents:
    - AUDITON_ENVELOPE: twelve compartments, eight supplied by the envelope, three legal freezes.
    - HUMINT_ENCODE: H1 to H7.
    - REQUIREMENTS_OWNERSHIP: 113 requirements, split 21 / 4 / 6 / 0 / 82.

    ROADMAP adds AUDITABILITY_REQUIREMENTS and AUDITON_REPLICATOR. BETA adds a short admission note. The envelope labels itself "`COMPOSITE OBJECT UNVERIFIED`. Not adversarially reviewed."

    Evidence:
    - The composition is ASSERTED.
    - The partition is INTERNALLY CHECKED for 99 rows.
    - The 14 NASA rows exist only in a workflow journal outside the repository (SS/REQUIREMENTS_OWNERSHIP.md:12-14).
    - "[source text withheld from the public copy]" (:117) and "76%" (:264) are CONTRADICTED by the same file's line 72 and table, which give fifteen, or 71%.
    - The replicator's review refuted "two of three headline claims" (HISTORY:manuscripts/definitions/REGISTER.md:14), and the replicator reopens the envelope's root of trust.

    Verdict: an unreviewed architecture over quoted controls, with counts that must be corrected before print.

    **L2, formal mathematics.** EMPTY on MAIN and ROADMAP: "Currently: **EMPTY** — no formulas held." (MAIN:L8/L2/formal-mathematics/FORMULAS_LEDGER.md:10). The sheets name two candidates that are not registered. One is the isomorphism (ℝ≥0,+) ≅ ((0,1],×), whose four-line proof holds when redone by hand. The other is the perpetuity argument.

    A predicate for the word exists. It is model-written, unratified and unregistered: [source text withheld from the public copy] (ROADMAP:L8/L4/work/writing/sourcebook/Auditonomous_Book_Material_Sourcebook_v0.1.md:113-132). It also sits inside auditnomous-main.docx in all three states. The repository's own log flags it: "[source text withheld from the public copy]" (ROADMAP:L8/L4/work/writing/sessions/SESSION_2026-08-05_VERIFICATION_LOG.md:134). The vocabulary paper (:305) and RM (:583, :647) record that no such predicate occurs. That negative finding is CONTRADICTED: the predicate is written `\operatorname{Aud}`, which a literal search misses.

    Two other if-and-only-if forms are also unregistered: AUDY:197, with conditions A to E, and "AuditonomousAction(α) ⇔ …" in the chat .docx files. BETA files a fixture predicate, while BETA's own L2 sheets say nothing is filed (CONTRADICTED). 7LM-MAIN's specification keeps "the project's formulas for life" out of L2 and places them at L3 when applied (spec :607-609).

    Verdict: no registered formal statement exists, and the one predicate on offer is ASSERTED and CONTRADICTED.

    **L3, engineering mathematics.** The Seal-Gated Interlock reads "Status: PROPOSAL. [source text withheld from the public copy]." It is UNRESOLVED: its attack pass was never folded in, and IEC 61508 and ISO 13849 are "NOT-CHECKED". The external priors record is EXTERNALLY CHECKED as recorded, but has no URL, fetch date, hash or ledger row. Approximation and tolerances are EMPTY. Verdict: no method exists for any defining criterion.

    **L4, computation and experiments.** Experiments are EMPTY in every state: "No experiment has been executed". The definition disclaims achievement, not testing (MAIN:DEF:57). The desk comparisons that exist all conclude that the system does not satisfy the definition:
    - eBIOS, against the firmware clause (MAIN:DEF:47, :252);
    - NASA DSA/Starling, in ROADMAP's Master Archive (:312-314);
    - the SpudCell, which "fails almost every clause" (Master Archive :486).

    MAIN holds the three extractions, EXTERNALLY CHECKED by their own single-pass record, and a deep-research report labelled "model output as run, never evidence".

    ROADMAP's eight probes and the OMMP codec ("NOT CANONICAL") were re-run on 11 November 2026. Every compared probe figure matched its record. The codec suite passed 65 checks, where its README says 66.

    BETA's fixture runs 16 synthetic cases and 32 events against two selected predicates, C6 stop and C7 record, "not full auditonomous meaning". All four of its *_achieved flags are false, and standards_autonomy is "unresolved". Its 12 tests passed, and the result reproduced except for the Python version.

    Evidence: INTERNALLY CHECKED. Verdict: the arithmetic reproduces, and none of it tests a system.

    **L5, lanes, review, findings.** Lanes (MAIN): eleven clusters, sixteen tensions and twelve record-ontology questions, all "OPEN" and untouched since 4 August 2026.

    Review, on MAIN:
    - C1 to C7. The quotes are EXTERNALLY CHECKED as recorded, none is resolved, and the cross-links are dead.
    - The perpetuity adjudication.
    - The catch-all's "#autonomous(1).txt". It is a 2025 draft, "Autonomous Theory: Post-Biological Intelligence" (CONJECTURE, unlabelled). From about line 636 it continues as a raw chat export carrying an account identifier and seven e-mail addresses, some of them third parties'. That export is now in every state's history.

    Review, on ROADMAP only:
    - six lambda documents and three dated records;
    - the external audit;
    - the docket, with 45 entries, 5 closed;
    - author assertions A-001 to A-009c (ASSERTED);
    - source requests SR-01 to SR-24;
    - a census dossier with nothing verified;
    - the defect ledger on your N/U algebra paper;
    - the cycles review and the Tic Tac adjudication;
    - CONS §11's 23 internal contradictions, "None resolved. None ranked." (:1117-1183). They are filed as retired, yet RM uses them as a feed.

    Findings: three on MAIN, four more on ROADMAP, one on BETA. Each ends "nothing adopted", and none has a recorded review. Institution is EMPTY.

    Verdict: claims were tested and narrowed, and almost nothing was ruled.

    **L6, the records.** MAIN holds ten record files and two retired sets, all on custody and layout. Every ledger says "External Sources Checked: NONE". The master ledger is CONTRADICTED by the tree. ROADMAP's restore record lists all 318 pre-prune paths, and the list is exact.

    Only HISTORY holds the freeze file, the hub ledger, your early drafts, and research the restore left out:
    - the term ledger AUTONOMOUS_TERMS.md, T-01 to T-25, all "UNVERIFIED";
    - TERM_LANES.md, the only per-term record of what was read at source;
    - the root AUTONOMOUS.md;
    - the definitions REGISTER.md;
    - intake/MANIFEST.md, "[source text withheld from the public copy]", which limits DEF's claims about where the word appears.

    The restore record says the peer holds the term ledger (ROADMAP:HIST/restore-2026-09-14.md:230-231). No Autonomous ref does (CONTRADICTED). The freeze file's contamination rule includes "[source text withheld from the public copy]." (HISTORY:FREEZE.md:65). It stands in no live tree.

    Verdict: sound on custody, stale on the tree.

    **L7, sources, bindings, conditions, release.** The source ledger has 60 rows, not the 62 that MAIN's sheets state. One sheet also says "The ledger has no rows" (L7/provenance/sources/0.md:55), and the ledger counts 27 staging records where 25 exist. BETA corrects the count to 60 and adds AUT-SOURCE-001.

    Fifty-eight rows point into aybllc/l6, which is labelled "private/INTERNAL" and was not available for this reading. Two exclusion rows are "HELD OUT of l6". In the ledger, "VERIFIED" means the staged file matched the archive copy. One such row reads "NOT READ" (PR-002).

    Reading is recorded for 14 of the 58 held sources. Two of those records are limited: the IEEE 1788-2015 record covers decorations only, and the ISO/IEC 22989 captures come from a withdrawn copy and have not been re-verified.

    The definition's dictionary, NIST, RFC and AI 100-1 citations have no rows. IEEE 7001 has row STD-004, but DEF cites the catalogue page instead. SP 800-53 has no row. HISTORY's _STAGING_TO_L6/ holds staged PDFs that no live tree holds, among them IEEE 7009-2024, 1920.1 and 1788.1-2017, all hold-private.

    One binding is pinned and confirmed, to Autonomous at 0504961. Three have no version: eb-audit, ebios with the Martin 2026 manuscript, and the Third Power Corpus. Nothing is released, and all six checklist boxes are unticked.

    Verdict: the base supports quotation from the fourteen sources that were read, and clears nothing for release.

    ## What has been checked, and against what

    External checks on record, and what each settled:

    1. **Word roots**, 30 July 2026, against American Heritage, Perseus, the NIST glossary, RFC 4949, [source text withheld from the public copy] IEEE 7001 scope page. This settled lexical ancestry only (MAIN:DEF:281-347).
    2. **Eleven [source text withheld from the public copy]**, 4 August 2026, in two intakes. A verifier found no fabrication.
       - Library intake: ARIES, Haber and Stornetta, Ferreira, FIPS 180-4, RFC 6962, RFC 9162. Its finding: "**[source text withheld from the public copy].**" (MAIN:STG/library/FINDINGS_2026-08-04.md:62). The finding is aimed at the Git claim and the constitutional sentence, not at DEF, and is labelled "CONTESTED", "NOT ADOPTED".
       - IEEE intake: 7001, 7007, 7009, 7014, 3152. 7001 calls for an independent recorder of "**non-modifiable** data" (MAIN:STG/ieee/FINDINGS_2026-08-04.md:107). 7014 defines auditability for empathic systems only, and requires deletion.
    3. **Three extractions, 99 rows.** The ISO, NASA and NIST rows are definitional. No body read states a least-function rule.
    4. **C1 to C7.** C1, C2 and C4 match the extractions. C2 is overstated. C4's "Heteronomous" is unverified in the bound entry.
    5. **Lambda**, 4 August 2026, against Rump 1999 and others.
       - λ = 1 is Rump's midpoint-radius product, and it encloses in exact arithmetic ("ESTABLISHED").
       - The λ = 0 radius is exact for sign-definite operands ("EXTERNALLY VERIFIED"). The interval is exact only with the centre shifted, and that shift is the repository's own step.
       - The "meaningful digit" argument is refuted.
       - The Rump 1999 quotes match Autonomous's copy (AUT:L7/provenance/prior-art/prior-art-lane/ru99.txt:117, :165-172).
       - Rump 2010 is not held, floating-point rounding is unchecked, and the adversarial pass has no recorded outcome (U-18).
    6. **The external audit**, 4 August 2026: "[source text withheld from the public copy] Git and kilogram sentences are wrong, and three blockers were false. Most corrections never reached the files concerned (R-09).
    7. **Perpetuity**, 2 August 2026 (REV/PERPETUITY_QUESTION_ADJUDICATION.md:91-100).
       - No theorem says an autonomous system must end.
       - The words have zero occurrences in five scholarly indexes and in Google Patents.
       - A 2018 blog, "a **prohibited source**", defeats "absolute lexical novelty of the noun".
    8. **Prior art**, 5 and 8 August 2026.
       - Standards indexes: "PARTIALLY CHECKED — negative" (ROADMAP:REV/WALK_ACROSS_repo-instrument-standards_2026-08-05.md:42).
       - 30 IEEE PDFs: zero hits (HISTORY:FREEZE.md:17-28).
       - A 260-line record of 8 August: "coinage not superseded; lexical novelty refuted; definitional novelty unrefuted". It was deleted from Autonomous at ab8f01f. Its verdict is kept at AUT:HIST/HUB_SURVEY_2026-08-14.md:951-970.
    9. **T3.** ISO 15489-1:2001 clause 7.2.2 lists five acts, and neither "falsify" nor "erase" is among them.
    10. **Cosmology as prior art for lambda.** Three claims refuted.
    11. **NIST SP 800-53 Rev. 5.** 215 control statements transcribed and recounted. No ledger row.

    Internal checks on record:
    - the 99 partition rows;
    - the probes;
    - DR-003;
    - the defect ledger's (2,1) ⊗ (7,2) = [3,25], against a true [5,27];
    - λ = 0 as coded, which fails whenever both radii are nonzero. The code line it was tested on is itself "UNVERIFIED" as eb-stack's code.
    - the bound definition's bytes, identical at 0504961 and on Autonomous main;
    - BETA's 16 cases;
    - the restore table;
    - a string search, recorded only in two unmerged papers, that found no record, audit, log, trace or account term in the eleven definitions. "Oversight" occurs in four of them.

    None of this bears on whether any system is auditonomous. Every EXTERNALLY CHECKED state rests on what the repository recorded. Only the Rump 1999 quotes were compared again.

    ## What is contradicted or open

    **The definition.**
    - X-01: four defining texts. HISTORY's register entered both CONS and AUDY as "ADOPTED as coinage" on 14 August 2026. Whether A to E define the noun or analyse it is open.
    - X-02: DEF:52 says "[source text withheld from the public copy]". Two records answer it, and neither cites the other.
      - The adjudication: "[source text withheld from the public copy]**" (REV/PERPETUITY_QUESTION_ADJUDICATION.md:216), pending your ruling.
      - The cycles review: "Audit is not necessarily post hoc" (ROADMAP:REV/AUTONOMOUS_vs_AUDITONOMOUS_CYCLES.md:136).

      Your remark behind the edit: "the udiot is always post hoc." The edit covers line 52 only. It does not touch sense 1 ("structurally unable to conceal") or sense 3 ("making concealment impossible").
    - X-03: two senses or three.
    - X-04: what the word blends.
    - X-05: firmware, against an intelligence layer above the ROM.
    - X-07: "immutable", after the override finding.
    - The adjective form: "[source text withheld from the public copy] stop path.** The drift check of 5 August 2026 returned "2 FAILED of 13" when the stop path left the kernel. You answered "[source text withheld from the public copy]." (HISTORY:FREEZE.md:167-186). AUDY records "[source text withheld from the public copy]" (:42-44). X-13: MAIN's distillation still has "[source text withheld from the public copy]." (FIND/DISTILLATION.md:38) and "it may refuse or delay" (:262).

    **CONS §11.** These items are CONTRADICTED or UNRESOLVED, and none has been re-verified against the corpus. They include:
    - C-2: "Bounded autonomy", [source text withheld from the public copy]."
    - C-4: a constraint on concealment only, against "unlawful motion is physically unreachable".
    - C-8: "FAILED CHECK on the independence claim" of the fourth derivation.
    - C-13: certification as a layer, or as a consumer.
    - C-14 and C-15: gate-then-ledger against ledger-then-gate, the conflict behind X-16.
    - C-20: the A-scale never meets the word.
    - In §10.4, the A2 and A3 ordinality fixes: "FAILED CHECK / OPEN".

    **State space.**
    - X-08: three positions on Q13.
    - X-09: packability, against autonomy-at-distance.
    - X-10: sixteen, against fifteen.
    - X-12: the root of trust.
    - X-15: law L5, against the replicator's review.
    - X-16: trace-before-release, against a one-way carrier.

    **Lambda.**
    - X-14: the thesis reads λ_A = 0 as "exactly known, zero uncertainty"; the departure protocol says "It does not mean numerical zero, exactness".
    - X-17: the vocabulary paper (:252) and the Autonomous finding (:33) call λ = 1 exact, against Rump's Theorem 2.4.
    - Your "lambda 0 DOES MAKE an enclosure claim" (MAIN:L8/L4/work/writing/sessions/SESSION_2026-08-05_AUDITON_ARCHITECTURE.md:388-402) has no recorded test.

    **Unrun checks.**
    - U-01: no novelty search at publisher-of-record or standards hosts. The "unrun" labels (ROADMAP:AUDY:263; FIND/DISTILLATION.md:134; MAIN:L7/provenance/prior-art/0.md:32) are stale.
    - U-02: the entailment search. It was queued at MAIN:HIST/LEDGER_2026-08-16_l6-close-and-normalization.md:48, beside partial evidence that "must not be overextended". Autonomous's auditability lane of 3 August 2026 (AUT:L8/L5/research/lanes/LANE_B_AUDITABILITY.md) also bears on it.
    - U-03 and U-04: the auditability extraction, and 78 against 113.
    - U-05: no L1 object has been reviewed.
    - U-06: the interlock's attack pass.
    - U-07: ISO/IEC 22989.
    - U-20: the λ_A operators, "named, none defined".

    **Missing objects.**
    - M-01: AUDY is not on MAIN.
    - M-02: the defining manuscript is not on MAIN or BETA.
    - M-03: abba-01/ebios is in no clone.
    - M-04: the NASA rows.
    - M-10: every formal object.
    - The HISTORY-only objects listed under L6, and the prior-art record.

    **The workflow.** MAIN's .github/workflows/integrity.yml still requires L7/governance/restrictions and L7/publications, and allows a root folder named USO (:23, :47-50). ROADMAP's copy is identical. BETA's matches 7lm 4ca3edb's, and the session branch's matches 7lm main's. No run on a combined tree is recorded (UNRESOLVED). The workflow carries your rule: "we cant enforce integroty by ebforceing no deletion. we can only imply no deletion to enforcer integiortyty".

    **Not settled.**
    - Whether IEEE 1788.1-2017 was read: one record says yes, two say no (X-18). The staged PDF is in HISTORY.
    - Whether BETA was made by Codex: its author is EDM, and it carries no generator trailer.

    ## The dependency on Autonomous

    Your rule of 5 September 2026 reads: "Auditonomous gets the definitions of autonomous from Autonomous and nowhere else." [source text withheld from the public copy] commit 0504961, dated 14 August 2026, Pacific time (MAIN:L7/peering/public/ingress/peer-1/object-1/0.md:13). The file is byte-identical on Autonomous main today, at a new path. BETA keeps the pin: "not a rebind".

    The rule is not yet the practice: "Three files at HEAD still take a definition of *autonomous* from somewhere other than this binding" (object-1/0.md:34). Only BETA says how each is to be handled, and RM counts a fourth (:586).

    What it supplies:
    - Eleven rows, A1 to A11. Its headline says "Six Tier-1 bodies"; its review counts 8 to 10. A10 defines "autonomic", not "autonomous".
    - Five usage rules, labelled "INTERNALLY DERIVED · COMPOSITE OBJECT UNVERIFIED".
    - An explicit refusal to pick one: "[source text withheld from the public copy]."

    What it does not supply:
    - **A consensus baseline.** The model requires one, and no ref holds one (EMPTY). "[source text withheld from the public copy]." stands only on the unmerged Autonomous beta.
    - **A reviewed entry.** Its review of 8 August 2026 "[source text withheld from the public copy] seven fixes. None has been made. There was one internal reviewer, and "External Sources Checked: NONE".
    - **A consistent register.** Its REGISTER.md lists "autonomy / autonomous" as not yet entered, against the entry's "ADOPTED".
    - **IEEE 1920.1, on which Q13 rests.** Only Auditonomous HISTORY holds a staged copy.
    - **A settled meaning of "auditability".** It is listed as "CONTESTED".
    - **A binding for AUTOMATION.md or REGISTER.md.**

    BETA's second binding pins commits that exist only on unmerged betas: 805cd42 in Autonomous and 4ca3edb in 7lm.

    ## The manuscript against the research

    No chapter has text. Each of the 27 chapter files, which exist only on ROADMAP, opens its text section with "*Not yet drafted.*", and the bibliography reads "No entry yet." Where RM marks a chapter "drafted", it means the Blocks, not chapter text.

    The chapter headers carry 141 feed citations. Between 63 and 66 of them resolve on MAIN, depending on how directories and one wildcard are counted. The vocabulary paper's claims table has one wrong row (16), one wrong line reference (3) and one overstated label (6), and the paper calls λ = 1 exact (:252).

    **Closest to usable.** Each still carries an open verification item.
    - Chapter 2: "Gates: none"; "registers complete".
    - Chapters 3 and 4, which also depend on D22.
    - Chapter 6.
    - Chapter 15: the lambda results, with their conditions.
    - Chapter 25, which also depends on D9.

    **Waiting on a ruling.**
    - Chapters 7 to 12: D3 to D6, D10, D13, D18 and D20.
    - Chapter 13: the counts and the contamination rule.
    - Chapter 14: D10.
    - Chapters 15 to 17: D7, D11, D14, D19, and the empty L2.
    - Chapters 19 to 24 and 26: D1, D8, D12 and D21. Every external number in them is unchecked.

    **Before the first drafting step.** RM's step is "then draft Chapter 2 and Chapter 19" (:603). It comes after eight moves and the review of the two papers, and none of these has a record:
    - PR #29 is unmerged.
    - No tag and no REVIEW_ record exist.
    - L2 is empty.
    - Moves 5 to 7 concern repositories not held here.

    BETA works on what moves 3 and 4 address, without citing RM.

    Chapter 2 needs three things:
    - a ruling on what it presents. RM calls the registers complete, BETA calls several comparisons contested, and the sourcebook withdrew its seed findings.
    - its seven quotations re-checked;
    - a merged branch to stand on.

    Chapter 19 needs four things:
    - rulings on D1 and D21 (named in its header) and on D8 (named in the table);
    - its verify items, all now "all NOT-CHECKED", checked;
    - its two feeds that are absent from MAIN;
    - a first-contact source in the ledger.

    **Against the model.** 7LM-MAIN's traversal gives L4 "production of the book artifact" and L5 "the book's research argument, interpretation, and teaching" (spec :611-613). The 7lm beta tip adds "## Manuscript work". Against that:
    - On ROADMAP, the corpus, chapters, sourcebook and prompts sit at L4 writing, and the roadmap and spine at L5.
    - The referee's criticism sits at L4, with nothing at L5.
    - The chapter headers copy RM.
    - No state carries the beta guidance.

    7LM-MAIN's "Not yet as stated" (:958) adds "The L0 epistemic rail is empty", and its :954 repeats "62 pointer rows". Whether the repositories agree with the model: UNRESOLVED.

    ## The first ten things to do

    1. **Owner.** Name the model commit. 7lm main c9dc061 lacks R1 to R6: 4ca3edb, which both betas pin, is not in main. Only the beta tip 97314c5 has the manuscript guidance. The model's own route is item-by-item HOA review at L7/peering/private/ (7LM-MAIN:L8/L6/7lm-field-guide.md §14). Your instruction of 11 November 2026 puts this first: "we need to uipdate the autonomous and auditonomous repos phsyciall; to match first". The pushed branch ccr-9391bd81-f2enmj mirrors the restructure on MAIN only.
    2. **Owner.** Decide whether ROADMAP and BETA join, in what order, and under which integrity workflow.
    3. **No ruling needed.** Prepare dated corrections now: 60 for 62 (also 7LM-MAIN :954), fifteen for sixteen, 71% for 76%, 21 for 22, and the stale prior-art labels. The rest waits for item 2.
    4. **Owner.** Rule which of the four texts is the definition, which version of AUDY, and the status of A to E.
    5. **Owner.** Rule on line 52 (D4), on senses 1 and 3, and on "immutable" or "apparent".
    6. **Owner.** On Autonomous: the baseline, the seven fixes, D22 and the register.
    7. **Network needed.** File the existing searches. Run the novelty search at publisher and standards hosts, then the entailment search.
    8. **No ruling needed.** Review the envelope adversarially, on the record. AUDY and the papers follow items 2, 4 and 6.
    9. **Owner, then session.** Supply the NASA journal or approve re-extraction, then reconcile 78 with 113.
    10. **Owner, then session.** Rule D11 and D14, and whether formal rows go to L2 or L3. Then prepare the rows.

    ## Decisions that are the owner's

    In order of how much each blocks:

    1. The model commit and the HOA route.
    2. ROADMAP and BETA.
    3. The definition among four texts, AUDY's version, A to E (D20).
    4. "Scholarly only", and D1.
    5. Line 52 (D4), senses 1 and 3, "immutable".
    6. Autonomous: baseline, fixes, pin (D22), register.
    7. The contamination rule.
    8. D11.
    9. L2 or L3; splits and registrations (D14).
    10. D10.
    11. The prohibited verb (D3); equivocation.
    12. Q13.
    13. Q9 (D5).
    14. The fourth derivation (D6).
    15. The named reader (D13).
    16. D18.
    17. D7.
    18. D9.
    19. D19.
    20. D8 and D21.
    21. The Autonomous Theory files and the Third Power Corpus (D12).
    22. D23.
    23. Your files in history.
    24. Purges and licences.
    25. The N/U paper.
    26. The adjective form.
    27. The default branch.
    28. The L0 epistemic rail.
    29. 7lm's rules file and layer lists.
    30. IEEE 7014's deletion requirement.
    31. Appendix C; BETA's dispositions.
    32. AU-NORM-04; the IEEE 754 copy.
    33. Binder placement; quotation clearance.
    34. "The refusal DISPOSES".
    35. The build-first order.
    36. Title and press (D2, D16).
  - **worklist**
    - item 1
      - **order**: 1
      - **action**: Name the model commit both repositories are to match. The candidates: 7lm main c9dc061 has the L7 restructure (in main since 20 September 2026), the L6 inbox with the layer lists, the sheet templates and the Auditonomous traversal, but not R1 to R6. 4ca3edb carries R1 to R6 and is pinned by both exemplar betas, but is not in main. The beta tip 97314c5 adds the manuscript guidance and lacks main's layer lists. Also say whether the update arrives by the model's own route: item-by-item HOA review at the adopter's L7/peering/private/ (7LM-MAIN:L8/L6/7lm-field-guide.md §14). No Auditonomous state binds 7lm there today.
      - **who**: owner
      - **why**: It is the first step in the owner's instruction of 11 November 2026, and every later change lands on that layout. The pushed session branch ccr-9391bd81-f2enmj (mirror commits f2d5b37 here and 8257118 in Autonomous; tips now 74b270e and a719cec) mirrors only the L7 restructure, on top of MAIN, and uses 7lm main's workflow. It carries none of the restore, BETA, R1 to R6 or the guidance. Three further unmerged 7lm heads retire the field guide that the beta edits in place.
      - **unblocks**: Every merge; O-01; M-20.
    - item 2
      - **order**: 2
      - **action**: Decide which of ROADMAP's restore (116 files; decision D15, 'TAKEN AS RULED') and BETA join the chosen state, in what order, and on which base (MAIN or the session branch). BETA brings the exemplar, the pinned binding, the 60-row and 21-row corrections, and the receiving-use dispositions. Also decide which .github/workflows/integrity.yml travels with them.
      - **who**: owner
      - **why**: Neither branch contains the other. MAIN cannot open what its own records cite: of 141 chapter feed citations, only 63 to 66 resolve there. MAIN's and ROADMAP's workflow still requires L7/governance/restrictions and L7/publications. BETA's workflow matches 7lm 4ca3edb, and the session branch's matches 7lm main. No run on a combined tree is recorded.
      - **unblocks**: M-01, M-02, M-05, M-18; all work on AUDY, the lambda thread, the docket and the corpus; items 8 and 10.
    - item 3
      - **order**: 3
      - **action**: Prepare dated corrections that keep the prior text. (1) 60 rows for 62, in MAIN's L7 sheets and at HIST/LEDGER_2026-08-16_l6-close-and-normalization.md:30, and the sheet's 'The ledger has no rows' (L7/provenance/sources/0.md:55). (2) The same 62 at 7LM-MAIN specification :954. (3) Fifteen for sixteen and 71% for 76% (SS/REQUIREMENTS_OWNERSHIP.md:117, :263-264). (4) 21 for 22 new rows (LEDGER.md:113). (5) 25 for 27 staging records (LEDGER.md:134). (6) The stale 'unrun' prior-art labels (MAIN:L7/provenance/prior-art/0.md:32, L7/provenance/0.md:36, FIND/DISTILLATION.md:134), citing the search record of 8 August 2026 (X-10, R-01, R-04).
      - **who**: work that can be done without the owner; the 7lm correction is for that repository's owner to enter
      - **why**: These are confirmed arithmetic and locator facts on MAIN and in 7lm main. Left as they are, they reach Chapter 13 in print and are copied into every later record.
      - **unblocks**: Chapters 2 and 13; an accurate prior-art position.
    - item 4
      - **order**: 4
      - **action**: Rule which text is the definition for the book, and how the texts relate where they overlap (X-01, D20). The candidates: the entry of 30 July 2026; AUDY v2 of 5 August 2026; the constitutional sentence (CONS:70, 'the primary definiens'); the fused form (CONS:80). Also rule which version of AUDY applies (O-02), and whether conditions A to E are definitional or 'anchor analysis'.
      - **who**: owner
      - **why**: Four texts define the word, two of them for different headwords, and none states which takes precedence. DEF:28 and AUDY:69 gloss the noun differently. Chapters 7 to 9 and 12, the L2 statements and the vocabulary paper all state the definition.
      - **unblocks**: D3, D4, D5 and D13 in context; M-10; Chapters 7 to 9 and 12; the A to E rows in item 11; the AUDY review in item 8.
    - item 5
      - **order**: 5
      - **action**: Rule the line-52 edit (D4), reading the cycles review beside it. Say whether sense 1 (DEF:22) and sense 3 (DEF:26) follow: they carry the same impossibility wording and have no proposed edit. Rule 'immutable' against 'apparent' (X-02, X-07).
      - **who**: owner
      - **why**: Three records bear on this sentence. The library intake found detection, never prevention, labelled CONTESTED. The adjudication found that the record, not the audit, is what is not post hoc. The cycles review disputes the adjudication's premise. This is the sentence a referee will test first.
      - **unblocks**: Chapters 7 and 8; the three unapplied nits (R-11) can ride on the same version.
    - item 6
      - **order**: 6
      - **action**: Settle the Autonomous side. (1) Say whether a consensus baseline is to be written or the plural entry stands (X-23). (2) Have REVIEW_4's seven fixes made by dated version (X-22). (3) Confirm or replace the pin at 0504961 (D22). (4) Correct Autonomous REGISTER.md:19, which lists 'autonomy / autonomous' as not yet entered. (5) Decide the extra rows and bindings (O-05). (6) Resolve the three files that still take 'autonomous' from elsewhere, plus the sourcebook's line 96.
      - **who**: owner
      - **why**: The second half of the word comes only from this object. Its [source text withheld from the public copy], and the model requires a baseline that no ref holds.
      - **unblocks**: Chapters 3 and 4; Q13 (X-08); O-03; the review of the baseline paper.
    - item 7
      - **order**: 7
      - **action**: First, file at L7/provenance/prior-art the searches already made: the scholarly-index and patent search of 2 August 2026 (REV/PERPETUITY_QUESTION_ADJUDICATION.md:91-100); the standards-index search of 5 August (ROADMAP:REV/WALK_ACROSS_repo-instrument-standards_2026-08-05.md:42); the 30-PDF sweep (HISTORY:FREEZE.md:17-28); and the record of 8 August, recoverable at Autonomous ab8f01f^:auditonomous/research/PRIOR_ART_SEARCH_2026-08-08.md. Then run the novelty search proper against publisher-of-record and standards hosts, which were blocked on 8 August, treating the 2018 blog and the domain registrations as leads only. Then run the entailment search queued on 16 August (U-02), starting from its named partial evidence and Autonomous's LANE_B_AUDITABILITY.md. Record each search with its indexes, queries, dates and a bounded finding. Capture the Cambridge and Oxford entries on the way (U-27).
      - **who**: work that can be done without the owner (needs network)
      - **why**: Lexical novelty is already refuted on the record. Whether the concept is new, and whether the word is needed, rest on searches that never reached the hosts that count.
      - **unblocks**: Chapters 5 and 7; AUDY's first falsification condition.
    - item 8
      - **order**: 8
      - **action**: Hold an adversarial review, on the record, of the envelope on MAIN now. Review AUDY after item 4. Review the two papers of 14 September 2026 after items 2 and 6: the vocabulary paper is on ROADMAP only, and the baseline paper is on Autonomous's closed PR #29 branch (U-05).
      - **who**: work that can be done without the owner
      - **why**: No L1 object has been reviewed, and the roadmap gates the first drafting step on the papers' review. Only the envelope can be reviewed on MAIN today.
      - **unblocks**: Chapter 12; roadmap step S0; the first drafting step.
    - item 9
      - **order**: 9
      - **action**: The owner supplies the workflow journal that holds the 14 NASA rows (REQUIREMENTS_OWNERSHIP.md:12-14 names a path on the owner's machine), or approves re-extraction from NASA sources, which would first need ledger rows. The session then: reconciles the 78-requirement run with the 113; finishes the auditability extraction beyond AC and AU; and assigns the 49 live AC controls left over (U-03, U-04, X-11). On the 78: its ISO, NIST and NASA tallies equal the 113's, so the gap appears to lie in IEEE, but no reconciliation is recorded.
      - **who**: owner, then a session
      - **why**: Today Chapter 13's numbers can be recounted for only 99 of the 113 requirements. The other 14 cannot be recovered without the owner.
      - **unblocks**: Chapter 13; a merged requirement count for the envelope.
    - item 10
      - **order**: 10
      - **action**: Prepare dated corrections to objects that stand on ROADMAP or BETA:
        - the vocabulary paper's claim 16 and RM's D20 text (:583, :630, :647), which deny the Aud(S,F) predicate that the sourcebook writes as \operatorname{Aud}(S,F);
        - the paper's rows 3 and 6 (X-25, R-14);
        - 'λ = 1 the exact interval-product radius' at paper :252, and the Autonomous finding at :33 (X-17);
        - BETA's line 52, now at line 54 (R-05);
        - BETA's L2 sheets, which say nothing is filed although AUDITONOMOUS_BETA_PREDICATE.md is filed;
        - the restore record's reason for leaving out the term ledger;
        - DISTILLATION.md:21, :38 and :262, which disagree with AUDY's reversal (X-13).
      - **who**: work that can be done without the owner, after item 2
      - **why**: Each object stands only on an unmerged branch, so each correction lands wherever item 2 puts that object.
      - **unblocks**: Clean citation of the definition and the vocabulary paper; Chapters 7 and 15.
    - item 11
      - **order**: 11
      - **action**: The owner rules D11 (the enclosure regime) and D14 (the file splits and the L2 registrations), and decides whether formal statements go to L2 or, as 7LM-MAIN's traversal places applied formulas, to L3 (spec :607-609). A session then prepares rows for the isomorphism, DR-003, the enclosure regime with its sign condition, and the Aud(S,F) form carrying the F-2 flag. The rows for conditions A to E wait for item 4. The owner enters all rows (M-10).
      - **who**: owner rules; a session prepares; the owner enters
      - **why**: No concept the definition relies on has a registered formal statement, and Part V is built on the formal layer. The one predicate on offer is flagged in the repository as contradicting FINDING_R157.
      - **unblocks**: Chapters 15 to 17; X-32.
    - item 12
      - **order**: 12
      - **action**: Say whether the contamination rule P1 to P3 (HISTORY:FREEZE.md:58-79) still binds. If it does, return it to a live position, then check two things against P2 and P3: Chapter 13's routing of requirements to compartments, and the vocabulary paper's use of IEEE 7009 and the NIST AU controls.
      - **who**: owner; the check can then be done without the owner
      - **why**: The rule bars citing a codified instrument as defining, supporting or requiring the coined term. It stands in no live tree. The restore record claims the sheets carry what the rule governed, and a search of the sheets does not bear that out.
      - **unblocks**: Chapter 13; the vocabulary paper; the composite labels on the envelope.
    - item 13
      - **order**: 13
      - **action**: Draft ledger rows for the definition's citations, SP 800-53, the works the findings cite, and the bound definition. Fill the 'Not held' table. [source text withheld from the public copy] the lawful copy (M-12, U-07). This needs the archive attached.
      - **who**: drafting can be done without the owner; the ledgering session is the owner's
      - **why**: By the ledger's own rule, each of these is an unledgered citation. The definition cites IEEE 7001's catalogue page, not row STD-004.
      - **unblocks**: Release rule 1; Chapters 3 and 4; Appendix A.
    - item 14
      - **order**: 14
      - **action**: Pin the unpinned bindings: eb-audit, and ebios with the Martin 2026 manuscript, naming which file is bound. Decide the Third Power Corpus (O-06, O-07).
      - **who**: owner
      - **why**: The sources under the definition have no version.
      - **unblocks**: U-24; release rule 1.
    - item 15
      - **order**: 15
      - **action**: Carry the external audit's corrections into the files they name (R-09). Fix the ISO 15489 gloss and the T3 count (X-37). Amend the cycles verdict (X-36). Draft replacement wording for the Git and kilogram sentences for the owner (X-28).
      - **who**: work that can be done without the owner; the owner for the corpus sentences
      - **why**: The audit of 4 August 2026 found these errors, and the files still carry them.
      - **unblocks**: Chapters 6, 8, 17, 20 and 24.
    - item 16
      - **order**: 16
      - **action**: Reconcile SOURCE_REQUESTS with what is now held. Read IEEE 1872-2015, IEEE 7010-2020 and IEEE 1788.1-2017 from the archive. Fetch Beer, Fisk and Rogers 2014. List what must be bought (U-13, M-19, R-10, X-18). Note that IEEE 1920.1 (19201-2022.pdf), 1788.1-2017 and 7009-2024 are staged in HISTORY:_STAGING_TO_L6/ and can be read with pdftotext under their hold-private terms, to check three things: the 1920.1 definition behind Q13, whether 1788.1 keeps decorations, and the wording of IEEE 7009 clause 1.3.2(e).
      - **who**: work that can be done without the owner (needs the archive, network, or the hold-private copies in history)
      - **why**: At least five requests are met or part-met and are still listed as open. Several checks thought impossible can be made from git objects.
      - **unblocks**: Row A5 and term T-02; X-18; Q13; Chapters 3, 15 and 16.
    - item 17
      - **order**: 17
      - **action**: Rule the definition-side decisions D3, D5, D6, D7, D9, D13, D18 and D19, the open questions in O-13, and Q13 (X-08). Say whether CONS §11's register of 23 contradictions stands as a live register or stays retired.
      - **who**: owner
      - **why**: Once the definition is fixed, these gate Part III, Chapter 12, Chapters 17 and 24, and Chapter 25. RM uses the retired register as a live feed.
      - **unblocks**: Chapters 8 to 12, 17, 24 and 25.
    - item 18
      - **order**: 18
      - **action**: The owner rules D10. A session then: runs the unrun arithmetic (U-10); files the missing scripts; recovers gen_drift.py; records the outcome of the lambda adversarial pass (U-18); drafts the λ_A operators (U-20); checks λ = 1 enclosure under floating-point rounding; and settles whether the quoted mul line is eb-stack's code.
      - **who**: owner, then work that can be done without the owner
      - **why**: Part V cannot state a regime or a mechanism before these are done. The λ = 1 result holds in exact arithmetic only, and the tested line is labelled UNVERIFIED.
      - **unblocks**: Chapters 14 to 16; X-14, X-16.
    - item 19
      - **order**: 19
      - **action**: Rule D1, with the ruling of 14 August 2026, 'scholarly only', in view (X-30). Then rule D8, D12 (including the home of '#autonomous(1).txt') and D21.
      - **who**: owner
      - **why**: These decide whether Part VI belongs in this book, and what Chapter 19 introduces.
      - **unblocks**: Chapters 19 to 24 and 26; U-15, U-16.
    - item 20
      - **order**: 20
      - **action**: On the chosen branch:
        - enumerate the prune of 15 August 2026 (M-18);
        - write a successor to the master ledger (R-02);
        - repair links with a path map (R-03);
        - return or re-home the objects that exist only in HISTORY: AUTONOMOUS_TERMS.md, TERM_LANES.md, FREEZE.md, manuscripts/definitions/REGISTER.md, intake/MANIFEST.md and the root AUTONOMOUS.md;
        - record the owner's decision on his own files in history (O-10).
      - **who**: work that can be done without the owner; the owner for O-10
      - **why**: The records should describe the tree that exists. The restore record's reason for leaving out the term ledger is contradicted, because no Autonomous ref holds it.
      - **unblocks**: Orientation; the L6 half of the manuscript guidance; Chapter 3's term rows.
    - item 21
      - **order**: 21
      - **action**: Settle the conditions on release:
        - the history purge of the third-party ISO file (O-08);
        - the history purge of the chat export in '#autonomous(1).txt', which carries an account identifier and third-party e-mail addresses;
        - the Ferreira licence, quotation clearance and an outbound licence (O-09).
        Then strip personal paths (R-16) and re-point the release checklist (R-03).
      - **who**: owner; the last two can be prepared without the owner
      - **why**: No item has been through the checklist, two of its boxes name paths that do not exist, and third-party personal data sits in every state's history.
      - **unblocks**: Any release of a paper or of the book.
    - item 22
      - **order**: 22
      - **action**: With network access, and after D1: re-fetch the census dossier, capture the official case documents and Chapter 19's four sources, and re-check Chapter 2's seven quotations (U-15, U-16, U-26).
      - **who**: work that can be done without the owner (needs network)
      - **why**: Every external number in Part VI is unchecked, and the roadmap placed this session after the chapter it gates.
      - **unblocks**: Chapters 2, 19, 20, 23 and 24.
    - item 23
      - **order**: 23
      - **action**: Run the interlock's attack pass and check IEC 61508 and ISO 13849 (U-06). Work the base-case question (Q-04).
      - **who**: work that can be done without the owner
      - **why**: The only method offered for enforcement by construction is an unbuilt proposal, and its likeliest failure is unanswered.
      - **unblocks**: Chapter 14; claim CR-31.
    - item 24
      - **order**: 24
      - **action**: Draft Chapter 2 and Chapter 19.
      - **who**: the writing, after items 4, 8, 19 and 22, and after the owner says whether the roadmap's build-first order still stands (O-20)
      - **why**: This is the roadmap's first drafting step. None of its preconditions has a record today. Chapter 2's header has no gates, but it still needs a ruling on what it presents and a merged branch to stand on.
      - **unblocks**: Roadmap step S6.
  - **owner_decisions**
    - 1. Name the model commit both repositories are to match: 7lm main c9dc061 (which lacks R1 to R6), 4ca3edb (which both betas pin) or the beta tip 97314c5 (which alone carries the manuscript guidance); and say whether updates arrive by the model's item-by-item HOA review at L7/peering/private/.
    - 2. Decide whether ROADMAP's restore and BETA join that state, in what order, on which base, and which integrity workflow travels with them.
    - 3. Rule which text is the definition for the book (the entry of 30 July 2026, AUDY v2, the constitutional sentence or the fused form), how they relate where they overlap (D20), which version of AUDY governs, and whether conditions A to E are definitional or 'anchor analysis'.
    - 4. Say whether your ruling of 14 August 2026, 'scholarly only', still stands; it settles D1 and whether Part VI belongs in this book.
    - 5. Rule whether line 52 is reworded (D4), whether senses 1 and 3 follow, and whether 'immutable' gives way to 'apparent'.
    - 6. On Autonomous, rule whether one consensus baseline is written or the plural entry stands, who makes REVIEW_4's seven fixes, whether the pin at 0504961 stays (D22), and how REGISTER.md and the files that take 'autonomous' from elsewhere are corrected.
    - 7. Say whether the freeze file's contamination rule P1 to P3 still binds and, if it does, where it returns in the live tree.
    - 8. Choose the enclosure regime the book uses (D11).
    - 9. Rule whether formal statements are registered at L2 or, when they are applied formulas, at L3 as 7lm main's traversal places them; and decide the three file splits and the L2 registrations (D14).
    - 10. Choose between trace-before-release and a pure one-way carrier (D10).
    - 11. Rule which verb is 'the one prohibited act' (D3), and [source text withheld from the public copy], as the library intake recommends.
    - 12. Rule what stands on Q13.
    - 13. Decide whether Q9 becomes the definitional dividing line (D5), and settle the definitions of observer and observed.
    - 14. Decide the fourth derivation (D6); the consolidated register records its independence claim as 'FAILED CHECK'.
    - 15. Decide whether the reviewer named by the engineering layer is an implementation convenience or constitutive (D13, the reader-agnostic divergence).
    - 16. Say whether the book prints eight compartments or twelve (D18).
    - 17. Rule between record-and-flag and non-formation for malformed states (D7).
    - 18. Decide whether reconstitution enters as a Part VII theme, enters as a stated objection in Chapter 25, or stays out (D9).
    - 19. Decide whether the change from Reactive to Responsive and the correction of the Block 51 mis-attribution are carried through the archive by dated correction (D19).
    - 20. Decide where the deep stratum and the evidence ranking go (D8), and which historical cases the book uses (D21).
    - 21. Name the home of the Autonomous Theory files, including '#autonomous(1).txt', and of the Third Power Corpus (D12).
    - 22. Rule whether the component repositories are harmonized, created anew or folded in (D23).
    - 23. Say whether your own files in history return: the five drafts deleted on 15 August 2026 and the working draft.
    - 24. Rule on the history purge of the third-party ISO file and of the chat export in '#autonomous(1).txt', on the Ferreira licence, on quotation clearance, and on an outbound licence.
    - 25. Say whether enclosure is the intended contract of the N/U algebra paper, and which version of the paper the defect ledger examined.
    - 26. Choose the adjective form, auditonomous or auditonomic, for which DEF:16 records 'no stated rule'.
    - 27. Decide the GitHub default branch, which DEF:408 says 'misrepresents the project'.
    - 28. Say whether the L0 epistemic rail takes the status vocabulary now held at L5, as 7lm main's 'Not yet as stated' notes.
    - 29. Rule on 7lm's own open calls: the held-off rules file on what a session or a model may touch, and whether the layer lists stay.
    - 30. Decide how the book treats IEEE 7014's deletion requirement against the constitutional sentence'[source text withheld from the public copy]'.
    - 31. Decide how DEF's Appendix C is handled, and whether BETA's receiving-use dispositions for the three files are adopted.
    - 32. Say whether AU-NORM-04 is superseded, and whether IEEE 754-2019, whose only byte-identical copy sits in l6's durable/delete/, is ledgered.
    - 33. Rule on placing held sources in the binder or keeping them internal, and on the conflict over IEEE quotation clearance.
    - 34. Say whether the finding 'the refusal DISPOSES, and enforcement is physical' (AUTONOMY_AT_DISTANCE B6) is adopted.
    - 35. Say whether the roadmap's build-first order still stands (O-20).
    - 36. Choose the title and the press (D2, D16).
  - **claims_register**
    - item 1
      - **id**: CR-01
      - **claim**: “auditonomous” (adj.) is the owner's coinage. The entry dates the word family to 2025-10-20 and the form itself to 2025-10-21, both in the abba-01/ebios repository.
      - **where_stated**: MAIN:DEF:18, 79, 85-178
      - **evidence_state**: INTERNALLY CHECKED by the entry's own record (DEF:353-356); not reproducible here, because ebios is in no clone. Absence of the word from five scholarly indexes is EXTERNALLY CHECKED as recorded (MAIN:REV/PERPETUITY_QUESTION_ADJUDICATION.md:89-100). Novelty is UNRESOLVED: no prior-art search has been run, and a 2018 blog titled AUDITONOMY stands as an unchecked lead.
      - **layer**: L0
      - **manuscript_use**: Chapter 7 (the coinage); front matter; vocabulary paper row 1.
      - **what_would_settle_it**: A pinned clone of abba-01/ebios to re-run the attestation; a recorded prior-art search with indexes, queries and dates; a registrar check on the blog and domain leads.
    - item 2
      - **id**: CR-02
      - **claim**: Sense 1 (of a system): it acts [source text withheld from the public copy]”.
      - **where_stated**: MAIN:DEF:22
      - **evidence_state**: ASSERTED as the author's definition. The strength of “unable to conceal” is CONTRADICTED by the repository's own adjudication (MAIN:REV/PERPETUITY_QUESTION_ADJUDICATION.md:216) and by the reading findings (detection, not prevention).
      - **layer**: L0
      - **manuscript_use**: Chapters 7 and 8; the book's central sentence.
      - **what_would_settle_it**: The owner's ruling on the line-52 edit, extended to lines 22 and 26; a formal non-concealment property at L2.
    - item 3
      - **id**: CR-03
      - **claim**: Sense 2 (a mode of human and AI working: the agent chooses its approach and keeps its reasoning shown) is the historically first sense. Sense 3 (accountability “secured by construction”) is a third sense built from one collocation.
      - **where_stated**: MAIN:DEF:24, 26, 30, 79, 117
      - **evidence_state**: Sense 2 ASSERTED; no later definition carries it forward. Sense 3 CONTRADICTED: one attestation is filed under two senses, and the entry's own labels paragraph counts two senses.
      - **layer**: L0
      - **manuscript_use**: Chapter 7; whether the book prints two senses or three.
      - **what_would_settle_it**: The owner's ruling on the number of senses and on which sense the book defines.
    - item 4
      - **id**: CR-04
      - **claim**: “[source text withheld from the public copy].
      - **where_stated**: ROADMAP:L8/L4/work/writing/manuscript/Auditonomous_Theory_Master_Archive.md:37; MAIN:DEF:28 (the noun's gloss, without the third clause)
      - **evidence_state**: ASSERTED. “a [source text withheld from the public copy], the embodied manuscript and the ebios draft (INTERNALLY CHECKED), and a ROADMAP record restates it as parameters “bound before dispatch and frozen, not absent” (ROADMAP:SS/AUDITABILITY_REQUIREMENTS.md:36-40). Which verb is “the one prohibited act” is UNRESOLVED (T3: six claimants).
      - **layer**: L0
      - **manuscript_use**: Chapter 8 (the constitution); front matter epigraph.
      - **what_would_settle_it**: Rulings D3 and D13; a decision whether the third clause stays as written.
    - item 5
      - **id**: CR-05
      - **claim**: Eight criteria define the word for a system: [source text withheld from the public copy] carried, never laundered; failure permitted, concealing it not; accountability by construction; autonomy bounded by a truth envelope; accountability measurable; discretion real.
      - **where_stated**: MAIN:DEF:36-43
      - **evidence_state**: ASSERTED. No test of any criterion against any system is recorded. None has a formal statement at L2 or a method at L3. “truth envelope” and “transformation path” are used and not defined.
      - **layer**: L0 (needs L2 and L3)
      - **manuscript_use**: Chapters 7 to 9; the test a reader would apply.
      - **what_would_settle_it**: An L2 statement for each criterion; a measure for “measurable accountability”; one worked test on a real system.
    - item 6
      - **id**: CR-06
      - **claim**: Auditability is “[source text withheld from the public copy]”, resting on the owner's instruction “it is meant to be firmware”.
      - **where_stated**: MAIN:DEF:22, 47
      - **evidence_state**: CONTRADICTED. The entry itself reports that no firmware artifact exists and that the corpus places eBIOS above the ROM (DEF:250); the instruction is recorded as “PLAUSIBLE”, not verified; AUDY and BETA carry no firmware requirement.
      - **layer**: L0
      - **manuscript_use**: Chapter 11 or 14 if kept; otherwise a stated intent.
      - **what_would_settle_it**: The owner's ruling whether firmware placement is definitional or intent; access to ebios branch v1.0.0-dev.
    - item 7
      - **id**: CR-07
      - **claim**: Auditonomous is “[source text withheld from the public copy]”.
      - **where_stated**: MAIN:DEF:52 (line 54 on BETA)
      - **evidence_state**: CONTRADICTED by MAIN:REV/PERPETUITY_QUESTION_ADJUDICATION.md:216 (“imprecise as written”); that adjudication is itself opposed by ROADMAP:REV/AUTONOMOUS_vs_AUDITONOMOUS_CYCLES.md:136. The recommended edit is UNRESOLVED and unapplied in every state.
      - **layer**: L0
      - **manuscript_use**: Chapters 7 and 8.
      - **what_would_settle_it**: The owner's ruling D4, taken with the cycles review in view.
    - item 8
      - **id**: CR-08
      - **claim**: The definition is “[source text withheld from the public copy]”.
      - **where_stated**: MAIN:DEF:57, 79; MAIN:REV/STATUS_AND_LABEL_DISCIPLINE.md:5-8
      - **evidence_state**: ASSERTED, and consistent in every state: experiments are EMPTY (MAIN:L8/L4/work/experiments/0.md:36) and BETA's result sets every achievement flag false.
      - **layer**: L0 / L4
      - **manuscript_use**: Chapter 1 (the reader's contract); the limit statement of every chapter.
      - **what_would_settle_it**: Nothing to settle. It lapses only when a system is built and tested.
    - item 9
      - **id**: CR-09
      - **claim**: “[source text withheld from the public copy].”
      - **where_stated**: ROADMAP:AUDY:69-70, 134-149 (absent from MAIN and BETA)
      - **evidence_state**: CONJECTURE by its own label (“CONJECTURE / INTERNAL ONLY”; “Composition not externally reviewed”). Its relation to DEF is UNRESOLVED. The restored bytes are those of Autonomous commit e27ca78; three later versions exist only in Autonomous history.
      - **layer**: L0
      - **manuscript_use**: Chapters 8 and 9; vocabulary paper row 5.
      - **what_would_settle_it**: The owner's ruling which text governs and which version; an adversarial review; the file on the merged state.
    - item 10
      - **id**: CR-10
      - **claim**: [source text withheld from the public copy] if and only if five conditions hold: A attested input, B enclosing bound (λ ≥ 1), C gate, D obligated record, E named reader. “[source text withheld from the public copy]”.
      - **where_stated**: ROADMAP:AUDY:§2-§5, 207-208; cited from MAIN:SS/AUDITON_ENVELOPE.md:253
      - **evidence_state**: CONJECTURE (“INTERNALLY DERIVED · CONJECTURE, not externally reviewed”). [source text withheld from the public copy] by the file's own statement; condition B's sources are “both unread” in the restored version; the four falsification conditions are untested.
      - **layer**: L0, to be stated at L2
      - **manuscript_use**: Chapter 9; the formal statements of Part V.
      - **what_would_settle_it**: The later version (9c123b0) restored or rejected; the conditions stated at L2; the falsification conditions run, starting with the prior-art search.
    - item 11
      - **id**: CR-11
      - **claim**: A received stop signal is not refusable; deviation from an ordinary instruction needs provenance, presence and a specific historical memory.
      - **where_stated**: ROADMAP:AUDY:42-61, 91-96 (owner, 2026-08-05: “NOt refusable”)
      - **evidence_state**: ASSERTED (the owner's ruling, inside a file labelled CONJECTURE). CONTRADICTED across states: MAIN:FIND/DISTILLATION.md:261-263 still quotes the reversed rule (“it may refuse or delay”), and the earlier conflict record (HISTORY:FREEZE.md:228-262) was never closed. Both objects read by the synthesizer.
      - **layer**: L0 / L1
      - **manuscript_use**: Chapters 9 and 11; the envelope's C6 row.
      - **what_would_settle_it**: AUDY on the merged state; a dated correction in the distillation; the IEEE 7009 R5/R6 classification of the stop and return functions.
    - item 12
      - **id**: CR-12
      - **claim**: The auditon is the maximal envelope: twelve compartments C1 to C12, four supplied by the platform and eight by the envelope. “[source text withheld from the public copy].” It [source text withheld from the public copy].”
      - **where_stated**: MAIN:SS/AUDITON_ENVELOPE.md:23-24, 51, 122-146
      - **evidence_state**: ASSERTED. Own label “COMPOSITE OBJECT UNVERIFIED. Not adversarially reviewed.” Four NIST control quotations INTERNALLY CHECKED against the held extraction. CONTRADICTED on the root of trust (C2) and threatened on the platform and envelope split by the ROADMAP replicator.
      - **layer**: L1
      - **manuscript_use**: Chapter 12.
      - **what_would_settle_it**: An adversarial review of the envelope; the owner's choice of C2 option; ruling D18.
    - item 13
      - **id**: CR-13
      - **claim**: “[source text withheld from the public copy].” Where a definition requires a [source text withheld from the public copy].”, and slots H1 to H7 may be substituted.
      - **where_stated**: MAIN:SS/AUDITON_ENVELOPE.md:102, 150-167; MAIN:SS/HUMINT_ENCODE.md:9-10, 76-84
      - **evidence_state**: ASSERTED. The files label their quotations “VERIFIED” with no locator to a held copy; one warrant ([source text withheld from the public copy]”; “Nothing in this document is adversarially reviewed.”
      - **layer**: L1
      - **manuscript_use**: Chapters 12 and 13.
      - **what_would_settle_it**: EU AI Act Art. 14 and ISO/IEC 17021-1 re-captured from publisher text; ISO/IEC 22989 re-read from the lawful copy; an adversarial review.
    - item 14
      - **id**: CR-14
      - **claim**: “[source text withheld from the public copy] buildable set is 21, not 113.”
      - **where_stated**: MAIN:SS/REQUIREMENTS_OWNERSHIP.md:47-54, 71-72
      - **evidence_state**: INTERNALLY CHECKED for the arithmetic and for 99 of the 113 rows (IEEE 55, ISO 24, NIST 20 recounted). The 14 NASA rows are in no file (UNRESOLVED). The assignment itself is ASSERTED (“INTERNALLY DERIVED”). “[source text withheld from the public copy]” is CONTRADICTED by the file's own table (fifteen, recounted by the synthesizer). The 113 excludes the auditability controls (Q11) and is unreconciled with an earlier run of 78.
      - **layer**: L1 (from L4 extractions)
      - **manuscript_use**: Chapter 13, whose title prints 113 and 21.
      - **what_would_settle_it**: The NASA rows recovered; 78 and 113 reconciled; the Q11 extraction finished; sixteen corrected to fifteen.
    - item 15
      - **id**: CR-15
      - **claim**: “[source text withheld from the public copy]”.
      - **where_stated**: MAIN:SS/REQUIREMENTS_OWNERSHIP.md:268-271
      - **evidence_state**: CONTRADICTED. ROADMAP:FIND/AUTONOMY_AT_DISTANCE.md:392-404 withdraws the “scores zero” claim; BETA records the headline as “not adopted as a present conformance finding” and “UNRESOLVED/CONTESTED”. IEEE 1920.1 is not among the bound Autonomous definitions.
      - **layer**: L1 / L5
      - **manuscript_use**: Chapters 3, 12 and 18.
      - **what_would_settle_it**: The owner's ruling on Q13; a decision whether IEEE 1920.1 enters the Autonomous entry; ISO's meaning of “oversight”.
    - item 16
      - **id**: CR-16
      - **claim**: A single auditon cannot be “autonomous” under ISO, IEEE, NASA and NIST at once: “NOT PACKABLE”, with nine irreducible conflicts.
      - **where_stated**: ROADMAP:FIND/AUDITON_PACKABILITY_2026-08-04.md:15-23 (absent from MAIN and BETA)
      - **evidence_state**: EXTERNALLY CHECKED in part (the standards sentences are locatable in held records). CONTRADICTED in part by the later autonomy-at-distance finding and softened by C5 (“CONTESTED”). The nine conflicts are not enumerated in the file.
      - **layer**: L5
      - **manuscript_use**: Chapters 4 and 12.
      - **what_would_settle_it**: An enumeration of the nine conflicts; a ruling which reading of “oversight” stands.
    - item 17
      - **id**: CR-17
      - **claim**: The λ = 1 product rule is Rump's midpoint-radius interval product (Rump 1999, BIT 39(3), Def. 2.1, Eq. 5) and always contains the true product.
      - **where_stated**: ROADMAP:REV/LAMBDA_EXTERNAL_VERIFICATION_2026-08-04.md:16-34
      - **evidence_state**: EXTERNALLY CHECKED. A reader confirmed the quoted equation and the isotonicity sentence against the Rump 1999 text held at AUT:L7/provenance/prior-art/prior-art-lane/ru99.txt:117, 121.
      - **layer**: L2 / L3
      - **manuscript_use**: Chapter 15: cite, do not coin.
      - **what_would_settle_it**: Settled for the mathematics. What remains is the choice of regime for the book (D11).
    - item 18
      - **id**: CR-18
      - **claim**: For operands that do not cross zero, the λ = 0 radius [source text withheld from the public copy], provided the centre is shifted by α·β.
      - **where_stated**: ROADMAP:REV/LAMBDA_EXTERNAL_VERIFICATION_2026-08-04.md:38-71 (owner's claim under test: “λ=[source text withheld from the public copy].”)
      - **evidence_state**: EXTERNALLY CHECKED against Rump 1999, proof case i (reader-confirmed at ru99.txt:165-172). The second confirmation, Rump 2010, is not held. The file's own adversarial pass “was still running” and has no recorded result.
      - **layer**: L2 / L3
      - **manuscript_use**: Chapters 15 and 16.
      - **what_would_settle_it**: A per-operation sign-definiteness check specified as a mechanism; the outcome of the adversarial pass recorded.
    - item 19
      - **id**: CR-19
      - **claim**: λ = 0 as coded in the quoted eb-stack multiplication, with the centre left at a·b, is not an enclosure.
      - **where_stated**: ROADMAP:REV/EBSTACK_LAMBDA_ANALYSIS.md:60-81; ROADMAP:L8/L4/work/computation/probes/ebstack_lambda_analysis.py
      - **evidence_state**: INTERNALLY CHECKED (exact-rational probe re-run on 11 November 2026; both worked examples redone by hand). The code line was taken from a prompt and has never been read in eb-stack (“UNVERIFIED”). The 9.49% containment figure is a property of the probe's integer grid.
      - **layer**: L4, feeding L2
      - **manuscript_use**: Chapters 15 and 16; decision D11.
      - **what_would_settle_it**: The eb-stack source read at a pinned commit.
    - item 20
      - **id**: CR-20
      - **claim**: λ_A = 0 names a decomposition state: the usable part of a known prior stays in operation and its unused remainder enters a provenance-preserving accumulator; nothing is pruned; q = k + r.
      - **where_stated**: ROADMAP:AUDY:361-447 (addendum marked “NOT ADOPTED”); MAIN:L7/peering/private/ingress/peer-2/object-1/auditonomous-departure-protocol.md:66-80; ROADMAP:REV/THESIS_lambda_decomposed_record.md:3-37
      - **evidence_state**: CONJECTURE. CONTRADICTED between two readings (thesis: “exactly known, zero uncertainty”; protocol: “It does not mean numerical zero, exactness”). Four operators are “named, none defined”; no bound on the accumulator is stated; a same-author ruling says λ_A = 0 must not be identified with λ_EB = 0.
      - **layer**: L0 / L2
      - **manuscript_use**: Chapter 16.
      - **what_would_settle_it**: The owner's ruling which reading governs; definitions of μ, τ, Coherent, Admissible and the update rule; a proof or disproof of a bound on the accumulator.
    - item 21
      - **id**: CR-21
      - **claim**: Whether a term changes any stored bit is decidable; pruning to loss does not compose over a chain; saving the remainder into a running total does.
      - **where_stated**: ROADMAP:REV/CONJECTURE_bit_exact_pruning.md:29-66, 158-245 (owner: “[source text withheld from the public copy]”)
      - **evidence_state**: INTERNALLY CHECKED as recorded (two runs, one against exact rationals); the scripts are not in the repository. The owner's own label is “CONJECTURE”. “λ is the fastest such criterion” is UNRESOLVED (“NOT TESTED”); the Kahan and Neumaier attributions are “UNVERIFIED”.
      - **layer**: L3 / L4
      - **manuscript_use**: Chapter 16.
      - **what_would_settle_it**: The scripts filed; Kahan 1965 and Neumaier 1974 obtained; an alternative criterion benchmarked.
    - item 22
      - **id**: CR-22
      - **claim**: Storage can be bounded by a “meaningful digit” budget.
      - **where_stated**: ROADMAP:REV/LAMBDA_EXTERNAL_VERIFICATION_2026-08-04.md:177-205
      - **evidence_state**: CONTRADICTED (“REFUTED”): catastrophic cancellation can destroy every significant digit in one subtraction (Goldberg 1991, as recorded; not held).
      - **layer**: L3
      - **manuscript_use**: Chapter 15: what not to claim.
      - **what_would_settle_it**: van Emden 2004, which the file names as the acquisition that would close it properly.
    - item 23
      - **id**: CR-23
      - **claim**: Making an exact decomposition with an enclosed residual the mandatory content of a pre-execution record is new: “no occupant of it was located”.
      - **where_stated**: ROADMAP:REV/THESIS_lambda_decomposed_record.md:85, 131-133
      - **evidence_state**: UNRESOLVED. Own label “PARTIALLY CHECKED — negative”. A deep-research run filed on MAIN as model output says the broad record-before-act claim [source text withheld from the public copy]”; its citations cannot be resolved from the repository.
      - **layer**: L5
      - **manuscript_use**: Chapters 6 and 16 (“the narrow novelty claimed deliberately”).
      - **what_would_settle_it**: A recorded prior-art search at the intersection; Dekker 1971 and Ogita, Rump and Oishi 2005 obtained; the ISO/IEC 24970 and prEN 18229-1 collision check.
    - item 24
      - **id**: CR-24
      - **claim**: Codified definitions of autonomy are privative (defined by an absence); the auditonomous layer is constructive (defined by obligations). Six candidate laws L1 to L6 follow.
      - **where_stated**: MAIN:FIND/DISTILLATION.md:3-5, 14-23, 84-101
      - **evidence_state**: CONJECTURE by its own label (“INTERNALLY DERIVED · CONJECTURE throughout”). L5 is CONTRADICTED in part by the replicator's accepted refutation (ROADMAP only). The legal and economics quotations of its section 7 appear nowhere else in the repository.
      - **layer**: L5
      - **manuscript_use**: Chapters 5, 18 and 25.
      - **what_would_settle_it**: The search for a constructive codified autonomy definition (it would refute L1); ledger rows and records for the section 7 sources; L5 restated or struck.
    - item 25
      - **id**: CR-25
      - **claim**: “Permit the breach, make it undeniable” is an established, codified pattern; audit and override cannot be one recursive loop; the achievable property is tamper-evidence, not immutability.
      - **where_stated**: MAIN:FIND/OVERRIDE_NECESSITY_2026-08-04.md:21-31, 319-320
      - **evidence_state**: EXTERNALLY CHECKED in part (RFC 6962, Haber and Stornetta, FIPS 180-4 and the AC-3(10) and AU-10 control statements are verbatim in held records). Proposition P-D CONTRADICTED by the finding's own refutation pass. The bootstrapping objection is UNRESOLVED. Nine cited authors have no record in the repository.
      - **layer**: L5
      - **manuscript_use**: Chapters 9, 11 and 14.
      - **what_would_settle_it**: Ledger rows for the uncited sources; the owner's ruling on “immutable” against “apparent”; an answer to the bootstrapping objection.
    - item 26
      - **id**: CR-26
      - **claim**: Physical segregation with a one-way carrier is codified but cannot prevent omission, and it collides with the rule that the trace commit precedes actuator release (EB:233). Forgetting as non-recall is supported and not novel.
      - **where_stated**: MAIN:FIND/SEGREGATION_AND_FORGETTING_2026-08-04.md:59, 83-90, 183-193
      - **evidence_state**: EXTERNALLY CHECKED in part (ARIES and IEEE 7014 quotations verbatim in the reading records). UNRESOLVED: “[source text withheld from the public copy].” The interlock proposal that answers it is unbuilt.
      - **layer**: L5 (L3 for the interlock)
      - **manuscript_use**: Chapters 9 and 14.
      - **what_would_settle_it**: Ruling D10; the interlock's attack pass; NIST SP 800-88 ledgered for the crypto-erase route.
    - item 27
      - **id**: CR-27
      - **claim**: Hash-chained and logged structures give detection, not prevention, and tamper-evidence needs a second party.
      - **where_stated**: MAIN:STG/library/FINDINGS_2026-08-04.md:12-36, 57-70
      - **evidence_state**: EXTERNALLY CHECKED (quotes compared with the primary PDFs under the reading protocol on 4 August 2026; 13 load-bearing quotes independently re-checked, as recorded). The PDFs are in the archive and could not be reopened here.
      - **layer**: L7 reading, feeding L5
      - **manuscript_use**: Chapters 6, 8 and 14; it bounds what the definition may claim.
      - **what_would_settle_it**: Settled as a reading result. Its consequence for DEF lines 22, 26 and 52 is the owner's.
    - item 28
      - **id**: CR-28
      - **claim**: No theorem says an autonomous system must end; “an auditonomous system can be perpetual” cannot be verified as posed; [source text withheld from the public copy]**”.
      - **where_stated**: MAIN:REV/PERPETUITY_QUESTION_ADJUDICATION.md:25-100, 123-154, 226-252
      - **evidence_state**: First leg EXTERNALLY CHECKED as recorded (“FAILED CHECK”). Second leg UNRESOLVED (“UNVERIFIABLE AS POSED”). The ratchet reading is CONJECTURE. [source text withheld from the public copy] a ruling whose verbatim wording was not found.
      - **layer**: L5
      - **manuscript_use**: Chapter 25.
      - **what_would_settle_it**: Publisher-of-record captures for the relayed quotes; the bounded-commitment claim checked against the logging literature.
    - item 29
      - **id**: CR-29
      - **claim**: Published standards contradict one another, and themselves, on “autonomous” (C1 to C7).
      - **where_stated**: MAIN:REV/CONTRADICTIONS.md:32-200
      - **evidence_state**: EXTERNALLY CHECKED for the quotations as the repository records them (C1, C2 and C4 matched to the extractions by a reader). None is resolved. C2's conclusion is CONTRADICTED by its own source entry; C4's “Heteronomous” classification is listed as unverified in the bound Autonomous entry; BETA calls the comparisons local and contested.
      - **layer**: L5
      - **manuscript_use**: Chapter 2 (method) and Chapter 3.
      - **what_would_settle_it**: The seven publisher re-checks; the IEEE 7009 clause 1.3.2(e) wording from the PDF; ISO/IEC 22989 Table 1 from the lawful copy.
    - item 30
      - **id**: CR-30
      - **claim**: “Autonomous” does not entail auditability: none of the eleven codified definitions contains record, audit, log, trace or account.
      - **where_stated**: Autonomous branch claude/scholarly-pair-baseline-k8ap82:L8/L4/work/writing/papers/AUTONOMOUS_BASELINE_PAPER_2026-09-14.md:118-122; ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:306
      - **evidence_state**: The eleven-text finding is INTERNALLY CHECKED (a reader re-ran the string search over rows A1 to A11). The general claim is CONJECTURE. The bounded search queued on 16 August 2026 is UNRESOLVED: it was never run.
      - **layer**: L5
      - **manuscript_use**: Chapter 5: the reason the word is needed.
      - **what_would_settle_it**: The queued search over the declared authority set at a pinned commit, with a clause-level reading and adversarial verification.
    - item 31
      - **id**: CR-31
      - **claim**: Moving the actuator enable to the sealed side makes unrecorded actuation inexpressible. The predicate asks whether an action is recorded, not whether it is permitted, and the proposal claims no prior formulation of it.
      - **where_stated**: MAIN:L8/L3/engineering-mathematics/PROPOSAL_seal_gated_interlock.md:6-8, 45-46, 93-127
      - **evidence_state**: UNRESOLVED (a proposal; nothing built; attack-pass result found in no state; IEC 61508 and ISO 13849 “NOT-CHECKED”). The novelty claim is ASSERTED with no recorded search. Its own limit: “[source text withheld from the public copy].”
      - **layer**: L3
      - **manuscript_use**: Chapter 14.
      - **what_would_settle_it**: The attack pass run and folded in; a recorded novelty search; the predicate stated at L2; something built.
    - item 32
      - **id**: CR-32
      - **claim**: For the 16 ordered two-step cases of a fixed-goal fixture, permit equals not-stop, every stopped event halts, the goal never changes, and each event has one digest-chained record.
      - **where_stated**: BETA:L8/L2/formal-mathematics/relations/AUDITONOMOUS_BETA_PREDICATE.md:3-7; BETA:FIND/AUDITONOMOUS_BETA_FINDINGS.md:7-11
      - **evidence_state**: INTERNALLY CHECKED (12 tests re-run and passed on 11 November 2026; result reproduced except the recorded Python version; pinned hashes recomputed). Synthetic by its own statement: “[source text withheld from the public copy].”
      - **layer**: L2 / L4
      - **manuscript_use**: At most a worked illustration. It supports no claim about the definition.
      - **what_would_settle_it**: Nothing further for the fixture. It does not bear on any defining criterion.
    - item 33
      - **id**: CR-33
      - **claim**: “Auditonomous gets the definitions of autonomous from Autonomous and nowhere else.” The source is one plural entry of eleven codified definitions, bound at commit 0504961.
      - **where_stated**: MAIN:L7/peering/public/ingress/peer-1/0.md:10; MAIN:L7/peering/public/ingress/peer-1/object-1/0.md:13; AUT:L8/L0/semantics/definitions/AUTONOMOUS.md:24-25, 70-80
      - **evidence_state**: INTERNALLY CHECKED for the binding (commit exists; blob ffbdc28 and SHA-256 2756…a12b identical at 0504961 and on Autonomous main). The consensus baseline the model asks for is EMPTY. The entry's own status is CONTRADICTED (banner “NOT ADVERSARIALLY REVIEWED”, status “ADOPTED”, register “Not yet entered”, review “BLOCKS”). Three files on MAIN still take “autonomous” from elsewhere.
      - **layer**: L7 / L0
      - **manuscript_use**: Chapters 3 and 4; Appendix A; vocabulary paper section 2.
      - **what_would_settle_it**: The owner's rulings on the baseline, the seven fixes and D22; a new binding record beside the old one if the pin moves.
    - item 34
      - **id**: CR-34
      - **claim**: Codified autonomy is defined against a human: “[source text withheld from the public copy].”
      - **where_stated**: AUT:L8/L5/research/findings/FINDING_autonomy_requires_a_human_referent.md:27-28; repeated at MAIN:FIND/DISTILLATION.md:14-15 and in vocabulary paper row 12
      - **evidence_state**: INTERNALLY CHECKED as a count over held text, but the ten rows counted are not A1 to A11 (two are not A-rows; A3, A9 and A10 are omitted). The inference drawn from it is ASSERTED; prior art for the argument was “Not searched”.
      - **layer**: L5 (Autonomous)
      - **manuscript_use**: Chapters 4 and 13 (HUMINT-ENCODE).
      - **what_would_settle_it**: A recount over the eleven rows; a prior-art search for the argument.
  - **open_register**
    - item 1
      - **id**: X-01
      - **kind**: contradiction
      - **statement**: Two texts claim to be the definition. DEF is “the active definition of record (AU-NORM-02)”. AUDY's header says “v2 definition governs”. MAIN's distillation calls AUDY “governing text” though MAIN does not hold it. No document states how they relate.
      - **source**: MAIN:README.md:11; ROADMAP:AUDY:3-5; MAIN:FIND/DISTILLATION.md:21
      - **who**: owner
      - **blocks**: Chapters 7 to 9 and 12; every L2 statement; the vocabulary paper.
    - item 2
      - **id**: X-02
      - **kind**: contradiction
      - **statement**: DEF says a system is “structurally unable to conceal” and that “auditonomy makes concealment impossible from the start”. The adjudication calls line 52 “imprecise as written” on three external quotes. The cycles review holds the opposite on whether audit is post hoc. The edit is recorded and unapplied in every state.
      - **source**: MAIN:DEF:22, 26, 52; MAIN:REV/PERPETUITY_QUESTION_ADJUDICATION.md:201-222; ROADMAP:REV/AUTONOMOUS_vs_AUDITONOMOUS_CYCLES.md:136
      - **who**: owner (decision D4)
      - **blocks**: Chapters 7 and 8.
    - item 3
      - **id**: X-03
      - **kind**: contradiction
      - **statement**: The entry lists three senses; its labels paragraph and both appendix lists speak of two; one attestation is filed under sense 3 and under the system sense.
      - **source**: MAIN:DEF:26, 79, 117
      - **who**: owner
      - **blocks**: Chapter 7.
    - item 4
      - **id**: X-04
      - **kind**: contradiction
      - **statement**: The etymology says “Blend of AUDIT + AUTONOMOUS.”; Appendix A says “a blend of AUTONOMOUS + AUDITABLE”, twice. The boundary note that was to resolve it was never written.
      - **source**: MAIN:DEF:18, 96, 181; MAIN:HIST/LEDGER_2026-08-16_l6-close-and-normalization.md:50
      - **who**: owner
      - **blocks**: Chapter 7 (etymology).
    - item 5
      - **id**: X-05
      - **kind**: contradiction
      - **statement**: Firmware: the definition places auditability at firmware level; the corpus it quotes puts eBIOS above the ROM (“Firmware-below and brain-above coexist unreconciled.”). No firmware artifact exists. AUDY and BETA carry no firmware requirement.
      - **source**: MAIN:DEF:47, 250, 404
      - **who**: owner; needs access to ebios
      - **blocks**: Chapters 11 and 14.
    - item 6
      - **id**: X-06
      - **kind**: contradiction
      - **statement**: Appendix C says the exact form is “unattested in the searched corpus”; the entry and Appendix A document 24 attestations of it. The two parts searched different corpora and the lines stand unqualified.
      - **source**: MAIN:DEF:18, 85-178, 280, 339
      - **who**: work that can be done without the owner (a dated qualifying note for the owner's merge)
      - **blocks**: Chapter 7.
    - item 7
      - **id**: X-07
      - **kind**: contradiction
      - **statement**: The override finding lists as not safe to claim “That anything is immutable”; the distillation and AUDY still define by an immutable record.
      - **source**: MAIN:FIND/OVERRIDE_NECESSITY_2026-08-04.md:319-320; MAIN:FIND/DISTILLATION.md:21-23; ROADMAP:AUDY:63, 69-70
      - **who**: owner
      - **blocks**: Chapters 8 and 9.
    - item 8
      - **id**: X-08
      - **kind**: contradiction
      - **statement**: Q13 has three positions. MAIN: [source text withheld from the public copy]”. ROADMAP: the “scores zero” claim “is withdrawn”. BETA: “not adopted as a present conformance finding”, “UNRESOLVED/CONTESTED”. Q13's own text is unstruck everywhere.
      - **source**: MAIN:SS/REQUIREMENTS_OWNERSHIP.md:268-271; ROADMAP:FIND/AUTONOMY_AT_DISTANCE.md:392-404; BETA:SS/REQUIREMENTS_OWNERSHIP.md:268
      - **who**: owner
      - **blocks**: Chapters 3, 12 and 18.
    - item 9
      - **id**: X-09
      - **kind**: contradiction
      - **statement**: The packability finding (4 August 2026) reads telemetry and remote logs as oversight and calls the NIST and ISO goal conflict irreducible. The autonomy-at-distance finding (5 August 2026) rejects that reading. C5 calls the same pair “Narrower than fatal”. Neither finding is marked superseded.
      - **source**: ROADMAP:FIND/AUDITON_PACKABILITY_2026-08-04.md:37, 59-63; ROADMAP:FIND/AUTONOMY_AT_DISTANCE.md:140-144; MAIN:REV/CONTRADICTIONS.md:130-134
      - **who**: owner
      - **blocks**: Chapters 4, 12 and 18.
    - item 10
      - **id**: X-10
      - **kind**: contradiction
      - **statement**: “[source text withheld from the public copy]” (76%) against the same file's “7001 (6) and 7009 (15)” and its 15-row table (71%). The wrong figure is repeated in five other documents. BETA does not correct it.
      - **source**: MAIN:SS/REQUIREMENTS_OWNERSHIP.md:71-72, 88-110, 117, 263-264; ROADMAP:L7/provenance/sources/STANDARDS_REGISTER.md:344, 492, 495; ROADMAP:REV/SPINE_v0.1_2026-08-14.md:138
      - **who**: work that can be done without the owner (dated corrections)
      - **blocks**: Chapter 13.
    - item 11
      - **id**: X-11
      - **kind**: contradiction
      - **statement**: The status of Q11 differs by state. MAIN: the auditability requirements were never extracted, “blocking”. ROADMAP's Part B: “[source text withheld from the public copy].”, while the restored standards register still marks it blocking. BETA: “Q11 extraction remains open.”
      - **source**: MAIN:SS/REQUIREMENTS_OWNERSHIP.md:259-261; ROADMAP:SS/AUDITABILITY_REQUIREMENTS.md:236-237; ROADMAP:L7/provenance/sources/STANDARDS_REGISTER.md:347-351; BETA:SS/REQUIREMENTS_OWNERSHIP.md:268
      - **who**: work that can be done without the owner, after the merge decision
      - **blocks**: Chapter 13.
    - item 12
      - **id**: X-12
      - **kind**: contradiction
      - **statement**: Root of trust (C2). The envelope says it “is an INTERFACE” to the base and that no PUF source is held. The replicator, the same day, says “[source text withheld from the public copy]”, gives two codified options and says PUFs are sourced in SR-4(3). The envelope was not amended.
      - **source**: MAIN:SS/AUDITON_ENVELOPE.md:224-236, 257; ROADMAP:SS/AUDITON_REPLICATOR.md:123-125, 530-547, 599
      - **who**: owner (which option)
      - **blocks**: Chapter 12.
    - item 13
      - **id**: X-13
      - **kind**: contradiction
      - **statement**: Stop rule. AUDY records the owner's reversal of 5 August 2026, “NOt refusable”, restoring the envelope's “non-overridable stop path”. MAIN's distillation still quotes the reversed wording, “it may refuse or delay”. The earlier conflict record is history-only and was never closed. BETA's “no stop latch” is related to neither.
      - **source**: ROADMAP:AUDY:42-46, 91-92; MAIN:FIND/DISTILLATION.md:261-263; HISTORY:FREEZE.md:228-262; BETA:SS/AUDITONOMOUS_BETA_ADMISSION.md:3
      - **who**: work that can be done without the owner (a dated correction), once AUDY is on the merged state
      - **blocks**: Chapters 9 and 11.
    - item 14
      - **id**: X-14
      - **kind**: contradiction
      - **statement**: λ_A = 0 has two readings. Thesis decode: “λ = 0: exactly known, zero uncertainty”. Departure protocol: “[source text withheld from the public copy]”. The roadmap's label for this tension, CH-01, has no record of its own.
      - **source**: ROADMAP:REV/THESIS_lambda_decomposed_record.md:10-11; MAIN:L7/peering/private/ingress/peer-2/object-1/auditonomous-departure-protocol.md:76; ROADMAP:RM:257
      - **who**: owner
      - **blocks**: Chapter 16.
    - item 15
      - **id**: X-15
      - **kind**: contradiction
      - **statement**: Candidate law L5 cites the replicator run as showing that drift is caught by a preserved reference in the sealed ledger. The replicator's accepted review says the re-anchored check is “Per-unit, memoryless, no ledger required”. The distillation was not updated.
      - **source**: MAIN:FIND/DISTILLATION.md:84-91; ROADMAP:SS/AUDITON_REPLICATOR.md:274-279, 314-318
      - **who**: work that can be done without the owner (a dated narrowing for the owner's merge)
      - **blocks**: Chapters 5 and 25.
    - item 16
      - **id**: X-16
      - **kind**: contradiction
      - **statement**: Trace-before-release (EB:233) against a pure one-way carrier: “[source text withheld from the public copy]”. The interlock proposal offers a third arrangement and is unbuilt.
      - **source**: MAIN:FIND/SEGREGATION_AND_FORGETTING_2026-08-04.md:83-90; MAIN:L8/L3/engineering-mathematics/PROPOSAL_seal_gated_interlock.md:36-46
      - **who**: owner (decision D10)
      - **blocks**: Chapters 9 and 14.
    - item 17
      - **id**: X-17
      - **kind**: contradiction
      - **statement**: The companion finding labels λ = 1 “the **exact** interval product radius”. The outside check says λ = 1 is the midpoint-radius product, which overestimates, and that the exact radius for sign-definite operands is the λ = 0 form at a shifted centre.
      - **source**: AUT:L8/L5/research/findings/FINDING_lambda_enclosure_boundary.md:31-34; ROADMAP:REV/LAMBDA_EXTERNAL_VERIFICATION_2026-08-04.md:50-56
      - **who**: work that can be done without the owner (a dated correction in Autonomous)
      - **blocks**: Chapter 15.
    - item 18
      - **id**: X-18
      - **kind**: contradiction
      - **statement**: IEEE 1788.1-2017: the session log says it was read and the question closed (“Q6 CLOSED.”); the standards register says “HELD but UNREAD.” and the roadmap “IEEE 1788.1 NOT READ”.
      - **source**: ROADMAP:L8/L4/work/writing/sessions/SESSION_2026-08-05_VERIFICATION_LOG.md:16; ROADMAP:L7/provenance/sources/STANDARDS_REGISTER.md:130, 367; ROADMAP:RM:248
      - **who**: work that can be done without the owner (needs the archive copy)
      - **blocks**: Chapter 15.
    - item 19
      - **id**: X-19
      - **kind**: contradiction
      - **statement**: IEEE 7001 clause 5.2.2 on recorder independence is tagged “(NORMATIVE)” in the override finding and in the staging findings, and “MIXED” in the reading record, which says the phrase qualifies an external device, not the system's own recorder.
      - **source**: MAIN:FIND/OVERRIDE_NECESSITY_2026-08-04.md:187-188; MAIN:STG/ieee/reading/IEEE-7001.md:115-119; MAIN:STG/ieee/FINDINGS_2026-08-04.md:103-107
      - **who**: work that can be done without the owner
      - **blocks**: Chapters 9 and 14.
    - item 20
      - **id**: X-20
      - **kind**: contradiction
      - **statement**: CONTRADICTIONS.md overstates in three places: C2 drops the condition its source states (an external authorizer); C4's heading says “identical” where its body says “Near-identical”, and its “Heteronomous” classification is an outstanding attack line in the bound entry; the IEEE 7009 clause 1.3.2(e) quotation is singular where the extraction is plural.
      - **source**: MAIN:REV/CONTRADICTIONS.md:60-63, 94-101, 198-199; MAIN:L8/L4/work/computation/ieee-requirements-for-autonomouos.md:857, 874, 993; AUT:L8/L0/semantics/definitions/AUTONOMOUS.md:16-17
      - **who**: work that can be done without the owner (needs the PDFs)
      - **blocks**: Chapters 2 and 3.
    - item 21
      - **id**: X-21
      - **kind**: contradiction
      - **statement**: The bound Autonomous entry carries four statuses: banner “NOT ADVERSARIALLY REVIEWED”, status line “ADOPTED”, register “Not yet entered”, and a review of 8 August 2026 that “[source text withheld from the public copy]”.
      - **source**: AUT:L8/L0/semantics/definitions/AUTONOMOUS.md:3, 24; AUT:L8/L0/semantics/definitions/REGISTER.md:19; AUT:L8/L5/research/review/REVIEW_4_AUTONOMOUS_ADJUDICATION.md:451
      - **who**: owner
      - **blocks**: Chapters 3 and 4.
    - item 22
      - **id**: X-22
      - **kind**: contradiction
      - **statement**: Defects that travel with the bound bytes: row A3 carries two labels; “the ten above” and “A1…A10” over eleven rows; “Six Tier-1 bodies” over nine; rule 2's falsification condition met and the rule unamended; rule 3 refuted [source text withheld from the public copy]. No corrected version exists on any ref.
      - **source**: AUT:L8/L0/semantics/definitions/AUTONOMOUS.md:39, 72, 244-246, 273-294; AUT:L8/L5/research/review/REVIEW_4_AUTONOMOUS_ADJUDICATION.md:42-43
      - **who**: owner (the seven fixes, by dated version)
      - **blocks**: Chapter 3; Appendix A.
    - item 23
      - **id**: X-23
      - **kind**: contradiction
      - **statement**: The model's specification has Auditonomous consume “the pinned Autonomous consensus baseline”. The bound entry says “[source text withheld from the public copy]”. The Autonomous beta says “[source text withheld from the public copy].” DEF predates the binding and is a delta over nothing.
      - **source**: MAIN:L8/L0/0.md:79; AUT:L8/L0/semantics/definitions/AUTONOMOUS.md:25; Autonomous beta:L8/L5/research/review/BETA_SOURCE_OVERLAY.md:11
      - **who**: owner
      - **blocks**: The “local delta” framing; Chapters 3 and 7.
    - item 24
      - **id**: X-24
      - **kind**: contradiction
      - **statement**: For Chapter 2 the roadmap calls the registers complete and the chapter “VERIFIED (components)”. BETA calls the same comparisons local, contested or unresolved and re-verifies nothing. The sourcebook's method section withdraws its own seed findings.
      - **source**: ROADMAP:RM:97-113; BETA:REV/CONTRADICTIONS.md:22-35; ROADMAP:L8/L4/work/writing/sourcebook/Auditonomous_Book_Material_Sourcebook_v0.1.md:1291-1317
      - **who**: owner
      - **blocks**: Chapter 2.
    - item 25
      - **id**: X-25
      - **kind**: contradiction
      - **statement**: The vocabulary paper's row 16, the roadmap's rewording of D20, and two readers of this pass state that no predicate Aud(S,F) occurs in the sourcebook. It does, in LaTeX, at line 116. A literal search for “Aud(” misses it.
      - **source**: ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:305; ROADMAP:RM:630, 647; ROADMAP:L8/L4/work/writing/sourcebook/Auditonomous_Book_Material_Sourcebook_v0.1.md:113-124
      - **who**: work that can be done without the owner (corrected in the open, the wrong version kept visible)
      - **blocks**: Decision D20 as worded; Chapters 7 and 12.
    - item 26
      - **id**: X-26
      - **kind**: contradiction
      - **statement**: Deletion rule. The status ladder says “Nothing is ever deleted.” The retired sheet says “No-deletion is not a rule enforced here”. The owner's words of 7 September 2026: “we cant enforce integroty by ebforceing no deletion. we can only imply no deletion to enforcer integiortyty”.
      - **source**: MAIN:REV/STATUS_LADDER.md:25; MAIN:L8/L6/retired/0.md:12; MAIN:HIST/harmonization-2026-09-05.md:152-154
      - **who**: owner
      - **blocks**: How corrections and retirements are recorded.
    - item 27
      - **id**: X-27
      - **kind**: contradiction
      - **statement**: The owner's claim “TO be autonomus it oto be forgetful.” is recorded in the docket as “UNSUPPORTED and contradicted”; a MAIN finding says the layering resolution is “now PARTIALLY VERIFIED”; the lane file still says “PENDING — lane running”.
      - **source**: MAIN:LANES/RECORD_ONTOLOGY_OPEN_QUESTIONS.md:127-140; ROADMAP:REV/RESEARCH_DOCKET.md:190; MAIN:FIND/SEGREGATION_AND_FORGETTING_2026-08-04.md:142
      - **who**: work that can be done without the owner to carry the outcomes into the lane file; the claim itself is the owner's
      - **blocks**: Chapter 9.
    - item 28
      - **id**: X-28
      - **kind**: contradiction
      - **statement**: Two corpus sentences are contradicted by primary sources: that [source text withheld from the public copy]” (Git gives detection, not prevention), and that the 2019 SI redefinition deleted the kilogram artifact (it was demoted and is conserved). Both stand in the manuscript corpus.
      - **source**: ROADMAP:REV/EXTERNAL_AUDIT_2026-08-04.md:46-88; ROADMAP:L8/L4/work/writing/manuscript/Auditonomous_Theory_Master_Archive.md:546, 619
      - **who**: owner (author text)
      - **blocks**: Chapters 10 and 17; Appendix G.
    - item 29
      - **id**: X-29
      - **kind**: contradiction
      - **statement**: The fourth derivation (Block 46) is the author's own instrument counted as an independent arrival: “[source text withheld from the public copy].”
      - **source**: ROADMAP:REV/RESEARCH_DOCKET.md:153; ROADMAP:RM:617
      - **who**: owner (decision D6)
      - **blocks**: Chapters 10 and 17.
    - item 30
      - **id**: X-30
      - **kind**: contradiction
      - **statement**: Owner ruling of 14 August 2026: “[source text withheld from the public copy]”. It survives only in history. The roadmap treats the same question (D1) as open, plans six first-contact chapters and never cites the ruling.
      - **source**: HISTORY:HUB_LEDGER.md:49-50; ROADMAP:RM:612
      - **who**: owner
      - **blocks**: Chapters 19 to 24 and 26.
    - item 31
      - **id**: X-31
      - **kind**: contradiction
      - **statement**: The owner's N/U algebra paper: its product rule omits the u1·u2 term, so the result has the right width at the wrong centre and does not contain the true product, while its section 9 claims coverage. Worked: (2,1) ⊗ (7,2) = [3,25] against a true [5,27].
      - **source**: ROADMAP:REV/NASA_PAPER_DEFECT_LEDGER.md:70-177
      - **who**: owner (is enclosure the intended contract)
      - **blocks**: Chapters 15 and 16.
    - item 32
      - **id**: X-32
      - **kind**: contradiction
      - **statement**: Two eBIOS documents give different formulas for composed uncertainty; one reduces to 1 for every input (“FORMULA INCONSISTENCY DETECTED”). It is unregistered at L2, and which formula is canonical is unruled.
      - **source**: MAIN:DEF:257; ROADMAP:REV/RESEARCH_DOCKET.md:66-68
      - **who**: owner
      - **blocks**: The criterion that uncertainty is carried; Chapter 15.
    - item 33
      - **id**: X-33
      - **kind**: contradiction
      - **statement**: Inside AUDY: “[source text withheld from the public copy]” stands beside rules for a received stop signal; the kernel is “the audit layer alone” and later the stop path rejoins it; bare λ means the enclosure parameter in sections 1 and 2 and the decomposition state in the addendum.
      - **source**: ROADMAP:AUDY:31-32, 44-45, 74, 91-94, 186, 202, 379
      - **who**: owner (a dated version)
      - **blocks**: Chapters 9 and 16.
    - item 34
      - **id**: X-34
      - **kind**: contradiction
      - **statement**: “8 of 10” definitions reference a human, but the ten rows counted are not A1 to A11. AUDY and MAIN's distillation say “ten” codified definitions; the binding sheet and the table say eleven.
      - **source**: AUT:L8/L5/research/findings/FINDING_autonomy_requires_a_human_referent.md:16-28; ROADMAP:AUDY:234-235; MAIN:FIND/DISTILLATION.md:14-15; MAIN:L7/peering/public/ingress/peer-1/object-1/0.md:28
      - **who**: work that can be done without the owner (a recount); the entry's wording is the owner's
      - **blocks**: Chapters 4 and 13.
    - item 35
      - **id**: X-35
      - **kind**: contradiction
      - **statement**: Inside the auditability record: AU-10 against AC-24(2), “Unresolved. Not repaired here.”; and AU-6 is classed as not carriable by any object while the envelope's C11 and slot H7 rest on AU-6.
      - **source**: ROADMAP:SS/AUDITABILITY_REQUIREMENTS.md:143-145, 206-228
      - **who**: work that can be done without the owner (analysis); the owner adopts
      - **blocks**: Chapters 12 and 13.
    - item 36
      - **id**: X-36
      - **kind**: contradiction
      - **statement**: The cycles review's external verdict says continuous audit is established “since 1991” and legally mandated under NIST and the EU AI Act. Later source requests record that the date is contestable, that the 1991 paper says “less-after-the fact”, and that NIST's framework is voluntary. The roadmap cites the verdict as verified.
      - **source**: ROADMAP:REV/AUTONOMOUS_vs_AUDITONOMOUS_CYCLES.md:136; ROADMAP:REV/SOURCE_REQUESTS.md:180-181; ROADMAP:RM:152
      - **who**: work that can be done without the owner
      - **blocks**: Chapter 6.
    - item 37
      - **id**: X-37
      - **kind**: contradiction
      - **statement**: T3: the ledger states as fixed that the definite article appears twice; the archive has six claimants across all three verbs. The gloss that ISO 15489-1:2001 is the one instrument holding all three is refuted: the clause contains neither “falsify” nor “erase”.
      - **source**: MAIN:LANES/THEME_LEDGER.md:156-160; ROADMAP:L8/L4/work/writing/manuscript/Auditonomous_Theory_Master_Archive.md:47, 90, 210, 232, 580, 593; ROADMAP:REV/EXTERNAL_AUDIT_2026-08-04.md:175-188
      - **who**: work that can be done without the owner (the count and the gloss); the ruling is D3
      - **blocks**: Chapter 8.
    - item 38
      - **id**: D1
      - **kind**: owner decision
      - **statement**: One academic book with the scenario narrative in a companion volume, or the narrative kept as case files, or two books. The ruling of 14 August 2026 (X-30) bears on it and is not weighed. Whether the Tic Tac adjudication and the census count as contact material is part of the same call.
      - **source**: ROADMAP:RM:612; HISTORY:HUB_LEDGER.md:49-50
      - **who**: owner
      - **blocks**: Chapters 19 to 24 and 26; Appendix I.
    - item 39
      - **id**: D2
      - **kind**: owner decision
      - **statement**: Title: three candidates stand, in date order.
      - **source**: ROADMAP:RM:613
      - **who**: owner
      - **blocks**: Front matter; the press proposal.
    - item 40
      - **id**: D3
      - **kind**: owner decision
      - **statement**: [source text withheld from the public copy]): four unranked readings; six claimants in the archive. Status in the lane file: “[source text withheld from the public copy].”
      - **source**: ROADMAP:RM:614; MAIN:LANES/THEME_LEDGER.md:156-272
      - **who**: owner
      - **blocks**: Chapter 8.
    - item 41
      - **id**: D4
      - **kind**: owner decision
      - **statement**: Whether line 52 of the definition is reworded to contrast record-by-design with record-bolted-on-later. Lines 22 and 26 carry the same wording and are outside the recorded edit.
      - **source**: ROADMAP:RM:615; MAIN:REV/PERPETUITY_QUESTION_ADJUDICATION.md:222
      - **who**: owner
      - **blocks**: Chapters 7 and 8.
    - item 42
      - **id**: D5
      - **kind**: owner decision
      - **statement**: Whether Q9 (“autonomous ASSUMES state, auditonomous CHECKS state”) becomes the definition's dividing line.
      - **source**: ROADMAP:RM:616; MAIN:LANES/RECORD_ONTOLOGY_OPEN_QUESTIONS.md:227-242
      - **who**: owner
      - **blocks**: Chapter 9.
    - item 43
      - **id**: D6
      - **kind**: owner decision
      - **statement**: How the fourth derivation is handled (see X-29).
      - **source**: ROADMAP:RM:617
      - **who**: owner
      - **blocks**: Chapters 10 and 17.
    - item 44
      - **id**: D7
      - **kind**: owner decision
      - **statement**: Record-and-flag (Block 46) against non-formation as correct behaviour (Block 50).
      - **source**: ROADMAP:RM:618; ROADMAP:REV/RESEARCH_DOCKET.md:162
      - **who**: owner
      - **blocks**: Chapters 17 and 24.
    - item 45
      - **id**: D8
      - **kind**: owner decision
      - **statement**: Where the evidence ranking goes after the cut of Block 36, and where the deep stratum (Blocks 33 and 34) goes. Two surviving blocks still cite the ranking as settled method.
      - **source**: ROADMAP:RM:619; MAIN:LANES/THEME_LEDGER.md:146-152
      - **who**: owner
      - **blocks**: Chapters 1 and 19.
    - item 46
      - **id**: D9
      - **kind**: owner decision
      - **statement**: Where the reconstitution counter-thesis (Blocks 37 and 38) goes; by its own text it “[source text withheld from the public copy]”.
      - **source**: ROADMAP:RM:620; MAIN:LANES/THEME_LEDGER.md:105-114, 154
      - **who**: owner
      - **blocks**: Chapter 25.
    - item 47
      - **id**: D10
      - **kind**: owner decision
      - **statement**: Trace-before-release or a pure one-way carrier (X-16); and whether the recall policy must itself be sealed.
      - **source**: ROADMAP:RM:621; MAIN:FIND/SEGREGATION_AND_FORGETTING_2026-08-04.md:183-193
      - **who**: owner
      - **blocks**: Chapters 9 and 14.
    - item 48
      - **id**: D11
      - **kind**: owner decision
      - **statement**: Enclosure regime for the book: λ = 1 throughout; λ = 0 with the sign-definiteness predicate carried; or both stated. The envelope already prints “λ=1 linear form” for compartment C3.
      - **source**: ROADMAP:RM:622; MAIN:SS/AUDITON_ENVELOPE.md:126
      - **who**: owner
      - **blocks**: Chapters 15 and 16; the L2 rows.
    - item 49
      - **id**: D12
      - **kind**: owner decision
      - **statement**: Whether the Autonomous Theory files are a source for Part VI, and where that separate work lives.
      - **source**: ROADMAP:RM:623; MAIN:HIST/harmonization-2026-09-05.md:113
      - **who**: owner
      - **blocks**: Chapters 20 and 22.
    - item 50
      - **id**: D13
      - **kind**: owner decision
      - **statement**: [source text withheld from the public copy]; AUDY names a reader. Design property or omission.
      - **source**: ROADMAP:RM:624; MAIN:REV/0.md:44
      - **who**: owner
      - **blocks**: Chapters 8 and 18.
    - item 51
      - **id**: D14
      - **kind**: owner decision
      - **statement**: Split or cite three mixed L1 files (the envelope, HUMINT_ENCODE, REQUIREMENTS_OWNERSHIP), and register the candidate objects at L2 and L3. The two restored L1 files have no split record at all.
      - **source**: ROADMAP:RM:625; MAIN:HIST/harmonization-2026-09-05.md:91-92
      - **who**: owner
      - **blocks**: Chapters 12, 13 and 15.
    - item 52
      - **id**: D15
      - **kind**: owner decision
      - **statement**: Restore from history. Taken as ruled by inference from the instruction “Them setup the Auditonomous repo before research.” The pull request that carried it was closed unmerged on 17 October 2026, and BETA was built without it.
      - **source**: ROADMAP:RM:626; ROADMAP:HIST/restore-2026-09-14.md:9
      - **who**: owner
      - **blocks**: Whether the 116 restored files reach the merged state.
    - item 53
      - **id**: D16
      - **kind**: owner decision
      - **statement**: Press and series.
      - **source**: ROADMAP:RM:627
      - **who**: owner
      - **blocks**: Length, register, and whether the papers precede the proposal.
    - item 54
      - **id**: D18
      - **kind**: owner decision
      - **statement**: Eight or twelve compartments in print. Both counts are arithmetically right (12 = 4 + 8).
      - **source**: ROADMAP:RM:628; MAIN:SS/AUDITON_ENVELOPE.md:137-144
      - **who**: owner
      - **blocks**: Chapter 12.
    - item 55
      - **id**: D19
      - **kind**: owner decision
      - **statement**: Propagate “Responsive” for “Reactive” into Blocks 43 and 44, and correct the Block 51 attribution.
      - **source**: ROADMAP:RM:629; ROADMAP:REV/RESEARCH_DOCKET.md:158
      - **who**: owner rules; the propagation needs no further ruling
      - **blocks**: Chapters 17 and 24.
    - item 56
      - **id**: D20
      - **kind**: owner decision
      - **statement**: Which framing of auditonomy governs: the five-axis auditon profile, the standards-indexed profile with its Aud(S,F) predicate, or a reconciled new definition. The decision's text misdescribes the sourcebook (X-25).
      - **source**: ROADMAP:RM:630
      - **who**: owner
      - **blocks**: Chapters 7 and 12.
    - item 57
      - **id**: D21
      - **kind**: owner decision
      - **statement**: The prospectus's four case laboratories or the table of contents' three case files.
      - **source**: ROADMAP:RM:633
      - **who**: owner
      - **blocks**: Chapters 19, 23 and 24.
    - item 58
      - **id**: D22
      - **kind**: owner decision
      - **statement**: Bind the definition of autonomous to Autonomous main c9076c3, to a tag exemplar-2026-09-14 (never created), or keep 0504961. BETA keeps 0504961 and writes “no rebind”; it does not name D22.
      - **source**: ROADMAP:RM:631; BETA:L7/provenance/sources/LEDGER.md:153
      - **who**: owner
      - **blocks**: Chapters 3 and 4.
    - item 59
      - **id**: D23
      - **kind**: owner decision
      - **statement**: Component repositories: harmonize each, create clean new ones, or fold them in. Fifteen were surveyed from roots and READMEs only.
      - **source**: ROADMAP:RM:632, 649-671
      - **who**: owner
      - **blocks**: Chapters 6, 9 and 14 to 17.
    - item 60
      - **id**: O-01
      - **kind**: owner decision
      - **statement**: Which model commit the two repositories match: 7lm main c9dc061 (11 November 2026), the 4ca3edb both betas pin, or the beta tip 97314c5 with the manuscript guidance. The 7lm beta is not an ancestor of 7lm main. Then: whether ROADMAP and BETA are merged onto the session branch of 11 November 2026, and in what order.
      - **source**: 7lm refs origin/main and origin/beta/common-contracts-r1-r6 (merge-base 2e5a6d6); BETA:L7/peering/public/ingress/peer-1/object-2/binding.json; local branch ccr-9391bd81-f2enmj (f2d5b37, 149ab6c; Autonomous 8257118)
      - **who**: owner
      - **blocks**: Every physical change to either repository.
    - item 61
      - **id**: O-02
      - **kind**: owner decision
      - **statement**: Which version of AUDY the owner means: the bytes restored on ROADMAP (Autonomous commit e27ca78, 462 lines) or the last version in Autonomous history (9c123b0, 475 lines), which adds two-tier stop enforcement and records condition B as grounded.
      - **source**: ROADMAP:AUDY:202, 272; ROADMAP:HIST/LEDGER_2026-08-14_reorganisation.md:21
      - **who**: owner
      - **blocks**: Chapter 9; condition B.
    - item 62
      - **id**: O-03
      - **kind**: owner decision
      - **statement**: The owner rule on “autonomous”: Appendix C of the definition, Q13, the autonomy rows of CONTRADICTIONS.md and the sourcebook's line 96 take the word from outside the binding. MAIN reserves the edit to the owner; BETA applied dispositions with no recorded ruling.
      - **source**: MAIN:L8/L0/semantics/definitions/0.md:34; MAIN:L7/peering/public/ingress/peer-1/object-1/0.md:34; BETA:REV/CONTRADICTIONS.md:22-35
      - **who**: owner
      - **blocks**: Chapter 3; roadmap step S3.
    - item 63
      - **id**: O-04
      - **kind**: owner decision
      - **statement**: Findings the reading records reserve: IEEE 7014 requires deletion of affective data, against “cannot erase”; [source text withheld from the public copy]; whether the reader is constitutive.
      - **source**: MAIN:STG/ieee/FINDINGS_2026-08-04.md:18-69; MAIN:STG/library/FINDINGS_2026-08-04.md:92-108
      - **who**: owner
      - **blocks**: Chapter 8.
    - item 64
      - **id**: O-05
      - **kind**: owner decision
      - **statement**: Whether IEEE 1920.1, IEEE 7007, ISO/IEC 25059 and the second ALFUS volume enter the Autonomous entry as rows or stop being used as definitions here; whether AUTOMATION.md and REGISTER.md are bound.
      - **source**: MAIN:REV/CONTRADICTIONS.md:52-58, 76, 147, 171; MAIN:L7/peering/public/ingress/peer-1/0.md:20-22
      - **who**: owner
      - **blocks**: Q13; rows C2, C3, C6 and C7.
    - item 65
      - **id**: O-06
      - **kind**: owner decision
      - **statement**: The Third Power Corpus v3: “[source text withheld from the public copy]?”
      - **source**: MAIN:L7/peering/private/egress/peer-2/object-1/OWNERSHIP_PENDING.md:12-13
      - **who**: owner
      - **blocks**: Nothing in the book; a pending transfer.
    - item 66
      - **id**: O-07
      - **kind**: owner decision
      - **statement**: Unpinned bindings: no commit for eb-audit; no commit for ebios and no hash for the Martin 2026 manuscript; which of its Markdown and PDF is the bound version.
      - **source**: MAIN:L7/peering/private/ingress/peer-2/object-1/0.md:13; MAIN:L7/peering/private/ingress/peer-3/object-1/0.md:13
      - **who**: owner (a ledgering act)
      - **blocks**: Release rule 1; Chapter 7.
    - item 67
      - **id**: O-08
      - **kind**: owner decision
      - **statement**: The history purge of the third-party ISO/IEC 22989 file (“pending owner execution”); the blob is still reachable in this clone. A rescue branch is recorded as holding pre-redaction personal data.
      - **source**: MAIN:STG/standards/SOURCE_LEDGER.md:418-434; MAIN:HIST/LEDGER_2026-08-16_l6-close-and-normalization.md:40
      - **who**: owner
      - **blocks**: Any change of visibility.
    - item 68
      - **id**: O-09
      - **kind**: owner decision
      - **statement**: Licence status of the Ferreira full text; how much quotation from IEEE standards a published work may carry; an outbound licence, copyright notice and patent position for the repository's own work.
      - **source**: MAIN:L7/governance/copyright/0.md:41-55; MAIN:L7/governance/patents/0.md:31
      - **who**: owner
      - **blocks**: Any release.
    - item 69
      - **id**: O-10
      - **kind**: owner decision
      - **statement**: The owner's own files in history only: five Office drafts deleted on 15 August 2026 with “principal's call on their home” open (three are the first files of 30 and 31 July 2026), the working draft auditonomous.odt, and the Deep Research Pro Prompt.
      - **source**: MAIN:HIST/LEDGER.md:32; ROADMAP:HIST/restore-2026-09-14.md:33, 191-195; manuscript status report of 3 November 2026
      - **who**: owner
      - **blocks**: Retention of the manuscript's own history.
    - item 70
      - **id**: O-11
      - **kind**: owner decision
      - **statement**: Twelve small placement calls left open between 5 and 7 September 2026: the ledger's position, binder/internal, the formulas ledger at L2 or L3, the datasets ledger's name, the eb-audit copy, peer granularity for standards bodies, three review-or-findings placements, the discipline text's home, the retired set's reading, CLAUDE.md.
      - **source**: MAIN:HIST/harmonization-2026-09-05.md:89-95, 107, 152; MAIN:HIST/7LM_ROUTING_PLAN_2026-09-05.md:157, 169, 172
      - **who**: owner
      - **blocks**: Layout only.
    - item 71
      - **id**: O-12
      - **kind**: owner decision
      - **statement**: Whether ruling AU-NORM-04 (“Definitions remain under manuscripts/definitions/”) is superseded. It exists only in a commit message and was overridden by the move of 5 September 2026.
      - **source**: MAIN:HIST/LEDGER_2026-08-16_l6-close-and-normalization.md:1; commit 4a1c1db
      - **who**: owner
      - **blocks**: The record of rulings.
    - item 72
      - **id**: O-13
      - **kind**: owner decision
      - **statement**: Record-ontology questions Q1 to Q9 (twelve with Q6a to Q6c), all “OPEN”; above all the separate definitions of observer and observed that the owner ruled on in kind (“[source text withheld from the public copy].”) and that are not written.
      - **source**: MAIN:LANES/RECORD_ONTOLOGY_OPEN_QUESTIONS.md:4, 35-72
      - **who**: owner
      - **blocks**: Chapter 9.
    - item 73
      - **id**: O-14
      - **kind**: owner decision
      - **statement**: Author assertions awaiting a decision: the narrowing in A-002; the three-step cycle of A-002b; the three-part test of A-003; when engineered non-recoverability is privacy and not concealment (A-008); the propulsion proposal A-009c.
      - **source**: ROADMAP:REV/AUTHOR_ASSERTIONS.md:68-113, 117-244, 248-317, 395-756, 1020-1136
      - **who**: owner
      - **blocks**: Chapters 9 and 11.
    - item 74
      - **id**: O-15
      - **kind**: owner decision
      - **statement**: Docket items marked for the owner and not covered above: P1 (what the symmetry of physicality ranges over); A1 (whether absorbing u = ∞ is right for an audit trail); F4; G1. DR-001 asks whether to [source text withheld from the public copy].”
      - **source**: ROADMAP:REV/RESEARCH_DOCKET.md:38-50, 56-64, 160, 172; ROADMAP:REV/dr-001-003/DR-001-uha-half-cell-decode.md:55
      - **who**: owner
      - **blocks**: Chapters 15 and 17.
    - item 75
      - **id**: O-16
      - **kind**: owner decision
      - **statement**: The envelope's map: whether the replicator's direction attribute (C2-in, C2-out) enters it; whether removing C8 makes C8 an envelope concern (“[source text withheld from the public copy]”); whether five more separation controls are cited.
      - **source**: ROADMAP:SS/AUDITON_REPLICATOR.md:87, 436-449; ROADMAP:SS/AUDITABILITY_REQUIREMENTS.md:238
      - **who**: owner
      - **blocks**: Chapter 12.
    - item 76
      - **id**: O-17
      - **kind**: owner decision
      - **statement**: The ebios core-architecture draft is, by its own statement, not canonical until the owner approves it. Three chapters feed from it.
      - **source**: MAIN:LANES/THEME_LEDGER.md:128-138; ROADMAP:L8/L4/work/writing/auditonomous_ebios_core_architecture_math_source-535f70d_draft.md
      - **who**: owner
      - **blocks**: Chapters 6, 14 and 15.
    - item 77
      - **id**: O-18
      - **kind**: owner decision
      - **statement**: Corpus housekeeping: which document governs the four cut blocks (the table of contents says cut; the archive still maps them to chapters); whether the fragment at Block_37:18 is intended.
      - **source**: MAIN:LANES/THEME_LEDGER.md:146-152, 284; ROADMAP:L8/L4/work/writing/manuscript/Auditonomous_Theory_Master_Archive.md:723-728, 748
      - **who**: owner
      - **blocks**: Chapters 1 and 25.
    - item 78
      - **id**: O-19
      - **kind**: owner decision
      - **statement**: Whether the consolidated document of 4 August 2026, history-only by AU-NORM-02, may stand in the tree as a retired object and feed seven chapters.
      - **source**: ROADMAP:HIST/restore-2026-09-14.md:74; ROADMAP:L8/L6/retired/consolidated-2026-08-04/0.md:8
      - **who**: owner
      - **blocks**: Chapters 1, 2, 7, 8, 11 and 18.
    - item 79
      - **id**: O-20
      - **kind**: owner decision
      - **statement**: Whether the roadmap's full build-first order (nine moves, including eight repository passes) still stands before Chapters 2 and 19, neither of which lists those moves in its own gate.
      - **source**: ROADMAP:RM:595-604
      - **who**: owner
      - **blocks**: The first drafting step.
    - item 80
      - **id**: U-01
      - **kind**: unrun check
      - **statement**: Prior-art search for the coinage and the definition: “**No prior-art search has been run.**” The prior-art position holds rules only. Scoped checks exist elsewhere (four analogy lanes; lambda cosmology) and are not recorded at the position.
      - **source**: ROADMAP:AUDY:262-263; MAIN:L7/provenance/prior-art/0.md:32; MAIN:FIND/DISTILLATION.md:134
      - **who**: work that can be done without the owner (needs network)
      - **blocks**: Chapter 7; every novelty claim.
    - item 81
      - **id**: U-02
      - **kind**: unrun check
      - **statement**: The auditability-gap search queued on 16 August 2026: does any codified definition of autonomous, merely by classifying a system autonomous, entail recoverable state and history. No record of a run exists in any state.
      - **source**: MAIN:HIST/LEDGER_2026-08-16_l6-close-and-normalization.md:48
      - **who**: work that can be done without the owner (needs network and a pinned Autonomous commit)
      - **blocks**: Chapter 5.
    - item 82
      - **id**: U-03
      - **kind**: unrun check
      - **statement**: The auditability extraction (Q11) was run only for SP 800-53 AC and AU, on ROADMAP. It was not run [source text withheld from the public copy], IEC, CCSDS, IETF, COSPAR, or SC-7(13), SC-32 and SI-10(1). About 49 live AC controls have no recorded disposition.
      - **source**: MAIN:SS/REQUIREMENTS_OWNERSHIP.md:259-261; ROADMAP:SS/AUDITABILITY_REQUIREMENTS.md:166, 172-177, 236
      - **who**: work that can be done without the owner
      - **blocks**: Chapter 13.
    - item 83
      - **id**: U-04
      - **kind**: unrun check
      - **statement**: 78 requirements (one run) against 113 (another run) of 4 August 2026: “unreconciled”. The 14 NASA rows are listed in no file in any state, so 113 cannot be recounted from the tree.
      - **source**: MAIN:SS/REQUIREMENTS_OWNERSHIP.md:15-21, 244; ROADMAP:FIND/AUDITON_PACKABILITY_2026-08-04.md:15
      - **who**: work that can be done without the owner (needs the workflow journal, or a fresh NASA extraction)
      - **blocks**: Chapter 13.
    - item 84
      - **id**: U-05
      - **kind**: unrun check
      - **statement**: No adversarial review is recorded for the envelope, HUMINT_ENCODE, AUDY, the composition as a whole, any finding, or the two papers of 14 September 2026.
      - **source**: MAIN:SS/AUDITON_ENVELOPE.md:24; MAIN:SS/HUMINT_ENCODE.md:149; ROADMAP:RM:583
      - **who**: work that can be done without the owner
      - **blocks**: Chapter 12; the first drafting step.
    - item 85
      - **id**: U-06
      - **kind**: unrun check
      - **statement**: The interlock's [source text withheld from the public copy]”; no result exists in any state. IEC 61508 and ISO 13849 are “NOT-CHECKED”. Its trust regress is open: “[source text withheld from the public copy]”.
      - **source**: MAIN:L8/L3/engineering-mathematics/PROPOSAL_seal_gated_interlock.md:6-8, 166-178
      - **who**: work that can be done without the owner
      - **blocks**: Chapter 14.
    - item 86
      - **id**: U-07
      - **kind**: unrun check
      - **statement**: The ISO/IEC 22989 captures and terms.json were taken from a withdrawn third-party copy; re-verification against the lawful copy STD-025 is open. [source text withheld from the public copy] also barred from reproduction at length.
      - **source**: MAIN:L7/governance/copyright/0.md:44; MAIN:STG/standards/extracted/ISO-IEC-22989-2022_captures.md:6-7; AUT:L8/L0/semantics/definitions/AUTONOMOUS.md:228-234
      - **who**: work that can be done without the owner (needs the archive)
      - **blocks**: Chapters 3, 4 and 13.
    - item 87
      - **id**: U-08
      - **kind**: unrun check
      - **statement**: The perpetuity adjudication's three next checks: publisher-of-record captures; the relayed quotes (Dyson, the NIST handbook, the PNAS pair) against publisher PDFs; the bounded-commitment claim against the logging literature. None is recorded as done.
      - **source**: MAIN:REV/PERPETUITY_QUESTION_ADJUDICATION.md:315-327, 348
      - **who**: work that can be done without the owner (needs network)
      - **blocks**: Chapter 25.
    - item 88
      - **id**: U-09
      - **kind**: unrun check
      - **statement**: T3 sources: no citator run on Bronston or Chiarella; Tiersma (1990) not obtained; ISO 15489-1:2016 clause 5.2.2.1 unread.
      - **source**: MAIN:LANES/THEME_LEDGER.md:189; ROADMAP:REV/SOURCE_REQUESTS.md:51-69, 158-159
      - **who**: work that can be done without the owner
      - **blocks**: Chapter 8.
    - item 89
      - **id**: U-10
      - **kind**: unrun check
      - **statement**: Does u = ∞ survive composition (docket A1), and the propagation table for every operation (A2): “INTERNALLY DERIVED, UNRUN”. No probe exists.
      - **source**: ROADMAP:REV/RESEARCH_DOCKET.md:56-64
      - **who**: work that can be done without the owner
      - **blocks**: Chapter 15.
    - item 90
      - **id**: U-11
      - **kind**: unrun check
      - **statement**: The IEEE 7009 R5/R6 classification of the corpus's own functions (stop, return) was never performed; the autonomy-at-distance finding says conformance turns on it and that nobody has done it.
      - **source**: ROADMAP:FIND/AUTONOMY_AT_DISTANCE.md (B6); HISTORY:FREEZE.md:256-260
      - **who**: work that can be done without the owner for the classification; the design choice is the owner's
      - **blocks**: Chapters 11 and 18.
    - item 91
      - **id**: U-12
      - **kind**: unrun check
      - **statement**: The search for a constructive codified definition of autonomy, which would refute candidate law L1, is unrun.
      - **source**: ROADMAP:RM:141-157
      - **who**: work that can be done without the owner (needs network)
      - **blocks**: Chapter 5.
    - item 92
      - **id**: U-13
      - **kind**: unrun check
      - **statement**: Held and unread: IEEE 1872-2015 and IEEE 7010-2020 (in the archive since 14 August 2026; term T-02 and row A5 wait on the first); IEEE 1788.1-2017 (see X-18).
      - **source**: ROADMAP:L7/provenance/sources/STANDARDS_REGISTER.md:310-316
      - **who**: work that can be done without the owner (needs the archive)
      - **blocks**: Chapters 3 and 15.
    - item 93
      - **id**: U-14
      - **kind**: unrun check
      - **statement**: Never read: the eb-stack code line under analysis (taken from a prompt); aybllc/ommp and aybllc/broken-zero (the codec here is a reconstruction, “CHOSEN-HERE — verify”); the private-repository sweep for the word.
      - **source**: ROADMAP:REV/EBSTACK_LAMBDA_ANALYSIS.md:131-132; ROADMAP:L8/L4/work/computation/ommp/README.md:4, 29-32; MAIN:HIST/LEDGER.md:63
      - **who**: work that can be done without the owner once access is given
      - **blocks**: Chapters 15 to 17.
    - item 94
      - **id**: U-15
      - **kind**: unrun check
      - **statement**: Census dossier: “Zero entries are byte-verified.” Its stated cause (an egress block) was disproved the same day; one citation carries an unregistered DOI.
      - **source**: ROADMAP:REV/CENSUS_SOURCES_DOSSIER.md:3, 114
      - **who**: work that can be done without the owner (needs network), after D1
      - **blocks**: Chapter 20.
    - item 95
      - **id**: U-16
      - **kind**: unrun check
      - **statement**: First-contact sources, none captured: GAO 1995, AARO 2024, ODNI 2021, the Navy's 2020 acknowledgement, NASA UAP IST 2023, Minor Planet Center codes, W3C PROV, the memory-reconstruction literature. The roadmap schedules this session after the chapter it gates.
      - **source**: ROADMAP:RM:288, 319-335, 603-604
      - **who**: work that can be done without the owner (needs network), after D1
      - **blocks**: Chapters 19, 23 and 24.
    - item 96
      - **id**: U-17
      - **kind**: unrun check
      - **statement**: External facts stated inside the corpus and never checked: NASA distributed autonomy and Starling, the synthetic cell (a rejected preprint labelled verified), NASA CP-2255, SEXTANT, AARO figures, lunar printing.
      - **source**: MAIN:LANES/THEME_LEDGER.md:344-355; ROADMAP:REV/RESEARCH_DOCKET.md:137-147
      - **who**: work that can be done without the owner (needs network)
      - **blocks**: Chapters 10 and 21; Appendix G.
    - item 97
      - **id**: U-18
      - **kind**: unrun check
      - **statement**: The lambda verification's adversarial refutation pass was still running when the file was written (“Verdicts may move”); no result is recorded, yet the roadmap carries its verdicts as settled.
      - **source**: ROADMAP:REV/LAMBDA_EXTERNAL_VERIFICATION_2026-08-04.md:232-233; ROADMAP:RM:622
      - **who**: work that can be done without the owner
      - **blocks**: Chapter 15.
    - item 98
      - **id**: U-19
      - **kind**: unrun check
      - **statement**: That λ is the fastest bit-exact criterion: “NOT TESTED”. The names and attributions (stagnation; Kahan; Neumaier) are “UNVERIFIED”.
      - **source**: ROADMAP:REV/CONJECTURE_bit_exact_pruning.md:182-184, 245
      - **who**: work that can be done without the owner
      - **blocks**: Chapter 16.
    - item 99
      - **id**: U-20
      - **kind**: unrun check
      - **statement**: The λ_A mechanism: “Four operators are named, none defined.”; no bound on the residual accumulator (owner: “[source text withheld from the public copy].”); no adversarial pass.
      - **source**: ROADMAP:AUDY:400-434
      - **who**: work that can be done without the owner to draft; the owner adopts
      - **blocks**: Chapter 16.
    - item 100
      - **id**: U-21
      - **kind**: unrun check
      - **statement**: Thesis open problems O-a to O-d, including the collision check against ISO/IEC 24970 and prEN 18229-1. Dekker 1971 is not held; the file once named for it is another paper.
      - **source**: ROADMAP:REV/THESIS_lambda_decomposed_record.md:49-58, 118-133
      - **who**: work that can be done without the owner
      - **blocks**: Chapter 16.
    - item 101
      - **id**: U-22
      - **kind**: unrun check
      - **statement**: The deep-research report of 5 August 2026 rules six repository propositions false or outdated and lists eight register corrections. None is recorded as applied or rejected; its citations are opaque tokens.
      - **source**: MAIN:L8/L4/work/computation/deep-research-auditonomous.md:23-30, 625-636
      - **who**: work that can be done without the owner (needs network)
      - **blocks**: Chapters 6 and 16.
    - item 102
      - **id**: U-23
      - **kind**: unrun check
      - **statement**: Lanes the docket says were launched, with no report found: P2 against the GUM (Type B evaluation); the reference-monitor lane (B5); the Searle check for the two-tier split.
      - **source**: ROADMAP:REV/RESEARCH_DOCKET.md:8-50, 88-96
      - **who**: work that can be done without the owner
      - **blocks**: Chapter 9.
    - item 103
      - **id**: U-24
      - **kind**: unrun check
      - **statement**: Embodied manuscript: declared content hash 7fd260a5… against 6a717c70… for the held file (“FAILED CHECK”, reproduced). It can only be settled against nu-algebra commit ea08f59, which is not available.
      - **source**: MAIN:LANES/THEME_LEDGER.md:346; ROADMAP:L7/peering/private/ingress/peer-3/object-1/martin_2026_embodied_auditonomy_lexrom_cabin_model_v0.2_ea08f59.md:18
      - **who**: work that can be done without the owner once the repository is attached
      - **blocks**: The peer-3 pin.
    - item 104
      - **id**: U-25
      - **kind**: unrun check
      - **statement**: No source pointer could be resolved: aybllc/l6 is on no machine used; commits b328334, e4f0d5c, bccf4e4 and 53b28f6 are unconfirmed. A watermark re-check is required before any change of visibility.
      - **source**: MAIN:L7/provenance/sources/LEDGER.md:20-79, 111-131
      - **who**: work that can be done without the owner once the archive is attached
      - **blocks**: Every citation of a held source.
    - item 105
      - **id**: U-26
      - **kind**: unrun check
      - **statement**: Chapter 2: “[source text withheld from the public copy]”. The seven are not listed; seven link marks in the register are the blocked-fetch mark.
      - **source**: ROADMAP:RM:111; MAIN:REV/CONTRADICTIONS.md:10-17
      - **who**: work that can be done without the owner (needs network)
      - **blocks**: Chapter 2.
    - item 106
      - **id**: U-27
      - **kind**: unrun check
      - **statement**: Definition anchors: Cambridge and Oxford are now reachable and were never captured (American Heritage stands as a substitute); the journal anchor “remains NOT-CHECKED”; Lewis and Short is “not byte-re-verified”.
      - **source**: ROADMAP:REV/EXTERNAL_AUDIT_2026-08-04.md:112-124; MAIN:DEF:308, 341-347
      - **who**: work that can be done without the owner (needs network)
      - **blocks**: Chapter 7.
    - item 107
      - **id**: U-28
      - **kind**: unrun check
      - **statement**: Space-sector standards for Chapter 18 are not held: ECSS-E-ST-70-11C, CCSDS, and the COSPAR classification of return.
      - **source**: ROADMAP:RM:274-281
      - **who**: work that can be done without the owner (needs network)
      - **blocks**: Chapter 18.
    - item 108
      - **id**: U-29
      - **kind**: unrun check
      - **statement**: HUMINT_ENCODE: the term counts over the SR, CM and SA families and the “38 blocked provisions” cannot be recounted from the tree; whether a composed substitute was ever accepted is “Not searched.”; H4 is “NOT-CHECKED”.
      - **source**: MAIN:SS/HUMINT_ENCODE.md:141-149, 159-161, 214
      - **who**: work that can be done without the owner
      - **blocks**: Chapter 13.
    - item 109
      - **id**: U-30
      - **kind**: unrun check
      - **statement**: Legal instruments relied on and unread or not held: [source text withheld from the public copy], Art. 26(5)), ISO/IEC 17021-1. The legal sources quoted in the distillation's section 7 have no provenance rows.
      - **source**: ROADMAP:REV/WALK_ACROSS_repo-instrument-standards_2026-08-05.md:94-135; MAIN:FIND/DISTILLATION.md:151-152
      - **who**: work that can be done without the owner (needs network)
      - **blocks**: Chapters 13, 18 and 21.
    - item 110
      - **id**: U-31
      - **kind**: unrun check
      - **statement**: Quotations labelled “VERIFIED” with no locator to a held copy: the ISO, IEEE, UN R157, NASA and EU quotes in the envelope and HUMINT_ENCODE; the priors record (no URL, date or hash); DR-003's three course pages (URL only).
      - **source**: MAIN:SS/AUDITON_ENVELOPE.md:23-24; MAIN:L8/L3/engineering-mathematics/uncertainty/PRIORS_EXTERNAL_2026-08-04.md:3-4; ROADMAP:REV/dr-001-003/DR-003-swap-flip-no-left-inverse.md:37-41
      - **who**: work that can be done without the owner
      - **blocks**: Chapters 12, 15 and 17.
    - item 111
      - **id**: U-32
      - **kind**: unrun check
      - **statement**: BETA: the evidence files its history names (T3-red.txt and others) are not in the tree; byte identity of the result under Python 3.14.4 is untested; its fault corrections are fresh rebuilds, true by construction.
      - **source**: BETA:HIST/AUDITONOMOUS_BETA_HISTORY.md:9-11; BETA:L8/L4/work/computation/auditonomous_beta.py:281-282
      - **who**: work that can be done without the owner
      - **blocks**: The beta's own record.
    - item 112
      - **id**: U-33
      - **kind**: unrun check
      - **statement**: Hypotheses stated and untested: the owner's “MOST IMPORTANT: I THINK DRIFT LIVES HERE! NOT ANYWHERE ELSE...(NEEDS A LOT OF STUDY)” at L0; the L3 working-life boundary; the L0 acceptance check has no recorded run.
      - **source**: MAIN:L8/L0/0.md:69; MAIN:L8/L3/0.md:63-73
      - **who**: work that can be done without the owner (a test has to be designed first)
      - **blocks**: Nothing in the book yet.
    - item 113
      - **id**: U-34
      - **kind**: unrun check
      - **statement**: Replicator and distance items: revocation at distance and parent compromise “UNVERIFIED” (“No RFC 5280 held.”); correlated process error “NOT-CHECKED”; the storage law's precondition asserted and not shown; the SA-8(9) statement not assessed against the NASA per-function finding.
      - **source**: ROADMAP:SS/AUDITON_REPLICATOR.md:554-563, 603-617; ROADMAP:FIND/AUTONOMY_AT_DISTANCE.md (B7)
      - **who**: work that can be done without the owner
      - **blocks**: Chapters 12 and 18.
    - item 114
      - **id**: U-35
      - **kind**: unrun check
      - **statement**: The referee report of 3 August 2026 set fourteen research tasks; none has a follow-up anywhere in the repository.
      - **source**: MAIN:L8/L4/work/writing/auditonomouos-important.docx; manuscript status report of 3 November 2026
      - **who**: work that can be done without the owner
      - **blocks**: The adversarial case against the book.
    - item 115
      - **id**: M-01
      - **kind**: missing object
      - **statement**: AUDY is absent from MAIN and BETA, though MAIN's envelope and distillation cite it (once as “governing text”).
      - **source**: MAIN:SS/AUDITON_ENVELOPE.md:76, 253; MAIN:FIND/DISTILLATION.md:21, 261
      - **who**: owner (merge decision)
      - **blocks**: Chapter 9.
    - item 116
      - **id**: M-02
      - **kind**: missing object
      - **statement**: The defining manuscript (Martin 2026, embodied auditonomy, v0.2) is absent from MAIN and BETA; DEF says it “now lives beside this entry at `manuscript/`”. On ROADMAP its Markdown and PDF are different texts.
      - **source**: MAIN:DEF:367; ROADMAP:L7/peering/private/ingress/peer-3/object-1/
      - **who**: owner (merge decision; pin)
      - **blocks**: DEF:28; Chapter 7.
    - item 117
      - **id**: M-03
      - **kind**: missing object
      - **statement**: Repositories no reader could open: abba-01/ebios (every corpus quotation in the definition), aybllc/l6 (every source), eb-stack or ebc, eb-audit, ommp, broken-zero, nua (the N/U paper), nu-algebra.
      - **source**: MAIN:DEF:83-185; MAIN:L7/provenance/sources/0.md:14-18
      - **who**: owner (attach or grant access)
      - **blocks**: Re-checking anything against its source.
    - item 118
      - **id**: M-04
      - **kind**: missing object
      - **statement**: No NASA extraction file exists in any state; only NASA-R6 and NASA-R10 are named, once.
      - **source**: MAIN:SS/REQUIREMENTS_OWNERSHIP.md:15, 157
      - **who**: work that can be done without the owner (re-extract)
      - **blocks**: Chapter 13.
    - item 119
      - **id**: M-05
      - **kind**: missing object
      - **statement**: Files that MAIN's records cite and only ROADMAP holds: the Master Archive, the ebios draft (EB:233), RESEARCH_DOCKET, the consolidated AUDITONOMOUS.md, STANDARDS_REGISTER, AUTONOMY_AT_DISTANCE, AUDITON_REPLICATOR, AUDITON_PACKABILITY.
      - **source**: MAIN:REV/CONTRADICTIONS.md:10, 46; MAIN:FIND/OVERRIDE_NECESSITY_2026-08-04.md:14, 169; MAIN:SS/REQUIREMENTS_OWNERSHIP.md:19; MAIN:REV/0.md:44
      - **who**: owner (merge decision)
      - **blocks**: Reading MAIN's own findings.
    - item 120
      - **id**: M-06
      - **kind**: missing object
      - **statement**: At no current head of either repository: THESIS_auditonomous_override.md, replicator-lane/gen_drift.py, COARSENING_VALIDATION, FINDING_coarsening_as_forgetting, FINDING_lambda_knob_and_retention, BREAK_THE_GLASS_obligated_record, ENCLOSURE_PRIOR_ART_2026-08-06. Some survive in Autonomous history.
      - **source**: MAIN:FIND/DISTILLATION.md:59, 85; ROADMAP:AUDY:337, 358, 433-434
      - **who**: work that can be done without the owner (recover from history)
      - **blocks**: Chapters 9 and 16.
    - item 121
      - **id**: M-07
      - **kind**: missing object
      - **statement**: In history only: FREEZE.md (the conflict records), HUB_LEDGER.md (the ruling of 14 August 2026), AUTONOMOUS_TERMS.md (the term rows the audit corrects), the definitions register.
      - **source**: HISTORY:FREEZE.md; HISTORY:HUB_LEDGER.md:49-50; HISTORY:manuscripts/definitions/REGISTER.md:12-17
      - **who**: owner
      - **blocks**: Knowing which rulings are in force.
    - item 122
      - **id**: M-08
      - **kind**: missing object
      - **statement**: Ruling texts not held: AU-NORM-01 to 04 (citations only); “DEAD FOR NOW” (reported, not quoted); rulings C-007 and C-008 (the companion's RULINGS.md is 1 byte).
      - **source**: MAIN:HIST/LEDGER_2026-08-16_l6-close-and-normalization.md:1, 32; MAIN:REV/PERPETUITY_QUESTION_ADJUDICATION.md:6; AUT:L8/L5/research/review/RULINGS.md
      - **who**: owner (restate)
      - **blocks**: The record of what the owner ruled.
    - item 123
      - **id**: M-09
      - **kind**: missing object
      - **statement**: Registers that do not exist: a definitions register; on MAIN, the register the status ladder says promotions are logged in; a register of contradictions between the repository's own findings; the authority-interface register queued on 16 August 2026.
      - **source**: MAIN:REV/STATUS_LADDER.md:25; MAIN:HIST/LEDGER_2026-08-16_l6-close-and-normalization.md:46
      - **who**: work that can be done without the owner (drafts)
      - **blocks**: Tracking status.
    - item 124
      - **id**: M-10
      - **kind**: missing object
      - **statement**: Layer 2 holds no relation, operator, proof or proof obligation. Unregistered candidates: the isomorphism, DR-003, the enclosure regime with its sign condition, conditions A to E, the Aud(S,F) form, three stipulated invariants.
      - **source**: MAIN:L8/L2/formal-mathematics/FORMULAS_LEDGER.md:10; MAIN:L8/L1/0.md:109; ROADMAP:RM:532
      - **who**: a session prepares rows; entering one is the owner's act
      - **blocks**: Part V.
    - item 125
      - **id**: M-11
      - **kind**: missing object
      - **statement**: Evidence kept outside the repository: workflow journal wf_b00a2270-83e; the audit's session journal; the definition's Appendix D agent returns; the bit-exact scripts; the distillation's section 7 session record; the quote audit the theme ledger announces.
      - **source**: MAIN:DEF:362; MAIN:FIND/DISTILLATION.md:151-152; ROADMAP:REV/CONJECTURE_bit_exact_pruning.md:203-204; MAIN:LANES/THEME_LEDGER.md:7
      - **who**: work that can be done without the owner, where recoverable
      - **blocks**: Re-checking the records' own checks.
    - item 126
      - **id**: M-12
      - **kind**: missing object
      - **statement**: Ledger rows that do not exist: the definition's six external citations; NIST SP 800-53 (extracted, no row); more than thirty works the findings cite; Rump, Kearfott and the other priors; any first-contact source; on MAIN, a row for the bound definition. The “Not held” table is empty.
      - **source**: MAIN:L7/provenance/sources/LEDGER.md:10-12, 98-100; MAIN:DEF:281-347
      - **who**: work that can be done without the owner to draft; the ledgering session is the owner's
      - **blocks**: Release rule 1; every citation.
    - item 127
      - **id**: M-13
      - **kind**: missing object
      - **statement**: The definitional instrument v0.1 that the walk-across compares both repositories with, and the v0.2 owed thirteen amendments, are in neither repository.
      - **source**: ROADMAP:REV/WALK_ACROSS_repo-instrument-standards_2026-08-05.md:5, 72-83
      - **who**: owner (say where it is)
      - **blocks**: That crosswalk's use.
    - item 128
      - **id**: M-14
      - **kind**: missing object
      - **statement**: The N/U algebra paper the defect ledger examines (19 pages) is not held; the ledger gives no hash or version.
      - **source**: ROADMAP:REV/NASA_PAPER_DEFECT_LEDGER.md:3-5
      - **who**: owner
      - **blocks**: Chapters 15 and 16.
    - item 129
      - **id**: M-15
      - **kind**: missing object
      - **statement**: On the Autonomous side: no consensus baseline; no tag exemplar-2026-09-14; the baseline paper and the read-only declaration exist only on the closed branch of pull request #29.
      - **source**: AUT:L7/peering/public/egress/0.md:37; Autonomous branch claude/scholarly-pair-baseline-k8ap82:L8/L6/history/exemplar-2026-09-14.md:11
      - **who**: owner
      - **blocks**: Chapters 3 and 4.
    - item 130
      - **id**: M-16
      - **kind**: missing object
      - **statement**: Positions with nothing filed: experiments; institution; datasets; the prior-art record; authority; four L0 positions; L3 approximation and tolerances.
      - **source**: MAIN:L8/L4/work/experiments/0.md:36; MAIN:L8/L5/institution/0.md:38-40; MAIN:L7/provenance/sources/datasets-LEDGER.md:5-16
      - **who**: no one, until there is something to file
      - **blocks**: Nothing by itself.
    - item 131
      - **id**: M-17
      - **kind**: missing object
      - **statement**: The book: no chapter text, an empty bibliography, no appendix files, a build script never run. The script that generated the chapter files is not in the repository.
      - **source**: ROADMAP:L8/L4/work/writing/book/0.md:8; ROADMAP:L8/L4/work/writing/book/bibliography.md:3
      - **who**: the writing, after the rulings
      - **blocks**: Everything in print.
    - item 132
      - **id**: M-18
      - **kind**: missing object
      - **statement**: MAIN has no enumeration of what the prune of 15 August 2026 removed (commit 8c98573, 214 files changed), against the repository's own rule of enumeration before deletion.
      - **source**: MAIN:HIST/harmonization-2026-09-05.md:19
      - **who**: work that can be done without the owner (carry ROADMAP's table), after the merge decision
      - **blocks**: Reading MAIN's own records.
    - item 133
      - **id**: M-19
      - **kind**: missing object
      - **statement**: Sources named as needed and not obtained: Beer, Fisk and Rogers 2014 (open access); Dekker 1971; Ogita, Rump and Oishi 2005; Kahan 1965; Neumaier 1974; van Emden 2004; ISO 15489-1:2016; Johnson et al. (ACM TECS); Haerder and Reuter 1983; the GUM; Moore 1966; Shapiro 2011; Birgisson 2014.
      - **source**: ROADMAP:REV/SOURCE_REQUESTS.md:30-166; ROADMAP:L7/provenance/sources/lists-2026-08-08/PRIMARY.md:9-17
      - **who**: work that can be done without the owner (needs network; some by purchase or library)
      - **blocks**: Chapters 3, 8, 15 and 16.
    - item 134
      - **id**: M-20
      - **kind**: missing object
      - **statement**: The model's manuscript guidance (7lm beta 97314c5) is in no branch of either repository. MAIN and ROADMAP still file L7/publications/ and governance/restrictions/.
      - **source**: 7lm origin/beta/common-contracts-r1-r6:L8/L4/work/writing/0.md:12-16; MAIN:L7/0.md:14
      - **who**: owner (O-01)
      - **blocks**: Where the manuscript and its release sit.
    - item 135
      - **id**: M-21
      - **kind**: missing object
      - **statement**: No session ledger in the stated format exists after 16 August 2026; the sessions of September and the beta build are recorded in other forms.
      - **source**: MAIN:L8/L6/retired/layout-2026-08-14/research/ledgers/README.md:46-52
      - **who**: owner (is the format still required)
      - **blocks**: The record of sessions.
    - item 136
      - **id**: R-01
      - **kind**: defect
      - **statement**: MAIN and ROADMAP say the source ledger has 62 rows; it has 60 ([source text withheld from the public copy] close-out says “22 new rows” and lists 21. BETA corrects both.
      - **source**: MAIN:L7/provenance/0.md:20, 33; MAIN:L7/provenance/sources/LEDGER.md:113; BETA:L7/provenance/sources/LEDGER.md:147-149
      - **who**: work that can be done without the owner (carry BETA's correction)
      - **blocks**: Any printed count.
    - item 137
      - **id**: R-02
      - **kind**: defect
      - **statement**: The master ledger, which the README calls the master index, describes nine areas that no longer exist and contradicts itself in three places.
      - **source**: MAIN:HIST/LEDGER.md:9-10, 16, 27-40; MAIN:README.md:13
      - **who**: work that can be done without the owner (a dated successor record; the old one is not rewritten)
      - **blocks**: Orientation.
    - item 138
      - **id**: R-03
      - **kind**: defect
      - **statement**: Dead links and retired paths: every cross-link in CONTRADICTIONS.md; the three MAIN L1 objects; the MAIN findings; the formulas ledger (`uso/l6/LEDGER.md`); the release checklist and binder rules; the theme ledger's aliases; AUDY's companion paths.
      - **source**: MAIN:REV/CONTRADICTIONS.md:10, 15-17; MAIN:L8/L2/formal-mathematics/FORMULAS_LEDGER.md:23; MAIN:L7/publications/binder/press-kit/README.md:18, 23; ROADMAP:AUDY:8, 179, 223
      - **who**: work that can be done without the owner (a path map; dated notes)
      - **blocks**: Following any citation.
    - item 139
      - **id**: R-04
      - **kind**: defect
      - **statement**: Sheets behind their directories: BETA's L1, L2, L3 and peering sheets do not list its new files; the L5 and L6 layer sheets omit holdings; the lane sheet says C1–C6 and T1–T11 where the ledger has C1–C11 and T1–T16; MAIN's L0 sheet says the L0 object defines Autonomous; the computation sheet says “It is empty at present.”
      - **source**: BETA:SS/0.md:35-39; MAIN:LANES/0.md:36; MAIN:L8/L0/0.md:77; MAIN:L8/L4/work/computation/0.md:54
      - **who**: work that can be done without the owner
      - **blocks**: The sheets as a guide.
    - item 140
      - **id**: R-05
      - **kind**: defect
      - **statement**: BETA's insertion moves the “line 52” clause to line 54 while its own records still cite :52; other DEF line citations shift by 2 to 16. The file is no longer the verbatim 410-line restoration (426 lines).
      - **source**: BETA:DEF:54; BETA:HIST/LEDGER.md:61; BETA:REV/PERPETUITY_QUESTION_ADJUDICATION.md:216
      - **who**: work that can be done without the owner
      - **blocks**: Every DEF line citation after a merge of BETA.
    - item 141
      - **id**: R-06
      - **kind**: defect
      - **statement**: “C<n>” names five series: envelope compartments C1–C12, standards contradictions C1–C7, internal contradictions C-1 to C-23, criteria C1–C13, rulings C-001 onward. BETA uses C6 and C7 in two senses in one file.
      - **source**: BETA:FIND/AUDITONOMOUS_BETA_FINDINGS.md:9, 24; MAIN:REV/CONTRADICTIONS.md:32
      - **who**: work that can be done without the owner (a naming note)
      - **blocks**: Reading any cross-reference.
    - item 142
      - **id**: R-07
      - **kind**: defect
      - **statement**: Labels used outside both written vocabularies (CONTESTED, UNVERIFIED, ESTABLISHED, NOT TESTED, UNVERIFIABLE AS POSED, and “INTERNALLY VERIFIED” meaning checked against an outside source). The ledger's VERIFIED means file identity. Relayed quotes are labelled VERIFIED in some places and PARTIALLY VERIFIED in others.
      - **source**: MAIN:REV/PERPETUITY_QUESTION_ADJUDICATION.md:67, 76, 327, 344; ROADMAP:REV/NASA_PAPER_DEFECT_LEDGER.md:36-56; MAIN:REV/STATUS_AND_LABEL_DISCIPLINE.md:10-13
      - **who**: owner (the label text changes [source text withheld from the public copy])
      - **blocks**: What VERIFIED means in print.
    - item 143
      - **id**: R-08
      - **kind**: defect
      - **statement**: Counts that do not match their own lists: HUMINT_ENCODE (“These three” over five rows; “eleven controls” over thirteen); the auditability record (21 over 22 rows; “approximately 90” for 62); the replicator (8 + 2 of 12); the packability finding (nine conflicts not enumerated; 58 of 78); the adjudication (16 claims over 19 rows); the A-009 tables; “69 paths moved” (68); a ledger sum of 43 for 40.
      - **source**: MAIN:SS/HUMINT_ENCODE.md:43, 159-161; ROADMAP:SS/AUDITABILITY_REQUIREMENTS.md:172-177; ROADMAP:REV/AUTHOR_ASSERTIONS.md:842-850; MAIN:HIST/harmonization-2026-09-05.md:22
      - **who**: work that can be done without the owner (dated corrections)
      - **blocks**: Any figure taken into a chapter.
    - item 144
      - **id**: R-09
      - **kind**: defect
      - **statement**: External-audit findings of 4 August 2026 never carried into the files they name: the Westby and Conselice volume and DOI; the Tic Tac equals sign and missing Mach altitude; the Morton citation; ommp.py:329; the census dossier's egress paragraph; “VERIFIED on two independent fetches”; the American Heritage substitution.
      - **source**: ROADMAP:REV/EXTERNAL_AUDIT_2026-08-04.md:94-147, 204-214, 253-300; ROADMAP:REV/CENSUS_SOURCES_DOSSIER.md:28-38, 114; MAIN:LANES/THEME_LEDGER.md:225
      - **who**: work that can be done without the owner
      - **blocks**: Chapters 7, 17, 20 and 24.
    - item 145
      - **id**: R-10
      - **kind**: defect
      - **statement**: Stale statuses: the interlock (“was still running”); lane questions Q5 and Q6c (“PENDING — lane running”); T3's superseded sentences; the replicator's “under review” rows; SOURCE_REQUESTS (five requests met or part-met elsewhere, unamended); the docket's B5, B6 and D3.
      - **source**: MAIN:LANES/RECORD_ONTOLOGY_OPEN_QUESTIONS.md:140, 195; ROADMAP:REV/SOURCE_REQUESTS.md:43-49, 142-149, 177; ROADMAP:REV/RESEARCH_DOCKET.md:28-29, 128
      - **who**: work that can be done without the owner (dated amendments)
      - **blocks**: Knowing what is still open.
    - item 146
      - **id**: R-11
      - **kind**: defect
      - **statement**: Three nits the definition's own verification found were never applied and are on no pending list: a citation span (:127 for 127-128); an unmarked cut in the RFC 4949 firmware quote; the unflagged constructed pronunciation.
      - **source**: MAIN:DEF:14, 47, 69, 351
      - **who**: owner (the definition changes by version)
      - **blocks**: Chapter 7.
    - item 147
      - **id**: R-12
      - **kind**: defect
      - **statement**: Corrections made by overwriting, against the rule that the wrong version stays visible: AUDY's fix list; T3's adopted-then-withdrawn definition; the Autonomous beta's deletion of a register row; the thesis's closing line still saying Dekker is held.
      - **source**: ROADMAP:AUDY:19-20, 42-43; MAIN:LANES/THEME_LEDGER.md:158, 272; ROADMAP:REV/THESIS_lambda_decomposed_record.md:49-58, 143-145
      - **who**: work that can be done without the owner (restore the earlier wording beside the correction)
      - **blocks**: The record's own rule.
    - item 148
      - **id**: R-13
      - **kind**: defect
      - **statement**: The roadmap: chapter gate lines and the decision table disagree in eight places; “three seam joints” lists four; sheets give the decision range as D1–D21; Chapter 22 cites a feed held in no tree; Chapter 19's drafting precedes its own verification session; it counts 62 ledger rows.
      - **source**: ROADMAP:RM:82-87, 312, 603-604, 612-633; ROADMAP:L8/L4/work/writing/book/0.md:8, 14
      - **who**: work that can be done without the owner
      - **blocks**: Using the roadmap as the plan.
    - item 149
      - **id**: R-14
      - **kind**: defect
      - **statement**: The vocabulary paper's claims table: row 16 is wrong (X-25); row 3 gives Block 3 line 10 where the sentence is at line 1; row 6 says every condition anchors to a VERIFIED control where its source marks condition B's sources “NOT-CHECKED”.
      - **source**: ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:292, 295, 305
      - **who**: work that can be done without the owner
      - **blocks**: The paper's use by Chapters 7 to 9.
    - item 150
      - **id**: R-15
      - **kind**: defect
      - **statement**: The restore record declines five Office drafts citing the harmonization record's section 8, which exists but names none of them; it misfiles the owner's working draft as packaging of the sourcebook; it says two objects went to L0 and L1 where its table places three.
      - **source**: ROADMAP:HIST/restore-2026-09-14.md:18, 33, 54-55, 191-195; MAIN:HIST/harmonization-2026-09-05.md:105-125
      - **who**: work that can be done without the owner (a dated correction)
      - **blocks**: Decision O-10.
    - item 151
      - **id**: R-16
      - **kind**: defect
      - **statement**: Personal paths (“/home/eric”) stand in 15 files on MAIN, including the definition; the release checklist forbids them.
      - **source**: MAIN:DEF:74, 266-278, 340; MAIN:L7/publications/binder/press-kit/README.md:22
      - **who**: work that can be done without the owner to prepare; the owner approves edits to the definition
      - **blocks**: Any release.
    - item 152
      - **id**: R-17
      - **kind**: defect
      - **statement**: Peering records: internal repositories sit under peering/public/; BETA files a computation as object-2 while its unchanged sheet reserves object-2 for AUTOMATION.md; ROADMAP's peer-3 sheet still says the manuscript is absent; MAIN's binding sheet says the definition “names this binding” and it does not.
      - **source**: MAIN:L7/peering/public/ingress/peer-1/object-1/0.md:18, 34; BETA:L7/peering/public/ingress/peer-1/0.md:20-22; ROADMAP:L7/peering/private/ingress/peer-3/0.md:8, 16
      - **who**: work that can be done without the owner
      - **blocks**: The desk.
    - item 153
      - **id**: R-18
      - **kind**: defect
      - **statement**: Copyright and source records: “the 31 WSU-licensed IEEE PDFs” against 30 + 3 and 34 ledger rows; four stamped rows lack the hold-private tag; STD-025 has no hash; one full-text paper copy is in the tree though the sheet says no source is copied.
      - **source**: MAIN:L7/governance/copyright/0.md:43, 45; MAIN:L7/provenance/sources/LEDGER.md:50-58
      - **who**: work that can be done without the owner
      - **blocks**: The conditions on quotation.
    - item 154
      - **id**: R-19
      - **kind**: defect
      - **statement**: Quotation fidelity: three SP 800-53 controls quoted in shortened form that drops operative words; the override finding presents a cleaned sentence in quotation marks as the owner's; percentages truncated, not rounded.
      - **source**: ROADMAP:SS/AUDITABILITY_REQUIREMENTS.md:49-55, 120-122, 193, 202; MAIN:FIND/OVERRIDE_NECESSITY_2026-08-04.md:12-13
      - **who**: work that can be done without the owner
      - **blocks**: Any quotation taken from these files.
    - item 155
      - **id**: R-20
      - **kind**: defect
      - **statement**: Reading records: RFC 9162 says 45 captures and holds 48 (43 compared); FIPS 180-4 says 25 pages and 24; IEEE 3152's verifier input was truncated (six defects stand); 19 items of the IEEE 7007 record were never compared.
      - **source**: MAIN:STG/library/reading/RFC9162_Certificate-Transparency-v2.md:27; MAIN:STG/ieee/reading/IEEE-3152.md:381-399
      - **who**: work that can be done without the owner (needs the archive)
      - **blocks**: Quoting those four sources.
    - item 156
      - **id**: R-21
      - **kind**: defect
      - **statement**: The Tic Tac adjudication: “VERIFIED arithmetic” with no outside source fetched; “~4 ORDERS OF MAGNITUDE” where its own figure is about 780 times; a Roosevelt attribution no official document carries; the 0.78 s input comes from an unofficial report.
      - **source**: ROADMAP:REV/TICTAC_PROPULSION_ADJUDICATION.md:40, 52-53, 111, 250, 362
      - **who**: work that can be done without the owner
      - **blocks**: Chapters 19 and 24.
    - item 157
      - **id**: R-22
      - **kind**: defect
      - **statement**: Probe and code notes: the 9.49% containment figure is a property of the probe's integer grid and the roadmap carries it as a property of the operator; the DR-001 probe prints 15/8 beside “the factor of 2”; the OMMP README says 66 where 65 checks run; the lambda probe's docstring keeps a withdrawn claim.
      - **source**: ROADMAP:REV/EBSTACK_LAMBDA_ANALYSIS.md:72-81; ROADMAP:RM:622; ROADMAP:L8/L4/work/computation/probes/dr001_half_cell.py:39-40; ROADMAP:L8/L4/work/computation/ommp/README.md:257
      - **who**: work that can be done without the owner
      - **blocks**: Chapters 15 and 17.
    - item 158
      - **id**: R-23
      - **kind**: defect
      - **statement**: The interlock proposal cites EB:233, EB:38 and LEX:487 with no key and neither source on MAIN; the same manuscript line is keyed LEX in one record and EMB in another; the sourcebook's only statement of the autonomy profile has a row of “=” where an equals sign belongs.
      - **source**: MAIN:L8/L3/engineering-mathematics/PROPOSAL_seal_gated_interlock.md:18-20; ROADMAP:L8/L4/work/writing/sourcebook/Auditonomous_Book_Material_Sourcebook_v0.1.md:65-70
      - **who**: work that can be done without the owner
      - **blocks**: Chapter 14.
    - item 159
      - **id**: R-24
      - **kind**: defect
      - **statement**: MAIN's distillation is stale against itself (law L6 “NOT-CHECKED” while its section 7.4 marks the same row verified) and its relative paths resolve nowhere.
      - **source**: MAIN:FIND/DISTILLATION.md:15, 21, 99-101, 124, 273-285
      - **who**: work that can be done without the owner (a dated note)
      - **blocks**: Chapter 5.
    - item 160
      - **id**: R-25
      - **kind**: defect
      - **statement**: File names are misspelled in the computation directory (autonomouos, auditonomopus) and in the writing directory (auditonomouos-important.docx, auditnomous-main.docx).
      - **source**: MAIN:L8/L4/work/computation/ (tree listing); MAIN:L8/L4/work/writing/ (tree listing)
      - **who**: owner (renames are his)
      - **blocks**: Citations by file name.
    - item 161
      - **id**: R-26
      - **kind**: defect
      - **statement**: The three Office files on MAIN are labelled “live drafts”; none is a draft of the book (a prospectus, a referee report, an extraction corpus).
      - **source**: MAIN:L8/L4/work/writing/0.md:33; MAIN:HIST/LEDGER.md:37
      - **who**: work that can be done without the owner (sheet wording)
      - **blocks**: What the manuscript directory is taken to hold.
    - item 162
      - **id**: Q-01
      - **kind**: question
      - **statement**: Does a repository aybllc/eb-stack exist? Two ROADMAP records describe a GitHub read of it on 5 August 2026 (commit c3ec814); the roadmap says “[source text withheld from the public copy]” and that [source text withheld from the public copy].
      - **source**: ROADMAP:REV/LAMBDA_PRIOR_ART_2026-08-05.md:173-177; ROADMAP:RM:655
      - **who**: owner (one line settles it)
      - **blocks**: The homonym ruling; Chapter 15.
    - item 163
      - **id**: Q-02
      - **kind**: question
      - **statement**: Did the owner rule before BETA applied its dispositions (Appendix C, Q13, C1–C7), and is its “no rebind” his ruling on D22? Was BETA made by Codex? The commit's author is EDM and it has no generator trailer.
      - **source**: BETA:714480d; BETA:HIST/AUDITONOMOUS_BETA_HISTORY.md:3
      - **who**: owner
      - **blocks**: How BETA is merged.
    - item 164
      - **id**: Q-03
      - **kind**: question
      - **statement**: Are abba-01/ebios and aybllc/ebios one object, and is docs/EINSTEIN_BRANCH.md on branch v1.0.0-dev? If it is on the attempt branch only, the firmware contradiction rests on a branch the owner ruled was only an attempt.
      - **source**: MAIN:DEF:384-410
      - **who**: owner, or a session with access
      - **blocks**: X-05.
    - item 165
      - **id**: Q-04
      - **kind**: question
      - **statement**: The [source text withheld from the public copy] itself”; of the bootstrapping objection, “[source text withheld from the public copy]”. The walk-across calls it the deepest open problem.
      - **source**: MAIN:FIND/OVERRIDE_NECESSITY_2026-08-04.md:162; ROADMAP:SS/AUDITON_REPLICATOR.md:488-492; ROADMAP:REV/WALK_ACROSS_repo-instrument-standards_2026-08-05.md:135
      - **who**: work that can be done without the owner; the owner adopts
      - **blocks**: Chapters 9, 12 and 14.
    - item 166
      - **id**: Q-05
      - **kind**: question
      - **statement**: Q10: who is the adopter or assessor for a scout beyond return (“*unresolved*”). Delivery is carriable; readership is not.
      - **source**: MAIN:SS/REQUIREMENTS_OWNERSHIP.md:254-257
      - **who**: owner
      - **blocks**: Chapters 13 and 18.
    - item 167
      - **id**: Q-06
      - **kind**: question
      - **statement**: The research question the perpetuity adjudication leaves: under what conditions a system can keep a monotone, tamper-evident commitment to its whole history while its operating state stays bounded. “[source text withheld from the public copy].”
      - **source**: MAIN:REV/PERPETUITY_QUESTION_ADJUDICATION.md:277-285
      - **who**: work that can be done without the owner
      - **blocks**: Chapter 25.
    - item 168
      - **id**: Q-07
      - **kind**: question
      - **statement**: Open technical questions with no check: whether an optimal coupling knob k exists; whether noise-symbol growth is unbounded; whether [source text withheld from the public copy] is new (“UNVERIFIED as novel”).
      - **source**: ROADMAP:AUDY:347-349; MAIN:L8/L3/engineering-mathematics/uncertainty/PRIORS_EXTERNAL_2026-08-04.md:119-129
      - **who**: work that can be done without the owner
      - **blocks**: Chapters 15 and 16.
    - item 169
      - **id**: Q-08
      - **kind**: question
      - **statement**: What “the source ledger” to be locked with Chapter 19 is (the L7 pointer ledger, the bibliography, or a ledger per chapter), and which seven quotations Chapter 2's re-check means.
      - **source**: ROADMAP:RM:111, 547
      - **who**: owner
      - **blocks**: Chapters 2 and 19.
    - item 170
      - **id**: Q-09
      - **kind**: question
      - **statement**: Remote state no reader checked (no network): the standing of pull requests #27 and #29, the exemplar tag, branch protection, repository visibility, whether today's session branch is pushed.
      - **source**: Local refs of the three clones on 11 November 2026
      - **who**: a session with network, or the owner
      - **blocks**: Decision O-01.
    - item 171
      - **id**: Q-10
      - **kind**: question
      - **statement**: Does branch rescue/reorg-2026-08-14 still exist? It is not among the fetched refs; the ledgers say it holds the first deployment and pre-redaction bytes (“never replay”).
      - **source**: MAIN:HIST/LEDGER_2026-08-14_redeploy.md:7; MAIN:HIST/LEDGER_2026-08-16_l6-close-and-normalization.md:40
      - **who**: owner
      - **blocks**: Decision O-08.
    - item 172
      - **id**: Q-11
      - **kind**: question
      - **statement**: Whether the labels “VERIFIED” given on 2 August 2026 to quotes read from mirrors, relays and index sweeps meet the outside-source rule restated on 8 August 2026.
      - **source**: MAIN:REV/STATUS_LADDER.md:13-18; MAIN:REV/PERPETUITY_QUESTION_ADJUDICATION.md:327
      - **who**: owner (the rule is his)
      - **blocks**: Chapter 25; R-07.
  - **claims_total**: 12
  - **claims_not_standing**
    - item 1
      - **claim**: No record in the repository tests any system against the definition, and the definition says so itself. Experiments are empty in MAIN, ROADMAP and BETA. BETA's one computation is a synthetic 16-case fixture whose result sets every achievement flag false.
      - **id**: KC-01
      - **verdict**: corrected
      - **reasoning**: Every cited locator resolves and every quoted string is verbatim, but three parts of the claim are imprecise or overstated.

        CONFIRMED
        - MAIN:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:57 reads "[source text withheld from the public copy]". ROADMAP carries the same blob (8b934b4).
        - MAIN:L8/L4/work/experiments/0.md:36 reads "Nothing is filed at this position; the position is admissible and empty. No experiment has been executed". The blob (a86e481) is identical in MAIN, ROADMAP and BETA, and 0.md is the only file in that directory in each state.
        - The sheet L8/L4/work/0.md:43 says in all three states: "No implemented system, experiment, or measurement is claimed."
        - BETA:L8/L4/work/computation/auditonomous_beta_result.json (parsed, not re-run): 16 inputs, 16 traces, 32 events, 32 records; environment.synthetic and model.synthetic are both true.
        - BETA:L8/L5/research/findings/AUDITONOMOUS_BETA_FINDINGS.md:11 reads "[source text withheld from the public copy]."

        WRONG OR IMPRECISE
        1. "The definition says so itself" is overstated. Line 57 disclaims achievement; it does not say that no test record exists. It says the eBIOS corpus has its own "compliance, proof-status, and validation statements", which it calls "[source text withheld from the public copy]". MAIN:...DEFINITION.md:64 even cites an eBIOS test docstring: "[source text withheld from the public copy]. Those tests live in abba-01/ebios, not in this repository. The plain "nothing tested, nothing built" statement comes from the two sheets, not from the definition.
        2. The line 57 locator is true of MAIN and ROADMAP only. BETA's definition is a different blob (8127041, 16 lines added on 2026-11-03) and the same sentence is at line 59.
        3. "No record tests any system against the definition" holds only for executed tests. Desk comparisons of named systems against the definition do exist:
           - All three states, in the definition itself: MAIN:...DEFINITION.md:47 and :252 (BETA :49 and :254) read eBIOS's own documents against the firmware clause — "no firmware artifact exists in the corpus".
           - ROADMAP only: Auditonomous_Theory_Master_Archive.md:312-314 maps NASA DSA/Starling — "[source text withheld from the public copy]", then "the absent clause ... no mandatory auditability".
           - ROADMAP only: the same file at :486 and Block_40_The_Wetware_Instance.md:25 — "[source text withheld from the public copy]."
           These are authorial prose (INTERNAL ONLY; the SpudCell passage is labelled by Block 40 "resonance, not evidence"), not test records. Each concludes non-satisfaction.
        4. BETA does run something against part of the definition's apparatus. The fixture is checked against two selected predicates, C6 stop and C7 record, taken from AUDITON_ENVELOPE. Findings :9 says "selected task execution is demonstrated" and that applying the complete senses "remains **unresolved**". The result's limitations say these [source text withheld from the public copy]".
        5. "Every achievement flag false" needs one qualifier. The /claims object has five keys: four *_achieved flags, all false, and standards_autonomy, which is the string "unresolved" rather than a boolean.
        6. "BETA's one computation" is imprecise. BETA:L8/L4/work/computation/0.md:38-44 lists the fixture plus six inherited outputs (three requirements extractions, a deep-research run and its two exports). The fixture is the only executed code in BETA.
        7. ROADMAP holds other code that the claim does not mention: eight numerical probes and a reconstructed OMMP codec with test_ommp.py. Their sheets say "None was re-run in the restoring pass" and "RECONSTRUCTION — NOT CANONICAL". None tests a system against the definition, so they do not refute the claim, but "experiments are empty" should not be read as "no code exists".

        NOT CHECKED
        - I did not execute test_auditonomous_beta.py or regenerate the result; my task did not authorise a run.
        - The pinned producer commit 805cd42 exists in /home/user/autonomous on origin/beta/7lm-exemplar-autonomous; I did not compare its bytes to the recorded hashes.

        EVIDENCE STATE
        - UNRESOLVED for "any system is auditonomous": no executed test of an implemented system exists, and BETA labels the full application "unresolved".
        - EMPTY for the experiments position in all three states.
        - INTERNALLY CHECKED, synthetic and bounded, for the BETA fixture's two selected predicates.
      - **corrected_statement**: No record in the repository reports an executed test, experiment or measurement of any implemented system against the definition, in MAIN, ROADMAP or BETA. The sheets say so: L8/L4/work/experiments/0.md:36 ("No experiment has been executed"; blob a86e481, identical in all three states, and the only file in that directory) and L8/L4/work/0.md:43 ("No implemented system, experiment, or measurement is claimed", same text in all three). The definition does not say that no test exists. At MAIN and ROADMAP line 57 (BETA line 59, a different blob) it disclaims achievement only: "[source text withheld from the public copy]". It labels the eBIOS corpus's own compliance, proof and validation statements, which live outside this repository, as "[source text withheld from the public copy]". What does exist are desk comparisons, not tests. The definition reads eBIOS's documents against the firmware clause ("no firmware artifact exists in the corpus", MAIN :47 and :252). In ROADMAP only, manuscript prose measures two named systems against the definition: NASA DSA/Starling (Master Archive :312-314, audit clause "absent") and the SpudCell (:486, "fails almost every clause"). BETA's only executed code is a synthetic 16-case fixture (32 events, 32 records) checked against two selected predicates, C6 stop and C7 record, "not full auditonomous meaning". Its result sets all four *_achieved flags false and standards_autonomy to "unresolved", and its findings leave application of the complete Auditonomous senses "unresolved". BETA's computation directory also holds six inherited extraction and deep-research outputs. ROADMAP additionally holds eight numerical probes and a non-canonical OMMP codec reconstruction, none re-run on restore and none testing a system against the definition.
      - **evidence_checked**
        - MAIN:L8/L5/research/review/STATUS_LADDER.md and STATUS_AND_LABEL_DISCIPLINE.md (read first; "[source text withheld from the public copy]")
        - MAIN:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:57 (quote verbatim; blob 8b934b4, identical in ROADMAP)
        - BETA:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:59 (same sentence, blob 8127041, +16 lines vs MAIN)
        - MAIN:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:47, :64, :79, :252 (firmware clause vs eBIOS documents; eBIOS test docstring citation; self-report labels)
        - MAIN/ROADMAP/BETA:L8/L4/work/experiments/0.md:36 (blob a86e481 in all three; directory listing shows only 0.md)
        - MAIN/ROADMAP/BETA:L8/L4/work/0.md:40-43 ("work/experiments/ — empty"; "No implemented system, experiment, or measurement is claimed")
        - BETA:L8/L4/work/computation/auditonomous_beta_result.json (parsed with python3 -I from a scratch copy: /claims, /execution/inputs len 16, /execution/traces len 16, /findings, /limitations, /faults, /model, /pins)
        - BETA:L8/L5/research/findings/AUDITONOMOUS_BETA_FINDINGS.md:7, :9, :11
        - BETA:L8/L4/work/computation/0.md:38-44, :56 (holdings: fixture plus six inherited outputs)
        - BETA:L8/L0/semantics/AUDITONOMOUS_BETA_SCOPE.md and L8/L2/formal-mathematics/relations/AUDITONOMOUS_BETA_PREDICATE.md (C6/C7 as selected predicates)
        - BETA:L8/L4/work/computation/test_auditonomous_beta.py (12 test methods listed; not executed)
        - ROADMAP:L8/L4/work/computation/0.md:44-46, probes/0.md:8-20, ommp/0.md:8-18, ommp/README.md:1-30
        - ROADMAP:L8/L4/work/writing/manuscript/Auditonomous_Theory_Master_Archive.md:312-314 and :486; Block_40_The_Wetware_Instance.md:22-30; Block_25_NASA_DSA_Exhibit.md:1-19; manuscript/0.md
        - ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:275 ("That any system is auditonomous" listed as not claimed)
        - ROADMAP:L8/L5/research/review/EXTERNAL_AUDIT_2026-08-04.md:1-20 and WALK_ACROSS_repo-instrument-standards_2026-08-05.md:1-20 (check claims and documents, not systems)
        - git grep across MAIN, ROADMAP and BETA under L7 and L8 for 'against the definition', 'thirteen criteria', 'conformance test', 'tested against', 'no experiment', 'unrun'
        - git ls-tree of all three states for .py/.json/.csv/test/experiment/result files; git diff --name-status MAIN..ROADMAP and MAIN..BETA
        - /home/user/autonomous: commit 805cd42 exists on origin/beta/7lm-exemplar-autonomous; research/AUDITON_CONFORMANCE_MATRIX.md exists only in that repository's history (c866842), not in any current state of either repository
    - item 2
      - **claim**: Two texts claim to be the definition and no document states their relation. The entry of 30 July 2026 is the record by ruling AU-NORM-02 and is on MAIN. AUDITONOMY.md of 5 August 2026 says its v2 definition governs, is labelled conjecture, and is on ROADMAP only, although MAIN's distillation calls it the governing text.
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
    - item 3
      - **claim**: The formal layer is empty on MAIN and ROADMAP: no relation, operator or proof is registered. One formal predicate for the word does exist, unratified and unregistered: Aud(S,F) if and only if Aut(S,F) and five conditions, in the model-written sourcebook. Reports that it does not exist are wrong.
      - **id**: KC-03
      - **verdict**: corrected
      - **reasoning**: Every cited locator checks out, but the claim is imprecise in three places and misses one contradicting record.

        CONFIRMED
        - The L2 register and positions are empty. MAIN:L8/L2/formal-mathematics/FORMULAS_LEDGER.md:10 reads "Currently: **EMPTY** — no formulas held."; both register tables (lines 16-18, 38-40) are blank.
        - MAIN:relations/0.md:33 and operators/0.md:33 read "Nothing is filed at this position; the position is admissible and empty." proofs/0.md:35 opens with the same sentence.
        - `git diff origin/main ROADMAP -- L8/L2` is empty, so all of this holds identically on ROADMAP.
        - The predicate exists at ROADMAP:L8/L4/work/writing/sourcebook/Auditonomous_Book_Material_Sourcebook_v0.1.md:113-124: "A compact formalization is:" followed by `\[source text withheld from the public copy]`. The five conditions are defined at lines 128-132, just outside the cited range.
        - The contrary reports exist and are wrong about the predicate: vocabulary paper :305 ("[source text withheld from the public copy])") and :158; roadmap record BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:583, :630 and :647 ("[source text withheld from the public copy]").
        - Cause of the false negative: the literal string `Aud(S,F)` occurs 0 times in the sourcebook because the text is `\operatorname{Aud}(S,F)`. The grep was right about the string and about the spine (0 hits) but wrong about the predicate. Roadmap :647 therefore "corrected" a first version of D20 that had been right.
        - "Unregistered": the predicate is not in the ledger and not among the unregistered candidates the L2 sheet lists (MAIN:L8/L2/0.md:76 names only the isomorphism and the perpetuity argument).
        - "Unratified": the sourcebook's label class at :18 is "[source text withheld from the public copy]"; :2252 still lists "[source text withheld from the public copy]…" as outstanding. The passage itself carries no label, and I found no ratification record.
        - "Model-written": sourcebook :10 "earlier assistant language"; its ledger row L002 "Pasted markdown.md, INCLUDED SELECTIVELY"; ROADMAP:SESSION_2026-08-05_VERIFICATION_LOG.md:125 "[source text withheld from the public copy]."

        WRONG OR IMPRECISE
        1. The predicate is not ROADMAP-only. It is also on MAIN (and BETA, same blob d03eb10) inside L8/L4/work/writing/auditnomous-main.docx, which is the Office form of the same sourcebook ("Auditonomous Book Material Sourcebook … Version 0.1"). In my text extraction of word/document.xml it sits at paragraphs 75-91. `git grep` cannot see inside the docx. On ROADMAP it also stands at L8/L4/work/computation/all-research-corpus-auditonomous.md:143-154, the pasted "AUTONOMY-STACK SSOT v0.1" (2026-08-05) it was extracted from.
        2. "One formal predicate for the word" undercounts. Two other iff-form formalisations of the word exist, also unregistered at L2:
           - ROADMAP:L8/L0/semantics/definitions/AUDITONOMY.md:197, "[source text withheld from the public copy]:", with conditions A-E at :199-205. The file's own label at :3 is "CONJECTURE / INTERNAL ONLY"; §2 at :191 is headed "prior form, retained".
           - MAIN, ROADMAP and BETA: L8/L4/work/writing/chat/auditonomous-chat-1.docx (extracted paragraphs 738-740) and auditonomouos-chat-2.docx (792-794), "Minimal formal test / AuditonomousAction(α) ⇔ ActionSpecific(α)∧ …", thirteen conjuncts.
           Aud(S,F) is the only one written as a predicate over (S,F) with Aut(S,F) as a conjunct.
        3. The claim omits that the repository's own record flags the predicate. ROADMAP:L8/L4/work/writing/sessions/SESSION_2026-08-05_VERIFICATION_LOG.md:134-137: "**[source text withheld from the public copy]." It cites FINDING_R157 §3 ("falsification condition 2 … is **engaged, not closed**"). The evidence state is therefore CONTRADICTED (flagged), not merely unratified. This log also read the predicate on 2026-08-05, which further contradicts the 2026-09-14 negative finding.
        4. "Empty" needs two qualifiers.
           - proofs/0.md:35 and L8/L2/0.md:76 name candidate exact objects that exist unregistered: the isomorphism (ℝ≥0,+) ≅ ((0,1],×) with its four-line proof in SESSION_2026-08-05_AUDITON_ARCHITECTURE.md §7.5, and the PERPETUITY_QUESTION_ADJUDICATION argument.
           - On BETA the layer is no longer empty by content. BETA:L8/L2/formal-mathematics/relations/AUDITONOMOUS_BETA_PREDICATE.md (7 lines, "Exact selected finite predicate — beta v1", added in 714480d) is filed, while BETA's relations/0.md:33 and FORMULAS_LEDGER.md:10 are unchanged and still say nothing is filed. That file holds fixture predicates of the exemplar ("conditional fixture predicates, not derived universal definitions"), not Aud(S,F).

        Evidence states: the L2 register is EMPTY (MAIN, ROADMAP). The Aud(S,F) predicate is ASSERTED by a model, unratified, and CONTRADICTED by F-2. The "does not exist" negative finding is CONTRADICTED. BETA's sheets are CONTRADICTED by BETA's own tree.
      - **corrected_statement**: KC-03 (corrected): The L2 register and its three positions are empty on MAIN and ROADMAP (L8/L2 is byte-identical between them): FORMULAS_LEDGER.md:10 "Currently: **EMPTY** — no formulas held."; relations/0.md:33, operators/0.md:33 and proofs/0.md:35 "Nothing is filed at this position". No relation, operator or proof is registered. The sheets do name two unregistered candidates (the isomorphism (ℝ≥0,+) ≅ ((0,1],×) with its four-line proof, and the perpetuity argument: proofs/0.md:35, L8/L2/0.md:76). On BETA one file is filed at relations/ (AUDITONOMOUS_BETA_PREDICATE.md, fixture predicates of the exemplar, not Aud(S,F)), while BETA's relations/0.md:33 and FORMULAS_LEDGER.md:10 still say nothing is filed.

        A formal predicate for the word does exist, unregistered and unratified: [source text withheld from the public copy]. It is model-written, originating in the pasted "AUTONOMY-STACK SSOT v0.1" of 2026-08-05. It stands at ROADMAP:L8/L4/work/writing/sourcebook/Auditonomous_Book_Material_Sourcebook_v0.1.md:113-124 (conditions defined at :128-132) and ROADMAP:L8/L4/work/computation/all-research-corpus-auditonomous.md:143-154. It is also on MAIN, ROADMAP and BETA inside the Office form of the sourcebook, L8/L4/work/writing/auditnomous-main.docx (blob d03eb10), so it is present in the merged state, where text grep cannot see it.

        It is not the only iff-form formalisation of the word. Two others exist, also unregistered: ROADMAP:L8/L0/semantics/definitions/AUDITONOMY.md:197 ("[source text withheld from the public copy]", conditions A-E, labelled CONJECTURE / INTERNAL ONLY, "prior form, retained"); and "AuditonomousAction(α) ⇔ …" (thirteen conjuncts, "Minimal formal test") in L8/L4/work/writing/chat/auditonomous-chat-1.docx and auditonomouos-chat-2.docx on all three states.

        The Aud(S,F) predicate is flagged in the repository's own record: ROADMAP:L8/L4/work/writing/sessions/SESSION_2026-08-05_VERIFICATION_LOG.md:134-137, [source text withheld from the public copy]" (FINDING_R157 §3). Its evidence state is ASSERTED by a model, unratified, and CONTRADICTED.

        The reports that it does not exist are wrong about the predicate: vocabulary paper :305 and :158; roadmap record :583, :630 and :647 (all ROADMAP only). Their grep was literally right about the string: "Aud(S,F)" occurs 0 times in the sourcebook because the text is `\operatorname{Aud}(S,F)`, and the spine has no occurrence. The roadmap's "correction" at :647 replaced a first version of D20 that had been right.
      - **evidence_checked**
        - MAIN:L8/L5/research/review/STATUS_LADDER.md and STATUS_AND_LABEL_DISCIPLINE.md (read first for the repository's labels)
        - MAIN:L8/L2/formal-mathematics/FORMULAS_LEDGER.md:10 'Currently: **EMPTY** — no formulas held.'; register tables at :16-18 and :38-40 blank
        - MAIN:L8/L2/formal-mathematics/relations/0.md:33 and operators/0.md:33 'Nothing is filed at this position; the position is admissible and empty.'
        - MAIN:L8/L2/formal-mathematics/proofs/0.md:35 same sentence plus 'Candidate (owner's call): the four-line proof of the isomorphism (ℝ≥0,+) ≅ ((0,1],×)'
        - MAIN:L8/L2/0.md:74-76 'EMPTY by its own declaration'; 'Candidate exact object not yet extracted or registered (owner's call)'
        - MAIN:L8/L2/formal-mathematics/0.md:39 'entering a row is the owner's act'
        - git diff origin/main ROADMAP -- L8/L2: empty. git diff origin/main BETA -- L8/L2: one added file
        - BETA:L8/L2/formal-mathematics/relations/AUDITONOMOUS_BETA_PREDICATE.md:1-7 'Exact selected finite predicate — beta v1 … conditional fixture predicates, not derived universal definitions'; referenced only by BETA:L8/L4/work/computation/auditonomous_beta.py:34 and auditonomous_beta_result.json:1442
        - ROADMAP:L8/L4/work/writing/sourcebook/Auditonomous_Book_Material_Sourcebook_v0.1.md:111-132 (predicate and its five conditions); :10, :18 (label classes); :2252 (ratification still outstanding); literal 'Aud(S,F)' count = 0
        - ROADMAP:L8/L4/work/writing/sourcebook/0.md:8,16 (restored 2026-09-14 from 1d83788; INTERNAL ONLY); Coverage ledger CSV row L002 'Pasted markdown.md, INCLUDED SELECTIVELY'
        - ROADMAP:L8/L4/work/computation/all-research-corpus-auditonomous.md:1-4, 139-160 ('AUTONOMY-STACK SSOT v0.1', same predicate)
        - MAIN/ROADMAP/BETA:L8/L4/work/writing/auditnomous-main.docx (blob d03eb10 on all three): word/document.xml extracted with python3 -I zipfile; paragraphs 2-12 identify it as the sourcebook v0.1; paragraphs 75-91 carry the Aud(S,F) predicate
        - MAIN:L8/L4/work/writing/0.md:33 describes auditnomous-main.docx as one of 'the live drafts'
        - MAIN/ROADMAP/BETA:L8/L4/work/writing/chat/auditonomous-chat-1.docx (extracted paragraphs 738-742) and auditonomouos-chat-2.docx (792-796): 'Minimal formal test / AuditonomousAction(α) ⇔ …'
        - ROADMAP:L8/L0/semantics/definitions/AUDITONOMY.md:3, 191-208 ('[source text withheld from the public copy]', A-E; CONJECTURE / INTERNAL ONLY); file absent on MAIN and BETA
        - ROADMAP:L8/L4/work/writing/sessions/SESSION_2026-08-05_VERIFICATION_LOG.md:123-137 (F-2 flags the predicate as contradicting FINDING_R157 §3; '[source text withheld from the public copy]')
        - ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:158 and :305 (the negative finding)
        - ROADMAP:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:583, :630, :647 (the negative finding repeated; D20 reworded)
        - ROADMAP:L8/L5/research/review/SPINE_v0.1_2026-08-14.md: no occurrence of the predicate (17 'Aud' hits, all 'Audi…')
        - git grep for operatorname{Aud}, 'Aud(', \\iff, ⇔, ⟺, 'iff', 'if and only if', AuditonomousAction across MAIN, ROADMAP, BETA and 1d83788 (text files only; MAIN and BETA text hits for Aud: none)
        - MAIN:L8/L4/work/computation/deep-research-auditonomous.md:283-288 (AO(a) ⇔ P1∧P2∧P3∧P4: an audited-override rule, not a predicate for the word; excluded from the count)
        - Not found: any ratification record for Aud(S,F), or any later correction of the negative finding on ROADMAP (last commit 9259c18, 2026-09-14)
    - item 4
      - **claim**: The lambda results that stand: λ = 1 is Rump's 1999 midpoint-radius product and always encloses; the λ = 0 radius is exact for sign-definite operands only when the centre is shifted; λ = 0 as coded, with the centre unshifted, is not an enclosure. All three records are on ROADMAP only.
      - **id**: KC-04
      - **verdict**: corrected
      - **reasoning**: Every cited locator checks out, and the mathematics is confirmed, but four parts of the claim are imprecise or overstated.

        **What I confirmed**
        - **λ = 1 is Rump's product.** ROADMAP:L8/L5/research/review/LAMBDA_EXTERNAL_VERIFICATION_2026-08-04.md:16-34 quotes Definition 2.1 Eq. (5), and the held text matches: autonomous origin/main:L7/provenance/prior-art/prior-art-lane/ru99.txt:117 "[source text withheld from the public copy]| + αβ >" (operator glyph garbled in the extraction) and :121 "[source text withheld from the public copy] repository's own label is "ESTABLISHED" (:33, :213).
        - **λ = 0 radius.** ru99.txt:165-172 reads "[source text withheld from the public copy]". The repository's label is "EXTERNALLY VERIFIED for sign-definite operands" (ROADMAP record :70) and "VERIFIED — the author is right" (:214).
        - **λ = 0 as coded.** ROADMAP:L8/L5/research/review/EBSTACK_LAMBDA_ANALYSIS.md:60-81 says "It is not an enclosure." and reports 1898/20000 containing.
        - **Probe re-run.** I ran a scratch copy of ROADMAP:L8/L4/work/computation/probes/ebstack_lambda_analysis.py on 2026-11-11 with python3 -I. It gave λ=0 → [3,25] against truth [5,27], containment False; λ=1 contains 20000/20000; λ=0 contains 1898/20000 (9.49%). All figures match the record.

        **Why it is corrected, not standing**
        1. **"All three records are on ROADMAP only" is true of the files, not of the results.**
           - The three files are absent from the MAIN and BETA trees. They are on ROADMAP because commit 62d2e3f (2026-09-14) restored them, and their blobs are byte-identical to HISTORY 1d83788:intake/research/.
           - MAIN and BETA state the λ = 0 result at L7/provenance/sources/staging-records/interval/DECORATIONS_2026-08-04.md:77: "[source text withheld from the public copy]".
           - MAIN:L8/L1/state-space/AUDITON_ENVELOPE.md:126 binds C3 to the "λ=1 linear form".
           - The companion repository records all three results on its merged state, at autonomous origin/main:L8/L5/research/findings/FINDING_lambda_enclosure_boundary.md:38-51 and :180-195 (also on its beta). That finding is internal and labels Rump "NOT-CHECKED" (:134).
           - The Rump text used for the external check is held in autonomous origin/main, not on ROADMAP.
        2. **"Always encloses" holds only in exact arithmetic.** Rump's isotonicity for Eq. (5) is over the reals, and the probe uses exact rationals. For floating point Rump gives a different algorithm with rounding terms: ru99.txt:384-385 "[source text withheld from the public copy]", then Algorithm 3.2 at :411-415. The quoted code is float-typed, and no record checks enclosure for it under rounding.
        3. **"As coded" rests on a quotation, not on the repository.** EBSTACK_LAMBDA_ANALYSIS.md:37 says "[source text withheld from the public copy]"; eb-stack was never cloned (:10-27). The record's own label is "INTERNALLY DERIVED" (:3).
        4. **"Is not an enclosure" has a degenerate exception.** My scratch check on the probe's own sample shows the 1898 passing cases are exactly those where one radius is zero; all 18102 cases with both radii nonzero fail.

        **Smaller precision points**
        - The centre shift is the record's derivation, not Rump 1999's words. Rump gives the endpoints (a−α)(b−β) and (a+α)(b+β), from which the centre ab + αβ follows. My scratch check found the shifted form exact on 11722 of 11722 sign-definite cases.
        - Rump's case i is literally A ≥ 0, B ≥ 0; other sign combinations follow from the symmetry at ru99.txt:159-160.
        - The Rump 2010 quotation in the record (:75-78) could not be confirmed: no Rump 2010 text is held in either repository.
        - The record's own limits (:232-240) say "the adversarial refutation pass was still running ... Verdicts may move" and "Nothing here is adopted." I found no later record of that pass's outcome for λ.

        **Counter-evidence the claim does not cite**
        - Two adjacent records call λ = 1 "exact": ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:252 "λ = 1 the exact interval-product radius", and autonomous origin/main FINDING_lambda_enclosure_boundary.md:33. Rump Theorem 2.4 (ru99.txt:141-157, ρ ≤ 1.5) and the record's own Result 2 contradict that wording.
        - MAIN:L8/L4/work/writing/sessions/SESSION_2026-08-05_AUDITON_ARCHITECTURE.md:388-402 carries the owner's statement "lambda 0 DOES MAKE an enclosure claim". The session scopes it as "over decisions, not intervals" and marks it falsifiable; no test is recorded.

        **Evidence states I assign**
        - λ = 1 identity and real-arithmetic enclosure: EXTERNALLY CHECKED.
        - λ = 0 radius exactness on sign-definite operands: EXTERNALLY CHECKED; the centre shift is INTERNALLY CHECKED.
        - λ = 0 unshifted non-enclosure: INTERNALLY CHECKED.
        - Whether the quoted line is eb-stack's shipping code: UNRESOLVED.
        - Floating-point enclosure of the coded λ = 1: UNRESOLVED.
        - λ = 1 called "exact" in the vocabulary paper and the autonomous finding: CONTRADICTED.
      - **corrected_statement**: The lambda results that stand, with their conditions: (1) λ = 1 is Rump's 1999 midpoint-radius product (Definition 2.1, Eq. (5)); it encloses the true product in real or exact-rational arithmetic (repository label: ESTABLISHED) and is not the exact radius (overestimation up to 1.5×, Rump Theorem 2.4). Enclosure of the float-typed code under rounding is not checked; Rump's floating-point Algorithm 3.2 adds rounding terms. (2) The λ = 0 radius aβ + αb [source text withheld from the public copy] for sign-definite operands ([source text withheld from the public copy], A ≥ 0 and B ≥ 0, other signs by symmetry; repository label: EXTERNALLY VERIFIED). It yields the exact interval only when paired with the centre shifted to ab + sgn(ab)·αβ; that shift is the repository's derivation, internally checked, not Rump 1999's wording. (3) λ = 0 with the centre left at a·b fails to enclose whenever both radii are nonzero (label: INTERNALLY DERIVED; probe re-run 2026-11-11 reproduces [3,25] against [5,27] and 1898/20000, the passes being exactly the cases with a zero radius). The `mul` line tested is quoted from an author-supplied prompt and is labelled UNVERIFIED as eb-stack's actual code. Where the records sit: the three files (LAMBDA_EXTERNAL_VERIFICATION_2026-08-04.md, EBSTACK_LAMBDA_ANALYSIS.md, ebstack_lambda_analysis.py) are on ROADMAP only among the live states of aybllc/auditonomous (restored 2026-09-14, byte-identical to HISTORY 1d83788:intake/research/) and absent from MAIN and BETA. The results are not ROADMAP-only: MAIN and BETA state the λ = 0 result at L7/provenance/sources/staging-records/interval/DECORATIONS_2026-08-04.md:77, MAIN binds "λ=1 linear form" at L8/L1/state-space/AUDITON_ENVELOPE.md:126, and aybllc/autonomous origin/main records all three internally at L8/L5/research/findings/FINDING_lambda_enclosure_boundary.md (Rump NOT-CHECKED there) and holds the Rump 1999 text. The external-verification record's own limits remain open: "adversarial refutation pass was still running ... Verdicts may move" and "Nothing here is adopted."
      - **evidence_checked**
        - MAIN:L8/L5/research/review/STATUS_LADDER.md and STATUS_AND_LABEL_DISCIPLINE.md (read for the repository's labels)
        - ROADMAP:L8/L5/research/review/LAMBDA_EXTERNAL_VERIFICATION_2026-08-04.md:1-240 (cited :16-71, :213-214 confirmed; limits at :232-240)
        - autonomous origin/main:L7/provenance/prior-art/prior-art-lane/ru99.txt:65-70, 117, 121, 141-172, 384-415 (Eq. (5), isotonicity, Theorem 2.4, case i, floating-point Algorithm 3.2)
        - autonomous origin/main:L7/provenance/prior-art/prior-art-lane/0.md (holdings: Rump 1999 only, no Rump 2010)
        - ROADMAP:L8/L5/research/review/EBSTACK_LAMBDA_ANALYSIS.md:1-141 (cited :60-81 confirmed; UNVERIFIED source line at :37; label at :3)
        - ROADMAP:L8/L4/work/computation/probes/ebstack_lambda_analysis.py (read, then a scratch copy run with python3 -I on 2026-11-11: [3,25] vs [5,27], 20000/20000, 1898/20000)
        - Own scratch check /tmp/claude-0/-home-user/bfcfd013-a2da-5019-961e-7f46116f08be/scratchpad/wf-handle/kc04/check.py: 1898 passes all have a zero radius; 18102 nonzero-radius cases all fail; shifted form exact on 11722/11722 sign-definite cases
        - git ls-tree on auditonomous origin/main, origin/beta/7lm-exemplar-auditonomous, ROADMAP and 1d83788 for lambda/Rump filenames (files only on ROADMAP and HISTORY intake/research/)
        - git rev-parse blob comparison 1d83788:intake/research/{EBSTACK_LAMBDA_ANALYSIS.md, LAMBDA_EXTERNAL_VERIFICATION_2026-08-04.md, ebstack_lambda_analysis.py} vs ROADMAP paths (identical); git log shows restore commit 62d2e3f 2026-09-14
        - MAIN and BETA:L7/provenance/sources/staging-records/interval/DECORATIONS_2026-08-04.md:77, 114
        - MAIN:L8/L1/state-space/AUDITON_ENVELOPE.md:126
        - MAIN:L8/L4/work/writing/sessions/SESSION_2026-08-05_AUDITON_ARCHITECTURE.md:384-402
        - autonomous origin/main:L8/L5/research/findings/FINDING_lambda_enclosure_boundary.md:1-218 (also present on origin/beta/7lm-exemplar-autonomous and origin/claude/scholarly-pair-baseline-k8ap82)
        - ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:252, 296
        - ROADMAP:L8/L5/research/review/LAMBDA_PRIOR_ART_2026-08-05.md:169 and grep for 'adversarial refutation' across ROADMAP (no later lambda refutation outcome found)
        - git grep on MAIN and BETA for LAMBDA_EXTERNAL_VERIFICATION, EBSTACK_LAMBDA_ANALYSIS, ebstack_lambda_analysis (no references)
    - item 5
      - **claim**: Two searches the work depends on were never run: the prior-art search for the coinage and its definition, and the search, queued on 16 August 2026, on whether any codified definition of autonomous entails recoverable records. What exists is a string search over the eleven definitions, which found no record or audit term.
      - **id**: KC-05
      - **verdict**: corrected
      - **reasoning**: Every cited locator reads as quoted, but the claim's first half is wrong in fact: a prior-art search for the coinage was run and recorded, and the "unrun" lines it cites are stale labels.

        **Part 1, prior-art search "never run": CONTRADICTED.**
        - **The search record exists in history.** aybllc/autonomous commit e1b3cb0 (2026-08-08, an ancestor of origin/main) added `auditonomous/research/PRIOR_ART_SEARCH_2026-08-08.md`, 260 lines. It logs 13 web probes (P1–P13) and 9 GitHub probes (G1–G9), finds four hits (H1–H4), and gives a verdict at lines 250–251: "search run 2026-08-08; coinage not superseded; lexical novelty refuted; definitional novelty unrefuted."
        - **It was removed, not refuted.** Commit ab8f01f (2026-08-14) deleted it with the whole `auditonomous/` directory ("removed on instruction"). The file is in no current tree of either repository; it is readable at autonomous ab8f01f^ (d124fa2). The commit message's "recoverable at 96b6382" is wrong for this file: I checked, and it is absent there.
        - **Its verdict survives on merged main.** aybllc/autonomous origin/main:L8/L6/history/HUB_SURVEY_2026-08-14.md:951-970 quotes the verdict, and line 1219 lists it again.
        - **The stale lines were never amended.** AUDITONOMY.md still read "No prior-art search has been run" at autonomous ab8f01f^ line 276, six days after the search, and the same sentence is carried at ROADMAP:AUDITONOMY.md:263. DISTILLATION.md:134 ("still unrun") was written 2026-08-05 and never updated; MAIN:L7/provenance/prior-art/0.md:32 and L7/provenance/0.md:36 repeat it.
        - **ROADMAP contradicts itself.** SPINE_v0.1_2026-08-14.md:93-94 cites `PRIOR_ART_SEARCH_2026-08-08.md` by name with the same verdict. WALK_ACROSS_repo-instrument-standards_2026-08-05.md:42 (X15) records "Prior-art searches run 2026-08-05" and downgrades the condition to "PARTIALLY CHECKED — negative". The roadmap's ch07 file and BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:168-170, 504 carry the 2016 and 2018 leads while still saying "run the prior-art search".
        - **A lexical search is on MAIN itself.** PERPETUITY_QUESTION_ADJUDICATION.md:91-100 (2026-08-02, also on ROADMAP and BETA) records zero occurrences in SpringerLink, PubMed, Europe PMC, Crossref and Google Scholar, and zero in Google Patents (labelled PARTIALLY VERIFIED). It also records the 2018 blog as defeating "absolute lexical novelty of the noun".
        - **What is true:** `L7/provenance/prior-art/` is EMPTY in all three states (rules only). No search is recorded there, and none against publisher-of-record or standards hosts; the 2026-08-08 record lists those routes as egress-blocked.

        **Part 2, auditability-gap search queued 2026-08-16 and not run: CONFIRMED, with an omission.**
        - The phrase occurs exactly once per state, at LEDGER_2026-08-16_l6-close-and-normalization.md:48, as item 3 of "Next Required Check". It has no hits in the three autonomous refs.
        - Only item 1 of that queue is marked answered (MAIN:L8/L6/history/0.md:36).
        - Two unmerged papers say it "has not been run": autonomous scholarly-pair AUTONOMOUS_BASELINE_PAPER_2026-09-14.md:122 and ROADMAP vocabulary paper:306.
        - The claim omits that line 48 itself names existing partial evidence: "5 read IEEE standards; the retired F-003 30-PDF sweep".

        **Part 3, the string search: CONFIRMED, but the locator is imprecise.**
        - The search is a repository record, not only a reader's re-run. It is dated 2026-09-14 and labelled "[source text withheld from the public copy]" at autonomous scholarly-pair AUTONOMOUS_BASELINE_PAPER_2026-09-14.md:118, and carried as claim 17 at ROADMAP vocabulary paper:306. Neither is on any main.
        - I re-ran it over the eleven Verbatim cells at autonomous origin/main AUTONOMOUS.md:70-80. There were no hits for [source text withheld from the public copy], recover-, provenance, attest-, report or document. "oversight" occurs in A2, A3, A9 and A11.
        - Three rows weaken "eleven definitions": A9's cell is part paraphrase, A10 defines "autonomic", and A3 is marked not re-verifiable.
      - **corrected_statement**: Of the two searches the work depends on, one was run and its record then dropped; the other was never run.

        (1) Prior-art search for the coinage: CONTRADICTED as "never run". A search was run on 2026-08-08 and recorded in aybllc/autonomous at commit e1b3cb0 as `auditonomous/research/PRIOR_ART_SEARCH_2026-08-08.md` (260 lines; 13 web probes and 9 GitHub probes; verdict "search run 2026-08-08; coinage not superseded; lexical novelty refuted; definitional novelty unrefuted"). The file was deleted on 2026-08-14 at ab8f01f and is in no current tree of either repository; it is readable at autonomous ab8f01f^. Its verdict survives on merged autonomous origin/main at L8/L6/history/HUB_SURVEY_2026-08-14.md:951-970 and is cited by name at ROADMAP:L8/L5/research/review/SPINE_v0.1_2026-08-14.md:93-94. Earlier partial searches are also on record: a scholarly-index and patent zero-occurrence search of 2026-08-02 (MAIN, ROADMAP and BETA: L8/L5/research/review/PERPETUITY_QUESTION_ADJUDICATION.md:91-100, which also records the 2018 blog as defeating lexical novelty of the noun), and a standards-index and web search of 2026-08-05 (ROADMAP: WALK_ACROSS_repo-instrument-standards_2026-08-05.md:42, "PARTIALLY CHECKED — negative"). The repository's own "unrun" labels are stale and were never amended after the search: ROADMAP:AUDITONOMY.md:263 "[source text withheld from the public copy]"; DISTILLATION.md:134 "still unrun" (written 2026-08-05); MAIN:L7/provenance/prior-art/0.md:32. What is still true: the prior-art position L7/provenance/prior-art/ is EMPTY in all three states, and no search against publisher-of-record or standards hosts is recorded (the 2026-08-08 record lists those routes as blocked). The 2026-08-08 search's finding is that the word is not new (a domain expired in 2016, a 2018 blog, a July 2026 agent-skill name) while no located source carries the definition.

        (2) Auditability-gap search: UNRESOLVED, never run. It was queued on 2026-08-16 as item 3 of "Next Required Check" at MAIN:L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:48, which is the only occurrence of the phrase in MAIN, ROADMAP and BETA. No record of it being run exists in any state of either repository, and two unmerged papers say it "has not been run". The same ledger line names existing partial evidence that "must not be overextended": "5 read IEEE standards; the retired F-003 30-PDF sweep".

        (3) What exists in its place is a string search dated 2026-09-14 over the eleven Verbatim cells of aybllc/autonomous L8/L0/semantics/definitions/AUTONOMOUS.md:70-80. It is recorded only in two unmerged papers: autonomous origin/claude/scholarly-pair-baseline-k8ap82:L8/L4/work/writing/papers/AUTONOMOUS_BASELINE_PAPER_2026-09-14.md:118, and ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:306. It found no [source text withheld from the public copy] or memory term, and a re-run on autonomous origin/main confirms this. The only adjacent word is "oversight", in A2, A3, A9 and A11. The finding is bounded to those eleven texts, of which A9's cell is part paraphrase, A10 defines "autonomic", and A3 is marked not re-verifiable.
      - **evidence_checked**
        - ROADMAP:L8/L0/semantics/definitions/AUDITONOMY.md:262-263 — "**[source text withheld from the public copy]`." (confirmed verbatim; file absent from MAIN and BETA)
        - MAIN:L7/provenance/prior-art/0.md:32 — "No prior-art search has been run (\"search still unrun\", `L8/L5/research/findings/DISTILLATION.md` §5); the record is empty." (confirmed; identical on ROADMAP and BETA)
        - MAIN:L7/provenance/0.md:36 — "the prior-art rules; the search itself has not been run."
        - MAIN:L8/L5/research/findings/DISTILLATION.md:6,134 — "Written 2026-08-05"; "prior-art search **still unrun**" (predates the 2026-08-08 search; never amended)
        - MAIN:L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:5,44,48 — dated 2026-08-16; item 3 of "Next Required Check": "**The auditability-gap search** (bounded, cross-repo)... Existing partial evidence (5 read IEEE standards; the retired F-003 30-PDF sweep) must not be overextended."
        - git grep -i 'auditability-gap' and 'auditability gap' over MAIN, ROADMAP, BETA: exactly one hit per state (the ledger line 48); zero hits in aybllc/autonomous origin/main, origin/beta/7lm-exemplar-autonomous, origin/claude/scholarly-pair-baseline-k8ap82
        - MAIN:L8/L6/history/0.md:36 — only "Item 1 of the 2026-08-16 queue (the authority-interface register) is answered"; nothing on item 3
        - aybllc/autonomous e1b3cb0:auditonomous/research/PRIOR_ART_SEARCH_2026-08-08.md:1-9,66-100,219-251 — "This record runs that search."; probes P1–P13, G1–G9; "search run 2026-08-08; coinage not superseded; lexical novelty refuted; definitional novelty unrefuted."
        - aybllc/autonomous git log: file added e1b3cb0 (2026-08-08, "land the auditonomy prior-art search record"), deleted ab8f01f (2026-08-14, "auditonomous/ removed on instruction (23 files, recoverable at 96b6382)"); both commits are ancestors of origin/main; file present at ab8f01f^ (d124fa2), absent at 96b6382 and from all three current autonomous refs; no such file ever added in aybllc/auditonomous (git log --all)
        - aybllc/autonomous origin/main:L8/L6/history/HUB_SURVEY_2026-08-14.md:951-970,1219 — "## 5.4 The prior-art record on the coinage — book-critical"; quotes the verdict; "The prior-art search on the coinage, with \"lexical novelty refuted, definitional novelty unrefuted.\""
        - aybllc/autonomous ab8f01f^:auditonomous/definitions/AUDITONOMY.md:276 — still "No prior-art search has been run" after the search (stale); ab8f01f^:auditonomous/DISTILLATION.md:134 likewise
        - ROADMAP:L8/L5/research/review/SPINE_v0.1_2026-08-14.md:93-94 — "[source text withheld from the public copy]`" (also at HISTORY 1d83788:manuscripts/SPINE_v0.1_2026-08-14.md:94; not on MAIN or BETA)
        - ROADMAP:L8/L5/research/review/WALK_ACROSS_repo-instrument-standards_2026-08-05.md:42 — "[source text withheld from the public copy]"; "PARTIALLY CHECKED — negative"
        - MAIN, ROADMAP, BETA:L8/L5/research/review/PERPETUITY_QUESTION_ADJUDICATION.md:91-100 — "[source text withheld from the public copy]... PubMed... Europe PMC REST... Crossref API... Google Scholar"; "[source text withheld from the public copy]"
        - ROADMAP:L8/L6/retired/consolidated-2026-08-04/AUDITONOMOUS.md:847-867 — §[source text withheld from the public copy]"
        - ROADMAP:L8/L4/work/writing/book/ch07-we-introduce-auditonomy-a-definition-not-a-lexeme.md:11,16,22 and ROADMAP:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:165-170,504 — "(search unrun)"; "[source text withheld from the public copy]"; "Next: run the prior-art search" (carries the search's results while labelling it unrun)
        - ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:281,306 — claim [source text withheld from the public copy]"
        - aybllc/autonomous origin/claude/scholarly-pair-baseline-k8ap82:L8/L4/work/writing/papers/AUTONOMOUS_BASELINE_PAPER_2026-09-14.md:118-122 — "[source text withheld from the public copy]... Hits: none"; "[source text withheld from the public copy]" (paper absent from autonomous origin/main and beta)
        - Re-run by me: python3 -I script over the Verbatim cells of aybllc/autonomous origin/main:L8/L0/semantics/definitions/AUTONOMOUS.md:70-80 (copied from the git object to /tmp/claude-0/-home-user/bfcfd013-a2da-5019-961e-7f46116f08be/scratchpad/wf-handle/KC-05/) — zero hits for 18 record/audit stems in all eleven rows; "oversight" in A2, A3, A9, A11
        - MAIN:L8/L6/history/LEDGER.md:39 — "`[source text withheld from the public copy]"; ls-tree of L7/provenance/prior-art/ in MAIN, ROADMAP, BETA shows only 0.md and README.md
    - item 6
      - **claim**: The source ledger has 60 rows, not 62, all pointers into a private archive no reader could open. Its label VERIFIED records that a file matches the archive copy, not that a claim was checked. A record of reading exists for 14 of the 58 held sources. The definition's own external citations have no rows.
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
    - item 7
      - **claim**: Auditonomous takes “autonomous” from one object: the Autonomous entry at commit 0504961 of 14 August 2026. Its bytes are unchanged on Autonomous main today. It is a plural entry of eleven definitions from nine bodies that declines to state a single definition, its own review blocks its gate pending seven fixes, and no consensus baseline exists.
      - **id**: KC-07
      - **verdict**: corrected
      - **reasoning**: Most of the claim is confirmed from the git objects; four parts are imprecise or rest on a locator that does not say what it is cited for.

        CONFIRMED
        - Binding. MAIN:L7/peering/public/ingress/peer-1/0.md:10 carries the owner's sentence "Auditonomous gets the definitions of autonomous from Autonomous and nowhere else. — owner, 2026-09-05". MAIN:.../object-1/0.md:13 reads "[source text withheld from the public copy]". Line 10 names the object `aybllc/autonomous:research/definitions/AUTONOMOUS.md`.
        - Date. Commit 050496161a848ea26492b8468e59afc7e0c07282 is dated 2026-08-14 18:56:51 -0700, which is 2026-08-15 01:56:51 UTC. "14 August" holds in the author's timezone only.
        - Bytes. I recomputed [source text withheld from the public copy], 315 lines. It is identical at 0504961:research/definitions/AUTONOMOUS.md and at Autonomous origin/main (c9076c3):L8/L0/semantics/definitions/AUTONOMOUS.md. It is also identical on Autonomous beta e64b382 and on 9b49910. The path differs between the pin and main; the bytes do not.
        - Plural entry. Lines 24-25 of the [source text withheld from the public copy]." Lines 70-80 hold eleven rows, A1 to A11.
        - Review. Autonomous origin/main:L8/L5/research/review/REVIEW_4_AUTONOMOUS_ADJUDICATION.md:451: "[source text withheld from the public copy]." Lines 458-466 list seven fixes (i) to (vii). The same blob is already present at commit 5a32fea (2026-08-08), so none of the seven fixes has been applied. I found no delta re-review and no CLEARS record on Autonomous main.

        IMPRECISE OR OVERSTATED
        1. "Takes 'autonomous' from one object" is the owner's rule and the binding, not confirmed practice on MAIN. MAIN:object-1/0.md:34 records: "Three files at HEAD still take a definition of *autonomous* from somewhere other than this [source text withheld from the public copy]). MAIN:L8/L6/history/harmonization-2026-09-05.md:93 leaves them open, and 7lm origin/main specification:958 repeats this under "Not yet as stated". I confirmed all three exist on MAIN (AUDITONOMOUS_DEFINITION.md:263, REQUIREMENTS_OWNERSHIP.md:268, CONTRADICTIONS.md:36-37). Only BETA (unmerged) says they "now carry explicit receiving-use dispositions" (BETA:object-1/0.md:36). BETA also adds a second ingress object from the same peer, object-2, which is a result handoff and not a definition.
        2. "Nine bodies" is a count no document makes. The entry's own headline says "[source text withheld from the public copy]" (line 39). REVIEW_4 F10 (lines 51, 299-306) calls that count [source text withheld from the public copy] Body column has ten distinct strings; the Auditonomous binding (MAIN:object-1/0.md:28) names eight organisations. Nine is reached only by merging the two IEEE rows while keeping the three ISO committees apart.
        3. "Eleven definitions" needs a caveat. A10 defines "autonomic", which the entry calls "a different word" (line 79). The entry's own §6 says "the ten above" and "A1…A10" (lines 244, 246), which is REVIEW_4 F4.
        4. "Blocks its gate" misnames the gate. It is the C-001 gate of RULINGS.md (opening "[source text withheld from the public copy]", REVIEW_4:9-10), not a gate belonging to the entry. The review blocks the prerequisite only: "[source text withheld from the public copy]" (line 469). The review is a single internal reviewer with "External Sources Checked: NONE" (line 503).
        5. "No consensus baseline exists" is not what the cited locator says. MAIN:L8/L0/0.md:79 only quotes the specification's requirement ("state and freeze the narrowest reasonable agreement…"; "Auditonomous consumes the pinned Autonomous consensus baseline"). On merged states the absence is confirmed by search only: a grep for "consensus baseline" and "narrowest reasonable agreement" across every ref of the three repositories returns only the requirement text. The explicit statement exists only on unmerged branches:
           - Autonomous beta e64b382:L8/L0/0.md:105: "a plural A1–A11 entry, not a demonstrated common consensus baseline".
           - Autonomous beta:L8/L5/research/review/BETA_SOURCE_OVERLAY.md:11: "[source text withheld from the public copy]."
           - Auditonomous BETA:L8/L0/0.md:81: "a complete consensus-plus-local-delta result is not claimed".
           - 7lm beta 97314c5:L7/0.md:190: "a research obligation, not an assertion that agreement has been established".
           The "baseline paper" on the closed-PR branch 9b49910 is a draft composition over the plural entry and states no narrowest-agreement baseline.

        ADDITIONAL CONTRADICTION NOT CITED
        Autonomous origin/main:L8/L0/semantics/definitions/REGISTER.md:19 [source text withheld from the public copy]", while the entry at line 24 says ADOPTED. Only the unmerged Autonomous beta corrects the register.

        EVIDENCE STATE (mine)
        - Byte identity: INTERNALLY CHECKED.
        - Single-source rule: ASSERTED by the owner, and CONTRADICTED in practice on MAIN by the three recorded files.
        - Gate: UNRESOLVED (blocked, seven fixes unapplied).
        - Consensus baseline: EMPTY (required by the specification, not produced).
      - **corrected_statement**: By [source text withheld from the public copy] and the binding at MAIN:L7/peering/public/ingress/peer-1/object-1/, Auditonomous is to take "autonomous" from one object: aybllc/autonomous:research/definitions/AUTONOMOUS.md at commit 0504961 (2026-08-14 18:56 -0700, which is 2026-08-15 UTC). MAIN's own binding record says three files still take a definition of autonomous from elsewhere ([source text withheld from the public copy]); only the unmerged BETA claims dispositions for them. The pinned bytes (blob ffbdc28, SHA-256 2756661749c3…a12b, 22,735 bytes) are unchanged on Autonomous main today at the new path L8/L0/semantics/definitions/AUTONOMOUS.md, and also on the Autonomous beta and closed PR #29 branches. The object is a plural entry of eleven rows, A1 to A11, that declines to state a single definition. Its headline says "Six Tier-1 bodies"; its own review counts 8 to 10 depending on grouping; no document says nine. Row A10 defines "autonomic", which the entry calls a different word, and the entry's own §6 still says "the ten above". Autonomous's internal adversarial review of 2026-08-08 (REVIEW_4) "[source text withheld from the public copy] a seven-item fix set. None of the seven is applied, since the blob predates the review, and the gate declaration is reserved to the owner. The Seven-Layer Model specification requires an Autonomous "consensus baseline", and none is found in any ref of the three repositories. On merged states this is confirmed by absence only: MAIN:L8/L0/0.md:79 states the requirement, not the absence. The explicit statement "[source text withheld from the public copy]" exists only on the unmerged Autonomous beta (e64b382), echoed by Auditonomous BETA and the 7lm beta. Autonomous main's REGISTER.md still lists "autonomy / autonomous" as not yet entered, contradicting the entry's ADOPTED status.
      - **evidence_checked**
        - MAIN:L8/L5/research/review/STATUS_LADDER.md and STATUS_AND_LABEL_DISCIPLINE.md (read for labels)
        - MAIN:L7/peering/public/ingress/peer-1/0.md:10,12,20,22 (owner's rule; only-source statement; holdings)
        - MAIN:L7/peering/public/ingress/peer-1/object-1/0.md:10,13,28,34 (object identity research/definitions/AUTONOMOUS.md; version 0504961; eight named bodies; three files still departing from the binding)
        - MAIN:L8/L0/0.md:79,98 (spec requirement of a consensus baseline quoted; rule restated; no statement that a baseline is absent)
        - MAIN:L8/L6/history/harmonization-2026-09-05.md:11,93 (three departures left as open owner decisions)
        - MAIN:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:263; MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:268; MAIN:L8/L5/research/review/CONTRADICTIONS.md:36-37 (the three departures exist)
        - ROADMAP (9259c18): L7/peering/public/ingress/peer-1/ unchanged from MAIN (git diff --stat shows no change there)
        - BETA (714480d):L7/peering/public/ingress/peer-1/object-1/0.md:13-19,36; object-2/0.md and binding.json; L8/L0/0.md:81; L7/provenance/sources/LEDGER.md:153 (AUT-SOURCE-001, same blob and SHA-256); L8/L0/semantics/AUDITONOMOUS_BETA_SCOPE.md
        - autonomous 0504961: git log -1 (050496161a848ea26492b8468e59afc7e0c07282, 2026-08-14 18:56:51 -0700, 'Update RULINGS.md'); ancestor of origin/main c9076c3
        - autonomous blob ffbdc28be7b47a83c9354526ac034596ba7b6e9a: sha256sum recomputed = 2756661749c3e322d3c13abc5104cb8d7b4d07203905611c4ec5196b9aa1a12b, 22,735 bytes, 315 lines, at 0504961:research/definitions/AUTONOMOUS.md, origin/main:L8/L0/semantics/definitions/AUTONOMOUS.md, e64b382 and 9b49910 (same path); same blob at 5a32fea/b0ef129/c866842:definitions/AUTONOMOUS.md
        - autonomous origin/main:L8/L0/semantics/definitions/AUTONOMOUS.md:24-25, 38-39, 70-80, 79, 244-247 (plural entry; 'Six Tier-1 bodies'; eleven rows; A10 'a different word'; 'the ten above', 'A1…A10')
        - autonomous origin/main:L8/L5/research/review/REVIEW_4_AUTONOMOUS_ADJUDICATION.md:1-34, 42-56, 299-306, 433-471, 503, 517-520 (15 findings; F10 8-10 bodies; [source text withheld from the public copy]; seven fixes; declaration is Eric's; no external sources checked)
        - autonomous origin/main:L8/L0/semantics/definitions/REGISTER.md:10-19 ('autonomy / autonomous' under 'Not yet entered')
        - autonomous origin/main:L7/peering/public/egress/peer-1/object-1/0.md:10-15; L7/peering/public/egress/0.md:37
        - autonomous origin/main: grep for CLEARS / delta re-review / REVIEW_4 (no later clearing record; L8/L6/history/LEDGER.md:813 and HUB_SURVEY_2026-08-14.md:793 repeat the block)
        - autonomous origin/beta/7lm-exemplar-autonomous (e64b382):L8/L0/0.md:105; L8/L5/research/review/BETA_SOURCE_OVERLAY.md:3,11; L8/L0/semantics/definitions/BETA_SCOPE.md; REGISTER.md diff; L7/peering/public/egress/peer-1/object-2/
        - autonomous origin/claude/scholarly-pair-baseline-k8ap82 (9b49910):L8/L4/work/writing/papers/AUTONOMOUS_BASELINE_PAPER_2026-09-14.md:1-120 and grep for baseline/consensus; L8/L6/history/exemplar-2026-09-14.md
        - git grep -i 'consensus baseline|narrowest reasonable agreement' over auditonomous MAIN/ROADMAP/BETA, autonomous main/beta/scholarly branch, 7lm main/beta (only requirement text, plus the beta negatives)
        - 7lm origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:42,44,958; 7lm origin/beta/common-contracts-r1-r6:L7/0.md:190
    - item 8
      - **claim**: The research is split across three branches that do not contain one another. MAIN holds 169 files, ROADMAP 328, BETA 186. The second definition, the lambda thread, the docket, the author assertions, four findings, the probes, the corpus and the roadmap are on ROADMAP only, and MAIN's own records cite files MAIN does not hold.
      - **id**: KC-08
      - **verdict**: corrected
      - **reasoning**: Most of KC-08 is confirmed from the git objects, but two parts are overstated and one cited figure does not reproduce.

        **Confirmed**
        - File counts: `git ls-tree -r --name-only | wc -l` gives MAIN (2165144) 169, ROADMAP (9259c18) 328, BETA (714480d) 186.
        - Ancestry: MAIN is an ancestor of both branches; neither branch is an ancestor of the other; their merge-base is 2165144.
        - ROADMAP-only by path (absent from the MAIN and BETA trees):
          - second definition: `L8/L0/semantics/definitions/AUDITONOMY.md` (ROADMAP:3, "[source text withheld from the public copy])")
          - docket: `L8/L5/research/review/RESEARCH_DOCKET.md`
          - author assertions: `L8/L5/research/review/AUTHOR_ASSERTIONS.md`
          - four findings: `AUDITON_PACKABILITY_2026-08-04.md`, `AUTONOMY_AT_DISTANCE.md`, `OMMP_ATTACHMENT_GAP_2026-08-04.md`, `UHA_AS_MAP_2026-08-04.md`
          - probes: `L8/L4/work/computation/probes/` (8 scripts and a sheet)
          - corpus: `L8/L4/work/writing/manuscript/` (Block_01 to Block_52, Master Archive, TOC)
          - roadmap: `L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md`
        - All five cited locators say what the claim says, and each target is absent from MAIN and present on ROADMAP:
          - MAIN:CONTRADICTIONS.md:10 — "[source text withheld from the public copy]"
          - MAIN:CONTRADICTIONS.md:46 — "[source text withheld from the public copy]"
          - MAIN:REQUIREMENTS_OWNERSHIP.md:19 — "(`intake/research/AUDITON_PACKABILITY_2026-08-04.md:15`)"; ROADMAP line 15 of that finding reads "78 requirements extracted, 46 definitions captured"
          - MAIN:OVERRIDE_NECESSITY_2026-08-04.md:14 — "(`RESEARCH_DOCKET.md:34`)"; ROADMAP docket line 34 reads "[source text withheld from the public copy].**"
          - MAIN:OVERRIDE_NECESSITY_2026-08-04.md:169 — "`ARCH:364`"; ARCH is defined at MAIN:L8/L5/research/lanes/THEME_LEDGER.md:9 as the Master Archive, and ROADMAP Master Archive line 364 carries "no watcher goes unwatched"
        - Further MAIN citations of absent files, not cited by the claim: MAIN:L8/L1/state-space/AUDITON_ENVELOPE.md:76 and :253, and MAIN:L8/L5/research/findings/DISTILLATION.md:21 and :261, all citing `definitions/AUDITONOMY.md`.

        **Wrong or imprecise**
        1. "Three branches that do not contain one another" is overstated. ROADMAP contains MAIN: all 169 MAIN paths are present (0 missing), 17 differ in content (all `0.md` sheets), and 159 are added. BETA descends from MAIN: it keeps 163 MAIN paths (33 modified), renames 6 (`L7/publications/*` to `L7/allications/publications/*`, `L7/governance/restrictions/0.md` to `L7/governance/controlled/0.md`) and adds 17. Only ROADMAP and BETA fail to contain each other: 165 ROADMAP paths are absent from BETA and 23 BETA paths are absent from ROADMAP.
        2. "The lambda thread … on ROADMAP only" is overstated. The thesis and its check records are ROADMAP-only: `THESIS_lambda_decomposed_record.md`, `LAMBDA_EXTERNAL_VERIFICATION_2026-08-04.md`, `LAMBDA_PRIOR_ART_2026-08-05.md`, `EBSTACK_LAMBDA_ANALYSIS.md`, `CONJECTURE_bit_exact_pruning.md`, `probes/ebstack_lambda_analysis.py` and two lambda prompts. But MAIN (and BETA, which inherits them) holds lambda material:
           - MAIN:L8/L4/work/computation/deep-research-auditonomous.md:1 — "[source text withheld from the public copy]"; line 79 — "[source text withheld from the public copy]:388 — "[source text withheld from the public copy]"; line 688 — an open owner's call on "λ as axiom vs. algebra semantics"
           - MAIN:L8/L3/engineering-mathematics/uncertainty/PRIORS_EXTERNAL_2026-08-04.md:120
           - MAIN:L7/provenance/sources/staging-records/interval/DECORATIONS_2026-08-04.md:77
           - MAIN:L7/peering/private/ingress/peer-2/object-1/auditonomous-departure-protocol.md:66-79 (`lambda_A`)
        3. The cited evidence figure "60 of 133 roadmap feed citations resolve on MAIN" did not reproduce. Counting the backticked citations in the 27 "- Feeds:" lines of ROADMAP:BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md §2 (the same count comes from the Feeds bullets of the 27 chapter files), I get 141 citations. Of these, 130 name a file in the ROADMAP tree, 63 a file in the MAIN tree and 62 a file in the BETA tree. Excluding the 8 that point outside the tree (aybllc/autonomous, `git:` history, scratchpad) leaves 133, of which 66 resolve on MAIN once the two directory citations and one wildcard are counted. The direction (roughly half or fewer resolve on MAIN) holds; the number 60 does not.

        **Qualifications**
        - The ROADMAP-only items are ROADMAP-only as files. MAIN's citations use old-layout names (bare filenames, `intake/research/…`), so even on ROADMAP the targets sit at different paths than cited.
        - BETA carries the same dangling citations unchanged (BETA:CONTRADICTIONS.md:10, 61; BETA:REQUIREMENTS_OWNERSHIP.md:19).
        - The counts include sheets, CI and README files, not only research.
      - **corrected_statement**: The research sits in three states, of which only two diverge. MAIN (2165144) holds 169 files and is an ancestor of both branches. ROADMAP (9259c18) holds 328: every one of MAIN's 169 paths (17 sheets changed in content) plus 159 added. BETA (714480d) holds 186: 163 of MAIN's paths (33 modified), 6 renamed and 17 added. ROADMAP and BETA do not contain each other (165 ROADMAP paths are absent from BETA; 23 BETA paths are absent from ROADMAP).

        On ROADMAP only, as files (absent from MAIN and BETA):
        - the second definition (L8/L0/semantics/definitions/AUDITONOMY.md);
        - the lambda thesis and its check records (THESIS_lambda_decomposed_record.md, LAMBDA_EXTERNAL_VERIFICATION_2026-08-04.md, LAMBDA_PRIOR_ART_2026-08-05.md, EBSTACK_LAMBDA_ANALYSIS.md, CONJECTURE_bit_exact_pruning.md, the ebstack_lambda probe and the lambda prompts);
        - the docket (RESEARCH_DOCKET.md) and the author assertions (AUTHOR_ASSERTIONS.md);
        - four findings (AUDITON_PACKABILITY, AUTONOMY_AT_DISTANCE, OMMP_ATTACHMENT_GAP, UHA_AS_MAP);
        - the eight probes, the 52-block corpus with Master Archive and TOC, and the roadmap.

        The lambda thread is not wholly ROADMAP-only. MAIN and BETA hold the deep-research run on "the λ-Decomposed Pre-Execution Record" (L8/L4/work/computation/deep-research-auditonomous.md), the session log's λ=0 section (SESSION_2026-08-05_AUDITON_ARCHITECTURE.md §7.3), PRIORS_EXTERNAL_2026-08-04.md, DECORATIONS_2026-08-04.md and the departure protocol's lambda_A.

        MAIN's own records cite files MAIN does not hold: CONTRADICTIONS.md:10 and :46, REQUIREMENTS_OWNERSHIP.md:19, OVERRIDE_NECESSITY_2026-08-04.md:14 and :169, and also AUDITON_ENVELOPE.md:76 and :253 and DISTILLATION.md:21 and :261 (citing definitions/AUDITONOMY.md). BETA inherits these dangling citations unchanged.

        Of the roadmap's feed citations, a recount gives 141 in the 27 chapter feed lines, of which 63 name a file on MAIN (62 on BETA, 130 on ROADMAP); of the 133 that point inside the repository, 66 resolve on MAIN when the two directory citations and one wildcard are counted. The figure "60 of 133" did not reproduce.
      - **evidence_checked**
        - git ls-tree -r --name-only | wc -l on origin/main (2165144) = 169, origin/claude/book-structure-roadmap-k8ap82 (9259c18) = 328, origin/beta/7lm-exemplar-auditonomous (714480d) = 186
        - git merge-base --is-ancestor: MAIN is an ancestor of ROADMAP and of BETA; ROADMAP is not an ancestor of BETA; BETA is not an ancestor of ROADMAP; merge-base of ROADMAP and BETA = 2165144
        - Path set differences (comm): MAIN minus ROADMAP = 0; ROADMAP minus MAIN = 159; MAIN minus BETA = 6; BETA minus MAIN = 23; ROADMAP minus BETA = 165; BETA minus ROADMAP = 23
        - git diff --name-status MAIN ROADMAP: 159 added, 17 modified (all 0.md sheets). MAIN to BETA: 17 added, 33 modified, 6 renamed
        - ROADMAP:L8/L0/semantics/definitions/AUDITONOMY.md:3 - "[source text withheld from the public copy])"; path absent from the MAIN and BETA trees
        - MAIN:L8/L5/research/review/CONTRADICTIONS.md:10 - "[source text withheld from the public copy]"; target only at ROADMAP:L7/provenance/sources/STANDARDS_REGISTER.md
        - MAIN:L8/L5/research/review/CONTRADICTIONS.md:46 - "[source text withheld from the public copy]"; target only at ROADMAP:L8/L5/research/findings/AUTONOMY_AT_DISTANCE.md
        - MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:19 - "(`intake/research/AUDITON_PACKABILITY_2026-08-04.md:15`)"; ROADMAP:L8/L5/research/findings/AUDITON_PACKABILITY_2026-08-04.md:15 - "[source text withheld from the public copy]."
        - MAIN:L8/L5/research/findings/OVERRIDE_NECESSITY_2026-08-04.md:14 - "[source text withheld from the public copy]`)"; ROADMAP:L8/L5/research/review/RESEARCH_DOCKET.md:34 - "[source text withheld from the public copy].**"
        - MAIN:L8/L5/research/findings/OVERRIDE_NECESSITY_2026-08-04.md:169 - "(`[source text withheld from the public copy]\"*)"; MAIN:L8/L5/research/lanes/THEME_LEDGER.md:9 - "ARCH = manuscript/Auditonomous_Theory_Master_Archive.md"; ROADMAP:L8/L4/work/writing/manuscript/Auditonomous_Theory_Master_Archive.md:364 carries the quote; file absent from MAIN
        - MAIN:L8/L1/state-space/AUDITON_ENVELOPE.md:76 and :253, MAIN:L8/L5/research/findings/DISTILLATION.md:21 and :261 cite `definitions/AUDITONOMY.md`, which MAIN does not hold (:21 - "(`definitions/AUDITONOMY.md`, governing text)")
        - Against 'lambda thread on ROADMAP only': MAIN:L8/L4/work/computation/deep-research-auditonomous.md:1 - "[source text withheld from the public copy]"; :79 - "[source text withheld from the public copy]"
        - Against 'lambda thread on ROADMAP only': MAIN:L8/L4/work/writing/sessions/SESSION_2026-08-05_AUDITON_ARCHITECTURE.md:388 - "[source text withheld from the public copy]"; :688 - "λ [source text withheld from the public copy], open"
        - Further lambda material on MAIN: L8/L3/engineering-mathematics/uncertainty/PRIORS_EXTERNAL_2026-08-04.md:120; L7/provenance/sources/staging-records/interval/DECORATIONS_2026-08-04.md:77; L7/peering/private/ingress/peer-2/object-1/auditonomous-departure-protocol.md:66-79 ("lambda_A != lambda_EB")
        - ROADMAP-only lambda files confirmed absent from MAIN and BETA: L8/L5/research/review/THESIS_lambda_decomposed_record.md, LAMBDA_EXTERNAL_VERIFICATION_2026-08-04.md, LAMBDA_PRIOR_ART_2026-08-05.md, EBSTACK_LAMBDA_ANALYSIS.md, CONJECTURE_bit_exact_pruning.md; L8/L4/work/computation/probes/ebstack_lambda_analysis.py; L8/L4/work/writing/prompts/Lambda_Explainer_Prompt.md and PROMPT_explain_lambda.md
        - ROADMAP-only confirmed by path: RESEARCH_DOCKET.md, AUTHOR_ASSERTIONS.md, the four findings, computation/probes/ (8 .py and 0.md), writing/manuscript/ (Block_01 to Block_52, Master Archive, TOC), BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md. None appears in BETA's 23 added or renamed paths
        - BETA still carries the dangling citations: BETA:L8/L5/research/review/CONTRADICTIONS.md:10 and :61; BETA:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:19
        - Feed recount (python3 -I script in scratch, over ROADMAP:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md §2 '- Feeds:' lines and the Feeds bullets of the 27 ROADMAP:L8/L4/work/writing/book/ch*.md): 141 citations; 130 resolve to a ROADMAP file, 63 to a MAIN file, 62 to a BETA file; 8 point outside the tree; 3 are directory or wildcard citations. '60 of 133' not reproduced
        - Read MAIN:L8/L5/research/review/STATUS_LADDER.md and MAIN:L8/L5/research/review/STATUS_AND_LABEL_DISCIPLINE.md first, as rule 7 requires
    - item 9
      - **claim**: The repository's own outside reading contradicts the definition's strongest sentence. Eleven sources read on 4 August 2026 claim detection, not prevention, and the adjudication of 2 August 2026 calls line 52 imprecise as written. The recommended edit is unapplied in every state, and a third file disputes the adjudication's premise.
      - **id**: KC-09
      - **verdict**: corrected
      - **reasoning**: Three of the claim's four parts are confirmed; the source count, its locator, and the way two separate records are merged are wrong.

        **Confirmed**
        - **Adjudication wording.** MAIN:L8/L5/research/review/PERPETUITY_QUESTION_ADJUDICATION.md:3 is dated 2026-08-02, and line 216 says DEF:52 "[source text withheld from the public copy]**." Line 222 gives the recommended edit, labelled "[source text withheld from the public copy]". The file is byte-identical on ROADMAP and BETA.
        - **Edit unapplied in every state.** The bullet "[source text withheld from the public copy]" stands at line 52 on MAIN and ROADMAP (file identical to MAIN) and at line 54 on BETA. BETA's diff to the definition is 16 insertions and no deletions, none touching the bullet. L8/L6/history/LEDGER.md:61 in all three states reads "recorded, not applied".
        - **Third file.** ROADMAP:L8/L5/research/review/AUTONOMOUS_vs_AUDITONOMOUS_CYCLES.md:136 reads "([source text withheld from the public copy]". That is against the adjudication's §6.1 heading "The audit itself IS post hoc" (line 201) and "the normal case, and the only case" (line 220). Neither file cites the other.

        **Wrong or imprecise**
        1. **"Eleven sources" is wrong.** The cited file is titled "[source text withheld from the public copy]" (line 1). Finding 1 rests on "Three independent literatures" (line 42) and quotes three documents: FIPS 180-4, Haber & Stornetta, RFC 6962. RFC 9162 carries the same sentence in its reading record (line 137). The six-source statement is a negative one: "[source text withheld from the public copy]." (lines 219-220). ARIES and Ferreira are used for other findings.
        2. **Where eleven comes from.** It is reached only by adding the five IEEE standards read the same day (MAIN:L7/provenance/sources/staging-records/ieee/FINDINGS_2026-08-04.md:1, "five standards read"). That file makes no detection-versus-prevention finding. Its Finding 3 quotes IEEE 7001 requiring a recorder of "**[source text withheld from the public copy]**" (line 107).
        3. **The locator is off.** Lines 12-36 of the library file are the source table and the verifier-flag notes. The detection finding is at lines 40-70 and 219-220.
        4. **The outside reading does not address the definition file or line 52.** Finding 1 is aimed at `ARCH:546` (the Git claim) and "the constitutional sentence". Its own label is "CONTESTED", and it says the [source text withheld from the public copy].**" (lines 57-70). The link to the definition's impossibility wording is by content only; no document in any state draws it.
        5. **The adjudication is a separate, earlier record.** It predates the 4 August reading by two days and rests on three different quotes (Schneier & Kelsey 1998, Crosby & Wallach 2009, Haeberlen et al. 2007; lines 212-214). Its stated defect is the record-versus-audit distinction, not prevention-versus-detection as such.
        6. **The pending edit is narrower than the claim implies.** It targets only the line-52 bullet. The same impossibility wording in sense 3 ("making concealment impossible", MAIN definition line 26) and sense 1 ("structurally unable to conceal", line 22) has no recommended edit. ROADMAP:L8/L6/retired/consolidated-2026-08-04/AUDITONOMOUS.md:713 says so for sense 3.
        7. **State of the third file.** CYCLES exists only on ROADMAP (and in HISTORY at intake/research/); it is absent from MAIN and BETA. It is dated the same day as the adjudication (line 3). It disputes only premise (ii); its verdict (i) at line 135 agrees with the adjudication that post hoc audit is not precluded. The conflict is already recorded, unranked, at ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:74 and :303 (decision D4).

        **Evidence state:** CONTRADICTED and UNRESOLVED. Repository labels: CONTESTED / NOT ADOPTED for the library finding; INTERNALLY DERIVED, pending the owner's ruling, for the edit.
      - **corrected_statement**: KC-09 (corrected): Two separate records in the repository challenge the definition's impossibility wording, and neither is adopted.

        (a) The adjudication of 2 August 2026 (MAIN:L8/L5/research/review/PERPETUITY_QUESTION_ADJUDICATION.md:201-222; identical on ROADMAP and BETA) calls the definition's line-52 bullet "imprecise as written" because "[source text withheld from the public copy]". It rests on the owner's "the udiot is always post hoc" and three external quotes it labels VERIFIED ([source text withheld from the public copy]). Its recommended edit is labelled INTERNALLY DERIVED and "Pending Eric's ruling".

        (b) The library intake read on 4 August 2026 covers six primary sources, not eleven (MAIN:L7/provenance/sources/staging-records/library/FINDINGS_2026-08-04.md:40-70 and 219-220). It finds "detection, never prevention": three literatures (FIPS 180-4, Haber & Stornetta 1991, RFC 6962, with RFC 9162 carrying the same sentence) claim detectability, and none of the six claims prevention against the record's own holder. That finding is aimed at ARCH:546 (the Git claim) and the constitutional sentence, not at the definition file or line 52. Its own label is CONTESTED, "[source text withheld from the public copy] five IEEE standards read the same day make no detection-versus-prevention finding; IEEE 7001 is quoted as requiring an independent recorder of "non-modifiable" data.

        The recommended edit is unapplied in every state: the bullet is unchanged at line 52 on MAIN and ROADMAP and at line 54 on BETA, and L8/L6/history/LEDGER.md:61 reads "recorded, not applied". It covers only that bullet; sense 3 ("making concealment impossible", line 26) and sense 1 ("structurally unable to conceal", line 22) have no recommended edit.

        A third file of the same date, present only on ROADMAP (and in HISTORY), disputes the adjudication's premise: ROADMAP:[source text withheld from the public copy]". It agrees with the adjudication that post hoc audit is not precluded (line 135). Neither file cites the other, and the conflict is carried unranked as decision D4 (ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:74 and :303).

        Evidence state: CONTRADICTED / UNRESOLVED.
      - **evidence_checked**
        - MAIN:L8/L5/research/review/STATUS_LADDER.md and MAIN:L8/L5/research/review/STATUS_AND_LABEL_DISCIPLINE.md (read for the repository's labels)
        - MAIN:L7/provenance/sources/staging-records/library/FINDINGS_2026-08-04.md:1-239 (whole file): line 1 'six primary sources'; lines 12-20 are the source table; lines 40-70 Finding 1 'detection, never prevention', CONTESTED, NOT ADOPTED; lines 219-220 'Searched for in all six'
        - MAIN:L7/provenance/sources/staging-records/library/README.md:25 'what the six sources establish'
        - MAIN:L7/provenance/sources/staging-records/ieee/FINDINGS_2026-08-04.md:1-194 (whole file): '[source text withheld from the public copy]; no detection-versus-prevention finding; line 107 IEEE 7001 'non-modifiable ... [source text withheld from the public copy]'
        - MAIN:L7/provenance/sources/staging-records/library/reading/RFC9162_Certificate-Transparency-v2.md:137 'The logs do not themselves prevent misissuance'
        - MAIN:L8/L5/research/review/PERPETUITY_QUESTION_ADJUDICATION.md:3 (date 2026-08-02), 201-222 (section 6.1, 'imprecise as written' at 216, recommended edit at 222), 306 (label row), 315-348 (failures and ledger entry); git diff shows the file identical on ROADMAP and BETA
        - MAIN and ROADMAP:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:52 (bullet unchanged; ROADMAP file identical to MAIN); also lines 22 and 26 (sense 1 'structurally unable to conceal', sense 3 'making concealment impossible')
        - BETA:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:54 (same bullet text); git diff MAIN..BETA on this file is 16 insertions, 0 deletions, none touching the bullet
        - MAIN, ROADMAP, BETA:L8/L6/history/LEDGER.md:61 '[source text withheld from the public copy].'
        - MAIN:L8/L6/retired/layout-2026-08-14/README.md:122-124 'The recommended rewording is recorded and **not applied**'
        - ROADMAP:L8/L5/research/review/AUTONOMOUS_vs_AUDITONOMOUS_CYCLES.md:3 (date 2026-08-02), 101-137 (section 6; verdicts at 135-137), 141-150; git ls-tree shows the file absent on MAIN and BETA and present in HISTORY at intake/research/AUTONOMOUS_vs_AUDITONOMOUS_CYCLES.md
        - git grep: no reference to the CYCLES file in the adjudication and no 'PERPETUITY' in the CYCLES file (neither cites the other)
        - ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:74 and :303 (conflict recorded, 'Neither file cites the other', decision D4)
        - ROADMAP:L8/L5/research/review/RESEARCH_DOCKET.md:192 (H3 'Recommended doctrine edit pending. [ERIC]')
        - ROADMAP:L8/L6/retired/consolidated-2026-08-04/AUDITONOMOUS.md:683 and :713 (DEF:52 stands unamended; no edit recommended for sense 3)
        - git grep across MAIN, ROADMAP, BETA for 'eleven sources' / '11 sources': no hits in any state
        - git grep across MAIN, ROADMAP, BETA for 'post-hoc audit examines what survived': the only live definition copy is the L8/L0 file in each state
    - item 10
      - **claim**: Three counts in the record are wrong or cannot be reproduced and would reach print: IEEE 7009 carries fifteen of the 21 envelope obligations, not sixteen; the source ledger has 60 rows, not 62; and the total of 113 requirements cannot be recounted, because the 14 NASA rows are in no file and an earlier run of 78 is unreconciled.
      - **id**: KC-10
      - **verdict**: corrected
      - **reasoning**: All three numbers in the claim are confirmed from git objects. Four parts are imprecise or true of a narrower set of states than the claim says, so the verdict is "corrected".

        **CONFIRMED**

        1. **7009 carries 15, not 16.** `MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:72` says "[source text withheld from the public copy])".
           - I recounted the table at lines 90-110: rows 1-6 are IEEE-7001 (R3, R5, R6, R7, R8, R9) and rows 7-21 are IEEE-7009 (R2-R9, R11, and six ASR rows). That is 6 + 15 = 21.
           - Line 117 says "**[source text withheld from the public copy].**" and lines 263-264 say "[source text withheld from the public copy]" and "bears 76% of the buildable requirement load". 76% is 16/21; 15/21 is 71%.
           - The file is byte-identical on ROADMAP. BETA's diff against MAIN adds only a Q13 paragraph and leaves "sixteen" and "76%" in place.
           - The IDs match the 24 IEEE-7009 headings in `MAIN:L8/L4/work/computation/ieee-requirements-for-autonomouos.md`: 15 E, 3 X (R1, R10, R12), 1 J (R13), 5 D.

        2. **The ledger has 60 rows.** `MAIN:L7/provenance/sources/LEDGER.md` lines 20-79 hold 60 register rows: PR 20, STD 34, INST 4, EXC 2, with no duplicate IDs. ROADMAP's copy is byte-identical.
           - The sheets on MAIN and ROADMAP say 62: `L7/provenance/0.md:20,33` ("62 pointer rows"), `L7/provenance/sources/0.md:10,41`, `L7/peering/private/ingress/peer-1/0.md:16`, `.../object-1/0.md:10`, and `L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:30`.
           - That last history line reads "62 rows (PR-001..020, STD-001..034, INST-001..004, EXC-001/002)"; the ranges it lists sum to 60.

        3. **Extraction files hold 55, 24 and 20 rows.** I counted 55 `### IEEE-` headings, 24 `### ISO-R` and 20 `### NIST-R` in the three MAIN files, which are identical on ROADMAP and BETA. That is 99 of 113.

        4. **The NASA rows are in no file.** `git grep` for `NASA-(R|D|Q)[0-9]+` over MAIN, ROADMAP, BETA and HISTORY returns one line: `REQUIREMENTS_OWNERSHIP.md:157`, naming only NASA-R6 and NASA-R10.
           - No NASA extraction file exists in any of the four trees.
           - `ROADMAP:L7/provenance/sources/STANDARDS_REGISTER.md:235` gives only the count: "**[source text withheld from the public copy])."
           - The only stated source is a journal outside the repository (`REQUIREMENTS_OWNERSHIP.md:13-14`, a `~/.claude/projects/...` path).

        5. **The 78 is unreconciled.** `ROADMAP:L8/L5/research/findings/AUDITON_PACKABILITY_2026-08-04.md:15` reads "**[source text withheld from the public copy].**" `MAIN:REQUIREMENTS_OWNERSHIP.md:244` reads "[source text withheld from the public copy]."

        **IMPRECISE OR OVERSTATED**

        - **(a) State.** The 62 error is live on MAIN and ROADMAP only. BETA already corrects it:
          - `BETA:L7/provenance/sources/LEDGER.md:149` says "[source text withheld from the public copy] same BETA line records a second arithmetic slip: "22 new rows" enumerates 21.
          - BETA's four sheets now say 60; only its two history files keep 62.
          - The claim cites no locator for the ledger at all.

        - **(b) "Cannot be recounted" is too strong.** 99 of 113 can be recounted and I did so. Only the 14 NASA rows cannot. The repository's own claim is the opposite: "[source text withheld from the public copy]." (lines 15-16). That is a claim about a journal the repository does not hold.

        - **(c) The 78 is not a cause of the missing recount.** It is a separate open item. The repository labels it "[source text withheld from the public copy]" (lines 19-20).
          - Evidence the claim does not cite: the 78-run's tally table at `ROADMAP:AUDITON_PACKABILITY_2026-08-04.md:214-218` sums to ISO 24, NIST 20, NASA 14. These equal the 113's lane counts for those three bodies. There is no IEEE row.
          - By my arithmetic the gap would then sit in IEEE (78 − 58 = 20 against 55). No document records that reconciliation.
          - MAIN cites the 78 by a dead path (`intake/research/...`); the file exists only on ROADMAP and HISTORY.
          - The cross-reference at line 21, "(see §6)", points to the D table, not to the limits in §10.

        - **(d) "Would reach print" is a forecast, and uneven across the three counts.** No chapter is written.
          - The unflagged carriers are all on ROADMAP, a closed unmerged PR:
            - `SPINE_v0.1_2026-08-14.md:138`: "sixteen of twenty-one are IEEE 7009".
            - `STANDARDS_REGISTER.md:344,492` and `lists-2026-08-08/PRIMARY.md:104`: "16 of the 21".
            - `BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:639`: "113 requirements, 21 obligations, 62 source rows ... are the corpus's own".
          - The same roadmap already gates on the 113: line 514 "the 78-versus-113 count reconciled" and line 520.
          - The 16-for-15 error is flagged nowhere in any state.

        **Evidence states (mine)**
        - 16 of 21: CONTRADICTED (the file disagrees with itself; my recount gives 15).
        - 62 rows: CONTRADICTED on MAIN and ROADMAP; INTERNALLY CHECKED and corrected on BETA.
        - 113: UNRESOLVED (99 INTERNALLY CHECKED, 14 not in the repository, 78 unreconciled).

        A fourth branch, `origin/ccr-9391bd81-f2enmj` (agent results of 2026-11-11), also holds no NASA rows. It is outside the three named states.
      - **corrected_statement**: KC-10 (corrected): Three counts in the record are wrong or not reproducible from the repository, and the first is flagged nowhere.

        1. IEEE 7009 carries fifteen of the 21 envelope obligations, not sixteen, and 71%, not 76%. REQUIREMENTS_OWNERSHIP.md contradicts itself: line 72 and the table at 90-110 give 7001 = 6 and 7009 = 15; lines 117 and 263-264 say "Sixteen" and "76%". This is uncorrected on MAIN, ROADMAP and BETA. On ROADMAP it is repeated at SPINE_v0.1_2026-08-14.md:138, STANDARDS_REGISTER.md:344 and 492, and lists-2026-08-08/PRIMARY.md:104.

        2. The source ledger L7/provenance/sources/LEDGER.md has 60 [source text withheld from the public copy]), not the 62 stated in the L7 sheets and in L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:30. This is wrong on MAIN and ROADMAP, and carried into ROADMAP:BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:639. It is already corrected to 60 in BETA's current guidance (BETA:LEDGER.md:149, which also records that "22 new rows" enumerates 21); BETA's history files still read 62.

        3. The total of 113 requirements can be recounted only to 99 from the repository (IEEE 55 + ISO 24 + NIST 20 in MAIN:L8/L4/work/computation/). The 14 NASA rows are in no file on MAIN, ROADMAP, BETA or HISTORY; only NASA-R6 and NASA-R10 are named, at REQUIREMENTS_OWNERSHIP.md:157. The file's "Lane counts verified on recovery" (lines 15-16) rests on a journal outside the repository.

        Separately, the earlier run of 78 (ROADMAP:AUDITON_PACKABILITY_2026-08-04.md:15; cited on MAIN by a dead path) is unreconciled by the file's own label (line 244). ROADMAP's book roadmap already lists that reconciliation as a gate (lines 514, 520). That run's tallies for ISO, NIST and NASA sum to 24, 20 and 14, the same as the 113's lanes, so the gap appears to lie in IEEE. That is this reader's arithmetic, not a recorded reconciliation.

        No chapter is written, so "would reach print" is a risk carried by ROADMAP's planning documents, not an established fact.
      - **evidence_checked**
        - MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:72 — "[source text withheld from the public copy])"
        - MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:88-110 — table recounted by me: rows 1-6 IEEE-7001, rows 7-21 IEEE-7009 (6 + 15 = 21)
        - MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:117 — "**[source text withheld from the public copy].**"
        - MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:263-264 — "[source text withheld from the public copy]" / "bears 76% of the buildable requirement load"
        - MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:15-21 — "[source text withheld from the public copy]"
        - MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:244 — "[source text withheld from the public copy]."
        - MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:157 — the only line in MAIN, ROADMAP, BETA or HISTORY matching NASA-(R|D|Q)[0-9]+; names NASA-R6 and NASA-R10 only
        - git diff origin/main vs ROADMAP on REQUIREMENTS_OWNERSHIP.md and the three extraction files: identical; origin/main vs BETA: REQUIREMENTS_OWNERSHIP.md gains 2 lines (a Q13 disposition paragraph), 'sixteen' and '76%' unchanged
        - MAIN:L8/L4/work/computation/ieee-requirements-for-autonomouos.md — 55 '### IEEE-' headings (24 are IEEE-7009: D1-D5, R1-R13, six ASR rows); line 41 "## The requirements — 55 total"
        - MAIN:L8/L4/work/computation/iso-iec-requirements-for-autonomous.md — 24 '### ISO-R' headings; MAIN:L8/L4/work/computation/nist-requirements-for-autonomouos.md — 20 '### NIST-R' headings
        - MAIN:L8/L4/work/computation/0.md Holdings — "55 verbatim IEEE rows recovered from workflow journal `wf_b00a2270-83e`"; no NASA file listed
        - MAIN:L7/provenance/sources/LEDGER.md:20-79 — 60 register rows counted (PR 20, STD 34, INST 4, EXC 2; no duplicate IDs); ROADMAP copy byte-identical
        - MAIN:L7/provenance/0.md:20,33 — "62 pointer rows"; MAIN:L7/provenance/sources/0.md:10,41; MAIN:L7/peering/private/ingress/peer-1/0.md:16; MAIN:L7/peering/private/ingress/peer-1/object-1/0.md:10 (same lines on ROADMAP)
        - MAIN:L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:30 — "62 rows (PR-001..020, STD-001..034, INST-001..004, EXC-001/002)" (the ranges listed sum to 60)
        - BETA:L7/provenance/sources/LEDGER.md:149 — "[source text withheld from the public copy]."
        - BETA:L7/provenance/0.md:20,33 and BETA:L7/provenance/sources/0.md:10,41,55 — "60 archive pointer rows"; BETA:L8/L6/history/AUDITONOMOUS_BETA_HISTORY.md:8 — "Corrected current archive guidance to 60 rows"
        - ROADMAP:L8/L5/research/findings/AUDITON_PACKABILITY_2026-08-04.md:15 — "**[source text withheld from the public copy].**"
        - ROADMAP:L8/L5/research/findings/AUDITON_PACKABILITY_2026-08-04.md:214-218 — tally table [source text withheld from the public copy] (sums 24, 20, 14; no IEEE row)
        - ROADMAP:L7/provenance/sources/STANDARDS_REGISTER.md:235 — "**[source text withheld from the public copy])."; :344 — "**[source text withheld from the public copy]**"; :492 — "[source text withheld from the public copy]"
        - ROADMAP:L7/provenance/sources/lists-2026-08-08/PRIMARY.md:104 — "[source text withheld from the public copy]**"
        - ROADMAP:L8/L5/research/review/SPINE_v0.1_2026-08-14.md:136-138 — "25. **113 Requirements, 21 Obligations**" ... "sixteen of twenty-one are IEEE 7009"
        - ROADMAP:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:514,520 — "the 78-versus-113 count reconciled"; :639 — "113 requirements, 21 obligations, 62 source rows ... are the corpus's own"
        - File listings (git ls-tree) for MAIN, ROADMAP, BETA and HISTORY filtered for nasa/PACKABILITY/STANDARDS_REGISTER/journal: STANDARDS_REGISTER.md and AUDITON_PACKABILITY exist only on ROADMAP and HISTORY; no NASA extraction file and no journal.jsonl in any tree
        - origin/ccr-9391bd81-f2enmj (74b270e, outside the three named states) — only NASA-R6 and NASA-R10 mentioned; no NASA rows
    - item 11
      - **claim**: No chapter of the book has text, and the first drafting step the roadmap names, Chapters 2 and 19, is not ready. Nine moves stand before it with no record of any. Of the 22 decisions, 21 are unruled and the remaining one, D15, was inferred. The roadmap, the chapter files and more than half the chapter feeds exist only on the closed branch.
      - **id**: KC-11
      - **verdict**: corrected
      - **reasoning**: Most of KC-11 is confirmed from the git objects, but four parts are imprecise or overstated.

        **Confirmed**
        - ROADMAP:L8/L4/work/writing/book/ holds 31 files, 27 of them chapter files, all from one commit (b1ec302, 2026-09-14). Each chapter file's Text section is a single paragraph at line 24-29 that opens "*[source text withheld from the public copy]".
        - ROADMAP:L8/L4/work/writing/book/0.md says "No chapter carries text yet; the headers are the built positions the text goes into."
        - ROADMAP:L8/L4/work/writing/book/bibliography.md:3 reads "No entry yet."
        - No chapter file, roadmap record or L8/L4/work/writing/manuscript/ corpus exists on MAIN, BETA or any other of the 14 fetched remote refs.
        - The decision table (roadmap lines 612-633) has 22 rows: D1-D16 and D18-D23, with no D17. Line 608: "Nothing below is adopted."
        - D15 (line 626): "[source text withheld from the public copy]".
        - The drafting step is at line 603: "[source text withheld from the public copy])".
        - I found no record that any move was carried out as specified:
          - autonomous 9b49910 (PR #29) is not an ancestor of autonomous origin/main or the autonomous beta.
          - Neither clone has any tag.
          - No REVIEW_ record of either paper exists on any ref, and neither paper is mentioned on MAIN or BETA.
          - L8/L2/formal-mathematics/FORMULAS_LEDGER.md is the same blob (8affefd) on MAIN, ROADMAP and BETA: "Currently: **EMPTY** — no formulas held."

        **Corrections**
        1. **"Nine moves stand before it."** Eight numbered moves (lines 595-602) precede it, plus the first clause of move 9 itself (adversarial review of the two papers). Drafting is the second half of move 9.
        2. **"No record of any."** This holds only in the sense above. BETA, without citing the roadmap, works the subject of moves 3-4 the other way:
           - It keeps the binding at 0504961 (BETA:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:20, "[source text withheld from the public copy]").
           - It adds current-use dispositions for three [source text withheld from the public copy] (BETA:L8/L6/history/AUDITONOMOUS_BETA_HISTORY.md:7).
           - It disclaims being a ruling (same file, line 3: "not a new source-owner decision or release").
           - Moves 5-7 concern nine component repositories that are not among the three local clones, so they are unchecked here; branch protection is not visible in git objects.
        3. **"Chapters 2 and 19 … not ready."** This is true of Chapter 19: gates D1 and D21, "every case number NOT-CHECKED", verify items "all NOT-CHECKED", and 2 of 4 feeds off MAIN. For Chapter 2 it is overstated. Its own header records "Gates: none" and "registers complete; chapter prose none", and all 4 feeds are present on ROADMAP (3 of 4 on MAIN and BETA). Chapter 2 is held only by the move sequence and by sitting on a closed branch.
        4. **"More than half the chapter feeds exist only on the closed branch."** My recount of the 27 headers does not reproduce 73 of 133:
           - 141 feed bullets: 65 resolve on MAIN, 64 on BETA, 132 on ROADMAP.
           - 76 (54%) do not resolve on MAIN; 67 (47.5%) resolve at a branch tip only on ROADMAP.
           - 9 resolve on no tip (pointers to aybllc/autonomous, git: locators, a scratchpad file, a glob).
           - By distinct path: 94 paths, 58 not on MAIN, 51 (54%) ROADMAP only.
           - So "more than half do not resolve on MAIN" is firm; "exist only on the closed branch" depends on the counting unit. The restored feeds also exist in HISTORY (1d83788) at their pre-prune paths: 66 of 72 "was git:" locators resolve exactly, and the other 6 are abbreviated names in the headers.

        **Nuances**
        - "27 files ending 'Not yet drafted.'" is loose: the files end "...written with the text, not before it."
        - Roadmap §4 (lines 433, 435, 442, 445, 446, 449) marks author prose "drafted" for Chapters 8, 10, 17, 20, 21 and 24 (Nimitz). That refers to Blocks and Master Archive material, not chapter text.
        - "21 unruled" is true of the roadmap's own table. The owner's ruling "Book register: **scholarly only**" at HISTORY:HUB_LEDGER.md:49 bears on D1 but is at no branch tip and is not cited by the roadmap.

        Scratch files are in /tmp/claude-0/-home-user/bfcfd013-a2da-5019-961e-7f46116f08be/scratchpad/wf-handle/KC-11/ (feeds.py, feeds2.py, roadmap.md, book/).
      - **corrected_statement**: No chapter of the book has text: the 27 chapter files (ROADMAP only, one commit b1ec302) are headers whose Text section opens "*Not yet drafted.*", and the bibliography reads "No entry yet." The first drafting step the roadmap names is the second half of move 9, "[source text withheld from the public copy])" (ROADMAP roadmap:603). Eight numbered moves (595-602) and the adversarial review of the two papers that opens move 9 stand before it. In the three local repositories there is no record that any of them was carried out as specified: autonomous PR #29 (9b49910) is unmerged, no tag exists, no REVIEW_ record of either paper exists, and the L2 formulas ledger is still EMPTY on MAIN, ROADMAP and BETA. Moves 5-7 concern component repositories not held locally and are unchecked. BETA (unmerged) nevertheless works the subject of moves 3-4 without citing the roadmap: it keeps the binding at 0504961 ("not a rebind"), adds current-use dispositions for three [source text withheld from the public copy], and says it is "not a new source-owner decision". Chapter 19 is not ready by its own header (gates D1 and D21 unruled; verify items "all NOT-CHECKED"; 2 of 4 feeds off MAIN). Chapter 2 has "Gates: none", "registers complete", and all 4 feeds on ROADMAP (3 of 4 on MAIN and BETA); it is held only by the move sequence and by sitting on the closed branch. Of the 22 decision rows (D1-D16, D18-D23; no D17), 21 are unruled in the roadmap's table and D15 is "TAKEN AS RULED … by the instruction", an inference. Outside the table, BETA's retained binding bears on D22 and the history-only ruling "scholarly only" (HISTORY:HUB_LEDGER.md:49) bears on D1; neither is a ruling of the row. Among all fetched refs the roadmap record and the chapter files exist only on the closed branch. Of 141 feed bullets in the chapter headers, 76 (54%) do not resolve on MAIN; 67 resolve at a branch tip only on ROADMAP (51 of 94 distinct paths, 54%), and these also survive in HISTORY at 1d83788; 9 resolve on no branch tip.
      - **evidence_checked**
        - MAIN:L8/L5/research/review/STATUS_LADDER.md and STATUS_AND_LABEL_DISCIPLINE.md (read first, for the repository's own labels)
        - ROADMAP:L8/L4/work/writing/book/ (ls-tree: 31 files = 27 chapter files + 0.md, 00-front-matter.md, bibliography.md, build.sh; git log on the path: only b1ec302, 2026-09-14)
        - ROADMAP:L8/L4/work/writing/book/ch01..ch27: last non-blank line of every file opens "*[source text withheld from the public copy]" (27 of 27)
        - ROADMAP:L8/L4/work/writing/book/0.md: "No chapter carries text yet; the headers are the built positions the text goes into."
        - ROADMAP:L8/L4/work/writing/book/bibliography.md:3: "[source text withheld from the public copy]"
        - ROADMAP:L8/L4/work/writing/book/ch02-...md:3 "Gates:** none"; :9-12 four feeds; :18 "registers complete; chapter prose none"; :22 "draft from the two registers"
        - ROADMAP:L8/L4/work/writing/book/ch19-...md:3 "[source text withheld from the public copy]"; :16 "all NOT-CHECKED"; :22 "[source text withheld from the public copy]"
        - ROADMAP:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:595-604 (ten moves; :603 "Adversarial review of the two papers ...; [source text withheld from the public copy])")
        - ROADMAP: same file :608 "Nothing below is adopted."; :612-633 (22 rows: D1-D16, D18, D19, D20, D22, D23, D21; 'D17' occurs 0 times in the file)
        - ROADMAP: same file :626 "[source text withheld from the public copy]"; :585 "D15, taken as ruled by the instruction"
        - ROADMAP: same file :589 S6 gate "[source text withheld from the public copy]"; :645 "the writing not begun (S6)"
        - ROADMAP: same file :433, 435, 442, 445, 446, 449 (§4 'Author prose' column reads "drafted (Blocks ...)" for Ch 8, 10, 17, 20, 21, 24)
        - Feed recount by my own script over the 27 headers (feeds.py, feeds2.py in scratch): 141 feed bullets; resolve on MAIN 65, BETA 64, ROADMAP 132; ROADMAP-only among tips 67; none of the three tips 9; distinct paths 94 (36 on MAIN, 51 ROADMAP-only); 66 of 72 'was git:' locators present at 1d83788
        - All 14 remote refs of auditonomous: files matching BOOK_STRUCTURE_AND_ROADMAP, L8/L4/work/writing/book/ or L8/L4/work/writing/manuscript/ exist only on origin/claude/book-structure-roadmap-k8ap82 (87 files); 0 on MAIN, BETA and the rest
        - MAIN and BETA: ls-tree L8/L4/work/writing/ (11 files each, no book/ or papers/ directory)
        - autonomous: 9b49910 (PR #29 branch) is not an ancestor of origin/main (c9076c3) or origin/beta/7lm-exemplar-autonomous (e64b382); git tag -l is empty in both clones; no 'exemplar-2026-09-14', 'BASELINE_PAPER' or 'VOCABULARY_PAPER' string on MAIN or BETA of either repository
        - REVIEW_ records: none in auditonomous on MAIN, BETA or ROADMAP; autonomous REVIEW_1..5 were last touched 2026-09-12 (4e19369), before the papers
        - L8/L2/formal-mathematics/FORMULAS_LEDGER.md: same blob 8affefd on MAIN, ROADMAP and BETA, "Currently: **EMPTY** — no formulas held."; BETA adds only relations/AUDITONOMOUS_BETA_PREDICATE.md
        - BETA:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:20 "[source text withheld from the public copy]"
        - BETA:L8/L6/history/AUDITONOMOUS_BETA_HISTORY.md:3 "This record concerns the authorized local candidate, not a new source-owner decision or release."; :7 "Appendix C ancestry and neighbor concepts, Q13 and C1–C7 now have explicit current-use dispositions"
        - BETA:L7/peering/public/ingress/peer-1/object-2/0.md:8 "Object-1 remains the unchanged historical definition binding."
        - BETA vs MAIN diff of L7/peering/public/ingress/peer-1/object-1/0.md, L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md and L8/L5/research/review/CONTRADICTIONS.md (+15 lines, 'Current receiving-use dispositions — 2026-11-03'); no 'D22', 'BOOK_STRUCTURE' or roadmap reference anywhere on BETA
        - HISTORY:HUB_LEDGER.md:49 "[source text withheld from the public copy]"
        - Not checkable from the three local clones: the nine component repositories of moves 5-7 (ebc, eb-carrier, nua, una, broken-zero, uha, ommp, ebios, eb-audit) and branch protection on autonomous main
    - item 12
      - **claim**: The model has three candidate states and the repositories match none in full. 7lm main (c9dc061, 11 November 2026) has the L7 restructure. The 7lm beta (97314c5, 3 November 2026) adds the R1 to R6 contracts and the manuscript guidance and is not merged into main. Both exemplar betas pin 4ca3edb. A session branch of 11 November 2026 mirrors the L7 restructure on top of MAIN only.
      - **id**: KC-12
      - **verdict**: corrected
      - **reasoning**: Every ref, hash, date and ancestry fact in the claim checks out. Four parts are imprecise or overstated.

        **Confirmed as written**
        - 7lm `origin/main` is c9dc061 (2026-11-11 10:08 -0800) and has `L7/allications/` and `L7/governance/controlled/`.
        - 7lm `origin/beta/common-contracts-r1-r6` is 97314c5 (2026-11-03 08:58 -0800); it is not an ancestor of main; the merge-base is 2e5a6d6.
        - 4ca3edb is the beta's first commit and is in no branch but the beta.
        - Both exemplar betas pin 4ca3edb at `binding.json:7` (`"architecture_commit": "4ca3edb9172c34e6b0033bd09e2379ed3da76d9d"`).
        - `## Manuscript work` appears only at 7LM-BETA:`L8/L4/work/writing/0.md:12`; no such heading exists in any state of auditonomous or autonomous.
        - The mirror commits f2d5b37 (auditonomous) and 8257118 (autonomous), both 11 Nov 2026 UTC, sit directly on `origin/main`; neither BETA nor ROADMAP is an ancestor of the session branch.

        **Corrections**
        1. **"Three candidate states" undercounts.** 7lm has three more unmerged heads, none in main or the beta:
           - `origin/audit/peering-descriptive-reframe-2026-09-20` (3555866): 122 commits, 79 files, mostly the owner's descriptive reframe of 20 Sep.
           - `origin/ccr-00099fac-hjosbo` (b5c3984): 8 commits.
           - `ccr-9391bd81-f2enmj` (4cbd74b).

           All three retire the field guide to `L8/L6/retired/field-guide-2026-09-20/`, while the beta edits it at its live path. Main and beta have also diverged: the beta lacks main's `L8/L6/in/7lm-layer-lists.md`.
        2. **The date on main is the layer-lists merge, not the restructure.** The L7 restructure reached main on 20 Sep 2026 (606d4b3, PR #17 merge 0d1ec40). The 11 Nov merge added one file.
        3. **4ca3edb is not the beta tip.** The manuscript guidance arrived in 97314c5, one commit after the pinned 4ca3edb, so the exemplars pin a state without it. The repository calls R1–R6 "corrections", not contracts (7LM-BETA:`L8/L6/history/specification-history.md:104-106`: "after the owner's approval of R1–R6").
        4. **"Match none in full" is overstated on the model's own check.** Against the 71-position canonical list in `integrity.yml`:
           - MAIN, ROADMAP, autonomous main and scholarly-pair each lack 8 positions.
           - Both exemplar betas and both session branches have all 71.
           - Auditonomous BETA's `integrity.yml` is byte-identical to 7lm 4ca3edb's; the auditonomous session branch's is byte-identical to 7lm main's.

           What no repository state has is the beta tip's guidance.

        **Smaller points**
        - BETA already contains the L7 restructure (the same six renames in auditonomous), so two unmerged auditonomous branches each carry it independently.
        - "Six renames" is true of auditonomous only; autonomous 8257118 has ten. The mirror commits also add six new `allications` sheets and edit about 45 others.
        - The session branch is not local-only: `origin/ccr-9391bd81-f2enmj` exists at the same tips, now 74b270e (auditonomous) and a719cec (autonomous), not the cited commits.
      - **corrected_statement**: The model (aybllc/7lm) has one merged state and several unmerged ones, and three of them matter to the repositories. (1) 7lm main (c9dc061, merge of PR #21 on 11 November 2026) carries the L7 restructure, which has been on main since PR #17 of 20 September 2026; the 11 November merge added only the layer lists at the L6 inbox. (2) The 7lm beta is two commits on merge-base 2e5a6d6 and has diverged from main (not merged into main, and it lacks main's layer lists). Its first commit, 4ca3edb (2 November 2026 PST), applies the owner-approved R1 to R6 corrections and adds bounded research objects. (3) Its tip, 97314c5 (3 November 2026), adds guidance to 18 sheets, including the "Manuscript work" section. Both exemplar betas pin 4ca3edb, not the tip, so they pin a state without the manuscript guidance. Three further unmerged 7lm heads exist (audit/peering-descriptive-reframe-2026-09-20 at 3555866, ccr-00099fac-hjosbo at b5c3984, and the session branch ccr-9391bd81-f2enmj at 4cbd74b); all three retire the field guide that the beta edits in place.

        No repository state carries the beta tip's guidance. MAIN and ROADMAP (and autonomous main and the scholarly-pair branch) lack 8 of the model's 71 canonical positions (L7/allications with its six children, and L7/governance/controlled). BETA already contains the L7 restructure and has all 71 positions, with an integrity workflow in auditonomous identical to 7lm 4ca3edb's. The session branch ccr-9391bd81-f2enmj (pushed; mirror commits f2d5b37 in auditonomous and 8257118 in autonomous, 11 November 2026; tips now 74b270e and a719cec) mirrors the L7 restructure directly on MAIN (six renames in auditonomous, ten in autonomous, plus six new allications sheets). It has all 71 positions and, in auditonomous, a workflow identical to 7lm main's, but contains nothing of BETA, ROADMAP, R1 to R6 or the manuscript guidance.
      - **evidence_checked**
        - 7lm refs: origin/main c9dc061 (2026-11-11 10:08:11 -0800, 'Merge pull request #21: the layer lists...'); origin/beta/common-contracts-r1-r6 97314c5 (2026-11-03 08:58:01 -0800); merge-base 2e5a6d6; beta is not an ancestor of main; 4ca3edb (2026-11-02 20:53:22 -0800) is contained only in the beta branch
        - 7lm `git diff --stat 2e5a6d6 origin/main`: one file, L8/L6/in/7lm-layer-lists.md (415 insertions)
        - 7lm `git log --diff-filter=A origin/main -- L7/allications/0.md L7/governance/controlled/0.md`: 606d4b3 2026-09-20 'The L7 restructure: allications, and controlled'; merged by 0d1ec40 (PR #17, 2026-09-20)
        - 7LM-BETA:L8/L4/work/writing/0.md:12 '## Manuscript work'; heading absent at 7lm origin/main, 2e5a6d6 and 4ca3edb (git grep)
        - 7lm `git diff --stat 4ca3edb 97314c5`: 18 sheets changed, including L8/L4/work/writing/0.md (+6); 97314c5 message: 'Update 18 existing 0.md documents for shared project structure, project-owned design choices, manuscript placement'
        - 7LM-BETA:L8/L6/history/specification-history.md:104-106 '### Owner-approved common architecture corrections of 2 November 2026' / 'Implemented by Codex, task T1, on 2 November 2026 ... after the owner's approval of R1–R6'
        - 7LM-BETA:L8/L6/history/specification-history.md:101 'The exemplar repositories `aybllc/autonomous` and `aybllc/auditonomous` still carry the former branch names and are not brought into step by this pass.'
        - BETA:L7/peering/public/ingress/peer-1/object-2/binding.json:7 '"architecture_commit": "4ca3edb9172c34e6b0033bd09e2379ed3da76d9d"' (auditonomous)
        - autonomous origin/beta/7lm-exemplar-autonomous:L7/peering/public/egress/peer-1/object-2/binding.json:7, same architecture_commit; autonomous BETA:L8/L5/research/findings/BETA_FINDINGS.md:13 '[source text withheld from the public copy] `4ca3edb...`'
        - 7lm other unmerged heads (`git log origin/main..<ref>`): origin/audit/peering-descriptive-reframe-2026-09-20 3555866 (122 commits, 79 files vs 2e5a6d6); origin/ccr-00099fac-hjosbo b5c3984 (8 commits); ccr-9391bd81-f2enmj 4cbd74b (8 commits); each includes 574500d 'The field guide retired: stale, deprecated, kept as an example'; none is an ancestor of main or the beta
        - 7lm `git diff --stat 2e5a6d6 4ca3edb`: L8/L6/7lm-field-guide.md edited at its live path (6 lines), while the 17 October lines rename it to L8/L6/retired/field-guide-2026-09-20/
        - auditonomous ccr-9391bd81-f2enmj: merge-base with origin/main is 2165144; six commits beyond main, f2d5b37 (2026-11-11 18:34:37 UTC, mirror) through tip 74b270e; BETA and ROADMAP are not ancestors; origin/ccr-9391bd81-f2enmj is at the same tip
        - autonomous ccr-9391bd81-f2enmj: merge-base with origin/main is c9076c3; 8257118 (2026-11-11 18:33:28 UTC, mirror) and tip a719cec; BETA and scholarly-pair are not ancestors
        - auditonomous `git show -M --name-status f2d5b37`: 5 renames to L7/allications/publications/ and 1 to L7/governance/controlled/0.md (six), 6 added allications sheets, about 45 modified files
        - autonomous `git show -M --name-status 8257118`: 9 renames to L7/allications/publications/ and 1 to L7/governance/controlled/0.md (ten)
        - auditonomous `git diff --name-status -M origin/main origin/beta/7lm-exemplar-auditonomous`: the same six renames are already in BETA; autonomous BETA has ten
        - Canonical 71-position list from 7lm 4ca3edb:.github/workflows/integrity.yml:45-57, checked against ls-tree of each state: auditonomous MAIN and ROADMAP, autonomous main and scholarly-pair each lack 8 (L7/governance/controlled, L7/allications and its six children); both exemplar betas and both session branches lack none
        - integrity.yml compared by diff: auditonomous BETA vs 7lm 4ca3edb 0 differing lines; auditonomous session branch vs 7lm origin/main 0 differing lines; autonomous copies differ by a retained local comment block
        - Heading grep '^#+ .*manuscript' on *0.md: none on auditonomous MAIN, BETA, f2d5b37 or session tip (other than a results-folder sheet), none on autonomous main, BETA, 8257118 or session tip; auditonomous BETA and session L8/L4/work/writing/0.md headings are identical and lack 'Manuscript work'
        - MAIN:L8/L5/research/review/STATUS_LADDER.md and MAIN:L8/L5/research/review/STATUS_AND_LABEL_DISCIPLINE.md read first, per rule 7
  - **gaps**
    - item 1
      - **severity**: high
      - **gap**: The report hardens "the prior-art search for the coinage was never run" (short answer, U-01, item 7). MAIN itself records three bounded searches and one result against the coinage that the report does not carry.
      - **finding**: CONFIRMED by reading. (a) Word search, MAIN:L8/L5/research/review/PERPETUITY_QUESTION_ADJUDICATION.md:91: ""[source text withheld from the public copy] ... PubMed ... Europe PMC REST ... Crossref API ... and Google Scholar". (b) Patents, same file :93: Google Patents "total_num_results: 0", labelled PARTIALLY VERIFIED because Espacenet, WIPO and USPTO "blocked non-interactive access". (c) Facet-by-facet prior art against named works (Schneier-Kelsey, Crosby-Wallach, PeerReview, Winfield-Jirotka, NTSB, PROV-DM, Avizienis, Dijkstra), :271: "[source text withheld from the public copy]." (d) A result AGAINST the coinage, :99: "[source text withheld from the public copy]." and :100, domains [source text withheld from the public copy]" ("a **lead only**"). (e) HISTORY:FREEZE.md:17-28: "NEGATIVE FINDING — VERIFIED 2026-08-05", `auditonom*` in "all 30 IEEE standard PDFs" = 0, self-downgraded to "PARTIALLY VERIFIED". (f) MAIN:L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:48: "Existing partial evidence (5 read IEEE standards; the retired F-003 30-PDF sweep) must not be overextended." The repository's own labels still say unrun (ROADMAP:L8/L0/semantics/definitions/AUDITONOMY.md:263 "**[source text withheld from the public copy]`"; ROADMAP:L7/provenance/prior-art/0.md:32 "the record is empty"), so two records disagree. My evidence states: absence of the adjective from five scholarly indexes = EXTERNALLY CHECKED as recorded (2026-08-02); concept novelty = UNRESOLVED; absolute novelty of the noun "auditonomy" = CONTRADICTED on a source the ladder prohibits; "never run" = CONTRADICTED by MAIN. Item 7 should be reworded: file the three existing searches at L7/provenance/prior-art, then run the novelty search proper, including the 2018 blog and the registrar check. The same applies to U-02: the entailment search is unrun but partial evidence exists, and Autonomous holds a dated auditability lane (AUT:L8/L5/research/lanes/LANE_B_AUDITABILITY.md:1-9, 2026-08-03).
    - item 2
      - **severity**: high
      - **gap**: The report says the manuscript guidance exists only at 7lm beta tip 97314c5 and that the session branch mirrors "only the L7 restructure, which all three candidates share". 7lm MAIN already carries an Auditonomous book traversal, an itemised list of what Auditonomous does not yet match, the procedure for bringing an adopter into step, and non-L7 changes no Auditonomous state has. Item 1 (the owner's stated first step) is assessed against the wrong baseline.
      - **finding**: CONFIRMED by reading 7lm origin/main c9dc061. (1) 7LM-MAIN:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:601-617, heading "### Auditonomous academic-book traversal": "L4 owns the Auditonomous model as made, written, instantiated, or operated, including production of the book artifact."; "L5 owns the book's research argument, interpretation, and teaching."; "L3 owns the project's formulas for life when they are applied, open-ended, constrained, approximate, or engineering formulas." and L2 "does not support life or own the project's formulas for life". That text predates both betas (git log -S finds it at c699e3e, 2026-09-12). It bears on report item 9, which sends every formal statement to L2. (2) Same file :958, "Not yet as stated" for Auditonomous: "three files still take a definition of autonomous from somewhere other than the binding ... The L0 epistemic rail is empty; its vocabulary stands at L5 as review status ... the L7 restructure is not yet mirrored." This is the model's own checklist for "match"; the report does not cite it, and does not list the epistemic-rail item at all. (3) Same file :954 repeats the row error: "Provenance: 62 pointer rows into l6" - so the 60-for-62 correction must also go to 7lm. (4) Procedure, 7LM-MAIN:L8/L6/7lm-field-guide.md §14: "The scaffold's update arrives, pinned to its hashes, as an item for HOA review at the adopter's `L7/peering/private/`: the scaffold is a peer, and its push is ingress. A person decides, item by item". No Auditonomous state binds 7lm as a private-ingress peer (MAIN private ingress = peer-1..3 only). (5) Non-L7 changes on 7lm main since the L7 restructure (git diff --stat 0d1ec40 origin/main): L8/L6/7lm-field-guide.md moved to L6, L8/L6/7lm-sheet-templates.md (136 lines), L8/L6/in/ (inbox), L8/L6/in/7lm-layer-lists.md (415 lines, merged by EDM 2026-11-11 as PR #21, "Filed at `L8/L6/in/`, the inbox for L6, as a proposal"). MAIN, ROADMAP, BETA and local f2d5b37 each hold 0 files matching L8/L6/in/, sheet-templates or field-guide. (6) Neither 4ca3edb nor 97314c5 is an ancestor of 7lm main (git merge-base --is-ancestor: both NOT in main); 4ca3edb's subject is "Apply approved R1–R6", so choosing 7lm main drops R1-R6 and the commit both beta bindings pin. What the 3 November commit adds over this is only the two paragraphs "## Manuscript work" in the writing sheet (diff 4ca3edb..97314c5). Evidence state for "positions mostly agree with the model": UNRESOLVED until checked against the main specification, not only the beta sheet.
    - item 3
      - **severity**: high
      - **gap**: The report counts "two definitions and no document states how they relate" (X-01). There are at least four defining texts, and the repository itself names the third as the primary one.
      - **finding**: CONFIRMED. (1) The constitutional sentence, ROADMAP:L8/L6/retired/consolidated-2026-08-04/AUDITONOMOUS.md:70: "[source text withheld from the public copy] same file :74 labels it "INTERNAL ONLY — authorial text; the primary definiens." (2) The fused form, :80: "[source text withheld from the public copy]"; :84-96 tabulates five differences and ends "Neither is preferred here. Both stand." (3) MAIN acknowledges both and sets them aside without a relation, MAIN:L8/L0/semantics/definitions/0.md:36: "Two statements of the coined concept from the intake corpus ... stand verbatim in [source text withheld from the public copy] ...; the definition here is the record." `git grep 'runtime without parameters'` under MAIN:L8/L0 finds only that sheet line, so the 410-line entry of record does not contain the sentence the book's corpus calls the definition; AUDY on ROADMAP has no hit either. (4) HISTORY:manuscripts/definitions/REGISTER.md:12 and :16 enter BOTH the consolidated document and AUDITONOMY.md as "ADOPTED as coinage" (2026-08-14), which is a third position on which text governs, superseded two days later by AU-NORM-02. (5) C-1 in the consolidated register (:1123) records that the engineering layer [source text withheld from the public copy]." Evidence state: which text governs = UNRESOLVED across four texts, not two; clause count = CONTRADICTED. D20 and report item 4 need the constitutional sentence and the fused form in the option set.
    - item 4
      - **severity**: high
      - **gap**: A research object on MAIN that no reader opened and that carries a release risk the report does not list: L8/L5/research/review/autonomous-theory/#autonomous(1).txt.
      - **finding**: CONFIRMED by reading the git object (746 lines, 1,060,768 bytes; also on BETA). Lines 1-~630 are the 2025 draft, MAIN:"L8/L5/research/review/autonomous-theory/#autonomous(1).txt":1 "# Autonomous Theory: Post-Biological Intelligence", :15 "[source text withheld from the public copy]". From line 636 the file is a raw chat-export dump: :649 contains "\"[source text withheld from the public copy]\": ...". Counts over the file: "uuid" 127 times, "chat_messages" 2, and seven distinct e-mail addresses including third parties' personal and institutional addresses. The report's release item covers only "strip personal paths (R-16)" and the peering reader stated "No scan for credentials or for third-party personal data was made". The sheet treats the file only as a homing question (MAIN:L8/L5/research/review/0.md:42 "they leave this repository once the owner nam[es its home]"). Two consequences: (i) an account identifier and third-party personal data sit in every state's history and must be on the release/purge list beside the ISO PDF; (ii) the draft is UAP material, so the owner's ruling of 14 August 2026 ("scholarly only") and D1/D12 bear on it. The companion PDF (02_AutonomousTheory(1).pdf) was not opened by me. Evidence state of the draft's claims: CONJECTURE (unlabelled in the file; the consolidated document :1173 quotes the related scale as "[source text withheld from the public copy])").
    - item 5
      - **severity**: high
      - **gap**: The register of 23 internal contradictions (C-1 to C-23) is absent from the report's account of what is contradicted. The review-core reader flagged its existence; the report carries only the items that happen to coincide with X-02, X-03 and X-05.
      - **finding**: Read in full at ROADMAP:L8/L6/retired/consolidated-2026-08-04/AUDITONOMOUS.md:1117-1183 (§[source text withheld from the public copy]."). Not in the report, each with the file's own verdict: C-2 :1125 "Bounded autonomy" [source text withheld from the public copy]."; C-4 :1141 the asymmetry claim ("constrains only *concealment*") against the engineering layer's hard constraint on action ("unlawful motion is physically unreachable"); C-5 :1143 the refusal doctrine against "Encrypted OTA updates: signed law module revisions"; C-6 :1145 ordering of the two halves; C-7 :1147 binary word used gradably ("the least auditonomous object imaginable"); C-8 :1149 "FAILED CHECK on the independence claim" of the fourth derivation (the report lists D6 as a decision, not as a failed check); C-10 :1153 conceal as second or third verb; C-13 :1159 Certification as layer or external consumer, "FAILED CHECK — direct conflict"; C-14/C-15 :1161-1163 gate-then-ledger against ledger-then-gate, "FAILED CHECK / OPEN" (this is the same ordering the report's X-16 treats only as trace-before-release against a one-way carrier); C-16 :1165 the EB carrier pair, "FAILED CHECK"; C-17 :1167 four-way against three-way cabin intersection; C-18 :1169; C-20 :1173 [source text withheld from the public copy]; C-21 :1179 gate granularity 7/5/9 steps; C-23 :1183 "Two adjective forms, no rule" (also MAIN:DEF:16 "[source text withheld from the public copy]"). Section 10.4 (:1104-1113) adds reserved items the report does not list, including the unapplied A2/A3 ordinality fixes marked "FAILED CHECK / OPEN" (:1112). Evidence state for each: CONTRADICTED / UNRESOLVED; the register exists only on ROADMAP and in HISTORY, under L6/retired, and the roadmap uses it as a live feed. I did not re-verify the 23 against the corpus line by line.
    - item 6
      - **severity**: medium
      - **gap**: Research that exists ONLY in HISTORY (1d83788) and that the report does not name: the term ledger and its coverage map. The restore record's stated reason for leaving them out is contradicted by the peer's tree.
      - **finding**: HISTORY:intake/imported/AUTONOMOUS_TERMS.md (23 KB; :1-8 "IMPORTED TERMS ... Source commit: `f15524e9...`", rows T-01 to T-25; :12-14 "**[source text withheld from the public copy]*") and HISTORY:intake/imported/TERM_LANES.md (13 KB; :3 "**[source text withheld from the public copy]."). TERM_LANES is the only per-term statement of what has been read at source: e.g. :52 "[source text withheld from the public copy])", :51/:53-56 ISO 8373, TR 29119-11, ALFUS, OECD, EU Recital 12 all "`TEXT UNCHECKED`", :57 [source text withheld from the public copy])", :60 IEEE 7010 "**no quote carried at all**". The report cites "term T-02" and the audit's term-ledger corrections without saying the ledger is in no live tree. ROADMAP:L8/L6/history/restore-2026-09-14.md:230-231 gives the reason "NOT RESTORED — owner rule ...; the peer holds this material (... [source text withheld from the public copy]/)". Checked: neither blob (bb83067, a621fbe) is in any tree of autonomous origin/main, its beta or the PR #29 branch; no path there matches TERMS or TERM_LANES; `git grep -l 'T-25'` on autonomous origin/main returns nothing. So the stated reason is CONTRADICTED for these two files (it holds for AUTONOMY_SCALE.md, whose blob ad3fa67 IS at AUT:L8/L4/work/writing/AUTONOMY_SCALE.md). Also HISTORY-only and unnamed: the root counterpart entry AUTONOMOUS.md (blob 753e6d0, in no autonomous ref), manuscripts/definitions/REGISTER.md, and intake/MANIFEST.md (:5 "[source text withheld from the public copy]", which bounds every "where the word appears" claim in the definition). Evidence state: the T-rows are mostly UNRESOLVED by their own labels; the object is missing from every live state (add to the M-list and to worklist item 14/18).
    - item 7
      - **severity**: medium
      - **gap**: The report names "the freeze file" as HISTORY-only but not what it holds: a binding rule on how codified sources may be used for the coined word, which no live state carries, plus a recorded drift.
      - **finding**: HISTORY:FREEZE.md:58-79, "[source text withheld from the public copy]". :3-8 quotes the owner: "[source text withheld from the public copy]". :153 "*[source text withheld from the public copy].**"; :85-87 "[source text withheld from the public copy]". Checked: `git grep -i 'contamination rule'` and 'P1 — A coined' return nothing under L7, L8 or README.md on MAIN, ROADMAP or BETA; the restore record :90 says "NOT RESTORED — rule text ... [source text withheld from the public copy]" - for P1-P3 that claim is not borne out by grep. The rule bears directly on the manuscript: Chapter 13 (requirements routed to compartments) and the vocabulary paper's use of IEEE 7009 and NIST AU controls are exactly what P2/P3 govern. FREEZE.md §6 (:163-230) also records "2 FAILED of 13" on the drift check and that the stop path left the kernel; the owner's reply is quoted "[source text withheld from the public copy]." That is the origin of the stop-path disagreement the report settles from AUDY alone. Evidence state: rule = ASSERTED (owner instruction), currently in no live tree; whether it still binds = UNRESOLVED, an owner decision not in the report's list.
    - item 8
      - **severity**: medium
      - **gap**: "The first ten things to do": three items sit before things they depend on, and two are assigned to work that only the owner can unblock.
      - **finding**: (a) Item 9 (L2 rows) states its own dependency, "Needs D11 and D14 first", yet D11 is ruled only at worklist item 16 and D14 at no item at all; ROADMAP:RM:622 (D11) and :625 (D14: "[source text withheld from the public copy]"). The rows for conditions A-E and the Aud form also depend on item 4, and the 7lm main specification sends applied or approximate formulas to L3, not L2 (7LM-MAIN specification :607-609). (b) Item 8 is marked "No ruling needed" / work without the owner, but the 14 NASA rows exist only in a journal on the owner's machine: MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:12-14 "[source text withheld from the public copy]" at `~/.claude/projects/-home-eric-ayb-auditonomous/3d9a5dc6-.../journal.jsonl`; :243 "[source text withheld from the public copy]." Recovery needs the owner to supply the file; re-extraction needs the network and NASA sources that have no ledger row. (c) Item 10 (adversarial reviews) is marked work without the owner, but its three objects are not reviewable on MAIN: AUDY is ROADMAP-only and its version is unruled (item 4); of "the two papers of 14 September" one is ROADMAP-only and the other is in another repository on a closed branch (ROADMAP:RM:583: "[source text withheld from the public copy])", present only on PR #29's branch per the dependency reader). It therefore depends on items 2, 4 and 6. Only the envelope review can start today. (d) Item 3 is marked "No ruling needed" but three of its five corrections are to objects that exist only on ROADMAP or BETA (the Aud(S,F) row and D20 text; BETA's line 54), so they depend on item 2; the two that can be prepared now are 60-for-62 and fifteen-for-sixteen, and the 62 must also be corrected in 7lm (specification :954). (e) Item 7's premise is wrong as written (see the first gap). (f) Item 1 lists three candidate commits but omits that the choice decides whether R1-R6 apply (4ca3edb is not in 7lm main) and that 7lm's own procedure is an item-by-item HOA review at L7/peering/private.
    - item 9
      - **severity**: medium
      - **gap**: Owner decisions that are in the sources and not in the report's list of nineteen.
      - **finding**: Confirmed in sources: (1) D7, ROADMAP:RM:618 "[source text withheld from the public copy])." (2) D9, :620 "[source text withheld from the public copy]." (3) D19, :629 "[source text withheld from the public copy]." (D8 and D21 appear only in worklist item 17, not in the decisions list; a grep for a D17 row found none.) (4) MAIN:DEF:408 "[source text withheld from the public copy]." (5) The reader-agnostic divergence (§2.8), named among the four open author's calls at MAIN:L8/L5/research/review/0.md:44 and at ROADMAP consolidated :1098-1101 ("[source text withheld from the public copy]"). (6) The adjective form, auditonomic or auditonomous (MAIN:DEF:16; consolidated C-23). (7) 7lm's own open calls, 7LM-MAIN:L8/L6/7lm-field-guide.md §15: "A held-off rules file about what a session or a model may touch."; and whether the layer lists stay (layer-lists :5 "is the owner's call, HOA"). (8) Whether the contamination rule P1-P3 still binds (previous gap). (9) Whether the L0 epistemic rail takes the status vocabulary now at L5 (7LM-MAIN specification :958). Reported by readers and not in the list, not re-read by me: the IEEE 7014 erasure collision and equivocation as a fourth prohibited act (sources reader); Appendix C handling and the BETA dispositions (definition, records readers); the IEEE-754 "surface to Eric before ledgering" caveat and whether AU-NORM-04 is superseded (records reader); binder/internal placement and the IEEE quotation-clearance conflict (peering reader); whether the refusal "DISPOSES" (findings reader); which version of the N/U paper was examined (docket reader).
    - item 10
      - **severity**: medium
      - **gap**: No reader covered .github/workflows/integrity.yml, and the three states disagree on it. It decides whether a merge onto the new model passes.
      - **finding**: MAIN:.github/workflows/integrity.yml:47-50 hard-codes the canonical positions the CI requires, including "L7/governance/restrictions" and "L7/publications" - the two positions the changed model retired - and still allows a root named USO (:23, :27). BETA rewrites the file (git diff --stat MAIN BETA: 21 insertions, 22 deletions; e.g. the root check becomes "README.md|L7|L8|.github|.gitignore"). ROADMAP's copy is identical to MAIN's (empty diff). Local f2d5b37 changes it too (5 insertions, 4 deletions; content not read, file list only). Consequence for report items 1-2: ROADMAP's 116 restored files were never checked against a workflow that knows allications/ and controlled/, and BETA's workflow has never run over ROADMAP's tree; whichever branch is merged second must carry the workflow that matches the chosen model commit. The workflow also records an owner rule the report does not quote, MAIN :3-4: "we cant enforce integroty by ebforceing no deletion. we can only imply no deletion to enforcer integiortyty" - which bears on worklist item 18 (enumerating the prune) and on item 16 of the decisions list. 7lm main and 7lm beta each carry their own integrity.yml (7lm beta changes it by 36 lines relative to 2e5a6d6); which one the adopters copy follows from item 1. Evidence state: UNRESOLVED (no run recorded on any combined tree; I ran nothing).
    - item 11
      - **severity**: low
      - **gap**: The report softens the replicator count and leaves one definitional register entry unassessed.
      - **finding**: The report says the replicator "records two of its headline claims refuted". HISTORY:manuscripts/definitions/REGISTER.md:14 states the denominator: "[source text withheld from the public copy]" and enters the object as "RETAINED with refutations on the record". Two of three is a materially different state from two of an unstated number; the report's X-15 (law L5 against the replicator's review) should carry it. The same register (:16) records AUDITONOMY.md as "[source text withheld from the public copy]" and "[source text withheld from the public copy])" - i.e. conditions A to E were demoted to "anchor analysis" under v2, while the report (L0 section and item 9) treats A to E as the definition's conditions to be formalised at L2. Whether A-E are definitional or anchor analysis is UNRESOLVED and belongs inside item 4. I did not re-read AUDITONOMY.md §0-§2 to test the register's description.
    - item 12
      - **severity**: low
      - **gap**: Scope note on what this critic did not close.
      - **finding**: Not opened by me and still uncovered by any reader's stated scope: MAIN:L8/L5/research/review/autonomous-theory/02_AutonomousTheory(1).pdf; ROADMAP:L8/L4/work/writing/sessions/SESSION_2026-08-05_VERIFICATION_LOG.md (cited by two readers, read in full by none); the 61 source PDFs and iso-iec-22989-2022_clause3_terms.txt (43 KB) that are in HISTORY:_STAGING_TO_L6/ and in no live tree (the report says no reader could open the archive, but the pre-prune tree in this clone holds the staged PDFs, e.g. HISTORY:"_STAGING_TO_L6/sources/ieee/pdf/7009-2024.pdf", "19201-2022.pdf" (IEEE 1920.1, on which Q13 rests), "_STAGING_TO_L6/sources/interval/IEEE-1788.1-2017_interval-arithmetic-simplified.pdf" (X-18) and the withdrawn ISO/IEC 22989 preview). So several checks the report marks impossible - the singular/plural wording of IEEE 7009 cl. 1.3.2(e), whether 1788.1 keeps decorations, the 1920.1 definition - could be made from git objects with pdftotext, subject to the hold-private licence condition on those files. HISTORY also holds intake/sweep-2026-07-30/ (nine files from abba-01 hubble repositories) and six manuscripts/main/research/chapter-chunk files, which the prior manuscript pass mentions and this report does not. HISTORY tree compared with live states by blob id (list at /tmp/claude-0/-home-user/bfcfd013-a2da-5019-961e-7f46116f08be/scratchpad/wf-handle/critic/).
  - **readers**
    - item 1
      - **key**: definition
      - **items**: 66
      - **defects**
        - item 1
          - **statement**: The definition says [source text withheld from the public copy]/`'. No such file exists in MAIN or BETA; it is only in ROADMAP (L7/peering/private/ingress/peer-3/object-1/) and HISTORY (intake/manuscript/).
          - **locator**: MAIN:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:367
        - item 2
          - **statement**: The object-1 binding sheet says the definition 'names this binding'. The definition on MAIN and ROADMAP contains no reference to the binding or the peer repository.
          - **locator**: MAIN:L7/peering/public/ingress/peer-1/object-1/0.md:34
        - item 3
          - **statement**: The definitions sheet says Appendix C quotes the root 'autonomous' from RFC 4949, NIST CSRC and the IEEE 7001 page. Those entries quote 'audit trail', 'firmware' and a transparency scope sentence.
          - **locator**: MAIN:L8/L0/semantics/definitions/0.md:34
        - item 4
          - **statement**: MAIN files cite `definitions/AUDITONOMY.md` (once as 'governing text') although the file is absent from MAIN and BETA and the path matches no layout position.
          - **locator**: MAIN:L8/L1/state-space/AUDITON_ENVELOPE.md:76 and :253; MAIN:L8/L5/research/findings/DISTILLATION.md:21 and :261
        - item 5
          - **statement**: The two rule files read before every pass cite `AUDITONOMOUS.md` (:1230 and §10), a file removed from HEAD at 8c98573 and present only in history and, on ROADMAP, at L8/L6/retired/consolidated-2026-08-04/.
          - **locator**: MAIN:L8/L5/research/review/STATUS_LADDER.md:14; MAIN:L8/L5/research/review/STATUS_AND_LABEL_DISCIPLINE.md:22
        - item 6
          - **statement**: AUDITONOMY.md refers to 'adjudicated stop' language and 'command is weighed, not obeyed' material 'below'; neither is in the file. Earlier wording was overwritten in place, against the ladder's rule that a wrong entry stays visible.
          - **locator**: ROADMAP:L8/L0/semantics/definitions/AUDITONOMY.md:42-43 and :58-59
        - item 7
          - **statement**: AUDITONOMY.md cites companion files by another repository's old relative paths ([source text withheld from the public copy], governance/RULINGS.md). None resolves in the Auditonomous tree; five are at no current head of either repository.
          - **locator**: ROADMAP:L8/L0/semantics/definitions/AUDITONOMY.md:8, :179, :223, :225, :240, :285, :337, :358
        - item 8
          - **statement**: The ROADMAP restore of AUDITONOMY.md used the freeze-pinned bytes of autonomous commit e27ca78 (462 lines). Three later versions (475 lines; 5c2b2e1, b8214ed, 9c123b0) exist in aybllc/autonomous history and are not mentioned in the restore record or the sheet. The restored version labels condition B's sources 'both unread' where the last version records them as read.
          - **locator**: ROADMAP:L8/L0/semantics/definitions/AUDITONOMY.md:202 and :272; AUTONOMOUS@9c123b0:auditonomous/definitions/AUDITONOMY.md
        - item 9
          - **statement**: The bound Autonomous definition says 'the ten above' over a table of eleven rows A1–A11; AUDITONOMY.md repeats 'ten'; the Auditonomous binding sheet says eleven.
          - **locator**: AUTONOMOUS@0504961:research/definitions/AUTONOMOUS.md:244; ROADMAP:L8/L0/semantics/definitions/AUDITONOMY.md:234; MAIN:L7/peering/public/ingress/peer-1/object-1/0.md:28
        - item 10
          - **statement**: BETA edits the definition file in place, so the 'line 52' clause is at line 54, yet BETA's ledger, review sheet and adjudication still cite :52, and the AU-NORM-02 description 'restored verbatim, 410 lines' no longer fits the BETA file (426 lines).
          - **locator**: BETA:L8/L6/history/LEDGER.md:61; BETA:L8/L5/research/review/PERPETUITY_QUESTION_ADJUDICATION.md:216; BETA:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:54
        - item 11
          - **statement**: BETA uses C6 and C7 for envelope compartments and for contradiction entries in the same findings file, and the L0 scope file does not say which series it means.
          - **locator**: BETA:L8/L5/research/findings/AUDITONOMOUS_BETA_FINDINGS.md:9 and :24; BETA:L8/L0/semantics/AUDITONOMOUS_BETA_SCOPE.md:7
        - item 12
          - **statement**: Three nits found by the definition's own verification (citation span, unmarked truncation of the RFC 4949 quote, unflagged constructed pronunciation) were never applied and appear on no pending list.
          - **locator**: MAIN:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:351 (nits); :14, :47, :69 (unchanged text)
        - item 13
          - **statement**: MAIN's sheet for the Auditonomous repository says 'In this exemplar, the L0 object is the locally authored semantic definition of Autonomous'. BETA changes it to Auditonomous.
          - **locator**: MAIN:L8/L0/0.md:77; BETA:L8/L0/0.md:77
        - item 14
          - **statement**: The text of owner rulings AU-NORM-01 to AU-NORM-04 is recorded nowhere; AU-NORM-04 appears only in the commit message of 4a1c1db and in a ledger title.
          - **locator**: MAIN:L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:1 and :32
        - item 15
          - **statement**: Appendix D points to the full agent returns in a home-directory journal outside the repository, so the outputs behind the 'SURVIVES ADVERSARIAL REVIEW' verdict are not held.
          - **locator**: MAIN:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:362
      - **open_questions**
        - Which text is the definition for the book: the three-sense entry of 2026-07-30 (record per AU-NORM-02), AUDITONOMY.md §0 v2 (2026-08-05, 'governs' by its own header), or both with a stated relation? No document in any state says. ROADMAP decision D20 is unruled.
        - Which version of AUDITONOMY.md does the owner mean: the freeze-pinned e27ca78 bytes restored on ROADMAP, or the last version in aybllc/autonomous history (9c123b0, 2026-08-06), which adds two-tier stop enforcement and grounds condition B? I found no record of a choice beyond the 2026-08-14 'pin-by-pin decisions' in the commit message of dabed3c.
        - I could not verify any quotation from abba-01/ebios or aybllc/eb-stack: neither repository is in the local clones. Every corpus quote in the definition, and EB2 and the λ homonym ruling in AUDITONOMY.md, rest on the checks those files record.
        - I could not re-check any external quotation (AHD, Perseus, RFC 4949, NIST, IEEE 7001, Schneier & Kelsey, Crosby & Wallach, Haeberlen et al.): no network. Their VERIFIED labels are the repository's.
        - Is docs/EINSTEIN_BRANCH.md present on ebios v1.0.0-dev? If it is attempt-branch-only, the firmware-below versus above-ROM contradiction (DEF:79 item 4) rests on a branch the owner ruled was only an attempt, and Appendix F's statement that only ORIGIN.md quotes are attempt-exclusive would be wrong.
        - Did the owner rule on BETA's handling of Appendix C (keep the quotes, add 'Current role' lines)? MAIN leaves it as 'the owner's edit'; I found no ruling in BETA's L0 files or its history record.
        - Has a prior-art search for the coinage been run? AUDITONOMY.md §6 says none ('NOT-CHECKED'); the HISTORY register cites a 'verified negative finding 2026-08-05' in FREEZE.md §1, which was not restored and which I did not open in history.
        - Do L1 or L2 files define 'truth envelope', 'transformation path' and 'epistemic state'? I did not search beyond L0 and the head of the two L1 files the L0 sheets cite.
        - The AUDITONOMY.md anchors labelled VERIFIED ([source text withheld from the public copy], AU-5(2)) were not traced to their provenance rows; that belongs to the L7 scope.
        - BETA object-2 pins an Autonomous commit (805cd42) and a 7LM commit (4ca3edb) that exist only on unmerged beta branches of those repositories. Whether a binding to unmerged commits is acceptable is for the owner; I confirmed only that both commits exist locally.
        - The exact relation between the two λ_A wordings (AUDITONOMY.md:379 'remains in operation' and the peer-2 protocol :74 'has completed its immediate operative role') is flagged on ROADMAP as CH-01 'two incompatible λ_A definitions'; I did not read the chat-ingestion record that names the pair, so I cannot say these are the two it means.
    - item 2
      - **key**: state-space
      - **items**: 26
      - **defects**
        - item 1
          - **statement**: "[source text withheld from the public copy]" and "76%" contradict the same file's "7001 (6) and 7009 (15)" and its 15-row table (71%). The figure is repeated in STANDARDS_REGISTER.md:344/:492/:495, PRIMARY.md:104 ("Three quarters"), STANDARDS_CITED.md:24 and SPINE_v0.1:138 on ROADMAP, and in FREEZE.md:259 in HISTORY. BETA, whose commit message claims corrected ledger arithmetic, leaves it unchanged.
          - **locator**: MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:117 and :263-264 vs :71-72
        - item 2
          - **statement**: Wrong internal cross-references in REQUIREMENTS_OWNERSHIP.md: "Reconciling them is open work (see §6)" points to §6, which is the D table (the unreconciled note is in §10, line 244); "NEW OPEN QUESTION — see §7/Q10" points to §7, the interface contract (Q10 is in §11, line 254).
          - **locator**: MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:21 and :146
        - item 3
          - **statement**: The three MAIN objects cite files by paths of the retired layouts (definitions/…, research/…, governance/…, intake/…, STANDARDS_REGISTER.md as a sibling link, and `../autonomous/definitions/AUDITON_ENVELOPE.md` for a file that is in this repository). On MAIN and BETA several targets are absent altogether: AUDITONOMY.md, AUDITON_REPLICATOR.md, STANDARDS_REGISTER.md, AUDITON_PACKABILITY_2026-08-04.md. The sheet says where the L0/L3/L5 citations stand but not that these targets are missing.
          - **locator**: MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:3, :9, :19, :30; MAIN:L8/L1/state-space/AUDITON_ENVELOPE.md:20, :76, :110, :174, :188, :253; MAIN:L8/L1/state-space/HUMINT_ENCODE.md:16, :39, :121, :282, :291-293
        - item 4
          - **statement**: The MAIN copies of all three objects are re-saves made at the prune commit 8c98573 (table padding and blank quote lines; no word changed by normalised diff). In the envelope the re-save inserted an empty quote line inside the owner's quoted sentence, splitting it across a heading boundary. The restore record calls the HISTORY versions "SUPERSEDED — a later version stands at HEAD" although they differ only in whitespace.
          - **locator**: MAIN:L8/L1/state-space/AUDITON_ENVELOPE.md:216-218 vs HISTORY:manuscripts/definitions/AUDITON_ENVELOPE.md:216-217; ROADMAP:L8/L6/history/restore-2026-09-14.md:343, :346, :363
        - item 5
          - **statement**: HUMINT_ENCODE.md: "These three are the warrant" follows a five-row table, and §5 repeats "one of only three warrants".
          - **locator**: MAIN:L8/L1/state-space/HUMINT_ENCODE.md:43 and :145-146 (table at :37-41)
        - item 6
          - **statement**: HUMINT_ENCODE.md §6.1 heading says "eleven controls" while the controls enumerated beneath it ([source text withheld from the public copy]) number thirteen.
          - **locator**: MAIN:L8/L1/state-space/HUMINT_ENCODE.md:159-161
        - item 7
          - **statement**: HUMINT_ENCODE.md slot H7 cites "(42006)" as the certification block; ISO/IEC 42006 is introduced nowhere else in the file, whose BLOCKED table cites ISO/IEC 17021-1 §3.6 and ISO/IEC 42001.
          - **locator**: MAIN:L8/L1/state-space/HUMINT_ENCODE.md:84 vs :52
        - item 8
          - **statement**: HUMINT_ENCODE.md cites "SCOPE_single_object.md §11–12" and "§3" for the replication exclusion; the scope ruling has sections 1 to 5 and the exclusion is at its lines 11-12 and §5 item 1 (the replicator cites the same exclusion as "§5.1").
          - **locator**: MAIN:L8/L1/state-space/HUMINT_ENCODE.md:282; aybllc/autonomous origin/main:L8/L0/universality/SCOPE_single_object.md:11-12 and :127-129; ROADMAP:L8/L1/state-space/AUDITON_REPLICATOR.md:17
        - item 9
          - **statement**: AUDITABILITY_REQUIREMENTS.md: heading "The AC controls that do bear — 21" over a 22-row table; exclusion list called "approximately 90 controls" sums to 62 as written and to 61 live controls in Part A; AC-2 is given "+13" enhancements where 12 are live.
          - **locator**: ROADMAP:L8/L1/state-space/AUDITABILITY_REQUIREMENTS.md:172-177, :181-202, :248
        - item 10
          - **statement**: AUDITABILITY_REQUIREMENTS.md: "[source text withheld from the public copy]" under a table with five starred rows (three double-starred).
          - **locator**: ROADMAP:L8/L1/state-space/AUDITABILITY_REQUIREMENTS.md:94-98 and :108
        - item 11
          - **statement**: AUDITABILITY_REQUIREMENTS.md percentages are truncated, not rounded: 96/132 = 72.7% printed 72%; 39/56 = 69.6% printed 69%; 135/188 = 71.8% printed 71% (the 71% is the headline of §2).
          - **locator**: ROADMAP:L8/L1/state-space/AUDITABILITY_REQUIREMENTS.md:49-55
        - item 12
          - **statement**: AUDITABILITY_REQUIREMENTS.md quotes three controls in quotation marks in shortened form that drops operative words present in Part A: AU-5(4) omits "unless an alternate audit logging capability exists"; AC-3(10) omits "[source text withheld from the public copy]-24(2) is given as "without user or process identity", which is the control's title paraphrased, not its text.
          - **locator**: ROADMAP:L8/L1/state-space/AUDITABILITY_REQUIREMENTS.md:120-122, :193, :202 vs MAIN:L7/provenance/sources/staging-records/standards/extracted/SP800-53r5_AC-AU_verbatim.md:1079-1082, :231-232, :950-952
        - item 13
          - **statement**: AUDITON_REPLICATOR.md: "[source text withheld from the public copy]" accounts for ten of twelve compartments.
          - **locator**: ROADMAP:L8/L1/state-space/AUDITON_REPLICATOR.md:71
        - item 14
          - **statement**: AUDITON_REPLICATOR.md §7 and its §8 status row still say the SR-family HUMINT question is "under review", while the file's own header and HUMINT_ENCODE §6 record that the review concluded. The header says "TWO OF THREE HEADLINE CLAIMS" over a five-row outcome table.
          - **locator**: ROADMAP:L8/L1/state-space/AUDITON_REPLICATOR.md:577, :589-590, :608 vs :3, :12
        - item 15
          - **statement**: AUDITON_REPLICATOR.md rests its scope standing on rulings C-007 and C-008 in governance/RULINGS.md; the rulings register in the companion repository is a 1-byte empty file, as the companion's own records state.
          - **locator**: ROADMAP:L8/L1/state-space/AUDITON_REPLICATOR.md:17-18, :29; aybllc/autonomous origin/main:L8/L5/research/review/RULINGS.md (1 byte); aybllc/autonomous origin/main:L8/L5/research/review/0.md:39
        - item 16
          - **statement**: BETA adds L8/L1/state-space/AUDITONOMOUS_BETA_ADMISSION.md without updating either Layer 1 sheet (both are the MAIN blobs), and the file carries no status label, date or author, against the repository's label discipline.
          - **locator**: BETA:L8/L1/state-space/0.md:35-39; BETA:L8/L1/0.md:107; BETA:L8/L1/state-space/AUDITONOMOUS_BETA_ADMISSION.md:1-5
        - item 17
          - **statement**: BETA inserts its Q13 disposition in the middle of a file whose stated protocol is append-and-strike (between Q12 and Q13); Q13 itself is neither struck nor annotated.
          - **locator**: BETA:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:268-273; protocol at :8-9
        - item 18
          - **statement**: The restore record says L0 and L1 received "[source text withheld from the public copy]" but its own table places three files there (AUDITONOMY.md at L0; AUDITON_REPLICATOR.md and AUDITABILITY_REQUIREMENTS.md at L1).
          - **locator**: ROADMAP:L8/L6/history/restore-2026-09-14.md:18 vs :54-55
        - item 19
          - **statement**: The ROADMAP standards register was restored without an amendment recording that Part B answered Q2a/S11 for AC and AU; it still marks Q2a "blocking" and S11 as to be run.
          - **locator**: ROADMAP:L7/provenance/sources/STANDARDS_REGISTER.md:347-351 and :484-489 vs ROADMAP:L8/L1/state-space/AUDITABILITY_REQUIREMENTS.md:236-237
        - item 20
          - **statement**: Label collision in the BETA findings: "C6 stop and C7 record" (envelope compartments) and "[source text withheld from the public copy]" (rows of CONTRADICTIONS.md) appear in the same short file without distinction.
          - **locator**: BETA:L8/L5/research/findings/AUDITONOMOUS_BETA_FINDINGS.md:9 and :24
        - item 21
          - **statement**: The conflict record for the C6 stop path (FREEZE.md §6c, flagged for the owner's reconciliation) exists only in history; FREEZE.md was deliberately not restored and no current sheet carries the conflict.
          - **locator**: HISTORY:FREEZE.md:228-262; ROADMAP:L8/L6/history/restore-2026-09-14.md:90
      - **open_questions**
        - NASA 14: the fourteen NASA requirements are listed in no file in any state, and the journal the ownership file names is outside the repository. I could not confirm the total of 113 or any E/J/X/D assignment for the NASA, ISO or NIST rows.
        - 78 vs 113: no document gives a breakdown of the 78 or says how the two runs relate. I could not tell whether 78 and 46 are disjoint (requirements and definitions) or overlapping.
        - Why the text says sixteen for IEEE 7009: probably a carry-over from the sixteen Annex A requirements (ASR-001 to ASR-016), but no record says so. If the 113 is meant to count ASR requirements individually, the totals would change (ten more rows), and no document addresses this.
        - HUMINT_ENCODE §6: the term counts over the SR/CM/SA families, the "eleven controls and twenty-seven enhancements" and the 38 blocked accreditation provisions could not be recounted. Part A covers only AC and AU and the accreditation documents are not in the tree.
        - Quotations from ISO, IEEE, UN R157, NASA, EU and DoD instruments in the envelope and HUMINT_ENCODE are labelled VERIFIED by the files, but no locator to a held copy is recorded in Layer 1. I did not check the source staging records under L7/provenance (outside this scope), so I cannot say whether a recorded comparison exists there.
        - The replicator's run: gen_drift.py and gen_drift.out are in no current tree of either repository, only in aybllc/autonomous history (commit c866842). I did not run them. The Monte-Carlo figures (0.008134, 71.0%, 0/20,000) are therefore unreproduced by me; only the closed-form figures were re-derived.
        - Whether the BETA admission's "no stop latch" is intended to take a side between the envelope's non-overridable stop and AUDITONOMY's adjudicated stop. The file does not say and I did not read the BETA computation.
        - Whether AU-6 classed ORG ("not carriable by any object") undermines C11 and the H7 substitute, or is consistent because C11 is "external to the unit". The documents do not address it.
        - Whether the owner regards the ROADMAP restorations (replicator, Part B, register) as part of the research record to be reconciled with BETA. BETA branches from MAIN and holds none of them, so the two candidate states disagree on what exists at Layer 1.
        - The ISO/IEC 22989 clause 5.13 custody question: still marked NOT RE-VERIFIABLE in the companion (aybllc/autonomous origin/main:L8/L0/semantics/definitions/AUTONOMOUS.md:72 and :228). I did not check the companion's beta branch for a change.
    - item 3
      - **key**: formal-engineering
      - **items**: 34
      - **defects**
        - item 1
          - **statement**: The formulas ledger tells users to cite provenance to `uso/l6/LEDGER.md`, a path that does not exist in MAIN; the register was relocated to L7/provenance/sources/LEDGER.md (MAIN:L7/provenance/0.md:33).
          - **locator**: MAIN:L8/L2/formal-mathematics/FORMULAS_LEDGER.md:23
        - item 2
          - **statement**: The L3 sheet attributes 'cell sizing, R ∝ (ρt)^¼' to §7.4 of the 2026-08-05 session. That formula is at §4.3 (session line 217); §7.4 (lines 409-441) is the Goldberg cancellation passage and contains only 'recoverable, not zero'. The approximation sheet (line 34) and the sessions sheet (L8/L4/work/writing/sessions/0.md:16) repeat '§7.4 scaling and precision reasoning'.
          - **locator**: MAIN:L8/L3/0.md:92
        - item 3
          - **statement**: The interlock proposal cites EB:233, EB:38 and LEX:487 with no key legend, and neither cited source file is held in MAIN. They resolve only in ROADMAP (L8/L4/work/writing/auditonomous_ebios_core_architecture_math_source-535f70d_draft.md:233, :38; L7/peering/private/ingress/peer-3/object-1/…v0.2_ea08f59.md:487) and HISTORY (intake/).
          - **locator**: MAIN:L8/L3/engineering-mathematics/PROPOSAL_seal_gated_interlock.md:18-20
        - item 4
          - **statement**: The same manuscript line is keyed LEX:487 in the proposal and EMB:487 in the author's-assertions record.
          - **locator**: MAIN:L8/L3/engineering-mathematics/PROPOSAL_seal_gated_interlock.md:20 versus ROADMAP:L8/L5/research/review/AUTHOR_ASSERTIONS.md:494
        - item 5
          - **statement**: The proposal's status still reads that an [source text withheld from the public copy]'. The text is unchanged since HISTORY (intake/research/PROPOSAL_seal_gated_interlock.md:6-8) and no result of that pass is recorded in MAIN, ROADMAP, BETA or HISTORY.
          - **locator**: MAIN:L8/L3/engineering-mathematics/PROPOSAL_seal_gated_interlock.md:6-8, 168-171
        - item 6
          - **statement**: The priors file uses verdict labels 'ESTABLISHED' and 'NOT TESTED', which are not among the registry labels listed in STATUS_AND_LABEL_DISCIPLINE.md:10-13 or on the status ladder.
          - **locator**: MAIN:L8/L3/engineering-mathematics/uncertainty/PRIORS_EXTERNAL_2026-08-04.md:111-120
        - item 7
          - **statement**: The priors file's header says '[source text withheld from the public copy]', but two verdict rows (NOT-CHECKED, NOT TESTED) cite no source, and the file gives no URL, fetch date or file hash for any quotation.
          - **locator**: MAIN:L8/L3/engineering-mathematics/uncertainty/PRIORS_EXTERNAL_2026-08-04.md:3-4, 119-120
        - item 8
          - **statement**: None of the priors file's sources (Rump, Kearfott, Neumaier, Comba and Stolfi, Stolfi and de Figueiredo) has a pointer row in the source ledger, in MAIN or ROADMAP (git grep for the five names returns no row), although the ROADMAP roadmap line 248 calls three of them 'held'.
          - **locator**: MAIN:L7/provenance/sources/LEDGER.md (no matching row); MAIN:L8/L3/engineering-mathematics/uncertainty/PRIORS_EXTERNAL_2026-08-04.md:10-70
        - item 9
          - **statement**: The priors file refers to internal results with no locator ('the aggregation tested internally', 'the internal finding', '[source text withheld from the public copy] internal documents are not in MAIN, and 'M(n,r)' occurs nowhere else in MAIN.
          - **locator**: MAIN:L8/L3/engineering-mathematics/uncertainty/PRIORS_EXTERNAL_2026-08-04.md:96-102
        - item 10
          - **statement**: In BETA the relations sheet still says 'Nothing is filed at this position' although AUDITONOMOUS_BETA_PREDICATE.md is filed there; the L2 layer and formal-mathematics sheets' Holdings omit it (blobs identical to MAIN).
          - **locator**: BETA:L8/L2/formal-mathematics/relations/0.md:33; BETA:L8/L2/0.md:72-76; BETA:L8/L2/formal-mathematics/0.md:37-39
        - item 11
          - **statement**: In BETA the L3 sheets' Holdings do not list AUDITONOMOUS_BETA_METHOD.md (blobs identical to MAIN).
          - **locator**: BETA:L8/L3/engineering-mathematics/0.md:35-38; BETA:L8/L3/0.md:88-90
        - item 12
          - **statement**: In BETA the formulas ledger still declares itself EMPTY although the beta predicate uses SHA-256 over canonical JSON as a formal object; no row and no change-log entry was added.
          - **locator**: BETA:L8/L2/formal-mathematics/FORMULAS_LEDGER.md:10
        - item 13
          - **statement**: The beta predicate file does not name the L0 and L1 files its symbols bind to (AUDITONOMOUS_BETA_SCOPE.md, AUDITONOMOUS_BETA_ADMISSION.md) and records nothing at proofs/, which the relations sheet asks of a filing (relations/0.md:10).
          - **locator**: BETA:L8/L2/formal-mathematics/relations/AUDITONOMOUS_BETA_PREDICATE.md:1-7
        - item 14
          - **statement**: The beta history cites evidence files T3-red.txt, T3-integration-wait.txt and T3-review-red.json; none is in the BETA tree (ls-tree search).
          - **locator**: BETA:L8/L6/history/AUDITONOMOUS_BETA_HISTORY.md:9-10
        - item 15
          - **statement**: In the ROADMAP sourcebook, the only statement of the autonomy profile is damaged: the equals sign between AP(S,F,D,Δ) and ⟨E,A,G,R,Q⟩ is a row of '=' characters (a heading underline), not an equation.
          - **locator**: ROADMAP:L8/L4/work/writing/sourcebook/Auditonomous_Book_Material_Sourcebook_v0.1.md:65-70
        - item 16
          - **statement**: The definition's Appendix E says [source text withheld from the public copy]/`'; MAIN:L8/L0/semantics/definitions/ holds only 0.md and the definition.
          - **locator**: MAIN:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:367-371
      - **open_questions**
        - Was the adversarial attack pass on the Seal-Gated Interlock ever completed, and where is its result? Searched MAIN, ROADMAP and HISTORY for 'attack pass', 'implicit ack', 'NUGate', 'interlock'; found none.
        - I could not re-verify any external quotation (no network): Rump 2010, Kearfott 1991/2013, Neumaier 2003, Comba and Stolfi 1993, Stolfi and de Figueiredo 1997 and TEMA 4, Goldberg 1991, and the standards behind the SGI's prior-art list. The EXTERNALLY CHECKED states rest on what the files record.
        - Do a conference proceedings paper (SIBGRAPI 1993), a colloquium monograph (1997) and TEMA meet the status ladder's outside-source rule? The priors file calls all of them peer-reviewed without saying how that was established.
        - Where are the 'held' copies of Rump 1999/2010, Comba and Stolfi 1993 and Stolfi and de Figueiredo 1997 that the ROADMAP roadmap (line 248) mentions? No ledger row points to them.
        - The SGI proposal's claim that a grep of eBIOS src/ finds no actuation code, and all eBIOS quotations in the L0 definition, concern the abba-01/ebios repository, which is not among the clones; unconfirmed.
        - Anderson 1972, TCSEC and NIST SP 800-82r3, cited by the SGI proposal as 'verified this session', were not found recorded anywhere in MAIN.
        - I did not run the beta's code or tests (not asked to). The claims '12 tests passed' and the red-run sequence in the beta history are unconfirmed; only the stored result JSON and the pinned hashes were checked.
        - The beta's binding calls itself immutable but pins a producer commit (805cd42) that is on the unmerged Autonomous beta and not on Autonomous main, and an architecture commit (4ca3edb) that is on the unmerged 7LM beta, one commit behind its tip. Whether that is acceptable is the owner's call.
        - Owner decisions that block Layers 2 and 3: register the isomorphism or not; L2 or L3 for the perpetuity argument; L3 or L5 for the priors file; D11 (enclosure regime λ); D20 (which framing of auditonomy governs); the pending line-52 edit to the definition.
        - Should the Auditonomous L2 and L3 sheets take the 7LM beta-tip paragraphs ('Using this position in a research project')? Those paragraphs would bear on where the priors file belongs.
        - Conditions A-E, which the roadmap wants stated formally at L2, are labelled CONJECTURE in the L1 envelope and are defined in a file (AUDITONOMY.md) that is not in MAIN. I did not read the ROADMAP copy (outside scope).
    - item 4
      - **key**: computation
      - **items**: 29
      - **defects**
        - item 1
          - **statement**: The computation sheet contradicts itself: Holdings lists six objects (nine on ROADMAP) while Standing says "It is empty at present." Corrected only on BETA (line 56).
          - **locator**: MAIN:L8/L4/work/computation/0.md:54 against :38-42; ROADMAP same file, same Standing line
        - item 2
          - **statement**: The count 113 cannot be recounted from any tree. The three files give 99; the NASA lane of 14 has no extraction file in MAIN, ROADMAP, BETA or HISTORY. Only NASA-R6 and NASA-R10 are named, once, in the ownership file.
          - **locator**: MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:15 and :157
        - item 3
          - **statement**: MAIN cites the source of the '78' figure at a path that does not exist on MAIN (`intake/research/AUDITON_PACKABILITY_2026-08-04.md:15`). The file exists only on ROADMAP (L8/L5/research/findings/) and in HISTORY.
          - **locator**: MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:19
        - item 4
          - **statement**: All three requirements files refer the reader to `STANDARDS_REGISTER.md` for NASA. No file of that name exists on MAIN or BETA; it exists on ROADMAP at L7/provenance/sources/STANDARDS_REGISTER.md and in HISTORY.
          - **locator**: MAIN:L8/L4/work/computation/nist-requirements-for-autonomouos.md:5 (same sentence at line 5 of the IEEE and ISO files)
        - item 5
          - **statement**: The extractions' evidence trail points outside the repository: workflow journal wf_b00a2270-83e under ~/.claude, PDFs under /home/eric/ayb/auditonomous/intake/sources/, text and hashes under /tmp/claude-1000/…/scratchpad/. None is reachable from the tree, so the VERIFIED label cannot be re-checked from the repository.
          - **locator**: MAIN:L8/L4/work/computation/ieee-requirements-for-autonomouos.md:9, :16, :1033; nist-requirements-for-autonomouos.md:16, :404
        - item 6
          - **statement**: No source-identity rows exist for the three extractions, by the sheet's own statement.
          - **locator**: MAIN:L8/L4/work/computation/0.md:44
        - item 7
          - **statement**: File names are spelled inconsistently: 'autonomouos' in the IEEE and NIST file names and both .odt names, 'auditonomopus' in the sources .odt, 'autonomous' in the ISO file name.
          - **locator**: MAIN:L8/L4/work/computation/ (tree listing)
        - item 8
          - **statement**: The deep-research report carries no resolvable citations in its own text: 43 distinct opaque tokens and zero URLs. The only key is the separate .odt export. The thesis it reviews is not on MAIN or BETA.
          - **locator**: MAIN:L8/L4/work/computation/deep-research-auditonomous.md:16, :19
        - item 9
          - **statement**: The ROADMAP sheet says the SSOT was "produced by the deep-research run". The file's own text is a conversational reply that refers to "the uploaded review" and "The current research report", and the verification log calls it 'pasted'.
          - **locator**: ROADMAP:L8/L4/work/computation/0.md:44 against ROADMAP:L8/L4/work/computation/all-research-corpus-auditonomous.md:8, :168-170
        - item 10
          - **statement**: The OMMP README's corrected pass count is itself off by one against a re-run: it says 66/66; the suite prints 65 PASS check lines plus an 'ALL PASS' banner.
          - **locator**: ROADMAP:L8/L4/work/computation/ommp/README.md:257-264
        - item 11
          - **statement**: Research records and the OMMP files still cite the probes and tests by pre-restore paths: `intake/research/energy_reserve_probe.py`, `intake/research/energy_logistics_probe.py`, `intake/research/emission_thrust_probe.py`, `intake/research/nu_enclosure_probe.py`, `tools/ommp/../../research/tictac_calc.py`, `python3 tools/ommp/test_ommp.py`.
          - **locator**: ROADMAP:L8/L5/research/review/AUTHOR_ASSERTIONS.md:843, :1020, :1085; NASA_PAPER_DEFECT_LEDGER.md:33; TICTAC_PROPULSION_ADJUDICATION.md:15; ROADMAP:L8/L4/work/computation/ommp/README.md:57; ommp/test_ommp.py:1
        - item 12
          - **statement**: dr001_half_cell.py prints a sampled ratio of 15/8 under the label "(the factor of 2 DR-001 claims)".
          - **locator**: ROADMAP:L8/L4/work/computation/probes/dr001_half_cell.py:39-40
        - item 13
          - **statement**: The beta history cites evidence files that are not in the BETA tree: `T3-red.txt`, `T3-integration-wait.txt`, `T3-review-red.json` / `.txt`, and "implementation evidence" holding the green test result and CLI execution. No test-evidence file is committed beside the result.
          - **locator**: BETA:L8/L6/history/AUDITONOMOUS_BETA_HISTORY.md:9-11
        - item 14
          - **statement**: The beta result is not byte-reproducible across interpreters because it embeds the Python version; a re-run under 3.13.16 differs from the committed file in that one field.
          - **locator**: BETA:L8/L4/work/computation/auditonomous_beta.py:180; BETA:L8/L4/work/computation/auditonomous_beta_result.json:18
        - item 15
          - **statement**: The beta 'fault correction' records describe a fresh rebuild after each injected fault, not a repair of the faulted packet; 'corrected_outcome.validation' is therefore true by construction.
          - **locator**: BETA:L8/L4/work/computation/auditonomous_beta.py:281-282
        - item 16
          - **statement**: The beta binding pins commits that are on beta branches only: producer 805cd42 is not an ancestor of autonomous origin/main, and architecture 4ca3edb is not an ancestor of 7lm origin/main (it is an ancestor of 7lm beta 97314c5).
          - **locator**: BETA:L7/peering/public/ingress/peer-1/object-2/binding.json (producer_commit, architecture_commit)
      - **open_questions**
        - What the '78 requirements extracted, 46 definitions captured' run comprised and how it relates to the 113. L1 calls it 'a different, smaller run', yet the packability file describes the same four lanes on the same day; no reconciliation exists.
        - Where the 14 NASA rows are. They are counted at L1 but exist in no tree; recovery needs the workflow journal, which is outside the repository.
        - Q11: the auditability-requirements extraction has not been run (L1 §8; beta findings line 24).
        - Whether the deep-research report's eight register corrections and six 'overtaken' rulings were ever adjudicated. MAIN records none. I did not trace ROADMAP registers beyond finding '2026/1744' in STANDARDS_CITED.md.
        - Whether the report's external claims are true (Regulation (EU) 2026/1744, [source text withheld from the public copy], the 2026 action-certificate preprints, the Vaara draft). Not checked: no network in this pass.
        - The prompt that started the deep-research run is in neither export.
        - Whether the SSOT came from the deep-research run or from a later chat turn.
        - Whether the OMMP README's 66 counted the 'ALL PASS' banner, or whether the suite emitted 66 check lines under Python 3.14.4. Only 3.13.16 was available.
        - Whether the beta result is byte-identical when regenerated under Python 3.14.4.
        - Whether the beta branch was made by Codex. The commit author and committer are 'EDM' and the commit has no generator trailer; the files searched carry no such trace.
        - Whether any of the ROADMAP probes or the BETA fixture should be filed under experiments/ rather than computation/. The experiments sheet is unchanged on both branches.
        - The 35 KB ommp.py and README lines 76-244 were not read line by line, and the 187 KB sources export was sampled after its first 84 lines.
    - item 5
      - **key**: review-core
      - **items**: 32
      - **defects**
        - item 1
          - **statement**: Every cross-link in CONTRADICTIONS.md is dead on MAIN and BETA. It links, as same-directory files, to STANDARDS_REGISTER.md, ISO_IEC_REQUIREMENTS.md, IEEE_REQUIREMENTS.md, NIST_REQUIREMENTS.md and AUTONOMY_AT_DISTANCE.md, and cites intake/sources/standards/SOURCE_LEDGER.md. The three extractions survive under other names at L8/L4/work/computation/ (ieee-requirements-for-autonomouos.md, iso-iec-requirements-for-autonomous.md, nist-requirements-for-autonomouos.md); STANDARDS_REGISTER.md and AUTONOMY_AT_DISTANCE.md exist only on ROADMAP and in HISTORY. No sheet maps old names to new.
          - **locator**: MAIN:L8/L5/research/review/CONTRADICTIONS.md:10, 15-17, 46-48, 71-72, 90, 113-114, 140-143, 167, 188, 209-210
        - item 2
          - **statement**: The agreement paragraph quotes IEEE 7009 cl. 1.3.2(e) [source text withheld from the public copy]"; the extraction it draws on reads "[source text withheld from the public copy]". The file says every quote is verbatim and VERIFIED.
          - **locator**: MAIN:L8/L5/research/review/CONTRADICTIONS.md:198-199 against MAIN:L8/L4/work/computation/ieee-requirements-for-autonomouos.md:874, 1043
        - item 3
          - **statement**: C2 states an unconditional incompatibility; the full entry it cites makes it conditional on an external authorizer and labels IEEE's intent UNVERIFIED.
          - **locator**: MAIN:L8/L5/research/review/CONTRADICTIONS.md:60-63 against MAIN:L8/L4/work/computation/ieee-requirements-for-autonomouos.md:857, 874, 993
        - item 4
          - **statement**: C4's heading says "The identical behaviour"; its body says "Near-identical behaviour". Its ISO 8373 quotation also drops the term-number marker "(3.1)" that the extraction prints.
          - **locator**: MAIN:L8/L5/research/review/CONTRADICTIONS.md:94, 98, 101 against MAIN:L8/L4/work/computation/iso-iec-requirements-for-autonomous.md:341
        - item 5
          - **statement**: The link mark for '[source text withheld from the public copy]' is defined and never used in the file.
          - **locator**: MAIN:L8/L5/research/review/CONTRADICTIONS.md:12
        - item 6
          - **statement**: BETA inserts a section at the top of a file that declares itself append-and-strike and that the review sheet and the routing plan describe as not edited; BETA's review/0.md is unchanged and does not mention the new section.
          - **locator**: BETA:L8/L5/research/review/CONTRADICTIONS.md:9, 22-35; BETA:L8/L5/research/review/0.md:35
        - item 7
          - **statement**: BETA's row for C2 routes "[source text withheld from the public copy]"; the bound blob contains no mention of IEEE 1920.1. The same blob lacks IEEE 7007 (row C3), ISO/IEC 25059 (row C7), ALFUS Volume II (row C6), IEEE 7001 cl. 4.2 (row C1) and ISO 8373 cl. 6.13.4 (row C4).
          - **locator**: BETA:L8/L5/research/review/CONTRADICTIONS.md:28-34 against autonomous blob ffbdc28be7b47a83c9354526ac034596ba7b6e9a (rows A1-A11 at lines 70-80)
        - item 8
          - **statement**: The adjudication's ledger says "Claims Evaluated: 16 (see §10)"; the section 10 table has 19 claim rows.
          - **locator**: MAIN:L8/L5/research/review/PERPETUITY_QUESTION_ADJUDICATION.md:293-311, 341
        - item 9
          - **statement**: Two rows of the labels summary (von Neumann constructor architecture; branching dichotomy) have no section in the body. Sources Acta Numerica 19 (2010) and PNAS 120 (2023) appear only in the ledger entry, and Encyclopedia of Mathematics only in the fidelity grading.
          - **locator**: MAIN:L8/L5/research/review/PERPETUITY_QUESTION_ADJUDICATION.md:310-311, 327, 339
        - item 10
          - **statement**: Fetch-layer-relayed quotes are labelled inconsistently: PARTIALLY VERIFIED for the J. Math. Biol. and PNAS quotes, VERIFIED for the NIST handbook, Dyson and Winfield quotes, although the file's own fidelity grading lists all of them as relayed and to be confirmed.
          - **locator**: MAIN:L8/L5/research/review/PERPETUITY_QUESTION_ADJUDICATION.md:67, 73 against 76, 110, 197; grading at 327
        - item 11
          - **statement**: Stale internal locator: the constitutional sentence is cited at manuscript/Block_03_The_Definition.md:10. That was right at commit 5a8d533 (2026-08-02); from 314ceba (2026-08-04) through HISTORY and ROADMAP it is at line 1 and line 10 reads "**II. The permissions triad**". The block files and intake/AUTONOMY_SCALE.md that the file cites are not on MAIN or BETA at all.
          - **locator**: MAIN:L8/L5/research/review/PERPETUITY_QUESTION_ADJUDICATION.md:135, 246, 252, 285
        - item 12
          - **statement**: On BETA the definition's "NOT audited-after-the-fact" bullet is at line 54 and line 52 is blank, so every reference to "AUDITONOMOUS_DEFINITION.md:52" on BETA points at the wrong line.
          - **locator**: BETA:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:52-54; BETA:L8/L5/research/review/0.md:44; BETA:L8/L5/research/review/PERPETUITY_QUESTION_ADJUDICATION.md:216
        - item 13
          - **statement**: The MAIN copies of both review documents were reformatted after HISTORY (table padding, blank lines). Text is unchanged, but line numbers moved: the consolidated document's PERP:207 and PERP:221 are lines 208 and 222 on MAIN.
          - **locator**: MAIN:L8/L5/research/review/PERPETUITY_QUESTION_ADJUDICATION.md:208, 222 against HISTORY:intake/research/PERPETUITY_QUESTION_ADJUDICATION.md:207, 221
        - item 14
          - **statement**: The status ladder says promotions are logged in "the register" and cites AUDITONOMOUS.md:1230 for its outside-source rule. Neither a register nor that file exists on MAIN or BETA.
          - **locator**: MAIN:L8/L5/research/review/STATUS_LADDER.md:14, 25
        - item 15
          - **statement**: L8/L5/0.md lists only CONTRADICTIONS.md and PERPETUITY_QUESTION_ADJUDICATION.md as review holdings; the directory also holds STATUS_LADDER.md, STATUS_AND_LABEL_DISCIPLINE.md and autonomous-theory/.
          - **locator**: MAIN:L8/L5/0.md:80
        - item 16
          - **statement**: Four different schemes share the letter C: C1-C7 (standards conflicts), C-1 to C-23 (internal contradictions, HISTORY and ROADMAP), C-1 to C-10 (session corrections in ROADMAP's SESSION_2026-08-05_VERIFICATION_LOG.md) and C-001 onward (governance rulings, cited as C-002 on MAIN). A criteria list numbered C1-C13 also appears in ROADMAP's vocabulary paper.
          - **locator**: MAIN:L8/L5/research/review/CONTRADICTIONS.md:32; HISTORY:AUDITONOMOUS.md:1123; ROADMAP:L8/L4/work/writing/sessions/SESSION_2026-08-05_VERIFICATION_LOG.md:50; MAIN:L8/L5/research/findings/DISTILLATION.md:67
      - **open_questions**
        - No standard, paper or PDF was opened. Every quote I call confirmed was matched against another record inside the repositories (reading records, extractions, capture records), never against the publisher's text. The held IEEE PDFs are licensed and not in the repository.
        - Which wording of IEEE 7009 cl. 1.3.2(e) is correct, singular (CONTRADICTIONS.md) or plural (the extraction)? Only the PDF settles it.
        - [source text withheld from the public copy] 5 really classed Heteronomous? Auditonomous holds a capture that says so; the bound Autonomous definition lists it as an outstanding attack line (possible inference from a merged cell) and downgrades the Table 1 row to PARTIALLY VERIFIED. C4 depends on it.
        - Did the owner rule which rows of C1-C7 are Autonomous's before the BETA section was written? MAIN reserves that edit to the owner; no ruling is recorded in scope.
        - Where does Autonomous record the disagreements this repository is meant to consume? grep of the autonomous repository (origin/main and beta/7lm-exemplar-autonomous) finds no copy of the 1920.1 definition, the 7007 Annex A sentence or the ALFUS Volume II sentence. I searched by exact phrase only.
        - The owner's own words for the DEAD FOR NOW ruling were not found. I searched text files on MAIN, ROADMAP and HISTORY by grep; I did not search the Office files or chat volumes.
        - Audit necessarily post hoc (adjudication section 6.1) or not (CYCLES verdict ii): the two files are unranked, and I did not assess their evidence against each other.
        - Whether the VERIFIED labels in the adjudication meet the ladder's outside-source rule where the text came from institutional mirrors, fetch-layer relays or index sweeps that include Google Scholar. The rule was restated on 2026-08-08, after the file's date.
        - Whether the three next required checks in the adjudication (publisher-of-record captures; relayed quotes against publisher PDFs; bounded-commitment claim against the logging literature) were ever run. Nothing in scope says so; I did not search ROADMAP's SOURCE_REQUESTS.md or RESEARCH_DOCKET.md.
        - Whether any of C-1 to C-23 changed status after 2026-08-04. I read the register as it stood at HISTORY and did not trace later rulings or re-verify its 23 entries.
    - item 6
      - **key**: lanes
      - **items**: 50
      - **defects**
        - item 1
          - **statement**: The sheet says the ledger holds clusters C1–C6 and tensions T1–T11. The ledger holds C1–C11 and T1–T16. The same miscount is in the routing plan the sheet was written from.
          - **locator**: MAIN:L8/L5/research/lanes/0.md:36; MAIN:L8/L5/research/lanes/THEME_LEDGER.md:15-138, 146-298; MAIN:L8/L6/history/7LM_ROUTING_PLAN_2026-09-05.md:172
        - item 2
          - **statement**: T3 states as 'fixed (textual observation, not interpretation)' that the definite article appears twice, on two verbs. The archive has a third exact occurrence on the third verb, '[source text withheld from the public copy]), plus three near-variants (ARCH:47, 90, 580). The ledger quotes ARCH:593 in T11 without registering it. ROADMAP's roadmap D3 counts 'six claimants in the archive'.
          - **locator**: MAIN:L8/L5/research/lanes/THEME_LEDGER.md:156, 160, 288; ROADMAP:L8/L4/work/writing/manuscript/Auditonomous_Theory_Master_Archive.md:47, 90, 210, 232, 580, 593; ROADMAP:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:614
        - item 3
          - **statement**: T1's closure (blocks 31, 32, 35, 36 cut) is not carried through the ledger: C1 and C5 still list them as members and quote cut text (ARCH:384, 426, 430); the block index still defines '(stub)' as a placeholder 'while the archive carries full text' and says the chapter mapping '[source text withheld from the public copy]'; T7 remains a live tension though one side is cut Block 36.
          - **locator**: MAIN:L8/L5/research/lanes/THEME_LEDGER.md:17, 23, 62, 68-69, 280, 304, 323, 325, 335
        - item 4
          - **statement**: T1 was rewritten from 'RESOLVED 2026-08-02 by the author; NOT a defect' to 'CLOSED 2026-08-02 by the author … CUT FROM THE BOOK' in commit 314ceba dated 2026-08-04, whose message concerns an IEEE standards reading and does not mention the change; the ledger's header date stays 2026-08-02. The TOC's 'cut from the book … 2026-08-02' wording entered in the same commit.
          - **locator**: commit 314ceba (2026-08-04 12:55:59 -0700) on intake/research/THEME_LEDGER.md and intake/manuscript/Auditonomous_Theory_TOC.md; MAIN:L8/L5/research/lanes/THEME_LEDGER.md:3, 146
        - item 5
          - **statement**: T3 was once recorded as 'DEFINED AND BOUNDED 2026-08-02 … Definition adopted' (locally scoped reading) and reverted to OPEN 28 minutes later. The present entry records the withdrawn 'imposed requirement' but not that a definition was adopted and withdrawn; that version is visible only in git history, against the status ladder's rule that the wrong version stay visible.
          - **locator**: commits 3406bd1 and 5762d10 on intake/research/THEME_LEDGER.md; MAIN:L8/L5/research/lanes/THEME_LEDGER.md:158, 272; MAIN:L8/L5/research/review/STATUS_LADDER.md:25-26
        - item 6
          - **statement**: The ledger header promises 'An adversarial quote audit follows this ledger.' None follows in the file, and the phrase 'quote audit' occurs nowhere else in MAIN, ROADMAP or HISTORY.
          - **locator**: MAIN:L8/L5/research/lanes/THEME_LEDGER.md:7
        - item 7
          - **statement**: T3 contains stale statements overtaken later in the same entry: '[source text withheld from the public copy]' and 'Findings pending' stand beside the reported ISO lane; the summary table and the sentence 'Exactly one surveyed instrument holds all three' are not marked superseded (only the convergence paragraph is).
          - **locator**: MAIN:L8/L5/research/lanes/THEME_LEDGER.md:201, 203, 221, 247, 249, 272
        - item 8
          - **statement**: Q5 and Q6c still read 'PENDING — lane running' and 'Nothing … is asserted until it reports'. The outcomes are recorded only in RESEARCH_DOCKET.md (H2: 'UNSUPPORTED and contradicted'; C5: 'Answered'), which exists on ROADMAP and HISTORY but not on MAIN. On MAIN the two lanes read as never having reported.
          - **locator**: MAIN:L8/L5/research/lanes/RECORD_ONTOLOGY_OPEN_QUESTIONS.md:140, 195; ROADMAP:L8/L5/research/review/RESEARCH_DOCKET.md:111-112, 190
        - item 9
          - **statement**: Q5's candidate resolution is labelled UNVERIFIED in the question file, while a findings file on MAIN says it is 'now PARTIALLY VERIFIED' against ARIES. The question file was not updated. The findings file cites the passage at line 134; it is at line 138 on MAIN.
          - **locator**: MAIN:L8/L5/research/lanes/RECORD_ONTOLOGY_OPEN_QUESTIONS.md:138; MAIN:L8/L5/research/findings/SEGREGATION_AND_FORGETTING_2026-08-04.md:125, 142
        - item 10
          - **statement**: The sheet says the ledger is 'carried unchanged'. The words are unchanged, but the reorganisation commit 8c98573 reformatted tables and spacing (ledger 309 to 355 lines; question file 250 to 255), so line locators written against the earlier files are stale: SOURCE_REQUESTS cites THEME_LEDGER:155 for the citator item, which was at 161 in HISTORY and is at 189 on MAIN.
          - **locator**: MAIN:L8/L5/research/lanes/0.md:36; ROADMAP:L8/L5/research/review/SOURCE_REQUESTS.md:159; MAIN:L8/L5/research/lanes/THEME_LEDGER.md:189
        - item 11
          - **statement**: Q1 says all table rows were '[source text withheld from the public copy]'. That file contains no mention of Micron or US10846955B2, the camera-layer row, which Q6c later relies on as part of 'the verified set'.
          - **locator**: MAIN:L8/L5/research/lanes/RECORD_ONTOLOGY_OPEN_QUESTIONS.md:21, 25, 189; MAIN:L8/L5/research/review/PERPETUITY_QUESTION_ADJUDICATION.md:256-275
        - item 12
          - **statement**: The question file is out of order and its closing cross-reference is out of date: Q4 follows Q9 with no status word, and the pointer to T3 says 'three literature lanes reported' where the ledger reports four (the ISO retrieval lane).
          - **locator**: MAIN:L8/L5/research/lanes/RECORD_ONTOLOGY_OPEN_QUESTIONS.md:246, 255; MAIN:L8/L5/research/lanes/THEME_LEDGER.md:249
        - item 13
          - **statement**: The archive itself was not corrected for the T1 cut: its chapter mapping still assigns Blocks 31, 32, 35 and 36 to chapters and its open items still speak of 'Blocks 33–36, Egypt through Enoch'. The ledger notes the mapping in its block index but lists no correction.
          - **locator**: ROADMAP:L8/L4/work/writing/manuscript/Auditonomous_Theory_Master_Archive.md:723-724, 727-728, 748; MAIN:L8/L5/research/lanes/THEME_LEDGER.md:335
        - item 14
          - **statement**: Two ledger locators are inexact by the ledger's own wording ('ARCH:270 vicinity'; 'ARCH:588–592 vicinity'; 'DEF:255–256 vicinity'), against its header claim that every quote carries a grep line number.
          - **locator**: MAIN:L8/L5/research/lanes/THEME_LEDGER.md:5, 91, 288, 292
      - **open_questions**
        - On what date did the owner rule that 'skipped' means cut? The entry says 2026-08-02; the commit that wrote it is dated 2026-08-04 and its message does not mention it. Not settled from the record.
        - Did the 'adversarial quote audit' announced in the ledger header ever exist? Not found in MAIN, ROADMAP or HISTORY by the phrase 'quote audit'; I did not search under other names.
        - Every external quotation in T3 and in Q1 to Q3 is labelled VERIFIED by the repository; I could not re-fetch any (no network), and only ARIES is held (reading record on MAIN, PDF in HISTORY). The EXTERNALLY CHECKED state I assign rests on the repository's own record.
        - Does ISO 15489-1:2016 clause 5.2.2.1 keep the concealment language? Recorded as an UNVERIFIED lead in T3 and as open request SR-03 on ROADMAP. If it was dropped, the one standards-body instrument holding all three verbs is a superseded edition.
        - Current authoritative status of Bronston and Chiarella (no citator run) and the content of Tiersma (1990): both NOT-CHECKED in the record.
        - Where is the full report of the Q5 real-time/embodiment lane and the Q6c liveness lane? I found only the outcome summaries in ROADMAP/HISTORY RESEARCH_DOCKET.md; I did not search L8/L6/retired/consolidated-2026-08-04/AUDITONOMOUS.md (ROADMAP) beyond a filename hit.
        - Is Q9 (assumes state vs checks state) adopted anywhere on BETA? The lanes files are identical on BETA, but BETA's AUDITONOMOUS_DEFINITION.md blob differs from MAIN and I did not read it beyond locating the line-52 bullet (line 54 there, same wording).
        - Whether the Block_37:18 uncleaned fragment is an intended addition or contamination (T9) is for the owner; nothing in the record says.
        - The embodied-manuscript hash can only be settled against nu-algebra commit ea08f59, which is not available in these clones.
        - What intake/sources/ held on 2026-08-02: the ledger says the directory existed and was unread; HISTORY tracks no files under it.
        - The owner's Q9 sentence is recorded with an ellipsis ('[source text withheld from the public copy] full wording is not in the lanes files.
    - item 7
      - **key**: findings
      - **items**: 29
      - **defects**
        - item 1
          - **statement**: MAIN CONTRADICTIONS.md cites and links AUTONOMY_AT_DISTANCE.md (three places), a finding that is not on MAIN (ROADMAP and HISTORY only). It also links STANDARDS_REGISTER.md (ROADMAP only) and ISO_IEC_REQUIREMENTS.md, IEEE_REQUIREMENTS.md, NIST_REQUIREMENTS.md, for which no file of those names exists in MAIN, ROADMAP or BETA.
          - **locator**: MAIN:L8/L5/research/review/CONTRADICTIONS.md:10, :15-17, :46, :68, :72
        - item 2
          - **statement**: The three MAIN findings cite line locators into files that are absent from MAIN: ARCH:364 (Master Archive, ROADMAP only), EB:233 (engineering draft, ROADMAP only), RESEARCH_DOCKET.md:34 (ROADMAP only), AUDITONOMOUS.md §2.8 (retired copy on ROADMAP only), tools/ommp (ROADMAP at L8/L4/work/computation/ommp/). The locators themselves are accurate on the ROADMAP copies.
          - **locator**: MAIN:L8/L5/research/findings/OVERRIDE_NECESSITY_2026-08-04.md:14, :169, :244, :281; MAIN:L8/L5/research/findings/SEGREGATION_AND_FORGETTING_2026-08-04.md:74
        - item 3
          - **statement**: DISTILLATION cites `research/THESIS_auditonomous_override.md` and `research/replicator-lane/`, which have never existed in the auditonomous repository at any commit; they exist only in aybllc/autonomous history (deleted at ab8f01f). Its relative paths `../definitions/AUTONOMOUS.md` and `definitions/AUDITONOMY.md` do not resolve from L8/L5/research/findings/.
          - **locator**: MAIN:L8/L5/research/findings/DISTILLATION.md:15, :21, :59, :85
        - item 4
          - **statement**: DISTILLATION is internally stale: law L6 says '[source text withheld from the public copy]', while the section 4 table and section 7.4 of the same file mark the mechanism-design row VERIFIED (components) and section 6 says the acquisition was 'closed 2026-08-05'. Law L2 likewise still carries Green 2022 as 'NOT-CHECKED — located, not retrieved'.
          - **locator**: MAIN:L8/L5/research/findings/DISTILLATION.md:99-101 versus :124, :146, :273-285; :55-56
        - item 5
          - **statement**: DISTILLATION section 7 says full source lists [source text withheld from the public copy]'. No such record is in the repository: the legal and economics case names occur on MAIN only inside DISTILLATION.md.
          - **locator**: MAIN:L8/L5/research/findings/DISTILLATION.md:151-152
        - item 6
          - **statement**: DISTILLATION says 'Ten definitions are on record (... A1–A11)'; the bound AUTONOMOUS.md in aybllc/autonomous has eleven rows A1-A11 ([source text withheld from the public copy] ISO standard). The count and the label range do not match as written.
          - **locator**: MAIN:L8/L5/research/findings/DISTILLATION.md:14-15; autonomous origin/main:L8/L0/semantics/definitions/AUTONOMOUS.md:70-80
        - item 7
          - **statement**: OVERRIDE_NECESSITY presents a cleaned sentence in quotation marks as the docket's prior statement; the docket's verbatim owner text is "[source text withheld from the public copy] normalisation is not flagged.
          - **locator**: MAIN:L8/L5/research/findings/OVERRIDE_NECESSITY_2026-08-04.md:12-13; ROADMAP:L8/L5/research/review/RESEARCH_DOCKET.md:12
        - item 8
          - **statement**: OVERRIDE_NECESSITY tags the IEEE 7001 cl. 5.2.2 recorder passage '(NORMATIVE)'; the reading record for the same passage says 'MIXED' and that it applies to an independent external device, not the EDR. The staging FINDINGS file says NORMATIVE. The two staging records disagree with each other.
          - **locator**: MAIN:L8/L5/research/findings/OVERRIDE_NECESSITY_2026-08-04.md:187-188; MAIN:L7/provenance/sources/staging-records/ieee/reading/IEEE-7001.md:119; MAIN:L7/provenance/sources/staging-records/ieee/FINDINGS_2026-08-04.md:105
        - item 9
          - **statement**: SEGREGATION_AND_FORGETTING cites RECORD_ONTOLOGY_OPEN_QUESTIONS.md:134; on MAIN that paragraph is at line 138 (it was at 134 in HISTORY). The lane file still reads 'UNVERIFIED' for the Q5 candidate resolution; the finding's upgrade to PARTIALLY VERIFIED was not carried into it.
          - **locator**: MAIN:L8/L5/research/findings/SEGREGATION_AND_FORGETTING_2026-08-04.md:125-126, :142; MAIN:L8/L5/research/lanes/RECORD_ONTOLOGY_OPEN_QUESTIONS.md:138
        - item 10
          - **statement**: At least thirty works cited in the findings have no LEDGER row and no staging record, against the LEDGER's own rule, and the LEDGER's 'Not held' table is empty although the findings name unobtained works. NIST SP 800-53 has an extraction but no LEDGER row.
          - **locator**: MAIN:L7/provenance/sources/LEDGER.md:10-12, :98-100 (see item K6 for the list)
        - item 11
          - **statement**: OMMP_ATTACHMENT_GAP says '[source text withheld from the public copy] three strings are 10 + 10 + 8 = 28 bytes.
          - **locator**: ROADMAP:L8/L5/research/findings/OMMP_ATTACHMENT_GAP_2026-08-04.md:84
        - item 12
          - **statement**: AUDITON_PACKABILITY asserts '9 irreducible conflicts' but does not enumerate nine; explicit 'Resolvable? NO' verdicts appear in sections 1, 4 and 5 only. Its section 8 tally table has no IEEE row and sums to 58 of the stated 78 requirements. The NASA document's SHA-256 is given only as a truncated prefix ('03a0793d…') found nowhere else on ROADMAP.
          - **locator**: ROADMAP:L8/L5/research/findings/AUDITON_PACKABILITY_2026-08-04.md:21, :77-78, :214-218
        - item 13
          - **statement**: AUDITON_PACKABILITY cites `intake/AUTONOMY_SCALE.md:113`; that file is in HISTORY only (the line is accurate there) and is not on MAIN, ROADMAP or BETA.
          - **locator**: ROADMAP:L8/L5/research/findings/AUDITON_PACKABILITY_2026-08-04.md:118; HISTORY:intake/AUTONOMY_SCALE.md:113
        - item 14
          - **statement**: AUTONOMY_AT_DISTANCE rests its Part A/Part B split and three rules on FREEZE.md (P1, P2, P3, §6c), which exists only in HISTORY. Its A3 check names the clause-3 terms extract 'held in this repository'; the LEDGER records that extract as not routed (poisoned lineage, git history only), so only the captures-file half of the check can be repeated.
          - **locator**: ROADMAP:L8/L5/research/findings/AUTONOMY_AT_DISTANCE.md:6, :28-36, :259, :348; MAIN:L7/provenance/sources/LEDGER.md:139-142
        - item 15
          - **statement**: AUDITONOMOUS_BETA_FINDINGS.md uses 'C6' and 'C7' in two senses in one file: envelope compartments (C6 Gate/stop, C7 Record; '32 C7 records') and CONTRADICTIONS.md rows ('[source text withheld from the public copy]').
          - **locator**: BETA:L8/L5/research/findings/AUDITONOMOUS_BETA_FINDINGS.md:7, :9, :24; MAIN:L8/L1/state-space/AUDITON_ENVELOPE.md:129-130
        - item 16
          - **statement**: No finding carries the fields the sheet and the retired rules require in that form (review status; evidence table with Source IDs; a section headed 'What this does not establish'; one claim per file). The sheet grandfathers only DISTILLATION as a multi-claim import; OVERRIDE_NECESSITY (five propositions) and SEGREGATION_AND_FORGETTING (two claims) are also multi-claim. No finding cites a source by its LEDGER id.
          - **locator**: MAIN:L8/L5/research/findings/0.md:19, :35, :39; MAIN:L8/L6/retired/layout-2026-08-14/research/findings/README.md (Required structure)
        - item 17
          - **statement**: MAIN and ROADMAP findings sheets point the released form of a finding to `L7/publications/`; the current 7LM (origin/main c9dc061) and BETA use `L7/allications/publications/`. The MAIN and ROADMAP sheets are behind the model.
          - **locator**: MAIN:L8/L5/research/findings/0.md:31; BETA:L8/L5/research/findings/0.md:31; 7lm origin/main:L7/0.md:22
        - item 18
          - **statement**: MAIN REQUIREMENTS_OWNERSHIP.md cites `intake/research/AUDITON_PACKABILITY_2026-08-04.md:15`, a path that does not exist on MAIN (the file is at L8/L5/research/findings/ on ROADMAP only).
          - **locator**: MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:19
        - item 19
          - **statement**: MAIN LEDGER search log says '22 new rows' but enumerates 21 (STD-026…034 = 9, INST-002…004 = 3, PR-014…020 = 7, EXC-001/002 = 2). The correction exists only on BETA.
          - **locator**: MAIN:L7/provenance/sources/LEDGER.md:113; BETA:L7/provenance/sources/LEDGER.md:147-149
        - item 20
          - **statement**: The findings sheet on BETA lists the beta finding but not the four ROADMAP findings, and the ROADMAP sheet lists the four but not the beta finding; no state has a sheet listing all eight.
          - **locator**: BETA:L8/L5/research/findings/0.md:35-39; ROADMAP:L8/L5/research/findings/0.md:35-42
      - **open_questions**
        - Where is the 'session record' that DISTILLATION section 7 says preserves the full source lists and verbatim legal and economics quotations? I searched MAIN and ROADMAP for the case names and found only DISTILLATION itself (and EB_RECEIPT_RIGOR_SPEC on ROADMAP for two of them); MAIN:L7/provenance/lineage/2026-08-05-observed-not-observable-session-provenance.md does not contain them.
        - Which position on Q13 stands: MAIN's 'cannot be autonomous ... by construction', AUTONOMY_AT_DISTANCE's withdrawal of 'scores zero', or BETA's 'not adopted as a present conformance' wording? No owner ruling found in my scope.
        - What are the nine irreducible conflicts of AUDITON_PACKABILITY? The adjudication output is not in the repository; REQUIREMENTS_OWNERSHIP places the related journal at a path outside the repository.
        - Is the 78 run simply the 113 run with a smaller IEEE lane (20 instead of 55)? The other three lane counts coincide; the 78 run's IEEE count is not recorded, so I could not settle it.
        - Does the owner's decision in AUTONOMY_AT_DISTANCE B6 ('the refusal DISPOSES') stand, and has 'return' been classified under IEEE 7009 (7009-R5/R6)? The finding says nobody has performed it; I found no later record in my scope.
        - EB:233 versus the one-way carrier: has the owner chosen, and were the adversarial attack findings folded into the Seal-Gated Interlock proposal? I read only the first 60 lines of the proposal.
        - The bootstrapping objection and the recall-policy sealing requirement: both are marked unanswered in the findings; I found no answer in my scope.
        - Has any finding been reviewed? No review record naming a finding was found in MAIN:L8/L5/research/review/ (files there: CONTRADICTIONS, PERPETUITY_QUESTION_ADJUDICATION, STATUS files, autonomous-theory). PERPETUITY_QUESTION_ADJUDICATION.md (42 KB) and the ROADMAP review files were not read.
        - I could not check any quotation against the source PDFs (they are in the l6 archive, not in these clones); 'EXTERNALLY CHECKED' above means the comparison is recorded in a reading record with a locator and I found the words there.
        - The eBIOS run reported in OVERRIDE_NECESSITY section 5 is against an external repository (github.com/abba-01/ebios) and could not be reproduced here.
        - I did not run the beta test suite or the beta computation (the task did not ask). BETA:L8/L6/history/AUDITONOMOUS_BETA_HISTORY.md claims 'The final full computation suite passed 12 tests'; that is unconfirmed by me. I did not recompute the record digests.
        - The 'Morton seam' demonstration that UHA_AS_MAP says was 'Demonstrated separately this session' was not located.
        - What the manuscript needs from these findings was not mapped chapter by chapter here; the three manuscript reports of 2026-11-03 do not mention any finding by name, so the link between the 27-chapter roadmap and the findings remains to be drawn (ROADMAP ch09 and BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md do cite Holmström and Kang, which suggests they draw on OVERRIDE_NECESSITY and SEGREGATION_AND_FORGETTING; not read).
        - Whether the four ROADMAP findings should be merged to MAIN as they are, given they depend on FREEZE.md, AUTONOMY_SCALE.md and other files that are retired or in history only.
    - item 8
      - **key**: review-lambda
      - **items**: 51
      - **defects**
        - item 1
          - **statement**: The thesis corrects itself in place (Dekker 1971 is NOT held; dd.txt is the DDSketch paper) but its closing Labels paragraph still says "Dekker held as `dd.txt`". The file contradicts itself.
          - **locator**: ROADMAP:L8/L5/research/review/THESIS_lambda_decomposed_record.md:49-58 vs :143-145
        - item 2
          - **statement**: The thesis decode gives the poles as "λ ∈ {0, 1}" and in the same sentence and in LD3 writes the residual as "λ ≥ 1".
          - **locator**: ROADMAP:L8/L5/research/review/THESIS_lambda_decomposed_record.md:10-11, 34
        - item 3
          - **statement**: The probe's docstring still says "Repo itself is PRIVATE/unreachable", a claim the document it serves withdrew as unsafe ("[source text withheld from the public copy]").
          - **locator**: ROADMAP:L8/L4/work/computation/probes/ebstack_lambda_analysis.py:1-2 vs ROADMAP:L8/L5/research/review/EBSTACK_LAMBDA_ANALYSIS.md:14-20
        - item 4
          - **statement**: The 9.49% containment figure is a property of the probe's sampling grid, not of the operator: lambda=0 as coded contains the truth exactly when one bound is zero, and with integer b drawn from 0..20 that happens with probability 41/441 = 9.30%. On continuous inputs the rate would be zero. The roadmap's D11 row carries "9.49 % of random pairs as coded" as if it described the operator.
          - **locator**: ROADMAP:L8/L5/research/review/EBSTACK_LAMBDA_ANALYSIS.md:72-81; ROADMAP:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:622
        - item 5
          - **statement**: dr001_half_cell.py prints a measured ratio of 15/8 beside the words "the factor of 2 DR-001 claims". Its comment "incl. both ends" is wrong (i runs 0..15, the upper end is never sampled), and its note that the worst cases are "not reachable exactly by a finite sample" is wrong for the centre case, where w/2 is reached at i = 0. (By reading; script not run.)
          - **locator**: ROADMAP:L8/L4/work/computation/probes/dr001_half_cell.py:24, 39-43
        - item 6
          - **statement**: DR-001 and DR-003 link their probes by the relative path `probes/...`, and REGISTER.md links `README.md`; none resolves from dr-001-003/. The sheets acknowledge this and say where the objects now stand, but the links are broken as written. DR-001 also names the codec `tools/ommp`, now at L8/L4/work/computation/ommp/.
          - **locator**: ROADMAP:L8/L5/research/review/dr-001-003/DR-001-uha-half-cell-decode.md:3, 36; DR-003-swap-flip-no-left-inverse.md:4; REGISTER.md:4; L8/L6/history/restore-2026-09-14.md:66
        - item 7
          - **statement**: Rump 2010 is cited as "[source text withheld from the public copy]"; page 44 is outside the stated page range (probably a PDF page of an author copy).
          - **locator**: ROADMAP:L8/L5/research/review/LAMBDA_EXTERNAL_VERIFICATION_2026-08-04.md:75-76
        - item 8
          - **statement**: The lambda verification file records no fetch route, URL or date for any of its six sources, and one (Hickey et al.) was read from an accepted-manuscript copy. The audit's own standard asks for a locator; here only publication, section and equation numbers are given.
          - **locator**: ROADMAP:L8/L5/research/review/LAMBDA_EXTERNAL_VERIFICATION_2026-08-04.md:18-19, 75-76, 110-112, 150-151, 179-180
        - item 9
          - **statement**: The lambda verification file says its adversarial refutation pass "was still running" and "Verdicts may move"; no result is recorded, yet the review sheet and the roadmap carry its verdicts as settled ("The external check settles the mathematics").
          - **locator**: ROADMAP:L8/L5/research/review/LAMBDA_EXTERNAL_VERIFICATION_2026-08-04.md:232-233; ROADMAP:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:622
        - item 10
          - **statement**: The prior-art file takes the Planck H0 value from the arXiv abstract page and cites Lewis and Bridle by arXiv number. STATUS_LADDER lists arXiv under NEVER for a VERIFIED source. The file flags the route itself. Its header also links `../../FREEZE.md`, which is not in the ROADMAP tree (present only in HISTORY).
          - **locator**: ROADMAP:L8/L5/research/review/LAMBDA_PRIOR_ART_2026-08-05.md:11, 17-21, 43-44, 220-222; MAIN:L8/L5/research/review/STATUS_LADDER.md:13-18
        - item 11
          - **statement**: The receipt-rigor specification speaks of eb-receipt's "five operations" throughout, but its kernel table has six rows ([source text withheld from the public copy], verify_chain).
          - **locator**: ROADMAP:L8/L5/research/review/EB_RECEIPT_RIGOR_SPEC_2026-08-05.md:172-187, 370
        - item 12
          - **statement**: The external audit's headline ([source text withheld from the public copy]) cannot be reconstructed from the file: no per-cluster verdict table; only 24 of 27 cluster codes appear (A9, B2, C5 are absent; A9 and C5 surface only in SOURCE_REQUESTS). It reports "52 agents" for 27 clusters each checked twice (which would be 54). The evidence is said to be in a session journal that is not in the repository.
          - **locator**: ROADMAP:L8/L5/research/review/EXTERNAL_AUDIT_2026-08-04.md:4-6, 25-29, 315-317; ROADMAP:L8/L5/research/review/SOURCE_REQUESTS.md:178-181
        - item 13
          - **statement**: The audit and the source-request list disagree on two clusters. Audit: TR 29119-11:2020 wording and clause "exact"; [source text withheld from the public copy]". SOURCE_REQUESTS: both are a "material discrepancy" that "needs the primary".
          - **locator**: ROADMAP:L8/L5/research/review/EXTERNAL_AUDIT_2026-08-04.md:162-169 vs ROADMAP:L8/L5/research/review/SOURCE_REQUESTS.md:176-177
        - item 14
          - **statement**: Audit findings never carried into the files they name: the Westby and Conselice volume and DOI; the Tic Tac equality sign and missing Eiband source; the code comment citing ARCH:558; the Morton citation; the census dossier's egress-denial paragraph; the 'VERIFIED on two independent fetches' label.
          - **locator**: ROADMAP:L8/L5/research/review/CENSUS_SOURCES_DOSSIER.md:28-38, 114, 339; TICTAC_PROPULSION_ADJUDICATION.md:52, 346; L8/L4/work/computation/ommp/ommp.py:329; MAIN and ROADMAP:L8/L5/research/lanes/THEME_LEDGER.md:225
        - item 15
          - **statement**: The conjecture's two computations cite scripts that were never filed (one at a /tmp scratch path). The probes sheet'[source text withheld from the public copy] numerical claim carries the code that produced its number "or it is a number without a route".
          - **locator**: ROADMAP:L8/L5/research/review/CONJECTURE_bit_exact_pruning.md:33, 203-204; ROADMAP:L8/L4/work/computation/probes/0.md:12
        - item 16
          - **statement**: The conjecture file reads out of time order: the "Status" table at lines 175-191 is the pre-resolution table (it lacks the save-the-remainder row) but sits after the RESOLUTION section and its "Revised status" table.
          - **locator**: ROADMAP:L8/L5/research/review/CONJECTURE_bit_exact_pruning.md:158-167 vs 175-191
        - item 17
          - **statement**: The conjecture's re-run table marks the corrected sum "exact" at N = 10 and speaks of error "0.0 exactly", but the exact total 1 + 2.5 ULP is not a representable double; the match can only be to the rounded value. (My arithmetic; the script is not held.)
          - **locator**: ROADMAP:L8/L5/research/review/CONJECTURE_bit_exact_pruning.md:208-219
        - item 18
          - **statement**: The label "CH-01 (two incompatible λ_A definitions)" is cited as a thing to verify before drafting chapter 16, but no record with that identifier exists anywhere in the ROADMAP tree.
          - **locator**: ROADMAP:L8/L4/work/writing/book/ch16-the-lambda-decomposed-pre-execution-record.md:18; ROADMAP:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:257
        - item 19
          - **statement**: IEEE 1788.1-2017 is recorded as read and closed in the session log (V-21, Q6 CLOSED) and as "HELD but UNREAD" / "NOT READ" in the standards register and the roadmap.
          - **locator**: ROADMAP:L8/L4/work/writing/sessions/SESSION_2026-08-05_VERIFICATION_LOG.md:16 vs ROADMAP:L7/provenance/sources/STANDARDS_REGISTER.md:130, 367 and ROADMAP:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:248
        - item 20
          - **statement**: DR-003 carries the top ladder status VERIFIED on three course-page URLs with no captured quote and no fetch date; the audit of four days earlier required verbatim quotes for verification.
          - **locator**: ROADMAP:L8/L5/research/review/dr-001-003/DR-003-swap-flip-no-left-inverse.md:37-41; ROADMAP:L8/L5/research/review/EXTERNAL_AUDIT_2026-08-04.md:16
        - item 21
          - **statement**: AUDITONOMY.md names three research files as dependents (FINDING_lambda_knob_and_retention.md, COARSENING_VALIDATION.md, FINDING_coarsening_as_forgetting.md) that exist in none of the trees searched: ROADMAP, HISTORY 1d83788, autonomous origin/main, autonomous beta.
          - **locator**: ROADMAP:L8/L0/semantics/definitions/AUDITONOMY.md:337, 358, 433-434
      - **open_questions**
        - Does a repository named aybllc/eb-stack exist? LAMBDA_PRIOR_ART.md:173-177 and AUDITONOMY.md:438-441 (ROADMAP) record a GitHub API read of repos/aybllc/eb-stack at commit c3ec814 on 2026-08-05; the roadmap (BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:655) says "[source text withheld from the public copy]" and that [source text withheld from the public copy]. I could not check either (no network; neither is a local clone). A rename would reconcile them, but no record says so.
        - Is the mul line quoted in the prompt the code eb-stack actually ships, and was the homonym-ruling branch ever merged? Neither is recorded.
        - Which two lambda_A definitions does 'CH-01' mean? I paired the thesis decode with the departure protocol because those are the two present; the roadmap does not say.
        - What did the adversarial refutation pass on the lambda verification conclude? The file says it was still running; I found no later record in the scope documents or the 2026-08-05 session log.
        - I could not re-read Rump 2010, Hickey et al. 2001, Brent and Zimmermann 2010, Goldberg 1991, Riess 2022, Planck 2018 or the CosmoMC documentation: none is held in either repository. Only the Rump 1999 and GUM quotes were confirmed against held text.
        - I did not run any probe (the task did not say to). The 1898/20000 sample count, the 66-test OMMP run and the conjecture's 200,000-case and million-step runs are therefore unconfirmed by me; the last two cannot be re-run from the repository at all because their scripts are not filed.
        - Were the audit's term-ledger corrections (T-01 edition, T-04 elision, T-12 prefix, NIST AI 100-1 truncation) applied? The ledger it names, AUTONOMOUS_TERMS.md, is not in the ROADMAP tree, and I did not find it by that name in autonomous origin/main; 'for a service,' still stands in autonomous origin/main:L8/L5/research/lanes/LANE_B_AUDITABILITY.md:31.
        - Does the deep-research run's statement that the broad record-as-permission claim is occupied by 2026 literature hold? Its citations are unresolvable tokens, and the repository labels the run as model output, never evidence.
        - DR-002's two measurements (bound reaching address -1; 17 consecutive addresses scattered across 8,192 cells at N = 8) have no probe and were reported from chat; not recomputed.
        - The whole thread sits on ROADMAP, whose pull request #27 was closed unmerged. Whether the owner intends these restored files to reach MAIN, and under which layer, is not recorded in the scope documents; BETA does not carry them.
    - item 9
      - **key**: review-docket
      - **items**: 33
      - **defects**
        - item 1
          - **statement**: All eight documents are byte-identical to their pre-prune blobs, so every internal path in them is from the retired layout and does not resolve on ROADMAP (for example `intake/research/nu_enclosure_probe.py`, now L8/L4/work/computation/probes/nu_enclosure_probe.py; `tools/ommp/../../research/tictac_calc.py`; `AUDITONOMOUS.md:1230`; `../sources/standards/SOURCE_LEDGER.md`). AUTONOMOUS_TERMS.md and AUTONOMY_SCALE.md, which several of them cite, are not in the ROADMAP tree.
          - **locator**: ROADMAP:L8/L5/research/review/NASA_PAPER_DEFECT_LEDGER.md:33; ROADMAP:L8/L5/research/review/TICTAC_PROPULSION_ADJUDICATION.md:15; ROADMAP:L8/L5/research/review/SOURCE_REQUESTS.md:14
        - item 2
          - **statement**: SOURCE_REQUESTS SR-05 says the Johnson et al. paper unblocks docket B1; the docket files that paper and the words "This single paper" under B2.
          - **locator**: ROADMAP:L8/L5/research/review/SOURCE_REQUESTS.md:157 vs ROADMAP:L8/L5/research/review/RESEARCH_DOCKET.md:81
        - item 3
          - **statement**: SOURCE_REQUESTS SR-03 cites "docket **D3/D129**"; there is no docket entry D129 (129 is the line number of D3).
          - **locator**: ROADMAP:L8/L5/research/review/SOURCE_REQUESTS.md:57
        - item 4
          - **statement**: Docket F7 says "three more raised later" and then lists four ([source text withheld from the public copy]).
          - **locator**: ROADMAP:L8/L5/research/review/RESEARCH_DOCKET.md:166
        - item 5
          - **statement**: Docket section 0a refers to "the self-composition defect (§A4 below)"; section A has only A1, A2, A3.
          - **locator**: ROADMAP:L8/L5/research/review/RESEARCH_DOCKET.md:50
        - item 6
          - **statement**: Docket section 0 says it revises B5 and that B6 "dissolves", and the external audit refutes D3's 'one instrument holds all three'; entries B5, B6 and D3 were never amended (the file has one commit).
          - **locator**: ROADMAP:L8/L5/research/review/RESEARCH_DOCKET.md:28-29, 92-96, 128
        - item 7
          - **statement**: The docket's section C maps only Q1, Q2, Q6, Q6b, Q6c, Q7, Q8, Q9 of the record-ontology file; Q3, Q4, Q5 and Q6a have no docket entry, although the docket describes itself as every open question in one place.
          - **locator**: ROADMAP:L8/L5/research/review/RESEARCH_DOCKET.md:100-118 vs ROADMAP:L8/L5/research/lanes/RECORD_ONTOLOGY_OPEN_QUESTIONS.md:76,127,165,246
        - item 8
          - **statement**: SOURCE_REQUESTS was last committed 2026-08-05 and still lists as open several requests that other records show met or part-met: SR-16 (IEEE 7014-2024 read; '[source text withheld from the public copy]'), SR-02 and SR-12 (IEEE 1872-2015 and 7010-2020 held in aybllc/l6 since 2026-08-14, unread), SR-04 (T-01 matched to ISO 8373:2021 cl. 3.2 by the external audit), SR-10 (ISO/IEC 42001:2023 listed OBTAINED in the standards register).
          - **locator**: ROADMAP:L8/L5/research/review/SOURCE_REQUESTS.md:43-49,142-149,162,164,177 vs ROADMAP:L7/provenance/sources/staging-records/ieee/FINDINGS_2026-08-04.md:18; ROADMAP:L7/provenance/sources/STANDARDS_REGISTER.md:105,310-316; ROADMAP:L8/L5/research/review/EXTERNAL_AUDIT_2026-08-04.md:151
        - item 9
          - **statement**: The census dossier's header still states an organisation-wide egress denial and that zero entries are verified; the external audit of the same date found the premise false, byte-verified the Planck age, and found the Westby and Conselice citation wrong (volume 902:63 should be 896:58; the DOI 10.3847/1538-4357/abb6ce is unregistered). The dossier was not amended.
          - **locator**: ROADMAP:L8/L5/research/review/CENSUS_SOURCES_DOSSIER.md:3-9,114 vs ROADMAP:L8/L5/research/review/EXTERNAL_AUDIT_2026-08-04.md:94-110,137-147,228
        - item 10
          - **statement**: AUTHOR_ASSERTIONS A-009: the table for "200,000 attempts" gives 28,718 + 81,418 + 13,117 = 123,253 in the no-check row. The probe source has a fourth, uncounted outcome (committed but could not act: a trace with no action), which accounts for the other 76,747. "26.1 % of started cycles" is computed over cycles that acted, not cycles that committed.
          - **locator**: ROADMAP:L8/L5/research/review/AUTHOR_ASSERTIONS.md:842-850; ROADMAP:L8/L4/work/computation/probes/energy_reserve_probe.py:46-49,74
        - item 11
          - **statement**: AUTHOR_ASSERTIONS A-009b: the table "depth at which relay costs 1000× direct" (19, 41, 152, 742) holds only if 'direct' is fixed at 8.0 units while S/P varies with P = 5 (5·r^d >= 8,000). Measured against the direct cost at each S/P (r^(d-1) >= 1,000) the depths are 19, 39, 143, 696. My hand calculation; the probe was not run.
          - **locator**: ROADMAP:L8/L5/research/review/AUTHOR_ASSERTIONS.md:994-999
        - item 12
          - **statement**: AUTHOR_ASSERTIONS A-009c: the '~1 eV' row gives 1.0 × 10⁻²⁷ N·s per transfer, which matches a unit of 1e-19 J; with 1 eV = 1.602e-19 J and three units dissipated the figure is 1.6e-27 N·s. Order of magnitude unaffected.
          - **locator**: ROADMAP:L8/L5/research/review/AUTHOR_ASSERTIONS.md:1068
        - item 13
          - **statement**: AUTHOR_ASSERTIONS A-002b says "nothing downstream depends on it", yet A-009 builds the rest invariant and the commit gate on the A-002b cycle.
          - **locator**: ROADMAP:L8/L5/research/review/AUTHOR_ASSERTIONS.md:121 vs 826-832, 872-884
        - item 14
          - **statement**: AUTHOR_ASSERTIONS names the companion repository `abba-01/autonomous` throughout; the walk-across of 2026-08-05 and the current remotes name it aybllc/autonomous.
          - **locator**: ROADMAP:L8/L5/research/review/AUTHOR_ASSERTIONS.md:9-16
        - item 15
          - **statement**: The NASA paper defect ledger uses a private label, `INTERNALLY VERIFIED`, to mean "[source text withheld from the public copy] label is not in the repository's registry (which has VERIFIED, PARTIALLY VERIFIED, INTERNALLY VALIDATED, INTERNALLY DERIVED) and its name says the opposite of its meaning. The ledger records no byte-check of its outside quotes, and D-008 says fetches were failing in the same session.
          - **locator**: ROADMAP:L8/L5/research/review/NASA_PAPER_DEFECT_LEDGER.md:36-56,439-442 vs MAIN:L8/L5/research/review/STATUS_AND_LABEL_DISCIPLINE.md:10-13
        - item 16
          - **statement**: The NASA paper defect ledger rests D-001 to D-007 on IEEE Std 1788-2015 without noting what docket G2 records: that the standard [source text withheld from the public copy] and 1788.1-2017 is the live one.
          - **locator**: ROADMAP:L8/L5/research/review/NASA_PAPER_DEFECT_LEDGER.md:49-55 vs ROADMAP:L8/L5/research/review/RESEARCH_DOCKET.md:174
        - item 17
          - **statement**: The paper the defect ledger examines is not held in this repository in any state examined; the ledger identifies it only as a 19-page PDF 'supplied to this session' and gives no hash, version or DOI.
          - **locator**: ROADMAP:L8/L5/research/review/NASA_PAPER_DEFECT_LEDGER.md:3-5
        - item 18
          - **statement**: The walk-across compares the repositories against `definitional-instrument-autonomy-auditonomy.md` v0.1 ("this project"); that file is not in aybllc/auditonomous (ROADMAP) or aybllc/autonomous (origin/main). Thirteen amendments are owed to a document the repositories do not hold.
          - **locator**: ROADMAP:L8/L5/research/review/WALK_ACROSS_repo-instrument-standards_2026-08-05.md:5,72-83,123-131
        - item 19
          - **statement**: The walk-across locators point to `autonomous/definitions/AUDITONOMY.md` at 6568e3c. No file of that name is on aybllc/autonomous origin/main, its beta, or the scholarly-pair branch; a file AUDITONOMY.md now stands on auditonomous ROADMAP at L8/L0/semantics/definitions/AUDITONOMY.md and is absent from auditonomous MAIN and BETA.
          - **locator**: ROADMAP:L8/L5/research/review/WALK_ACROSS_repo-instrument-standards_2026-08-05.md:13,34-40
        - item 20
          - **statement**: The cycles document's verdict (ii) says continuous audit is established "since 1991" and "[source text withheld from the public copy])". SOURCE_REQUESTS SR-19 and SR-20 record that the date is contestable, that the 1991 paper says 'less-after-the fact', and that NIST's framework is voluntary. The cycles document was not amended, and the book roadmap cites it as "VERIFIED external".
          - **locator**: ROADMAP:L8/L5/research/review/AUTONOMOUS_vs_AUDITONOMOUS_CYCLES.md:136 vs ROADMAP:L8/L5/research/review/SOURCE_REQUESTS.md:180-181; ROADMAP:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:152
        - item 21
          - **statement**: The propulsion adjudication's summary table says the vacuum mechanism "FAILS BY ~4 ORDERS OF MAGNITUDE"; its own figures give 0.128 per cent, a shortfall of about 780 times ("~800×" at line 366), which is about three orders.
          - **locator**: ROADMAP:L8/L5/research/review/TICTAC_PROPULSION_ADJUDICATION.md:40 vs 111, 366
        - item 22
          - **statement**: The propulsion adjudication labels its kinematics "VERIFIED arithmetic"; the status ladder reserves VERIFIED for a check against a cited outside source, and the file says no external source was fetched. The external audit also found an equals sign where a strict lower bound is meant ("<60 s") and a Mach number given without a reference altitude.
          - **locator**: ROADMAP:L8/L5/research/review/TICTAC_PROPULSION_ADJUDICATION.md:52-53,346-347,362 vs MAIN:L8/L5/research/review/STATUS_LADDER.md:8-18; ROADMAP:L8/L5/research/review/EXTERNAL_AUDIT_2026-08-04.md:253-260
        - item 23
          - **statement**: The propulsion adjudication attributes the GoFast video to the "2015 Roosevelt" encounters; the external audit records that "[source text withheld from the public copy] the attribution is unsupported.
          - **locator**: ROADMAP:L8/L5/research/review/TICTAC_PROPULSION_ADJUDICATION.md:250,327-328 vs ROADMAP:L8/L5/research/review/EXTERNAL_AUDIT_2026-08-04.md:267-268
        - item 24
          - **statement**: The book roadmap's Ch 24 feed attributes "[source text withheld from the public copy]" to the propulsion adjudication. That file says those two reports "were not consulted" and labels the point NOT-CHECKED; the statement comes from the external audit, section 6.2.
          - **locator**: ROADMAP:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:330 vs ROADMAP:L8/L5/research/review/TICTAC_PROPULSION_ADJUDICATION.md:374-375; ROADMAP:L8/L5/research/review/EXTERNAL_AUDIT_2026-08-04.md:262-266
        - item 25
          - **statement**: The owner's decision "Book register: scholarly only" is recorded only in HUB_LEDGER.md in history. No file on ROADMAP carries it, and the roadmap lists the question it appears to answer (D1) as an open owner decision without citing it.
          - **locator**: HISTORY:HUB_LEDGER.md@3c25633:49-50 vs ROADMAP:L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:612
        - item 26
          - **statement**: The review sheet describes the walk-across among "The structures of the book"; the document is a crosswalk and custody finding, not a book structure. The roadmap uses only its section 9 (acquisition blockers).
          - **locator**: ROADMAP:L8/L5/research/review/0.md:52
      - **open_questions**
        - Does the owner's decision of 2026-08-14 ("[source text withheld from the public copy]") still stand after the instruction of 2026-09-13? I have that later instruction only as the roadmap paraphrases it ("[source text withheld from the public copy]") and did not find its verbatim text in my scope.
        - Is the Tic Tac propulsion adjudication 'conspiracy/contact material' under that ruling? The document disclaims any claim about what was observed and is used by the roadmap only as method (Ch 19) and case laboratory (Ch 24), both gated on D1. The same question applies to the census dossier (Ch 20) and to A-009c's propulsion proposal.
        - How were the outside quotations in the NASA paper defect ledger (Arb, Revol, Benet et al., JCGM 100, Octave, Hargreaves) obtained? D-008 says direct fetches returned 000 and 403 in that session and that search summaries were used for Moore; the ledger records no byte-check for D-001 to D-007.
        - Which version of 'The NASA Paper & Small Falcon Algebra' was examined, and is it the version published under DOI 10.5281/zenodo.17172694? The PDF is not held here; the roadmap says the paper lives in aybllc/nua, which is outside my scope. Whether the published paper has been corrected is not recorded.
        - What became of the two lanes the docket says were launched or running: the GUM Type A / Type B test of P2, and the reference-monitor prior-art lane B5? I found no report of either on ROADMAP (searched for 'Type B'; listed L8/L5/research/lanes/ and findings/).
        - Have IEEE 1872-2015 and IEEE 7010-2020, recorded as held in aybllc/l6 since 2026-08-14, been read? The standards register says T-02 is unchanged "until that read happens"; aybllc/l6 is not among the repositories I could inspect.
        - Does the definitional instrument (v0.1, and a v0.2 carrying the thirteen amendments) exist anywhere the owner can point to? It is in neither repository.
        - The numerical tables behind A-009, A-009b, A-009c, the NASA ledger and the propulsion adjudication come from five probe scripts that the restoring pass did not re-run and that I was not authorised to run. Their percentages (for example 15.93, 75.65, 12.24 per cent; 28,718 unsealed) are therefore reproduced on record but not re-confirmed.
        - EXTERNAL_AUDIT section 6.3 says the propulsion file's '[source text withheld from the public copy]'. The propulsion adjudication as it stands on ROADMAP has no human-tolerance section. I could not settle whether the audit refers to an earlier revision, to tictac_calc.py, or to another file.
        - Docket E1, E2, E4 and F1, F2, F4, F5, F7 describe the state of manuscript Blocks 25-27, 36, 39, 45, 46, 49-52. I confirmed only F3 against the blocks; whether the others still stand as described on ROADMAP is for the pass that covers the manuscript corpus.
        - The external quotations in the docket (sections B, C, G, H) and in the cycles document carry no page, URL or capture locators in these files. The cycles document says per-lane verification records exist; I did not find them in my scope and could not confirm any external quote myself (no network).
    - item 10
      - **key**: sources
      - **items**: 27
      - **defects**
        - item 1
          - **statement**: MAIN and ROADMAP state the register has 62 rows; it has 60 ([source text withheld from the public copy] history record that first says 62 lists ranges that total 60. Corrected in BETA only.
          - **locator**: MAIN:L7/provenance/0.md:20,33; MAIN:L7/provenance/sources/0.md:10,41; MAIN:L7/peering/private/ingress/peer-1/0.md:16; MAIN:L7/peering/private/ingress/peer-1/object-1/0.md:10; MAIN:L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:30
        - item 2
          - **statement**: The close-out search-log entry says "22 new rows" and [source text withheld from the public copy]).
          - **locator**: MAIN:L7/provenance/sources/LEDGER.md:113
        - item 3
          - **statement**: The sources sheet says "The ledger has no rows; that is admissible." while the same sheet describes a populated register. Corrected in BETA.
          - **locator**: MAIN:L7/provenance/sources/0.md:55 against :10
        - item 4
          - **statement**: The provenance sheet says "`lineage/`, `authority/` — empty" although lineage holds record EBA-PROV-2026-08-05-01. Corrected in BETA.
          - **locator**: MAIN:L7/provenance/0.md:37 against MAIN:L7/provenance/lineage/0.md:32
        - item 5
          - **statement**: The ledger says "The 27 markdown working records" moved to staging-records. 27 is the count of all non-PDF staged files at HISTORY 1d83788; three of them (two Third Power Corpus files and the clause-3 text) were routed elsewhere or not routed by the same section, so 24 moved. The tree holds 25 files plus the sheet, and two of them (terms.json, the numbered .txt) are not markdown.
          - **locator**: MAIN:L7/provenance/sources/LEDGER.md:134-142; HISTORY:_STAGING_TO_L6/ (88 files, 61 PDFs)
        - item 6
          - **statement**: The 2026-08-16 sweep entry's categories (13 + 17 + 13 + 45 + 3) total 91 against its stated "all 88 staged files", and its 43 held does not match the close-out's 40; the difference is not explained.
          - **locator**: MAIN:L7/provenance/sources/LEDGER.md:112 against :124-131
        - item 7
          - **statement**: Label vocabulary not followed: the column rule lists six labels, but 22 rows use others (ACCESSIONED x19, "Acquired lawfully", EXCLUDED, PROHIBITED SOURCE). The ID rule lists LAW- (no rows) and omits EXC- (two rows).
          - **locator**: MAIN:L7/provenance/sources/LEDGER.md:83,88-89 against :54,59-79
        - item 8
          - **statement**: The 'Not held' table is empty although the scope's own records name sources needed and not obtained (Beer, Fisk and Rogers 2014; the published HEALPix article; the complete Payne-Hanek article).
          - **locator**: MAIN:L7/provenance/sources/LEDGER.md:98-100 against :25,57 and MAIN:L7/provenance/sources/staging-records/standards/SOURCE_LEDGER.md:251-253
        - item 9
          - **statement**: Unledgered citations in the defining entry: American Heritage Dictionary, Liddell-Scott and Lewis and Short via Perseus, NIST CSRC Glossary, RFC 4949 and NIST AI 100-1 have no ledger row, against the ledger's own rule.
          - **locator**: MAIN:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:282-336 against MAIN:L7/provenance/sources/LEDGER.md:10-12
        - item 10
          - **statement**: NIST SP 800-53 Rev. 5 was retrieved, hashed and extracted (215 control statements held in the repository) but has no ledger row.
          - **locator**: MAIN:L7/provenance/sources/staging-records/standards/extracted/SP800-53r5_AC-AU_verbatim.md:7-20
        - item 11
          - **statement**: Four rows whose labels report an IEEE Xplore stamp carry no WSU class-2 hold-private tag (STD-021, STD-022, INST-001, PR-013), while the staging manifest says all 33 IEEE files carry the WSU watermark.
          - **locator**: MAIN:L7/provenance/sources/LEDGER.md:50,51,57,58 against MAIN:L7/provenance/sources/staging-records/ieee/README.md:85
        - item 12
          - **statement**: STD-025 (ISO/IEC 22989 lawful copy) has no hash, date of check or verification outcome, and the repository's 22989 captures cite the withdrawn copy's SHA-256.
          - **locator**: MAIN:L7/provenance/sources/LEDGER.md:54; MAIN:L7/provenance/sources/staging-records/standards/extracted/ISO-IEC-22989-2022_captures.md:6-7
        - item 13
          - **statement**: RFC 9162 reading record says "All 45 captures" but holds 48 capture headings (C1 to C48); the findings table says 48; the verifier compared 43.
          - **locator**: MAIN:L7/provenance/sources/staging-records/library/reading/RFC9162_Certificate-Transparency-v2.md:27,135-517,549-552
        - item 14
          - **statement**: FIPS 180-4 reading record says "[source text withheld from the public copy]" and, twelve lines later, "[source text withheld from the public copy]."
          - **locator**: MAIN:L7/provenance/sources/staging-records/library/reading/NIST_FIPS-180-4_Secure-Hash-Standard.md:17,29
        - item 15
          - **statement**: IEEE 3152 reading record: the verifier's quote list was truncated, so 40 of the record's 43 items (12 terms + 31 captures) were compared; six defects (three unmarked splices, two wrong page citations, one splice across a heading) remain on the record.
          - **locator**: MAIN:L7/provenance/sources/staging-records/ieee/reading/IEEE-3152.md:381-399
        - item 16
          - **statement**: Staging records repeatedly cite intake/imported/AUTONOMOUS_TERMS.md (rows T-02, T-08, T-13 and others) as the thing verified; that file exists in no current state (MAIN, ROADMAP, BETA), only in HISTORY 1d83788. The sheet acknowledges old paths are not rewritten but does not say the target is absent.
          - **locator**: MAIN:L7/provenance/sources/staging-records/ieee/FINDINGS_2026-08-04.md:27; MAIN:L7/provenance/sources/staging-records/standards/extracted/terms.json:_meta.governing_rule; HISTORY:intake/imported/AUTONOMOUS_TERMS.md:82
        - item 17
          - **statement**: The datasets ledger's column rule and the source ledger's upkeep rule still name paths from the earlier layout (uso/l6/LEDGER.md, research/, manuscripts/).
          - **locator**: MAIN:L7/provenance/sources/datasets-LEDGER.md:21; MAIN:L7/provenance/sources/LEDGER.md:10-12
        - item 18
          - **statement**: ROADMAP STANDARDS_REGISTER: capture locations name intake/sources/... paths that no longer exist; several OBTAINED rows name no capture location (against its rule 5); the companion link is relative but the companion is at L8/L1/state-space/; the coverage summary gives IEEE 8 held and 2 gaps where the table shows 9 held or held-unread plus 1872-2015; amendment A-004 (2026-08-14) is not reflected in the header's "Last amendment: 2026-08-05 (A-003)".
          - **locator**: ROADMAP:L7/provenance/sources/STANDARDS_REGISTER.md:8-9,85,101-109,121-130,227,310
        - item 19
          - **statement**: ROADMAP PRIMARY.md (2026-08-08) lists IEEE 1788-2015, 7009-2024, 7014-2024, 7001-2021 and 1788.1-2017 as paywalled items to acquire, although the staging records show them imported and (four of them) read on 2026-08-04.
          - **locator**: ROADMAP:L7/provenance/sources/lists-2026-08-08/PRIMARY.md:92-97 against MAIN:L7/provenance/sources/staging-records/ieee/README.md:1-5
        - item 20
          - **statement**: ROADMAP STANDARDS_CITED.md: the listed raw family counts sum to 270; the file states 271 distinct identifiers.
          - **locator**: ROADMAP:L7/provenance/sources/lists-2026-08-08/STANDARDS_CITED.md:14-16
        - item 21
          - **statement**: The task brief places the row-count note in BETA's staging-records/0.md; in BETA that file changes only one governance path. The note is in BETA's LEDGER.md and the provenance and sources sheets.
          - **locator**: BETA:L7/provenance/sources/staging-records/0.md:30; BETA:L7/provenance/sources/LEDGER.md:147-149
      - **open_questions**
        - Do the 58 pointer rows still resolve? aybllc/l6 is not on this machine (/home/user holds only 7lm, auditonomous, autonomous), so no l6 path, commit (b328334, e4f0d5c, 53b28f6) or hash could be checked by me.
        - Has the history purge of the third-party-licensed ISO/IEC 22989 PDF been carried out on the server? In this clone the blob f5e74bad... (3,225,650 bytes) is still present and reachable from commits 8660aea and 9a9ab96 on main, beta and roadmap. The record says the owner must execute or authorize it.
        - Do the ISO/IEC 22989 captures and terms.json match the lawful copy STD-025? They were taken from the withdrawn copy; no re-check is recorded.
        - Has the owner ruled on the findings the reading records reserve to him: the IEEE 7014 erasure collision, §2.8 reading (b), equivocation as a fourth prohibited act, and re-wording 'cannot be altered' to 'apparent' or detectable? All are marked OPEN or NOT ADOPTED in this scope; any later ruling would be outside it.
        - Does IEEE 1788.1-2017 retain the decoration system (register Q6)? Held, unread.
        - Has IEEE 1872-2015 been read to settle T-02? The ROADMAP register says it is held in l6 since 2026-08-14; no ledger row and no reading record exist.
        - What is the licence status of the Ferreira numbered full text held in the repository? Recorded as the owner's call and not yet made.
        - Which ledger sources does the manuscript actually need? The ledger has no bears-on column, and about 30 of the 60 rows are drone, UAV, factory, networking, pulsar and CMB material that the staging records say belong to the sibling autonomous or uha work.
        - Should web-fetched dictionary, glossary and RFC pages (the definition's anchors) and ISO OBP readings be given ledger rows, and with what fixity, given that the byte-check copies lived in temporary scratch directories?
        - Were the 19 items of the IEEE 7007 record that the verifier did not receive (76 items held, 57 compared) and the 5 uncompared RFC 9162 captures ever verified? No record found in this scope.
        - Why the sweep entry of 2026-08-16 totals 91 against 88 staged files, and where the figure 62 came from; my inference (40 + 22) is not recorded anywhere.
        - Whether the ROADMAP register and lists (closed, unmerged PR #27) are meant to return to MAIN; until then the standards coverage, verification log and acquisition order exist only on that branch.
    - item 11
      - **key**: peering-governance
      - **items**: 30
      - **defects**
        - item 1
          - **statement**: MAIN says the source ledger has 62 rows; it has 60 ([source text withheld from the public copy] same figure is in the 2026-08-16 history record. ROADMAP keeps 62; BETA corrects to 60.
          - **locator**: MAIN:L7/0.md:220 ; MAIN:L7/peering/private/ingress/peer-1/0.md:16 ; MAIN:L7/peering/private/ingress/peer-1/object-1/0.md:10 ; MAIN:L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:30
        - item 2
          - **statement**: The ledger's close-out search log says '22 new rows' but the rows it names number [source text withheld from the public copy]). BETA records the correction without altering the original line.
          - **locator**: MAIN:L7/provenance/sources/LEDGER.md:113 ; BETA:L7/provenance/sources/LEDGER.md:149
        - item 3
          - **statement**: MAIN's publications sheet says 'The harmonized specification is filed as a produced writing artifact at L8/L4/work/writing/'. No such file exists on MAIN (the folder holds three Office documents, two chat volumes, one session record and sheets). BETA retracts the sentence.
          - **locator**: MAIN:L7/publications/0.md:43
        - item 4
          - **statement**: The release checklist and binder rules name paths that exist in no state: uso/l6/LEDGER.md, research/review/, research/, manuscripts/definitions/AUDITONOMOUS_DEFINITION.md. The current homes are L7/provenance/sources/LEDGER.md, L8/L5/research/review/ and L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md.
          - **locator**: MAIN:L7/publications/binder/press-kit/README.md:18,23 ; MAIN:L7/publications/binder/README.md:11,23 ; MAIN:L7/publications/binder/internal/README.md:18
        - item 5
          - **statement**: OWNERSHIP_PENDING.md says the corpus is '[source text withheld from the public copy]'. The file now sits at an L7 egress position and the durable lifecycle was retired on 2026-09-06.
          - **locator**: MAIN:L7/peering/private/egress/peer-2/object-1/OWNERSHIP_PENDING.md:13-14
        - item 6
          - **statement**: The peer-2 egress sheets name aybllc/ncf-research as 'the intended destination' and call the transfer 'pending', while OWNERSHIP_PENDING.md leaves three outcomes open (Auditonomous, another AYBLLC repository, or a historical artifact). The position presumes an answer the owner has not given.
          - **locator**: MAIN:L7/peering/private/egress/peer-2/0.md:8 ; MAIN:L7/peering/private/egress/peer-2/object-1/OWNERSHIP_PENDING.md:12-13
        - item 7
          - **statement**: The departure protocol's header gives 'Mirror location: manuscripts/main/research/eb-carrier/eb-audit/', a path that no longer exists; the copy is at L7/peering/private/ingress/peer-2/object-1/. The file is peer-owned and marked NO EDIT.
          - **locator**: MAIN:L7/peering/private/ingress/peer-2/object-1/auditonomous-departure-protocol.md:7
        - item 8
          - **statement**: The copyright sheet says 'the 31 WSU-licensed IEEE PDFs'. The reconciliation report says the directory held '30 + 3 papers', and 34 ledger rows carry a WSU label. The sheet also calls ieee/papers/README.md the 'per-file watermark manifest'; that file lists three papers only, and the full manifest is in ieee/README.md.
          - **locator**: MAIN:L7/governance/copyright/0.md:43 ; MAIN:L7/peering/private/egress/peer-1/object-1/RECONCILIATION_FROM_L6_2026-08-16.md:90
        - item 9
          - **statement**: [source text withheld from the public copy]' condition is sourced to intake/imported/AUTONOMOUS_TERMS.md:36, a file that exists only in HISTORY (1d83788), not on MAIN, ROADMAP or BETA.
          - **locator**: MAIN:L7/provenance/sources/staging-records/ieee/README.md:21-22
        - item 10
          - **statement**: BETA files object-2 as the finite computation result, but the unchanged peer sheet in BETA still reserves object-2 and object-3 for AUTOMATION.md and REGISTER.md and says 'none is bound at this pass'. The Holdings paragraphs of the peer sheet, the public-ingress sheet, the peering sheet and L7/0.md in BETA do not mention object-2.
          - **locator**: BETA:L7/peering/public/ingress/peer-1/0.md:20-22 ; BETA:L7/peering/public/ingress/0.md:34
        - item 11
          - **statement**: On ROADMAP the object-1 sheet says the two manuscript files are held, but the peer sheet one level up (unchanged, same blob as MAIN) still says 'Nothing of them is held here; the manuscript path cited in Appendix E does not exist in this repository' and calls the manuscript 'a cold backup, absent from live trees'.
          - **locator**: ROADMAP:L7/peering/private/ingress/peer-3/0.md:8,16 ; ROADMAP:L7/peering/private/ingress/peer-3/object-1/0.md:15-16
        - item 12
          - **statement**: The restored manuscript declares a content sha256 of 7fd260a5...; the held Markdown file hashes to 6a717c70.... The held Markdown and PDF are different texts (4,075 against 3,465 words; the PDF lacks the self-reference table). The Markdown has two sections numbered 19. The sheet's Version row still says no hash is pinned.
          - **locator**: ROADMAP:L7/peering/private/ingress/peer-3/object-1/martin_2026_embodied_auditonomy_lexrom_cabin_model_v0.2_ea08f59.md:18, :363, :379
        - item 13
          - **statement**: The autonomous bindings sit under peering/public/ while their governance rows say the repositories are INTERNAL. BETA states the mismatch in words but keeps the position.
          - **locator**: MAIN:L7/peering/public/ingress/peer-1/object-1/0.md:14,18 ; BETA:L7/peering/public/ingress/peer-1/object-2/0.md:8
        - item 14
          - **statement**: MAIN's desk sheet quotes the model as naming L7/publications/ a canonical direct branch; the model's own text has read L7/allications/ since 2026-09-20.
          - **locator**: MAIN:L7/0.md:14 ; MAIN:L7/peering/0.md:8
        - item 15
          - **statement**: The closing sentence of the Holdings section opens a quotation that is never closed.
          - **locator**: MAIN:L7/0.md:225
      - **open_questions**
        - The aybllc/l6 commits b328334, e4f0d5c, bccf4e4 and 53b28f6 could not be confirmed: no l6 clone exists locally and the network was not used.
        - Whether the departure-protocol copy is byte-identical to the canonical file in aybllc/eb-audit could not be checked; no eb-audit clone exists and no commit is pinned.
        - abba-01/ebios is held nowhere, and the nu-algebra commit ea08f59 that the Martin manuscript names is not available, so the manuscript's declared content hash could not be confirmed.
        - Which of the two held manuscript files (Markdown or PDF) is the bound version is not recorded.
        - Which 7lm commit the two repositories are to match is not settled on the desk: BETA pins 4ca3edb; 7lm beta head is 97314c5 (one commit later); 7lm main is c9dc061, merged 2026-11-11, and does not contain 4ca3edb.
        - A local commit f2d5b37 ('The L7 restructure mirrored by hand: allications, and controlled; the words match the folders', dated 2026-11-11, author Claude) exists on local branch ccr-9391bd81-f2enmj in /home/user/auditonomous. It is not one of the four named states. I saw only its file list, which shows the same L7 moves as BETA plus edits to more sheets; I did not examine its content.
        - BETA's statement that Appendix C, Q13 and the C1-C7 comparisons 'now carry explicit receiving-use dispositions' was not checked; those files are outside this scope.
        - BETA's statement that 'All actual dependency bytes are checked before import' is a claim about the L4 code and was not tested here.
        - Whether the history purge of the third-party ISO/IEC 22989 PDF, recorded on 2026-08-16 as pending owner execution, has since been carried out was not checked.
        - GitHub visibility of aybllc/auditonomous, aybllc/autonomous and aybllc/l6 (stated as INTERNAL or private) could not be confirmed.
        - Whether quotations from IEEE standards may appear in a published paper without clearance is stated two ways (the copyright sheet permits quotation; the HISTORY note requires clearance before publication) and no ruling is on the desk.
        - Whether binder/internal/ belongs at L8/L4/work/writing/ is recorded as the owner's decision and is unruled.
        - No scan for credentials or for third-party personal data was made; only the '/home/eric' path count was taken.
    - item 12
      - **key**: records
      - **items**: 77
      - **defects**
        - item 1
          - **statement**: The master ledger's table 'The tree, by state' describes nine areas (uso/l6/, common/durable/, intake/, research/, binder/, manuscripts/main/, manuscripts/definitions/, manuscripts/prior-art/, _STAGING_TO_L6/) and a root HUB_LEDGER.md and intake/MOVE_LOG.md. git ls-tree -r origin/main finds 0 paths under every one. The README of MAIN (line 13) still calls this file 'the master index'.
          - **locator**: MAIN:L8/L6/history/LEDGER.md:9-10,27-40
        - item 2
          - **statement**: The master ledger contradicts itself in three places: line 16 says sources are '[source text withheld from the public copy]' while line 40 says 'RECONCILED 2026-08-16' and the directory removed; line 31 says the uso/l6 register is 'opened (empty — no rows yet)' while line 40 refers readers to it for dispositions and the same-day session ledger calls it complete; lines 47-48 say [source text withheld from the public copy]/`' while line 40 records that directory's removal.
          - **locator**: MAIN:L8/L6/history/LEDGER.md:16,31,40,47-48
        - item 3
          - **statement**: The master ledger row for manuscripts/definitions/ waits on 'Principal: REGISTER/README restore-or-replace', while the session ledger of the same date records ruling AU-NORM-01, 'Intentionally blank (AU-NORM-01, do not restore)'. The two files were then deleted on 2026-09-07.
          - **locator**: MAIN:L8/L6/history/LEDGER.md:38 against MAIN:L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:35
        - item 4
          - **statement**: The master ledger records statuses '[source text withheld from the public copy]' for records and a register that are not in MAIN (no DR-00x or REGISTER file in git ls-tree origin/main). They exist only at HISTORY and in ROADMAP (L8/L5/research/review/dr-001-003/).
          - **locator**: MAIN:L8/L6/history/LEDGER.md:32
        - item 5
          - **statement**: '62 rows' is wrong: the pointer register in MAIN has 60 rows (PR 20, STD 34, INST 4, EXC 2, counted), and the ranges given in the same sentence sum to 60. The routing plan repeats 62 twice. The register's own close-out line says '22 new rows' and enumerates 21. BETA records both corrections; MAIN and ROADMAP do not.
          - **locator**: MAIN:L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:30; MAIN:L8/L6/history/7LM_ROUTING_PLAN_2026-09-05.md:80,206; MAIN:L7/provenance/sources/LEDGER.md:113
        - item 6
          - **statement**: The 2026-08-16 session ledger breaks the 'already held' PDFs into 13 byte-identical + 17 watermark-delta + 11 residual-tolerant + 2 scan = 43, but the total it and the master ledger give is 40. The sources ledger's final accounting says '14 Xplore-stamp-delta', which does sum to 40.
          - **locator**: MAIN:L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:16 against MAIN:L7/provenance/sources/LEDGER.md:127-128
        - item 7
          - **statement**: The 2026-08-16 ledger is titled 'owner rulings AU-NORM-01..04' but states only 01, 02 and 03. AU-NORM-04 ('Definitions remain under manuscripts/definitions/') exists only in the commit message of 4a1c1db, which by the repository's own rule is not L6 memory. The harmonization of 2026-09-05 moved the definition out of manuscripts/definitions/ without recording that it supersedes AU-NORM-04.
          - **locator**: MAIN:L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:1; MAIN:L8/L6/history/harmonization-2026-09-05.md:37
        - item 8
          - **statement**: The harmonization record says '69 paths moved by `git mv` (renames, no deletions)'. In the commit that added it (ccc0554) 68 paths left their old location (tree comparison of ccc0554^ and ccc0554; git reports R=68, D=0). The 69th is apparently the root README.md, whose retired copy is an addition while the root file was rewritten in place.
          - **locator**: MAIN:L8/L6/history/harmonization-2026-09-05.md:22
        - item 9
          - **statement**: The harmonization record says every OWNER DECISION row of the plan 'is left exactly where it was', but rows the plan marked 'MOVE · OWNER DECISION' were moved (LEDGER.md, PRIORS_EXTERNAL, THEME_LEDGER, CONTRADICTIONS and others) and rows marked 'RETIRE · OWNER DECISION' were retired (five research READMEs). Three of those questions (CONTRADICTIONS review-or-findings, PRIORS L3-or-L5, THEME_LEDGER lanes-or-review) and the README retirements are missing from §5, the record's list of decisions left open, which the README presents as 'every decision left to the author'.
          - **locator**: MAIN:L8/L6/history/harmonization-2026-09-05.md:3,89-95 against MAIN:L8/L6/history/7LM_ROUTING_PLAN_2026-09-05.md:157,165,169,172,177,179,183,200
        - item 10
          - **statement**: The deletion test of §10 ('0 bytes preserve nothing') was applied to two 0-byte files and not to two others: manuscripts/README.md and manuscripts/main/README.md remain in the retired set at 0 bytes (git ls-tree -l).
          - **locator**: MAIN:L8/L6/history/harmonization-2026-09-05.md:152 against MAIN:L8/L6/retired/layout-2026-08-14/manuscripts/README.md
        - item 11
          - **statement**: The L6 layer sheet's two holdings lists omit sheets-2026-09-07.md, 7LM_ROUTING_PLAN_2026-09-05.md and retired/layout-2026-09-06/, all present in the tree. ROADMAP's copy additionally omits its two new records and third retired set; BETA's omits its beta history file.
          - **locator**: MAIN:L8/L6/0.md:70-75,86-89
        - item 12
          - **statement**: The retired sheet's 'Holds' section has the line 'In this repository:' with nothing after it.
          - **locator**: MAIN:L8/L6/retired/0.md:22-23
        - item 13
          - **statement**: The history sheet describes this repository's LEDGER.md with the quotation 'declared, not silently repaired' and 'retired objects'. That phrase is not in this repository's LEDGER.md (git grep over MAIN finds it only in the sheet); it is a section title of the Autonomous repository's master ledger ('Known staleness — declared, not silently repaired', autonomous origin/main:L8/L6/history/0.md:35). The description was carried over from the sibling's sheet.
          - **locator**: MAIN:L8/L6/history/0.md:35
        - item 14
          - **statement**: The history sheet states 'this clone is shallow', a fact about one session's clone, in a sheet that is supposed to state the directory as it stands. The ledgers name rescue/reorg-2026-08-14 as where the first deployment and pre-redaction bytes survive; that branch is not among the origin refs, and commits 9aefa6e and 73c3ae1 named in the ledgers are not objects in the clone. Those pointers cannot be followed from the remote as fetched.
          - **locator**: MAIN:L8/L6/history/0.md:35; MAIN:L8/L6/history/LEDGER.md:8; MAIN:L8/L6/history/LEDGER_2026-08-14_redeploy.md:7
        - item 15
          - **statement**: After the rule of 2026-09-07 that sheets say what is, the three L6 sheets still speak of the past pass: 'the L6 record of this displacement event', 'the record of this pass', 'as it stood before this pass'.
          - **locator**: MAIN:L8/L6/0.md:74,88; MAIN:L8/L6/history/0.md:37; MAIN:L8/L6/retired/0.md:34
        - item 16
          - **statement**: MAIN's L6 sheet names 'Released publications — `L7/publications/`'. The model has changed: aybllc/7lm origin/main states 'Canonical direct L7 branches are L7/provenance/, L7/governance/, L7/peering/, and L7/allications/' (7lm:L7/0.md:16), and governance/restrictions has become governance/controlled. BETA corrects both; MAIN and ROADMAP still carry the old paths.
          - **locator**: MAIN:L8/L6/0.md:82 against BETA:L8/L6/0.md:82
        - item 17
          - **statement**: The status ladder, carried verbatim into MAIN, says 'Nothing is ever deleted' and that promotions 'are logged in the register'. The retired sheet says 'No-deletion is not a rule enforced here or anywhere in the repository', and MAIN holds no register. Two current documents disagree on the deletion rule.
          - **locator**: MAIN:L8/L5/research/review/STATUS_LADDER.md:25 against MAIN:L8/L6/retired/0.md:12
        - item 18
          - **statement**: ROADMAP's restore record declines five .odt files of HISTORY common/durable/durable/orphan/ (auditonomous-manuscript.odt, auditonomous.odt, autonomous-theory.odt, my-book.odt, stream-eb-carrier-imporotant.odt) with the reason that the harmonization §8 dispositions stand. §8 names none of them (git grep of those names over MAIN L8/L6: no hit); it disposes of different files. The five were deleted by the prune 8c98573 while 'principal's call on their home' was open, and no record enumerates where their content stands.
          - **locator**: ROADMAP:L8/L6/history/restore-2026-09-14.md:33,191-195 against MAIN:L8/L6/history/harmonization-2026-09-05.md:111-123
        - item 19
          - **statement**: ROADMAP's reconciliation sweep misstates two class counts: class C as listed is 30 items (11+3+3+4+6+2+1), stated 29; class B's standard numbers match 16 files in the pre-prune tree, stated 17. The overall total of 61 is right. The record is labelled unreviewed model output and was superseded on 2026-08-16.
          - **locator**: ROADMAP:L8/L6/history/L6_RECONCILIATION_2026-08-14.md:19-20,46-51,59-72
        - item 20
          - **statement**: BETA's L6 record cites evidence that is not in the repository: T3-red.txt, T3-integration-wait.txt, T3-review-red.json/.txt and a 'private implementation move manifest' that enumerates the moved blobs. The repository's rule puts the enumeration that precedes a move or deletion in the L6 record; here it is held outside. The record also refers to 'the four saved holdings discrepancies' without saying which they are.
          - **locator**: BETA:L8/L6/history/AUDITONOMOUS_BETA_HISTORY.md:6,8,9-10
        - item 21
          - **statement**: MAIN has no record enumerating what the prune of 2026-08-15 (8c98573: 214 files changed, 99,383 lines deleted) removed. The repository's rule is enumeration before deletion; the only full enumeration is ROADMAP's restore record §9, unmerged. MAIN documents cite files that cannot be opened in MAIN (for example AUDITONOMOUS.md §2.8).
          - **locator**: MAIN:L8/L6/history/harmonization-2026-09-05.md:19; MAIN:L8/L5/research/review/0.md:44
        - item 22
          - **statement**: The 2026-08-16 queue item 5 says 'Two flagged ambiguities' and gives three line numbers (18/96/181); the promised boundary note in the interface register was never written (no match in the binding record).
          - **locator**: MAIN:L8/L6/history/LEDGER_2026-08-16_l6-close-and-normalization.md:50
      - **open_questions**
        - Did the owner accept the restore of 2026-09-14? The record infers the ruling (D15) from an instruction that does not mention restoring; PR #27 was closed unmerged and BETA was built without it. I could not read the PR discussion (no network).
        - ROADMAP and BETA are disjoint candidates on the same MAIN. No record says which is to be merged first or whether one replaces the other. BETA follows the changed model (L7/allications/, governance/controlled/); ROADMAP does not.
        - What do the five .odt drafts deleted at the prune contain (auditonomous-manuscript.odt, my-book.odt and three others at 1d83788:common/durable/durable/orphan/)? I did not extract them; the names suggest owner-authored manuscript material that no current record accounts for.
        - Does the branch rescue/reorg-2026-08-14 still exist anywhere? It is not among the fetched origin refs, and commits 9aefa6e and 73c3ae1 are not in the clone. The ledgers say it holds the first deployment and pre-redaction personal data ('never replay').
        - The custody claims of 2026-08-16 (61/61 PDFs dispositioned, 19 accessions triple-hash verified) rest on commits e4f0d5c and bccf4e4 in aybllc/l6, which I was not given. They are recorded as verified; I could not confirm them.
        - Was the caveat about IEEE-754-2019 (its only byte-identical copy in l6 sat under durable/delete/, 'surface to Eric before ledgering') ever answered? No record in this repository.
        - Was the IL-001 purge directive (owner: "remove that copy") executed on the remote? The pre-prune tree in this clone still lists the iTeh ISO/IEC 22989 preview PDF, so history here is not rewritten.
        - Is AU-NORM-04 ('Definitions remain under manuscripts/definitions/') superseded in the owner's view? It exists only in a commit message and was overridden by the 2026-09-05 move without a record.
        - What exactly are BETA's dispositions for Appendix C, Q13 and C1-C7, and do they satisfy the owner rule? The L6 note asserts them; the files are outside Layer 6 and I did not inspect them.
        - Is the session-ledger format (one entry per session, with External Sources Checked and Failures) still required? It lives only in a retired rule text, and no session after 2026-08-16 produced one.
        - Counts in the two 2026-08-14 ledgers (151 files, 123 and 124 renames) could not be re-derived because their commits are not in the clone.
    - item 13
      - **key**: autonomous-dependency
      - **items**: 46
      - **defects**
        - item 1
          - **statement**: Row A3 of the bound entry carries two labels at once: [source text withheld from the public copy], the Label cell still reads VERIFIED. (The repository's REVIEW_4 F1 records this; the cell is uncorrected. DEFINITION_LIST_AUTONOMOUS.md:25 gives the downgraded label.)
          - **locator**: AUT-MAIN:L8/L0/semantics/definitions/AUTONOMOUS.md:72
        - item 2
          - **statement**: §6 of the entry says "[source text withheld from the public copy]" and rule 1 says "its index (A1…A10)", but the table has eleven rows, A1 to A11. The compilation says "(A1–A11)".
          - **locator**: AUT-MAIN:L8/L0/semantics/definitions/AUTONOMOUS.md:244,246 against :80 and DEFINITION_LIST_AUTONOMOUS.md:14
        - item 3
          - **statement**: §0 says "[source text withheld from the public copy] §1 table and the repository's own ingress sheet carry nine issuing bodies (peer-1 to peer-9).
          - **locator**: AUT-MAIN:L8/L0/semantics/definitions/AUTONOMOUS.md:39 against AUT-MAIN:L7/peering/public/ingress/0.md (Holdings)
        - item 4
          - **statement**: §3a is headed "[source text withheld from the public copy] criteria".
          - **locator**: AUT-MAIN:L8/L0/semantics/definitions/AUTONOMOUS.md:179 against :184-196 and :264
        - item 5
          - **statement**: The banner says "[source text withheld from the public copy]" and lists them as ([source text withheld from the public copy]): item (3) is skipped in the numbering.
          - **locator**: AUT-MAIN:L8/L0/semantics/definitions/AUTONOMOUS.md:11,15-19
        - item 6
          - **statement**: Status conflict inside one directory: AUTONOMOUS.md says "[source text withheld from the public copy] directory sheet records it as "a recorded inconsistency, carried unchanged". Only the unmerged beta changes the register.
          - **locator**: AUT-MAIN:L8/L0/semantics/definitions/AUTONOMOUS.md:24 against REGISTER.md:19; sheet 0.md:35
        - item 7
          - **statement**: Rows A9 and A10 differ between the two definition objects. AUTONOMOUS.md A9 is a paraphrase attributed to "AI Roadmap 2.0" and A10 is the truncated "an autonomic system is a self-governing system"; DEFINITION_LIST gives A9 as a verbatim "EASA glossary" sentence and A10 as "NOTE 2: An autonomic system is a *self-governing system* that can manage itself in accordance with high-level objectives." Both are labelled VERIFIED. A6 likewise drops the source marker "<A.4>" that the list keeps.
          - **locator**: AUT-MAIN:L8/L0/semantics/definitions/AUTONOMOUS.md:75,78,79 against DEFINITION_LIST_AUTONOMOUS.md:28,31,32
        - item 8
          - **statement**: The bound entry and its companions cite internal paths of the layout before 2026-08-14 that no longer exist at those paths (for example `governance/RULINGS.md`, `research/DEFINITION_OF_AUTONOMOUS_v2.md`, `sources/QUARANTINE_AND_REMEDIATION.md`, `research/FINDING_overridability_third_axis.md`, `definitions/AUTOMATION.md`). The v2 file now sits at L8/L6/retired/error-records/. Because the object is pinned, a reader following the binding cannot resolve them on origin/main.
          - **locator**: AUT-MAIN:L8/L0/semantics/definitions/AUTONOMOUS.md:12,26,30,102,108,234,294; REGISTER.md:12,19-25
        - item 9
          - **statement**: The human-referent finding says its count [source text withheld from the public copy]`", but its ten rows include ISO/IEC 22989 3.1.16 (heteronomy) and IEEE 7001 §4.2, which are not A-rows, and omit A3, A9 and A10. "8 of 10" is therefore not a count over A1 to A11. Auditonomous MAIN repeats the figure as "Ten definitions are on record (… A1–A11)".
          - **locator**: AUT-MAIN:L8/L5/research/findings/FINDING_autonomy_requires_a_human_referent.md:16-28,115 ; MAIN:L8/L5/research/findings/DISTILLATION.md:14-15
        - item 10
          - **statement**: The MAIN binding record says the Auditonomous definition "names this binding". The definition file on MAIN contains none of the strings 'peer-1', 'ingress' or 'aybllc/autonomous'; only the directory sheet names the binding. (The beta adds a naming line 20 to the definition.)
          - **locator**: MAIN:L7/peering/public/ingress/peer-1/object-1/0.md:34 against MAIN:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md (grep, 0 hits)
        - item 11
          - **statement**: MAIN finding file refers to the peer definition by a relative path `../definitions/AUTONOMOUS.md` that resolves to no file on MAIN (the local copy existed only in HISTORY at the repository root and at manuscripts/definitions/).
          - **locator**: MAIN:L8/L5/research/findings/DISTILLATION.md:15,55
        - item 12
          - **statement**: On the beta, the peer sheet still says AUTOMATION.md and REGISTER.md "would be `object-2/` and `object-3/`" and "none is bound at this pass", while peer-1/object-2/ on the same commit holds the beta computation binding. The ingress sheet and the peer sheet's Holdings on the beta also still list object-1 only.
          - **locator**: BETA:L7/peering/public/ingress/peer-1/0.md:20-22 against BETA:L7/peering/public/ingress/peer-1/object-2/binding.json; BETA:L7/peering/public/ingress/0.md:34
        - item 13
          - **statement**: On the autonomous beta, the egress peer sheet's Holdings still list only object-1 and the egress sheet still describes the peer-directed object as object-1 only, although egress/peer-1/object-2/ is added by the same branch (peer-1/0.md is not in the diff; egress/0.md changes only two path strings).
          - **locator**: AUT-BETA:L7/peering/public/egress/peer-1/0.md (unchanged from main, Holdings) and AUT-BETA:L7/peering/public/egress/0.md:17-18,31
        - item 14
          - **statement**: The autonomous beta corrects REGISTER.md by deleting the "Not yet entered" row for autonomy/autonomous and adding an "entered" row, rather than leaving the superseded row visible and marked. The repository'[source text withheld from the public copy]; the old row survives only in git history and in BETA_SOURCE_OVERLAY.md's description.
          - **locator**: AUT-BETA:L8/L0/semantics/definitions/REGISTER.md (diff against origin/main, hunk at old line 19); rule at MAIN:L8/L5/research/review/STATUS_LADDER.md:25-26
        - item 15
          - **statement**: The Autonomous register cites the coinage at `../auditonomous/definitions/AUDITONOMY.md` §0. No file named AUDITONOMY.md exists on auditonomous MAIN.
          - **locator**: AUT-MAIN:L8/L0/semantics/definitions/REGISTER.md:13
        - item 16
          - **statement**: All seven statements of the binding on MAIN give the peer path as `research/definitions/AUTONOMOUS.md` (and the peer sheet gives `research/definitions/AUTOMATION.md`, `research/definitions/REGISTER.md`). Those paths do not exist on autonomous origin/main; they resolve only at the bound commit. This is recorded as deliberate (harmonization-2026-09-05.md:170), but the binding record itself does not state the current path; only an L6 history line does.
          - **locator**: MAIN:L7/peering/public/ingress/peer-1/object-1/0.md:10,13; MAIN:L8/L6/history/harmonization-2026-09-05.md:170,174
        - item 17
          - **statement**: The HISTORY counterpart entry says its rows were imported from abba-01/autonomous at commit `f15524e`, and the MAIN binding record says the transfer to aybllc/autonomous left "commit SHAs unchanged". f15524e is not an object in the autonomous clone.
          - **locator**: HISTORY:AUTONOMOUS.md:11-12 ; MAIN:L7/peering/public/ingress/peer-1/object-1/0.md:11
      - **open_questions**
        - D22 is unruled. The beta in effect chose 'keep 0504961, no rebind' and it is byte-safe (the object has not changed). Is that the owner's ruling, or does the owner still want a new binding record naming the current path and commit, written beside the old one?
        - Is Autonomous to state a single 'consensus baseline' as the 7LM specification says, or does the plural entry stand as the baseline? Every ref I read leaves this open; the beta explicitly declines to create one.
        - Which A-rows is the 'autonomous' inside 'auditonomous' read under? The only answer on record (rows A1, A2, A5, A6, A11; three axes) is in the unmerged, unreviewed PR #29 paper and the ROADMAP vocabulary paper.
        - IEEE 1920.1, IEEE 7007, ISO/IEC 25059 and the second ALFUS volume are used by Auditonomous (Q13, C1-C7) but are not A-rows; IEEE 1920.1 is nowhere in the autonomous repository. Should they be admitted to the Autonomous entry (it has no admission policy, REVIEW_4 F6) or dropped as definition sources in Auditonomous? I did not read the beta's per-row 'receiving-use dispositions' for C1-C7 and Q13.
        - The seven REVIEW_4 fixes: no dated version of AUTONOMOUS.md with any of them exists in the clone. Who makes them and when is not recorded. I read only REVIEW_4's verdict lines, not its body, and did not read AUDIT_L6_ADVERSARIAL.md §1.5 (the contested A11 drift note).
        - Does the tag exemplar-2026-09-14 exist on the remote? `git tag` in the local autonomous clone is empty; I did not fetch. PR #29 is closed unmerged, so the declaration it would mark is not on main.
        - Is the baseline paper (PR #29 branch only) to be carried into main or the beta? Neither has a papers/ directory in the autonomous repository.
        - Commit f15524e (named by the pruned counterpart entry) could not be resolved; the autonomous clone reports itself shallow, so absence here does not show it never existed.
        - I did not run autonomous_beta.py, its 15 tests, or the Auditonomous consumer; I verified only that the pinned code and result hashes match the bytes at 805cd42. Whether the result JSON says what BETA_FINDINGS.md reports (16 cases, 32 events, 0 goal changes) was not recomputed.
        - The object-2 binding pins 7lm architecture commit 4ca3edb; the 7lm beta branch head is one commit later (97314c5, 2026-11-03). Whether the pin must move if the model changed again was not examined.
        - No external quotation in any A-row, finding or lane was re-verified against its standard (no network; the repository's own VERIFIED labels and REVIEW_3/REVIEW_4 records are what stand). Whether the lawful ISO/IEC 22989 copy (STD-025 in aybllc/l6) is held, and A3 re-verified, could not be checked from these clones.
        - The auditability-gap search queued on 2026-08-16 (does any codified definition of autonomous entail recoverable records?) has no result on any ref I read; I did not search the whole of BETA or ROADMAP for a later run.
    - item 14
      - **key**: manuscript-map
      - **items**: 59
      - **defects**
        - item 1
          - **statement**: The vocabulary paper's claims-table row 16 and its §5.2 state as a verified negative finding that no predicate Aud(S,F) occurs in the sourcebook. The sourcebook has it at line 116 in LaTeX (\operatorname{Aud}(S,F)). The roadmap's 14 September rewording of D20 and its §9 correction (1) repeat the error.
          - **locator**: ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:305 and :154; ROADMAP:RM:630 and :647; against ROADMAP:L8/L4/work/writing/sourcebook/Auditonomous_Book_Material_Sourcebook_v0.1.md:116
        - item 2
          - **statement**: Three records give the constitutional sentence's place in Block 3 as line 10. It is at line 1; line 10 reads "**II. The permissions triad**". The reference was inherited from the consolidated document, written before the block's header was removed on 4 August.
          - **locator**: ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:292; ROADMAP:L8/L4/work/writing/book/00-front-matter.md:9; ROADMAP:L8/L4/work/writing/manuscript/0.md:8; source of the error ROADMAP:L8/L6/retired/consolidated-2026-08-04/AUDITONOMOUS.md:72
        - item 3
          - **statement**: Vocabulary paper row 6 says [source text withheld from the public copy] cited section grounds condition B in "[source text withheld from the public copy]`)" and condition A in "hardware root". Rump 1999 is verified in a separate record; Warmus 1956 appears in no check found.
          - **locator**: ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:295; against ROADMAP:L8/L0/semantics/definitions/AUDITONOMY.md:201-202
        - item 4
          - **statement**: The roadmap's chapter gate lines and its decision table's 'Blocks' column disagree in eight places: D1 lists Ch 19–24 but Ch 21's gate is none; D6 lists Ch 17 but Ch 17's gate omits it; D8 lists Ch 19 but Ch 19's gate omits it; D12 lists Ch 22 but Ch 22's gate omits it; D21 lists Ch 24 but Ch 24's gate omits it, while Ch 19's gate names D21 and D21's row does not list Ch 19; D22 lists Ch 3 and 4, whose gates are D14 and none; D23 lists Ch 6, 9, 14–17, none of whose gates name it; Ch 3's gate names D14, whose row does not list Ch 3. The 27 chapter files copy the gate lines.
          - **locator**: ROADMAP:RM:612-633 against RM:123, 132, 265, 287, 305, 314, 332
        - item 5
          - **statement**: The book sheet and the vocabulary paper give the decision range as D1–D21. The roadmap they cite has D22 and D23 (and no D17: 22 decisions numbered to 23).
          - **locator**: ROADMAP:L8/L4/work/writing/book/0.md:8; ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:12 and :316; against ROADMAP:RM:631-632
        - item 6
          - **statement**: The book sheet states the drafting order as Part 0, then Parts II–V, [source text withheld from the public copy]. That is phase P3 of the 13 September order, which the roadmap strikes through as superseded; the order in force starts with Chapter 2 and Chapter 19.
          - **locator**: ROADMAP:L8/L4/work/writing/book/0.md:14; against ROADMAP:RM:680 and RM:603
        - item 7
          - **statement**: The roadmap's §9 says every history-prefixed feed was re-pointed and two remain history-only. Three remain: HUB_LEDGER.md (Ch 5), the Malmstrom note (Ch 23), and the OMMP codec at git:8c98573^ (Ch 17 and Appendix H), which the same branch restored to L8/L4/work/computation/ommp/. Appendix B still cites git:1d83788:AUDITONOMOUS.md §11 although that file was restored.
          - **locator**: ROADMAP:RM:647; against RM:263, RM:373, RM:379; ROADMAP:L8/L4/work/computation/ommp/0.md
        - item 8
          - **statement**: Chapter 22 lists as a feed a leads table in a session scratchpad (scratchpad/leads/LEADS.md). The file is in no tree of the repository; the roadmap's §8 says so of the leads table generally.
          - **locator**: ROADMAP:RM:312; ROADMAP:RM:637
        - item 9
          - **statement**: The roadmap counts the source ledger as 62 rows, twice. BETA's correction of 3 November counts 60 archive rows and finds that a past '22 new rows' statement enumerates 21.
          - **locator**: ROADMAP:RM:413 and RM:639; against BETA:L7/provenance/sources/LEDGER.md (section "Attributable receiving correction — 2026-11-03")
        - item 10
          - **statement**: The roadmap introduces "The three seam joints" and lists four. Its Part VI heading says leg B while Chapter 18 inside it is labelled leg A, and its diagram draws Chapter 18 inside the leg B box. The front matter says "The legs never interleave" while Part VII runs leg A (Ch 25), leg B (Ch 26), both (Ch 27).
          - **locator**: ROADMAP:RM:82-87; RM:71; RM:270-274; ROADMAP:L8/L4/work/writing/book/00-front-matter.md:21 and :71
        - item 11
          - **statement**: Five chapter files (8, 10, 17, 20, 21) say "What exists now: drafted (…)" a few lines above a Text section that says "Not yet drafted." The word is used for source blocks in one place and for chapter text in the other.
          - **locator**: ROADMAP:L8/L4/work/writing/book/ch08-the-constitution-bounded-autonomy-mandatory-auditability-a-runtime-without-parameters.md:19 and :27
        - item 12
          - **statement**: CONTRADICTIONS.md links four files by bare relative name (STANDARDS_REGISTER.md, ISO_IEC_REQUIREMENTS.md, IEEE_REQUIREMENTS.md, NIST_REQUIREMENTS.md). None exists in its directory on any ref; the extractions stand under L8/L4/work/computation/ with different names, and the standards register is on ROADMAP only, under L7. The note also cites the retired path intake/sources/standards/SOURCE_LEDGER.md.
          - **locator**: MAIN:L8/L5/research/review/CONTRADICTIONS.md:10, 15-17, 207
        - item 13
          - **statement**: The Tic Tac adjudication says its numbers reproduce by running tools/ommp/../../research/tictac_calc.py, "committed alongside this file". On ROADMAP the script is at L8/L4/work/computation/probes/tictac_calc.py and the document is at L8/L5/research/review/.
          - **locator**: ROADMAP:L8/L5/research/review/TICTAC_PROPULSION_ADJUDICATION.md:15-16
        - item 14
          - **statement**: The roadmap names the release position as L7/publications/ (done-condition 9 and step S6), as do the book and papers sheets and MAIN's writing sheet. The model's position is L7/allications/publications/, which BETA has.
          - **locator**: ROADMAP:RM:40 and RM:589; ROADMAP:L8/L4/work/writing/book/0.md:25; MAIN:L8/L4/work/writing/0.md:27; against 7LM-BETA:L8/0.md:22
        - item 15
          - **statement**: The roadmap's method paragraph calls the three Office files "the three manuscripts" and the chat volumes "the two chat transcripts"; its own §3 table calls the same files "[source text withheld from the public copy] "live drafts" label persists on MAIN, ROADMAP and BETA sheets (found by the prior pass; BETA repeats it).
          - **locator**: ROADMAP:RM:5; ROADMAP:RM:416; BETA:L8/L4/work/0.md:39; MAIN:L8/L4/work/writing/0.md:33
        - item 16
          - **statement**: The vocabulary paper's row 12 and the peer's finding count 8 of 10 definitions, while the same paper's row 17 and §2 speak of eleven definitions (A1–A11). The term entry AUDITONOMY.md §4 also says "Autonomy has ten codified definitions" and cites the peer file by a bare path, not through the binding.
          - **locator**: ROADMAP:L8/L4/work/writing/papers/AUDITONOMOUS_VOCABULARY_PAPER_2026-09-14.md:301 and :306; AUTONOMOUS-MAIN:L8/L5/research/findings/FINDING_autonomy_requires_a_human_referent.md:27; ROADMAP:L8/L0/semantics/definitions/AUDITONOMY.md:234-235
        - item 17
          - **statement**: The roadmap's order of work places the drafting of Chapter 19 (move 9) before the network session (move 10) that the chapter's own "Verify before drafting" list requires.
          - **locator**: ROADMAP:RM:603-604; ROADMAP:L8/L4/work/writing/book/ch19-evidence-before-explanation-the-unknown-is-not-a-thing-the-evidence-supply-chain-motion-without-range-technological-hindsight.md:16
      - **open_questions**
        - Which model commit the two repositories are to be brought into line with: 4ca3edb (what both beta exemplars pin), 97314c5 (the beta scaffold tip, which adds the manuscript guidance) or 7lm origin/main c9dc061 of 2026-11-11, which does not contain the beta branch.
        - Whether the local unpushed commits of 2026-11-11 (auditonomous f2d5b37, autonomous 8257118) are that update in progress. They were seen in the object store but are outside the three named states and were not read beyond their file lists.
        - How ROADMAP's content (the restore, the roadmap, the book tree, the vocabulary paper) and BETA's structure are to be combined. Neither contains the other, and no record plans the merge.
        - Whether BETA's 'no rebind' at 0504961 is the owner's ruling on D22. BETA never names D22.
        - Whether the owner's 14 August ruling ('scholarly only', history only) already answers D1, and how it stands beside the 13 September instruction for an academic book on 'auditbonomy and first contact'.
        - Whether the full build-first order (moves 1 to 8, including eight repository harmonizations and the L2 registrations) is still required before Chapters 2 and 19, neither of which lists those items in its own gate.
        - Which reading of the C1–C7 register Chapter 2 is to present: the roadmap's 'registers complete' and 'VERIFIED (components)', or BETA's 'local contested reading' with unresolved clauses. I did not re-verify any standard's text.
        - What 'the source ledger' to be locked with Chapter 19 is: the L7 pointer ledger, the book's bibliography, or the per-chapter ledger the prospectus asks for.
        - Which seven quotations the roadmap means by 'the seven codified quotations'. The number matches the seven open-circle link marks in CONTRADICTIONS.md, but the roadmap does not list them.
        - Whether a document filed under L8/L6/retired (the consolidated defining document) may serve as a live feed for seven chapters and Appendix B, or should have an active position.
        - Whether the chapter files keep copies of the L5 roadmap entries as headers or point to the L5 record, given the model's sentence against duplicating.
        - Not checked in this pass: the contents of source-ledger rows IL-001 to IL-004; the perpetuity adjudication §6.1; the '.docx' sourcebook against its '.md' (the prior pass found them text-identical); the peer's fifteen component repositories (not cloned locally); GitHub-side state such as branch protection, the exemplar tag and pull-request status (no network use).
        - Not run: the roadmap's integrity checks, the Tic Tac calculation script and the BETA computation. The task did not ask for them.
- **workflowProgress**
  - item 1
    - **type**: workflow_phase
    - **index**: 1
    - **title**: Read
  - item 2
    - **type**: workflow_phase
    - **index**: 2
    - **title**: Synthesize
  - item 3
    - **type**: workflow_phase
    - **index**: 3
    - **title**: Verify
  - item 4
    - **type**: workflow_phase
    - **index**: 4
    - **title**: Final
  - item 5
    - **type**: workflow_agent
    - **index**: 1
    - **label**: read:definition
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: a7e78bf89b22df8c7
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179896
    - **lastProgressAt**: 1794433179896
    - **cached**: yes
    - **resultPreview**: {"scope":"The definition of record and Layer 0 of aybllc/auditonomous: MAIN L8/L0 (AUDITONOMOUS_DEFINITION.md read in full, all seven L0 sheets), ROADMAP L8/L0 (AUDITONOMY.md read in full, sheet diffs), BETA L8/L0 (inserted section, AUDITONOMOUS_BETA_SCOPE.md, sheet diffs). Cross-references followed only where L0 names them: the Autonomous binding at L7/peering/public/ingress/peer-1/object-1, PERP…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 6
    - **type**: workflow_agent
    - **index**: 2
    - **label**: read:state-space
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: a5e36a0f8e73e2ee5
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179897
    - **lastProgressAt**: 1794433179897
    - **cached**: yes
    - **resultPreview**: {"scope":"Layer 1 (L8/L1/) of aybllc/auditonomous in three states: MAIN (origin/main 2165144), ROADMAP (origin/claude/book-structure-roadmap-k8ap82 9259c18), BETA (origin/beta/7lm-exemplar-auditonomous 714480d). HISTORY (1d83788) has no L8/L1; its predecessors are manuscripts/definitions/ and manuscripts/main/. Read in full from git objects: both sheets, AUDITON_ENVELOPE.md, HUMINT_ENCODE.md, REQU…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 7
    - **type**: workflow_agent
    - **index**: 3
    - **label**: read:formal-engineering
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: a3bd0996ac7a4eec6
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179897
    - **lastProgressAt**: 1794433179897
    - **cached**: yes
    - **resultPreview**: {"scope":"Layers 2 and 3 of aybllc/auditonomous. MAIN (origin/main 2165144): all 13 files under L8/L2 and L8/L3. BETA (714480d): the two added files (beta predicate, beta method), plus the code/result/binding they point to. ROADMAP (9259c18): diff against MAIN under L8/L2 and L8/L3 (empty). Cross-references followed: MAIN L0 definition; MAIN session of 2026-08-05 §7.4/§7.5; MAIN perpetuity adjudic…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 8
    - **type**: workflow_agent
    - **index**: 4
    - **label**: read:computation
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: a817990bad911277e
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179898
    - **lastProgressAt**: 1794433179898
    - **cached**: yes
    - **resultPreview**: {"scope":"Layer 4 computation and experiments (not writing): MAIN L8/L4/work/computation/ (sheet + six objects) and L8/L4/work/experiments/0.md; BETA auditonomous_beta.py, test_auditonomous_beta.py, auditonomous_beta_result.json and the sheet change; ROADMAP all-research-corpus-auditonomous.md, probes/ (sheet + eight scripts), ommp/ (sheet, README, three modules, one test). All read from git objec…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 9
    - **type**: workflow_agent
    - **index**: 5
    - **label**: read:review-core
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: a587dfb1f69135863
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179899
    - **lastProgressAt**: 1794433179899
    - **cached**: yes
    - **resultPreview**: {"scope":"Layer 5 review, core set, aybllc/auditonomous. Read from git objects only: MAIN (origin/main 2165144) L8/L5/0.md, L8/L5/research/0.md, L8/L5/research/review/{0.md, CONTRADICTIONS.md, PERPETUITY_QUESTION_ADJUDICATION.md, STATUS_LADDER.md, STATUS_AND_LABEL_DISCIPLINE.md}; BETA (714480d) diff under L8/L5/research/review (one file changed: CONTRADICTIONS.md, +15 lines). Cross-references foll…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 10
    - **type**: workflow_agent
    - **index**: 6
    - **label**: read:lanes
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: a2e1582fc86b8d021
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179899
    - **lastProgressAt**: 1794433179899
    - **cached**: yes
    - **resultPreview**: {"scope":"Layer 5 lanes of aybllc/auditonomous: MAIN:L8/L5/research/lanes/0.md (49 lines), THEME_LEDGER.md (355 lines, read in full), RECORD_ONTOLOGY_OPEN_QUESTIONS.md (255 lines, read in full). Cross-references followed only to confirm or locate a cited line: the Master Archive, TOC, Block outlines, embodied manuscript and eBIOS draft (ROADMAP and HISTORY), AUDITONOMOUS_DEFINITION.md and PERPETUI…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 11
    - **type**: workflow_agent
    - **index**: 7
    - **label**: read:findings
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: a891a0764089ee237
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179900
    - **lastProgressAt**: 1794433179900
    - **cached**: yes
    - **resultPreview**: {"scope":"Layer 5 findings and institution in /home/user/auditonomous: MAIN (origin/main 2165144) findings sheet + DISTILLATION, OVERRIDE_NECESSITY, SEGREGATION_AND_FORGETTING + three institution sheets; ROADMAP (9259c18) four restored findings and sheet change; BETA (714480d) AUDITONOMOUS_BETA_FINDINGS and sheet change. Cross-references followed: MAIN CONTRADICTIONS.md, LEDGER.md, staging reading…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 12
    - **type**: workflow_agent
    - **index**: 8
    - **label**: read:review-lambda
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: a32ae4946f5c69f5a
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179902
    - **lastProgressAt**: 1794433179902
    - **cached**: yes
    - **resultPreview**: {"scope":"The lambda thread and the external checks. ROADMAP (origin/claude/book-structure-roadmap-k8ap82, 9259c18) under L8/L5/research/review/: LAMBDA_EXTERNAL_VERIFICATION_2026-08-04.md, LAMBDA_PRIOR_ART_2026-08-05.md, THESIS_lambda_decomposed_record.md, EBSTACK_LAMBDA_ANALYSIS.md, EXTERNAL_AUDIT_2026-08-04.md, CONJECTURE_bit_exact_pruning.md, EB_RECEIPT_RIGOR_SPEC_2026-08-05.md, dr-001-003/ (s…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 13
    - **type**: workflow_agent
    - **index**: 9
    - **label**: read:review-docket
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: ac332c4ca0b46bd4a
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179903
    - **lastProgressAt**: 1794433179903
    - **cached**: yes
    - **resultPreview**: {"scope":"ROADMAP only (origin/claude/book-structure-roadmap-k8ap82, 9259c18), L8/L5/research/review/: RESEARCH_DOCKET.md, AUTHOR_ASSERTIONS.md, SOURCE_REQUESTS.md, CENSUS_SOURCES_DOSSIER.md, NASA_PAPER_DEFECT_LEDGER.md, WALK_ACROSS_repo-instrument-standards_2026-08-05.md, AUTONOMOUS_vs_AUDITONOMOUS_CYCLES.md, TICTAC_PROPULSION_ADJUDICATION.md. Left scope only to follow specific cross-references: …
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 14
    - **type**: workflow_agent
    - **index**: 10
    - **label**: read:sources
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: a73b627f3e649e2f8
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179904
    - **lastProgressAt**: 1794433179904
    - **cached**: yes
    - **resultPreview**: {"scope":"The source base, L7/provenance, of /home/user/auditonomous: MAIN (origin/main 2165144) in full; ROADMAP additions (STANDARDS_REGISTER.md, lists-2026-08-08/); BETA changes (LEDGER.md and the three sheets). Read from git objects only. Cross-references followed: MAIN L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md (citation spot-check), MAIN L8/L5/research/findings/DISTILLATION.md §5…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 15
    - **type**: workflow_agent
    - **index**: 11
    - **label**: read:peering-governance
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: a88eb01c4ad6743f9
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179906
    - **lastProgressAt**: 1794433179906
    - **cached**: yes
    - **resultPreview**: {"scope":"The rest of the desk of aybllc/auditonomous: L7/0.md, L7/peering (all peers and objects), L7/governance (all sheets), L7/publications (sheets and the three binder READMEs) on MAIN (origin/main 2165144); the L7 diff MAIN -> BETA (origin/beta/7lm-exemplar-auditonomous 714480d); the peer-3 object on ROADMAP (origin/claude/book-structure-roadmap-k8ap82 9259c18). Cross-references followed onl…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 16
    - **type**: workflow_agent
    - **index**: 12
    - **label**: read:records
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: a5a64280553bb653f
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179907
    - **lastProgressAt**: 1794433179907
    - **cached**: yes
    - **resultPreview**: {"scope":"Layer 6 (the repository's own records) of aybllc/auditonomous: MAIN L8/L6/ in full (sheets, master ledger, three session ledgers, harmonization record, routing plan, sheets record, two retired sets); ROADMAP additions (restore-2026-09-14.md, L6_RECONCILIATION_2026-08-14.md, retired/consolidated-2026-08-04/); BETA additions (AUDITONOMOUS_BETA_HISTORY.md and the two sheet edits). Read only…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 17
    - **type**: workflow_agent
    - **index**: 13
    - **label**: read:autonomous-dependency
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: acb9c2beedda1dc25
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179908
    - **lastProgressAt**: 1794433179908
    - **cached**: yes
    - **resultPreview**: {"scope":"What Auditonomous takes from Autonomous, and the state of that source. Read as git objects only: aybllc/autonomous origin/main (c9076c3), its bound commit 0504961, its beta (e64b382 / 805cd42) and closed PR #29 branch (9b49910); aybllc/auditonomous MAIN (origin/main), BETA (714480d), ROADMAP (9259c18), HISTORY (1d83788); aybllc/7lm origin/main and beta only for the one cross-referenced r…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 18
    - **type**: workflow_agent
    - **index**: 14
    - **label**: read:manuscript-map
    - **phaseIndex**: 1
    - **phaseTitle**: Read
    - **agentId**: a1e17682d48284a46
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179910
    - **lastProgressAt**: 1794433179910
    - **cached**: yes
    - **resultPreview**: {"scope":"The manuscript against the research, and against the Seven-Layer Model's guidance for a manuscript project. Read-only, from git objects only. States read: auditonomous MAIN origin/main 2165144, ROADMAP origin/claude/book-structure-roadmap-k8ap82 9259c18, BETA origin/beta/7lm-exemplar-auditonomous 714480d, HISTORY 1d83788; autonomous origin/main c9076c3, origin/beta/7lm-exemplar-autonomou…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 19
    - **type**: workflow_agent
    - **index**: 15
    - **label**: synthesize
    - **phaseIndex**: 2
    - **phaseTitle**: Synthesize
    - **agentId**: a2d8964904f1ccfb5
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179924
    - **lastProgressAt**: 1794433179924
    - **cached**: yes
    - **resultPreview**: {"report":"# Auditonomous: where the research stands, and what the manuscript can take from it\n\nRead on 11 November 2026 from git objects only. Nothing was changed.\n\n**States.** MAIN = origin/main 2165144, unchanged since 11 September 2026. ROADMAP = the closed branch of pull request #27, 9259c18. BETA = origin/beta/7lm-exemplar-auditonomous 714480d, committed 2 November 2026 (Pacific time). H…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 20
    - **type**: workflow_agent
    - **index**: 16
    - **label**: critic
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a9934e59f246ccd5c
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179934
    - **lastProgressAt**: 1794433179934
    - **cached**: yes
    - **resultPreview**: {"gaps":[{"severity":"high","gap":"The report hardens \"the prior-art search for the coinage was never run\" (short answer, U-01, item 7). MAIN itself records three bounded searches and one result against the coinage that the report does not carry.","finding":"CONFIRMED by reading. (a) Word search, MAIN:L8/L5/research/review/PERPETUITY_QUESTION_ADJUDICATION.md:91: \"\"auditonomous\" / \"auditonomy…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 21
    - **type**: workflow_agent
    - **index**: 17
    - **label**: verify:KC-01
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: abda7eba2af3827df
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179936
    - **lastProgressAt**: 1794433179936
    - **cached**: yes
    - **resultPreview**: {"id":"KC-01","verdict":"corrected","reasoning":"Every cited locator resolves and every quoted string is verbatim, but three parts of the claim are imprecise or overstated.\n\nCONFIRMED\n- MAIN:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:57 reads \"[source text withheld from the public copy]\". ROADMAP carries the same blob (8b934b4).\n- MAIN…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 22
    - **type**: workflow_agent
    - **index**: 18
    - **label**: verify:KC-02
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a133d29ab86e54e0e
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179936
    - **lastProgressAt**: 1794433179936
    - **cached**: yes
    - **resultPreview**: {"id":"KC-02","verdict":"corrected","reasoning":"Every cited locator checks out verbatim, but three parts of the claim are imprecise or overstated.\n\nCONFIRMED\n- MAIN:README.md:11 reads \"The L0 object, the active definition of record (AU-NORM-02): `L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md`.\" The entry's header (MAIN:L8/L0/semantics/definitions/AUDITONOMOUS_DEFINITION.md:3) says \…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 23
    - **type**: workflow_agent
    - **index**: 19
    - **label**: verify:KC-03
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a1d0e99aecb35c624
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179936
    - **lastProgressAt**: 1794433179936
    - **cached**: yes
    - **resultPreview**: {"id":"KC-03","verdict":"corrected","reasoning":"Every cited locator checks out, but the claim is imprecise in three places and misses one contradicting record.\n\nCONFIRMED\n- The L2 register and positions are empty. MAIN:L8/L2/formal-mathematics/FORMULAS_LEDGER.md:10 reads \"Currently: **EMPTY** — no formulas held.\"; both register tables (lines 16-18, 38-40) are blank.\n- MAIN:relations/0.md:33…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 24
    - **type**: workflow_agent
    - **index**: 20
    - **label**: verify:KC-04
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a2af2e94d95984846
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179936
    - **lastProgressAt**: 1794433179936
    - **cached**: yes
    - **resultPreview**: {"id":"KC-04","verdict":"corrected","reasoning":"Every cited locator checks out, and the mathematics is confirmed, but four parts of the claim are imprecise or overstated.\n\n**What I confirmed**\n- **λ = 1 is Rump's product.** ROADMAP:L8/L5/research/review/LAMBDA_EXTERNAL_VERIFICATION_2026-08-04.md:16-34 quotes Definition 2.1 Eq. (5), and the held text matches: autonomous origin/main:L7/provenanc…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 25
    - **type**: workflow_agent
    - **index**: 21
    - **label**: verify:KC-05
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: abf6344cd4cf40cb9
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179937
    - **lastProgressAt**: 1794433179937
    - **cached**: yes
    - **resultPreview**: {"id":"KC-05","verdict":"corrected","reasoning":"Every cited locator reads as quoted, but the claim's first half is wrong in fact: a prior-art search for the coinage was run and recorded, and the \"unrun\" lines it cites are stale labels.\n\n**Part 1, prior-art search \"never run\": CONTRADICTED.**\n- **The search record exists in history.** aybllc/autonomous commit e1b3cb0 (2026-08-08, an ancesto…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 26
    - **type**: workflow_agent
    - **index**: 22
    - **label**: verify:KC-06
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a18936ada6730ca9e
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179937
    - **lastProgressAt**: 1794433179937
    - **cached**: yes
    - **resultPreview**: {"id":"KC-06","verdict":"corrected","reasoning":"Checked every cited locator against git objects on MAIN, ROADMAP and BETA. The core of the claim holds, but three parts are imprecise or overstated.\n\n1. \"60 rows, not 62\" — CONFIRMED for the ledger; state qualifier needed.\n- MAIN:L7/provenance/sources/LEDGER.md:20-79 has 60 register [source text withheld from the public copy] (my own count). The ROADMAP…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 27
    - **type**: workflow_agent
    - **index**: 23
    - **label**: verify:KC-07
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a35a8afc5de22c623
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179937
    - **lastProgressAt**: 1794433179937
    - **cached**: yes
    - **resultPreview**: {"id":"KC-07","verdict":"corrected","reasoning":"Most of the claim is confirmed from the git objects; four parts are imprecise or rest on a locator that does not say what it is cited for.\n\nCONFIRMED\n- Binding. MAIN:L7/peering/public/ingress/peer-1/0.md:10 carries the owner's sentence \"Auditonomous gets the definitions of autonomous from Autonomous and nowhere else. — owner, 2026-09-05\". MAIN:…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 28
    - **type**: workflow_agent
    - **index**: 24
    - **label**: verify:KC-08
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a64483703efa54aa7
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179937
    - **lastProgressAt**: 1794433179937
    - **cached**: yes
    - **resultPreview**: {"id":"KC-08","verdict":"corrected","reasoning":"Most of KC-08 is confirmed from the git objects, but two parts are overstated and one cited figure does not reproduce.\n\n**Confirmed**\n- File counts: `git ls-tree -r --name-only | wc -l` gives MAIN (2165144) 169, ROADMAP (9259c18) 328, BETA (714480d) 186.\n- Ancestry: MAIN is an ancestor of both branches; neither branch is an ancestor of the other…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 29
    - **type**: workflow_agent
    - **index**: 25
    - **label**: verify:KC-09
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a408f3cdbdc0ba95f
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179937
    - **lastProgressAt**: 1794433179937
    - **cached**: yes
    - **resultPreview**: {"id":"KC-09","verdict":"corrected","reasoning":"Three of the claim's four parts are confirmed; the source count, its locator, and the way two separate records are merged are wrong.\n\n**Confirmed**\n- **Adjudication wording.** MAIN:L8/L5/research/review/PERPETUITY_QUESTION_ADJUDICATION.md:3 is dated 2026-08-02, and line 216 says DEF:52 \"[source text withheld from the public copy]…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 30
    - **type**: workflow_agent
    - **index**: 26
    - **label**: verify:KC-10
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a613e9050ad9a2200
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179938
    - **lastProgressAt**: 1794433179938
    - **cached**: yes
    - **resultPreview**: {"id":"KC-10","verdict":"corrected","reasoning":"All three numbers in the claim are confirmed from git objects. Four parts are imprecise or true of a narrower set of states than the claim says, so the verdict is \"corrected\".\n\n**CONFIRMED**\n\n1. **7009 carries 15, not 16.** `MAIN:L8/L1/state-space/REQUIREMENTS_OWNERSHIP.md:72` says \"[source text withheld from the public copy])\".\n  …
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 31
    - **type**: workflow_agent
    - **index**: 27
    - **label**: verify:KC-11
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a95e997319a88f837
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179938
    - **lastProgressAt**: 1794433179938
    - **cached**: yes
    - **resultPreview**: {"id":"KC-11","verdict":"corrected","reasoning":"Most of KC-11 is confirmed from the git objects, but four parts are imprecise or overstated.\n\n**Confirmed**\n- ROADMAP:L8/L4/work/writing/book/ holds 31 files, 27 of them chapter files, all from one commit (b1ec302, 2026-09-14). Each chapter file's Text section is a single paragraph at line 24-29 that opens \"*Not yet drafted.* The owner's order o…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 32
    - **type**: workflow_agent
    - **index**: 28
    - **label**: verify:KC-12
    - **phaseIndex**: 3
    - **phaseTitle**: Verify
    - **agentId**: a39ecd9621626fbd5
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179938
    - **lastProgressAt**: 1794433179938
    - **cached**: yes
    - **resultPreview**: {"id":"KC-12","verdict":"corrected","reasoning":"Every ref, hash, date and ancestry fact in the claim checks out. Four parts are imprecise or overstated.\n\n**Confirmed as written**\n- 7lm `origin/main` is c9dc061 (2026-11-11 10:08 -0800) and has `L7/allications/` and `L7/governance/controlled/`.\n- 7lm `origin/beta/common-contracts-r1-r6` is 97314c5 (2026-11-03 08:58 -0800); it is not an ancestor…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
  - item 33
    - **type**: workflow_agent
    - **index**: 29
    - **label**: final
    - **phaseIndex**: 4
    - **phaseTitle**: Final
    - **agentId**: a9bdd65cd3d9b76f0
    - **model**: claude-opus-5-5
    - **state**: done
    - **startedAt**: 1794433179964
    - **queuedAt**: 1794433179939
    - **attempt**: 1
    - **lastToolName**: StructuredOutput
    - **lastToolSummary**: # Auditonomous: where the research stands, and what the man…
    - **promptPreview**: You are one agent in a READ-ONLY quality-assurance workflow over local git clones. Nothing may be changed.

      REPOSITORIES (all refs are already fetched; do not fetch; do not use the network)
      - /home/user/auditonomous = aybllc/auditonomous: the research home of "auditonomous" (adj.), a word coined by Eric D. Martin, and of the theory, engineering doctrine and record format built around it. Three sta…
    - **promptFramed**: yes
    - **lastProgressAt**: 1794434242892
    - **tokens**: 279293
    - **toolCalls**: 20
    - **durationMs**: 1062928
    - **resultPreview**: {"report":"# Auditonomous: where the research stands, and what the manuscript can take from it\n\nRead on 11 November 2026 from git objects only. Nothing was changed.\n\n**States.** MAIN = origin/main 2165144, unchanged since 11 September 2026. ROADMAP = the closed branch of pull request #27, 9259c18. BETA = origin/beta/7lm-exemplar-auditonomous 714480d, committed 2 November 2026 (Pacific time). H…
- **totalTokens**: 279293
- **totalToolCalls**: 20
