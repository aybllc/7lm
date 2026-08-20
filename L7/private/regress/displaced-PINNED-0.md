# L7/PINNED - fixed authority bindings

The Scientific Desktop pins an authority artifact when this scaffold must consume something it does
not own. A pin is a fixed binding: it names the owner, names the artifact, fixes one immutable
version, and declares the scope this scaffold consumes it for. The binding lives here; the authority
content stays in the owning repository. A pin settles which referent is meant. It does not establish
scientific validity, it does not confer semantic authority on any layer of uso/, and it does not
adjudicate meaning anywhere.

## Required binding fields

One pin per file. Every pin states all five fields. A pin missing a field is not admitted.

| Field | Requirement | Why it is required |
| --- | --- | --- |
| Owning repository or issuing authority | Name the repository, standards body, or publisher that owns the artifact, exactly as the owner designates itself. | Ownership is what makes the artifact an authority artifact for a consumer, and it is the only address a defect can be routed back to. |
| Repository-relative artifact path | Give the path inside the owning repository; for a published standard give the clause, entry, or section locator instead. | An owner name alone does not identify which artifact is bound. |
| Exact immutable version | Give a commit id, release tag, or edition plus date that cannot move. A branch name, "latest", "main", or "current" is not admitted. | A moving reference silently changes what was consumed and invalidates every downstream statement that named this pin. |
| Integrity identifier | Give a hash or equivalent digest when the owner publishes one, or when you can compute one over the exact fetched artifact. Otherwise write "not available". | It lets a later reader detect that the artifact in hand differs from the artifact bound. Integrity is a preventive property, not evidence of validity. |
| Declared consumer scope | State in one or two sentences what this scaffold consumes the artifact FOR, and what it does not consume it for. | An authority artifact is authoritative only within a scope; an undeclared scope invites a higher layer to reuse the pin for a question the owner never covered. |

## Manual work

1. Confirm the artifact is genuinely owned elsewhere. If a layer inside uso/ can state it without
   importing unresolved assumptions, it is a local artifact with a layer owner, not a pin.
2. Locate the exact version by hand and record the five fields above in a new file in this
   directory, one pin per file.
3. Write the declared consumer scope in your own words. Do not paste the owner's abstract, title, or
   scope clause in place of your consumer scope.
4. Record an integrity identifier when one exists; write "not available" rather than omitting the
   field.
5. Cite the pin from the consuming side. The uso/ artifact or the composition NAMES the pin;
   nothing is copied downward from here.
6. When two active pins disagree, record the disagreement as a contradiction or a tension in the
   consuming artifact, and leave both pins active and unedited.
7. When you re-consume a pin, re-check by hand that the version still resolves and that the
   integrity identifier still matches. Record a failed check as a failed check.
8. When a binding is replaced, keep the earlier pin file and record the successor relation in both
   files.

## Immutability is a manual rule in this phase

- An admitted binding and the referenced authority content are treated as read-only by repository
  rule. Do not edit, delete, move, copy, rename, replace, or paraphrase them, and do not route the
  authority content down into uso/.
- Only the binding lives here. The authority artifact remains in its owning repository, in the
  owner's custody, under the owner's control and versioning.
- No OS permissions, Git hooks, branch protection, or Actions are implemented in this phase. Nothing
  enforces this rule mechanically. A human enforces it, or it is not enforced.

## Multiple pins may be active at once

- Pinning one authority does not rank, merge, invalidate, harmonize, or supersede another.
- Independently scoped authorities may disagree. Disagreement is not automatically an owner defect;
  it is often two owners answering two different questions inside two different declared scopes.
- Coexisting pins do not combine into a single authority. If one application needs one of them, that
  selection is made in /L7/compositions and is application-scoped there.

## Owner-defect procedure

Use this only when the owner's artifact is defective within the owner's own declared scope, not when
it merely disagrees with another authority or fails to answer a local question.

1. Exit the consumer USO. Do not repair the artifact here and do not annotate a correction into the
   pin.
2. Correct the artifact in the owning repository, through that owner's process.
3. Admit a NEW exact binding to the corrected version, restating all five fields.
4. Preserve the earlier binding and record the successor relation between the two bindings, so a
   reader can see what was consumed before the correction.

## Terms used here

`pin`, `canonical`, `integrity`, and `successor relation` are defined in /uso/l0/definitions/0.md;
name the row there rather than restating it here.

## Keep out

- This directory does not become a definitions, terminology, taxonomy, thesaurus, ontology, or
  standards-content directory. Terms, definitions, and semantics are owned by layers inside uso/.
- No copies, extracts, mirrors, paraphrases, or reformattings of authority content. A quotation used
  in an argument belongs in the uso/ artifact making that argument, with its locator, not here.
- No ranking, scoring, harmonization, federation, or thesaurus union across pinned authorities.
- No validity claims. Repository custody, an exact hash, authority, internal consistency, and
  provenance do not by themselves establish scientific validity.
- No scripts, hooks, workflows, schemas, or generated indexes of this directory in this phase.

Record any reusable process problem you hit here in /L7/process-lessons.md.
