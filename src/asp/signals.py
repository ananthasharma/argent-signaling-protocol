import re
from dataclasses import dataclass

from .header import ASPHeader, score_to_hex


@dataclass(frozen=True)
class RawFeatures:
    context_overlap: float
    citation_score: float
    novel_ratio: float
    question_overlap: float


@dataclass(frozen=True)
class ASPSignals:
    certainty: float
    grounding: float
    stochasticity: float
    drift: float | None = None

    def to_header(self, assumptions: dict[str, list[str]] | None = None) -> ASPHeader:
        return ASPHeader(
            certainty=score_to_hex(self.certainty),
            grounding=score_to_hex(self.grounding),
            stochasticity=score_to_hex(self.stochasticity),
            assumptions=assumptions or {},
        )


def clamp(value: float) -> float:
    return min(1.0, max(0.0, value))


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[A-Za-z0-9]+", text.lower()))


def compute_raw_features(
    answer: str,
    question: str,
    context: str,
    cited_chunks: set[str] | None = None,
    retrieved_chunks: set[str] | None = None,
) -> RawFeatures:
    answer_tokens = tokenize(answer)
    question_tokens = tokenize(question)
    context_tokens = tokenize(context)

    if not answer_tokens:
        return RawFeatures(0.0, 0.0, 1.0, 0.0)

    context_overlap = len(answer_tokens & context_tokens) / len(answer_tokens)
    question_overlap = len(answer_tokens & question_tokens) / len(answer_tokens)
    novel_tokens = answer_tokens - context_tokens - question_tokens
    novel_ratio = len(novel_tokens) / len(answer_tokens)
    citation_score = compute_citation_score(cited_chunks or set(), retrieved_chunks or set())

    return RawFeatures(
        context_overlap=context_overlap,
        citation_score=citation_score,
        novel_ratio=novel_ratio,
        question_overlap=question_overlap,
    )


def compute_citation_score(cited_chunks: set[str], retrieved_chunks: set[str]) -> float:
    if not cited_chunks:
        return 0.0
    if cited_chunks & retrieved_chunks:
        return 1.0
    return 0.4


def compute_signals(features: RawFeatures) -> ASPSignals:
    grounding = clamp(0.60 * features.context_overlap + 0.40 * features.citation_score)
    stochasticity = clamp(0.70 * features.novel_ratio + 0.30 * (1.0 - features.citation_score))
    certainty = grounding * (1.0 - stochasticity)
    return ASPSignals(
        certainty=certainty,
        grounding=grounding,
        stochasticity=stochasticity,
    )