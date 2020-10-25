class Walker(object):
    
    x = 300/2
    y = 300/2
    
    def display(self):
        stroke(0)
        point(Walker.x, Walker.y)
    
    def step(self):
        probability = random(1)
        if probability < 0.4:
            Walker.x += 1
        elif probability < 0.6:
            Walker.x -= 1
        elif probability < 0.8:
            Walker.y += 1
        else: 
            Walker.y -= 1

andador = Walker()

def setup():
    size(300,300)
    background(255)
    
def draw():
    andador.step()
    andador.display()
