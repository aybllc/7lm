# verify:D18

Agent result, as returned. Workflow: Resolutions for the 23 owner decisions. Run `wf_3293f65c-a92`. Phase: Verify.

- **quotes**
  - item 1
    - **locator**: /home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:482
    - **verbatim**: yes
  - item 2
    - **locator**: owner's instructions of 11 November 2026
    - **verbatim**: yes
    - **correction**: Not a git object; it matches the instruction as typed in the task brief, character for character ("we need to uipdate the autonomous and auditonomous repos phsyciall; to match first .").
  - item 3
    - **locator**: /home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:336
    - **verbatim**: yes
    - **correction**: Verbatim as far as it goes; it is the first four sentences of a longer message on that line.
  - item 4
    - **locator**: /home/user/7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:930
    - **verbatim**: yes
  - item 5
    - **locator**: /home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:500
    - **verbatim**: yes
  - item 6
    - **locator**: /home/user/7lm@origin/main:L8/L4/work/writing/7lm-harmonized-architecture-specification.md:2
    - **verbatim**: yes
    - **correction**: Verbatim fragment; the sentence runs on to line 3: "below this comment and reads back to it unchanged."
  - item 7
    - **locator**: /home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:484
    - **verbatim**: yes
  - item 8
    - **locator**: /home/user/autonomous@a719cec:L8/L6/history/harmonization-2026-09-05.md:217
    - **verbatim**: no
    - **correction**: The text is character for character exact, but it is not at line 217, which is blank. It is the last sentence of line 211 at a719cec (and at 8257118): /home/user/autonomous@a719cec:L8/L6/history/harmonization-2026-09-05.md:211. The matching sentence for the other exemplar is at /home/user/auditonomous@294c843:L8/L6/history/harmonization-2026-09-05.md:204 ("Twelve folders carry no sheet").
  - item 9
    - **locator**: /home/user/7lm@origin/ccr-9391bd81-f2enmj:L8/L6/history/harmonization-2026-09-04.md:518
    - **verbatim**: yes
    - **correction**: Verbatim at the branch tip, 95bea5d.
  - item 10
    - **locator**: /home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:510 (the 'against' quotation)
    - **verbatim**: yes
- **inference_holds**: no
- **objection**: The core holds: the quotations support drafting the correction as a proposal, applying nothing, and waiting for both the mirrors and the owner's word (REC:482, REC:484, SPEC:930). Five parts of the resolution claim more than the quotations say, or miss a word of the owner.

  1. SPEC:934 is left without a fix. REC:484 requires each finding to reach the owner as "file, what is wrong, the exact fix". The resolver set aside the option of naming the unsheeted folders under "Not yet as stated" as "the owner's to word". The owner's word of 6 September 2026 (REC:113, missed) is the reason that section exists: the exemplars are documented as they are, imperfect. The specification's history says the same at /home/user/7lm@origin/main:L8/L6/history/specification-history.md:68: "the two exemplars are documented as instantiated, imperfections included." So the proposal should carry exact wording for SPEC:934 as well. SPEC:934 is also untrue on both exemplar mains today: I listed the same six and twelve unsheeted folders at a719cec and 294c843, and the mirror does not create them. It does not wait on the mirror; it waits on decision 14 (whether those folders get sheets).

  2. "A text diff held outside the repository" runs against a later word of the owner, 11 November 2026: "have them check in their results periodically so we dont lose them." and "put them in auditonomous too and the public one its public". The drafted proposal is a result and should be checked in where the other agent results go, with the specification untouched.

  3. A precedent was missed that answers most of the version-date question. On 12 September 2026 the exemplars caught up with a rename and the stale sentences were removed from the exemplar section: /home/user/7lm@origin/main:L8/L6/history/specification-history.md:81 "The sentences that said the repositories carried the old names until the rename pass are removed from the two dispositions ... and from the exemplar section". Line 82 adds "The version date is 12 September 2026 in the header comment, the dateline, the Version box, and the generated rendering's footer and description. No rule changes". With the 20 September version now on main (SPEC:2), precedent points to a new version date. The cost is then understated: beyond three sentences, the date changes in the header comment, the dateline, the Version box, and the .docx footer and description. Three more live files name the version: L8/L4/work/writing/0.md, the plate sheet and its generator.

  4. The trigger is too narrow. Decision 6 (which mirror lands) is open; both exemplar betas make the same two moves. The correction should follow whichever mirror reaches each main, not PRs #30 and #28 by number. SPEC:950 depends only on Autonomous and SPEC:958 only on Auditonomous; SPEC:938 needs both. The exact text must also be drawn against the specification on scaffold main at that time: on the beta the passages sit at lines 936, 940, 952 and 960, and PR #19 rewords line 950 and carries "version of 6 October 2026".

  5. Two smaller overreaches. REC:336 says the repositories mirror the scaffold by hand; it does not say the specification's statement is corrected "after they match, and not before". That sequencing rests on SPEC:930 alone. And "the guide is retired verbatim" is true only on the unmerged PR #20 branch (same blob, 0c9626e, at the retired path). On main the guide is live at L8/L6/7lm-field-guide.md, so asking the owner to confirm that GUIDE:474 "stands uncorrected, as the retired guide's text" presupposes decision 8. If PR #20 does not merge, GUIDE:474 is live text that says something untrue and needs its own proposed fix.

  No later word of the owner reverses the core. "I didn't want anything automated yet" (PR #20 record, line 518) is consistent with patching the .docx by hand and adding no check. The brief gives the Auditonomous PR #28 branch as 294c843; its tip is now 428bbaf (agent check-ins on top), with 294c843 an ancestor and the record and unsheeted folders unchanged.
- **missed_quotation**: "this was my last controlling dfocument. we nee to update it agniostical;ly then using autoniomous andautonomus as an exmaple even if its not perect right hnow i woaant iot documenyted that way" (/home/user/7lm@origin/main:L8/L6/history/harmonization-2026-09-04.md:113). It cuts against leaving SPEC:934 unproposed: the owner asked for the exemplars to be documented as they are, imperfect, so the unsheeted folders belong in the exemplar section's "Not yet as stated" account. A second, from the owner's instructions of 11 November 2026: "have them check in their results periodically so we dont lose them." It cuts against holding the drafted proposal outside the repository.
- **corrected_resolution**: Split it, with four changes.

  1. Draft now, as a proposal with the exact replacement text and nothing applied, the correction of SPEC:938 and of the last sentences of SPEC:950 and SPEC:958. Check the draft in with the other agent results, as the owner's word of 11 November asks; do not hold it outside the repository. The specification, its .docx and specification-history.md stay untouched.

  2. Add SPEC:934 to the same proposal with exact wording, following the owner's word of 6 September that the exemplars be documented as they are. Offer two fixes: (a) narrow the bullet and name the unsheeted folders in each "Not yet as stated" paragraph (six in Autonomous, twelve in Auditonomous); or (b) no change to the specification if the owner has sheets written at those folders under decision 14. This item does not wait on the mirror, since it is untrue on both mains today.

  3. Apply the three mirror sentences only on the owner's word, and only once a mirror is on each exemplar's main, whichever mirror the owner lands under decision 6. SPEC:950 follows Autonomous, SPEC:958 follows Auditonomous, SPEC:938 needs both. Draw the text against the specification on scaffold main at that time; the line numbers and wording differ if the beta or PR #19 has merged. Patch the .docx by hand in the same commit and add an entry in specification-history.md. By the precedent of 12 September 2026 (specification-history.md:81-82) propose a new version date, which also changes the header comment, dateline, Version box, the .docx footer and description, and the three other live files that name the version. The owner confirms the date.

  4. GUIDE:474 goes to the owner as a question tied to decision 8. If PR #20 merges, the retired guide's text stands verbatim and is not corrected. If it does not, the guide is live on main and the sentence "Both exemplar repositories do exactly this." needs a proposed fix of its own.
- **corrected_confidence**: The quotations favour the core (propose, apply nothing, wait for the mirrors and the owner's word): REC:482, REC:484 and SPEC:930 are verbatim and on point, and the 12 September precedent in specification-history.md supports it. On SPEC:934 the owner's word of 6 September favours documenting the unsheeted folders, but the wording and the choice between documenting and sheeting are the owner's. The version date rests on record precedent, not on a word of the owner. GUIDE:474 depends on the undecided PR #20.
