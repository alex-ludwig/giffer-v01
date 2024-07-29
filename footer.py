import customtkinter as ctk
import webbrowser

# MAIN SETUP
footer_background_color = ["#333", "#111"]
footer_text_color = "#666"
footer_text = "Feito por Alex Ludwig"
footer_url = "https://www.alexludwig.com.br"
footer_hover_color = "#333"

class FooterWidget(ctk.CTkFrame):
    
    def __init__(self, master, **kwargs):
        
        super().__init__(master, fg_color=footer_background_color, **kwargs)

        # self == footer itself
        #self.grid(row=7, column=0, padx=0, sticky="nsew", columnspan=7, rowspan=2)
        self.grid_columnconfigure(0, weight=1)
        
        footer_link = ctk.CTkButton(
            self,
            text=footer_text,
            text_color=footer_text_color,
            hover_color=footer_hover_color,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=0,
            height=40,
            command=self.get_url
        ).grid(row=0, column=0, sticky="nsew")
        
    def get_url(self):
        webbrowser.open(footer_url)
        #return "as"