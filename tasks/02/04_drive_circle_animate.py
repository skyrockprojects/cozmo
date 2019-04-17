#!/usr/bin/env python3

'''
Make cozmo drive in a circle while his head is looking upward and his lift is mid-air
after he has driven full circle, let him make a random animation.
'''
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
    
    for _ in range(4):
        circle()
       


def circle():
        print('circle')
         # Drive in a circle