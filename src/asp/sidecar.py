from dataclasses import dataclass

from .header import ASPHeader
from .routing import RoutingDecision, route_response
from .signals import ASPSignals, compute_raw_features, compute_signals


@dataclass(frozen=True)
class AgentMessage:
    answer: str
    question: str
    context: str
    cited_chunks: set[str]
    retrieved_chunks: set[str]


@dataclass(frozen=True)
class SidecarResult:
    header: ASPHeader
    signals: ASPSignals
    decision: RoutingDecision


def inspect_message(message: AgentMessage, attempt: int = 0) -> SidecarResult:
    features = compute_raw_features(
        answer=message.answer,
        question=message.question,
        context=message.context,
        cited_chunks=message.cited_chunks,
        retrieved_chunks=message.retrieved_chunks,
    )
    signals = compute_signals(features)
    header = signals.to_header(assumptions={})
    decision = route_response(signals, attempt=attempt)
    return SidecarResult(header=header, signals=signals, decision=decision)