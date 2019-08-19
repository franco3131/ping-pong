import pygame
from pygame.locals import *






circleVx=5
circleVy=6
circleX=400 
circleY=300
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
    
        



    










# initialize pygame
pygame.init()

# create the screen object
# here we pass it a size of 800x600
screen = pygame.display.set_mode((800, 600))


player = PLAYER()
cpu=CPU()
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
    print(cpu.getPositionY())
    
    pygame.draw.circle(screen, (0,0,0), (circleX, circleY), radius, 10)

    if circleVx+circleX>=800  :
        circleVx*=-1
        playerHP=playerHP-20
        player.setHPScore(playerHP)
        
    elif circleVx+circleX<=0:
        circleVx*=-1
        cpuHP=cpuHP-20
        cpu.setHPScore(cpuHP)
    elif (circleVx+circleX+radius>=player.getPositionX() and (circleVy+circleY>=player.getPositionY() and circleVy+circleY<=(player.getPositionY()+100))) or (circleX+circleVx<=cpu.getPositionX()+25 and (circleVy+circleY>=cpu.getPositionY() and circleVy+circleY<=(cpu.getPositionY()+100))):
        circleVx*=-1
    elif circleVy+circleY>=600 or circleVy+circleY<=0:
        circleVy*=-1
    elif(((circleVy>0 and cpu.getVelocityY()<0) or (circleVy<0 and cpu.getVelocityY()>0)) and circleX==300 and circleVx==-5 and (circleY-player.getPositionY()>50)) :
        cpu.setVelocityY(cpu.getVelocityY()*(-1))
    elif((circleVy>0 and cpu.getVelocityY()>0) and circleY>300 and player.getPositionY()<300 and circleX<400 and circleVx==-5) :
        if player.getPositionY()<300:
            cpu.setVelocityY(5)
        else:
            cpu.setVelocityY(2)
    elif((circleVy>0 and cpu.getVelocityY()>0) and circleY<300 and circleX<400  and circleVx==-5) :
        if player.getPositionY()>300:
            cpu.setVelocityY(5)
        else:
            cpu.setVelocityY(2)
    elif((circleVy<0 and cpu.getVelocityY()<0) and circleY<300 and circleX<400 and circleVx==-5) :
        if player.getPositionY()>300:
            cpu.setVelocityY(-5)
        else:
            cpu.setVelocityY(-2)
  
    elif((circleVy<0 and cpu.getVelocityY()<0) and circleY>300 and circleX<400 and circleVx==-5) :
        if player.getPositionY()<300:
           cpu.setVelocityY(-5)
        else:
            cpu.setVelocityY(-2)
    

    if cpu.getPositionY()+cpu.getVelocityY()>=502:
        cpu.setVelocityY(cpu.getVelocityY()*(-1))
    elif cpu.getPositionY()+cpu.getVelocityY()<=0:
        cpu.setVelocityY(cpu.getVelocityY()*(-1))
    
   
    screen.fill(pygame.Color("black"))
    cpu.scoreDisplay()
    player.scoreDisplay()
  
   

    circleX+=circleVx
    circleY+=circleVy
    

        
    pygame.draw.circle(screen, (255,255,255), (circleX, circleY), radius, 10)
  
 
    player.drawImage()
    
    cpu.drawImage()



      
    # Update the display
    pygame.display.flip()