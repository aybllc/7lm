# verify:K18:1

Agent result, as returned. Workflow: Manuscript status of 3 November 2026. Run `wf_1cf4205c-c72`. Phase: Verify. Checked in 2026-11-11 19:56 UTC.

- **refuted**: no
- **confidence**: high
- **reason**: Every quoted phrase, number, date, path and ancestry statement in claim K18 and its offered evidence re-checks verbatim against the repository (all commands read-only: git -C /home/user/auditonomous log/show/ls-tree/grep/merge-base; working tree left at 2165144 = origin/main, HEAD detached).

  COMMIT IDENTITY AND DATES (verified)
  - 8c98573 = 8c9857372843686b9d19452399a51bfd800b28b4; author AND committer date 2026-08-15 23:28:27 -0700; author "Eric D. Martin"; subject exactly "Reorganize working tree to the shared aybllc model layout". Single parent (%P = 1d83788d85052a874b51c3e49c7c623c2a1b12f7), i.e. not a merge.
  - `git rev-parse --short 8c98573^` -> 1d83788. 1d83788: author and committer date 2026-08-14 17:40:15 -0700, author "Eric D. Martin", subject exactly "F-005: retire the freeze check on Eric's instruction".
  - `git log --oneline 1d83788..8c98573` lists only 8c98573, so 1d83788 is the immediate pre-prune tree. The ten commits up to 1d83788 (all 2026-08-14) are additive, not prunes: shortstats show deletions of 38, 15, 2, 0, 18, 1, 4 lines (e.g. e9511f5 2026-08-14 16:26:40 "Redeploy the shared repo layout on ca87bba" = 154 files, +2873/-18; dabed3c "Restore five auditonomy documents deleted by the sibling restructure" = +2014/-2). No pruning was committed before 8c98573.
  - `git merge-base --is-ancestor 1d83788 origin/main` -> true; same for 8c98573. Both sit on origin/main's first-parent line (`git log --first-parent origin/main`: 8c98573 at position 11, 1d83788 at 12).

  COMMIT BODY (verified, body lines numbered from `git log -1 --format=%B 8c98573`)
  - lines 3-4: "Eric's manual prune and promotion (2026-08-14/15), committed on his" / "instruction after session review:" (the claim's quote spans this line break).
  - line 6: "- Retire intake/ entirely (131 files) and the root governance set"; count verified: 123 `D` entries under intake/ + 8 `R` entries whose source is intake/research/ = 131; `git ls-tree -r 8c98573 -- intake/` returns 0 files.
  - line 11: "(205 deletions total; all content remains reachable in history)."; 179 D + 26 R = 205 verified.
  - line 12: "Add 29 files" = 3 A + 26 R verified. line 15 "Update six READMEs/registers" = 6 M entries.

  STAT (verified)
  - `git show --shortstat 8c98573`: " 214 files changed, 1255 insertions(+), 99383 deletions(-)".
  - `--stat=200` line 61: "intake/manuscript/Auditonomous_Theory_Master_Archive.md | 748 --"; line 156: "manuscripts/SPINE_v0.1_2026-08-14.md | 238 -"; line 174: "manuscripts/main/MANUSCRIPT.tex | 22 -".
  - name-status: "D manuscripts/main/MANUSCRIPT.tex" present. Name-status totals: A 3, D 179, M 6, R 26 (R059, R063, R076, R079, R080 x2, R088, R090, R091, R094 x3, R100 x14).

  THE REMOVED SET NAMED IN THE CLAIM (name-status D lines, and absence confirmed by `git ls-tree -r --name-only 8c98573 | grep -iE 'corpus|spine|\.tex$|sourcebook|chat-3|prompt|/notes/'`, which returns only the two `_STAGING_TO_L6/.../The_Third_Power_Corpus_v3.{md,docx}` paths)
  - corpus: D intake/deep-research/all-research-corpus-auditonomous.md (15,044 B); D intake/manuscript/Auditonomous_Theory_Master_Archive.md (152,366 B, 748 lines) together with the whole intake/manuscript/ set at 1d83788 (Auditonomous_Theory_TOC.md, Block_01..Block_52 .md files incl. Block_31/32/35/36 named "_skipped.md" at 8 bytes each, martin_2026_embodied_auditonomy_lexrom_cabin_model_v0.2_ea08f59.md and the _v0_2.pdf). At 1d83788, AUDITONOMOUS.md lines 5-15 uses "the corpus" for this material ("[source text withheld from the public copy]") and cites intake/manuscript/Auditonomous_Theory_Master_Archive.md:51/128/540/546/665/669.
  - spine: D manuscripts/SPINE_v0.1_2026-08-14.md (15,816 B; first added f67968b 2026-08-14, so it existed about one day).
  - .tex: D manuscripts/main/MANUSCRIPT.tex (665 B, 22 lines; added e9511f5 2026-08-14). Its line 2 reads "% [source text withheld from the public copy])", line 9 "[source text withheld from the public copy]."
  - Sourcebook set: D manuscripts/main/Auditonomous_Book_Material_Sourcebook_v0.1.docx (81,886 B), .md (93,997 B), _CHAT-HIST.docx (73,264 B).
  - chat-3: D manuscripts/auditonoomous-chat-3.docx (54,751 B).
  - prompts: D intake/prompts/Lambda_Explainer_Prompt.md, intake/prompts/chat.txt, intake/prompts/first/Auditonomous_Primary_Manuscript_Extraction_Verification_Prompt_v2.md; also D intake/research/PROMPT_explain_lambda.md and D manuscripts/main/notes/auditonomous-08-03-26-prompt.odt and -prompt-brick.odt. No path containing "prompt" remains at 8c98573.
  - notes: manuscripts/main/notes/ (6 entries at 1d83788) no longer exists at 8c98573: D audiontiomouns, D notes.txt (added 71f75cb 2026-08-05), D the two *-prompt*.odt; R100 notes/auditonomous-08-03-26.odt -> manuscripts/main/open-research/auditonomous-08-03-26.odt; R100 "[source text withheld from the public copy]" -> manuscripts/main/open-research/auditonomouos-important.docx.
  - Also deleted (not named in the claim): manuscripts/main/auditonomous.odt, Auditonomous_Book_Extraction_Bundle_v0.1.zip, Auditonomous_Coverage_Exclusion_Ledger_v0.1.csv, Auditonomous_Source_Manifest_v0.1.json, AUDITABILITY_REQUIREMENTS.md, AUTONOMY_AT_DISTANCE.md, REQUIREMENTS_OWNERSHIP.md, STANDARDS_REGISTER.md.

  REPOSITORY'S OWN STATEMENTS AGREE WITH THE CLAIM
  - origin/main and roadmap branch, L8/L6/retired/layout-2026-08-14/README.md:93: "freeze retired by F-005 `1d83788`; files pruned by `8c98573`; all remain in git history)".
  - roadmap branch (origin/claude/book-structure-roadmap-k8ap82, head 9259c18 2026-09-14 02:04:14 +0000), L8/L6/history/restore-2026-09-14.md:3: "[source text withheld from the public copy]`)".
  - roadmap L8/L5/research/review/BOOK_STRUCTURE_AND_ROADMAP_2026-09-13.md:5: "[source text withheld from the public copy]."
  - roadmap L7/provenance/sources/lists-2026-08-08/0.md:8: "Five files restored on 2026-09-14 from git `1d83788` (`uso/l6/provenance/`), where they had stood until the prune of 2026-08-15".
  - 8c98573 is cited in 16 files on the roadmap branch and 14 on origin/main (e.g. L8/L6/history/LEDGER.md x5, L8/L6/retired/layout-2026-08-14/README.md x5).

  UNRESOLVED / NOT CHECKED
  - First-add commit for manuscripts/auditonoomous-chat-3.docx and the three Sourcebook files returned empty from `git log --all --diff-filter=A -- <path>` (with and without --follow); probably created by rename in an earlier restructure. Not needed for K18; not pursued.
  - Whether 8c98573 was literally the branch tip ("HEAD") at commit time cannot be read from a remote reflog; it is on origin/main's first-parent line, which is the strongest available evidence.
- **correction**: Claim stands; three imprecisions to carry forward, none of which falsifies it:
  (1) "the corpus" is ambiguous in project usage. The theory corpus under intake/ (Master Archive, TOC, 52 Blocks, lexrom model) and intake/deep-research/all-research-corpus-auditonomous.md were deleted outright. But manuscripts/main/README.md at 1d83788 (lines 1-3, 25-29) calls a different set "the reference corpus" (AUDITABILITY_REQUIREMENTS, AUTONOMY_AT_DISTANCE, CONTRADICTIONS, IEEE/ISO_IEC/NIST_REQUIREMENTS, REQUIREMENTS_OWNERSHIP, STANDARDS_REGISTER); of these, 8c98573 renamed IEEE/ISO/NIST into manuscripts/main/auditnomous-model/requirements/ (R079/R094/R094), moved CONTRADICTIONS.md to open-research/ (R063), deleted the other four, and added a new 27,455-byte REQUIREMENTS_OWNERSHIP.md under requirements/ (A). The commit body line 13 says it "Add[ed] ... the auditnomous-model requirements corpus", and _STAGING_TO_L6/sources/{extracted,original}/The_Third_Power_Corpus_v3.{md,docx} survived the prune unchanged. So "removed the corpus" is exact for the intake theory corpus and wrong if read as "every corpus".
  (2) "Sourcebook set" removed as paths (3 D entries), but Auditonomous_Book_Material_Sourcebook_v0.1_CHAT-HIST.docx was byte-identical (blob 20036f6ca2971b493c5707a458ff7906043aec15) to manuscripts/auditonomous-chat-1.docx at 1d83788, and that blob persists at 8c98573 as manuscripts/main/chat/auditonomous-chat-1.docx (and on origin/main as L8/L4/work/writing/chat/auditonomous-chat-1.docx). The .docx and .md Sourcebook blobs are absent from the 8c98573 tree.
  (3) "notes" removed as a directory, but two of its six files were relocated (R100) rather than deleted: notes/auditonomous-08-03-26.odt -> manuscripts/main/open-research/auditonomous-08-03-26.odt and the Adversarial Blueprint .docx -> manuscripts/main/open-research/auditonomouos-important.docx (these are two of the five documents extracted to Markdown for this workflow).
  Side fact (contradiction inside 8c98573 itself, not part of K18): body line 15 says "Update six READMEs/registers for the new layout", but four of the six M files were blanked to 0 bytes (manuscripts/README.md 1284->0, manuscripts/main/README.md 2085->0, manuscripts/definitions/README.md 2360->0, manuscripts/definitions/REGISTER.md 2659->0; blob e69de29); only common/durable/README.md (4592->3875) and manuscripts/definitions/AUDITON_ENVELOPE.md (17553->21235) carry text. origin/main later notes "`README.md`/`REGISTER.md` remain 0-byte (their `1d83788` predecessors describe pruned files". The 1d83788 READMEs that were blanked are the ones stating ".tex is the source of truth", "main/MANUSCRIPT.tex is a **stub**", "[source text withheld from the public copy]", and that auditonomous.odt and the Sourcebook_v0.1.* files "[source text withheld from the public copy]".
