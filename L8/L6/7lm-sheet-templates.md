# The Seven-Layer Model: Sheet Templates

A sheet is the `0.md` in a directory. In the current 7LM scaffold, every canonical directory has one. Its first line is the directory's own path from the root, written like `# L8/L3/engineering-mathematics/`, and its body states the semantic meaning of that directory: what occurs there and what distinguishes it from neighboring positions.

The directory may otherwise remain empty when unused. The `0.md` does not need to manufacture content for the directory, but a current canonical sheet is not complete if it contains only a heading. Detail can range from a minimal semantic statement to a full information sheet; the minimum is meaning, not population.

A new repository's sheets start at the degree its owner chooses. Three degrees are given here. The sheets of `aybllc/7lm` are complete, detailed, and rigorous: the full degree. Where a template and the specification differ, the specification controls.

A template is copied into the folder as its `0.md`, the angle-bracketed parts replaced, and the brackets removed. Keep the first line exact.

A template here is the content of a sheet, at a degree. The form in which all of a repository's sheets are republished outward is a separate choice; section 14 of the guide states what is meant there one day; for now everything is HOA.

---

## Minimal

The smallest current sheet states the path and at least one substantive semantic statement describing what occurs in the directory. Minimal means concise; it does not mean semantically blank.

```markdown
# <path from root>/

<What this directory represents or what occurs here, stated in at least one substantive sentence.>
```

At L0, one sentence:

```markdown
# L8/L0/

The foundational ontological, semantic, epistemic, and universality distinctions used by this bounded object before an admissible state is declared.
```

At L1, two:

```markdown
# L8/L1/

The states this object admits under the contract L0 established, the states it excludes, and the invariants that hold across them. Nothing moves here; transitions begin at L2.
```

For a directory beneath a layer, the same semantic minimum applies:

```markdown
# L8/L1/state-space/

The admissible and excluded states, dimensions, identity conditions, and static invariants of the bounded object before formal operation begins.
```

The branch may contain no other files when unused. The sheet still states what the coordinate means.

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
**Path:** `<path from root>/` · **Position or Layer:** <use "Layer" for L0-L6 interior layers; use "Position" for L7 surface positions> · **Owner:** <the owning position>

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

- This branch may remain otherwise empty. Presence in the canonical topology states the meaning of the position; it does not require a project to populate that position with artifacts.
- <Inherited terms and dispositions that touch this position, or that none does.>
- Machine metadata: described at <the layer's sheet>; <instantiated or not>.
```

Worked examples at this degree are the sheets of this repository: a position, `L7/allications/notifications/0.md`; a layer, `L8/L0/0.md`.
