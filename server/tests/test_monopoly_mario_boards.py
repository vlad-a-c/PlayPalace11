"""Integration tests for Wave 1 Monopoly Mario board runtime behavior."""

from server.games.monopoly.game import MonopolyGame, MonopolyOptions
from server.users.test_user import MockUser


def _start_two_player_game(options: MonopolyOptions | None = None) -> MonopolyGame:
    game = MonopolyGame(options=options or MonopolyOptions())
    game.add_player("Host", MockUser("Host"))
    game.add_player("Guest", MockUser("Guest"))
    game.host = "Host"
    game.on_start()
    return game


def test_board_rules_auto_applies_pass_go_override(monkeypatch):
    game = _start_two_player_game(
        MonopolyOptions(
            preset_id="classic_standard",
            board_id="mario_kart",
            board_rules_mode="auto",
        )
    )
    host = game.current_player
    assert host is not None

    monkeypatch.setattr(
        "server.games.monopoly.board_rules.mario_kart.PASS_GO_CREDIT_OVERRIDE",
        275,
    )
    host.position = 39
    rolls = iter([1, 1])
    monkeypatch.setattr("server.games.monopoly.game.random.randint", lambda a, b: next(rolls))

    game.execute_action(host, "roll_dice")

    assert host.cash == 1775
