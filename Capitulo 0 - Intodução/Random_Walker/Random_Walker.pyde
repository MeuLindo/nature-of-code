class Walker(object):
    
    x = 300
    y = 300
    
    def display(self):
        stroke(0)
        point(Walker.x, Walker.y)
    
    def step(self):
        stepx = int(random(3))-1
        stepy = int(random(3))-1
        
        Walker.x += stepx
        Walker.y += stepy

andador = Walker()

def setup():
    size(300,300)
    background(255)
    
def draw():
    andador.step()
    andador.display()
