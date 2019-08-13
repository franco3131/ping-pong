# import the pygame module
import pygame
import random

playerX=740   
playerY=100
cpuX=30
cpuY=0
height=0
cpuVy=2
circleVx=5
circleVy=6
circleX=400 
circleY=300
radius=20
playerHP=500
cpuHP=500
cpuHeight=100
 


# import pygame.locals for easier access to key coordinates
from pygame.locals import *

# Define our player object and call super to give it all the properties and methods of pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25, 100))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.surfs = pygame.Surface((25, 100))
        self.surfs.fill((255, 255, 255))
        self.rect = self.surfs.get_rect()

# initialize pygame
pygame.init()

# create the screen object
# here we pass it a size of 800x600
screen = pygame.display.set_mode((800, 600))

# instantiate our player; right now he's just a rectangle
player = Player()
clock = pygame.time.Clock()

# Variable to keep our main loop running
running = True



# Our main loop!
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
            elif event.key == pygame.K_UP:
                surf3 = pygame.Surface((25, 100))
                surf3.fill((0, 0, 0))
                screen.blit(surf3, (playerX, playerY))
                playerY=playerY-40
          
            elif event.key == pygame.K_DOWN:
                surf3 = pygame.Surface((25, 100))
                surf3.fill((0, 0, 0))
                screen.blit(surf3, (playerX, playerY))
                playerY=playerY+40
             
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False
       
    # Draw the player to the screen
    surf2 = pygame.Surface((25, 100))
    surf2.fill((0, 0, 0))
    screen.blit(surf2, (cpuX, cpuY))
    r=random.randint(0, 5)
    

    
    cpuY+=cpuVy
    pygame.draw.circle(screen, (0,0,0), (circleX, circleY), radius, 10)

    if circleVx+circleX>=800  :
        circleVx*=-1
        playerHP=playerHP-20
    elif circleVx+circleX<=0:
        circleVx*=-1
        cpuHP=cpuHP-20
    elif (circleVx+circleX+radius>=playerX and (circleVy+circleY>=playerY and circleVy+circleY<=(playerY+100))) or (circleX+circleVx<=cpuX+25 and (circleVy+circleY>=cpuY and circleVy+circleY<=(cpuY+100))):
        circleVx*=-1
    elif circleVy+circleY>=600 or circleVy+circleY<=0:
        circleVy*=-1
    elif(((circleVy>0 and cpuVy<0) or (circleVy<0 and cpuVy>0)) and circleX==300 and circleVx==-5 and (circleY-playerY>50)) :
        cpuVy*=-1
    elif((circleVy>0 and cpuVy>0) and circleY>300 and playerY<300 and circleX<400 and circleVx==-5) :
        if playerY<300:
            cpuVy=5
        else:
            cpuVy=2
    elif((circleVy>0 and cpuVy>0) and circleY<300 and circleX<400  and circleVx==-5) :
        if playerY>300:
            cpuVy=5
        else:
            cpuVy=2
    elif((circleVy<0 and cpuVy<0) and circleY<300 and circleX<400 and circleVx==-5) :
        if playerY>300:
            cpuVy=-5
        else:
            cpuVy=-2
  
    elif((circleVy<0 and cpuVy<0) and circleY>300 and circleX<400 and circleVx==-5) :
        if playerY<300:
            cpuVy=-5
        else:
            cpuVy=-2
    


    
        
    
    if cpuY+cpuVy>=502:
        cpuVy*=-1
    elif cpuY+cpuVy<=0:
        cpuVy*=-1
    
   
   
    font = pygame.font.Font('freesansbold.ttf', 32) 
    screen.fill(pygame.Color("black")) # erases the entire screen surface

    textsurface = font.render("CPU :"+str(cpuHP), False, (255, 255, 255))
    screen.blit(textsurface,(0,0))
    
    textsurface = font.render("player :"+str(playerHP), False, (255, 255, 255))
    screen.blit(textsurface,(600,0))
    
 
   

    circleX+=circleVx
    circleY+=circleVy
    

        
    pygame.draw.circle(screen, (255,255,255), (circleX, circleY), radius, 10)
  
    surf3 = pygame.Surface((25, 100))
    surf3.fill((0, 0, 0))
    screen.blit(surf3, (playerX, playerY))
    screen.blit(player.surfs, (playerX, playerY))
    player.surfs.fill((255, 255, 255))
    pygame.display.update()
    screen.blit(player.surf, (cpuX, cpuY))
    pygame.display.update()

     
      
    # Update the display
    pygame.display.flip()