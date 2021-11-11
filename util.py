from ursina import *
from sims import *

# draws slider UI component for variables in solar system model
def initSolarSystemSliders(self):
    self.sliders = list()
    sliderX = ThinSlider(text="X Position", max=5, default=1, x=-.65, y=(0.4*.75), step=0.1)
    self.sliders.append(sliderX)
    sliderX2 = ThinSlider(text="X MOD", max=25, default=1, x=-.65, y=(0.4*.75) - 0.025, step=0.1)
    self.sliders.append(sliderX2)
    sliderY = ThinSlider(text="Y Position", max=5, default=1, x=-.65, y=(0.4*.75) - .05, step=0.1)
    self.sliders.append(sliderY)
    sliderY2 = ThinSlider(text="Y MOD", max=5, default=1, x=-.65, y=(0.4*.75) - .075, step=0.1)
    self.sliders.append(sliderY2)
    sliderZ = ThinSlider(text="Z Position", max=5, default=1, x=-.65, y=(0.4*.75) - .1, step=0.1)
    self.sliders.append(sliderZ)
    sliderZ2 = ThinSlider(text="Z MOD", max=25, default=1, x=-.65, y=(0.4*.75) - .125, step=0.1)
    self.sliders.append(sliderZ2)
    sliderA = ThinSlider(text="SPEED", max=100, default=1, x=-.65, y=(0.4*.75) - .15, step=1)
    self.sliders.append(sliderA)

    for slider in self.sliders:
        slider.min = 0
        slider.dynamic = True
        slider.bg.color = color.black
        slider.label.color = color.black
        slider.scale *= .75

def destroySliders(self):
    for slider in self.sliders:
        destroy(slider)
