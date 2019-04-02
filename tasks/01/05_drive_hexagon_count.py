#!/usr/bin/env python3

'''
Make cozmo drive in a hexagon and count the sides while doing it.
'''
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
    
    for _ in range(4):
        print("?")
        # Drive in a hexagon and let cozmo count the sides of it here. 