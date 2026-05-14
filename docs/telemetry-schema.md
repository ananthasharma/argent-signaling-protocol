# Telemetry Schema

ASP telemetry records every routing decision and the signal values that caused it.

## 1. Example Telemetry Event

```json
{
  "event_id": "evt_000001",
  "timestamp": "2026-04-16T12:00:00Z",
  "flow_id": "flow_123",
  "agent_id": "agent_a",
  "attempt": 1,
  "asp_header": "[@C:D; @G:F; @S:2; A:[K:42, L:09]]",
  "signals": {
    "certainty": 0.86,
    "grounding": 1.0,
    "stochasticity": 0.13,
    "drift": 0.11
  },
  "routing": {
    "decision": "EXECUTE",
    "reason": "grounded_low_stochasticity"
  },
  "evidence": {
    "retrieved_chunks": ["chunk_9", "chunk_10"],
    "cited_chunks": ["chunk_9"]
  }
}
```

## 2. Required Fields

| Field | Purpose |
| --- | --- |
| `event_id` | Unique telemetry event identifier |
| `flow_id` | Multi-agent workflow identifier |
| `agent_id` | Agent that produced the response |
| `attempt` | Attempt count |
| `asp_header` | Serialized ASP header |
| `signals` | Raw signal values |
| `routing.decision` | Controller action |
| `routing.reason` | Human-readable reason |

## 3. Optional Fields

| Field | Purpose |
| --- | --- |
| `retrieved_chunks` | Evidence made available to the agent |
| `cited_chunks` | Evidence cited in the answer |
| `failure_class` | Pass, grounded partial, citation gap, ungrounded |
| `human_review_status` | Review state |
| `model_id` | Model that produced output |
| `estimator_id` | Signal estimator used |

## 4. Audit Objective

A reviewer should be able to reconstruct:

- what the agent generated,
- what evidence was available,
- how signals were computed,
- why the route was chosen,
- whether the message propagated downstream.# Telemetry Schema

ASP telemetry records every routing decision and the signal values that caused it.

## 1. Example Telemetry Event

```json
{
	"event_id": "evt_000001",
	"timestamp": "2026-04-16T12:00:00Z",
	"flow_id": "flow_123",
	"agent_id": "agent_a",
	"attempt": 1,
	"asp_header": "[@C:D; @G:F; @S:2; A:[K:42, L:09]]",
	"signals": {
		"certainty": 0.86,
		"grounding": 1.0,
		"stochasticity": 0.13,
		"drift": 0.11
	},
	"routing": {
		"decision": "EXECUTE",
		"reason": "grounded_low_stochasticity"
	},
	"evidence": {
		"retrieved_chunks": ["chunk_9", "chunk_10"],
		"cited_chunks": ["chunk_9"]
	}
}
```

## 2. Required Fields

| Field | Purpose |
| --- | --- |
| `event_id` | Unique telemetry event identifier |
| `flow_id` | Multi-agent workflow identifier |
| `agent_id` | Agent that produced the response |
| `attempt` | Attempt count |
| `asp_header` | Serialized ASP header |
| `signals` | Raw signal values |
| `routing.decision` | Controller action |
| `routing.reason` | Human-readable reason |

## 3. Optional Fields

| Field | Purpose |
| --- | --- |
| `retrieved_chunks` | Evidence made available to the agent |
| `cited_chunks` | Evidence cited in the answer |
| `failure_class` | Pass, grounded partial, citation gap, ungrounded |
| `human_review_status` | Review state |
| `model_id` | Model that produced output |
| `estimator_id` | Signal estimator used |

## 4. Audit Objective

A reviewer should be able to reconstruct:

- what the agent generated,
- what evidence was available,
- how signals were computed,
- why the route was chosen,
- whether the message propagated downstream.
