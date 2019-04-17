#!/usr/bin/env python3

'''Play some animations on Cozmo

Plays animations by fetching lists of supported triggers from the robot,
and playing 2 selections of them: one random selection and one by filtering
for a name.
'''

import cozmo
import random

def cozmo_program(robot: cozmo.robot.Robot):
    # grab a list of animation triggers
    all_animation_triggers = robot.anim_triggers

    # randomly shuffle the animations
    random.shuffle(all_animation_triggers)

    # select the first three animations from the shuffled list
    triggers = 3
    chosen_triggers = all_animation_triggers[:triggers]
    print('Playing {} random animations:'.format(triggers))

    # play the three random animations one after the other, waiting for each to complete
    for trigger in chosen_triggers:
        print('Playing {}'.format(trigger.name))
        robot.play_anim_trigger(trigger).wait_for_completed()

cozmo.run_program(cozmo_program)
