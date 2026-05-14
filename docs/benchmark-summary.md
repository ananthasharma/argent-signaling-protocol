# Benchmark Summary

This document summarizes the experimental results reported in:

**Trustworthy Multi-Agent Systems: Mitigating Semantic Drift with the Argent Signaling Protocol**  
Anantha Sharma, 2026

## 1. Standalone Controller Benchmark

The standalone benchmark evaluated ASP over a 27-question document-grounded QA task based on a pharmaceutical license agreement.

Three local models were evaluated:

- Qwen 0.8B
- Dobby 8B
- SmolLM3 3B

Aggregate passes improved from:

```text
12/81 baseline passes
to
21/81 ASP-controlled passes
```

The controller produced:

- 10 fail-to-pass recoveries,
- 1 regression,
- 58 repair interventions,
- 12 containment interventions,
- 11 clean pass-throughs.

## 2. Model-Specific Behavior

| Model | Observed ASP role |
| --- | --- |
| Qwen 0.8B | Repair layer |
| Dobby 8B | Repair layer |
| SmolLM3 3B | Mixed repair / containment triage |

ASP did not behave as a generic retry loop. It adapted to the failure regime of the governed model.

## 3. Multi-Agent Sidecar Benchmark

In the multi-agent benchmark, an ASP sidecar sat between:

- Agent A: retrieval QA agent,
- Agent B: downstream risk-assessment agent.

In the baseline condition, all upstream outputs reached Agent B.

In the ASP-gated condition:

```text
24/27 outputs were blocked
0 ungrounded outputs reached Agent B
```

This demonstrated containment of ungrounded upstream content before downstream propagation.

## 4. Interpretation

ASP changes how failure propagates.

It does not necessarily make weak models more capable. Instead, it helps controllers and downstream agents determine whether to:

- trust,
- repair,
- warn,
- block,
- escalate.

This is especially relevant for regulated AI systems where auditability and failure legibility are required.
# Benchmark Summary

This document summarizes the experimental results reported in:

**Trustworthy Multi-Agent Systems: Mitigating Semantic Drift with the Argent Signaling Protocol**  
Anantha Sharma, 2026

---

## 1. Standalone controller benchmark

The standalone benchmark evaluated ASP over a 27-question document-grounded QA task based on a pharmaceutical license agreement.

Three local models were evaluated:

- Qwen 0.8B
- Dobby 8B
- SmolLM3 3B

Aggregate passes improved from:

```text
12/81 baseline passes
to
21/81 ASP-controlled passes
```

The controller produced:

- 10 fail-to-pass recoveries,
- 1 regression,
- 58 repair interventions,
- 12 containment interventions,
- 11 clean pass-throughs.

## 2. Model-specific behavior

| Model | Observed ASP role |
| --- | --- |
| Qwen 0.8B | Repair layer |
| Dobby 8B | Repair layer |
| SmolLM3 3B | Mixed repair / containment triage |


ASP did not behave as a generic retry loop. It adapted to the failure regime of the governed model.


## 3. Multi-agent sidecar benchmark

In the multi-agent benchmark, an ASP sidecar sat between:

- Agent A: retrieval QA agent,
- Agent B: downstream risk-assessment agent.

In the baseline condition, all upstream outputs reached Agent B.

In the ASP-gated condition:

```text
24/27 outputs were blocked
0 ungrounded outputs reached Agent B
```

This demonstrated containment of ungrounded upstream content before downstream propagation.

## 4. Interpretation

ASP changes how failure propagates.

It does not necessarily make weak models more capable. Instead, it helps controllers and downstream agents determine whether to:

- trust,
- repair,
- warn,
- block,
- escalate.

This is especially relevant for regulated AI systems where auditability and failure legibility are required.