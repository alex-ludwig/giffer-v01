import contextlib
from tkinter import filedialog
from PIL import Image
import os

class ExportToGif():
    
    def __init__(self):
        pass
    
    #def export(self, folder, array, path='example.gif', duration=50):
    def export(self, array, extension, gif_properties, frame_duration=50):
        
        #gif_filename = gif_properties["filename"]

        # use exit stack to automatically close opened images
        try:
            with contextlib.ExitStack() as stack:

                # lazily load images
                all_images = (stack.enter_context(Image.open(image_file))
                        for image_file in array)

                # extract  first image from iterator
                image_sequence = next(all_images)

                # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
                file_dialog = filedialog.asksaveasfile(
                    mode='w',
                    defaultextension=".gif",
                    initialdir=os.getcwd(),
                    initialfile=gif_properties["filename"])
                
                if file_dialog:
                    #im.save(file) # saves the image to the input file name. 
                    image_sequence.save(
                        fp=gif_properties["filename"],
                        format='GIF',
                        append_images=all_images,
                        save_all=True,
                        duration=gif_properties["duration"],
                        loop=0)
            
            
                    print("exported!")
                
        except Exception as err:
            print("Gif Export Error:",err)
        
