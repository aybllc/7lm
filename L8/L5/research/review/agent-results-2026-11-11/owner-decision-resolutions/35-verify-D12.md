# verify:D12

Agent result, as returned. Workflow: Resolutions for the 23 owner decisions. Run `wf_3293f65c-a92`. Phase: Verify.

- **quotes**
  - item 1
    - **locator**: /home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:121
    - **verbatim**: yes
    - **correction**: Verbatim (owner's words, typos intact). But the 'bears' note overclaims: these are not 'the owner's only quoted words on the root'. specification-history.md:37 on main files the same words under the rule heading 'The same root in every repository; solutions brought as workflows', and a later owner word (H:336, 20 Sept) says 'All repos should mirror the 7lm. Manually.' The quote settles only exemplar-versus-exemplar, not scaffold-versus-exemplar, which is the actual decision.
  - item 2
    - **locator**: /home/user/7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:281
    - **verbatim**: yes
    - **correction**: Verbatim substring of line 281 (the line begins earlier with '**[Clarification]** README.md is where a reader starts; ...'). Identical on origin/beta/common-contracts-r1-r6 (97314c5) and on the PR #20 branch.
  - item 3
    - **locator**: /home/user/7lm@origin/main:README.md:5
    - **verbatim**: yes
    - **correction**: Verbatim; it is the last sentence of line 5, not the whole line.
  - item 4
    - **locator**: /home/user/7lm@origin/main:README.md:13
    - **verbatim**: yes
    - **correction**: Verbatim, whole line. Root at c9dc061 confirmed by ls-tree: .github, L7, L8, README.md. Same line 13 on beta and PR #20.
  - item 5
    - **locator**: /home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:123
    - **verbatim**: yes
    - **correction**: Verbatim, last sentence of line 123. The fragments 'the example of the root it prescribes' and 'there is nothing here to ignore' used in 'against' and 'alternatives' are also verbatim from this line.
  - item 6
    - **locator**: /home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:186
    - **verbatim**: yes
    - **correction**: Verbatim fragment. Context the resolver left out: this is one of seven accuracy findings about the FIELD GUIDE, confirmed by an agent pass against the specification, not an owner ruling. In 'who_acts' the resolver puts "permitted, not required" in quotation marks; the source reads 'permitted at the root, not required', so that shortened form is not character for character.
  - item 7
    - **locator**: /home/user/7lm@origin/main:.github/workflows/integrity.yml:23
    - **verbatim**: yes
    - **correction**: Verbatim apart from leading indentation. The 'bears' note is imprecise: per H:121 'merge all three' merged the exemplars' checks (autonomous #25, auditonomous #23) with scaffold #8; the scaffold's own copy of the check came afterwards in commit 351aff1 (2026-09-07, merged by PR #9), per H:123 'Done here.' The same case line stands at autonomous@origin/main:.github/workflows/integrity.yml:51 and auditonomous@origin/main:.github/workflows/integrity.yml:23.
  - item 8
    - **locator**: /home/user/autonomous@origin/main:README.md:15
    - **verbatim**: yes
    - **correction**: Verbatim, whole line; the identical sentence is confirmed at /home/user/auditonomous@origin/main:README.md:15, and on both exemplars' PR and beta branches.
  - item 9
    - **locator**: /home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:482
    - **verbatim**: yes
    - **correction**: Verbatim (owner, 2026-09-20).
  - item 10
    - **locator**: /home/user/autonomous@origin/main:L8/L6/history/harmonization-2026-09-05.md:102
    - **verbatim**: yes
    - **correction**: Verbatim fragment (used in 'alternatives').
  - item 11
    - **locator**: /home/user/7lm@origin/main:README.md:5 (fragment 'the start, not the documentation', used in 'alternatives' as 'the owner's rule')
    - **verbatim**: yes
    - **correction**: The words are verbatim from README.md:5 ('This file is the start, not the documentation.') but they are the README's wording, not the owner's. The owner's own words are: "the read me files all need updating. Again. we dont use the reasd me for teh docuemtnation" (/home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:129). Attribute accordingly.
- **inference_holds**: yes
- **objection**: Every quotation checks out character for character at its locator; the defects are in attribution and reach, not in the text.

  1. A later owner word was ignored. The resolver calls the 6 September sentence "the owner's only quoted words on the root". It is not the last word that bears. On 20 September the owner wrote "All repos should mirror the 7lm. Manually." (H:336), and on 11 November he typed that the two repos must be updated "phsyciall; to match". Read literally against the scaffold's tree (root: .github, L7, L8, README.md, no .gitignore), "mirror" and "match" cut toward removing .gitignore from the exemplars or adding one to the scaffold. The resolution survives this only because what is mirrored is the model of record, and the specification (line 281) says the root "may hold" .gitignore; but that is an inference the owner has not confirmed, and the resolver should have shown him the sentence instead of asserting the present state "already satisfies him".

  2. The owner quote used does not reach the question. "the root needs to be the same for both" is about the two exemplars. The decision is scaffold versus exemplars. Only the specification, the check and the record carry the resolution; no owner word names .gitignore anywhere in the three records.

  3. The resolution adds a condition the controlling text does not carry. "permitted ... when there is something to ignore" comes from the field guide (7lm@origin/main:L8/L6/7lm-field-guide.md:371, "a `.gitignore` if there is anything to ignore") and from the record's explanation of the scaffold's own case (H:123). The specification says only "and .gitignore" under "may hold". The field guide is the document the owner ordered deprecated on 17 October and PR #20 retires, so the condition should not be stated as rule.

  4. A supporting owner word was missed: "we dont use the reasd me for teh docuemtnation" (H:129). It is stronger support for reading the README sentence as non-controlling than the README's own line 5, and it is the owner's.

  5. The README is not the only live text omitting .gitignore. 7lm@origin/main:L8/L6/in/7lm-layer-lists.md:415 reads "The root holds `README.md`, `L7/`, `L8/`, `.github/`, and nothing else." It sits in the L6 inbox and is not rule text, but the decision's framing ("the README does not") undercounts.

  6. Small imprecisions: the scaffold's check was not itself among the "merge all three" (it came in 351aff1 via PR #9); H:186 is an agent-verified finding about the field guide, not an owner ruling; "the start, not the documentation" is README wording, not the owner's.

  None of this overturns the substance. Specification, check (three repositories, all branches including beta 97314c5 and the 11 November mirrors), and record agree that .gitignore is admitted and not demanded, and changing nothing is consistent with "Don't change the system unless you ask or are unsure".
- **missed_quotation**: Cuts the other way (later than the 6 September word the resolver relied on): "All repos should mirror the 7lm. Manually. We update 7lm and focus on it only. No outside updates until we are sure I'm close." — /home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:336 (owner, 2026-09-20). With it, the owner's instruction of 11 November 2026 as typed: "we need to uipdate the autonomous and auditonomous repos phsyciall; to match first".

  Supports the resolution and was not used: "the read me files all need updating. Again. we dont use the reasd me for teh docuemtnation" — /home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:129 (owner, 2026-09-07).
- **corrected_resolution**: Keep the substance, correct the framing. Put to the owner: the specification says the root "may hold" .gitignore (spec:281), the check admits it in all three repositories, and the record says it is "permitted at the root, not required" (H:186); so .gitignore is permitted at a canonical root and not required, and nothing is changed in any tree. State the rule without the added condition "when there is something to ignore": that wording is the field guide's and the record's explanation of the scaffold's own case (H:123), not the specification's. Ground the reading of the scaffold README in the owner's own word, "we dont use the reasd me for teh docuemtnation" (H:129): the README is not where the rule lives. Show him the counter-reading in his own later words, "All repos should mirror the 7lm. Manually." (H:336) and "phsyciall; to match" (11 November): if he means the roots literally identical, the choice is his between adding a .gitignore to the scaffold and removing it from the exemplars, and the Autonomous file is recorded as "the owner's file; its copyright commentary is its own rule history" (autonomous H:102). Note for him that the layer lists at L8/L6/in/7lm-layer-lists.md:415 also omit .gitignore, so if he asks for alternative (a) the same one-sentence question arises there. No agent writes anything unless he asks.
- **corrected_confidence**: the quotations favour it, on the specification, the check and the record; no word of the owner names .gitignore, and his later "All repos should mirror the 7lm. Manually." is an unweighed counter-reading that only he can settle
