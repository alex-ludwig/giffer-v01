import customtkinter as ctk
from PIL import Image, ImageTk

header_background_color = "#DDD"#["#DDD", "#111"]
logo_link = 'assets/logo.png'
logo_text = "Giffer"
logo_size_tuple = (100,100)

class HeaderWidget(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        
        super().__init__(master, fg_color=header_background_color, **kwargs)
        
        # add widgets onto the frame...
        self.grid_columnconfigure(0, weight=1)
        
        #logo_text_label = ctk.CTkLabel(self, text=logo_text)#, font=("serif", "20 bold"))
        #logo_text_label.grid(row=0, column=0, sticky="nsew")
        
        logo_image = Image.open(logo_link)
        logo = ctk.CTkImage(logo_image, size=logo_size_tuple)
        logo_holder = ctk.CTkLabel(self, image=logo, text="").grid(row=0, column=0, sticky="nsew")
        #print("a")