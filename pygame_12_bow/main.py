import pygame,sys
from pygame.locals import *

pygame.init()
def ExitGame():
    """
        Function that stops the game
    """
    pygame.quit()
    sys.exit()
class Bow :
    def __init__(self):
        """
            The bow that must move
        """
        self.image = pygame.image.load("miniarc.png")
        self.axe_x = 21
        self.axe_y = 216
        self.angle = 0
        self.rotate = pygame.transform.rotate(self.image,self.angle)
    def Update(self):
        self.angle += 45
        print("et up")
        
class Arrow :
    arrowspeed=20
    def __init__(self):
        """
            You're shooting at the hive !
        """
        self.axe_x=21
        self.axe_y=222
        self.image=pygame.image.load("arrow.png")
    def Update(self):
        pass
#SCREEN
screen = pygame.display.set_mode((1400, 240))
#WHAT TO SHOW
background = pygame.image.load("background.png")
arrow = Arrow()
arm = Bow()
running = True
new_angle=0
while running :
    moveup = False
    movedown = False
    for event in pygame.event.get():
        
        if event.type == QUIT:
            ExitGame()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                ExitGame()
            if event.key == K_UP:
                moveup = True
            if event.key == K_DOWN:
                movedown = True
                
        if event.type == KEYUP:
            if event.key == K_UP:
                moveup = False
            if event.key == K_DOWN:
                movedown = False
        if moveup :
            
            arm.image = pygame.transform.rotate(arm.image,0) #On affiche le bras non modifié / on réinitialise le bras avant de le re-modifier
            angle = 5 #On garde l'angle précédent pour l'incrémenter
            new_angle += angle #On prend l'angle et l'incrémentation
            if new_angle >= 45:
                new_angle = 45
            elif new_angle < 0:
                new_angle = 0
            if new_angle > 25:
                arm.axe_x = 19
                arm.axe_y = 209
            elif new_angle <= 25:
                arm.axe_x = 21
                arm.axe_y = 211
            elif new_angle == 0:
                arm.axe_x = 21
                arm.axe_y = 216
            arm.image = pygame.transform.rotate(arm.image,new_angle) #On
        if movedown :
            arm.image = pygame.transform.rotate(arm.image,0) #On affiche le bras non modifié / on réinitialise le bras avant de le re-modifier
            angle = -5 #On garde l'angle précédent pour l'incrémenter
            new_angle += angle #On prend l'angle et l'incrémentation
            if new_angle >= 45:
                new_angle = 45
            elif new_angle < 0:
                new_angle = 0
            if new_angle > 25:
                arm.axe_x = 19
                arm.axe_y = 209
            elif new_angle <= 25:
                arm.axe_x = 21
                arm.axe_y = 211
            elif new_angle == 0:
                arm.axe_x = 21
                arm.axe_y = 216
            arm.image = pygame.transform.rotate(arm.image,new_angle)

    screen.blit(background, (0,0)) #bg + ninja
    screen.blit(arm.image, (arm.axe_x,arm.axe_y)) #initial position of arm and bow
    screen.blit(arrow.image, (arrow.axe_x,arrow.axe_y)) #initial position of arrow
    pygame.display.flip()
    