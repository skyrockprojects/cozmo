#!/usr/bin/env python3

'''Display Cozmo's camera feed back on his face (like a mirror)
'''

import sys
import time

try:
    import numpy as np
except ImportError:
    sys.exit("Cannot import numpy: Do `pip3 install --user numpy` to install")

try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")

import cozmo


def calc_pixel_threshold(image: Image):
    '''Calculate a pixel threshold based on the image.

    Anything brighter than this will be shown on (light blue).
    Anything darker will be shown off (black).
    '''

    # Convert image to gray scale
    grayscale_image = image.convert('L')

    # Calculate the mean (average) value
    mean_value = np.mean(grayscale_image.getdata())
    return mean_value


def cozmo_face_mirror(robot: cozmo.robot.Robot):
    '''Continuously display Cozmo's camera feed back on his face.'''

    robot.camera.image_stream_enabled = True
    get_in_position(robot)

    face_dimensions = cozmo.oled_face.SCREEN_WIDTH, cozmo.oled_face.SCREEN_HALF_HEIGHT

    print("Press CTRL-C to quit")

    while True:
        duration_s = 0.1  # time to display each camera frame on Cozmo's face

        latest_image = robot.world.latest_image

        if latest_image is not None:
            # Scale the camera image down to fit on Cozmo's face
            resized_image = latest_image.raw_image.resize(face_dimensions,
                                                          Image.BICUBIC)

            # Flip the image left/right so it displays mirrored
            resized_image = resized_image.transpose(Image.FLIP_LEFT_RIGHT)

            # Calculate the pixel threshold for this image. This threshold
            # will define how bright a pixel needs to be in the source image
            # for it to be displayed as lit-up on Cozmo's face.
            pixel_threshold = calc_pixel_threshold(resized_image)

            # Convert the image to the format to display on Cozmo's face.
            screen_data = cozmo.oled_face.convert_image_to_screen_data(
                resized_image,
                pixel_threshold=pixel_threshold)

            # display the image on Cozmo's face
            robot.display_oled_face_image(screen_data, duration_s * 1000.0)

        time.sleep(duration_s)


cozmo.robot.Robot.drive_off_charger_on_connect = False  # Cozmo can stay on his charger for this example
cozmo.run_program(cozmo_face_mirror)
