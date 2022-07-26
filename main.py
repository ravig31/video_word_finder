import imghdr
import cv2 as cv
import numpy as np
from time import time
from windowcapture import WindowCapture
import textreader

screencap = WindowCapture("(82) Singing and Racing to ACCEPT match! #LOL #leagueoflegends - YouTube - Google Chrome")

time_loop = time()
while(True):

    screenshot = screencap.get_screenshot()
    
    cv.imshow("Computer Vision", screenshot)
    textreader.img_read_text(screenshot)

    print("FPS {}".format(1 / (time() - time_loop)))
    time_loop = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print("Done.")




