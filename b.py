import c

class B(c.C):
    
    def __init__(self, master, **kwargs):
        print("BBB")
        super().__init__() #bg_color="blue", fg_color="transparent", 
        
        #super().__init__(self, master) #bg_color="blue", fg_color="transparent",  
        print("B", master)
        self.name = "BBB"
        master.b2a(self.name)
        pass
    
    def ch(self):
        print("bbbbbbb")