import pygame,sys

from pygame.locals import *
pygame.init()


#Class police
class police:    
    velocity=15
    def __init__(self):
        """
            911 We call the Police !
        """
        self.image=LoadPictures("miniarc.png")
        self.imagerect=self.image.get_rect()
        self.imagerect.left=21
        self.imagerect.top=216
    def Update(self):
        ScoreFont.blit(self.image,self.imagerect)

    def return_height(self):
        return self.imagerect.top
#Class bullet
class bullet:
    bulletspeed=20
    def __init__(self):
        """
            They're shooting at us !
        """
        self.image=LoadPictures("arrow.png")
        self.imagerect=self.image.get_rect()
        self.Height=222
        self.surface=pygame.transform.scale(self.image,(10,7))
        self.imagerect=pygame.Rect(21,self.Height,20,20)
    def Update(self):
        self.imagerect.right-=self.bulletspeed
def ExitGame():
    """
        Function that stops the game
    """
    pygame.quit()
    sys.exit()
def LoadPictures(path):
    """
        Loading the pictures
    """
    return pygame.image.load(path)
#Variables
Width = 1400
Height = 240
Fps = 30
BackGround = pygame.image.load("background.png")
Title = pygame.image.load("background.png")
pygame.display.set_icon(Title)
pygame.display.set_mode((1400, 240))

#Game
clock=pygame.time.Clock()
ScoreFont=pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Shoot'hive")
scorefont=pygame.font.SysFont(None,30)
pygame.display.update()
TopScore=0
police=police()

while True:
    bullet_list=[]
    moveup = movedown = gravity = False
    addcounter=0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                ExitGame()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    moveup = True
                    movedown = False
                    gravity = False
                    
                if event.key == K_ESCAPE:
                    ExitGame()
            if event.type == KEYUP:
                if event.key == K_UP:
                    gravity = True
                    moveup = False
        addcounter += 1
        Add = 20
        if(addcounter == Add):
            addcounter = 0
            newbullet = bullet()
            bullet_list.append(newbullet)
        if(addcounter > Add):
            addcounter = 0
        for b in bullet_list:
            bullet.Update(b)
        for b in bullet_list:
            if b.imagerect.left <= 0:
                bullet_list.remove(b)
        for b in bullet_list:
            ScoreFont.blit(b.surface, b.imagerect)
        police.Update()
        ScoreFont.blit(BackGround, (0,0))
        ScoreFont.blit(police.image,police.imagerect)
        pygame.display.update()
        clock.tick(Fps)
    

