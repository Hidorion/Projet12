#coding:utf-8
import pygame
import math
import random

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

        self.button_tri_inventory = pygame.image.load("images/button/button_tri_inventory.png")
        self.button_tri_inventory_rect = self.button_tri_inventory.get_rect()
        self.button_tri_inventory_rect.x = 990
        self.button_tri_inventory_rect.y = 555

        # print(math.ceil(screen.get_width() - (screen.get_width() / 10 * 2)))
        # print(math.ceil(screen.get_height() - (screen.get_height() / 10 * 2)))
        self.interface_inventory = pygame.transform.scale(self.interface_inventory,( 960 , 576 ))
        self.interface_inventory_rect = self.interface_inventory.get_rect()
        self.interface_inventory_rect.x = screen.get_width() / 10
        self.interface_inventory_rect.y = screen.get_height() / 10
        self.list_object_inventory = pygame.sprite.Group()
        
        
        self.last_obj = ""

    def print_inventory(self, screen) :
        screen.blit(self.interface_inventory, (self.interface_inventory_rect.x, self.interface_inventory_rect.y))
        x = 150
        y = 112
        counter = 0
        for obj in self.list_object_inventory:
            if obj.name == "eau" and obj.quantity == 100:
                obj.image = pygame.transform.scale(pygame.image.load(f"images/ressources/Objets/eau.png"), (50, 42))
            elif obj.name == "eau" and obj.quantity == 0: 
                obj.image = pygame.transform.scale(pygame.image.load(f"images/ressources/Objets/eau_vide.png"), (50, 42))
            else : 
                obj.image = pygame.transform.scale(pygame.image.load(f"images/ressources/Objets/{obj.name}.png"), (50, 42))
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
        screen.blit(self.button_tri_inventory, self.button_tri_inventory_rect)
        

    def add_list_object(self, pseudo):
        sql = create_registration()
        result = sql.read_inventory(pseudo)
        for obj in result :
            self.list_object_inventory.add(Object(obj, 0, 0))

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

        

    def pick_up_object(self, game):
        
        """
            Collision avec les fruit, les delete et les add a l'inventaire
        """
        if len(self.list_object_inventory) < 69 :
            for obj in self.player.game.group_object :
                if self.player.rect_character.rect.colliderect(obj.rect) and self.player.game.pressed.get(pygame.K_q):
                    self.list_object_inventory.add(obj)
                    self.player.game.group_object.remove(obj)

    def delete_inventory(self, obj):

        self.player.game.group_object.add(obj)
        obj.rect.x = self.player.rect_character.rect.x + random.randint(-30, 30)
        obj.rect.y = self.player.rect_character.rect.y + random.randint(-30, 30)
        self.list_object_inventory.remove(obj)

    def sort_inventory(self, pseudo):

        sql = create_registration()
        sql.delete_table_inventory(self.player.id_player)
        # Pour chaque objet dans l'inventaire, je l'ajouet à la BDD
        for obj in self.list_object_inventory :
            sql.add_inventory(self.player.id_player, obj.id_object, obj.quantity)
        self.list_object_inventory = pygame.sprite.Group()
        result = sql.read_inventory(pseudo)
        for obj in result :
            self.list_object_inventory.add(Object(obj, 0, 0))

    def delete_add_wood(self, obj):
        self.update_vital_sign(self.last_obj)
        sql = create_registration()
        result = sql.read_information_object(obj.object)
        for loop in range(obj.quantity):
            if len(self.list_object_inventory) < 69 :
                self.list_object_inventory.add(Object(result[0], 0, 0))
        self.player.game.group_tree.remove(obj)

    def move_tree(self, obj):
        obj.pv -= 1
        
        if self.player.rect_character.rect.x  > obj.rect.x + obj.image.get_width() / 2:
            obj.image = pygame.transform.rotate(obj.image, 15)
            obj.rect.x -= 23
            obj.rect.y -= 7
            for fruit in self.player.game.list_object_map :
                if fruit.rect.colliderect(obj.rect) :
                    fruit.rect.x += -12
                    fruit.rect.y += 3

        else :
            obj.image = pygame.transform.rotate(obj.image, - 15)
            obj.rect.x += -3
            obj.rect.y += -5
            for fruit in self.player.game.list_object_map :
                if fruit.rect.colliderect(obj.rect) :
                    fruit.rect.x += 10
                    fruit.rect.y += 5

    def drop_fruit(self, obj) :
        obj.pv -= 1
        for fruit in self.player.game.list_object_map :
                if fruit.rect.colliderect(obj.rect) :
                    fruit.rect.y = obj.rect.y + obj.image.get_height() / 1.3
                    self.player.game.group_object.add(fruit)
                    self.player.game.list_object_map.remove(fruit)
    
    def interaction_tree(self, obj):
        if obj.pv == 3:
            self.move_tree(obj)
        elif obj.pv == 2 :
            self.drop_fruit(obj)
        else : 
            self.delete_add_wood(obj)

    def first_break_stone(self, obj):
        obj.pv -= 1
        obj.image = pygame.image.load(f"images/ressources/environment/{obj.name}2.png")
        sql = create_registration()
        result = sql.read_information_object(obj.object)
        for loop in range(2):
            if len(self.list_object_inventory) < 69 :
                self.list_object_inventory.add(Object(result[0], 0, 0))
        self.update_vital_sign(self.last_obj)

    def seconde_break_stone(self, obj) :
        obj.pv -= 1
        self.update_vital_sign(self.last_obj)
        sql = create_registration()
        result = sql.read_information_object(obj.object)
        if len(self.list_object_inventory) < 69 :
            self.list_object_inventory.add(Object(result[0], 0, 0))
        self.player.game.group_stone.remove(obj)

    def interaction_stone(self, obj):
        if obj.pv == 3 :
            self.first_break_stone(obj)
        elif obj.pv == 2 :
            self.seconde_break_stone(obj)

        
