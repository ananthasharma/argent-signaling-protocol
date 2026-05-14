from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json

from .routing import RoutingDecision
from .signals import ASPSignals


@dataclass(frozen=True)
class TelemetryEvent:
    event_id: str
    flow_id: str
    agent_id: str
    attempt: int
    asp_header: str
    signals: dict
    routing: dict
    timestamp: str

    def to_json(self) -> str:
        return json.dumps(asdict(self), sort_keys=True)


def create_telemetry_event(
    event_id: str,
    flow_id: str,
    agent_id: str,
    attempt: int,
    asp_header: str,
    signals: ASPSignals,
    decision: RoutingDecision,
) -> TelemetryEvent:
    return TelemetryEvent(
        event_id=event_id,
        flow_id=flow_id,
        agent_id=agent_id,
        attempt=attempt,
        asp_header=asp_header,
        signals={
            "certainty": signals.certainty,
            "grounding": signals.grounding,
            "stochasticity": signals.stochasticity,
            "drift": signals.drift,
        },
        routing={
            "decision": decision.route.value,
            "reason": decision.reason,
        },
        timestamp=datetime.now(timezone.utc).isoformat(),
    )