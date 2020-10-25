

def setup():
    size(500,500)
    

def draw():
    time = 0
    loadPixels()
    xoff = 0
    
    noiseDetail(20)
    for x in range(width):
        yoff = 0
        for y in range(height):
            bright = map(noise(xoff,yoff), 0, 1, 0, 255)
            pixels[x+y*width] = color(bright)
            yoff += 0.01
        xoff += 0.01
    
    updatePixels()
