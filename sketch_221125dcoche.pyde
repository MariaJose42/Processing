class coche:
    def __init__(self, pos_x,pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def actualiza(self, teclaPulsada):
        if(self.pos_y == height):
            self.pos_y= height
        elif(self.pos_y == 0):
            self.pos_y= 0
        if(self.pos_y == height):
            self.pos_y= height
        if(self.pos_y == height):
            self.pos_y= height
            
            
        print(teclaPulsada)
        if(teclaPulsada==38):
            self.pos_y = self.pos_y - 1                
        elif(teclaPulsada == 40):
            self.pos_y = self.pos_y + 1             
        elif(teclaPulsada == 39):
            self.pos_x = self.pos_x + 1
        elif(teclaPulsada == 37):
            self.pos_x = self.pos_x - 1
            
    def mostrar(self):
        square(self.pos_x , self.pos_y , 20)
        

            
        

c1= coche(10,10)

def setup():
    size(800,400)
    print("width:",width)
    print("height:", height)
    
def draw():
    clear()
    background(125)
    c1.actualiza(keyCode)
    c1.mostrar()
    c1.rebota()
