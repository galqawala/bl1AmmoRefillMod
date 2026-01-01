# Ammo Refill Mod

A Borderlands 1 SDK mod that automatically refills a random ammo type when all ammo is depleted.

## Features

- Automatically detects when all ammo types are at 0
- Randomly selects one ammo type to refill to maximum capacity
- Runs efficiently with once-per-second checks
- Works seamlessly in the background

## Installation

1. Place the `AmmoRefillMod` folder in your `sdk_mods` directory
2. The mod will auto-enable by default
3. Start playing!

## How it Works

The mod hooks into the player tick function and checks ammo levels once per second. When it detects that all ammo pools are empty, it randomly selects one ammo type and refills it to maximum capacity.

## License

GPL-3.0