from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()


platform = Entity(model="plane", collider = "mesh", texture = "grass", scale = 100, position = (0,-10,0))
model = Entity(model = "pendulum", collider = "mesh", texture = "mc_brick.png", position = (0,0,5))

app.run()