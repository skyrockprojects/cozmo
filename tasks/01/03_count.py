#!/usr/bin/env python3

import cozmo

def cozmo_program(robot: cozmo.robot.Robot):

    for i in range(5):
        
        robot.say_text(str(i+1)).wait_for_completed()


cozmo.run_program(cozmo_program)
