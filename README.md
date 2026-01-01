# Ammo Refill Mod

A Borderlands 1 SDK mod that automatically refills a random ammo type when all ammo is depleted.

## Features

- Automatically detects when all ammo types are at or below threshold
- Randomly selects one ammo type to refill to maximum capacity
- Configurable enable/disable toggle
- Adjustable threshold (0-50%) - default 0%
- Runs efficiently with once-per-second checks
- Works seamlessly in the background

## Configuration Options

- **Auto Refill Enabled**: Toggle to enable/disable the mod (default: True)
- **Refill Threshold (%)**: Percentage threshold for triggering refill (default: 0%, range: 0-50%)
  - At 0%: Refills when all ammo types are completely empty
  - At 10%: Refills when all ammo types are at 10% or less of maximum

## Installation

1. Place the `AmmoRefillMod` folder in your `sdk_mods` directory
2. The mod will auto-enable by default
3. Configure options in the mod menu
4. Start playing!

## How it Works

The mod hooks into the player tick function and checks ammo levels once per second. When it detects that all ammo pools are at or below the configured threshold, it randomly selects one ammo type and refills it to maximum capacity.

## License

GPL-3.0