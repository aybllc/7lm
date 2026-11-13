# verify:docx-fidelity

Agent result, as returned. Workflow: Review of the specification correction. Run `wf_d267b581-d7d`. Phase: Verify.

- **verdicts**
  - item 1
    - **id**: docx-1
    - **upheld**: yes
    - **class**: outside-the-change
    - **reason**: Reproduced, and the class is right.

      Evidence re-derived from the .docx at 33c3878 (exported with `git -C /home/user/7lm show 33c3878:L8/L4/work/writing/7lm-harmonized-architecture-specification.docx`, sha256 2831a64a..., identical to the working-tree file), counted twice: by regex and by an XML parse (/tmp/claude-0/-home-user/bfcfd013-a2da-5019-961e-7f46116f08be/scratchpad/spec-fix/review/verify-docx-fidelity/scripts/survey.py and /tmp/claude-0/-home-user/bfcfd013-a2da-5019-961e-7f46116f08be/scratchpad/spec-fix/review/verify-docx-fidelity/scripts/survey2.py).

      - word/document.xml has 982 paragraphs: Title 1, Subtitle 1, Heading1 12, Heading2 18, Heading3 11, Quote 3, Caption 18, ListBullet 13, ListNumber 8, Code 186, and 711 with no pStyle (the default style, which word/styles.xml marks as Normal). There are 0 rStyle references and 29 tables, all TableGrid.
      - word/footer1.xml has 1 paragraph, style Footer.
      - Subtitle, List Bullet and Footer are built-in (no w:customStyle); only Code carries w:customStyle="1".

      So three styles in use are missing from the parenthesis at 0.md line 24: Subtitle (the line "Harmonized Authoritative Architecture Specification"), List Bullet (the 13 bullets of "Exemplars as instantiated", among them the copyright bullet this commit rewrote) and Footer (the dateline this commit patched). The list closes with "and a monospace Code style", so it reads as complete and is not.

      Class: `git show 33c3878 -- L8/L4/work/writing/0.md` changes line 22 only; line 24 is untouched. The same parenthesis and the same omission go back to aba46a2 (6 September 2026: Subtitle 1, ListBullet 12, Footer 1), earlier than the reviewer's "at least 12 September". The commit's own history text (§41 and "Changes of 12 November 2026") says nothing about styles. The only other copy of the sentence is L8/L6/in/optimistic-thompson-branch-text.md:3371, which is not live text and must stay.

      The replacement list is complete against the file: 12 built-in styles plus Code, nothing else referenced (word/numbering.xml only links list styles to numbering definitions).
    - **exact_fix**: Proposal for the owner, not applied. In /home/user/7lm/L8/L4/work/writing/0.md line 24, replace

      (Title, Headings 1–3, Normal, Quote, Caption, List Number, Table Grid, and a monospace Code style)

      with

      (Title, Subtitle, Headings 1–3, Normal, Quote, Caption, List Bullet, List Number, Table Grid, Footer, and a monospace Code style)

      The rest of the line stays as it is (the old string occurs exactly once, en dash U+2013 in "1–3"). It is not the sheet's first line, and no rule or path changes. If applied, record it by appending to L8/L6/history/harmonization-2026-09-04.md, not by rewriting §41. L8/L6/in/optimistic-thompson-branch-text.md:3371 is left alone.
  - item 2
    - **id**: docx-2
    - **upheld**: yes
    - **class**: outside-the-change
    - **reason**: Reproduced, and the class is right. Both phrases are inexact as claimed; both are minor.

      docProps/core.xml at 33c3878 holds exactly: "Version of 12 November 2026, generated from the canonical Markdown beside it: built-in styles only, one page per top-level section; reads back to the Markdown unchanged."

      - "built-in styles only": word/styles.xml defines Code as `<w:style w:type="paragraph" w:customStyle="1" w:styleId="Code">`, based on NoSpacing with Consolas fonts, and 186 paragraphs of word/document.xml use it. The sheet beside it (0.md line 24) does name the Code style.
      - "one page per top-level section": word/document.xml has 12 w:pageBreakBefore, all 12 on the 12 Heading1 paragraphs, with 0 `w:br w:type="page"` and 1 sectPr; the Heading1 style definition itself has none. So each top-level section starts a new page, which is what 0.md line 24 says ("every top-level section starting a new page"). The sections are not one page long: headless LibreOffice lays the file out on 51 pages (`pdfinfo` on /tmp/claude-0/-home-user/bfcfd013-a2da-5019-961e-7f46116f08be/scratchpad/spec-fix/review/verify-docx-fidelity/pdf/spec.pdf: Pages: 51), with the 12 sections starting on pages 6, 10, 13, 16, 19, 21, 24, 29, 32, 35, 45 and 48.

      Class: the parent 8ea0d0b has the same description with "20 September 2026", and the wording goes back unchanged, date apart, to aba46a2 (6 September 2026). The commit changed only the date, as §41 says ("the description in docProps/core.xml"), and the owner asked for the spec sentences, not for this. No text file in the tree quotes the phrase (`git grep 'one page per top-level section' 33c3878` finds nothing) and the only script in the tree is the plate-sheet generator, so nothing else depends on the wording.

      The reviewer's replacement is accurate against the file and matches the sheet's wording; it needs no XML escaping.
    - **exact_fix**: Proposal for the owner, not applied. In /home/user/7lm/L8/L4/work/writing/7lm-harmonized-architecture-specification.docx, member docProps/core.xml (one of the three members the commit already patched), the dc:description to read:

      Version of 12 November 2026, generated from the canonical Markdown beside it: built-in styles and one monospace Code style, every top-level section starting a new page; reads back to the Markdown unchanged.

      The other 17 members stay byte for byte and in their order. If applied, record it by appending to L8/L6/history/harmonization-2026-09-04.md, not by rewriting §41.
