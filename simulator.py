from objects import *
from variables import *
import thread,time
import random
'''
#################
Usercode Function
#################
'''    

def SR_filter(listname,markertype):
    temporary_list=[]
    for l in listname:
        if l.marker_type== markertype:
            temporary_list.append(l)
    listname=temporary_list
    return listname


def distance_orderer(listname):
    listname=sorted(listname, key=lambda Marker:Marker.distance)
    return listname

def usercode0():
    time.sleep(10)
    while True:
        R0.motors[0].speed = 0
        R0.motors[1].speed = 0
        markers = R3.see()
        markers = SR_filter(markers, 'TOKEN')
        
        if len(markers)>0:
            markers = distance_orderer(markers)
            angle = markers[0].bearing.y
            print angle
            if angle >5 and angle <30:
                R0.motors[0].speed = -75
                R0.motors[1].speed = 75
                time.sleep(0.2)
            elif angle < -5 and angle > -30:
                R0.motors[0].speed = 75
                R0.motors[1].speed = -75
                time.sleep(0.2)
            elif angle <5 and angle >-5:
                R0.motors[0].speed = 80
                R0.motors[1].speed = 80
                time.sleep(1)
        else:
            R0.motors[0].speed = -100
            R0.motors[1].speed = 100
            time.sleep(0.5)

def usercode1():
    time.sleep(10)
    while True:
        R1.motors[0].speed = 0
        R1.motors[1].speed = 0
        markers = R1.see()
        markers = SR_filter(markers, 'TOKEN')
        
        if len(markers)>0:
            markers = distance_orderer(markers)
            angle = markers[0].bearing.y
            print angle
            if angle >5 and angle <30:
                R1.motors[0].speed = -75
                R1.motors[1].speed = 75
                time.sleep(0.2)
            elif angle < -5 and angle > -30:
                R1.motors[0].speed = 75
                R1.motors[1].speed = -75
                time.sleep(0.2)
            elif angle <5 and angle >-5:
                R1.motors[0].speed = 80
                R1.motors[1].speed = 80
                time.sleep(1)
        else:
            R1.motors[0].speed = -100
            R1.motors[1].speed = 100
            time.sleep(0.5)

def usercode2():
    time.sleep(10)
    while True:
        R2.motors[0].speed = 0
        R2.motors[1].speed = 0
        markers = R2.see()
        markers = SR_filter(markers, 'TOKEN')
        
        if len(markers)>0:
            markers = distance_orderer(markers)
            angle = markers[0].bearing.y
            print angle
            if angle >5 and angle <30:
                R2.motors[0].speed = -75
                R2.motors[1].speed = 75
                time.sleep(0.2)
            elif angle < -5 and angle > -30:
                R2.motors[0].speed = 75
                R2.motors[1].speed = -75
                time.sleep(0.2)
            elif angle <5 and angle >-5:
                R2.motors[0].speed = 80
                R2.motors[1].speed = 80
                time.sleep(1)
        else:
            R2.motors[0].speed = -100
            R2.motors[1].speed = 100
            time.sleep(0.5)

def usercode3():
    time.sleep(10)
    while True:
        R3.motors[0].speed = 0
        R3.motors[1].speed = 0
        markers = R3.see()
        markers = SR_filter(markers, 'TOKEN')
        
        if len(markers)>0:
            markers = distance_orderer(markers)
            angle = markers[0].bearing.y
            print angle
            if angle >5 and angle <30:
                R3.motors[0].speed = -75
                R3.motors[1].speed = 75
                time.sleep(0.2)
            elif angle < -5 and angle > -30:
                R3.motors[0].speed = 75
                R3.motors[1].speed = -75
                time.sleep(0.2)
            elif angle <5 and angle >-5:
                R3.motors[0].speed = 80
                R3.motors[1].speed = 80
                time.sleep(1)
        else:
            R3.motors[0].speed = -100
            R3.motors[1].speed = 100
            time.sleep(0.5)
a=Arena()
populate_walls(7,7)
for i in xrange(40,NUMBER_OF_TOKENS+40):
    token_list.append(Token(i))
robotlist = []
R0=Robot(0)
R2=Robot(2)
R1=Robot(1)
R3=Robot(3)

robotlist.append(R0)
robotlist.append(R1)
robotlist.append(R2)
robotlist.append(R3)

thread.start_new_thread(usercode0,())
thread.start_new_thread(usercode1,())
thread.start_new_thread(usercode2,())
thread.start_new_thread(usercode3,())

while True:
    n = 2
    for i in range(n):
        # Simulation step
        world.step(dt/n)
    for robot in robotlist:
        robot.update() 
    for token in token_list:
        token.update()
    rate(RATE)
