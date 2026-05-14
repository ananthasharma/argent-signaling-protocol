from asp.routing import Route, route_response
from asp.signals import ASPSignals


def test_route_execute_for_grounded_low_stochasticity() -> None:
    decision = route_response(
        ASPSignals(certainty=0.86, grounding=0.90, stochasticity=0.10, drift=0.05),
        attempt=0,
    )

    assert decision.route is Route.EXECUTE


def test_route_warn_for_moderate_drift() -> None:
    decision = route_response(
        ASPSignals(certainty=0.52, grounding=0.70, stochasticity=0.20, drift=0.18),
        attempt=0,
    )

    assert decision.route is Route.WARN
    assert decision.reason == "moderate_drift"


def test_route_block_for_ungrounded_high_stochasticity() -> None:
    decision = route_response(
        ASPSignals(certainty=0.10, grounding=0.10, stochasticity=0.90, drift=0.30),
        attempt=0,
    )

    assert decision.route is Route.BLOCK
    assert decision.reason == "ungrounded_high_stochasticity"


def test_route_yield_when_retry_budget_exhausted() -> None:
    decision = route_response(
        ASPSignals(certainty=0.40, grounding=0.50, stochasticity=0.40, drift=0.15),
        attempt=2,
    )

    assert decision.route is Route.YIELD