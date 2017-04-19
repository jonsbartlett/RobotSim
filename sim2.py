from objects import *
from variables import *
import thread,time
import random

a=Arena()
populate_walls(7,7)
for i in xrange(40,NUMBER_OF_TOKENS+40):
    token_list.append(Token(i))

a=odelib.RotationalActuator()

while True:
    n = 2
	
    for i in range(n):
        # Simulation step
        a.UpdateSettings(world)
        world.step(dt/n)
    rate(RATE)
