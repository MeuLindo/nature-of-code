class Walker(object):
    
    x = 150
    y = 150
    
    def display(self):
        stroke(0)
        point(Walker.x, Walker.y)
    
    def step(self):
        stepx = randomGaussian()
        stepy = randomGaussian()
        
        Walker.x += stepx
        Walker.y += stepy

andador = Walker()

def setup():
    size(300,300)
    background(255)
    
def draw():
    andador.step()
    andador.display()
