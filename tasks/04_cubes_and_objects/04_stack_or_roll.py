#!/usr/bin/env python3

'''Make Cozmo perform different actions based on the number of Cubes he finds.

This script shows off simple decision making.
It tells Cozmo to look around, and then wait until he sees a certain amount of objects.
Based on how many object he sees before he times out, he will do different actions.
0-> be angry
1-> roll block (the block must not be face up)
2-> stack blocks (the blocks must all be face up)
'''

import cozmo


def cozmo_program(robot: cozmo.robot.Robot):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)

    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=10)

    print("Found %s cubes" % len(cubes))

    lookaround.stop()

    if len(cubes) == 0:
        robot.play_anim_trigger(cozmo.anim.Triggers.MajorFail).wait_for_completed()
    elif len(cubes) == 1:
        robot.run_timed_behavior(cozmo.behavior.BehaviorTypes.RollBlock, active_time=60)
    else:
        robot.run_timed_behavior(cozmo.behavior.BehaviorTypes.StackBlocks, active_time=60)


cozmo.run_program(cozmo_program)
