# coding : utf-8
import pygame

class Character_rect():

    def __init__(self, x, y):
        self.image = pygame.Surface((28, 15))
        self.rect = self.image.get_rect()
        self.rect.x = x + 2
        self.rect.y = y + 15

