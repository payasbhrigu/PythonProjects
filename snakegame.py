#Snake Game
#by Payas Bhrigu

#Game imports
import pygame,sys,time,random
check_errors = pygame.init()
if(check_errors[1]>0):
    print("(!)Had {0} initializing errors,exiting...".format(check_errors[1]))
    sys.exit(-1)    #-1 is a convention to report errors in initialization
else:
    print("(+)PyGame initialized succesfully!")
#Play Surface 
playSurface = pygame.display.set_mode((780,560))
pygame.display.set_caption('My Snake Game!')
#Colors
red = pygame.Color(255,0,0) #gameover
green = pygame.Color(0,255,0)   #snake
white = pygame.Color(255,255,255)   #background
scorecolor = pygame.Color(33,123,243) #score
brown = pygame.Color(160,82,45) #food
blue  = pygame.Color(0,0,245)
#fps controller
fpsController = pygame.time.Clock()

#important variables
snakePos = [100,50]
snakeBody = [[100,50], [90,50], [80,50]]
foodPos = [random.randrange(1,78)*10,random.randrange(1,56)*10]
foodSpawn = True
direction = 'RIGHT'
changeTo = direction
score=0
def showScore(choice=1):
    SFont = pygame.font.SysFont('monaco',25)
    Ssurf = SFont.render('Score :'+str(score),True,scorecolor)
    Srect = Ssurf.get_rect()
    if choice==1:
        Srect.midtop=(400,10)
    else :
        Srect.midtop=(360,80)
    playSurface.blit(Ssurf,Srect)
    pygame.display.flip()
def gameOver():
    myFont = pygame.font.SysFont('monaco',70)
    GOsurf = myFont.render('Game Over!!',True,red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360,15)
    playSurface.blit(GOsurf,GOrect)
    pygame.display.flip()
    showScore(0)
    time.sleep(4)
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                changeTo = 'RIGHT'
            if event.key==pygame.K_LEFT:
                changeTo = 'LEFT'
            if event.key==pygame.K_UP:
                changeTo = 'UP'
            if event.key==pygame.K_DOWN:
                changeTo = 'DOWN'
            if event.key==pygame.K_ESCAPE:
                pygame.event.post(pygame.event.EVENT(pygame.QUIT))
    #validation of directions
    if changeTo=='RIGHT' and not direction=='LEFT':
        direction='RIGHT'
    if changeTo=='LEFT' and not direction=='RIGHT':
        direction='LEFT'
    if changeTo=='UP' and not direction=='DOWN':
        direction='UP'
    if changeTo=='DOWN' and not direction=='UP':
        direction='DOWN'
    #update snake position(x,y)
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10
#food Spawn
    if foodSpawn==False :
        foodPos=[random.randrange(1,78)*10,random.randrange(1,56)*10]
    foodSpawn=True
    
    #snake body mechanism
    snakeBody.insert(0,list(snakePos))
    if snakePos[0]==foodPos[0] and snakePos[1]==foodPos[1]:
        score+=1
        foodSpawn=False
    else:   snakeBody.pop()
    
    
    playSurface.fill(white)
    #draw snake
    for pos in snakeBody:
        pygame.draw.ellipse(playSurface,green,pygame.Rect(pos[0],pos[1],10,10))
    #draw food
    pygame.draw.circle(playSurface,brown,(foodPos[0],foodPos[1]),5)
    
    if snakePos[0]>770 or snakePos[0]<0:
        gameOver()
    if snakePos[1]>550 or snakePos[1]<0:
        gameOver()
    for block in snakeBody[1:]:
        if snakePos[0]==block[0] and snakePos[1]==block[1]:
            gameOver()
    showScore()
    pygame.display.flip()   #to update the screen with code
    fpsController.tick(25)