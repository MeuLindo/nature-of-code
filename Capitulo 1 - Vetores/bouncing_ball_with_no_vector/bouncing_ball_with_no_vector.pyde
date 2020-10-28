x = 100
y = 100
xspeed = 1
yspeed = 3.3

def setup():
    size(640, 360)
    background(255)
    
def draw():
    background(255)
    global x, y, xspeed, yspeed
    
    x += xspeed
    y += yspeed
    
    if (x > width) or (x < 0):
        xspeed *= -1
    if (y > height) or (y < 0):
        yspeed *= -1
    
    stroke(0)
    fill(175)
    ellipse(x,y,16,16)
