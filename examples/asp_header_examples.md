# ASP Header Examples

## 1. Strongly Grounded Response

```text
[@C:E; @G:F; @S:1; A:[K:12, L:07]]
```

Interpretation:

- high certainty,
- maximal grounding,
- low unsupported generation,
- based on known and learned evidence.

Likely route: `EXECUTE`

## 2. Grounded but Incomplete Response

```text
[@C:A; @G:D; @S:2; A:[K:12, L:09]]
```

Interpretation:

- grounded in source material,
- low stochasticity,
- may be incomplete.

Likely route: `REGENERATE`

## 3. Citation Gap

```text
[@C:8; @G:A; @S:4; A:[L:21, P:03]]
```

Interpretation:

- some grounding,
- citation may be absent or imprecise,
- answer may be repairable.

Likely route: `REGENERATE`

## 4. Ungrounded Output

```text
[@C:3; @G:1; @S:C; A:[H:17]]
```

Interpretation:

- low certainty,
- weak grounding,
- high unsupported generation,
- speculative assumption.

Likely route: `BLOCK` or `ESCALATE`# ASP Header Examples

## 1. Strongly Grounded Response

```text
[@C:E; @G:F; @S:1; A:[K:12, L:07]]
```

Interpretation:

- high certainty,
- maximal grounding,
- low unsupported generation,
- based on known and learned evidence.

Likely route: `EXECUTE`

## 2. Grounded but Incomplete Response

```text
[@C:A; @G:D; @S:2; A:[K:12, L:09]]
```

Interpretation:

- grounded in source material,
- low stochasticity,
- may be incomplete.

Likely route: `REGENERATE`

## 3. Citation Gap

```text
[@C:8; @G:A; @S:4; A:[L:21, P:03]]
```

Interpretation:

- some grounding,
- citation may be absent or imprecise,
- answer may be repairable.

Likely route: `REGENERATE`

## 4. Ungrounded Output

```text
[@C:3; @G:1; @S:C; A:[H:17]]
```

Interpretation:

- low certainty,
- weak grounding,
- high unsupported generation,
- speculative assumption.

Likely route: `BLOCK` or `ESCALATE`
