#!/usr/bin/env python3

'''Hello World

Make Cozmo say 'Hello World' in this simple Cozmo SDK example program.
'''

import cozmo


def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Hello World").wait_for_completed()


cozmo.run_program(cozmo_program)
