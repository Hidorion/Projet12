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
# from champ_select.load_character import Avatar



pygame.init()
pygame.display.set_caption("Projet 2")
x_screen = 700
y_screen = 700

screen = pygame.display.set_mode((x_screen, y_screen))




clock = pygame.time.Clock()


game = Game(screen)
# avatar = Avatar(screen)

running = True
# displayer champ_select


if __name__ == "__main__":

    
    while running :
        
        


        for event in pygame.event.get():

            if event.type == pygame.QUIT :
                running = False

            elif event.type == pygame.KEYDOWN :
                game.pressed[event.key] = True

            elif event.type == pygame.KEYUP :
                game.pressed[event.key] = False


            elif event.type == pygame.MOUSEBUTTONDOWN and game.validation_champ_select == True :
                for index, avatar in enumerate(game.champ_select.list_rect_avatar) :
                    if avatar.collidepoint(event.pos) :
                        game.selected_champ = True
                        game.avatar_choose = index
                        game.create_player(screen, index + 1)
                if game.champ_select.button_rect.collidepoint(event.pos) and game.selected_champ == True :
                    game.validation_champ_select = False
                    game.play = True
            
        game.update(screen)
        # clock.tick(120)
        pygame.display.flip()