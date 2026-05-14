# Argent Signaling Protocol

![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-2F6690)
![License: MIT](https://img.shields.io/badge/license-MIT-52796F.svg)
![Status: alpha](https://img.shields.io/badge/status-alpha-B56576)

**Argent Signaling Protocol (ASP)** is a lightweight, auditable signaling protocol for trustworthy multi-agent AI systems.

ASP attaches compact machine-readable quality signals to AI-generated responses so that controllers, sidecars, downstream agents, and human reviewers can distinguish:

- grounded but incomplete answers that may be repairable,
- citation or attribution gaps that may require regeneration,
- ungrounded outputs that should be contained before they propagate downstream.

The protocol is designed for multi-agent systems where intermediate outputs become operational state. In such systems, a downstream agent may treat an upstream answer as settled fact even when that answer is only partially supported or has drifted away from source evidence.

ASP makes that failure state visible.

## Why It Matters

In document-grounded and regulated AI systems, not all bad answers are equal.

A response may cite the correct material but miss required terms. That is often repairable.

Another response may produce fluent but unsupported prose with no grounding in the retrieved source. That is not a repair problem; it is a containment problem.

Most retry strategies treat both cases similarly: retry and hope. ASP provides structured signals that allow a controller to route failures differently.

## Protocol Overview

Every ASP-instrumented response carries a compact header:

```text
[@C:X; @G:Y; @S:Z; A:[K:id, L:id, P:id, H:id]]
```

| Field | Meaning |
| --- | --- |
| `@C` | Certainty signal |
| `@G` | Grounding signal |
| `@S` | Stochasticity / unsupported-generation signal |
| `A:[...]` | Assumption index |

The signal fields use hexadecimal digits from `0` to `F`, representing a compact 16-point quality scale.

Example of a grounded response:

```text
[@C:D; @G:F; @S:2; A:[K:42, L:09]]
```

Example of an ungrounded response:

```text
[@C:3; @G:1; @S:C; A:[H:17]]
```

### Assumption Index

The assumption index classifies the evidentiary basis of claims.

| Tag | Category | Meaning |
| --- | --- | --- |
| `K` | Known | Directly stated in the source document |
| `L` | Learned | Derived during processing from retrieved evidence |
| `P` | Projected | Inferred from partial evidence |
| `H` | Hypothetical | Speculative or unsupported |

This gives downstream systems and auditors a structured way to understand whether a response is grounded in evidence or drifting into unsupported inference.

## Reference Architecture

ASP is intended to operate as a sidecar or interception layer between agents.

```text
Agent A
	|
	v
ASP Sidecar
	|
	+--> pass grounded output downstream
	+--> repair grounded partial output
	+--> block ungrounded output
	+--> escalate unresolved cases to human review
	|
	v
Agent B
```

The sidecar computes ASP signals, applies routing policy, emits telemetry, and prevents ungrounded outputs from silently becoming downstream context.

## Routing Behavior

ASP supports deterministic routing decisions such as:

| Condition | Failure class | Controller action |
| --- | --- | --- |
| Strong citation and sufficient term coverage | Pass | Execute |
| Correct grounding but incomplete coverage | Grounded partial | Repair |
| Good overlap but weak or missing citation | Citation gap | Repair |
| Weak grounding and high stochasticity | Ungrounded | Contain or escalate |

The goal is not merely to retry more intelligently. The goal is to make the system's failure state legible.

## Research Background

This repository accompanies the research work:

*Trustworthy Multi-Agent Systems: Mitigating Semantic Drift with the Argent Signaling Protocol*  
Anantha Sharma, 2026

The paper evaluates ASP in two modes:

1. Standalone controller mode over a 27-question document-grounded QA benchmark.
2. Multi-agent sidecar mode between an upstream retrieval agent and a downstream decision agent.

In the standalone benchmark, ASP improved aggregate passes from 12/81 to 21/81. In the multi-agent sidecar benchmark, ASP blocked 100% of ungrounded upstream outputs from reaching the downstream decision agent.

## Diagrams

- [diagrams/asp-sidecar-architecture.md](diagrams/asp-sidecar-architecture.png)
- [diagrams/asp-routing-flow.md](diagrams/asp-routing-flow.png)

## Repository Contents

- `docs/`: Protocol specification, sidecar architecture, routing policy, telemetry schema, and benchmark summary.
- `diagrams/`: Mermaid diagrams for sidecar deployment and routing behavior.
- `examples/`: ASP headers, sample agent messages, telemetry logs, and routing decisions.
- `src/asp/`: Minimal reference implementation for parsing headers, computing signals, routing outputs, and recording telemetry.
- `tests/`: Unit tests for protocol parsing, signal computation, routing behavior, and the CLI.

## Quick Start

```bash
python -m pytest
```

Inspect the sample agent message with the CLI:

```bash
python -m asp.cli inspect examples/sample_agent_message.json --telemetry --pretty
```

If the package is installed in editable or standard mode, the console entry point is also available:

```bash
asp inspect examples/sample_agent_message.json --telemetry
```

The reference implementation is intentionally small. It is meant to document the contract and provide a transparent baseline that can be adapted to richer grounding estimators, verifier models, or production sidecars.

## Current Status

This repository is an early reference implementation and documentation companion for the Argent Signaling Protocol.

The current implementation focuses on:

- protocol header parsing,
- transparent signal computation,
- deterministic routing policy,
- sidecar-style gating,
- telemetry examples.

Future work may include:

- NLI-based grounding estimation,
- semantic entropy-based stochasticity estimation,
- assumption lifecycle tracking,
- multi-turn drift monitoring,
- integration with agent frameworks,
- benchmark reproduction scripts.

## Citation

If you use this work, please cite:

```bibtex
@misc{sharma2026argent,
	title={Trustworthy Multi-Agent Systems: Mitigating Semantic Drift with the Argent Signaling Protocol},
	author={Sharma, Anantha},
	year={2026},
	note={Accepted for presentation at AISB XTAI 2026}
}
```

## Author

Anantha Sharma  
AI Strategy, Enterprise Architecture, and Applied Research  
ORCID: https://orcid.org/0000-0002-9064-3362  
LinkedIn: https://www.linkedin.com/in/anantha-sharma