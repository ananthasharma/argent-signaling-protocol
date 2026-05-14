from asp.header import parse_asp_header
from asp.signals import RawFeatures, compute_raw_features, compute_signals


def test_compute_raw_features_uses_overlap_and_citations() -> None:
    features = compute_raw_features(
        answer="Change in Control includes merger and sale of assets",
        question="What is Change in Control?",
        context="Change in Control includes merger, consolidation, and sale of substantially all assets.",
        cited_chunks={"chunk_9"},
        retrieved_chunks={"chunk_9", "chunk_10"},
    )

    assert features.context_overlap > 0.5
    assert features.citation_score == 1.0
    assert features.novel_ratio < 0.5
    assert features.question_overlap > 0.0


def test_compute_signals_matches_documented_formula() -> None:
    features = RawFeatures(
        context_overlap=0.75,
        citation_score=1.0,
        novel_ratio=0.10,
        question_overlap=0.20,
    )

    signals = compute_signals(features)

    assert round(signals.grounding, 2) == 0.85
    assert round(signals.stochasticity, 2) == 0.07
    assert round(signals.certainty, 4) == 0.7905


def test_signal_header_quantization_produces_expected_hex_digits() -> None:
    features = RawFeatures(
        context_overlap=0.75,
        citation_score=1.0,
        novel_ratio=0.10,
        question_overlap=0.20,
    )

    header = compute_signals(features).to_header({"K": ["12"], "L": ["07"]})

    parsed = parse_asp_header(header.to_string())
    assert parsed.certainty == "C"
    assert parsed.grounding == "D"
    assert parsed.stochasticity == "1"