windowwidth = 840
windowheight = 400
pitchwidth = 640
pitchheight = 260
goalsize = 110

import pygame

pygame.init()
import numpy as np
win = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption("ball")

clock = pygame.time.Clock()


font = pygame.font.Font(None, 50)

playerradius = 15
playerbouncing = 0.5
playerinvmass = 0.5
playerdamping = 0.96
accel = 0.1
kickaccel = 0.07
kickstrength = 5

ballradius = 10
balldamping = 0.99
ballinvmass = 1
ballbouncing = 0.5

redstart = (200, 200)
pinkstart = (640, 200)
ballstart = (420, 200)
goalpostradius = 8
goalpostbouncingquotient = 0.5
goallinethickness = 3
kickingcircleradius = 15
kickingcirclethickness = 2

redcolour = (255, 0, 0)
pinkcolour = (255, 0, 255)
ballcolour = (0, 0, 0)
goallinecolour = (199, 230, 189)
goalpostcolour = (150, 150, 150)
pitchcolour = (127, 162, 112)
bordercolour = (113, 140, 90)
kickingcirclecolour = (255, 255, 255)

centrecircleradius = 70
centrecirclecolour = (199, 230, 189)
centrecirclethickness = 3
centrelinethickness = 3

textcolour = (0, 0, 0)
textposition = (215, 25)


pitchcornerx = int(np.floor((windowwidth - pitchwidth)/2))
pitchcornery = int(np.floor((windowheight - pitchheight)/2))


goalcornery = int(np.floor((windowheight - goalsize)/2))
y1 = pitchcornerx - 30

z1 = pitchcornerx + pitchwidth
z2 = goalcornery

a1 = y1 + 2*ballradius
a2 = int(np.floor(goalcornery-goallinethickness/2))

b1 = z1
b2 = int(np.floor(goalcornery-goallinethickness/2))

movespacex = [playerradius, windowwidth - playerradius]
movespacey = [playerradius, windowheight - playerradius]

ballspacex = [pitchcornerx + ballradius, pitchcornerx + pitchwidth - ballradius]
ballspacey = [pitchcornery + ballradius, pitchcornery + pitchheight - ballradius]
goaly = [goalcornery, goalcornery + goalsize]

class player(object):
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.xint = x
        self.yint = y
        self.colour = colour
        self.xacc = 0
        self.yacc = 0
        self.kicking = False
        self.accelaration = accel
        self.velocity = np.array([0, 0])
        self.speed = 0
        self.kicking = False
        self.kickdirection = [0, 0]
        self.distancetoball = 100
        self.bouncingquotient = playerbouncing
        self.radius = playerradius

    def draw(self, win):
        pygame.draw.circle(win, self.colour, (self.xint, self.yint), playerradius)

class ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xint = x
        self.yint = y
        self.velocity = [0, 0]
        self.xacc = 0
        self.yacc = 0
        self.bouncingquotient = ballbouncing
        self.radius = ballradius
        self.speed = 0

    def draw(self, win):
        pygame.draw.circle(win, (255, 255, 255), (self.xint, self.yint), ballradius)

class goalpost(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bouncingquotient = goalpostbouncingquotient
        self.velocity = [0, 0]
        self.radius = goalpostradius

    def draw(self, win):
        pygame.draw.circle(win, goalpostcolour, (self.x, self.y), goalpostradius)

def redrawgamewindow():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, bordercolour, (0, 0, windowwidth, windowheight))
    pygame.draw.rect(win, pitchcolour, (pitchcornerx, pitchcornery, pitchwidth, pitchheight))
    pygame.draw.rect(win, pitchcolour, (pitchcornerx - 30, goalcornery, 30, goalsize))
    pygame.draw.rect(win, pitchcolour, (windowwidth - pitchcornerx, goalcornery, 30, goalsize))
    pygame.draw.rect(win, goallinecolour, (pitchcornerx - goallinethickness // 2, pitchcornery - goallinethickness // 2, goallinethickness, pitchheight + goallinethickness))
    pygame.draw.rect(win, goallinecolour, (windowwidth- pitchcornerx - goallinethickness // 2, pitchcornery - goallinethickness // 2, goallinethickness, pitchheight + goallinethickness))
    pygame.draw.rect(win, goallinecolour, (pitchcornerx - goallinethickness // 2, pitchcornery - goallinethickness // 2, pitchwidth + goallinethickness, goallinethickness))
    pygame.draw.rect(win, goallinecolour, (pitchcornerx - goallinethickness // 2, windowheight - pitchcornery - goallinethickness // 2, pitchwidth + goallinethickness, goallinethickness))

    pygame.draw.ellipse(win, centrecirclecolour, (ballstart[0] - centrecircleradius, ballstart[1] - centrecircleradius, 2*centrecircleradius, 2*centrecircleradius), centrecirclethickness)
    pygame.draw.rect(win, centrecirclecolour, (windowwidth // 2 - centrelinethickness // 2, pitchcornery, centrelinethickness, pitchheight))

    red.draw(win)
    pink.draw(win)
    b.draw(win)
    redgoalpost1.draw(win)
    redgoalpost2.draw(win)
    pinkgoalpost1.draw(win)
    pinkgoalpost2.draw(win)

    if red.kicking == True:
        pygame.draw.ellipse(win, kickingcirclecolour, (red.x - kickingcircleradius, red.y - kickingcircleradius, 2*kickingcircleradius, 2*kickingcircleradius), kickingcirclethickness)
    else:
        pygame.draw.ellipse(win, (0, 0, 0), (red.x - kickingcircleradius, red.y - kickingcircleradius, 2*kickingcircleradius, 2*kickingcircleradius), kickingcirclethickness)
    if pink.kicking == True:
        pygame.draw.ellipse(win, kickingcirclecolour, (pink.x - kickingcircleradius, pink.y - kickingcircleradius, 2*kickingcircleradius, 2*kickingcircleradius), kickingcirclethickness)
    else:
        pygame.draw.ellipse(win, (0, 0, 0), (pink.x - kickingcircleradius, pink.y - kickingcircleradius, 2*kickingcircleradius, 2*kickingcircleradius), kickingcirclethickness)

    pygame.draw.ellipse(win, (0, 0, 0,), (b.x - ballradius, b.y - ballradius, 2 * ballradius, 2 * ballradius), 2)

    string = str(redscore) + ":" + str(pinkscore)
    text = font.render(string, True, (255, 255, 255))
    win.blit(text, (215, 25))
    pygame.display.update()

def collision(obj1, obj2):
    bouncingq = obj1.bouncingquotient * obj2.bouncingquotient
    collisionnormal = np.array([obj1.x - obj2.x, obj1.y - obj2.y]) / (np.linalg.norm([obj1.x - obj2.x, obj1.y - obj2.y]))
    collisiontangent = np.array([obj1.y - obj2.y, - (obj1.x - obj2.x)]) / (np.linalg.norm([obj1.x - obj2.x, obj1.y - obj2.y]))
    obj1component = np.dot(np.array(obj1.velocity), collisionnormal)
    obj2component = np.dot(np.array(obj2.velocity), collisionnormal)
    velocityafter = (obj1component + obj2component)*bouncingq*2
    obj1tangentvelocity = np.dot(np.array(obj1.velocity), collisiontangent)
    obj2tangentvelocity = np.dot(np.array(obj2.velocity), collisiontangent)
    obj1.velocity = velocityafter * np.array(collisionnormal) + obj1tangentvelocity * np.array(collisiontangent)
    obj2.velocity = velocityafter * np.array(collisionnormal) + obj2tangentvelocity * np.array(collisiontangent)
    obj2.x = obj1.x - collisionnormal[0]*(obj1.radius + obj2.radius + 1)
    obj2.y = obj1.y - collisionnormal[1]*(obj1.radius + obj2.radius + 1)

def collisiongoalpost(obj1, obj2):
    bouncingq = obj1.bouncingquotient * obj2.bouncingquotient
    collisionnormal = np.array([obj1.x - obj2.x, obj1.y - obj2.y]) / (np.linalg.norm([obj1.x - obj2.x, obj1.y - obj2.y]))
    collisiontangent = np.array([obj1.y - obj2.y, - (obj1.x - obj2.x)]) / (np.linalg.norm([obj1.x - obj2.x, obj1.y - obj2.y]))
    obj1component = np.dot(np.array(obj1.velocity), collisionnormal)
    obj2component = np.dot(np.array(obj2.velocity), collisionnormal)
    velocityafter = (obj1component + obj2component)*bouncingq*2
    obj1tangentvelocity = np.dot(np.array(obj1.velocity), collisiontangent)
    obj2tangentvelocity = np.dot(np.array(obj2.velocity), collisiontangent)
    obj1.velocity = - velocityafter * np.array(collisionnormal) + obj1tangentvelocity * np.array(collisiontangent)
    obj2.velocity = velocityafter * np.array(collisionnormal) + obj2tangentvelocity * np.array(collisiontangent)
    obj2.x = obj1.x - collisionnormal[0]*(obj1.radius + obj2.radius + 1)
    obj2.y = obj1.y - collisionnormal[1]*(obj1.radius + obj2.radius + 1)

def kick(obj1, ball):
    kickdirection = np.array([ball.x - obj1.x, ball.y - obj1.y]) / (np.linalg.norm([ball.x - obj1.x, ball.y - obj1.y]))
    ball.velocity = np.array(ball.velocity) + kickstrength * ballinvmass * kickdirection

def goal(red, pink, b, redscore, pinkscore):
    if b.x <= a1:
        pinkscore += 1
        red.x = redstart[0]
        red.y = redstart[1]
        pink.x = pinkstart[0]
        pink.y = pinkstart[1]
        b.x = ballstart[0]
        b.y = ballstart[1]
        b.velocity = np.array([0, 0])
        red.velocity = np.array([0, 0])
        pink.velocity = np.array([0, 0])
    elif b.x >= b1 + 5:
        redscore += 1
        red.x = redstart[0]
        red.y = redstart[1]
        pink.x = pinkstart[0]
        pink.y = pinkstart[1]
        b.x = ballstart[0]
        b.y = ballstart[1]
        b.velocity = np.array([0, 0])
        red.velocity = np.array([0, 0])
        pink.velocity = np.array([0, 0])

    return [redscore, pinkscore]


red = player(redstart[0], redstart[1], redcolour)
pink = player(pinkstart[0], pinkstart[1], pinkcolour)
b = ball(ballstart[0], ballstart[1])

redgoalpost1 = goalpost(pitchcornerx, goalcornery)
redgoalpost2 = goalpost(pitchcornerx, goalcornery + goalsize)
pinkgoalpost1 = goalpost(windowwidth - pitchcornerx, goalcornery)
pinkgoalpost2 = goalpost(windowwidth - pitchcornerx, goalcornery + goalsize)

goalposts = [redgoalpost1, redgoalpost2, pinkgoalpost1, pinkgoalpost2]
shitthatmoves = [red, pink, b]

redspeed = 0
pinkspeed = 0
pinkscore = 0
redscore = 0

run = True
while run:
    clock.tick(60)

    #should keep things on board
    if red.x <= movespacex[0] or red.x >= movespacex[1]:
        red.velocity[0] = 0
        if red.x <= movespacex[0]:
            red.x = movespacex[0]
        if red.x >= movespacex[1]:
            red.x = movespacex[1]
    if red.y <= movespacey[0] or red.y >= movespacey[1]:
        red.velocity[1] = 0
        if red.y <= movespacey[0]:
            red.y = movespacey[0]
        if red.y >= movespacey[1]:
            red.y = movespacey[1]
    if pink.x <= movespacex[0] or pink.x >= movespacex[1]:
        pink.velocity[0] = 0
        if pink.x <= movespacex[0]:
            pink.x = movespacex[0]
        if pink.x >= movespacex[1]:
            pink.x = movespacex[1]
    if pink.y <= movespacey[0] or pink.y >= movespacey[1]:
        pink.velocity[1] = 0
        if pink.y <= movespacey[0]:
            pink.y = movespacey[0]
        if pink.y >= movespacey[1]:
            pink.y = movespacey[1]
    if b.x <= ballspacex[0] or b.x >= ballspacex[1]:
        if b.y >= goaly[0] and b.y <= goaly[1]:
            pass
        else:
            b.velocity[0] = - 0.5 * b.velocity[0]
            if b.x <= ballspacex[0]:
                b.x = ballspacex[0]

            if b.x >= ballspacex[1]:
                b.x = ballspacex[1]
    if b.y <= ballspacey[0] or b.y >= ballspacey[1]:
        b.velocity[1] = - 0.5 * b.velocity[1]
        if b.y <= ballspacey[0]:
            b.y = ballspacey[0]
        if b.y >= ballspacey[1]:
            b.y = ballspacey[1]

    keys = pygame.key.get_pressed()

    #red movement controls
    if keys[pygame.K_LEFT]:
        if keys[pygame.K_UP]:
            red.xacc = - 1/(2)**(1/2)
            red.yacc = - 1/(2)**(1/2)
        elif keys[pygame.K_DOWN]:
            red.xacc = - 1/(2)**(1/2)
            red.yacc = 1/(2)**(1/2)
        else:
            red.xacc = -1
            red.yacc = 0

    elif keys[pygame.K_RIGHT]:
        if keys[pygame.K_UP]:
            red.xacc = 1/(2)**(1/2)
            red.yacc = - 1/(2)**(1/2)
        elif keys[pygame.K_DOWN]:
            red.xacc = 1/(2)**(1/2)
            red.yacc = 1/(2)**(1/2)
        else:
            red.xacc = 1
            red.yacc = 0

    elif keys[pygame.K_UP]:
        red.xacc = 0
        red.yacc = -1

    elif keys[pygame.K_DOWN]:
        red.xacc = 0
        red.yacc = 1

    else:
        red.xacc = 0
        red.yacc = 0

    if keys[pygame.K_SPACE]:
        red.kicking = True
    else:
        red.kicking = False

    #pink movement controls

    #left blank because I don't know what we want here, but feel free to fill













    #moves the players and ball
    if red.kicking == False:
        red.velocity = np.array(red.velocity) + np.array([red.xacc, red.yacc])*red.accelaration
    else:
        red.velocity = np.array(red.velocity) + np.array([red.xacc, red.yacc])*kickaccel

    if pink.kicking == False:
        pink.velocity = np.array(pink.velocity) + np.array([pink.xacc, pink.yacc])*pink.accelaration
    else:
        pink.velocity = np.array(pink.velocity) + np.array([pink.xacc, pink.yacc])*kickaccel

    red.velocity = red.velocity * playerdamping

    red.x += red.velocity[0]
    red.y += red.velocity[1]

    pink.velocity = pink.velocity * playerdamping

    pink.x += pink.velocity[0]
    pink.y += pink.velocity[1]

    b.velocity = np.array(b.velocity) * balldamping

    b.x += b.velocity[0]
    b.y += b.velocity[1]

    b.xint = int(b.x)
    b.yint = int(b.y)

    red.xint = int(red.x)
    red.yint = int(red.y)

    pink.xint = int(pink.x)
    pink.yint = int(pink.y)

    #finds distances to ball, kicking vectors, ect
    red.kickdirection = np.array([b.x - red.x, b.y - red.y])/(np.linalg.norm([b.x - red.x, b.y - red.y]))
    red.distancetoball = (np.linalg.norm(np.array([b.x - red.x, b.y - red.y])))
    pink.kickdirection = np.array([b.x - pink.x, b.y - pink.y])/(np.linalg.norm([b.x - pink.x, b.y - pink.y]))
    pink.distancetoball = (np.linalg.norm([b.x - pink.x, b.y - pink.y]))

    if red.distancetoball <= playerradius + ballradius + 4:

        if red.kicking == False:
            if red.distancetoball <= playerradius + ballradius:
                collision(b, red)
        else:
            kick(red, b)

    if pink.distancetoball <= playerradius + ballradius + 4:

        if pink.kicking == False:
            if pink.distancetoball <= playerradius + ballradius:
                collision(b, pink)
        else:
            kick(pink, b)

    #checks for bounces off goalposts
    for thing in shitthatmoves:
        for goalpost in goalposts:
            vector =  np.array([goalpost.x - thing.x, goalpost.y - thing.y])
            distance = np.linalg.norm(vector)
            if distance <= goalpostradius + thing.radius:
                thing.x = goalpost.x - vector[0]/np.linalg.norm(vector)
                thing.y = goalpost.y - vector[1]/np.linalg.norm(vector)
                collisiongoalpost(goalpost, thing)
                goalpost.x = int(goalpost.x)
                goalpost.y = int(goalpost.y)

    #checks for players bouncing off each other
    differencevector = np.array([pink.x - red.x, pink.y - red.y])
    distance = np.linalg.norm(differencevector)
    if distance <= 2*playerradius:
        collision(red, pink)

    G = goal(red, pink, b, redscore, pinkscore)
    redscore = G[0]
    pinkscore = G[1]
    redrawgamewindow()


    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
