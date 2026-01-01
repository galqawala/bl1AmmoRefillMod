from mods_base import build_mod, get_pc, hook
from unrealsdk.hooks import Type, prevent_hooking_direct_calls
import unrealsdk
from ui_utils import show_hud_message
import random

check_counter = 0


@hook("WillowGame.WillowPlayerController:PlayerTick", Type.POST)
def check_ammo_refill(obj, __args, __ret, __func):
    global check_counter
    check_counter += 1
    if check_counter % 60 != 0:  # Check once per second (assuming 60 FPS)
        return

    pc = get_pc()
    if pc is None:
        return

    # Get the resource pool manager
    rpm = pc.ResourcePoolManager
    if rpm is None:
        return

    # Get all ammo pools
    ammo_pools = []
    for pool in rpm.ResourcePools:
        if pool is None:
            continue
        if pool.Definition is None:
            continue
        if pool.Definition.Name.startswith("Ammo_"):
            ammo_pools.append(pool)

    if not ammo_pools:
        return

    # Check if all ammo is 0
    all_zero = all(pool.CurrentValue == 0 for pool in ammo_pools)

    if all_zero:
        # Pick a random ammo pool and refill
        with prevent_hooking_direct_calls():
            random_pool = random.choice(ammo_pools)
            random_pool.CurrentValue = random_pool.MaxValue


build_mod()
