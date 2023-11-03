from abc import ABC,abstractmethod

class app(ABC):
    @abstractmethod
    def chat(self):
        pass
    
    def abs(self):
        print("non abstract method")
        
class whatsapp(app):
    def chat(self):
        print("hi whatsapp")
        
class instagram(app):
    def chat(self):
        print("hi insta")
        
class X(app):
    def chat(self):
        print("hi X")
        
w=whatsapp()
w.abs()
w.chat()

i=instagram()
i.chat()

x=X()
x.chat()
