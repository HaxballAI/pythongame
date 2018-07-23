win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("ball")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 70)

dc = 0.5

class player(object):
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.xvel = 0
        self.yvel = 0
        self.xacc = 0
        self.yacc = 0
        
    
    def draw(self, win):
        pygame.draw.circle(win, self.colour, (self.x, self.y), 20)
        
class ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xvel = 0
        self.yvel = 0
        self.xacc = 0
        self.yacc = 0
    
    def draw(self, win):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), 10)
    
def redrawgamewindow():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (50, 100, 400, 300))
    pygame.draw.rect(win, (0, 0, 255), (25, 210, 25, 80))
    pygame.draw.rect(win, (0, 0, 255), (450, 210, 25, 80))
    pygame.draw.rect(win, (255, 255, 255), (45, 210, 5, 80))
    pygame.draw.rect(win, (255, 255, 255), (450, 210, 5, 80))
    you.draw(win)
    you2.draw(win)
    b.draw(win)
    string = str(red) + ":" + str(pink)
    text = font.render(string, True, (255, 255, 255))
    win.blit(text, (215, 25))
    pygame.display.update()
    
    
def goal(you, you2, b, red, pink):
    if b.x <= 45:
        pink += 1
        you.x = 120
        you.y = 250
        you2.x = 380
        you2.y = 250
        b.x = 250
        b.y = 250
        b.xvel = 0
        b.yvel = 0
        you.xvel = 0
        you.yvel = 0
        you2.xvel = 0
        you2.yvel = 0
    elif b.x >= 455:
        red += 1
        you.x = 120
        you.y = 250
        you2.x = 380
        you2.y = 250
        b.x = 250
        b.y = 250
        b.xvel = 0
        b.yvel = 0
        you.xvel = 0
        you.yvel = 0
        you2.xvel = 0
        you2.yvel = 0
    
    return [red, pink]
    
    
you = player(120, 250, (255, 0, 0))
you2 = player(380, 250, (255, 0, 255))
b = ball(250, 250)
accelarating = False
youspeed = 0
pink = 0
red = 0

run = True
while run:
    clock.tick(30)
    
    
    keys = pygame.key.get_pressed()
    
    if you.x <= 70 or you.x >= 430:
        you.xvel = 0
        
    if you.y <= 120 or you.y >= 380:
        you.yvel = 0
        
    if you2.x <= 70 or you2.x >= 430:
        you2.xvel = 0
        
    if you2.y <= 120 or you2.y >= 380:
        you2.yvel = 0    
    
        
    if b.x <= 60 or b.x >= 440:
        if b.y >= 210 and b.y <= 290:
            pass
        else:
            b.xvel = - b.xvel
        
    if b.y <= 110 or b.y >= 390:
        b.yvel = - b.yvel
    
    if you.y >= 120 and you.y <= 380:
        if you.x >= 70 and you.x <= 430:
            
            if keys[pygame.K_LEFT]:
                you.xvel -= 1
                accelarating = True

            if keys[pygame.K_RIGHT]:
                you.xvel += 1   
                accelarating = True

            if keys[pygame.K_UP]:
                you.yvel -= 1
                accelarating = True

            if keys[pygame.K_DOWN]:
                you.yvel += 1
                accelarating = True
    
    if you2.y >= 120 and you2.y <= 380:
        if you2.x >= 70 and you2.x <= 430:
            
            if keys[pygame.K_a]:
                you2.xvel -= 1
                accelarating = True

            if keys[pygame.K_d]:
                you2.xvel += 1   
                accelarating = True

            if keys[pygame.K_w]:
                you2.yvel -= 1
                accelarating = True

            if keys[pygame.K_s]:
                you2.yvel += 1
                accelarating = True
    
    
    
    youspeed = np.linalg.norm([you.xvel, you.yvel])        
    
    toball = [b.x - you.x, b.y - you.y]
    distance = np.linalg.norm(toball)
    
    if toball[1] > 0:
        angle = np.arctan(toball[0]/toball[1])
    if toball[1] < 0:
        angle = np.arctan(toball[0]/toball[1]) + np.pi
    else:
        if toball[0] > 0:
            angle = np.pi/2
        else:
            angle = 3*np.pi/2
        
    youspeed2 = np.linalg.norm([you2.xvel, you2.yvel])        
    
    toball2 = [b.x - you2.x, b.y - you2.y]
    distance2 = np.linalg.norm(toball2)
    
    if toball2[1] > 0:
        angle2 = np.arctan(toball2[0]/toball2[1])
    if toball2[1] < 0:
        angle2 = np.arctan(toball2[0]/toball2[1]) + np.pi
    else:
        if toball[0] > 0:
            angle2 = np.pi/2
        else:
            angle2 = 3*np.pi/2    
    
        
    if distance <= 30:
        b.xvel = int(np.floor(toball[0] * youspeed/30))
        b.yvel = int(np.floor(toball[1] * youspeed/30))
        b.x += 1
        b.y += 1
    b.x += b.xvel
    b.y += b.yvel
    
    
    if distance2 <= 30:
        b.xvel = int(np.floor(toball2[0] * youspeed2/30))
        b.yvel = int(np.floor(toball2[1] * youspeed2/30))
        b.x += 1
        b.y += 1
    b.x += b.xvel
    b.y += b.yvel
    
    you.x += you.xvel
    you.y += you.yvel
    
    you2.x += you2.xvel
    you2.y += you2.yvel
    
    if you.x >= 430:
        you.x = 430
        
    if you.y >= 380:
        you.y = 380
        
    if you.x <= 70:
        you.x = 70
        
    if you.y <= 120:
        you.y = 120
    
    if you2.x >= 430:
        you2.x = 430
        
    if you2.y >= 380:
        you2.y = 380
        
    if you2.x <= 70:
        you2.x = 70
        
    if you2.y <= 120:
        you2.y = 120
    
    if b.x <= 60:
        if b.y >= 290 or b.y <= 210:
            b.x = 60
        
    if b.y <= 110:
        b.y = 110
        
    if b.x >= 440:
        if b.y >= 290 or b.y <= 210:
            b.x = 440
        
    if b.y >= 390:
        b.y = 390
    
    Q = goal(you, you2, b, red, pink)
    red = Q[0]
    pink = Q[1]
    redrawgamewindow()
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False