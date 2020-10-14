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
from getpass import getpass
from registration.connection import forget_psd
from play import Variables as var
from play.map_obstacles import Obstacle
from play.map import Map
from play.loading_game import start_loading
from registration.connection_form import run_game
from play.object import Object



pygame.init()
pygame.display.set_caption("Projet 2")

screen = pygame.display.set_mode((var.x_screen, var.y_screen))

# loading l'image de chargement
map_loading = pygame.image.load("images/Bg/chargement.png")
map_loading = pygame.transform.scale(map_loading, (var.x_screen, var.y_screen))

# Instancier la class game 
game = Game(screen)


if __name__ == "__main__":
    # Fonction qui lance le login, récupération de True si inscription, False si connexion. Récupération du nom du pseudo
    game.validation_champ_select, game.pseudo = run_game()
    running = True
    while running :
        # Lancement du chargement des map avec la barre de chargement
        if game.loading :
            # Lancement des deux Thread, un pour charger les map et l'autre pour l'animation de chargement
            start_loading(screen, game, map_loading)
            # Fonction qui enregistre le joueur dans la table player, puis instancier le player
            game.instance_player(screen)
            # Fonction qui récupère les objets du player dans la BDD et les add a l'inventaire du player
            game.player.inventory.add_list_object(game.pseudo)
            game.play = True
            game.loading = False

        for event in pygame.event.get():
            # Si l'utilisation quitte le jeu
            if event.type == pygame.QUIT :
                # Fonction met à jour les informations du player dans pas BDD
                game.update_player()
                # Fonction qui envoi au serveur que le player se déconnecte
                game.data_exchange("disconnect")
                running = False

            elif event.type == pygame.KEYDOWN :
                game.move = True 
                game.pressed[event.key] = True

                if event.key == pygame.K_ESCAPE  :
                    if game.inventory :
                        game.inventory = False

            elif event.type == pygame.KEYUP :
                game.move = False
                game.pressed[event.key] = False
                game.not_pressed[event.key] = True


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
                    for obj in game.player.inventory.list_object_inventory :
                        if obj.rect.collidepoint(event.pos) and game.pressed.get(pygame.K_e) :
                            game.player.inventory.delete_inventory(obj)
                        elif obj.rect.collidepoint(event.pos) and obj.category == "Outils":
                            game.player.inventory.last_obj = obj
                        elif obj.rect.collidepoint(event.pos) and obj.category != "Ressource":
                            game.player.inventory.update_vital_sign(obj)
                            game.player.inventory.list_object_inventory.remove(obj)
                    if game.player.inventory.button_tri_inventory_rect.collidepoint(event.pos) :
                        game.player.inventory.sort_inventory(game.pseudo)

                elif game.play :
                    if game.player.inventory.rect.collidepoint(event.pos) :
                        game.inventory = True
                        game.play = False




        game.update(screen)
        # clock.tick(10)
        pygame.display.flip()