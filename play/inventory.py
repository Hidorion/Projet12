#coding:utf-8
import pygame
import math

from registration.registration_player import create_registration
from play.object import Object
from play.map import Map

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
        self.list_object_inventory= pygame.sprite.Group()
        self.list_object_map = pygame.sprite.Group()
        
        self.last_obj = ""

    def print_inventory(self, screen) :
        screen.blit(self.interface_inventory, (self.interface_inventory_rect.x, self.interface_inventory_rect.y))
        x = 150
        y = 112
        counter = 0
        for obj in self.list_object_inventory:
            obj.rect.x = x
            obj.rect.y = y
            screen.blit(obj.image, obj.rect)
            x += 95
            counter += 1
            if counter == 10:
                y += 75
                x = 149.5
                counter = 0

        for obj in self.list_object_inventory:
            screen.blit(obj.image, obj.rect)
        

    def add_list_object(self, pseudo):
        sql = create_registration()
        result = sql.read_inventory(pseudo)
        for obj in result :
            self.list_object_inventory.add(Object(obj, 0, 0))
        result = sql.read_information_object("Banane")
        Map("images/Bg/Foret_interaction.tmx", self.player.game).interaction(12800, 0, result)

    def update_vital_sign(self, obj) :
        """ 
            improves the player's vital signs
        """ 
        self.player.stamina += obj.stamina
        self.player.stamina = 100 if self.player.stamina > 100 else self.player.stamina
        self.player.food += obj.food
        self.player.food = 100 if self.player.food > 100 else self.player.food
        self.player.hydratation += obj.hydratation
        self.player.hydratation = 100 if self.player.hydratation > 100 else self.player.hydratation

        self.list_object_inventory.remove(obj)
