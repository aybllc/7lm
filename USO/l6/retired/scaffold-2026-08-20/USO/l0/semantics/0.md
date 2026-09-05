# L0 - Semantics

This directory holds source-scoped meanings: what an expression means, under which source, at which
version, within which scope, and how one interpretation stands to another. Meaning is recorded per
source, never as a corpus average. Two sources that read a term differently produce two
interpretations here, both current, until an owner adjudicates a controlling use for a stated
scope. Higher layers must NAME the interpretation they use; they may not silently select one.

## What one interpretation record states

- The exact source identity, its version or edition, and the scope the source itself declares.
- The expression as the source writes it, and the reading in plain prose.
- What the reading excludes, and which readings it is being distinguished from.
- Definition status, the layer owner or candidate owners, and the date of adjudication if any.
- The live alternatives that remain current alongside it.

## Syntax is not meaning

A well-formed expression is not thereby a meaningful one. ISO/IEC/IEEE 31320-2:2012, 3.1.195,
defines "syntax" as "The structural components or features of a language and rules that define the
ways in which the language constructs may be assembled together to form sentences", and 3.1.175
defines "semantics" as "The meaning of the syntactic components of a language". The same standard
keeps the two jobs apart in its own scope: "This standard defines the semantics and syntax of
IDEF1X. It does so by defining the valid constructs of the language and specifying how they can be
combined to form a valid model" (1.1 Scope, page 1). Check well-formedness first, then ask
separately what the expression means, under whose reading, and within what scope.

## Relation types between interpretations

Whenever two interpretations are related, name the relation type. These are different relations and
must never be collapsed into one another.

| Relation | Asserts | Does NOT assert | Basis | Source or locator |
| --- | --- | --- | --- | --- |
| identity | The two names denote the same thing; substitution is safe throughout the stated scope. | Any agreement between the sources on anything else. | Project rule | - |
| equivalence | As defined in /uso/l0/definitions/0.md: two expressions present aspects of the same thing within a named scope. | Identity, or interchangeability outside that named scope. | Adapted from [source] | PROV-DM (W3C Rec. 30 April 2013), as carried by the /uso/l0/definitions/0.md row |
| synonym | One source uses two terms for one concept. | That a second source uses either term the same way. | Project working use | Terminology standards (ISO 1087, ISO 25964) NOT held locally |
| quasi-synonym | Near-substitutes grouped for retrieval, with the residual difference recorded. | Equivalence or identity. | Project working use | - |
| broader term | Within one source's structure, the referenced concept is the more general one. | Subsumption of instances, or the same hierarchy in another source. | Project working use | - |
| narrower term | Within one source's structure, the referenced concept is the more specific one. | Instance membership, or the same hierarchy in another source. | Project working use | - |
| related term | An association that is explicitly not synonymy. | Any hierarchy, equivalence, or identity. | Adapted from [source] | ISO/IEC/IEEE 24765:2017, 1.3: "Cross‐references are used to show a term's relationship to other terms in the dictionary: cf. refers to related terms that are not synonyms." 24765 1.3 fixes only related-versus-synonym, not the broader-term/narrower-term/related-term distinction, which stays Project working use per /uso/l0/definitions/0.md. |
| similarity | A measured or judged closeness under a named measure, with the measure stated. | Any semantic relation whatsoever. | Project working use | - |
| semantic mapping | An assigned correspondence between two things, recorded as ordered pairs for a stated purpose. | That the mapped items are the same, or that either source authorized the mapping. | Adapted from [source] | ISO/IEC/IEEE 31320-2:2012, 3.1.107 "mapping"; IEEE Std 2755-2017, 2.3 "semantic mapping" |

Semantic mapping is not identity. PROV-DM, 5.5.2, warns of exactly this weakness in general
relations: "Note that alternateOf is a necessarily very general relationship that, in reasoning,
only states that the two alternate entities respectively fix some aspects of some common thing
(possibly evolving over time), and so there is some relevant connection between the provenance of
the alternates."

## Manual work

1. Open one record per source, not one per term. A term with three sources gets three records.
2. Quote or cite the source's own declared scope before writing the reading, and keep the reading
   inside that scope.
3. Write the reading in prose, then write what it excludes. A reading with no exclusions has not
   been read closely enough.
4. Compare records pairwise and, for each pair you relate, choose exactly one relation type from
   the table above and record why that type and not the adjacent one.
5. Where two readings differ materially, keep both. Record the difference, the scope of each, and
   the consequence of choosing one; do not merge them early to make a table tidy.
6. Where an owner adjudicates a controlling use, record the scope, the version, the owner, and the
   date, and leave the non-selected readings marked as live alternatives.
7. Note the terminology hazard as a standing condition: ISO/IEC 2382:2015, 0.1, states that "the reader is warned that the
   dynamics of language and the problems associated with the standardization and maintenance of
   vocabularies may introduce duplications and inconsistencies".
8. Register each adjudicated interpretation so /uso/l0/semantic-formulas and higher layers can name
   it by source, version, and scope.

## Keep out

- No unscoped meanings. An interpretation without a source, a version, and a scope is not a record.
- No untyped relations. If you cannot name the relation type, you have not established a relation.
- No authority from similarity. A similarity measure or an automatically inferred relation may
  support review and may prioritize what a human reads next; it cannot create semantic authority.
- No early merge, and no harmonization across independently scoped authorities. Disagreement
  between two pinned authorities is not by itself a defect in either owner.
- No repairing an owner's unresolved meaning from here or from above. If an owner's artifact is
  defective, the correction is made in the owning repository and a new binding is admitted.
- No promotion of a formal result into an interpretation. Formal consistency under one reading does
  not select that reading.

Reusable process problems discovered while doing this work belong in /L7/process-lessons.md, not in
this directory.
