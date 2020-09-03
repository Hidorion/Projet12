# coding: utf-8

#import
import math
import pygame



class Map :

    def __init__(self, screen):

        self.background_desert = pygame.image.load("images/bg/XXL.png")
        self.background_desert_rect = self.background_desert.get_rect()
        self.background_desert_rect.x = 0
        self.background_desert_rect.y = 0

        self.mini_map = pygame.image.load("images/bg/mini_map.png")
        self.mini_map = pygame.transform.scale(self.mini_map, (math.ceil(screen.get_width() /4), math.ceil(screen.get_height() /4)))
        self.mini_map_rect = self.mini_map.get_rect()
        self.mini_map_rect.x = math.ceil(screen.get_height() - screen.get_height() /4)
        self.mini_map_rect.y = math.ceil(screen.get_width() - screen.get_width() /4)

        self.mini_map_full = pygame.image.load("images/bg/mini_map.png")
        self.mini_map_full = pygame.transform.scale(self.mini_map_full, (math.ceil(screen.get_width() +2), math.ceil(screen.get_height() + 2)))
        self.mini_map_full_rect = self.mini_map_full.get_rect()
        self.mini_map_full_rect.x = 0
        self.mini_map_full_rect.y = 0


    



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