import cv2 as cv
from ui import *
from video_editing import *
from basic_operations import *

cap = cv.VideoCapture(video_path())
fps = get_fps(cap)

file = File(cap, fps)
file.play()
