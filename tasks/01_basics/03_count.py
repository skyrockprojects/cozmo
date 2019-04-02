#!/usr/bin/env python3

'''Count to 5

Make Cozmo count from 1 to 5
'''

import cozmo


def cozmo_program(robot: cozmo.robot.Robot):
    # A "for loop" runs for each value i in the given range - in this example
    # starting from 0, while i is less than 5 (so 0,1,2,3,4).
    for i in range(5):
        # Add 1 to the number (so that we count from 1 to 5, not 0 to 4),
        # then convert the number to a string and make Cozmo say it.
        robot.say_text(str(i+1)).wait_for_completed()


cozmo.run_program(cozmo_program)
