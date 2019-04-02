#!/usr/bin/env python3

'''Tell Cozmo to roll a cube that is placed in front of him.

This example demonstrates Cozmo driving to and rolling a cube.
You must place a cube in front of Cozmo so that he can see it.
The cube should be centered in front of him.
'''

import cozmo
from cozmo.util import degrees

async def roll_a_cube(robot: cozmo.robot.Robot):
    await robot.set_head_angle(degrees(-5.0)).wait_for_completed()

    print("Cozmo is waiting until he sees a cube")
    cube = await robot.world.wait_for_observed_light_cube()

    print("Cozmo found a cube, and will now attempt to roll with it:")
    # Cozmo will approach the cube he has seen and roll it
    # check_for_object_on_top=True enforces that Cozmo will not roll cubes with anything on top
    action = robot.roll_cube(cube, check_for_object_on_top=True, num_retries=2)
    await action.wait_for_completed()
    print("result:", action.result)

cozmo.run_program(roll_a_cube)
