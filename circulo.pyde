#mouseX
#mouseY

def setup():
    size(400,400)
    #RGB - RED - GREEN - BLUE
    #background(125)
    
def draw():
    clear()
    rojo= random(0,255)
    verde= random(0,255)
    azul= random(0,255)
    
    #background(rojo,verde,azul)
    background(frameCount%255)
    
    if((mouseX< 200) and (mouseY<200)):
        fill(0,0,255)
    elif((mouseX>200) and (mouseY<200)):
        fill(0,255,0)
    elif((mouseX>200) and (mouseY>200)):
        fill(255,0,0)
    elif((mouseX<200) and (mouseY>200)):
        fill(0)
        
    #ellipse(mouseX,mouseY,50,50)
    square(mouseX,mouseY,60)
