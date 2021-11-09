from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

window.borderless = False

app = Ursina()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture  = load_texture('assets/dirt_block.png')
sky_texture   = load_texture('assets/skybox.png')
arm_texture   = load_texture('assets/arm_texture.png')
acc_texture   = load_texture('assets/acc_block.png')
mc_brick      = load_texture('assets/mc_brick.png')
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
 

    

    if debug == True:
        print(player.position.y)

    
    # if player falls through the map, return to starting point.
    if player.position.y < -10:

        if debug == True:
            print("falling!")
        
        player.y = 1
        player.x = 1
        player.z = 1

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
                if block_pick == 5: voxel = OscBlock(position = self.position + mouse.normal, texture = acc_texture)

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


class pendulum(Entity):
    def __init__(self,rotation=(0,0,0), texture = mc_brick):
        super().__init__(
            parent = scene,
            texture = mc_brick,
            model = 'assets/pendulum',
            color = color.gray,
            scale = .3,
            rotation = Vec3(0,0,0),
            position = Vec3(5,2.5,5))
    def update(self):
       # self.t += time.dt
        self.rotation += Vec3(0.5,0,0)




def terrainGen():
    for z in range(20):
        for x in range(20):
            voxel = Voxel(position = (x,0,z))




class OscBlock(Button):
    def __init__(self, position = (0,0,0), texture = acc_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            scale = 0.5)


        self.cube = Entity(model="cube", color=color.red, scale=0.2)
        self.t = 0.0

    def update(self):
        self.t += time.dt
        self.cube.x = math.cos(self.t) + self.position.x
        self.cube.y = self.position.y
        self.cube.z = math.sin(self.t) + self.position.z
        if self.hovered and held_keys['right mouse']:
            destroy(self.cube)
            destroy(self)


terrainGen()

player = FirstPersonController()
sky = Sky()
hand = Hand()
pendulum()

app.run()