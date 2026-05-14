from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from .sidecar import AgentMessage, inspect_message
from .telemetry import create_telemetry_event


def _read_json_input(input_path: str) -> dict[str, Any]:
    if input_path == "-":
        return json.load(sys.stdin)
    return json.loads(Path(input_path).read_text())


def _build_agent_message(payload: dict[str, Any]) -> AgentMessage:
    return AgentMessage(
        answer=payload["answer"],
        question=payload["question"],
        context=payload["context"],
        cited_chunks=set(payload.get("cited_chunks", [])),
        retrieved_chunks=set(payload.get("retrieved_chunks", [])),
    )


def _inspect_command(args: argparse.Namespace) -> int:
    payload = _read_json_input(args.input)
    attempt = args.attempt if args.attempt is not None else payload.get("attempt", 0)
    result = inspect_message(_build_agent_message(payload), attempt=attempt)

    output: dict[str, Any] = {
        "asp_header": result.header.to_string(),
        "signals": {
            "certainty": result.signals.certainty,
            "grounding": result.signals.grounding,
            "stochasticity": result.signals.stochasticity,
            "drift": result.signals.drift,
        },
        "routing": {
            "decision": result.decision.route.value,
            "reason": result.decision.reason,
        },
    }

    if args.telemetry:
        flow_id = args.flow_id or payload.get("flow_id", "flow_local")
        agent_id = args.agent_id or payload.get("agent_id", "agent_local")
        event = create_telemetry_event(
            event_id=args.event_id,
            flow_id=flow_id,
            agent_id=agent_id,
            attempt=attempt,
            asp_header=result.header.to_string(),
            signals=result.signals,
            decision=result.decision,
        )
        output["telemetry"] = json.loads(event.to_json())

    print(json.dumps(output, indent=2 if args.pretty else None, sort_keys=True))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="asp", description="Argent Signaling Protocol reference CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    inspect_parser = subparsers.add_parser(
        "inspect",
        help="Inspect an agent message JSON payload and emit ASP routing output",
    )
    inspect_parser.add_argument("input", help="Path to a JSON message file or '-' for stdin")
    inspect_parser.add_argument("--attempt", type=int, help="Override the attempt count")
    inspect_parser.add_argument("--telemetry", action="store_true", help="Emit a telemetry event in the output")
    inspect_parser.add_argument("--event-id", default="evt_local", help="Telemetry event identifier")
    inspect_parser.add_argument("--flow-id", help="Override the flow identifier")
    inspect_parser.add_argument("--agent-id", help="Override the agent identifier")
    inspect_parser.add_argument("--pretty", action="store_true", help="Pretty-print the JSON response")
    inspect_parser.set_defaults(handler=_inspect_command)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())