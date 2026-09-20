# 7LM audit: 96 recommendations and proposed edit plan

**Status:** Preliminary review, awaiting owner adjudication. Recommendations are not adopted architecture and have not been implemented.

**Review date:** 20 September 2026.

**Filing baseline:** `6609f38669e6091ffdcb0adaa78f1e33b1802239`.

This document preserves the 96-item audit previously provided in the task conversation so it can be opened directly from GitHub. Filing it does not complete the unfinished audit or validate its external claims.

## Read this first

The repository contains a substantial research-organization framework, but it does not yet demonstrate a validated system for scientific discovery. Its strongest ideas—separating ownership, evidence, interpretation, and publication—are undermined in several places by conflicting instructions and claims stronger than their supporting evidence.

**Coverage is not complete.** The audit inventoried 117 files and reviewed the live textual specification, sheets, guide, templates, workflow, Python generator, both HTML documents, historical records, and retired textual documents. The five DOCX files and original PDF were not examined internally. The 9,080-line archived branch extract was sampled, not read completely. The audit did not run CI, render documents, or independently verify external repositories or standards.

The original review was read-only. This filing adds only this review document; it implements none of the proposed changes. This is not an IEEE/ISO certification or a claim of institutional endorsement.

Labels:

- **Error:** A reviewer finding of a demonstrable inconsistency or technical error.
- **Clarify:** Ambiguous policy or an unresolved architectural decision.
- **Addition:** A proposed improvement, not an existing requirement.
- **Verify:** A claim requiring evidence beyond this inspection.

These labels express the reviewer's assessment, not an owner's adjudication.

## Proposed edit plan

- [ ] First: resolve authorship, copyright ownership, binding identity/status/retirement, and used-source traceability.
- [ ] Second: qualify the error-detection and scientific claims; remove contradictory filing instructions.
- [ ] Third: repair validator logic and establish document-generation provenance.
- [ ] Then: evaluate whether the architecture measurably improves research.
- [ ] Before claiming an exhaustive audit: inspect all six binary documents, finish the archived branch extract, verify document equivalence, and separately validate cited external evidence.

Changes to architecture require owner decisions. Historical text and quotations should remain unchanged; corrections should identify the prior statement and the superseding decision.

## Contents

- [1. Peer ownership and lifecycle — items 1–6](#1-peer-ownership-and-lifecycle)
- [2. Copyright, licensing, and governance — items 7–11](#2-copyright-licensing-and-governance)
- [3. Provenance and source traceability — items 12–16](#3-provenance-and-source-traceability)
- [4. Root, sheets, and documentation contracts — items 17–25](#4-root-sheets-and-documentation-contracts)
- [5. Review, intake, and outward acts — items 26–31](#5-review-intake-and-outward-acts)
- [6. Scientific and mathematical claims — items 32–43](#6-scientific-and-mathematical-claims)
- [7. Formal-mathematics sheets — items 44–48](#7-formal-mathematics-sheets)
- [8. UHA/oMMP exemplar — items 49–57](#8-uhaommp-exemplar)
- [9. Workflow correctness and assurance limits — items 58–67](#9-workflow-correctness-and-assurance-limits)
- [10. HTML and diagram generation — items 68–77](#10-html-and-diagram-generation)
- [11. Authority, document conversion, and historical evidence — items 78–86](#11-authority-document-conversion-and-historical-evidence)
- [12. Additions needed to evaluate scientific usefulness — items 87–96](#12-additions-needed-to-evaluate-scientific-usefulness)
- [Matters not classified as defects](#matters-not-classified-as-defects)
- [Outstanding verification](#outstanding-verification)

## 1. Peer ownership and lifecycle

Primary file: `/home/runner/work/7lm/7lm/L7/peering/0.md`

1. **Error — acceptance incorrectly becomes authorship.** Line 29 says accepted material is carried inward “as the object's own authorship.” Line 54 explicitly prohibits turning a peer definition into locally authored content. Distinguish the received object from locally authored analysis or adaptation.

2. **Clarify — immutable location versus retirement relocation.** Lines 28–31 promise that bound objects never move. However, `/home/runner/work/7lm/7lm/L8/L6/7lm-field-guide.md:506` instructs retiring the old binding into L6. Specify whether retirement preserves the binding path, creates a historical snapshot, or relocates a record with a permanent redirect.

3. **Clarify — binding status has competing authoritative homes.** The peer sheet owns status at line 28; the object sheet owns standing at `/home/runner/work/7lm/7lm/L7/peering/private/ingress/peer-1/object-1/0.md:15`; governance also holds these decisions at `/home/runner/work/7lm/7lm/L7/governance/0.md:20`. Name one controlling record and make the others references.

4. **Error — version information is simultaneously required and excluded.** `/home/runner/work/7lm/7lm/L7/peering/private/ingress/peer-1/object-1/0.md:8–19` requires an exact version in the binding, then says the directory does not hold “source, version, authority.” Distinguish the required version identifier from the canonical provenance record.

5. **Clarify — peer identity across four positions.** The peering sheet promises corresponding ingress/egress numbers, while public/private positions are independently organized. State whether the same peer must retain one number across all four positions and how identity changes are recorded.

6. **Clarify — object identity versus delivery identity.** Line 22 treats each delivery or handoff as an object position. Elsewhere an object is a persistent bounded thing. Define how repeated deliveries, revised versions, and multiple exchanges of the same object differ.

## 2. Copyright, licensing, and governance

Relevant files:

- `/home/runner/work/7lm/7lm/L7/governance/copyright/0.md`
- `/home/runner/work/7lm/7lm/L7/governance/licensing/0.md`
- `/home/runner/work/7lm/7lm/L7/governance/controlled/0.md`

7. **Error — the single-home copyright rule conflicts with licensing instructions.** Copyright line 18 requires every copyright/licence condition to be stated once there. Licensing lines 8–20 instruct users to record those terms locally. Separate licence instruments and administrative status from the controlling interpretation of their conditions.

8. **Clarify — derived restrictions can duplicate controlling conditions.** Controlled lines 8–19 require restrictions derived from copyright and licences, while copyright says controlled should point there rather than restate conditions. Define the difference between a restriction record and a duplicate rule.

9. **Error — sibling cross-references perpetuate the conflict.** `/home/runner/work/7lm/7lm/L7/governance/access/0.md:26` and `/home/runner/work/7lm/7lm/L7/governance/permissions/0.md:26` direct licence terms to licensing, not the declared single authoritative location.

10. **Addition — establish an object-specific rights decision record.** Generic directory descriptions cannot answer whether a particular quotation, derivative document, or release is permitted. Record the applicable source, scope, decision, responsible party, and unresolved conditions without duplicating the legal text.

11. **Clarify — handling restrictions are not affirmative permissions.** `/home/runner/work/7lm/7lm/L7/governance/permissions/0.md:10` calls NO EDIT/NO DELETE a standing permission. These are restrictions on handling; they do not establish permission to obtain, reproduce, or distribute the content.

## 3. Provenance and source traceability

Relevant files:

- `/home/runner/work/7lm/7lm/L7/provenance/sources/0.md`
- `/home/runner/work/7lm/7lm/L7/provenance/sources/source-ledger.md`
- `/home/runner/work/7lm/7lm/L8/L0/semantics/definitions/0.md`

12. **Clarify — sources are used, but the source ledger is empty.** Definitions lines 50–85 adapt several standards and recommendations. The source sheet requires exact source/version records at lines 32–33, but its ledger has no rows. Empty unused capabilities are permitted; that does not resolve traceability for sources already used.

13. **Addition — complete provenance for inherited definitions.** The inherited status is explicitly disclosed, which is good. Each retained external adaptation still needs its exact source location, the material actually consulted, and a distinction between quotation, paraphrase, and local rule.

14. **Clarify — the archive binding is asserted but incompletely instantiated.** `/home/runner/work/7lm/7lm/L7/peering/private/ingress/0.md:37–46` identifies a pinned archive binding. The subordinate peer/object sheets remain generic placeholders. Either instantiate the binding or explicitly identify the parent prose as the temporary binding record.

15. **Clarify — “integrity” has different meanings.** Definitions line 85 uses an access/modification-protection meaning. Elsewhere integrity includes canonical paths, preservation, and reconstructability. Give these separate scoped meanings rather than allowing one word to imply all assurances.

16. **Addition — separate source availability from source validity.** A pinned source can become inaccessible without becoming false; an accessible source can be withdrawn or invalidated. Record these as independent states.

## 4. Root, sheets, and documentation contracts

17. **Error — the README excludes a permitted root file.** `/home/runner/work/7lm/7lm/README.md:13` says the listed root entries are present “and nothing else.” The specification and workflow permit `.gitignore`. Align the README with that allowance.

18. **Error — the templates still imply that child folders are optional.** `/home/runner/work/7lm/7lm/L8/L6/7lm-sheet-templates.md:3` says a folder beneath a layer is a design choice “through and through.” Canonical child folders are required. It is their sheet content—not their existence—that is optional.

19. **Error — not every sheet uses the full template.** The blanket claim at `/home/runner/work/7lm/7lm/L8/L6/7lm-sheet-templates.md:5` and `/home/runner/work/7lm/7lm/L8/L6/7lm-field-guide.md:457` conflicts with the deliberately minimal `/home/runner/work/7lm/7lm/L8/L6/in/0.md`. Correct the blanket claim; do not expand the inbox merely for symmetry.

20. **Clarify — header-only sheets versus required semantic descriptions.** The specification requires a semantic description; the templates permit only a path heading. Explicitly state that header-only sheets are a permitted exception and explain what semantic assurance they do not provide.

21. **Clarify — two directions are not exactly two permissible routes.** `/home/runner/work/7lm/7lm/L8/L6/7lm-field-guide.md:102` says there are exactly two legitimate ways through the structure; line 144 permits skipping layers. Describe two organizing directions without implying only two complete sequences.

22. **Clarify — “no automation” is too broad.** Several sheets use this phrase although a workflow and generator exist. Consistently say that scientific routing, semantic adjudication, and directory metadata automation are not implemented.

23. **Error — an explanatory heading-level claim is stale.** `/home/runner/work/7lm/7lm/L8/L1/0.md:54` says the specification uses H2 for four case headings. The current specification uses H3.

24. **Clarify — L7 is both “not a layer” and called a layer.** The specification distinguishes seven interior layers from the numbered external face, but surrounding prose repeatedly calls L7 a layer. Standardize “interior dependency layer,” “position,” and “external face.”

25. **Clarify — active guides extend L6 beyond its principal definition.** `/home/runner/work/7lm/7lm/L8/L6/0.md:74–75` intentionally places current guide/template source documents at L6. The specification principally describes historical memory and reconstruction. Incorporate the approved current-reference role into that definition rather than leaving an exception implicit.

## 5. Review, intake, and outward acts

Relevant files:

- `/home/runner/work/7lm/7lm/L8/L5/research/review/0.md`
- `/home/runner/work/7lm/7lm/L7/allications/0.md`
- `/home/runner/work/7lm/7lm/L7/allications/applications/0.md`
- `/home/runner/work/7lm/7lm/L7/allications/participations/0.md`

26. **Clarify — the review directory both accepts and excludes the same material.** Review lines 22 and 36 admit everything awaiting review; lines 26–29 exclude claims, findings, evidence, and proofs. Separate unclassified intake from reviews of already-owned artifacts.

27. **Clarify — “nothing is deleted” needs an explicit scope.** Review line 36 uses an absolute prohibition, while the specification permits deletion after enumeration. Explain whether intake is a protected exception or whether the sentence means “nothing is silently discarded during triage.”

28. **Error — “application” mixes two different activities.** Applications line 8 includes applying a method to an external case; line 12 defines every application as asking an external authority. A method application need not ask anyone for anything. Separate the senses.

29. **Error — one-off outward acts versus continuing participation.** The allications parent says each act occurs once on a date; participation records cover a period. Distinguish an initiating act, continuing relationship, and individual contribution.

30. **Clarify — persistent outward surfaces have no assigned position.** Allications line 23 explicitly excludes websites, accounts, and exposed interfaces and says no current position holds them. This is a disclosed architectural gap, not an accidental missing folder.

31. **Addition — define boundaries between outward-act categories.** A submission can simultaneously communicate, apply, notify, and publish. Specify whether records may reference several roles or which representation controls filing; avoid duplicating the same event as unrelated objects.

## 6. Scientific and mathematical claims

Primary file: `/home/runner/work/7lm/7lm/L8/L4/work/writing/7lm-harmonized-architecture-specification.md`

32. **Error — one extra bit cannot catch “any error.”** Line 68 makes this claim. A parity bit does not detect arbitrary multi-bit changes, and it does not detect semantic errors. Preserve the design metaphor but remove the universal technical assertion.

33. **Clarify — indexing is a convention, not a mathematical necessity.** Lines 54–66 conflate ordinal position, index, magnitude, and physical existence. Zero-based layer numbering and one-based peer numbering are legitimate design choices; physicality does not require one-based indexing.

34. **Clarify — “L2 does not mathematically support life” is not operationally defined.** Lines 520–526 label it a hypothesis, appropriately, but provide no testable meaning of “support life.” Define the claim before using it as a research boundary.

35. **Error — exact mathematics is not inherently incapable of feedback or adaptation.** Line 524 places mathematics depending on continuation, adaptation, feedback, or environmental exchange at L3. These can have exact formal representations. Distinguish formal models from approximate methods and physical realizations.

36. **Clarify — the life hypothesis loses its qualification when reused.** The academic-book traversal at line 607 repeats the restriction without the nearby hypothesis label. Carry the epistemic qualification into every consequential use.

37. **Clarify — the scale/status prohibition is overgeneralized.** Line 681 excludes scales, ladders, and status vocabularies from L1/L2 categorically. Administrative review ladders can belong at L5, while ordered sets, formal state enumerations, and measurement-scale structures can have legitimate lower-layer representations.

38. **Addition — make the semantic-drift hypothesis falsifiable.** Lines 343–345 preserve it as open research. Define observable drift, its unit of analysis, and how to distinguish changed meanings from incorrect transformations or interpretations of unchanged meanings.

39. **Clarify — intellectual-property/energy conversion needs precise limits.** Lines 536–578 use this as the L4 definition. The field guide usefully distinguishes intellectual artifacts from legal rights, but the authoritative text should also state that this is not a physical equivalence or conservation law.

40. **Clarify — membership testing versus “no calculation” at L1.** Lines 364–369 prohibit calculation but permit testing membership and compatibility. Distinguish owning a predicate, evaluating it, and recording the evaluation.

41. **Clarify — “first failing layer” does not identify root cause by itself.** Lines 85–87 and the field guide's fault procedure can stop at the first observed symptom. Distinguish the first encountered failure from the underlying failed dependency.

42. **Clarify — universal applicability needs nonmathematical profiles.** The architecture allows sparse layers, but its dependency language often assumes exact mathematics followed by engineering. Explain valid handoffs for observational, qualitative, exploratory, and historical research without inventing mathematical artifacts.

43. **Clarify — metadata is described as both present and optional.** Line 21 says each directory separately carries machine-readable metadata; later text and the sheets say none is instantiated. Clearly distinguish the proposed metadata model from present conformance requirements.

## 7. Formal-mathematics sheets

44. **Clarify — exactness does not require unitlessness.** `/home/runner/work/7lm/7lm/L8/L2/formal-mathematics/relations/0.md:10` excludes units of measurement. Exact quantity equations and dimensional relationships can contain units without measured uncertainty. Narrow the exclusion to engineering choices and uncertain values if that is intended.

45. **Clarify — total/partial relation terminology is underspecified.** The same file's lines 10 and 19 apply partiality language to every relation. General relations are not necessarily functions; define the intended property rather than importing function terminology indiscriminately.

46. **Clarify — carriers are not generally operators.** `/home/runner/work/7lm/7lm/L8/L2/formal-mathematics/operators/0.md:19` describes carriers as operators acting on states. A carrier commonly denotes an underlying set or type. Define the local sense or separate the categories.

47. **Error — partiality should not replace domain specification.** Operators line 10 permits “domain and codomain or its partiality.” A partial operator still needs its input/output types and defined subset or condition. Require these together.

48. **Addition — distinguish storage standing from evidential standing.** `/home/runner/work/7lm/7lm/L8/L2/formal-mathematics/proofs/0.md:8–21` correctly retains unproved obligations. Make explicit that “equal standing” means equal visibility in the record, not equal warrant, and carry open assumptions into dependent claims.

## 8. UHA/oMMP exemplar

File: `/home/runner/work/7lm/7lm/L7/provenance/prior-art/uha-ommp-exemplar.html`

49. **Error — an admissibility rule does not make malformed bytes unrepresentable.** Lines 366 and 380–383 infer “no byte pattern” from exponent constraints. With independently encoded fields, invalid combinations can still exist as raw bytes. Distinguish invalid encoding, rejected decoding, and construction that genuinely prevents representation.

50. **Clarify — the exemplar makes an unsupported causal inference.** Lines 210–214 conclude that the model caused the clean separation. Shared authorship and compatible organization illustrate the method; they do not isolate its causal contribution.

51. **Error — “transcription, not interpretation” contradicts the document's work.** Lines 638–643 deny interpretation while the page assigns layer roles and argues conclusions; line 688 explicitly says it “files and argues.” Describe it as an interpretive mapping.

52. **Clarify — the diagrammed peer relationship lacks a binding record.** Lines 678–679 acknowledge this. Mark the diagrams as a proposed or inferred relation rather than letting them resemble completed architectural conformance.

53. **Clarify — append-only evidence and enumerated deletion are not established as equivalent.** Lines 625–632 equate the older invariant with the current deletion rule. Document the retained invariant and the changed mechanism instead of claiming only placement changed.

54. **Error — the colour legend disagrees with the drawing.** Line 614 says crimson marks the added positions, but the L7/L8 additions use the UHA colour. Correct the legend or styling.

55. **Clarify — the document remains in a category it disputes.** Lines 664–671 explain why the earlier model is internal history rather than external prior art. The parent sheet explicitly acknowledges this exception. Resolve the filing decision without rewriting the historical record.

56. **Verify — reported external results remain unverified here.** The 41 passing tests, 19 successful digest checks, numerical margin, and formula claims need their exact underlying reports. Their appearance in this page is not independent confirmation.

57. **Verify — internal/embargoed standing needs an explicit distribution decision.** Lines 685–688 identify restrictions. Confirm the document's permitted audience and applicable rights record. This audit has not established a leak or legal violation.

## 9. Workflow correctness and assurance limits

File: `/home/runner/work/7lm/7lm/.github/workflows/integrity.yml`

58. **Error — the conflict check can fail open.** Line 15 negates `grep`. Both “no match” and a read/execution error become success after negation. Distinguish a clean scan from an unsuccessful scan.

59. **Error — conflict-marker coverage is incomplete.** The pattern assumes seven-character markers and does not recognize the diff3 ancestor marker. It cannot support an unqualified claim to detect all unresolved conflict markers.

60. **Error — legitimate text can trigger the conflict check.** An exact seven-equals line is rejected regardless of whether it is a conflict separator, Markdown content, or a quoted example. Use context-aware detection or documented exclusions.

61. **Error — whitespace splitting mishandles permitted material paths.** Lines 38 and 66 iterate over command substitution output. Directories containing spaces can be split into unrelated paths, producing incorrect sheet checks or notices.

62. **Error — the validator still accepts the superseded root layout.** Lines 19–28 and 46 retain USO/lowercase compatibility after the canonical rename. Either declare a legacy conformance profile or require the current topology.

63. **Clarify — root checks verify names more than object types.** The workflow does not fully establish that each permitted root name is the intended file or directory type. Add explicit type expectations if “canonical root” is the assurance being claimed.

64. **Clarify — retirement exemptions are location-based.** Lines 40 and 67 exempt nested retired content by path pattern. That preserves historical headings, intentionally, but does not establish that the content is a genuine unchanged snapshot.

65. **Clarify — a green workflow does not imply full architectural conformance.** Missing noncanonical sheets are deliberately notices; content, bindings, rights, dependency pins, and deletion enumerations are not verified. Name the result “structural checks passed,” not general integrity or scientific validity.

66. **Addition — regression-test the validator itself.** Include cases for valid layouts, missing sheets, wrong headings, paths with spaces, legitimate marker-like text, retired snapshots, and scanner errors.

67. **Addition — improve workflow reproducibility and hardening.** The runner image and checkout tag move over time, and token permissions are implicit. Pin appropriately and declare the permissions actually required. These are hardening recommendations, not findings of an exploitable vulnerability.

## 10. HTML and diagram generation

Files:

- `/home/runner/work/7lm/7lm/L8/L0/pedagogy/7lm-plate-sheet.py`
- `/home/runner/work/7lm/7lm/L8/L0/pedagogy/7lm-plate-sheet.html`
- `/home/runner/work/7lm/7lm/L7/provenance/prior-art/uha-ommp-exemplar.html`

68. **Error — standalone HTML lacks a doctype.** Both pages begin with a title. Normal standalone HTML loading therefore uses quirks mode. Generate a standards-mode document.

69. **Addition — declare UTF-8 explicitly.** The pages contain non-ASCII text but no charset declaration. Do not depend on server headers or browser encoding inference.

70. **Addition — declare document language.** Neither page establishes its language for assistive technologies.

71. **Addition — supply viewport metadata.** Responsive CSS exists, but the missing viewport declaration can prevent intended mobile sizing.

72. **Addition — make archival presentation independent of live font services.** Both pages request Google Fonts. Fallbacks exist, but typography and network behaviour are not self-contained or fully reproducible.

73. **Addition — validate print and accessible diagram alternatives.** Dense fixed-coordinate SVGs and minimum-width scrolling merit print, zoom, and keyboard/screen-reader checks. Existing SVG labels are useful but not necessarily sufficient for the complete diagrams.

74. **Error — the generator reports characters as bytes.** Python line 302 labels `len(page)` as bytes despite writing UTF-8. Report characters or measure the encoded output.

75. **Addition — separate escaped text from trusted SVG markup.** The text helper at lines 33–36 interpolates strings directly. Current inputs are static, so this is not an established injection vulnerability; future reuse should not treat arbitrary text as markup.

76. **Error — the repository-wide single-drawing-source claim is false.** `/home/runner/work/7lm/7lm/L8/L0/pedagogy/0.md:21` says every drawing is defined in the generator. The exemplar contains independently authored SVGs. Limit the claim to the plate sheet.

77. **Addition — check generated-file freshness.** Document the supported generation procedure and verify that the committed HTML matches its generator. No such verification was found in the workflow.

## 11. Authority, document conversion, and historical evidence

78. **Clarify — document authority changes need a formal adoption event.** `/home/runner/work/7lm/7lm/L8/L4/work/writing/0.md:22–26` makes Markdown controlling now and edited DOCX controlling later. Record exactly when that transition occurs and which revision was adopted.

79. **Verify — Markdown/DOCX equivalence is asserted, not established by this audit.** The specification's opening comment promises unchanged readback. The binary documents were not examined, so no equivalence conclusion is justified.

80. **Addition — preserve a reproducible conversion process.** Historical prose describes document generation and XML patching, but the repository does not supply the corresponding conversion/validation machinery. Record the process, tool versions, inputs, and expected output comparison.

81. **Error in assurance reasoning — finding every text run is insufficient.** `/home/runner/work/7lm/7lm/L8/L6/history/harmonization-2026-09-04.md:500` describes checking that every DOCX text run occurs in Markdown. That does not prove ordering, multiplicity, table structure, links, or complete equivalence. Preserve the historical statement but strengthen future verification.

82. **Verify — large review-count claims need underlying records.** The same history file's line 496 reports extensive agent reviews and 59 defects. Counts are not review evidence. Retain the actual findings, dispositions, checked revisions, and relevant outputs if those claims are to support assurance.

83. **Addition — use immutable revision identifiers alongside dates.** The history explicitly records multiple passes under one version date. Dates are useful labels but insufficient exact identifiers for downstream dependency bindings.

84. **Clarify — current exemplar descriptions need snapshot-specific provenance.** `/home/runner/work/7lm/7lm/L8/L6/history/specification-history.md:39–41` records older inspection commits, while the guide describes the exemplars “today.” Bind each description to its actual observed revision and date.

85. **Addition — preserve context around historical fragments.** `/home/runner/work/7lm/7lm/L8/L6/history/sheets-2026-09-07.md` contains intentionally extracted fragments, including incomplete sentences. Add source revision and original location metadata where needed; do not silently complete the quotations.

86. **Error in reading-aid quality — the PDF extraction scrambles tree glyphs.** `/home/runner/work/7lm/7lm/L8/L6/retired/specification-draft-2026-09-03/7lm-architecture-specification-draft.txt:176–244` places branch characters after entries. Keep the frozen extraction, but label the structural extraction limitation or provide a separately identified corrected reading aid.

## 12. Additions needed to evaluate scientific usefulness

These are proposals—not requirements the current scaffold already claims to satisfy.

87. **One complete end-to-end research example.** Show a bounded question, definitions, applicable state/formal/engineering representations, performed work, evidence, interpretation, review, release, and retained history, with resolvable dependencies.

88. **Measurable success criteria.** Define what improvement 7LM predicts: fewer ownership mistakes, faster reconstruction, more reliable error localization, better reproducibility, or improved discovery outcomes.

89. **A comparison against simpler alternatives.** Compare the model with an ordinary research repository or another documented organization method. Attractive examples alone cannot establish benefit.

90. **Inter-reviewer filing agreement.** Give independent researchers ambiguous artifacts and measure whether the rules lead them to the same owners and boundaries. Disagreement identifies underspecified rules.

91. **Adversarial architectural cases.** Exercise conflicting definitions, circular dependencies, withdrawn sources, inaccessible archives, ownership transfers, failed reproductions, and results that invalidate earlier assumptions.

92. **Claim-level evidence records.** Connect each claim to its premises, evidence, limitations, review standing, and conditions that would defeat it. Keep authority, endorsement, and empirical support separate.

93. **Dependency-change impact records.** When a lower contract changes, identify affected consumers and distinguish “needs reassessment” from “disproved.” The framework currently explains ownership better than propagation.

94. **A complete binding lifecycle.** Define receipt, quarantine, adoption, supersession, withdrawal, retirement, unavailable source, and restored access, including who may authorize each transition.

95. **Human-readable conformance profiles.** Separate structural conformance, documentary traceability, reproducibility, and scientific validation. Passing one must not imply passing the others.

96. **Stable requirement identifiers and a traceability table.** Connect each controlling rule to its explanations, examples, checks, exceptions, and open decisions. This would reduce drift without requiring automated scientific judgment.

## Matters not classified as defects

- `allications` is intentional terminology.
- Zero-based layer numbering is a legitimate convention.
- L7/L8 filesystem siblinghood and the conceptual envelope are explicitly distinguished.
- Empty optional capabilities are permitted.
- Historical paths and original quotations should remain unchanged.
- Unproved obligations belong in the research record when honestly labelled.
- The parked infographic proposals are not missing implementation requirements.
- Manual operation is a deliberate design choice, not inherently a deficiency.
- The exemplar repositories are explicitly described as imperfect implementations, not architectural authorities.

## Outstanding verification

Before claiming an exhaustive audit:

- Inspect the five DOCX files and original PDF internally.
- Finish reading the archived branch extract rather than relying on the sample.
- Check Markdown/DOCX and PDF/text equivalence, including ordering and structure.
- Validate the external evidence cited by the exemplars and standards-derived definitions.
- Separately assess workflow execution and document rendering; neither was performed during the original audit.

Publishing this register makes the recommendations accessible. It does not close these outstanding checks or implement the edit plan.
