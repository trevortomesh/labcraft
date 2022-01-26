from asyncore import read
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from sims import *
from util import * 
from forces import *

import json

save_data = {}

window.borderless = False

app = Ursina()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture  = load_texture('assets/dirt_block.png')
sky_texture   = load_texture('assets/skybox.png')
arm_texture   = load_texture('assets/arm_texture.png')
osc_texture   = load_texture('assets/osc_block.png')
earth_texture = load_texture('assets/earth_block.png')
mc_brick      = load_texture('assets/mc_brick.png')
sun_texture   = load_texture('assets/sun.png')
pendulum_texture = load_texture('assets/mc_brick.png')

punch_sound   = Audio('assets/punch_sound',loop = False, autoplay = False)
block_pick = 1

window.fps_counter.enabled = False
window.exit_button.visible = False

debug = False

def update():

    
    global block_pick
    global debug

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['5']: block_pick = 5
    if held_keys['6']: block_pick = 6
    if held_keys['7']: block_pick = 7

    
    # escape keypress will breakout mouse control from first person view
    if held_keys['escape']: mouse.locked = False
    # ` keypress will return first person mouse lock
    if held_keys['`']: mouse.locked = True
 

    

    if debug == True:
        print(player.position.y)

    
    # if player falls through the map, return to starting point.
    if player.position.y < -10:

        if debug == True:
            print("falling!")
        
        player.y = 1
        player.x = 1
        player.z = 1
    
    #save_data['playerPosition'] = player.get_position()
    if held_keys['enter']: save(readSceneData())

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            scale = 0.5)


    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
                if block_pick == 5: voxel = solarSystem(position = self.position + mouse.normal, texture = sun_texture)
                if block_pick == 6: voxel = pendulum(position = self.position+mouse.normal, texture = pendulum_texture)
                if block_pick == 7: ball = Ball(position = self.position + mouse.normal)

            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True)

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm',
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4,-0.6))

    def active(self):
        self.position = Vec2(0.3,-0.5)

    def passive(self):
        self.position = Vec2(0.4,-0.6)


class pendulum(Button):
    def __init__(self,position=(0,0,0), texture = pendulum_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            texture = pendulum_texture,
            color = color.gray,
            origin_y = 0.5,
            scale = 0.5)

        self.pendulum = Entity(model = "pendulum", collider = "mesh", texture = "mc_brick.png", scale = 0.1)


    def update(self):
        simple_pendulum(self)

        if self.hovered and held_keys['right mouse']:
            destroy(self.pendulum)        
            destroy(self)
          
    

class solarSystem(Button):
    def __init__(self, position = (0,0,0), texture = sun_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            scale = 0.5)

        self.planet = Entity(model="assets/block", scale= 0.1, texture = earth_texture)
        self.t = 0.0

        initSolarSystemSliders(self)      

    def update(self):
        oscSim(self)
        if self.hovered and held_keys['right mouse']:
            destroySliders(self)
            destroy(self.planet)
            destroy(self)

class Ball(Entity):
    def __init__(self, position = (0, 0, 0), yOffset = (0, 10, 0), direction = (0, 0, 0)):
        super().__init__(
            parent = scene,
            #position = position,
            position = position + yOffset,
            direction = direction,
            model = 'sphere',
            collider = 'sphere',
            #texture = 'circle',
            color = color.red,
            scale = 1.0)
        
    
    def update(self):
        if held_keys['g']:
            applyGravity(self)



def terrainGen():
    for z in range(20):
        for x in range(20):
            voxel = Voxel(position = (x,0,z))

def treeGen():
    for y in range(5):
        voxel = Voxel(position = (5, y, 5))
    
    for z in range(4, 7):
        for x in range(4, 7):
            voxel = Voxel(position = (x, 5, z))
    
    for z in range(3, 8):
        for x in range(3, 8):
            voxel = Voxel(position = (x, 6, z))
    for z in range(3, 8):
        for x in range(3, 8):
            voxel = Voxel(position = (x, 7, z))
    
    for z in range(4, 7):
        for x in range(4, 7):
            voxel = Voxel(position = (x, 8, z))
    
    apple = Ball((7, 5, 3), (0, 0, 0))



terrainGen()
treeGen()

player = FirstPersonController()
sky = Sky()
hand = Hand()
# pendulum()

app.run()