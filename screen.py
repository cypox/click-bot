import time
import cv2
import mss
import numpy as np
from pynput.mouse import Button, Controller
from pynput import keyboard


def process(img, mode):
    if mode == 1:
        _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    elif mode == 2:
        img = cv2.Canny(img, 100, 200)
    else:
        pass
    return img


mouse = Controller()


with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 40, "left": 0, "width": 800, "height": 640}
    mode = 3

    while "Screen capturing":
        last_time = time.time()
        # Get raw pixels from the screen, save it to a Numpy array
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)

        img = process(img, mode)

        # Display the picture
        cv2.imshow("OpenCV/Numpy normal", img)

        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        k = cv2.waitKey(10)
        if k & 0xFF == ord("1"):
            mode = 1
        if k & 0xFF == ord("2"):
            mode = 2
        if k & 0xFF == ord("3"):
            mode = 3
        if k & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
