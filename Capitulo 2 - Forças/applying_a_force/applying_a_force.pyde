class Mover(object):
    
    def __init__(self):
        self.location = PVector(random(100),random(100))
        self.velocity = PVector(0,0)
        self.acceleration = PVector(0,0)
        self.topspeed = 1000
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topspeed)
        self.location.add(self.velocity)
        self.acceleration.mult(0)
        
    def applyForce(self, force):
        self.acceleration.add(force)
        
    def display(self):
        stroke(0)
        fill(175)
        ellipse(self.location.x, self.location.y, 16,16)
        
    def checkEdges(self):
        if self.location.x > width-2:
            self.velocity.x *= -1
        elif self.location.x < 2:
            self.velocity.x *= -1
        else:
            pass
        if self.location.y > height-2:
            self.velocity.y *= -1
        elif self.location.y < 2:
            self.velocity.y *= -1
        else:
            pass
        
mover = Mover()
        
def setup():
    size(300,300)
    
def draw():
    background(255)
    
    global mover
    gravidade = PVector(0,0.08)
    mover.applyForce(gravidade)
    
    if mousePressed:
        vento = PVector(0.1, 0)
        mover.applyForce(vento)
    
    mover.update()
    mover.checkEdges()
    mover.display()    
