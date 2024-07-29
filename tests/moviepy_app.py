import tkinter as tk
from tkinter import ttk
from tkvideo import tkvideo
from moviepy.editor import *

print("##############################\n##############################\n##############################\n")

win = tk.Tk()
win.geometry("500x350")

video_frame = ttk.Frame(master=win, width=400, height=200)
video_frame.pack()

video_holder = ttk.Label(master=video_frame, foreground="#333", text="Hey")
video_holder.pack()






video_file = VideoFileClip("assets/ANIME.mp4")
#video_file = "assets/ANIME.mp4"
video_duration = video_file.duration
print(video_duration)
video_fps = video_file.fps
video_file = video_file.subclip(0, 0.1)

player = tkvideo.TkVideo(video_file, video_holder, loop = 0, size = (400,200))
player.play()





# Make the text. Many more options are available.
'''
txt_clip = ( TextClip("My Holidays 2013",fontsize=70,color='white')
             .set_position('center')
             .set_duration(10) )
'''
#result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
#result.write_videofile("myHolidays_edited.webm",fps=25)
win.mainloop()