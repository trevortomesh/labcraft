from ursina import *

def oscSim(self):
    self.t += time.dt * self.sliders[3].value
    self.planet.x = (math.cos(self.t) + self.position.x) * self.sliders[0].value
    self.planet.y = self.position.y * self.sliders[1].value
    self.planet.z = (math.sin(self.t) + self.position.z) * self.sliders[2].value
    #print(self.sliders[0].value)

def simple_pendulum(self):
    self.pendulum.x = self.position.x + 0.7
    self.pendulum.y = self.position.y
    self.pendulum.z = self.position.z
    self.pendulum.rotation += Vec3(0.5,0,0)
