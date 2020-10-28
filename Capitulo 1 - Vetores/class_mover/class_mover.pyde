class Mover(object):
    
    def __init__(self):
        self.location = PVector(random(100),random(100))
        self.velocity = PVector(random(-2,2), random(-2,2))
    
    def update(self):
        self.location.add(self.velocity)
        
    def display(self):
        stroke(0)
        fill(175)
        ellipse(self.location.x, self.location.y, 16,16)
        
    def checkEdges(self):
        if self.location.x > width:
            self.location.x = 0
        elif self.location.x < 0:
            self.location.x = width
        else:
            pass
        if self.location.y > height:
            self.location.y = 0
        elif self.location.y < 0:
            self.location.y = height
        else:
            pass
        
mover = Mover()
        
def setup():
    size(300,300)
    
def draw():
    background(255)
    
    global mover
    mover.update()
    mover.checkEdges()
    mover.display()    
