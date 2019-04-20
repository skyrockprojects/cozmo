#!/usr/bin/env python3

'''Display images on Cozmo's face (oled screen)
'''

import os
import sys
import time

try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")

import cozmo


def get_in_position(robot: cozmo.robot.Robot):
    '''If necessary, Move Cozmo's Head and Lift to make it easy to see Cozmo's face'''
    # If Cozmo's lift height is higher than 45mm (robot.lift_height.distance_mm)
    # or its head is smaller than 40 degrees (robot.head_angle.degrees < 40): 
    with robot.perform_off_charger():
        print("test")
    # set the lift height to 0.0 (robot.set_lift_height())
    # set the head angle to the maximum (robot.set_head_angle())
    # wait for complete

def cozmo_program(robot: cozmo.robot.Robot):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    # call the get_in_position function here
    sdk_png = os.path.join(current_directory, "..", "..", "face_images", "cozmosdk.png")
    hello_png = os.path.join(current_directory, "..", "..", "face_images", "hello_world.png")

    # load some images and convert them for display cozmo's face
    image_settings = [(sdk_png, Image.BICUBIC),
                      (hello_png, Image.NEAREST)]
    face_images = []
    for image_name, resampling_mode in image_settings:
        image = Image.open(image_name)

        # resize to fit on Cozmo's face screen
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)

        # convert the image to the format used by the oled screen
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,
                                                                 invert_image=True)
        face_images.append(face_image)

    # display each image on Cozmo's face for duration_s seconds (Note: this
    # is clamped at 30 seconds max within the engine to prevent burn-in)
    # repeat this num_loops times

    num_loops = 10
    duration_s = 2.0

    print("Press CTRL-C to quit (or wait %s seconds to complete)" % int(num_loops*duration_s) )

    robot.display_oled_face_image(face_image[0], 1.0 * 1000.0)

    # for _ in range(num_loops):
    #     display each image on Cozmo's face for duration_s seconds 
    


# Cozmo is moved off his charger contacts by default at the start of any program.
# This is because not all motor movement is possible whilst drawing current from
# the charger. In cases where motor movement is not required, such as this example
# we can specify that Cozmo can stay on his charger at the start:
cozmo.robot.Robot.drive_off_charger_on_connect = False

cozmo.run_program(cozmo_program)

