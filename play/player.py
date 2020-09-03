# coding: utf-8

#import
import math
import pygame



class Player :

    def __init__(self, screen, index):

        self.avatar = f'avatar{index}'
        self.character_image = pygame.image.load(f"images/ressources/{self.avatar}/character_up.png")
        self.character_image = pygame.transform.scale(self.character_image, (math.ceil(screen.get_height() / 25), math.ceil(screen.get_width() / 20)))
        self.character_image_rect = self.character_image.get_rect()
        self.character_image_rect.x = math.ceil(screen.get_width() / 2)
        self.character_image_rect.y = screen.get_height() / 2 - self.character_image.get_height()

        self.health = 10
        self.velocity = 1
        self.move = 0