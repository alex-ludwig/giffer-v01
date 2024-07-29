import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import os
import sys

# Redirect stderr to /dev/null to suppress macOS specific warnings
sys.stderr = open(os.devnull, 'w')
local = os.getcwd() 


class VideoPlayer:
    def __init__(self, root, video_path):
        self.root = root
        self.video_path = video_path
        self.cap = cv2.VideoCapture(self.video_path)

        if not self.cap.isOpened():
            print("Error: Could not open video file.")
            return

        self.root.title("Video Player")
        self.label = ttk.Label(root)
        self.label.pack()

        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)
            self.root.after(25, self.update_frame)
        else:
            self.cap.release()


root = tk.Tk()
video_path = os.getcwd() + "/assets/ANIME.mp4"  # Replace with your video file path
VideoPlayer(root, video_path)
root.geometry("550x225")
root.mainloop()

print("a")
