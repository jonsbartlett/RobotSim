from objects import *
from variables import *
import thread,time
import random
from visual.controls import *

for i in xrange(1):
    token_list.append(Token(40))

populate_walls(7,7)
a=Arena()
R=Robot()
R1 = Robot(3.75,0.15,-3.75)


def usercode0():
    while True:
        R.motors[0].speed = 75
        R.motors[1].speed = 76

def usercode1():
    while True:
        R1.motors[0].speed = -75
        R1.motors[1].speed = -75
                    
thread.start_new_thread(usercode0,())        
thread.start_new_thread(usercode1,())
        
while True:
    n = 2
    for i in range(n):
        # Simulation step
        world.step(dt/n)
    R.update()
    R1.update()
    for token in token_list:
        token.update()
    rate(RATE)