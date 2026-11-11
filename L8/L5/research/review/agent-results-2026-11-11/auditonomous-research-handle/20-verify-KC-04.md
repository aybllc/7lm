# verify:KC-04

Agent result, as returned. Workflow: Handle on the Auditonomous research and manuscript. Run `wf_9c2917a7-7f0`. Phase: Verify.

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
