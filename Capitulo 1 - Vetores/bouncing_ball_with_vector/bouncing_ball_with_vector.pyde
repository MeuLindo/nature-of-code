location = PVector(100,100)
velocity = PVector(1, 10)

def setup():
    size(640, 360)
    
    
def draw():
    background(255)
    global location, speed    
    
    location.add(velocity)
    if (location.x > width) or (location.x < 0):
        velocity.x *= -1
    if (location.y > height) or (location.y < 0):
        velocity.y *= -1
        
    stroke(0)
    background(175)
    ellipse(location.x, location.y, 50,50)
