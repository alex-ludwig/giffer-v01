import b

b1 = ""
class A():
    
    def __init__(self) -> None:
        print("AAA")
        
        self.b = b.B(self)
        b1 = self.b
        pass
    
    def b2a(self, _from):
        print("B 2 A", _from)
        print(b1)
    
    def a2b(self):
        print("A 2 B")
        self.b.ch()
    
    
a1 = A()
a1.a2b()
a1.b.ch()