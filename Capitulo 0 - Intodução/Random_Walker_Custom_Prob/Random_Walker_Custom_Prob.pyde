class Walker(object):
    
    x = 150
    y = 150
    
    def display(self):
        stroke(0)
        point(Walker.x, Walker.y)
    
    def step(self):
        
        stepsize = random(1)
        prob = stepsize
        qualifier = random(1)
        if qualifier < prob:        
            Walker.x += random(-stepsize, stepsize)
            Walker.y += random(-stepsize, stepsize)
            print(Walker.x)
            print(Walker.y)

andador = Walker()

def setup():
    size(300,300)
    background(255)
    
def draw():
    andador.step()
    andador.display()
