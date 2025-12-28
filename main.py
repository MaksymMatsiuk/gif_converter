import cv2 as cv
from ui import *
from basic_operations import *

file = File()

app = App()
app.create_button("open", file.open_video)
app.create_button("play", file.play)
app. create_button("save", file.save_as_gif)
app.run()

