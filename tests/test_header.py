from asp.header import ASPHeader, hex_to_score, parse_asp_header, score_to_hex


def test_parse_header_with_all_assumption_tags() -> None:
    header = parse_asp_header("[@C:D; @G:F; @S:2; A:[K:42, L:09, P:13, H:17]]")

    assert header == ASPHeader(
        certainty="D",
        grounding="F",
        stochasticity="2",
        assumptions={"K": ["42"], "L": ["09"], "P": ["13"], "H": ["17"]},
    )


def test_parse_header_handles_empty_assumptions() -> None:
    header = parse_asp_header("[@C:8; @G:A; @S:4; A:[]]")

    assert header.assumptions == {"K": [], "L": [], "P": [], "H": []}


def test_round_trip_header_serialization() -> None:
    header = ASPHeader(
        certainty="a",
        grounding="f",
        stochasticity="2",
        assumptions={"K": ["42"], "L": ["09"], "P": [], "H": []},
    )

    assert parse_asp_header(header.to_string()) == ASPHeader(
        certainty="A",
        grounding="F",
        stochasticity="2",
        assumptions={"K": ["42"], "L": ["09"], "P": [], "H": []},
    )


def test_parse_header_rejects_invalid_tag() -> None:
    try:
        parse_asp_header("[@C:D; @G:F; @S:2; A:[Z:99]]")
    except ValueError as exc:
        assert "Invalid assumption tag" in str(exc)
    else:
        raise AssertionError("Expected ValueError for invalid assumption tag")


def test_hex_score_helpers_are_inverse_at_simple_points() -> None:
    assert score_to_hex(0.0) == "0"
    assert score_to_hex(1.0) == "F"
    assert hex_to_score("8") == 8 / 15