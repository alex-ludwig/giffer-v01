import customtkinter as ctk
from tkinter import filedialog, TOP, END, ALL
from tkinterdnd2 import TkinterDnD, DND_FILES, DND_ALL


'''
---------------------
 I N P U T   A R E A
--------------------- 
'''

drag_area_text = "Drag and Drop!"
button_area_text = "or Pick Files!"
input_area_color = "#FFF" #["#FFF", "#111"]
entry_area_color = "#E1E1E1" #["#FFF", "#111"]
input_text_color = ("#333", "#000")
class InputWidget(ctk.CTkFrame, TkinterDnD.DnDWrapper):
    
    # Self-Initiate
    def __init__(self, master, **kwargs):
        
        # Initiate CustomTkinter
        super().__init__(master, fg_color=input_area_color, **kwargs) #bg_color="red", fg_color="transparent",
        
        # SET UP
        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure((0,1,2,3,4), weight=1)
        
        # ---------------------------------------------------------
        # TEXT 1
        self.text1 = ctk.CTkLabel(
            self,
            text=drag_area_text,
            text_color=input_text_color).grid(
            row=0,
            column=1,
            pady=5,
            sticky="s")
        
        
        
        # ---------------------------------------------------------
        # DRAG AND DROP
        # setup
        self.entry_widget = ctk.CTkEntry(
            self,
            height=200,
            fg_color=entry_area_color,
            border_color="#DDD")
        self.entry_widget.grid(row=1, column=1, sticky="new")
        self.entry_widget.grid_columnconfigure(0, weight=1)
        self.entry_widget.grid_rowconfigure(0, weight=1)
        
        # functionality
        try:
            
            self.TkdndVersion = TkinterDnD._require(self)
            self.entry_widget.drop_target_register(DND_ALL)
            self.entry_widget.dnd_bind("<<Drop>>", self.drag_and_drop)
        
        except Exception as err:
            print("DnD not ok. Reason:", err)
        
      
        # ---------------------------------------------------------
        # TEXT 2 2    
        self.text2 = ctk.CTkLabel(
            self,
            text=button_area_text,
            text_color=input_text_color).grid(
            row=2,
            column=1,
            sticky="s",
            pady=10)     
            
        # ---------------------------------------------------------
        # BUTTON
        self.button_text = ctk.StringVar(value="Buscar")
        self.file_picker = ctk.CTkButton(
            self,
            corner_radius=10,
            textvariable=self.button_text,
            command=self.file_picker,
            height=40,
            fg_color="#333").grid(
            row=3,
            column=1,
            sticky="new",
            pady=10)
        
        self.loaded = False
    
    # ---------------------------------------------------------
    # DRAG AND DROP RESULTS
    def drag_and_drop(self, event):
        
        if self.loaded == False:
            
            try:
                self.loaded = True
                file_path = event.data
                all_files = self.tk.splitlist(file_path)
                all_names = [get_file_name(i) for i in all_files]
                extension = [get_file_extension(i) for i in all_files]
                self.show_files(all_files, all_names, extension[0])
                
            except Exception as err:
                print("Drag and Drop Error. Reason:", err)
            
            
            
        else:
            try:
                self.restart_all(self)
                self.loaded = False
            except Exception as err:
                print("Restart. Reason:", err)
        
        
    
    # FILE BROWSING RESULTS
    def file_picker(self):
        
        if self.loaded == False:
            try:
                self.loaded = True
                all_files = filedialog.askopenfilenames()
                all_names = [get_file_name(_file) for _file in all_files]
                extension = [i[-4:] for i in all_files]
                self.show_files(all_files, all_names, extension[0])
                
            except Exception as err:
                print("File Picker Error. Reason:", err)
        else:
            self.loaded = False
            self.restart_all()
            print("Ready for new files\n\n\n" + "----"*5)
    
    
    
    # ------------------------------------------------------------------------------------
    def show_files(self, paths, files, extension):
        
        self.result_box = ctk.CTkTextbox(
            self.entry_widget,
            width=0,
            height=0,
            bg_color="transparent",
            fg_color="transparent",
            text_color=input_text_color)
        
        self.result_box.insert("0.0",text="\n".join(files))
        self.result_box.grid(row=0, column=0, sticky="nsew")
        self.result_box.configure(state="disabled")
        
        self.button_text.set(value="Recomeçar")
        
        try:
            self.master.adjust_output(paths, files, extension)
            
        except Exception as err:
            print("show_files not ok", err)
    
    # ------------------------------------------------------------------------------------------
    def restart_all(self):
        
        try:
            self.result_box.grid_remove()
            self.result_box.configure(state="normal")
            self.result_box.delete("1.0",END)
            self.result_box.grid(row=0, column=0, sticky="nsew")
            
            self.button_text.set(value="Buscar")

        except Exception as err:
            print("restart_all not ok", err)



# EXTRA
def get_file_name(name_path):
    
    # gets the last "/" in the name_path
    _last = [i for i in range(len(name_path)) if name_path[i] == "/"][-1]
    _in = _last + 1
    #returns the slice of the name
    return name_path[_in:]



def get_file_extension(file_path):
    return file_path[-4:]