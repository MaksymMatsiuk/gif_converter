import tkinter as tk
from basic_operations import *

root = tk.Tk()
root.title("Main window")
root.geometry("400x300")

button_select = tk.Button(root, text="Select video", command= File.video_path())
button_select.pack(pady=10)


root.mainloop()

