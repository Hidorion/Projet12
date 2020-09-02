# coding: utf-8

#import
import math
import pygame



class Player :

    def __init__(self, screen, pressed):

        self.character_image = pygame.image.load("images/ressources/avatar1/character_up.png")
        self.character_image_rect = self.character_image.get_rect()
        self.character_image_rect.x = math.ceil(screen.get_width() / 2)
        self.character_image_rect.y = screen.get_height() - self.character_image.get_height()

        self.pressed = pressed
        self.health = 10
        self.velocity = 1
        self.move = 0

    def move_right(self):
        self.character_image_rect.x += self.velocity
        self.change_image("images/ressources/avatar1/character_right.png", "images/ressources/avatar1/character_right_move.png" )

    def move_left(self):
        self.character_image_rect.x -= self.velocity
        self.change_image("images/ressources/avatar1/character_left.png", "images/ressources/avatar1/character_left_move.png" )

    def move_up(self):
        self.character_image_rect.y -= self.velocity
        self.change_image("images/ressources/avatar1/character_up.png", "images/ressources/avatar1/character_up_move.png" )

    def move_down(self):
        self.character_image_rect.y += self.velocity
        self.change_image("images/ressources/avatar1/character_down.png", "images/ressources/avatar1/character_down_move.png" )
    
    def change_image(self, not_move, move):
        self.move += 1
        if (self.move >= 0 and self.move <= 15) or self.move >= 45 : 
            self.character_image = pygame.image.load(not_move)
        else : 
            self.character_image = pygame.image.load(move)
        if self.move == 60 :
            self.move = 0
    