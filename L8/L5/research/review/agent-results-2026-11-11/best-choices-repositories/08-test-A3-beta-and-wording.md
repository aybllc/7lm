# test:A3-beta-and-wording

Agent result, as returned. Workflow: Best choices: the scaffold, the exemplars, the eleven proposals. Run `wf_8e87a1b5-8ec`. Phase: Test.

- **verdicts**
  - item 1
    - **id**: M5
    - **quotes_ok**: yes
    - **state_ok**: no
    - **stands**: yes
    - **final_best_choice**: Do not merge beta/common-contracts-r1-r6, now or after pull request #19; leave it untouched at 97314c5. Treat your R1–R6 approval as not covering 97314c5. Any correction you want from it reaches main as its own pass, item by item, under a new version date, with your approval quoted.
    - **final_why**: A plain merge puts the R1–R6 text under the version of 12 November, whose row says only the exemplar section changed. It also rewrites three lines of the retired field guide, which the record keeps verbatim. It conflicts with main in 2 files, and in 7 with pull request #19, now pushed as 8aa66c1. No file quotes your approval. 97314c5, made the next day, claims no approval, has no record entry and says it is not a merge. One item rewrites the clarification that rests on your ruling of 6 September. Holding loses nothing and keeps the exemplar betas' pin to 4ca3edb resolvable.
    - **final_confidence**: high
    - **note**: The pick stands. Both quotations are verbatim at 6de996b: the record at line 482, and specification-history.md at line 28.

      One statement is stale. The reconciliation of #19 is no longer 'built locally (38e2ec3, not pushed)'. origin/ccr-00099fac-hjosbo is now 8aa66c1, amended from 38e2ec3 at 20:10 UTC, and the two commits differ only in the record and specification-history.md. Measured in a fresh scratch copy, git merge-tree against 8aa66c1 conflicts in the same 7 files.

      Re-verified in scratch copies:
      - Main conflicts with the beta in 2 files, the .docx and specification-history.md.
      - The merged specification keeps the dateline 'Version of 12 November 2026' (line 18) and carries the beta's scale text (line 683).
      - The retired guide changes at lines 96, 150 and 230.
      - R1–R6 is named in no file of any ref outside the agent results except beta specification-history.md:106.
      - 97314c5 touches 18 sheets and no history file. It mentions no approval and disclaims being a merge.
      - The beta adds 8 files. The check changes by 17 lines added and 19 removed. Main's check still admits USO/ at integrity.yml:27-28.

      One evidence locator carries a remark about the colleague's own runs touching timestamps in /home/user/7lm. [source text withheld from the public copy] owner and should be dropped.

      Two things the colleague missed, both supporting the pick:
      - The owner, 2026-10-17: 'Put the field guide into l6 as provenance stale. Deprecated and to be used as an example.' (scaffold record line 518).
      - The precedent of §40 ('fix them', line 530). It kept the guide edits of #19 and the audit branch off the retired copy, which 'stays verbatim' (line 534). This beta was never reconciled that way.
  - item 2
    - **id**: RH1
    - **quotes_ok**: yes
    - **state_ok**: no
    - **stands**: yes
    - **final_best_choice**: Name the scaffold's main (today 6de996b) as what both exemplars match, in tree and sheets' first lines; 4ca3edb and 97314c5 count only once on main. Updates come by hand passes, each naming the commit matched in a new dated record entry, not by the unbuilt review at L7/peering/private/.
    - **final_why**: Your merge of pull requests #29 and #30 put mirrors of the scaffold's main on both exemplars, and nothing of 4ca3edb or 97314c5. Since then main has changed 13 files outside the agent results. None is a canonical position or the check, so both exemplars match 6de996b at all 71 positions. The beta commits are unmerged, and carrying them out would be an outside update ahead of the scaffold. You put the review route 'in the future' and said 'for now everything is HOA'; none of it is built. No record names the commit mirrored, so each pass should name it.
    - **final_confidence**: high
    - **note**: The pick stands, tightened. Both quotations are verbatim, at record lines 336 and 350.

      Corrections:
      1. 'No exemplar main names any scaffold commit' is untrue. Auditonomous main names fb22e25, a scaffold commit of 5 September, at L8/L6/history/7LM_ROUTING_PLAN_2026-09-05.md:6. What holds is the evidence bullet: no exemplar main names c9dc061, 6de996b, 4ca3edb or 97314c5. So no record pins what the mirror of 11 November matched.
      2. The locator note '(each pass made from main)' at Autonomous record line 213 and Auditonomous line 206 means each exemplar's own main, as against its beta. That the mirror follows the scaffold's main is shown at Autonomous record lines 187-189 and Auditonomous lines 180-182, and by the check blob f43dd04.
      3. The canonical list is integrity.yml:47-59 (71 positions). Lines 47-51 hold only the 35 L7 positions.
      4. The colleague's on_yes adds a line to the section of 11 November. The records keep sections as they were written ('A record states what was so when it was written', scaffold record line 327; §42 leaves §41 unchanged). The pin belongs in a new dated entry.

      Missed, and supporting the pick: the owner, 2026-09-20, 'for now everything is HOA' (scaffold record line 376).

      Verified:
      - c9dc061 to 6de996b changes 13 files outside the agent results, one a rename of the guide, and the check blob is unchanged.
      - All 71 positions are sheeted on all three mains and all three betas.
      - Both exemplar betas pin 4ca3edb at binding.json:7.
      - The manuscript guidance is at beta L8/L4/work/writing/0.md:12. The layer lists are absent from 97314c5.
  - item 3
    - **id**: M4-6
    - **quotes_ok**: yes
    - **state_ok**: yes
    - **stands**: yes
    - **final_best_choice**: Let the mirror's wording stand, as merged. Keep beta/7lm-exemplar-autonomous (e64b382) and beta/7lm-exemplar-auditonomous (714480d) exactly as they are: not merged, rebased, reconciled or deleted. Anything wanted from them reaches main one item at a time, by its own pull request, never by merging either branch.
    - **final_why**: Your merge of pull requests #29 and #30 settled the wording: both mains carry the mirror of the scaffold's main. Measured today, the betas conflict with their mains in 12 and 13 files. In each repository 34 files are changed on both sides and end different, so a merge would also blend 22 and 21 files without warning. Wording after a sheet's first line is a design choice, so nothing requires reconciling them. Keeping both branches loses nothing and keeps their pins resolvable. Among them is the Auditonomous beta's pin to Autonomous commit 805cd42, which only the Autonomous beta holds.
    - **final_confidence**: high
    - **note**: The pick stands. Both quotations are verbatim, at record lines 543 and 350.

      Re-measured in scratch copies (9fa3744 against e64b382, aa30b03 against 714480d):
      - 12 and 13 conflicts, exactly the files listed.
      - Merge bases c9076c3 and 2165144.
      - 34 files in each repository changed on both sides and different; 22 and 21 of them merge without a conflict.
      - All 71 positions sheeted on both mains and both betas.
      - The Auditonomous beta's check is blob cd39c5b, the scaffold beta's file.

      One clause in the cost is inexact: 'their check files ... follow an unmerged scaffold commit'. The Autonomous beta's check (blob 670bd3e) is not the scaffold beta's file. It hard-codes the uppercase list as 4ca3edb does, but still admits USO/ at the root. The clause is true of Auditonomous and of both pins.

      Added support for keeping, not deleting: the Auditonomous beta's binding (L7/peering/public/ingress/peer-1/object-2/binding.json:5) pins Autonomous commit 805cd42. Only origin/beta/7lm-exemplar-autonomous holds that commit.
  - item 4
    - **id**: M7
    - **quotes_ok**: yes
    - **state_ok**: yes
    - **stands**: yes
    - **final_best_choice**: Keep all of it on the two beta branches, untouched; take none of it to main by merging. Have the 31 items put to you one by one as proposals (file, what is wrong, exact fix); each reaches main only on your yes, by its own pull request.
    - **final_why**: Merging would settle, without you, decisions both records leave open. Auditonomous's record lists Appendix C, Q13 and the CONTRADICTIONS rows as owner decisions left open with nothing done, and its review sheet says CONTRADICTIONS.md is not edited. Autonomous's record holds the REGISTER contest open, and the beta settles it by deleting the blocker row. None of these edits conflicts with main, so a merge would take them in without a prompt. Item-by-item proposals are the form the record's standing of 20 September sets, and keeping the branches loses nothing.
    - **final_confidence**: high
    - **note**: The pick stands. Both quotations are verbatim, at record lines 482 and 150.

      Verified with git diff --numstat from the merge bases:
      - The Autonomous beta adds 13 files that are not sheets. It edits REGISTER.md (2 lines added, 2 removed), DEFINITION_LIST_AUTONOMOUS.md (2 added), the press-kit README.md (4 added, 5 removed) and GLOSSARY_AUTONOMOUS.md (2 added).
      - The Auditonomous beta adds 10 such files. It edits AUDITONOMOUS_DEFINITION.md (16 added), REQUIREMENTS_OWNERSHIP.md (2), CONTRADICTIONS.md (15) and LEDGER.md (8).
      - That makes 31 items.

      Also verified:
      - The REGISTER entry is at beta line 12; the deleted blocker row is at main line 19.
      - Auditonomous record line 93 and its review sheet line 35 say what the colleague reports, as does Autonomous record line 81.
      - The mirror left the six named files untouched.

      The strongest alternative weighed: filing the beta's research objects as PARKED at the catch-all on main. The owner's words support the catch-all: 'research/review/ works as a catch all' (specification-history.md line 27). It is still the worse choice. The objects pin 4ca3edb and 805cd42, commits off the scaffold's main, and BETA_SOURCE_OVERLAY.md is written to govern the register.

      Consistency: the research resolver's RH2 says BETA joins 'only after the 7lm decides its own beta' (auditonomous 33135b7, agent-results-2026-11-11/best-choices-research/01-resolve-B1-branches-and-order.md line 11). Under a yes to M5 that condition does not arise, which agrees with this pick.
  - item 5
    - **id**: M10
    - **quotes_ok**: yes
    - **state_ok**: no
    - **stands**: yes
    - **final_best_choice**: No. Keep the exemplars as merged: line 8 of L7/allications/0.md with your quotation of 19 September, and your words of 11 November as written in both exemplar records. When pull request #19 reaches the scaffold's main, do not copy its lines 8 and 10 into the exemplars.
    - **final_why**: The instruction of 6 October survives only in indirect speech, and it concerns what the public sees; the scaffold heads the exemplars as private. The specification, on main and in pull request #19 (now pushed as 8aa66c1, same lines), says each repository's records carry the words verbatim. What a sheet says after its first line is a design choice, so the exemplars stay in step without the new wording. Its line 8 points to a record neither exemplar holds. You merged line 8 twice after the 7 September pull-out of such quotations. Publishing the exemplars would change this.
    - **final_confidence**: medium
    - **note**: The pick stands. Both quotations are verbatim: record line 350, and agent-results 0.md line 8 on 6de996b (time as in owner-words.txt line 7).

      One statement is stale. #19's reconciliation is no longer 'built locally (38e2ec3, not pushed)'. PR #19's branch is now 8aa66c1, pushed and amended at 20:10 UTC. L7/allications/0.md lines 8 and 10 and the specification line 940 are unchanged there.

      Verified:
      - Line 8 is identical on the three mains.
      - Neither exemplar holds harmonization-2026-09-04.md.
      - The b5c3984 record at line 514 is in indirect speech.
      - L7/0.md line 159 heads the exemplars as private.
      - The exemplar records match the cited lines: Autonomous 185 and 167, Auditonomous 178 and 160.
      - Line 8 entered in 606d4b3 and reached main in 0d1ec40 (EDM, 20 September). Neither exemplar beta's sheet quotes the owner.

      Missed and weighed: 'the 0.md file only states the space of the dir and what it does' (record line 336) cuts against a quotation in a sheet. §27 (line 350, read at line 352) makes what a sheet says after its first line a design choice. The owner's later acts of merging line 8 keep the pick ahead of dropping its first sentence, which is the colleague's ready fix if the owner wants the 7 September rule applied.
  - item 6
    - **id**: PR28
    - **quotes_ok**: yes
    - **state_ok**: no
    - **stands**: yes
    - **final_best_choice**: Mark #28 ready and merge it into Auditonomous main as it stands (now 33135b7, check-in no. 13: 352 files in that one folder, nothing else); later check-ins follow by new pull request. The complete copy lives there, at the scaffold's public-copy path, nowhere public.
    - **final_why**: You asked for the results in Auditonomous so they are not lost, and on 13 November you merged the public copy into the scaffold's main with pull request #20. The complete copy exists only on #28's branch. The scaffold's public sheet says it is at that path in Auditonomous, which is untrue of its main until #28 merges. The merge is clean and adds only that folder: 352 files at check-in no. 13, each of its 14 folders sheeted, no conflict markers. Auditonomous is not public, and its copyright sheet lets quotations travel there. One revert undoes it.
    - **final_confidence**: high
    - **note**: The pick stands, restated for today. Both quotations are verbatim at scaffold main agent-results 0.md line 8, with times as in owner-words.txt lines 6 and 7.

      The state has moved since the colleague wrote. At 20:11 UTC, check-in no. 13 moved #28's branch from 3696894 to 33135b7, adding 41 files: the #19 review and this run's best-choices results. Measured in a fresh scratch copy:
      - 352 files added, all under the folder, nothing else.
      - The test merge is clean and its result equals the tip's tree.
      - 14 folders, each headed by its path; no conflict-marker lines.
      - 17,165,405 bytes.
      - Three workflows still 'Running' (0.md lines 28-30 and 40).

      The public copy on scaffold main is still check-in no. 12 (311 files). The public check-in no. 13 sits on scaffold branch ccr-9391bd81-f2enmj at 029f3bb, not on main. Both no. 13 copies hold the same 352 paths.

      At no. 12, the 222 files that differed were 213 carrying the withheld marker and 9 sub-sheets saying so.

      Missed, and supporting the pick:
      - The owner's 'merge 20' of 13 November (owner-words.txt line 20). Its merge, 6de996b, brought the 311-file public copy to main.
      - 'keep pushing the check-ins to both repos' (owner-words.txt line 9).

      A separate one-line fix for both copies at the next check-in: the folder sheet's Object line (0.md line 3) says the workflows ran on 11 November, and it now also holds four of 13 November.
