from mods_base import build_mod, get_pc, hook, BoolOption, SliderOption
from unrealsdk.hooks import Type, prevent_hooking_direct_calls
import unrealsdk
from ui_utils import show_hud_message
import random

check_counter = 0

auto_refill_enabled = BoolOption("Auto Refill Enabled", True)
refill_threshold = SliderOption("Refill Threshold (%)", 0, 0, 50, 1)

@hook("WillowGame.WillowPlayerController:PlayerTick", Type.POST)
def check_ammo_refill(obj, __args, __ret, __func):
    global check_counter
    
    if not auto_refill_enabled.value:
        return
        
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

    # Check if all ammo is at or below threshold
    threshold_ratio = refill_threshold.value / 100.0
    for pool in ammo_pools:
        if pool.CurrentValue > (pool.MaxValue * threshold_ratio):
            return

    # All pools are at or below threshold, pick a random one to refill
    with prevent_hooking_direct_calls():
        random_pool = random.choice(ammo_pools)
        random_pool.CurrentValue = random_pool.MaxValue


build_mod()
