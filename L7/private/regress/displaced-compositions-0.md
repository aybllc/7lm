# L7/compositions - application-scoped selections

A composition is the written record of one application: what it is for, which local artifacts and
pins it selects, which source-scoped meanings and mappings it selects where more than one is live,
and which material alternatives and contradictions it did not select. Compositions sit at L7,
outside the USO, because selecting for one application is a different act from owning, adjudicating,
or superseding. A composition reads uso/; it never owns it. A composition is not an L4 application
record: the apparatus, data, protocol, software, and the claims an application itself makes are
owned at /uso/l4, and a composition NAMES that L4 record rather than restating it — what is recorded
here is only the selection across owners, which layer artifacts and which pins this use binds
together.

## What every composition declares

| Section | Requirement |
| --- | --- |
| Purpose and scope | What this composition is built to do, for whom, and where the application stops. State what it is not for. |
| Selected local artifacts and pins | The exact uso/ artifacts by layer and path, and the exact pins by /L7/PINNED filename. Name versions wherever the artifact carries one. |
| Selected source-scoped meanings and mappings | For every term, definition, interpretation, state space, assumption, or semantic mapping with more than one live alternative, name the one used here and the layer artifact that owns it. |
| Material unselected alternatives and contradictions | The live alternatives not selected, plus each contradiction, tension, or inconsistency this application works across, each with a one-line reason for non-selection and its current disposition. |

## Manual work

1. Write purpose and scope first, and keep it narrow. A composition scoped to "everything" cannot
   honestly enumerate what it did not select.
2. List the selected local artifacts by layer and path, and the selected pins by filename. If a
   needed artifact has no layer owner yet, stop and route it first; a composition cannot create an
   owner.
3. Name every lower-layer definition, interpretation, state space, and assumption this composition
   uses. Naming is required; silent selection is not permitted.
4. For each selection where live alternatives exist, name the selected source-scoped meaning and the
   artifact that owns it, so a reader can tell selection from adjudication.
5. List the material unselected alternatives. Material means it would change a result, an
   interpretation, or a boundary of this application, not merely that it exists.
6. List the contradictions, tensions, and inconsistencies you worked across, each with its own
   disposition. Do not collapse them into one another and do not resolve them here.
7. Mark every selection inside the composition as application-scoped, so a later reader cannot read
   it as adjudication at a layer.
8. Leave unselected live alternatives exactly where they are, current, in their owning layers.
9. When the application changes, revise the composition and record the successor relation to the
   earlier one. Do not rewrite layer artifacts to match a new composition.

## Boundary

- A composition-specific or application-specific choice is application-scoped. It is not universal
  supersession, not adjudication, not ratification, and not a change of canonical status.
- Non-selection is not history. Unselected live alternatives remain current and do NOT move to
  uso/l6/history. Only rejection, recall, failure, or supersession adjudicated by the layer owner
  sends an artifact to L6, and those dispositions are different from one another.
- A composition does not acquire ownership of anything it selects. The layer owner keeps ownership
  of the local artifact; the owning repository keeps ownership of the pinned authority artifact.
- A composition cannot repair, silently select, or redefine an unresolved lower-layer meaning. Where
  the meaning is unresolved, the composition names the open question and stays inside it, or waits.
- No authority content is copied here from /L7/PINNED, and no definition is coined here. Terms and
  definitions belong to their layer owner in uso/.
- Consistency is not an argument for an interpretation. Formal consistency under one interpretation
  does not choose that interpretation, and similarity between two artifacts does not establish
  identity, equivalence, or semantic authority.
- Working inside a composition does not raise the epistemic status of any claim it uses, and
  provenance or integrity of a selected artifact does not establish its scientific validity.

Record any reusable process problem you hit here in /L7/process-lessons.md.
