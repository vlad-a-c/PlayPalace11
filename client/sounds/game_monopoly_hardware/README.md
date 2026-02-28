# Monopoly Hardware Placeholder Sounds

This folder contains temporary placeholder sounds for Monopoly hardware-emulation events.

These files are intentionally marked as placeholders and should be replaced with original
board-authentic captures once licensed sources are available.

## Original Intake Pipeline

No code changes are required to swap in originals.

1. Put an original capture at one of these target paths:
   - `client/sounds/game_monopoly_hardware/original/play_theme.ogg`
   - `client/sounds/game_monopoly_hardware/original/star_wars_theme.ogg`
   - `client/sounds/game_monopoly_hardware/original/junior_coin_sound_powerup.ogg`
2. Runtime automatically prefers the `original/` asset when present and falls back to placeholder otherwise.
3. Optional helper script:
   - `python server/scripts/monopoly/install_hardware_sound_replacement.py --event <event_id> --source /abs/path/file.ogg`
   - Add `--dry-run` to preview target path without copying.

## Mapping

- `play_theme_placeholder.ogg`
  - Event: `play_theme`
  - Current source: copied from `client/sounds/game_pig/roundstart.ogg`
  - Replacement needed: yes
  - Original target: `game_monopoly_hardware/original/play_theme.ogg`

- `star_wars_theme_placeholder.ogg`
  - Event: `star_wars_theme`
  - Current source: copied from `client/sounds/game_pig/roundstart.ogg`
  - Replacement needed: yes
  - Original target: `game_monopoly_hardware/original/star_wars_theme.ogg`

- `junior_coin_sound_placeholder.ogg`
  - Event: `junior_coin_sound_powerup`
  - Current source: copied from `client/sounds/game_pig/bank.ogg`
  - Replacement needed: yes
  - Original target: `game_monopoly_hardware/original/junior_coin_sound_powerup.ogg`
