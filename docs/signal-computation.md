# Signal Computation

This document describes one transparent implementation of ASP signal computation for document-grounded QA.

The protocol does not require this estimator. ASP defines the message contract; implementations may use token overlap, NLI, retrieval traces, verifier models, sampling disagreement, or white-box model signals.

## 1. Raw Features

For a generated answer, define:

| Symbol | Meaning |
| --- | --- |
| `oc` | Context overlap: fraction of answer tokens appearing in retrieved context |
| `scite` | Citation score |
| `n` | Novel ratio: fraction of answer tokens absent from context and question |
| `oq` | Question overlap: fraction of answer tokens also appearing in the question |

## 2. Citation Score

A simple citation score can be defined as:

| Condition | Score |
| --- | --- |
| Valid retrieved citation | `1.0` |
| Citation present but not valid for retrieved set | `0.4` |
| No citation | `0.0` |

## 3. Signal Formulas

```text
@G = clamp(0.60 * oc + 0.40 * scite)
@S = clamp(0.70 * n + 0.30 * (1 - scite))
@C = @G * (1 - @S)
```

Where:

```text
clamp(x) = min(1, max(0, x))
```

## 4. Interpretation

### Grounding `@G`

High when the answer uses source language and cites the correct evidence.

### Stochasticity `@S`

High when the answer contains unsupported material or lacks valid citation.

### Certainty `@C`

High only when grounding is strong and stochasticity is low.

## 5. Quantization

Continuous values in `[0, 1]` can be quantized to hexadecimal digits:

```text
hex_value = round(score * 15)
```

Examples:

| Score | Hex |
| --- | --- |
| `0.00` | `0` |
| `0.50` | `8` |
| `0.87` | `D` |
| `1.00` | `F` |

## 6. Alternative Estimators

ASP can also support:

- NLI-based grounding,
- verbalized confidence,
- semantic entropy,
- sample disagreement,
- retrieval trace coverage,
- verifier-model scoring,
- logit-based uncertainty where available.

The implementation should record which estimator produced the signal values.# Signal Computation

This document describes one transparent implementation of ASP signal computation for document-grounded QA.

The protocol does not require this estimator. ASP defines the message contract; implementations may use token overlap, NLI, retrieval traces, verifier models, sampling disagreement, or white-box model signals.

## 1. Raw Features

For a generated answer, define:

| Symbol | Meaning |
| --- | --- |
| `oc` | Context overlap: fraction of answer tokens appearing in retrieved context |
| `scite` | Citation score |
| `n` | Novel ratio: fraction of answer tokens absent from context and question |
| `oq` | Question overlap: fraction of answer tokens also appearing in the question |

## 2. Citation Score

A simple citation score can be defined as:

| Condition | Score |
| --- | --- |
| Valid retrieved citation | `1.0` |
| Citation present but not valid for retrieved set | `0.4` |
| No citation | `0.0` |

## 3. Signal Formulas

```text
@G = clamp(0.60 * oc + 0.40 * scite)
@S = clamp(0.70 * n + 0.30 * (1 - scite))
@C = @G * (1 - @S)
```

Where:

```text
clamp(x) = min(1, max(0, x))
```

## 4. Interpretation

### Grounding `@G`

High when the answer uses source language and cites the correct evidence.

### Stochasticity `@S`

High when the answer contains unsupported material or lacks valid citation.

### Certainty `@C`

High only when grounding is strong and stochasticity is low.

## 5. Quantization

Continuous values in `[0, 1]` can be quantized to hexadecimal digits:

```text
hex_value = round(score * 15)
```

Examples:

| Score | Hex |
| --- | --- |
| `0.00` | `0` |
| `0.50` | `8` |
| `0.87` | `D` |
| `1.00` | `F` |

## 6. Alternative Estimators

ASP can also support:

- NLI-based grounding,
- verbalized confidence,
- semantic entropy,
- sample disagreement,
- retrieval trace coverage,
- verifier-model scoring,
- logit-based uncertainty where available.

The implementation should record which estimator produced the signal values.
