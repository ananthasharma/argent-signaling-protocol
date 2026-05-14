# Argent Signaling Protocol Specification

## 1. Purpose

The Argent Signaling Protocol is a compact signaling layer for AI-generated messages in multi-agent systems.

Its purpose is to expose quality, provenance, and assumption signals at the message boundary so that downstream agents, controllers, and human supervisors can reason about whether a response should be accepted, repaired, contained, or escalated.

ASP is designed for environments where:

- agents exchange intermediate outputs,
- those outputs influence downstream decisions,
- failures must be auditable,
- unsupported content must not propagate silently.

## 2. Header Format

Each ASP-instrumented message carries a header:

```text
[@C:X; @G:Y; @S:Z; A:[K:id, L:id, P:id, H:id]]
```

Example:

```text
[@C:D; @G:F; @S:2; A:[K:42, L:09]]
```

The header is intended to travel with the natural-language payload.

## 3. Signal Fields

### `@C` - Certainty

Represents how confident the system is in the answer, based on grounded evidence and signal stability.

High certainty should not be interpreted as an internal posterior probability. It is an auditable proxy.

### `@G` - Grounding

Represents how strongly the answer is anchored in retrieved or supplied evidence.

High grounding means the answer can be traced to source material.

### `@S` - Stochasticity

Represents unsupported, unstable, or novel content not grounded in evidence.

High stochasticity indicates a greater risk of unsupported generation.

## 4. Hexadecimal Scale

Signals are serialized as hexadecimal digits:

```text
0 1 2 3 4 5 6 7 8 9 A B C D E F
```

Where:

- `0` indicates the lowest level,
- `F` indicates the highest level.

Internally, implementations may compute continuous values in `[0, 1]` and quantize them into hexadecimal form.

## 5. Assumption Index

The assumption index records the evidentiary status of claims.

| Tag | Category | Meaning |
| --- | --- | --- |
| `K` | Known | Directly stated in retrieved or source evidence |
| `L` | Learned | Derived from evidence during processing |
| `P` | Projected | Inferred from partial evidence |
| `H` | Hypothetical | Unsupported or speculative |

Example:

```text
A:[K:42, L:09, P:13]
```

## 6. Routing Intent

The ASP header is not merely descriptive. It is intended to support routing decisions such as:

- execute,
- warn,
- regenerate,
- yield,
- block,
- escalate.

The exact policy may differ by deployment, but the routing decision should be reproducible from the signal values, thresholds, and telemetry log.

## 7. Design Principles

ASP prioritizes:

- compactness,
- auditability,
- model-agnostic operation,
- deterministic routing,
- sidecar deployment,
- transparent telemetry.

The protocol is intentionally lightweight. It is not a replacement for human review, formal verification, or domain-specific validation.# Argent Signaling Protocol Specification

## 1. Purpose

The Argent Signaling Protocol is a compact signaling layer for AI-generated messages in multi-agent systems.

Its purpose is to expose quality, provenance, and assumption signals at the message boundary so that downstream agents, controllers, and human supervisors can reason about whether a response should be accepted, repaired, contained, or escalated.

ASP is designed for environments where:

- agents exchange intermediate outputs,
- those outputs influence downstream decisions,
- failures must be auditable,
- unsupported content must not propagate silently.

## 2. Header Format

Each ASP-instrumented message carries a header:

```text
[@C:X; @G:Y; @S:Z; A:[K:id, L:id, P:id, H:id]]
```

Example:

```text
[@C:D; @G:F; @S:2; A:[K:42, L:09]]
```

The header is intended to travel with the natural-language payload.

## 3. Signal Fields

### `@C` - Certainty

Represents how confident the system is in the answer, based on grounded evidence and signal stability.

High certainty should not be interpreted as an internal posterior probability. It is an auditable proxy.

### `@G` - Grounding

Represents how strongly the answer is anchored in retrieved or supplied evidence.

High grounding means the answer can be traced to source material.

### `@S` - Stochasticity

Represents unsupported, unstable, or novel content not grounded in evidence.

High stochasticity indicates a greater risk of unsupported generation.

## 4. Hexadecimal Scale

Signals are serialized as hexadecimal digits:

```text
0 1 2 3 4 5 6 7 8 9 A B C D E F
```

Where:

- `0` indicates the lowest level,
- `F` indicates the highest level.

Internally, implementations may compute continuous values in `[0, 1]` and quantize them into hexadecimal form.

## 5. Assumption Index

The assumption index records the evidentiary status of claims.

| Tag | Category | Meaning |
| --- | --- | --- |
| `K` | Known | Directly stated in retrieved or source evidence |
| `L` | Learned | Derived from evidence during processing |
| `P` | Projected | Inferred from partial evidence |
| `H` | Hypothetical | Unsupported or speculative |

Example:

```text
A:[K:42, L:09, P:13]
```

## 6. Routing Intent

The ASP header is not merely descriptive. It is intended to support routing decisions such as:

- execute,
- warn,
- regenerate,
- yield,
- block,
- escalate.

The exact policy may differ by deployment, but the routing decision should be reproducible from the signal values, thresholds, and telemetry log.

## 7. Design Principles

ASP prioritizes:

- compactness,
- auditability,
- model-agnostic operation,
- deterministic routing,
- sidecar deployment,
- transparent telemetry.

The protocol is intentionally lightweight. It is not a replacement for human review, formal verification, or domain-specific validation.
