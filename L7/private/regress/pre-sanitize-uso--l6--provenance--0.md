# L6 Provenance - Source Identity and Origin

This directory records where local material came from, precisely enough that another person can
retrieve the same object and check the same thing. Provenance answers identity, origin, version, and
handling. It does not answer whether the material is true, sound, or fit for the use made of it. The
local table is source-ledger.md; this file states what a complete entry must contain.

## Manual work

1. Record a source when it is first used, not when the work is written up.
2. Establish recoverable identity first: enough designation that the same object can be obtained
   again by someone who has only the entry.
3. Record the responsible issuer or creator - the agent that bears responsibility for the object,
   which is often not the site or system it was obtained from.
4. Record the exact version: edition, revision, date of issue, or content hash. "Latest" is not a
   version.
5. Record the locator and the retrieval date together; a locator without a date does not identify
   what was actually obtained.
6. Record the scope the source declares for itself, in the source's own terms, and separately record
   the local use made of it.
7. Record every transformation applied between the source object and the local copy: extraction,
   conversion, excerpting, reformatting, translation, correction.
8. Record gaps: parts not obtained, not read, unavailable, or paywalled. An unread part is recorded
   as unread, never as consulted.
9. Record contradictions with other sources or with local artifacts as contradictions, and leave
   them unresolved here.
10. Add the finished entry as one row of source-ledger.md.

## Required fields

| Field | Record | Rule |
|---|---|---|
| Source ID | Stable local identifier | Never reused for a different object |
| Source identity | Title or designation sufficient to retrieve the object again | Identity, not description |
| Issuer or creator | The responsible agent | The distributor is not automatically the issuer |
| Exact version | Edition, revision, date of issue, or content hash | One version per row; a new version is a new row |
| Locator | Where this copy was obtained, including a local path if held | Recorded even for physical holdings |
| Retrieval date | When it was obtained in this form | Paired with the locator, never omitted |
| Declared scope | The scope the source states for itself | In the source's terms, not the local terms |
| Local use | Which artifact or layer uses it, and for what | Use is separate from the source's declared scope |
| Transformations | Every change between source object and local copy | Including excerpting and reformatting |
| Gaps | Parts not obtained, not read, or unavailable | Unread is recorded as unread |
| Contradictions | Disagreement with other sources or local artifacts | Recorded, not reconciled here |

The ledger header carries eight columns: Source identity and Locator share its 'Source and locator'
column, and the transformations, gaps, and contradictions required above are recorded in its
'Status / notes' column, each prefixed with its field name. Any conversion, excerpting,
reformatting, or timestamp normalisation applied between the source object and the local copy is
recorded there verbatim and is never omitted as housekeeping.

## What provenance does not do

Provenance supports audit and retrieval. It does not establish scientific validity.

- An exact hash proves fixity: that this object is byte-identical to the one recorded. It proves
  nothing about whether the content is correct.
- Custody, careful handling, and a complete chain of origin do not make a claim true.
- The authority of an issuer does not transfer to the local use made of the material.
- Recording a source is not endorsing it. A contradicted, withdrawn, or wrong source is still
  recorded, with its status noted.
- Compare PROV-DM: The PROV Data Model, W3C Recommendation 30 April 2013, Abstract: "Provenance is
  information about entities, activities, and people involved in producing a piece of data or thing,
  which can be used to form assessments about its quality, reliability or trustworthiness." Forming
  an assessment is not the same act as establishing validity, and that specification says nothing
  about this scaffold.

## Boundary

- Do not copy, paraphrase, or restate the content of a pinned authority into uso/. A pin is a
  binding; the content stays with its owner.
- Do not merge two versions of a source into one row, and do not overwrite a row when a new version
  appears.
- Do not harmonize disagreeing sources. Independently scoped sources may disagree without either
  being defective.
- Do not use this directory as an intake point. New material enters at L7 ingress.
- Do not cite anything here that was not actually obtained and read in the form recorded.
- Every time recorded here is a time about the source object — its issue, retrieval, or handling.
  Times inside the material a source describes, such as when a phenomenon occurred or when an
  instrument recorded it, are content and belong to the layer that owns that artifact, never to
  this ledger.

When a difficulty here is about the process rather than about a particular source, record it in
/L7/process-lessons.md.
