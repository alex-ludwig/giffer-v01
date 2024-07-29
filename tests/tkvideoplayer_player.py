#pip install --only-binary :all: tkvideoplayer
import tkinter as tk
from tkVideoPlayer import TkinterVideo
print("\n##############################\n##############################\n##############################\n")


    

root = tk.Tk()
root.geometry("500x350")

'''videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer.load(r"assets/ANIME.mp4")
videoplayer.pack(expand=True, fill="both")

def video_events_manager(event):
    print("A")
    print(videoplayer.seek)
    

videoplayer.bind("<<Loaded>>", video_events_manager)


#videoplayer.play() # play the video'''
#print(videoplayer.is_paused())

root.mainloop()