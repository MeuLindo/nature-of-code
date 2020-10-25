
def setup():
    size(640,360)
    
    
def draw():
    num = randomGaussian()
    print(num)
    sd = 60
    mean = 320
    x = sd * num + mean
    
    noStroke()
    fill(x/2, x/3, x/4, 10)
    ellipse(x, x/2, 16, 16)
