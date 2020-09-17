# coding: utf-8

#import
import hashlib
import pygame
import math
import time
from play.game import Game
from registration.requeteSQL import create_registration
from registration.registration import sign_in
from getpass import getpass
from registration.connection import forget_psd
from Log_in_n_out.log_in import check_logs
from play import Variables as var
from play.camera import Camera
# from champ_select.load_character import Avatar



pygame.init()
pygame.display.set_caption("Projet 2")

screen = pygame.display.set_mode((var.x_screen, var.y_screen))




clock = pygame.time.Clock()

cam = Camera(var.x_screen // 2, var.y_screen // 2)
game = Game(screen)


game.map_foret_sol = game.create_map("images/bg/Foret.tmx", False)
game.map_foret_behind = game.create_map("images/bg/Foret_behind.tmx", False)

game.map_montagne_sol = game.create_map("images/bg/Montagne.tmx", False)
game.map_montagne_behind = game.create_map("images/bg/Montagne_behind.tmx", False)

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
                                                
        #cam.apply(game.map_rect)
        #cam.apply(game.map_rect)    
        game.update(screen)
        
        # clock.tick(10)
        pygame.display.flip()