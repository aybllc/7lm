# L1 - Admissibility

L1 states what is admissible: which state variables exist, what values they may take, over
what domains, and under what structure. L1 fixes the shape of an admissible state. It does
not fix meaning - meaning is owned at L0 - and it does not derive, prove, approximate, or
measure anything.

## What L1 owns

- Admissible state variables and the domains their values are drawn from.
- Structural constraints and invariants that hold over whole admissible states.
- Exclusions: what the declaration deliberately refuses to admit, and why.
- Boundary cases at the edge of each declared domain.
- The separation of missing, undefined, and inapplicable from each other and from a value.

## What L1 must name from below

Every L1 declaration names the L0 interpretation it selects: the definition it uses, the
source-scoped meaning of each term, and that definition's definition status. A declaration
that does not name its L0 interpretation is not admissible at L1, because no reader can
tell which meaning the declaration is about. Naming is the whole obligation - L1 imports
the meaning by reference and never restates it.

## Children

- `state-space/` - the declarations themselves: variables, values, domains, structure,
  invariants, exclusions, boundary cases, non-value markers, and the named L0
  interpretation each declaration selects.

## Manual work

1. Identify the L0 artifacts your declaration will use and record the identity and definition status of each.
2. Check whether those meanings are settled. If live alternatives, contradiction, or tension remain at L0, say so in the declaration and mark it provisional.
3. Write or extend a declaration under `state-space/`, naming the selected L0 interpretation in the declaration header.
4. Confirm the declaration imports nothing unresolved from a higher layer: no operator, no derivation, no finite precision, no application choice.
5. Confirm L1 is the lowest layer that can state the artifact without importing an unresolved higher-layer assumption; if L0 can already state it, it belongs at L0.
6. Send anything whose owner or routing is not yet adjudicated back through L7 ingress instead of parking it here as if it were settled.
7. Raise unresolved lower-layer meaning as an L0 matter, in L0, and leave only the named dependency here.

## Boundary

- L1 may not repair, silently select, or redefine an unresolved L0 meaning. Naming the ambiguity is L1 work; ending it is not.
- L1 holds no operators, axioms, derivations, proofs, or counterexamples. Those are L2.
- L1 holds no finite representation, resolution, tolerance, error, or uncertainty. Those are L3.
- A declaration may state the quantity kind and the unit that fix a variable's domain by NAMING the L0 interpretation that carries them; what L1 excludes is the finite side of a unit — resolution, rounding, tolerance, error, and uncertainty — which is L3.
- L1 holds no composition-specific or application-specific selection; such a choice is made at L4 or in an L7 composition and is never universal supersession.
- Authority content is never copied into L1. A pinned authority is named by its immutable binding; its content stays in the owning repository.
- Admissibility is not scientific validity. A declaration can be internally consistent, exactly stated, and still be wrong about the world.

Record reusable process problems found while doing L1 work in /L7/process-lessons.md.
