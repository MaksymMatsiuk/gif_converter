import tkinter as tk
from basic_operations import *

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main window")
        self.root.geometry("400x300")

    def run(self):
        self.root.mainloop()

    def create_button(self, text, command):
        button = tk.Button(self.root, text=text, command=command)
        button.pack(pady=5)

