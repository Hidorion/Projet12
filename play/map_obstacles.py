#coding UTF-8

import pygame

class Obstacle(pygame.sprite.Sprite) :

    def __init__(self, x, y, image):

        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = pygame.Rect(x + 10, y, 20, 20)