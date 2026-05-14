# Assumption Index

The ASP assumption index records the evidentiary basis of the claims contained in a model response.

It exists to answer a simple audit question: is this statement directly supported by source evidence, derived from that evidence, weakly inferred, or unsupported?

## Categories

| Tag | Name | Meaning | Typical handling |
| --- | --- | --- | --- |
| `K` | Known | Directly stated in retrieved or supplied evidence | Safe to preserve if other signals remain strong |
| `L` | Learned | Derived from evidence during processing | Usually acceptable with adequate grounding |
| `P` | Projected | Inferred from incomplete evidence | May require repair, warning, or verification |
| `H` | Hypothetical | Speculative or unsupported | Candidate for containment or escalation |

## Why It Matters

The same grounding score can hide materially different reasoning states.

- A mostly grounded answer with several `P` entries may still be repairable.
- A low-grounding answer dominated by `H` entries is a containment problem.
- A response composed mostly of `K` and `L` entries is easier to audit and defend.

The assumption index therefore complements the scalar signals rather than replacing them.

## Example

```text
[@C:A; @G:D; @S:3; A:[K:12, L:07, P:19]]
```

In this example, the response is mostly grounded but contains at least one projected inference. A controller may choose targeted regeneration rather than outright blocking.

## Operational Guidance

- Use stable identifiers for assumption entries when possible.
- Keep the tag set small enough to audit consistently.
- Record the estimator or workflow that generated the tags.
- Do not treat the assumption index as legal proof; it is operational metadata for governance and routing.# Assumption Index

The ASP assumption index records the evidentiary basis of the claims contained in a model response.

It exists to answer a simple audit question: is this statement directly supported by source evidence, derived from that evidence, weakly inferred, or unsupported?

## Categories

| Tag | Name | Meaning | Typical handling |
| --- | --- | --- | --- |
| `K` | Known | Directly stated in retrieved or supplied evidence | Safe to preserve if other signals remain strong |
| `L` | Learned | Derived from evidence during processing | Usually acceptable with adequate grounding |
| `P` | Projected | Inferred from incomplete evidence | May require repair, warning, or verification |
| `H` | Hypothetical | Speculative or unsupported | Candidate for containment or escalation |

## Why It Matters

The same grounding score can hide materially different reasoning states.

- A mostly grounded answer with several `P` entries may still be repairable.
- A low-grounding answer dominated by `H` entries is a containment problem.
- A response composed mostly of `K` and `L` entries is easier to audit and defend.

The assumption index therefore complements the scalar signals rather than replacing them.

## Example

```text
[@C:A; @G:D; @S:3; A:[K:12, L:07, P:19]]
```

In this example, the response is mostly grounded but contains at least one projected inference. A controller may choose targeted regeneration rather than outright blocking.

## Operational Guidance

- Use stable identifiers for assumption entries when possible.
- Keep the tag set small enough to audit consistently.
- Record the estimator or workflow that generated the tags.
- Do not treat the assumption index as legal proof; it is operational metadata for governance and routing.
