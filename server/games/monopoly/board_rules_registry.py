"""Capability registry for Monopoly board-specific rule packs."""

from __future__ import annotations

from dataclasses import dataclass

from .board_rules import (
    junior_super_mario,
    mario_celebration,
    mario_collectors,
    mario_kart,
    mario_movie,
)

@dataclass(frozen=True)
class BoardRulePack:
    """Declarative capabilities for one board rule-pack."""

    rule_pack_id: str
    status: str
    capability_ids: tuple[str, ...]


RULE_PACKS: dict[str, BoardRulePack] = {
    "mario_collectors": BoardRulePack(
        rule_pack_id="mario_collectors",
        status="partial",
        capability_ids=(
            "pass_go_credit_override",
            "startup_board_announcement",
        ),
    ),
    "mario_kart": BoardRulePack(
        rule_pack_id="mario_kart",
        status="partial",
        capability_ids=(
            "pass_go_credit_override",
            "startup_board_announcement",
        ),
    ),
    "mario_celebration": BoardRulePack(
        rule_pack_id="mario_celebration",
        status="partial",
        capability_ids=(
            "pass_go_credit_override",
            "startup_board_announcement",
        ),
    ),
    "mario_movie": BoardRulePack(
        rule_pack_id="mario_movie",
        status="partial",
        capability_ids=(
            "pass_go_credit_override",
            "startup_board_announcement",
        ),
    ),
    "junior_super_mario": BoardRulePack(
        rule_pack_id="junior_super_mario",
        status="partial",
        capability_ids=(
            "pass_go_credit_override",
            "startup_board_announcement",
        ),
    ),
}
RULE_PACK_MODULES = {
    "mario_collectors": mario_collectors,
    "mario_kart": mario_kart,
    "mario_celebration": mario_celebration,
    "mario_movie": mario_movie,
    "junior_super_mario": junior_super_mario,
}


def get_rule_pack(rule_pack_id: str) -> BoardRulePack | None:
    """Return one board rule-pack by id."""
    return RULE_PACKS.get(rule_pack_id)


def supports_capability(rule_pack_id: str, capability_id: str) -> bool:
    """Return True when a rule-pack advertises one capability id."""
    pack = get_rule_pack(rule_pack_id)
    return bool(pack and capability_id in pack.capability_ids)


def get_pass_go_credit_override(rule_pack_id: str) -> int | None:
    """Return pass-GO override for one rule-pack when declared."""
    module = RULE_PACK_MODULES.get(rule_pack_id)
    if module is None:
        return None
    value = getattr(module, "PASS_GO_CREDIT_OVERRIDE", None)
    if isinstance(value, int):
        return value
    return None
