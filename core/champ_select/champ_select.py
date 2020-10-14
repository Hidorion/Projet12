# coding: utf-8

#import
import pygame
import math
import math

class Avatar :

    def __init__(self, screen):

        

        self.background_champ_select = pygame.image.load("images/bg/background_champ_select.png").convert_alpha()
        self.background_champ_select = pygame.transform.scale(self.background_champ_select, (screen.get_width(), screen.get_height()))

        self.avatar1_image = pygame.image.load("images/ressources/avatar1/character_down.png")
        self.avatar1_image = pygame.transform.scale(self.avatar1_image, (math.ceil(screen.get_height() / 4), math.ceil(screen.get_width() / 6)))
        self.avatar1_image_rect = self.avatar1_image.get_rect()
        self.avatar1_image_rect.x = math.ceil(screen.get_width() / 15.6)
        self.avatar1_image_rect.y = screen.get_height() / 4.8

        self.avatar2_image = pygame.image.load("images/ressources/avatar2/character_down.png")
        self.avatar2_image = pygame.transform.scale(self.avatar2_image, (math.ceil(screen.get_height() / 4), math.ceil(screen.get_width() / 6)))
        self.avatar2_image_rect = self.avatar2_image.get_rect()
        self.avatar2_image_rect.x =  math.ceil(screen.get_width() / 3.33)
        self.avatar2_image_rect.y = self.avatar1_image_rect.y

        self.avatar3_image = pygame.image.load("images/ressources/avatar3/character_down.png")
        self.avatar3_image = pygame.transform.scale(self.avatar3_image, (math.ceil(screen.get_height() / 4), math.ceil(screen.get_width() / 6)))
        self.avatar3_image_rect = self.avatar3_image.get_rect()
        self.avatar3_image_rect.x = math.ceil(screen.get_width() / 1.88)
        self.avatar3_image_rect.y = self.avatar1_image_rect.y

        self.avatar4_image = pygame.image.load("images/ressources/avatar4/character_down.png")
        self.avatar4_image = pygame.transform.scale(self.avatar4_image, (math.ceil(screen.get_height() / 4), math.ceil(screen.get_width() / 6)))
        self.avatar4_image_rect = self.avatar4_image.get_rect()
        self.avatar4_image_rect.x = math.ceil(screen.get_width() / 1.3)
        self.avatar4_image_rect.y = self.avatar1_image_rect.y

        self.avatar5_image = pygame.image.load("images/ressources/avatar5/character_down.png")
        self.avatar5_image = pygame.transform.scale(self.avatar5_image, (math.ceil(screen.get_height() / 4), math.ceil(screen.get_width() / 6)))
        self.avatar5_image_rect = self.avatar5_image.get_rect()
        self.avatar5_image_rect.x = math.ceil(screen.get_width() / 15.6)
        self.avatar5_image_rect.y = screen.get_height() / 1.78

        self.avatar6_image = pygame.image.load("images/ressources/avatar6/character_down.png")
        self.avatar6_image = pygame.transform.scale(self.avatar6_image, (math.ceil(screen.get_height() / 4), math.ceil(screen.get_width() / 6)))
        self.avatar6_image_rect = self.avatar6_image.get_rect()
        self.avatar6_image_rect.x = math.ceil(screen.get_width() / 3.33)
        self.avatar6_image_rect.y = self.avatar5_image_rect.y

        self.avatar7_image = pygame.image.load("images/ressources/avatar7/character_down.png")
        self.avatar7_image = pygame.transform.scale(self.avatar7_image, (math.ceil(screen.get_height() / 4), math.ceil(screen.get_width() / 6)))
        self.avatar7_image_rect = self.avatar7_image.get_rect()
        self.avatar7_image_rect.x = math.ceil(screen.get_width() / 1.88)
        self.avatar7_image_rect.y = self.avatar5_image_rect.y

        self.avatar8_image = pygame.image.load("images/ressources/avatar8/character_down.png")
        self.avatar8_image = pygame.transform.scale(self.avatar8_image, (math.ceil(screen.get_height() / 4), math.ceil(screen.get_width() / 6)))
        self.avatar8_image_rect = self.avatar8_image.get_rect()
        self.avatar8_image_rect.x = math.ceil(screen.get_width() / 1.3)
        self.avatar8_image_rect.y = self.avatar5_image_rect.y

        self.button = pygame.image.load("images/button/button_champ.png").convert_alpha()
        self.button = pygame.transform.scale(self.button, (math.ceil(screen.get_height() / 2), math.ceil(screen.get_width() / 18 )))
        self.button_rect = self.button.get_rect()
        self.button_rect.x = math.ceil(screen.get_width() / 2 - self.button.get_width() / 2)
        self.button_rect.y = math.ceil(screen.get_height() / 1.15)

        self.list_rect_avatar = [self.avatar1_image_rect, self.avatar2_image_rect, self.avatar3_image_rect, self.avatar4_image_rect, self.avatar5_image_rect, self.avatar6_image_rect, self.avatar7_image_rect, self.avatar8_image_rect]
        

    def update(self, screen) :

        screen.blit(self.avatar1_image, self.avatar1_image_rect)
        screen.blit(self.avatar2_image, self.avatar2_image_rect)
        screen.blit(self.avatar3_image, self.avatar3_image_rect)
        screen.blit(self.avatar4_image, self.avatar4_image_rect)
        screen.blit(self.avatar5_image, self.avatar5_image_rect)
        screen.blit(self.avatar6_image, self.avatar6_image_rect)
        screen.blit(self.avatar7_image, self.avatar7_image_rect)
        screen.blit(self.avatar8_image, self.avatar8_image_rect)
        screen.blit(self.button, self.button_rect)
