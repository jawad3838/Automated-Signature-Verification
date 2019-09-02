# import the necessary packages
import argparse
import cv2
import os
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
ref_point = []
cropping = False
canvas_size = (1920, 1080)
crop_img = None
image = None

def shape_selection(event, x, y, flags, param):
        # grab references to the global variables
        global ref_point, cropping

        # if the left mouse button was clicked, record the starting
        # (x, y) coordinates and indicate that cropping is being
        # performed
        if event == cv2.EVENT_LBUTTONDOWN:
                ref_point = [(x, y)]
                cropping = True

        # check to see if the left mouse button was released
        elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
                ref_point.append((x, y))
                cropping = False
                # draw a rectangle around the region of interest
                cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
                cv2.imshow("image", image)


def get_cropped_image(image_name):

        # load the image, clone it, and setup the mouse callback function
        global crop_img
        global image
        image = cv2.imread(image_name)
        clone = image.copy()
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.setMouseCallback("image", shape_selection)
        # keep looping until the 'q' key is pressed
        while True:
          # display the image and wait for a keypress
          cv2.resizeWindow('image', canvas_size)
          cv2.imshow("image", image)
          key = cv2.waitKey(1) & 0xFF

          # if the 'r' key is pressed, reset the cropping region
          if key == ord("r"):
                image = clone.copy()

          # if the 'c' key is pressed, break from the loop
          elif key == ord("c"):
                break

        # if there are two reference points, then crop the region of interest
        # from the image and display it
        if len(ref_point) == 2:
                crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
                crop_img = cv2.fastNlMeansDenoising(crop_img, None, 9, 13)
                cv2.imshow("crop_img", crop_img)
                #cv2.imwrite(os.path.splitext(image_name)[0]+'_cropped.png', crop_img)
                cv2.waitKey(0)
        # close all open windows
        cv2.destroyAllWindows()
        return crop_img
