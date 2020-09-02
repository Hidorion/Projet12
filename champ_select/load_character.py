# coding: utf-8

#import
import pygame
import math

class Avatar :

    def __init__(self, screen):

        self.avatar1_image = pygame.image.load("images/ressources/avatar1/character_down.png")
        self.avatar1_image = pygame.transform.scale(self.avatar1_image, (120, 160))
        self.avatar1_image_rect = self.avatar1_image.get_rect()
        self.avatar1_image_rect.x = math.ceil(screen.get_width() / 15.5)
        self.avatar1_image_rect.y = screen.get_height() / 6

        self.avatar2_image = pygame.image.load("images/ressources/avatar2/character_down.png")
        self.avatar2_image = pygame.transform.scale(self.avatar2_image, (120, 160))
        self.avatar2_image_rect = self.avatar2_image.get_rect()
        self.avatar2_image_rect.x =  self.avatar1_image_rect.x + 188
        self.avatar2_image_rect.y = screen.get_height() / 6

        self.avatar3_image = pygame.image.load("images/ressources/avatar3/character_down.png")
        self.avatar3_image = pygame.transform.scale(self.avatar3_image, (120, 160))
        self.avatar3_image_rect = self.avatar3_image.get_rect()
        self.avatar3_image_rect.x = self.avatar2_image_rect.x + 188
        self.avatar3_image_rect.y = screen.get_height() / 6

        self.avatar4_image = pygame.image.load("images/ressources/avatar4/character_down.png")
        self.avatar4_image = pygame.transform.scale(self.avatar4_image, (120, 160))
        self.avatar4_image_rect = self.avatar4_image.get_rect()
        self.avatar4_image_rect.x = self.avatar3_image_rect.x + 188
        self.avatar4_image_rect.y = screen.get_height() / 6

        self.avatar5_image = pygame.image.load("images/ressources/avatar5/character_down.png")
        self.avatar5_image = pygame.transform.scale(self.avatar5_image, (120, 160))
        self.avatar5_image_rect = self.avatar5_image.get_rect()
        self.avatar5_image_rect.x = math.ceil(screen.get_width() / 15.5)
        self.avatar5_image_rect.y = screen.get_height() / 1.92

        self.avatar6_image = pygame.image.load("images/ressources/avatar6/character_down.png")
        self.avatar6_image = pygame.transform.scale(self.avatar6_image, (120, 160))
        self.avatar6_image_rect = self.avatar6_image.get_rect()
        self.avatar6_image_rect.x = self.avatar1_image_rect.x + 188
        self.avatar6_image_rect.y = screen.get_height() / 1.92

        self.avatar7_image = pygame.image.load("images/ressources/avatar7/character_down.png")
        self.avatar7_image = pygame.transform.scale(self.avatar7_image, (120, 160))
        self.avatar7_image_rect = self.avatar7_image.get_rect()
        self.avatar7_image_rect.x = self.avatar2_image_rect.x + 188
        self.avatar7_image_rect.y = screen.get_height() / 1.92

        self.avatar8_image = pygame.image.load("images/ressources/avatar8/character_down.png")
        self.avatar8_image = pygame.transform.scale(self.avatar8_image, (120, 160))
        self.avatar8_image_rect = self.avatar8_image.get_rect()
        self.avatar8_image_rect.x = self.avatar3_image_rect.x + 188
        self.avatar8_image_rect.y = screen.get_height() / 1.92

    def update(self, screen) :

        screen.blit(self.avatar1_image, self.avatar1_image_rect)
        screen.blit(self.avatar2_image, self.avatar2_image_rect)
        screen.blit(self.avatar3_image, self.avatar3_image_rect)
        screen.blit(self.avatar4_image, self.avatar4_image_rect)
        screen.blit(self.avatar5_image, self.avatar5_image_rect)
        screen.blit(self.avatar6_image, self.avatar6_image_rect)
        screen.blit(self.avatar7_image, self.avatar7_image_rect)
        screen.blit(self.avatar8_image, self.avatar8_image_rect)
