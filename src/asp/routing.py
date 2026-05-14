from dataclasses import dataclass
from enum import Enum

from .signals import ASPSignals


class Route(str, Enum):
    EXECUTE = "EXECUTE"
    WARN = "WARN"
    REGENERATE = "REGENERATE"
    YIELD = "YIELD"
    BLOCK = "BLOCK"
    ESCALATE = "ESCALATE"


@dataclass(frozen=True)
class RoutingPolicy:
    tau_warn: float = 0.12
    tau_crit: float = 0.22
    g_min: float = 0.33
    s_max: float = 0.67
    e_max: int = 2


@dataclass(frozen=True)
class RoutingDecision:
    route: Route
    reason: str


def route_response(
    signals: ASPSignals,
    attempt: int,
    policy: RoutingPolicy | None = None,
) -> RoutingDecision:
    policy = policy or RoutingPolicy()
    drift = signals.drift if signals.drift is not None else 0.0

    if attempt >= policy.e_max:
        return RoutingDecision(Route.YIELD, "retry_budget_exhausted")

    if (
        drift <= policy.tau_warn
        and signals.grounding >= policy.g_min
        and signals.stochasticity <= policy.s_max
    ):
        return RoutingDecision(Route.EXECUTE, "grounded_low_stochasticity")

    if policy.tau_warn < drift <= policy.tau_crit:
        return RoutingDecision(Route.WARN, "moderate_drift")

    if (
        drift > policy.tau_crit
        or signals.grounding < policy.g_min
        or signals.stochasticity > policy.s_max
    ):
        if signals.grounding < policy.g_min and signals.stochasticity > policy.s_max:
            return RoutingDecision(Route.BLOCK, "ungrounded_high_stochasticity")
        return RoutingDecision(Route.REGENERATE, "repairable_signal_failure")

    return RoutingDecision(Route.ESCALATE, "unclassified_state")