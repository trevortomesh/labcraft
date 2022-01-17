from ursina import *

GRAVITY = -9.8

def applyGravity(entity):

    check_for_collision_below = raycast(entity.position, (0, -1, 0), ignore=(entity,), distance=0.5)
    if not check_for_collision_below:
        entity.y += GRAVITY * time.dt
