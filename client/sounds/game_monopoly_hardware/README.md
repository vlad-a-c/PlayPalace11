# Monopoly Hardware Sound Assets

This folder contains temporary placeholder sounds and optional sourced stand-ins for
Monopoly hardware-emulation events.

The sourced stand-ins are not board-authentic captures. They keep gameplay audible until
original board captures are sourced and licensed.

## Original Intake Pipeline

No code changes are required to swap in originals.

1. Put an original capture at one of these target paths:
   - `client/sounds/game_monopoly_hardware/original/play_theme.ogg`
   - `client/sounds/game_monopoly_hardware/original/star_wars_theme.ogg`
   - `client/sounds/game_monopoly_hardware/original/junior_coin_sound_powerup.ogg`
2. Runtime automatically prefers the `original/` asset when present and falls back to placeholder otherwise.
3. Optional helper script:
   - `uv run --project server --extra dev python -m server.scripts.monopoly.install_hardware_sound_replacement --event <event_id> --source /abs/path/file.ogg`
   - Add `--dry-run` to preview target path without copying.

## Current Sourced Stand-ins

Installed `original/` assets (runtime currently prefers these):

- `game_monopoly_hardware/original/play_theme.ogg`
  - Event: `play_theme`
  - Source: `https://opengameart.org/content/50-rpg-sound-effects`
  - Direct file: `https://opengameart.org/sites/default/files/RPGsounds_Kenney.zip` (`OGG/metalClick.ogg`)
  - Author: Kenney
  - License: CC0
  - SHA256: `9851a69d0c613e13bceef08060ecc4148f098ef487927cbebe270d642398a3b3`

- `game_monopoly_hardware/original/star_wars_theme.ogg`
  - Event: `star_wars_theme`
  - Source: `https://opengameart.org/content/space-theme`
  - Direct file: `https://opengameart.org/sites/default/files/spacetheme.ogg`
  - Author: JSKNYC
  - License: CC-BY 3.0
  - SHA256: `9cc03e44e80bbdda67de60db9dcfb5ede60f45940a274fa85a1cd6cbafa8e57a`

- `game_monopoly_hardware/original/junior_coin_sound_powerup.ogg`
  - Event: `junior_coin_sound_powerup`
  - Source: `https://commons.wikimedia.org/wiki/File:Coins_dropped_in_metallic_moneybox.ogg`
  - Direct file: `https://commons.wikimedia.org/wiki/Special:FilePath/Coins_dropped_in_metallic_moneybox.ogg`
  - License: Public domain
  - SHA256: `4730ef7a3494bcebeab02f3d452afdca62edb4d9e5c7acdd530cde1dbb0f58b5`

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
