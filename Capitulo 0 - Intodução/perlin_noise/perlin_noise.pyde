def setup():
    size(500,500)

def draw():
    t = 0
    while(True):
        background(0)
        n = noise(t)
        x = map(n, 0, 1, 0, width)
        fill(255)
        ellipse(x, 180, 16, 16)
        
        t += 0.01
