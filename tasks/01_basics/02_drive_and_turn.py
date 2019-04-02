#!/usr/bin/env python3

'''Drive And Turn

Make Cozmo drive forwards and then turn 90 degrees to the left.
'''

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):
    # Drive forwards for 150 millimeters at 50 millimeters-per-second.
    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()

    # Turn 90 degrees to the left.
    # Note: To turn to the right, just use a negative number.
    robot.turn_in_place(degrees(90)).wait_for_completed()


cozmo.run_program(cozmo_program)
