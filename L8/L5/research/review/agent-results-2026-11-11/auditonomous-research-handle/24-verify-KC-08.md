# verify:KC-08

Agent result, as returned. Workflow: Handle on the Auditonomous research and manuscript. Run `wf_9c2917a7-7f0`. Phase: Verify.

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
