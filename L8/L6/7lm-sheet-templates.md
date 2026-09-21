# The Seven-Layer Model: Sheet Templates

A sheet is the `0.md` in a folder. Two things about it are not design choices: it exists, in every folder of the tree the scaffold pushes, and its first line is the folder's own path from the root, written like `# L8/L3/engineering-mathematics/`. Everything after the first line is a design choice. For a layer's own sheet, `L8/L0/0.md` through `L8/L6/0.md`, the recommendation is at least one sentence more than the layer's number — one at L0, two at L1, three at L2, and so on — stating the space of the folder and what it does. A folder beneath a layer is a design choice through and through: its sheet may be blank, the first line and nothing else. A blank sheet is skipped, and is tagged at the end of the document that collects the sheets as an audit exception for HOA review.

A new repository's sheets start at the degree its owner chooses. Three degrees are given here. The sheets of `aybllc/7lm` are complete, detailed, and rigorous: the full degree. Where a template and the specification differ, the specification controls.

A template is copied into the folder as its `0.md`, the angle-bracketed parts replaced, and the brackets removed. Keep the first line exact.

A template here is the content of a sheet, at a degree. The form in which all of a repository's sheets are republished outward is a separate choice; section 14 of the guide states what is meant there one day; for now everything is HOA.

---

## Minimal

The requirement and the recommendation, and nothing else. For a layer's own sheet, the first line is the path and the body is at least one sentence more than the layer's number, stating the space of the folder and what it does.

```markdown
# <path from root>/

<The space of this folder and what it does, in at least one sentence more than the layer's number.>
```

At L0, one sentence:

```markdown
# L8/L0/

What this object means before anything else is said: the ontological, semantic, epistemic, and universality distinctions it authored itself, and only those.
```

At L1, two:

```markdown
# L8/L1/

The states this object admits under the contract L0 established, the states it excludes, and the invariants that hold across them. Nothing moves here; transitions begin at L2.
```

For a folder beneath a layer, the minimal sheet is blank: the first line and nothing else.

```markdown
# L8/L1/state-space/
```

A blank sheet passes the one CI check, which reads the first line and nothing after it. It is skipped, and it is tagged at the end of the document that collects the sheets as an audit exception for HOA review: a person sees the list of what was left blank and decides.

---

## Standard

The four questions a filer asks of a folder, each under its own heading. The first line is the path. This degree and the full one serve a layer's own sheet and a folder beneath it alike.

```markdown
# <path from root>/

## What this directory is

<What the folder is, in the specification's terms where it has them.>

## Why it exists

<What it keeps apart from what.>

## Holds

- <A kind of thing filed here.>

## Does not hold

- <A kind of thing that looks as if it belongs here, and the path where it belongs.>
```

Filled, at L4:

```markdown
# L8/L4/work/writing/

## What this directory is

Writing this object produced — manuscripts, notes, specifications — in the form it was made.

## Why it exists

Keeps the produced file at the layer that made it, apart from its argument at L5, its history at L6, and its release at L7.

## Holds

- Produced writing, in its formats.

## Does not hold

- What the writing argues — `L8/L5/research/`
- Its drafts, versions, and corrections — `L8/L6/history/`
- Its released identity — `L7/allications/publications/`
```

---

## Full

The form the sheets of `aybllc/7lm` take: the standard four, with the object identified on a line beneath the path, the boundary the specification states for the position, and the position's standing — whether it may remain empty, what inherited term touches it, whether machine metadata is instantiated. A position sheet takes the form below. A layer's own sheet, `L8/Ln/0.md`, takes a different form. Beneath the object and path line it states the layer in prose; then the specification's information sheet for the layer — core question, function, directional inputs, output, hard boundary, machine metadata — with what the layer owns, what occurs there, its boundary indicators, its directory structure, a prose-and-rationale row for each child, the specification's notes on the layer, and its direction.

```markdown
# <path from root>/

**Object:** <One line: what this position is for, in the specification's words where it has them.>
**Path:** `<path from root>/` · **Layer:** <Ln — NAME> · **Owner:** <the owning position>

## What this directory is

<What the folder is, quoting the specification's prose cell for the position.>

## Why it exists

<The specification's Why cell, and what the position keeps apart from what.>

## Holds

- <A kind of thing filed here.>

## Does not hold

- <A kind of thing that looks as if it belongs here, and the path where it belongs.>

## Boundary / traversal rule

<The boundary the specification states for this position or its layer.>

## Standing

- This branch may remain empty. Presence in the agnostic topology establishes admissible capability, not mandatory population; unused now does not mean removed.
- <Inherited terms and dispositions that touch this position, or that none does.>
- Machine metadata: described at <the layer's sheet>; <instantiated or not>.
```

Worked examples at this degree are the sheets of this repository: a position, `L7/allications/notifications/0.md`; a layer, `L8/L0/0.md`.
