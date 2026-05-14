# Sidecar Architecture

ASP can be deployed as a sidecar between agents.
The sidecar intercepts agent messages, computes ASP signals, applies routing policy, emits telemetry, and controls whether the message may continue downstream.

## 1. Simple Pipeline

```text
Question
  |
  v
Retrieval Agent
  |
  v
Agent A
  |
  v
ASP Sidecar
  |
  +--> pass to Agent B
  +--> regenerate through Agent A
  +--> block output
  +--> escalate to human review
```

## 2. Multi-Agent Architecture

```text
Agent 1 --> ASP Sidecar --> Agent 2 --> ASP Sidecar --> Agent 3
                    |                         |
                    v                         v
              Telemetry Log             Telemetry Log
```

## 3. Why Sidecar Deployment?

Sidecar deployment allows ASP to operate without modifying the agent internals.

Benefits:

- model-agnostic operation,
- clear enforcement point,
- centralized telemetry,
- independent protocol evolution,
- compatibility with multiple agent frameworks.

## 4. Governance Role

The sidecar acts as a quality gate.

It can:

- prevent ungrounded content propagation,
- distinguish repairable failures from containment failures,
- preserve audit logs,
- enforce retry budgets,
- support human escalation.# Sidecar Architecture

ASP can be deployed as a sidecar between agents.
The sidecar intercepts agent messages, computes ASP signals, applies routing policy, emits telemetry, and controls whether the message may continue downstream.

## 1. Simple Pipeline

```text
Question
	|
	v
Retrieval Agent
	|
	v
Agent A
	|
	v
ASP Sidecar
	|
	+--> pass to Agent B
	+--> regenerate through Agent A
	+--> block output
	+--> escalate to human review
```

## 2. Multi-Agent Architecture

```text
Agent 1 --> ASP Sidecar --> Agent 2 --> ASP Sidecar --> Agent 3
										|                         |
										v                         v
							Telemetry Log             Telemetry Log
```

## 3. Why Sidecar Deployment?

Sidecar deployment allows ASP to operate without modifying the agent internals.

Benefits:

- model-agnostic operation,
- clear enforcement point,
- centralized telemetry,
- independent protocol evolution,
- compatibility with multiple agent frameworks.

## 4. Governance Role

The sidecar acts as a quality gate.

It can:

- prevent ungrounded content propagation,
- distinguish repairable failures from containment failures,
- preserve audit logs,
- enforce retry budgets,
- support human escalation.
