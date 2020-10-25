
        

andador = Walker()

def setup():
    size(1366,768)
    background(255)
    
def draw():
    andador.step()
    andador.display()
    
    
    
class Walker(object):

x = width/2
y = height/2
tx = 0
ty = 10000

def display(self):
    stroke(0)
    point(self.x, self.y)

def step(self):
    
    self.x = map(noise(self.tx), 0, 1, 0, 300)
    self.y = map(noise(self.ty), 0, 1, 0, 300)
    print(self.x)
    print(self.y)
    self.tx += 0.01
    self.ty += 0.01
