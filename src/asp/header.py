from dataclasses import dataclass
import re

HEX_DIGITS = "0123456789ABCDEF"
ASSUMPTION_TAGS = ("K", "L", "P", "H")
HEADER_PATTERN = re.compile(
    r"\[@C:([0-9A-Fa-f]);\s*@G:([0-9A-Fa-f]);\s*@S:([0-9A-Fa-f]);\s*A:\[(.*?)\]\]"
)


@dataclass(frozen=True)
class ASPHeader:
    certainty: str
    grounding: str
    stochasticity: str
    assumptions: dict[str, list[str]]

    def to_string(self) -> str:
        parts: list[str] = []
        for tag in ASSUMPTION_TAGS:
            for value in self.assumptions.get(tag, []):
                parts.append(f"{tag}:{value}")
        assumption_text = ", ".join(parts)
        return (
            f"[@C:{validate_hex(self.certainty)}; @G:{validate_hex(self.grounding)}; "
            f"@S:{validate_hex(self.stochasticity)}; A:[{assumption_text}]]"
        )


def validate_hex(value: str) -> str:
    normalized = value.upper()
    if normalized not in HEX_DIGITS:
        raise ValueError(f"Invalid ASP hex digit: {value}")
    return normalized


def parse_asp_header(header: str) -> ASPHeader:
    match = HEADER_PATTERN.fullmatch(header.strip())
    if not match:
        raise ValueError(f"Invalid ASP header format: {header}")

    certainty, grounding, stochasticity, assumption_text = match.groups()
    assumptions: dict[str, list[str]] = {tag: [] for tag in ASSUMPTION_TAGS}

    if assumption_text.strip():
        for item in assumption_text.split(","):
            if ":" not in item:
                raise ValueError(f"Invalid assumption entry: {item.strip()}")
            tag, value = item.strip().split(":", 1)
            normalized_tag = tag.strip().upper()
            normalized_value = value.strip()
            if normalized_tag not in assumptions:
                raise ValueError(f"Invalid assumption tag: {normalized_tag}")
            if not normalized_value:
                raise ValueError("ASP assumption values must be non-empty")
            assumptions[normalized_tag].append(normalized_value)

    return ASPHeader(
        certainty=validate_hex(certainty),
        grounding=validate_hex(grounding),
        stochasticity=validate_hex(stochasticity),
        assumptions=assumptions,
    )


def score_to_hex(score: float) -> str:
    bounded = min(1.0, max(0.0, score))
    index = round(bounded * 15)
    return HEX_DIGITS[index]


def hex_to_score(value: str) -> float:
    return HEX_DIGITS.index(validate_hex(value)) / 15.0
