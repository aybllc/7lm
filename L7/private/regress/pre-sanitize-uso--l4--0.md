# L4 - Application and Implementation

L4 is the present application and implementation boundary of this scaffold: the outer edge at which
selected L0-L3 artifacts are put to work against real data, apparatus, protocols, and software. It
is the current edge of the work, not a permanent ceiling; the boundary moves outward when the lower
layers are ready to support the move. An L4 record states what one application selected, for what
scope, and what it deliberately left unselected.

## Manual work

1. Confirm the object is an application. If the work proposes a new definition, interpretation,
   state space, formal result, or engineering method, it belongs to a lower layer; send it back
   through L7 ingress instead of absorbing it here.
2. Give the application an identifier and a short statement of what it attempts and for what scope.
3. Name every selected L0-L3 artifact by layer, file, and exact version. Naming is mandatory: a
   higher layer may use a lower-layer definition, interpretation, state space, or assumption only
   by naming it.
4. Name every pinned authority the application relies on, by its binding in /L7/public/ingress. Cite the
   binding only; authority content stays in the owning repository and is never copied into uso/.
5. Record the interpretations selected - which L0 interpretation of each term with more than one
   live meaning this application uses, and the layer artifact that owns it. Selection is not
   adjudication and is not a semantic mapping.
6. Record the concrete apparatus of the work: data, apparatus, protocols, and software, each with
   identity, exact version, configuration, and operating conditions.
7. Record assumptions explicitly, including assumptions inherited from lower layers and any adopted
   without examination.
8. Record the live alternatives not selected, one line each on why this application did not select
   them. They remain current and remain owned by their layers.
9. Record limitations: what the result does not establish, what remains unvalidated, and what
   observation would falsify it.

## Record fields

One record per application; every field is filled or explicitly marked absent.

| Field | Record | Rule |
|---|---|---|
| Application ID | Stable local identifier and date | Never reused for different work |
| Purpose and scope | What is attempted, for which scope | Scope is stated, never assumed universal |
| Selected artifacts | L0-L3 artifacts by layer, file, exact version | Named, not summarised or paraphrased |
| Pins used | Bindings in /L7/public/ingress | Binding only; authority content stays with its owner |
| Interpretations selected | Term to the L0 interpretation actually used, and the layer artifact that owns it | Selection is not adjudication and is not a semantic mapping |
| Data | Dataset identity, version, extent, conditions | Recorded even when the data are local |
| Apparatus | Instruments, hardware, settings, calibration state | Record what was not controlled |
| Protocols | The procedure as actually followed, with deviations | Record the run performed, not the run planned |
| Software | Programs, versions, environment, configuration | Version pins, not names alone |
| Assumptions | Assumptions used and the layer each comes from | Inherited assumptions are listed, not implied |
| Alternatives not selected | Live alternatives available, and why unselected | They stay current in their own layer |
| Limitations | What is not established; checks still open | Absence of contradiction is not support |
| Epistemic status | Status of each claim this application makes | An internal run is not external validation |

## Scope of an L4 selection

An L4 selection is application-scoped and settles nothing outside the application.

- Selection is not supersession. Unselected live alternatives remain current; nothing about
  non-selection sends an alternative to L6 history.
- Selection is not adjudication. If a choice was forced because a lower-layer meaning is unclear,
  the unclarity is a lower-layer matter and returns there.
- Selection is not ratification and not validation. A working implementation shows the thing can be
  done as specified here; it supplies no independent external support.
- Two applications may select differently and both remain legitimate. Divergence between them is a
  recorded fact, not a defect to be harmonized.

## Keep out

- Do not automate routing, interpretation selection, contradiction resolution, or any lower-layer
  judgment. Work at L4 is manual.
- Do not repair a lower-layer meaning. L4 may only select among what the lower layers actually
  state; if nothing statable exists, the application stops and the gap is recorded.
- Do not select silently. An unrecorded choice between competing meanings is a defect in the record.
- Do not admit new material here. New sources, authority artifacts, and objects enter at L7 ingress.
- Do not move an unselected alternative to L6, and do not label it rejected, failed, or superseded.
- Do not treat repository custody, an exact hash, authority, or internal consistency as scientific
  validity.

When a difficulty here is about the process rather than about this application, record it in
/L7/process-lessons.md.
