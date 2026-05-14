import json

from asp.cli import main


def test_cli_inspect_emits_header_route_and_telemetry(tmp_path, capsys) -> None:
    payload = {
        "flow_id": "flow_123",
        "agent_id": "retrieval_agent_a",
        "attempt": 1,
        "question": "What events qualify as a Change in Control under the agreement?",
        "context": "Section 1.6 defines Change in Control to include merger, consolidation, sale of substantially all assets, and acquisition of voting control.",
        "answer": "Change in Control includes merger, consolidation, sale of substantially all assets, and acquisition of voting control.",
        "retrieved_chunks": ["chunk_9", "chunk_10"],
        "cited_chunks": ["chunk_9"],
    }
    input_path = tmp_path / "message.json"
    input_path.write_text(json.dumps(payload))

    exit_code = main(["inspect", str(input_path), "--telemetry", "--pretty"])

    captured = capsys.readouterr()
    data = json.loads(captured.out)

    assert exit_code == 0
    assert data["asp_header"].startswith("[@C:")
    assert data["routing"]["decision"] == "EXECUTE"
    assert data["telemetry"]["flow_id"] == "flow_123"