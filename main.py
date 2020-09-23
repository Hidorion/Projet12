# coding: utf-8

#import module
import hashlib
import pygame
import math
import time
import pytmx
import threading

#import fichier
from play.game import Game
from registration.requeteSQL import create_registration
from registration.registration import sign_in
from getpass import getpass
from registration.connection import forget_psd
from Log_in_n_out.log_in import check_logs
from play import Variables as var
from play.map_obstacles import Obstacle
from play.map import Map
from play.loading_game import start_loading



pygame.init()
pygame.display.set_caption("Projet 2")

screen = pygame.display.set_mode((var.x_screen, var.y_screen))


map_loading = pygame.image.load("images/Bg/chargement.png")

clock = pygame.time.Clock()

game = Game(screen)



# game.map_foret_sol = pygame.image.load("images/Bg/Foret.png")




# game.obstacle = game.create_map("images/bg/mini_map_test_obstacle.tmx", True)
# avatar = Avatar(screen)

# displayer champ_select


if __name__ == "__main__":
    # Checkplayer = int(input("Que voulez vous faire ? : \n(1 Inscription - 2 Connexion - 3 Mot de passe oublié) "))
    # if Checkplayer == 1:
    #     sign_in()
    # elif Checkplayer == 2:
    #     check_logs()
    # elif Checkplayer == 3:
    #     forget_psd()
    # else:
    #     sign_in()
    running = True
    while running :
        
        if game.play == False :                     
            start_loading(screen, game, map_loading)
            game.play = True


        for event in pygame.event.get():

            if event.type == pygame.QUIT :
                running = False

            elif event.type == pygame.KEYDOWN :
                game.pressed[event.key] = True

                if event.key == pygame.K_ESCAPE and game.full_screen_map == True :
                    game.full_screen_map = False
                    game.play = True

            elif event.type == pygame.KEYUP :
                game.pressed[event.key] = False
                


            elif event.type == pygame.MOUSEBUTTONDOWN :
                if game.validation_champ_select :
                    for index, avatar in enumerate(game.champ_select.list_rect_avatar) :
                        if avatar.collidepoint(event.pos) :
                            game.selected_champ = True
                            game.avatar_choose = index
                            # game.create_player(screen, index + 1)

                    if game.champ_select.button_rect.collidepoint(event.pos) and game.selected_champ == False:
                        game.not_select = True
                    elif game.champ_select.button_rect.collidepoint(event.pos) and game.selected_champ == True :
                        game.validation_champ_select = False
                        game.play = True

                # elif game.map.mini_map_rect.collidepoint(event.pos) and game.play == True :
                #     game.full_screen_map = True
                #     game.play = False

        
       



        game.update(screen)
        
        # clock.tick(10)
        pygame.display.flip()