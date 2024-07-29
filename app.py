import os, sys
import customtkinter as ctk
import footer, header, input, output
import random

# Redirect stderr to /dev/null to suppress macOS specific warnings
sys.stderr = open(os.devnull, 'w')


'''
G I F F E R   A P P
v0.1

'''
ctk.set_appearance_mode("System")
a = random.randint(0,1000)

# SET TO BE DONE VIA UI!!!!!
gif_properties = {
    "duration":1000, 
    "filename":f"image{a}.gif"}

class App(ctk.CTk):
    
    def __init__(self, name, w, h, *args, **kwargs):
        
        print("\n" + "##############################"*3+"\n")
        super().__init__(fg_color="#DDD")
        print("\n" + "##############################"*3+"\n")

        self.title(name)
        self.geometry(str(w)+ "x" + str(h))
       
        self.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1)
        self.grid_columnconfigure((0,1,2,3), weight=1)
        
        # SET UP ------------------------------------------------
        try:
            # HEADER
            self.app_header = header.HeaderWidget(self)
            self.app_header.grid(
                row=0,
                column=0,
                pady=(10,0),
                padx=20,
                sticky="new",
                columnspan=7)
        
            # MAIN PART
            self.app_input = input.InputWidget(self)
            self.app_input.grid(
                row=1,
                column=0,
                padx=(20,10),
                pady=20,
                sticky="nsew",
                columnspan=3,
                rowspan=6)
            
            self.app_output = output.OutputWidget(self)
            self.app_output.grid(
                row=1,
                column=3,
                padx=(10,20),
                pady=20,
                sticky="nsew",
                columnspan=1,
                rowspan=6)
            
            # FOOTER
            self.app_footer = footer.FooterWidget(self)
            self.app_footer.grid(
                row=7,
                column=0,
                padx=0,
                sticky="sew",
                columnspan=7,
                rowspan=2)
            
        except Exception as err:
            print("Cannot build. Reason:", err)

       
    # -----------------------------------------------
    def adjust_output(self, paths, files, extension):
        
        try:
            self.app_output.set_result(paths, files, extension, gif_properties)
            #print("Send to Output", paths, files, extension)
            
            #app.app_output.set_result(paths, files, extension)
        except Exception as err:
            print("adjust_output. Reason:", err)

            

app = App("Giffer v0.1", 800, 550)
app.mainloop()

