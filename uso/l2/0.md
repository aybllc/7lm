# L2 - Exact Mathematics

L2 holds exact mathematics stated under a named L0 interpretation and a named L1
declaration. Exact means that nothing in the artifact has a resolution, a unit, a rounding
rule, or an uncertainty. L2 says what follows, given a meaning and given an admissible
state space; it does not choose the meaning and it does not touch the world.

## What L2 owns

- Mathematical objects, their notation, and their domains and codomains.
- Operators, axioms, and the derivations and proofs built from them.
- Counterexamples, kept as first-class artifacts rather than as notes on failed attempts.
- Open obligations: everything the artifact needs but has not established.

## What L2 must name from below

- The L0 interpretation it selects, by identity and definition status.
- The L1 declaration it works over, by name, including which state variables, domains, and
  invariants it relies on.

An L2 artifact that names neither is unplaceable: a reader cannot tell what it is exact
about.

## Two limits that define this layer

- Formal consistency under one interpretation does not choose that interpretation. A
  derivation that goes through under interpretation A tells you how A behaves formally. It
  is not a reason to prefer A over a live alternative B, and it does not retire B.
- L2 cannot adjudicate L0 semantics. Where a named interpretation is unresolved, L2 records
  the dependency as an open obligation and stops. Deriving with a meaning does not settle
  the meaning.

## Children

- `formal-mathematics/` - the exact artifacts themselves: objects, notation, domains,
  codomains, operators, axioms, derivations, proofs, counterexamples, and the open
  obligations register.

## Manual work

1. Name the selected L0 interpretation and the L1 declaration before writing any mathematics.
2. Check that the named L1 declaration actually admits the objects you are about to use; if it does not, the fix is a new or extended L1 declaration, not a widening assumed here.
3. State the artifact exactly, with explicit domains and codomains for every operator.
4. Record every open obligation as open, in the register, at the moment you notice it.
5. Treat any new object assembled from existing valid pieces as unverified until its compatibility has been shown and written down.
6. Keep counterexamples and failed derivations; a counterexample is an L2 result, not an embarrassment to be deleted.
7. Route anything whose owner or layer is not yet adjudicated back through L7 ingress instead of settling it here by default.

## Boundary

- No finite-precision results, no measurement, no units-with-uncertainty. Those are L3, and importing one here destroys the exactness that makes L2 useful.
- L2 may not repair an unresolved L1 declaration or an unresolved L0 meaning; it names the dependency and leaves the repair to the owning layer.
- A composition-specific or application-specific choice made at L4 or in an L7 composition is not universal supersession of an L2 artifact.
- Internal consistency, repository custody, an exact hash, or clean provenance does not establish scientific validity.

Record reusable process problems found while doing L2 work in /L7/process-lessons.md.
