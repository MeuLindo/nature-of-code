randomCounts = [0 for x in range(1,101)]

def setup():
    size(1000,240)
    
    
def draw():
    background(255)
    index = int(random(len(randomCounts)))
    randomCounts[index] += 1
    
    stroke(0)
    fill(175)
    w = width/len(randomCounts)
    
    for i in range(0, len(randomCounts)):
        rect(i*w, height-randomCounts[i], w, randomCounts[i])
    
