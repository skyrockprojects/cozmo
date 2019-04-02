#!/usr/bin/env python3


'''Control Cozmo's Backpack lights

This script shows how you can control Cozmo's backpack lights and set
them to different colors.
'''

import time

import cozmo


def cozmo_program(robot: cozmo.robot.Robot):
    # set all of Cozmo's backpack lights to red, and wait for 2 seconds
    robot.set_all_backpack_lights(cozmo.lights.red_light)
    time.sleep(2)
    # set all of Cozmo's backpack lights to green, and wait for 2 seconds
    robot.set_all_backpack_lights(cozmo.lights.green_light)
    time.sleep(2)
    # set all of Cozmo's backpack lights to blue, and wait for 2 seconds
    robot.set_all_backpack_lights(cozmo.lights.blue_light)
    time.sleep(2)
    # set just Cozmo's center backpack lights to white, and wait for 2 seconds
    robot.set_center_backpack_lights(cozmo.lights.white_light)
    time.sleep(2)
    # turn off Cozmo's backpack lights and wait for 2 seconds
    robot.set_all_backpack_lights(cozmo.lights.off_light)
    time.sleep(2)


cozmo.run_program(cozmo_program)
