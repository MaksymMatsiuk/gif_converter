import cv2 as cv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide the main Tkinter window
Tk().withdraw()

# Open file dialog to select video
def video_path():
    video_path = askopenfilename(title="Select a video file", filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")])
    return video_path

