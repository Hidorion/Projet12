#coding UTF-8

import pygame

class Obstacle(pygame.sprite.Sprite) :

    def __init__(self, x, y, width, height):

        pygame.sprite.Sprite.__init__(self)
        # self.image = image
        self.rect = pygame.Rect(x, y, width, height)