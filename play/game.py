# coding: utf-8

#import
import pygame
from play.character import Player

class Game:

    def __init__(self, screen) :
        self.pressed = {}
        self.player = Player(screen, self.pressed)
        self.last_movement = "up"
        self.validation_movement = True


    def update(self, screen):

        self.movement(screen)
        screen.blit(self.player.character_image, self.player.character_image_rect)
        


    def movement(self, screen) :

        if self.pressed.get(pygame.K_RIGHT) and self.player.character_image_rect.x + self.player.velocity < screen.get_width() - self.player.character_image.get_width():
            self.player.move_right()
            self.last_movement = "right"

        elif self.pressed.get(pygame.K_LEFT) and self.player.character_image_rect.x - self.player.velocity > 0:
            self.player.move_left()
            self.last_movement = "left"

        elif self.pressed.get(pygame.K_UP) and self.player.character_image_rect.y - self.player.velocity > 0 :
            self.player.move_up()
            self.last_movement = "up"

        elif self.pressed.get(pygame.K_DOWN) and self.player.character_image_rect.y + self.player.velocity < screen.get_height() - self.player.character_image.get_height():
            self.player.move_down()
            self.last_movement = "down"

            
            


        
        