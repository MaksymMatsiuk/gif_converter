import cv2 as cv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide the main Tkinter window

class UI_Func:
    def path():
            ui_func = UI_Func()
            Tk().withdraw()
            video_path = askopenfilename(title="Select a video file", filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")])
            return video_path