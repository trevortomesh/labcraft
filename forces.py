from ursina import *

# below function not yet implemented for anything -- the thought is to allow the player ("pusher") to push an object
def checkForPushing(pusher, pushed):
    check_for_collision_between = raycast(pusher.position, pusher.direction, ignore=(pusher,), distance=0.5)
    if check_for_collision_between:
        pushed.direction += pusher.direction * pusher.velocity * time.dt