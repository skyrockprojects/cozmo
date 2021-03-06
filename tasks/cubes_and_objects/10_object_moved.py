#!/usr/bin/env python3


'''Demonstrate the use of Object Moving events to detect when the cubes are moved.

This script is a simple example of how to subscribe to Object Moving events to
track when Cozmo detects that a cube is being moved.
'''

import time

import cozmo


def handle_object_moving_started(evt, **kw):
    # This will be called whenever an EvtObjectMovingStarted event is dispatched -
    # whenever we detect a cube starts moving (via an accelerometer in the cube)
    print("Object %s started moving: acceleration=%s" %
          (evt.obj.object_id, evt.acceleration))


def handle_object_moving(evt, **kw):
    # This will be called whenever an EvtObjectMoving event is dispatched -
    # whenever we detect a cube is still moving a (via an accelerometer in the cube)
    print("Object %s is moving: acceleration=%s, duration=%.1f seconds" %
          (evt.obj.object_id, evt.acceleration, evt.move_duration))


def handle_object_moving_stopped(evt, **kw):
    # This will be called whenever an EvtObjectMovingStopped event is dispatched -
    # whenever we detect a cube stopped moving (via an accelerometer in the cube)
    print("Object %s stopped moving: duration=%.1f seconds" %
          (evt.obj.object_id, evt.move_duration))


def cozmo_program(robot: cozmo.robot.Robot):
    # Add event handlers that will be called for the corresponding event
    robot.add_event_handler(cozmo.objects.EvtObjectMovingStarted, handle_object_moving_started)
    robot.add_event_handler(cozmo.objects.EvtObjectMoving, handle_object_moving)
    robot.add_event_handler(cozmo.objects.EvtObjectMovingStopped, handle_object_moving_stopped)

    # keep the program running until user closes / quits it
    print("Press CTRL-C to quit")
    while True:
        time.sleep(1.0)


cozmo.robot.Robot.drive_off_charger_on_connect = False  # Cozmo can stay on his charger for this example
cozmo.run_program(cozmo_program)
