from ursina import *

def oscSim(self):
    self.t += time.dt * self.sliders[6].value
    self.planet.x = (math.cos(self.t) * self.sliders[1].value + self.position.x) * self.sliders[0].value
    self.planet.y = (self.position.y * self.sliders[2].value) / self.sliders[3].value
    self.planet.z = (math.sin(self.t) * self.sliders[5].value + self.position.z) * self.sliders[4].value


def simple_pendulum(self):
    self.pendulum.x = self.position.x + 0.7
    self.pendulum.y = self.position.y
    self.pendulum.z = self.position.z
    self.pendulum.rotation += Vec3(0.5,0,0)
