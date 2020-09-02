# coding: utf-8

#import
import hashlib
import pygame
import math
from play.game import Game
from registration.requeteSQL import create_registration
from registration.registration import user_input
from getpass import getpass
from registration.connection import forget_psd
from champ_select.display_champ_select import champ_select
# from champ_select.load_character import Avatar



pygame.init()
pygame.display.set_caption("Projet 2")
screen = pygame.display.set_mode((800, 600))

background_forest = pygame.image.load("images/bg/desert.jpg")
background_champ_select = pygame.image.load("images/bg/background_champ_select.png")
clock = pygame.time.Clock()


game = Game(screen)
# avatar = Avatar(screen)

running = True
# displayer champ_select
champ_select = True

if __name__ == "__main__":

    
    while running :

        # while champ_select :
        #     champ_select(screen, background_champ_select )

        screen.blit(background_forest, (0,0))
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT :
                running = False


            elif event.type == pygame.KEYDOWN :
                game.pressed[event.key] = True

            elif event.type == pygame.KEYUP :
                game.pressed[event.key] = False

            
        game.update(screen)
        # clock.tick(120)
        pygame.display.flip()