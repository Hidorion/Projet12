#coding:utf-8
import pygame
import math

from registration.registration_player import create_registration
from play.object import Object

class Inventory():

    def __init__(self, screen, player):
        self.player = player
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
        self.list_object = pygame.sprite.Group()
        self.last_obj = ""

    def print_inventory(self, screen) :
        screen.blit(self.interface_inventory, (self.interface_inventory_rect.x, self.interface_inventory_rect.y))
        for obj in self.list_object :
            screen.blit(obj.image, obj.rect)
        

    def add_list_object(self, pseudo):
        sql = create_registration()
        result = sql.read_inventory(pseudo)
        x = 150
        y = 112
        counter = 0
        for obj in result :
            self.list_object.add(Object(obj, x, y))
            x += 95
            counter += 1
            if counter == 10:
                y += 80
                x = 150
                counter = 0

    def update_vital_sign(self, obj) :
        """ 
            improves the player's vital signs
        """ 

        if self.player.stamina + obj.stamina < 100 or self.player.stamina + obj.stamina > 100 :
            self.player.stamina += obj.stamina
        elif self.player.food + obj.food < 100 or self.player.food + obj.food > 100 :
            self.player.food += obj.food
        elif self.player.hydratation + obj.hydratation < 100 or self.player.hydratation + obj.hydratation > 100 :
            self.player.hydratation += obj.hydratation
