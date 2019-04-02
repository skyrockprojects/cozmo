#!/usr/bin/env python3


'''Tell Cozmo to drive up to a cube that he sees placed in front of him.

This example demonstrates Cozmo driving to and docking with a cube, without
picking it up.  You must place a cube in front of Cozmo so that he can see it.
The cube should be centered in front of him.
'''

import cozmo
from cozmo.util import degrees

async def dock_with_cube(robot: cozmo.robot.Robot):
    await robot.set_head_angle(degrees(-5.0)).wait_for_completed()

    print("Cozmo is waiting until he sees a cube.")
    cube = await robot.world.wait_for_observed_light_cube()

    print("Cozmo found a cube, and will now attempt to dock with it:")
    # Cozmo will approach the cube he has seen
    # using a 180 approach angle will cause him to drive past the cube and approach from the opposite side
    # num_retries allows us to specify how many times Cozmo will retry the action in the event of it failing
    action = robot.dock_with_cube(cube, approach_angle=cozmo.util.degrees(180), num_retries=2)
    await action.wait_for_completed()
    print("result:", action.result)

cozmo.run_program(dock_with_cube)
