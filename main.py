import cv2 as cv
from ui import *
from video_editing import *
from basic_operations import *

def start():
    video_path = File.video_path()
    cap = cv.VideoCapture(video_path)
    fps = get_fps(cap)


    file = File(cap, fps)
    file.play()

app = App()
app.create_button("some", start)
app.create_button("save", )
app.run()



#cap = cv.VideoCapture(File.video_path())
#fps = get_fps(cap)

#file = File(cap, fps)
#file.play()

