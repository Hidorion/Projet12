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
        self.move = 0



    



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