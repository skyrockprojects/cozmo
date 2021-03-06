#!/usr/bin/env python3

'''Play some animations on Cozmo

Play an animation using a trigger, and then another animation by name.
'''

import cozmo


def cozmo_program(robot: cozmo.robot.Robot):
    # Play an animation via a Trigger - see:
    # http://cozmosdk.anki.com/docs/generated/cozmo.anim.html#cozmo.anim.Triggers
    # for a list of available triggers.
    # A trigger can pick from several appropriate animations for variety.
    print("Playing Animation Trigger 1:")
    robot.play_anim_trigger(cozmo.anim.Triggers.CubePounceLoseSession).wait_for_completed()

    # Play the same trigger, but this time ignore the track that plays on the
    # body (i.e. don't move the wheels). See the play_anim_trigger documentation
    # for other available settings.
    print("Playing Animation Trigger 2: (Ignoring the body track)")
    robot.play_anim_trigger(cozmo.anim.Triggers.CubePounceLoseSession, ignore_body_track=True).wait_for_completed()



cozmo.run_program(cozmo_program)
