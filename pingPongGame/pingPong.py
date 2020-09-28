'''
Created on Sep 18, 2020

@author: davidfranco
'''
import pygame
from pygame.locals import *



playerX=740   
playerY=100
cpuX=30
cpuY=0
height=0
cpuVy=2
circleVx=4
circleVy=6
circleX=400 
circleY=300
radius=20
playerHP=500
cpuHP=500
cpuHeight=100
 


class PingPong(pygame.sprite.Sprite):
    def __init__(self):
        super(PingPong, self).__init__()
        self.cpuSurface = pygame.Surface((25, 100))
        self.cpuSurface.fill((255, 255, 255))
        self.rect = self.cpuSurface.get_rect()
        
        self.playerSurface = pygame.Surface((25, 100))
        self.playerSurface.fill((255, 255, 255))
        self.rect = self.playerSurface.get_rect()
        
        self.playerHP=500
        self.cpuHP=500
        
        self.playerX=740
        self.playerY=100
        
        
        
        
        
    def scoreDisplay(self):
            font = pygame.font.Font('freesansbold.ttf', 32) 
            screen.fill(pygame.Color("black")) # erases the entire screen surface
        
            textsurface = font.render("CPU :"+str(self.getCPUHpScore()), False, (255, 255, 255))
            screen.blit(textsurface,(0,0))
            
            textsurface = font.render("player :"+str(self.getPlayerHpScore()), False, (255, 255, 255))
            screen.blit(textsurface,(600,0))
    
    
    def setPlayerHPScore(self,playerHP_):
            self.playerHP=playerHP_
        
    def getPlayerHpScore(self):
            return self.playerHP;
        
    def setCPUHPScore(self,cpuHP_):
            self.cpuHP=cpuHP_
        
    def getCPUHpScore(self):
            return cpuHP;  
        
    def clearPlayerImage(self): 
            surf3 = pygame.Surface((25, 100))
            surf3.fill((0, 0, 0))
            screen.blit(surf3, (self.getPlayerPositionX(), self.getPlayerPositionY()))
    def drawPlayerImage(self):
            screen.blit(self.playerSurface, (self.getPlayerPositionX(),self.getPlayerPositionY()))
            self.playerSurface.fill((255, 255, 255))
            pygame.display.update()
            
        
    def getPlayerPositionX(self):
        return self.playerX 
    def setPlayerPositionX(self,playerX_):
        self.playerX=playerX_
    def getPlayerPositionY(self):
        return self.playerY
    def setPlayerPositionY(self,playerY_):
        self.playerY=playerY_ 
    def setCpuPositionY(self,cpuY_):
        self.cpuY=cpuY_
    def getCpuPositionY(self):
        return self.cpuY
    def getCpuVelocityY(self):
        return self.cpuVy
    def setCpuVelocityY(self,cpuVy_):
        self.cpuVy=cpuVy_
    

# initialize pygame
pygame.init()


screen = pygame.display.set_mode((800, 600))

entities = PingPong()
clock = pygame.time.Clock()

running = True


while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == pygame.K_UP:
                entities.clearPlayerImage();
                entities.setPlayerPositionY(entities.getPlayerPositionY()-40)
              
            elif event.key == pygame.K_DOWN:
                entities.clearPlayerImage()
                entities.setPlayerPositionY(entities.getPlayerPositionY()+40)
      
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False
       
 
  
    

    
    cpuY+=cpuVy
    pygame.draw.circle(screen, (0,0,0), (circleX, circleY), radius, 10)
    print(circleVy+circleY)
    print("player")
    print(playerY)
    if circleVx+circleX>=800  :
        circleVx*=-1
        playerHP=playerHP-20
        entities.setPlayerHPScore(playerHP)
        
    elif circleVx+circleX<=0:
        circleVx*=-1
        cpuHP=cpuHP-20
        entities.setCPUHPScore(cpuHP)
       
    elif (circleVx+circleX>=playerX and (circleVy+circleY>= entities.getPlayerPositionY() and circleVy+circleY<=( entities.getPlayerPositionY()+100))) or (circleX+circleVx<=cpuX+25 and (circleVy+circleY>=cpuY and circleVy+circleY<=(cpuY+100))):
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
    
   
    entities.scoreDisplay()
    
 
   

    circleX+=circleVx
    circleY+=circleVy
    

        
    pygame.draw.circle(screen, (255,255,255), (circleX, circleY), radius, 10)
  
 
    entities.drawPlayerImage()
    
    screen.blit(entities.cpuSurface, (cpuX, cpuY))
    pygame.display.update()



      
    # Update the display
    pygame.display.flip()