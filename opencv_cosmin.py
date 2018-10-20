import cv2
import sys
import numpy as np

kernel = np.ones((3, 3), np.uint8)
target_array = [[1, 0, -1], [0, 0, 0], [-1, 0, 1]]
for i, line in enumerate(target_array):
    for j, el in enumerate(line):
        kernel[i][j] = np.uint8(el)

camera = cv2.VideoCapture('http://192.168.1.143:8080/stream/video.mjpeg')
while camera.isOpened():

    retval, im = camera.read()
    overlay = im.copy()
    img_thresholded = cv2.inRange(overlay, (60, 60, 60), (120, 120, 120))
    opening = cv2.morphologyEx(img_thresholded, cv2.MORPH_OPEN, kernel)
    cv2.imshow('gray_image.png', opening)
    opening= (255-opening)
    im2, contours, hierarchy = cv2.findContours(opening.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)
        cv2.circle(im, center, radius, (0, 255, 0), 2)
        # labelling the circles around the centers, in no particular order.
        i = 0
        position = (center[0] - 10, center[1] + 10)
        text_color = (0, 0, 255)
        cv2.putText(im, "hole", position, cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 3)
        cv2.imshow("Output", im)
        opacity = 0.5
        cv2.addWeighted(overlay, opacity, im, 1 - opacity, 0, im)

        # Uncomment to resize to fit output window if needed
        # im = cv2.resize(im, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
        cv2.imshow("Output", im)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

camera.release()
cv2.destroyAllWindows()
