#!/usr/bin/env python3


'''Tell Cozmo to drive to the specified pose and orientation.

Define a destination pose for Cozmo. If relative_to_robot is set to true,
the given pose will assume the robot's pose as its origin.
'''

import cozmo
from cozmo.util import degrees, Pose


def cozmo_program(robot: cozmo.robot.Robot):
    robot.go_to_pose(Pose(100, 100, 0, angle_z=degrees(45)), relative_to_robot=True).wait_for_completed()


cozmo.run_program(cozmo_program)
