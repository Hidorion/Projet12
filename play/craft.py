import pygame
from registration.requeteSQL import create_registration


class Crafting():
    
    def __init__(self, screen, player):
        self.player = player
        self.crafting_interface = pygame.image.load("images/Bg/crafting.png")
        self.crafting_interface = pygame.transform.scale(self.crafting_interface,( 960 , 576 ))
        self.crafting_interface_rect = self.crafting_interface.get_rect()
        self.crafting_interface_rect.x = screen.get_width() / 10
        self.crafting_interface_rect.y = screen.get_height() / 10
        self.crafting_interface = pygame.transform.scale(self.crafting_interface,( 960 , 576 ))
        self.crafting_interface_rect = self.crafting_interface.get_rect()
        self.crafting_interface_rect.x = screen.get_width() / 10
        self.crafting_interface_rect.y = screen.get_height() / 10


    def show_crafting(screen,self):
        screen.blit(self.crafting_interface, (self.crafting_interface_rect.x, self.crafting_interface_rect.y))


