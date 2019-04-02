#!/usr/bin/env python3

'''Hello World

Make Cozmo say 'Hello <your name>' in this simple Cozmo SDK example program.
'''

import cozmo


def cozmo_program(robot: cozmo.robot.Robot):
    text = "Hello"
    robot.say_text(text).wait_for_completed()


cozmo.run_program(cozmo_program)
