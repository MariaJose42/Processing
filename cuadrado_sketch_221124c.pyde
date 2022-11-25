def setup():
    size(800,400)
    background(200)
    
def draw():
    clear()
    background(200)
    square(frameCount%800 ,height/2,30)
    
