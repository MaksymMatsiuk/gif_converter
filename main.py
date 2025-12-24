import cv2 as cv
from ui import *
from video_editing import *
from basic_operations import *


#video_path = File.video_path()
#cap = cv.VideoCapture(video_path)
#fps = get_fps(cap)


file = File()

app = App()
app.create_button("open", file.open_video)

app.create_button("read", file.read_video)
app.create_button("play", file.play)
app.run()



#cap = cv.VideoCapture(File.video_path())
#fps = get_fps(cap)

#file = File(cap, fps)
#file.play()

