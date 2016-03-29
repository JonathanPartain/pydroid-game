import sys, pygame
from random import randint

pygame.init()

size = width, height = 800, 600
speed = [2, 2]
green = 0,255,0
black = 1, 1, 1
screen = pygame.display.set_mode((size))
pygame.display.set_caption('Pick up the squares!')
UP='up'
DOWN='down'
LEFT='left'
RIGHT='right'

ballx = 400
bally = 300
ballpos = (ballx, bally)
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect(topleft = (ballx, bally))

endBlipx = 0
endBlipy = 0


blipx = randint(1,800)
blipy = randint(1,600)

blippos = (blipx, blipy)
blip = pygame.image.load("blip.png")
bliprect = blip.get_rect(topleft = (blipx, blipy))


enemy1x = randint(1,800)
enemy1y = randint(1,600)
enemy1pos = (enemy1x, enemy1y)
enemy1 = pygame.image.load("enemy.png")
enemy1rect = blip.get_rect(topleft = (enemy1x, enemy1y))

enemy2x = randint(1,800)
enemy2y = randint(1,600)
enemy2pos = (enemy2x, enemy2y)
enemy2 = pygame.image.load("enemy.png")
enemy2rect = blip.get_rect(topleft = (enemy2x, enemy2y))

enemy1changex = 5
enemy1changey = 5

enemy2changex = 5
enemy2changey = 5


newPosx = randint(1,795)
newPosy = randint(1,595)

background = pygame.Surface(screen.get_size())
background = background.convert()    
background.fill((250, 250, 250))



scoreNum = 0


font = pygame.font.Font(None, 36)
text = font.render("{}{}".format("Score: ", scoreNum),8,(250,0,0))
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(text, textpos)




clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
# Movement

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        ballx  -= 5
        ballrect.x -=5
    if keys[pygame.K_RIGHT]:
        ballx += 5
        ballrect.x += 5
    if keys[pygame.K_UP]:
        bally -= 5
        ballrect.y -= 5
    if keys[pygame.K_DOWN]:
        bally +=5
        ballrect.y += 5
    
    if ballrect.colliderect(bliprect): 
        blipx = randint(1,795)
        blipy = randint(1,595)
        bliprect = blip.get_rect(topleft = (blipx, blipy))
        
        scoreNum = int(scoreNum)
        scoreNum = scoreNum + 1
        scoreNum = str(scoreNum)
        text = font.render("{}{}".format("Score: ", scoreNum),8,(250,0,0))
        scoreNum = int(scoreNum)
        
        
    if ballx >= 765:
        ballx -= 5
        ballrect.x -= 5
    if bally <= -5:
        bally += 5
        ballrect.y += 5
    if ballx <=-5:
        ballx +=5
        ballrect.x +=5
    if bally >=565:
        bally -=5
        ballrect.y -=5
        
    if scoreNum >= 5:
        
        
        screen.blit(enemy1, (enemy1x, enemy1y))
        screen.blit(enemy1, (enemy1rect))
        
        enemy1x += enemy1changex
        enemy1y += enemy1changey
        enemy1rect.x += enemy1changex
        enemy1rect.y += enemy1changey
        
        if enemy1x > 795 or enemy1x < 5:
            enemy1changex = enemy1changex * -1
        if enemy1y > 595 or enemy1y < 5:
            enemy1changey = enemy1changey * -1
        
    if scoreNum >= 6:
        
        screen.blit(enemy2, (enemy2x, enemy2y))
        screen.blit(enemy2, (enemy2rect))
    
        enemy2x += enemy2changex
        enemy2y += enemy2changey
        enemy2rect.x += enemy2changex
        enemy2rect.y += enemy2changey
        
        if enemy2x > 795 or enemy2x < 5:
            enemy2changex = enemy2changex *-1
        if enemy2y > 595 or enemy2y < 5:
            enemy2changey = enemy2changey * -1
        
    
       
    
    if ballrect.colliderect(enemy1rect):
        screen.fill(black)
        pygame.draw.rect(screen, black, (ballrect.x, ballrect.y, 20, 20))
        text = font.render("{}".format("You lose!!"), 8, (250,0,0))
        scoreNum = 0

    
    if ballrect.colliderect(enemy2rect):
        screen.fill(black)
        pygame.draw.rect(screen, black, (ballrect.x, ballrect.y, 20, 20))
        text = font.render("{}".format("You lose!!"), 8, (250,0,0))
        scoreNum = 0
    
    
    if scoreNum == 10:
    
        text = font.render("{}".format("You win!"), 8, (250,0,0))

        

    screen.fill(black)
    screen.blit(ball,(ballrect))
    screen.blit(ball, (ballx, bally))
    screen.blit(blip,(bliprect))
    screen.blit(blip, (blipx, blipy))
    screen.blit(enemy1, (enemy1x, enemy1y))
    screen.blit(enemy1, (enemy1rect))
    screen.blit(enemy2, (enemy2x, enemy2y))
    screen.blit(enemy2, (enemy2rect)) 
    screen.blit(text, textpos)
    pygame.display.update()
    clock.tick(40)
