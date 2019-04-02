#!/usr/bin/env python3


'''Use custom objects to create a wall in front of Cozmo.

This example demonstrates how you can create custom objects in the world, and
automatically have Cozmo path around them as if they are real obstacles.

It creates a wall in front of cozmo and tells him to drive around it.
He will plan a path to drive 200mm in front of himself after these objects are created.

The `use_3d_viewer=True` argument causes the 3D visualizer to open in a new
window - this shows where Cozmo believes this imaginary object is.
'''

import cozmo
from cozmo.util import degrees, Pose


def cozmo_program(robot: cozmo.robot.Robot):
    fixed_object = robot.world.create_custom_fixed_object(Pose(100, 0, 0, angle_z=degrees(0)),
                                                        10, 100, 100, relative_to_robot=True)
    if fixed_object:
        print("fixed_object created successfully")

    robot.go_to_pose(Pose(200, 0, 0, angle_z=degrees(0)), relative_to_robot=True).wait_for_completed()


cozmo.run_program(cozmo_program, use_3d_viewer=True)
