from ursina import *

def oscSim(self):
    self.t += time.dt
    self.planet.x = math.cos(self.t) + self.position.x
    self.planet.y = self.position.y
    self.planet.z = math.sin(self.t) + self.position.z

def simple_pendulum(self):
    self.pendulum.x = self.position.x + 0.7
    self.pendulum.y = self.position.y
    self.pendulum.z = self.position.z
    self.pendulum.rotation += Vec3(0.5,0,0)
