x=500
y=400
ysp=0
grav=0.1
jump=True
dp=0
def setup():
    size(1000,800)
def draw():
    global x,y,ysp,grav,jump,pr,dp
    rect (x,y,50,50)
    ysp=ysp+grav
    y=y+ysp
    if y > height:
        y = height
        ysp=0
        jump=False
        dp=1
    if keyPressed == True:
        if key =="w" and not jump:
            if jump
