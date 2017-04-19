from PIL import Image
from visual import *

'''
##################
Colours and Images
##################
'''
#imports two images we need to use 
#im2 = Image.open('floor.png')
#materials.saveTGA("floor",im2)
#im = Image.open('marker-0.jpg')
#im = asarray(im)


#converts images to usable textures
tex = materials.texture(data=materials.loadTGA("marker-0"), mapping='sign')
#tex2 = materials.texture(data=materials.loadTGA("floor"), mapping='sign')

#defines any useful colours we need, RGB scale between 0-1, user colour_mapper function to convert from 0-255 to 0-1
color.brown = (0.38,0.26,0.078)
color.orange = (0.85,0.54,0.18)
