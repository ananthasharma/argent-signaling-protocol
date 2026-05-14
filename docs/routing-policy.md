# Routing Policy

ASP supports deterministic routing based on grounding, stochasticity, drift, and retry budget.

## 1. Example Routing Actions

| Action | Meaning |
| --- | --- |
| `EXECUTE` | Accept and pass downstream |
| `WARN` | Pass with warning or request review |
| `REGENERATE` | Retry with targeted repair prompt |
| `YIELD` | Stop automated repair |
| `BLOCK` | Prevent downstream propagation |
| `ESCALATE` | Send to human review |

## 2. Example Routing Policy

```text
Execute:
  if E < Emax
  and drift <= tau_warn
  and grounding >= g_min
  and stochasticity <= s_max

Warn:
  if E < Emax
  and tau_warn < drift <= tau_crit

Regenerate:
  if E < Emax
  and (
    drift > tau_crit
    or grounding < g_min
    or stochasticity > s_max
  )

Yield:
  if E >= Emax
```

## 3. Failure Classes

| Failure class | Description | Typical action |
| --- | --- | --- |
| Pass | Grounded and sufficient | Execute |
| Grounded partial | Correct material but incomplete | Regenerate |
| Citation gap | Good overlap but weak citation | Regenerate |
| Ungrounded | Insufficient evidence | Block or escalate |

## 4. Policy Notes

A deployment may use stricter thresholds for regulated environments.

For example:

- legal QA may require high citation precision,
- medical QA may require human review on any low-grounding output,
- financial decisioning may require both evidence grounding and model-risk telemetry.

ASP does not mandate one universal policy. It provides the signals required to make policy enforceable and auditable.# Routing Policy

ASP supports deterministic routing based on grounding, stochasticity, drift, and retry budget.

## 1. Example Routing Actions

| Action | Meaning |
| --- | --- |
| `EXECUTE` | Accept and pass downstream |
| `WARN` | Pass with warning or request review |
| `REGENERATE` | Retry with targeted repair prompt |
| `YIELD` | Stop automated repair |
| `BLOCK` | Prevent downstream propagation |
| `ESCALATE` | Send to human review |

## 2. Example Routing Policy

```text
Execute:
	if E < Emax
	and drift <= tau_warn
	and grounding >= g_min
	and stochasticity <= s_max

Warn:
	if E < Emax
	and tau_warn < drift <= tau_crit

Regenerate:
	if E < Emax
	and (
		drift > tau_crit
		or grounding < g_min
		or stochasticity > s_max
	)

Yield:
	if E >= Emax
```

## 3. Failure Classes

| Failure class | Description | Typical action |
| --- | --- | --- |
| Pass | Grounded and sufficient | Execute |
| Grounded partial | Correct material but incomplete | Regenerate |
| Citation gap | Good overlap but weak citation | Regenerate |
| Ungrounded | Insufficient evidence | Block or escalate |

## 4. Policy Notes

A deployment may use stricter thresholds for regulated environments.

For example:

- legal QA may require high citation precision,
- medical QA may require human review on any low-grounding output,
- financial decisioning may require both evidence grounding and model-risk telemetry.

ASP does not mandate one universal policy. It provides the signals required to make policy enforceable and auditable.
