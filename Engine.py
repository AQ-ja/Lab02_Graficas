from GL import Renderer, V3, _color
from obj import Texture
from shaders import *

import random

width = 960
height = 540

rend = Renderer(width, height)

rend.directional_light = V3(1,0,0)

rend.active_texture = Texture('Models/earthDay.bmp')
rend.active_texture2 = Texture('Models/earthNight.bmp')
rend.active_shader = textureBlend

rend.glLoadModel("Models/model.obj",
                 translate = V3(0, 0, -10),
                 scale = V3(0.01,0.01,0.01),
                 rotate = V3(0, 80, 0) )

rend.glFinish("output.bmp")