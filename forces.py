from ursina import *

GRAVITY = (-9.8/2)

def applyGravity(entity):
    # Checks if entity is currently colliding with anything below itself, if NOT then it applies gravity
    check_for_collision_below = raycast(entity.position, (0, -1, 0), ignore=(entity,), distance=0.5)
    if not check_for_collision_below:
        # TODO: GRAVITY should work by modulating a veloctiy, not a position..
        entity.y += GRAVITY * time.dt


# below function not yet implemented for anything -- the thought is to allow the player ("pusher") to push an object
def checkForPushing(pusher, pushed):
    check_for_collision_between = raycast(pusher.position, pusher.direction, ignore=(pusher,), distance=0.5)
    if check_for_collision_between:
        pushed.direction += pusher.direction * pusher.velocity * time.dt