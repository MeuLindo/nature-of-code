class Mover(object):
    
    def __init__(self):
        self.location = PVector(random(50,200),random(50,200))
        self.velocity = PVector(0,0)
        self.acceleration = PVector(0,0)
        self.mass = random(1,3)
        self.topspeed = 1000
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topspeed)
        self.location.add(self.velocity)
        self.acceleration.mult(0)
        
    def applyForce(self, force):
        f = PVector.div(force,self.mass)
        self.acceleration.add(f)
        
    def display(self):
        stroke(0)
        fill(175)
        ellipse(self.location.x, self.location.y, self.mass*20,self.mass*20)
        
    def checkEdges(self):
        if self.location.x + (self.mass*20) >= width:
            self.velocity.x *= -1
        elif self.location.x - (self.mass*20) <= 0.0:
            self.velocity.x *= -1
        else:
            pass
        if self.location.y + (self.mass*20) >= height:
            self.velocity.y *= -1
        elif self.location.y - (self.mass*20) <= 0.0:
            self.velocity.y *= -1
        else:
            pass
        
movers = [Mover() for i in range(10)]

def setup():
    size(300,300)
    
    
def draw():
    background(255)
    
    global movers
    for mover in movers:
    
        gravidade = PVector(0,0.08)
        mover.applyForce(gravidade)
        
        if mousePressed:
            vento = PVector(0.1, 0)
            mover.applyForce(vento)
    
        mover.update()
        mover.checkEdges()
        mover.display()    
