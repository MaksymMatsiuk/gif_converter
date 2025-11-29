import cv2 as cv
from tkinter.filedialog import askopenfilename
import imageio

class File:
    def __init__(self, cap, fps):
        self.cap = cap
        self.fps = fps
        self.frames = []

    def open_in_original_speed(self):
        delay = int(1000/self.fps)
        return delay
    
    def play(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            self.frames.append(frame)
            cv.imshow("Video", frame)
            if cv.waitKey(self.open_in_original_speed()) & 0xFF == ord('q'):
                break
        
        self.cap.release()
        cv.destroyAllWindows()

    def save_as_gif(self, path):
        rgb_frames = [cv.cvtColor(f, cv.COLOR_BGR2RGB) for f in self.frames]
        imageio.mimsave(path, rgb_frames, fps = self.fps)

    
