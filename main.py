# coding: utf-8

#import module
import hashlib
import pygame
import math
import time
import pytmx
import threading

#import fichier
from core.play.game import Game
from core.registration.sql_queries import create_registration
from core.registration.check_connection import forget_psd
from core.play import variables as var
from core.play.map_obstacles import Obstacle
from core.play.map import Map
from core.play.loading_game import start_loading
from core.registration.connection_form import run_game
from core.play.object import Object



pygame.init()
pygame.display.set_caption("Projet 2")

screen = pygame.display.set_mode((var.x_screen, var.y_screen))

# loading l'image de chargement
map_loading = pygame.image.load("assets/pics/backgrounds_pics/chargement.png")
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
                game.pressed[event.key] = True

                if event.key == pygame.K_ESCAPE  :
                    running = False

            elif event.type == pygame.KEYUP :
                game.pressed[event.key] = False
                # Permet d'ouvrir l'inventaire 
                game.not_pressed[event.key] = True


            if event.type == pygame.MOUSEBUTTONDOWN :
                # Si le champ select est en cours 
                if game.validation_champ_select :
                    # Pour chaque rect d'avatar
                    for index, avatar in enumerate(game.champ_select.list_rect_avatar) :
                        # Si le clique de la souris est en collision avec un avatar
                        if avatar.collidepoint(event.pos) :
                            # Envoi la validation qu'un avatar est selectionné, et envoi  l'index de l'avatar
                            game.selected_champ = True
                            game.avatar_choose = index
                    # Si le champ select est open et que l'utilisateur appui sur valider sans selectionner un avatar
                    if game.champ_select.button_rect.collidepoint(event.pos) and game.selected_champ == False:
                        game.not_select = True
                    # Si le champ select est open et que l'utilisateur a selectionné un avatar
                    elif game.champ_select.button_rect.collidepoint(event.pos) and game.selected_champ == True :
                        game.validation_champ_select = False
                elif game.inventory :
                    # Pour chaque objet dans l'inventaire du player
                    for obj in game.player.inventory.list_object_inventory :
                        # Si l'utilisateur appui sur E et clique sur un objet
                        if obj.rect.collidepoint(event.pos) and game.pressed.get(pygame.K_e) :
                            # Delete de l'objet selectionné
                            game.player.inventory.delete_inventory(obj)
                        
                        elif obj.rect.collidepoint(event.pos) and obj.category == "Outils":
                            game.player.inventory.last_obj = obj
                        # Si l'utilisateur clic sur un objet qui est dans la categorie "ressources"
                        elif obj.rect.collidepoint(event.pos) and obj.category != "Ressource":
                            # Fonction qui met à jour les signes vitaux du player avec les catéristiques de l'objet
                            game.player.inventory.update_vital_sign(obj)
                            # Delete de l'objet
                            game.player.inventory.list_object_inventory.remove(obj)
                    # Si l'utilisateur clic sur le tri dans l'inventaire
                    if game.player.inventory.button_tri_inventory_rect.collidepoint(event.pos) :
                        # Fonction qui envoi les objets dans la BDD pour les récupérer triés
                        game.player.inventory.sort_inventory(game.pseudo)

                elif game.play :
                    # Si l'utilisateur clic sur le sac à dos de l'inventaire
                    if game.player.inventory.rect.collidepoint(event.pos) :
                        game.inventory = True
                        game.play = False



        # Fonction qui met à jour tout le jeu
        game.update(screen)
        pygame.display.flip()