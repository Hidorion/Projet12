#coding:utf-8
import pygame
import math

class Inventory():

    def __init__(self, screen):
        self.image = pygame.image.load("images/ressources/interface/bag.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1060
        self.rect.y = 390
        self.interface_inventory = pygame.image.load("images/Bg/inventory.png")
        # print(math.ceil(screen.get_width() - (screen.get_width() / 10 * 2)))
        # print(math.ceil(screen.get_height() - (screen.get_height() / 10 * 2)))
        self.interface_inventory = pygame.transform.scale(self.interface_inventory,( 960 , 576 ))
        self.interface_inventory_rect = self.interface_inventory.get_rect()
        self.interface_inventory_rect.x = screen.get_width() / 10
        self.interface_inventory_rect.y = screen.get_height() / 10

    def print_inventory(self, screen) :
        screen.blit(self.interface_inventory, (self.interface_inventory_rect.x, self.interface_inventory_rect.y))