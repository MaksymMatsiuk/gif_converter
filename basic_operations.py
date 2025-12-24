import cv2 as cv
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import imageio
import os


class File:
    def __init__(self):
        self.cap = None
        self.fps = None
        self.frames = []
    
    @staticmethod
    def video_path():
        return askopenfilename(title="Select a video file", filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")])

    def open_video(self):
        path = File.video_path()
        if not path:
            return
        
        self.cap = cv.VideoCapture(path)
        self.fps = self.cap.get(cv.CAP_PROP_FPS)
        self.frames = []

    def read_video(self):
        if self.cap is None:
            print("no video opened")
            return

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            self.frames.append(frame)
        self.cap.release()


    def open_in_original_speed(self):
        delay = int(1000/self.fps)
        return delay

    def play(self):
        if not self.frames:
            print("Read video first")
            return
        
        delay = int(1000/self.fps)


        for frame in self.frames:
            cv.imshow("Video", frame)
            if cv.waitKey(int(delay)) & 0xFF == ord('q'):
                break
        cv.destroyAllWindows()

    def save_as_gif(self):
        if not self.frames:
            print("Nothing to save")
            return
        
        path = asksaveasfilename(
            defaultextension=".gif",
            filetypes=[("GIF files", "*.gif")]
        )
        if not path:
            return        

        rgb_frames = [cv.cvtColor(f, cv.COLOR_BGR2RGB) for f in self.frames]
        imageio.mimsave(path, rgb_frames, fps = self.fps)

    
class Folder_Manager:
    pass