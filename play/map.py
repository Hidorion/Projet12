# coding: utf-8

#import
import math
import pygame
import pytmx
from play.map_obstacles import Obstacle



class Map :

    def __init__(self, file):

        tm = pytmx.load_pygame(file, pixelalpha=True)
        # defini la largeur de la map, le nombre de tuile, et la taille des tuiles
        self.width = tm.width * tm.tilewidth
        # pareil pour la haute, nombre et taille des tuiles
        self.height = tm.height * tm.tileheight
        self.tmx_data = tm
        # Création du groupe de sprite d'obstacle
        self.group_obstacle = pygame.sprite.Group()

    def render(self, surface, cant_walk):
        #sauvegarder la commande
        save_command = self.tmx_data.get_tile_image_by_gid
        # parcourir les couche de la map
        # Pour chaque calque visible
        for layer in self.tmx_data.visible_layers :
            # Vérifier si le layer contient que des tuiles et pas des objets
            if isinstance(layer, pytmx.TiledTileLayer): 
                # pour chaque x, y et id de chaque image
                for x, y, gid, in layer :
                    # Recherche si le l'id correspond a une surface
                    tile = save_command(gid)
                    if tile :
                        if cant_walk :
                            self.group_obstacle.add(Obstacle(x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight, tile))
                        else :
                        # dessiner sur la surface toute les tuiles
                            surface.blit(tile, (x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight))
    
    # creer la surface pour les tile
    def make_map(self, cant_walk):
        temp_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.render(temp_surface, cant_walk)
        return temp_surface
        
        
        
        
        
        # self.layer = self.tm.get_layer_by_name("can_walk1")
        # self.surface = ""
        # for x, y, image in self.layer.tiles():
        #     self.surface.blit(image,(x*32, y*32))
        # # for x, y, image in self.layer2.tiles():
        # #     screen.blit(image,(x*32, y*32))

        # self.tm2 = pytmx.load_pygame('images/Bg/test_mini_map.tmx', pixelalpha=True)
        # self.layer2 = self.tm2.get_layer_by_name("cant_walk2")









        # # self.tm = pygame.image.load("images/bg/XXL.png")
        # # self.tm_rect = self.tm.get_rect()
        # # self.tm_rect.x = 0
        # # self.tm_rect.y = 0

        # self.mini_map = pygame.image.load("images/bg/mini_map.png")
        # self.mini_map = pygame.transform.scale(self.mini_map, (math.ceil(screen.get_width() /4), math.ceil(screen.get_height() /4)))
        # self.mini_map_rect = self.mini_map.get_rect()
        # self.mini_map_rect.x = math.ceil(screen.get_height() - screen.get_height() /4)
        # self.mini_map_rect.y = math.ceil(screen.get_width() - screen.get_width() /4)

        # self.mini_map_full = pygame.image.load("images/bg/mini_map.png")
        # self.mini_map_full = pygame.transform.scale(self.mini_map_full, (math.ceil(screen.get_width() +2), math.ceil(screen.get_height() + 2)))
        # self.mini_map_full_rect = self.mini_map_full.get_rect()
        # self.mini_map_full_rect.x = 0
        # self.mini_map_full_rect.y = 0


    



    # def move_right(self):
    #     self.character_image_rect.x += self.player.velocity
    #     self.change_image("images/ressources/avatar1/character_right.png", "images/ressources/avatar1/character_right_move.png" )

    # def move_left(self):
    #     self.character_image_rect.x -= self.player.velocity
    #     self.change_image("images/ressources/avatar1/character_left.png", "images/ressources/avatar1/character_left_move.png" )

    # def move_up(self):
    #     self.character_image_rect.y -= self.player.velocity
    #     self.change_image("images/ressources/avatar1/character_up.png", "images/ressources/avatar1/character_up_move.png" )

    # def move_down(self):
    #     self.character_image_rect.y += self.player.velocity