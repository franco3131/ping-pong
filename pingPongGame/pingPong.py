import pygame
from pygame.locals import *


radius=20
playerHP=500
cpuHP=500



# import pygame.locals for easier access to key coordinates

# Define our player object and call super to give it all the properties and methods of pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'player'
class PLAYER(pygame.sprite.Sprite):
    def __init__(self):
        super(PLAYER, self).__init__()
        self.playerSurface = pygame.Surface((25, 100))
        self.playerSurface.fill((255, 255, 255))
        self.rect = self.playerSurface.get_rect()
        self.playerHP=500
        self.playerX=740
        self.playerY=100
      
        
        
        
    def scoreDisplay(self):
            font = pygame.font.Font('freesansbold.ttf', 32)  # erases the entire screen surface
            textsurface = font.render("player :"+str(self.getHpScore()), False, (255, 255, 255))
            screen.blit(textsurface,(600,0))
    
    
    def setHPScore(self,playerHP_):
            self.playerHP=playerHP_
        
    def getHpScore(self):
            return self.playerHP;
        

    def clearImage(self): 
            playerImage = pygame.Surface((25, 100))
            playerImage.fill((0, 0, 0))
            screen.blit(playerImage, (self.getPositionX(), self.getPositionY()))
    
    def drawImage(self):
            screen.blit(self.playerSurface, (self.getPositionX(),self.getPositionY()))
            self.playerSurface.fill((255, 255, 255))
            pygame.display.update()
            
        
    def getPositionX(self):
        return self.playerX 
    def setPositionX(self,playerX_):
        self.playerX=playerX_
    def getPositionY(self):
        return self.playerY
    def setPositionY(self,playerY_):
        self.playerY=playerY_ 
  
    

class CPU(pygame.sprite.Sprite):
    def __init__(self):
        super(CPU, self).__init__()
        self.cpuSurface = pygame.Surface((25, 100))
        self.cpuSurface.fill((255, 255, 255))
        self.rect = self.cpuSurface.get_rect()
        self.cpuHP=500
        self.cpuX=30
        self.cpuY=0
        self.cpuVy=2
        
            
    def scoreDisplay(self):
            cpuFont = pygame.font.Font('freesansbold.ttf', 32) 
            textsurface2 = cpuFont.render("CPU :"+str(self.getHpScore()), False, (255, 255, 255))
            screen.blit(textsurface2,(0,0))
       
            
            
    def setPositionY(self,cpuY_):
        self.cpuY=cpuY_
        
    def getPositionY(self):
        return self.cpuY
    
    def setPositionX(self,cpuX_):
        self.cpuX=cpuX_
    def getPositionX(self):
        return self.cpuX
    def getVelocityY(self):
        return self.cpuVy
    def setVelocityY(self,cpuVy_):
        self.cpuVy=cpuVy_  
    def setHPScore(self,cpuHP_):
            self.cpuHP=cpuHP_
    def getHpScore(self):
            return cpuHP;  
        
    def drawImage(self):
        screen.blit(self.cpuSurface, (self.getPositionX(), self.getPositionY()))
        self.cpuSurface.fill((255, 255, 255))
        pygame.display.update()   
    
    def moveUpDownAtBorder(self): 
        if self.getPositionY()+self.getVelocityY()>=502:
            self.setVelocityY(self.getVelocityY()*(-1))
        elif self.getPositionY()+self.getVelocityY()<=0:
            self.setVelocityY(self.getVelocityY()*(-1))



    

class CIRCLE(pygame.sprite.Sprite):
    def __init__(self):
        super(CIRCLE, self).__init__()
        self.circleVx=5
        self.circleVy=6
        self.circleX=400 
        self.circleY=300


    def setPositionX(self,circleX_): 
        self.circleX=circleX_
    def getPositionX(self):
        return self.circleX
    def setVelocityX(self,circleVx_):
        self.circleVx=circleVx_
    def getVelocityX(self):
        return self.circleVx
    def setPositionY(self,circleY_): 
        self.circleY=circleY_
    def getPositionY(self):
        return self.circleY
    def setVelocityY(self,circleVy_):
        self.circleVy=circleVy_
    def getVelocityY(self):
        return self.circleVy

    def drawCircleImage(self):
        pygame.draw.circle(screen, (255,255,255), (circle.getPositionX(), circle.getPositionY()), radius, 10)
    def clearCircleImage(self):
        pygame.draw.circle(screen, (0,0,0), (circle.getPositionX(), circle.getPositionY()), radius, 10)




# initialize pygame
pygame.init()

# create the screen object
# here we pass it a size of 800x600
screen = pygame.display.set_mode((800, 600))


player = PLAYER()
cpu=CPU()
circle=CIRCLE()
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
                player.clearImage();
                player.setPositionY(player.getPositionY()-40)
              
            elif event.key == pygame.K_DOWN:
                player.clearImage()
                player.setPositionY(player.getPositionY()+40)
      
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False
       
 
  
    

    cpu.setPositionY(cpu.getPositionY()+cpu.getVelocityY())
   
    circle.drawCircleImage()
    pygame.draw.circle(screen, (0,0,0), (circle.getPositionX(), circle.getPositionY()), radius, 10)

    if circle.getVelocityX()+circle.getPositionX()>=800:
        circle.setVelocityX(circle.getVelocityX()*(-1))
        playerHP=playerHP-20
        player.setHPScore(playerHP)
    elif circle.getVelocityX()+circle.getPositionX()<=0:
        circle.setVelocityX(circle.getVelocityX()*(-1))
        cpuHP=cpuHP-20
        cpu.setHPScore(cpuHP)
    elif (circle.getVelocityX()+circle.getPositionX()+radius>=player.getPositionX() and (circle.getVelocityY()+circle.getPositionY()>=player.getPositionY() and circle.getVelocityY()+circle.getPositionY()<=(player.getPositionY()+100))) or (circle.getPositionX()+circle.getVelocityX()<=cpu.getPositionX()+25 and (circle.getVelocityY()+circle.getPositionY()>=cpu.getPositionY() and circle.getVelocityY()+circle.getPositionY()<=(cpu.getPositionY()+100))):
         circle.setVelocityX(circle.getVelocityX()*(-1))
    elif circle.getVelocityY()+circle.getPositionY()>=600 or circle.getVelocityY()+circle.getPositionY()<=0:
        circle.setVelocityY(circle.getVelocityY()*(-1))
    elif(((circle.getVelocityY()>0 and cpu.getVelocityY()<0) or (circle.getVelocityY()<0 and cpu.getVelocityY()>0)) and circle.getPositionX()==300 and circle.getVelocityX()==-5 and (circle.getPositionY()-player.getPositionY()>50)) :
        cpu.setVelocityY(cpu.getVelocityY()*(-1))
    elif((circle.getVelocityY()>0 and cpu.getVelocityY()>0) and circle.getPositionY()>300 and player.getPositionY()<300 and circle.getPositionX()<400 and circle.getVelocityX()==-5) :
        if player.getPositionY()<300:
            cpu.setVelocityY(5)
        else:
            cpu.setVelocityY(2)
    elif((circle.getVelocityY()>0 and cpu.getVelocityY()>0) and circle.getVelocityY()<300 and circle.getPositionX()<400  and circle.getVelocityX()==-5) :
        if player.getPositionY()>300:
            cpu.setVelocityY(5)
        else:
            cpu.setVelocityY(2)
    elif((circle.getVelocityY()<0 and cpu.getVelocityY()<0) and circle.getPositionY()<300 and circle.getPositionX()<400 and circle.getVelocityX()==-5) :
        if player.getPositionY()>300:
            cpu.setVelocityY(-5)
        else:
            cpu.setVelocityY(-2)
  
    elif((circle.getVelocityY()<0 and cpu.getVelocityY()<0) and circle.getVelocityY()>300 and circle.getPositionX()<400 and circle.getVelocityX()==-5) :
        if player.getPositionY()<300:
           cpu.setVelocityY(-5)
        else:
            cpu.setVelocityY(-2)
    
    
    
    cpu.moveUpDownAtBorder()
    
   
    screen.fill(pygame.Color("black"))
    cpu.scoreDisplay()
    player.scoreDisplay()
  
   
    circle.setPositionX(circle.getPositionX()+circle.getVelocityX())
    circle.setPositionY(circle.getPositionY()+circle.getVelocityY())
 
    

        
    circle.drawCircleImage()
 
    player.drawImage()
    
    cpu.drawImage()



      
    # Update the display
    pygame.display.flip()