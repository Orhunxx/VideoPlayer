from tkinter import filedialog
from tkinter import *
import cv2 as cv
import tkinter

def rescaleFrame(frame, scale= 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture("videos/MRV_20181124_18_53_30.mp4 ")

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow("Video", frame_resized)

    if cv.waitKey(20) & 0xFF==ord("d"):
        break


capture.release()
cv.destroyAllWindows()