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
# from registration.registration import sign_in
from getpass import getpass
from registration.connection import forget_psd
# from Log_in_n_out.log_in import check_logs
from play import Variables as var
from play.map_obstacles import Obstacle
from play.map import Map
from play.loading_game import start_loading
from registration.connection_form import run_game
from play.object import Object



pygame.init()
pygame.display.set_caption("Projet 2")

screen = pygame.display.set_mode((var.x_screen, var.y_screen))


map_loading = pygame.image.load("images/Bg/chargement.png")
map_loading = pygame.transform.scale(map_loading, (var.x_screen, var.y_screen))

clock = pygame.time.Clock()

game = Game(screen)



# game.map_foret_sol = pygame.image.load("images/Bg/Foret.png")




# game.obstacle = game.create_map("images/bg/mini_map_test_obstacle.tmx", True)
# avatar = Avatar(screen)

# displayer champ_select


if __name__ == "__main__":
    game.validation_champ_select, game.pseudo = run_game()
    running = True
    while running :
        
        if game.play == False and game.validation_champ_select == False:
            start_loading(screen, game, map_loading)
            game.instance_player(screen)
            game.player.inventory.add_list_object("kagari")
            game.play = True

        for event in pygame.event.get():

            if event.type == pygame.QUIT :
                game.update_player()
                running = False

            elif event.type == pygame.KEYDOWN :
                game.pressed[event.key] = True

                if event.key == pygame.K_ESCAPE  :
                    if game.inventory :
                        game.inventory = False

            elif event.type == pygame.KEYUP :
                game.pressed[event.key] = False
                


            if event.type == pygame.MOUSEBUTTONDOWN :
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

                elif game.inventory :
                    for obj in game.player.inventory.list_object :
                        if obj.rect.collidepoint(event.pos) and obj.category == "Outils":
                            game.player.inventory.last_obj = Object([obj.name, obj.quantity, obj.action, obj.category, obj.stamina, obj.food, obj.hydratation, obj.id_parent], 0, 0)
                        elif obj.rect.collidepoint(event.pos) :
                            game.player.inventory.update_vital_sign(obj)
                            game.player.inventory.list_object.remove(obj)
                elif game.play :
                    if game.player.inventory.rect.collidepoint(event.pos) :
                        game.inventory = True

                # elif game.map.mini_map_rect.collidepoint(event.pos) and game.play == True :
                #     game.full_screen_map = True
                #     game.play = False


        




        game.update(screen)
        
        # clock.tick(10)
        pygame.display.flip()