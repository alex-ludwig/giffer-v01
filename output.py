import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import Canvas
from tkvideo import tkvideo
import os
import sys
import export_to_gif

# Redirect stderr to /dev/null to suppress macOS specific warnings
sys.stderr = open(os.devnull, 'w')
local = os.getcwd() 

'''
-----------------------
 O U T P U T   A R E A
-----------------------
'''  

output_area_color = "#FFF" #["#FFF", "#111"]
output_text = "File Manager"
output_text_color = ("#333", "#000")

to_gif = export_to_gif.ExportToGif()

class OutputWidget(ctk.CTkFrame):
    
    def __init__(self, master, **kwargs):
        
        super().__init__(master, fg_color=output_area_color, **kwargs) #bg_color="blue", fg_color="transparent",  
        
        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure((0,1,2,3), weight=1)
        
        self.label = ctk.CTkLabel(
            self,
            text="File Manager",
            text_color=output_text_color).grid(
            row=0,
            column=1,
            sticky="new")
        
        self.canvas = Canvas(self, bg="#E1E1E1", highlightthickness=0)
        self.canvas.grid(row=2, column=0, padx=10, pady=10, columnspan=3, sticky="n")
        #print("Output Ready")
        
        self.control_frame = ctk.CTkFrame(
            self,
            bg_color="#333",
            height=40,
            corner_radius=10
            )
        self.control_frame.grid(row=3, column=0, padx=10, pady=10, columnspan=3, sticky="new")
        
    def set_result(self, paths, files, extension, gif_properties):
        
        print("setting up results\n\n")
        
        if extension != ".mp4": 
            extra = f"Image Sequence - Extension: [{extension}]"
        else: 
            extra = "Video to Gif"
        
        #self.extension_box.insert("0.0", text=extra)
        self.show_image(paths, files, extension)
        to_gif.export(paths, extension, gif_properties)
        


    '''
    - Show image or video. 
    - If Video, ideally the player...
    - If image sequence, ideally check all images (play or seek)

    VIDEO? 
        - Player
        - Check/Change: Speed, FPS, In, Out
        
    IMAGE? 
        - "Player"
        - Check/Change" Speed, keyframes, 
        
    - Export
    - Restart
    
    - Logo, Branding..
    - Make it a SOFTWARE
    
    '''
    def show_image(self, paths, files, extension):
        
        #print(extension)
        if extension != ".mp4":
            
            try:
                image_file = Image.open(paths[0])
                
                image_width = image_file.size[0]
                image_height = image_file.size[1]
                image_aspect_ratio = int(image_width)/int(image_height)
                
                canvas_width = int(self.canvas.winfo_reqwidth())
                canvas_height = int(self.canvas.winfo_reqheight())
                canvas_width_end = canvas_width
                
                #print(canvas_width, canvas_height)
                if image_height > canvas_width:
                    canvas_width_end = canvas_height
                    
                canvas_height_end = int(canvas_width_end*image_aspect_ratio)
                new_size = (canvas_width_end, canvas_height_end)
                #print(new_size)
                
                
                image_file = image_file.resize(size=(canvas_width_end, canvas_height_end), resample=Image.Resampling.LANCZOS)
                image_asset = ImageTk.PhotoImage(image_file)
                self.image_asset = image_asset
                self.canvas.create_image(canvas_width/2, canvas_height/2, anchor="center" , image=image_asset)
                self.canvas.configure(background="#FFF")
                self.canvas.update()
                
                
            
                
                
            except Exception as err:
                print("image not ok", err)
                
                
            
            # image_holder = ctk.CTkLabel(self.canvas, image=imagetk, text="")
            # image_holder.grid(row=1, column=0, sticky="nsew")
            
        else:
            
            try:
                player = tkvideo(paths[0], files[0], label="video_label", loop = 1, size = (640,460))
                print("video\n\n\n")
            except Exception as err:
                print("video not ok", err)
            