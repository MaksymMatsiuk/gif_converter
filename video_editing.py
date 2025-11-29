import cv2 as cv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()

def get_all_video_properties(cap):
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv.CAP_PROP_FPS)

    return width, height, fps

def get_fps(cap):
    fps = cap.get(cv.CAP_PROP_FPS)
    return fps

def open_in_original_speed(fps):
    delay = int(1000/fps)
    return delay