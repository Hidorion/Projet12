# coding: utf-8

#import
import math
import pygame
import pytmx
import random

from play.map_obstacles import Obstacle
from play.object import Object
from play.object import Environment



class Map :

    def __init__(self, file, game):

        self.game = game
        tm = pytmx.load_pygame(file, pixelalpha=True)
        # defini la largeur de la map, le nombre de tuile, et la taille des tuiles
        self.width = tm.width * tm.tilewidth
        # pareil pour la haute, nombre et taille des tuiles
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        #sauvegarder la commande
        save_command = self.tmxdata.get_tile_image_by_gid
        # parcourir les couche de la map
        # Pour chaque calque visible
        for layer in self.tmxdata.visible_layers :
            
            # Vérifier si le layer contient que des tuiles et pas des objets
            if isinstance(layer, pytmx.TiledTileLayer): 
                # pour chaque x, y et id de chaque image
                for x, y, gid, in layer :
                    # Recherche si le l'id correspond a une surface
                    tile = save_command(gid)
                    if tile :
                    # dessiner sur la surface toute les tuiles
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))
    
    # creer la surface pour les tile
    def make_map(self):
        temp_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.render(temp_surface)
        return temp_surface

    def obstacle(self, position_x, position_y) :
        for tile in self.tmxdata:
            # pour chaque tuile qui a le nom de "wall"
            if tile.name == "wall":
                self.game.group_obstacle.add(Obstacle(tile.x + position_x, tile.y + position_y, tile.width, tile.height))

    def interaction(self, position_x, position_y, sql):
        for tile in self.tmxdata:
            if tile.name == "pommier" :
                result = sql.read_information_object("Pomme")
                self.game.player.group_environment.add(Environment(tile.name, "Bois", "hachette", 5, tile.x + position_x, tile.y + position_y - 5))
                self.game.player.inventory.list_object_map.add(Object(result[0], tile.x + position_x + 33, tile.y + position_y + 5))
                self.game.player.inventory.list_object_map.add(Object(result[0], tile.x + position_x + 18, tile.y + position_y + 47))
                self.game.player.inventory.list_object_map.add(Object(result[0], tile.x + position_x + 60, tile.y + position_y + 25))
            elif tile.name == "cocotier" :
                result = sql.read_information_object("Noix de coco")
                self.game.player.group_environment.add(Environment(tile.name, "Bois", "hachette", 5, tile.x + position_x -1, tile.y + position_y - 5))
                self.game.player.inventory.list_object_map.add(Object(result[0], tile.x + position_x + 40, tile.y + position_y + 30))
                self.game.player.inventory.list_object_map.add(Object(result[0], tile.x + position_x + 5, tile.y + position_y + 40))
            elif tile.name == "bananier" :
                result = sql.read_information_object("Banane")
                self.game.player.group_environment.add(Environment(tile.name, "Bois", "hachette", 5, tile.x + position_x -1, tile.y + position_y - 5))
                self.game.player.inventory.list_object_map.add(Object(result[0], tile.x + position_x + 40, tile.y + position_y + 27))
                self.game.player.inventory.list_object_map.add(Object(result[0], tile.x + position_x + 5, tile.y + position_y + 37))
            elif tile.name == "ananas" :
                result = sql.read_information_object("Ananas")
                self.game.player.inventory.list_object_map.add(Object(result[0], tile.x + position_x, tile.y + position_y))
            elif tile.name == "carotte" :
                result = sql.read_information_object("Carotte")
                self.game.player.inventory.list_object_map.add(Object(result[0], tile.x + position_x, tile.y + position_y))
                

        
        
        
        
