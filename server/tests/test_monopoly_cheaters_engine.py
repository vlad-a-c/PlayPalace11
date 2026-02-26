"""Tests for deterministic Monopoly cheaters engine behavior."""

from server.games.monopoly.cheaters_engine import CheatersEngine
from server.games.monopoly.cheaters_profile import DEFAULT_CHEATERS_PROFILE


def test_engine_blocks_early_end_turn_with_penalty():
    engine = CheatersEngine(DEFAULT_CHEATERS_PROFILE)
    engine.on_turn_start("p1", turn_index=0)
    outcome = engine.on_turn_end_attempt("p1", context={"turn_has_rolled": False})
    assert outcome.status == "penalty"
    assert outcome.cash_delta < 0
    assert outcome.message_key == "monopoly-cheaters-early-end-turn-blocked"


def test_engine_allows_end_turn_after_roll():
    engine = CheatersEngine(DEFAULT_CHEATERS_PROFILE)
    engine.on_turn_start("p1", turn_index=0)
    outcome = engine.on_turn_end_attempt("p1", context={"turn_has_rolled": True})
    assert outcome.status == "allow"


def test_engine_escalates_penalty_after_threshold():
    engine = CheatersEngine(DEFAULT_CHEATERS_PROFILE)
    engine.on_turn_start("p1", turn_index=0)
    first = engine.on_turn_end_attempt("p1", context={"turn_has_rolled": False})
    second = engine.on_turn_end_attempt("p1", context={"turn_has_rolled": False})
    assert second.cash_delta <= first.cash_delta
    assert second.reason_code == "escalated_repeat_violation"
