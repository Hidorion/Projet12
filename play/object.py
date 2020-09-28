# coding:utf-8

import pygame
import math

class Object(pygame.sprite.Sprite):
    """
        Create the object class for the inventory
    """
    def __init__(self, list_inventaire, x, y) :
        pygame.sprite.Sprite.__init__(self)
        
        self.name = list_inventaire[0].lower()
        self.quantity = list_inventaire[1]
        self.action = list_inventaire[2]
        self.category = list_inventaire[3]
        self.image = pygame.image.load(f"images/ressources/Objets/{self.name}.png")
        self.image = pygame.transform.scale(self.image, (50, 42))
        self.rect = self.image.get_rect()
        self.stamina = list_inventaire[4]
        self.food = list_inventaire[5]
        self.hydratation = list_inventaire[6]
        self.id_parent = list_inventaire[7]
        self.rect.x = x 
        self.rect.y = y