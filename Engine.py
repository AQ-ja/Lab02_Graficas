from GL import Renderer, V3, _color
from obj import Texture
from shaders import *

import random

width = 960
height = 540

rend = Renderer(width, height)

rend.directional_light = V3(1,0,0)

#rend.active_texture = Texture('Models/earthDay.bmp')
#rend.active_texture2 = Texture('Models/earthNight.bmp')
#rend.active_shader = textureBlend

rend.glLoadModel("Models/Sphere.obj",
                 translate = V3(0, 0, 0),
                 scale = V3(0.8,0.8,0.8),
                 rotate = V3(0, 0, 0) )

rend.glLoadModel("Models/Sphere.obj", 
                 translate=V3(0, 50, 0),
                 scale= V3(0.8,0.8,0.8),
                 rotate= V3(0, 80, 0))


rend.glFinish("Lab02.bmp")
