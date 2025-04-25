import cv2 as cv
# library to use `getbbox()` to find bounding boxes.
from PIL import Image

from util import get_limits

# color to be picked in BGR. (yellow)
yellowcolor = [0, 255, 255] 

# get feed from default webcam
cap = cv.VideoCapture(0)

while True:
    # get the frame
    ret, frame = cap.read() 
    # convert to HSV colorspace
    hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    #get the HSV threshold ranges
    lowerLimit, upperLimit = get_limits(yellowcolor)
    # binary image where yellow objects are white blobs.
    mask = cv.inRange(hsvImage, lowerLimit, upperLimit)

    # simpler way to extract the bounding box using Pillow
    # alternative for OpenCV’s  (cv2.boundingRect)
    mask_ = Image.fromarray(mask)
    # Returns (x1, y1, x2, y2) or `None` if no object found
    # (x1, y1): Top-left corner of the box.
    # (x2, y2): Bottom-right corner.
    bbox = mask_.getbbox()

    # draw a green rectangle around the detected area.
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # show current frame
    cv.imshow('frame', frame)

    # wating one millisecond between frames and breaking the loop if q is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    
cap.release()
    
cv.destroyAllWindows()