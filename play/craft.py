
import pygame
from registration.requeteSQL import create_registration
from play.object import Object
from play.map import Map

class Crafting():
    
    def __init__(self, screen, player):
        self.player = player
        self.crafting_interface = pygame.image.load("images/Bg/crafting.png")
        self.crafting_interface = pygame.transform.scale(self.crafting_interface,( 960 , 576 ))
        self.crafting_interface_rect = self.crafting_interface.get_rect()
        self.crafting_interface_rect.x = screen.get_width() / 10
        self.crafting_interface_rect.y = screen.get_height() / 10
        self.list_object_craft = pygame.sprite.Group()


    def show_crafting(self,screen):
        sql = create_registration()
        player = self.player
        result = sql.read_crafting(player)
        for obj in result :
            self.list_object_craft.add(Object(obj, 0, 0))
        screen.blit(self.crafting_interface, (self.crafting_interface_rect.x, self.crafting_interface_rect.y))
        x = 150
        y = 112
        counter = 0
        for obj in self.list_object_craft:
            obj.rect.x = x
            obj.rect.y = y
            screen.blit(obj.image, obj.rect)
            x += 95
            counter += 1
            if counter == 10:
                y += 75
                x = 149.5
                counter = 0
        for obj in self.list_object_craft:
            screen.blit(obj.image, obj.rect)
