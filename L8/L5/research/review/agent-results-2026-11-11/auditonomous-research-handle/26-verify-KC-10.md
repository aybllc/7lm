# verify:KC-10

Agent result, as returned. Workflow: Handle on the Auditonomous research and manuscript. Run `wf_9c2917a7-7f0`. Phase: Verify.

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
