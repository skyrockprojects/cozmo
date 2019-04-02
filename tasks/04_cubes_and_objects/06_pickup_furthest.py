#!/usr/bin/env python3

'''Make Cozmo pick up the furthest Cube.

This script shows simple math with object's poses.

The robot attempts to find three Cubes within his view, which
you can see in the camera window that opens when the script
is run. Each Cube will show with an outline and cube number
if the Cube is in the frame.

The robot waits until 3 Cubes are found, and then attempts to
pick up the furthest one. It calculates this based on the
reported poses of the Cubes.
'''

import cozmo


def cozmo_program(robot: cozmo.robot.Robot):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=3, object_type=cozmo.objects.LightCube, timeout=60)
    lookaround.stop()

    max_dst, targ = 0, None
    for cube in cubes:
        translation = robot.pose - cube.pose
        dst = translation.position.x ** 2 + translation.position.y ** 2
        if dst > max_dst:
            max_dst, targ = dst, cube

    if len(cubes) < 3:
        print("Error: need 3 Cubes but only found", len(cubes), "Cube(s)")
    else:
        robot.pickup_object(targ, num_retries=3).wait_for_completed()


cozmo.run_program(cozmo_program, use_viewer=True)
