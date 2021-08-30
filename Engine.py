# Programa principal
from numpy import min_scalar_type
from Shaders import toon
from GL import Renderer, V3, _color
from obj import Texture
from Shaders import *

import random

width = 1920
height = 1080

rend = Renderer(width, height)

rend.directional_light = V3(0,0,-1)

rend.active_texture = Texture('Models/model.bmp')

# Primer shader (toon shader)
rend.active_shader = toon
rend.glLoadModel("Models/model.obj", translate = V3(-3, 0, -10), scale = V3(3,3,3), rotate= V3(1, 0.5, 0))

# Segundo shader 
rend.active_shader = neonish
rend.glLoadModel("Models/model.obj", translate = V3(1.4, 2.5, -10), scale = V3(2,2,2), rotate= V3(0, 0, 0))

# Tercer shader 
rend.active_shader = redish
rend.glLoadModel("Models/model.obj", translate= V3(2.8, 0.5, -5), scale=V3(1, 1, 1), rotate = V3(0, 0, 0))


# Cuarto shader
rend.active_shader = dotish
rend.glLoadModel("Models/model.obj", translate= V3(1, -1, -4), scale=V3(1, 1, 1), rotate = V3(2, 0, 2))





rend.glFinish("Lab02.bmp")