# coding: utf-8

#import
import pygame
import math
from play.map import Map
from play.player import Player
from champ_select.champ_select import Avatar


class Game:

    def __init__(self, screen) :
        
        self.map = Map(screen)
        # self.player = Player(screen)
        self.champ_select = Avatar(screen)
        # Permet de définir la dernière direction du personnage
        self.last_movement = "up"
        #Calcul le nombre de tour pour changer l'image du personnage
        self.move = 0
        self.pressed = {}
        self.validation_champ_select = True
        self.selected_champ = False
        self.avatar_choose = 0
        self.play = False
        self.list_image_avatar_x = [self.champ_select.avatar1_image_rect.x, self.champ_select.avatar2_image_rect.x, 
        self.champ_select.avatar3_image_rect.x, self.champ_select.avatar4_image_rect.x, self.champ_select.avatar5_image_rect.x, 
        self.champ_select.avatar6_image_rect.x, self.champ_select.avatar7_image_rect.x, self.champ_select.avatar8_image_rect.x]

        self.list_image_avatar_y = [self.champ_select.avatar1_image_rect.y, self.champ_select.avatar2_image_rect.y, 
        self.champ_select.avatar3_image_rect.y, self.champ_select.avatar4_image_rect.y, self.champ_select.avatar5_image_rect.y, 
        self.champ_select.avatar6_image_rect.y, self.champ_select.avatar7_image_rect.y, self.champ_select.avatar8_image_rect.y]

        # self.list_avatar = ["avatar1", "avatar2", "avatar3", "avatar4", "avatar5", "avatar6", "avatar7", "avatar8"]



    def update(self, screen):

        # self.player.avatar = self.list_avatar[self.avatar_choose]
        if self.play :
            self.movement(screen)
            screen.blit(self.map.background_desert, self.map.background_desert_rect)
            screen.blit(self.player.character_image, self.player.character_image_rect)       

        if self.validation_champ_select :
            screen.blit(self.champ_select.background_champ_select, (0,0))
            if self.selected_champ :
                pygame.draw.rect(screen,(0,0,255),(self.list_image_avatar_x[self.avatar_choose], self.list_image_avatar_y[self.avatar_choose], self.champ_select.avatar1_image.get_width(), self.champ_select.avatar1_image.get_height()))
            self.champ_select.update(screen)

    def create_player(self, screen, index):
        self.player = Player(screen, index)

    def movement(self, screen) :

        # si telle touche est pressée, j'appelle la fonction pour déplacer la carte
        if self.pressed.get(pygame.K_RIGHT) :# and self.map.background_desert_rect.x + self.player.velocity < self.map.background_desert.get_width():
            self.move_right()
            self.last_movement = "right"

        elif self.pressed.get(pygame.K_LEFT) :# and self.map.background_desert_rect.x > - 3200 :
            self.move_left()
            self.last_movement = "left"

        elif self.pressed.get(pygame.K_UP) : #and self.map.background_desert_rect.y > - 3200 :
            self.move_up()
            self.last_movement = "up"

        elif self.pressed.get(pygame.K_DOWN): # and self.map.background_desert_rect.y + self.player.velocity < self.map.background_desert.get_height():
            self.move_down()
            self.last_movement = "down"


        # Met dans la position arrêt le personnage
        if self.pressed.get(pygame.K_RIGHT) == False and self.last_movement == "right" :
            self.player.character_image = pygame.image.load(f"images/ressources/{self.player.avatar}/character_right.png")

        elif self.pressed.get(pygame.K_LEFT) == False and self.last_movement == "left" :
            self.player.character_image = pygame.image.load(f"images/ressources/{self.player.avatar}/character_left.png")

        elif self.pressed.get(pygame.K_UP) == False and self.last_movement == "up" :
            self.player.character_image = pygame.image.load(f"images/ressources/{self.player.avatar}/character_up.png")

        elif self.pressed.get(pygame.K_DOWN) == False and self.last_movement == "down" :
            self.player.character_image = pygame.image.load(f"images/ressources/{self.player.avatar}/character_down.png")



    def move_right(self):

        self.map.background_desert_rect.x -= self.player.velocity
        self.change_image(f"images/ressources/{self.player.avatar}/character_right.png", f"images/ressources/{self.player.avatar}/character_right_move.png" )

    def move_left(self):
        self.map.background_desert_rect.x += self.player.velocity
        self.change_image(f"images/ressources/{self.player.avatar}/character_left.png", f"images/ressources/{self.player.avatar}/character_left_move.png" )

    def move_up(self):
        self.map.background_desert_rect.y += self.player.velocity
        self.change_image(f"images/ressources/{self.player.avatar}/character_up.png", f"images/ressources/{self.player.avatar}/character_up_move.png" )

    def move_down(self):
        self.map.background_desert_rect.y -= self.player.velocity
        self.change_image(f"images/ressources/{self.player.avatar}/character_down.png", f"images/ressources/{self.player.avatar}/character_down_move.png" )

    
    def change_image(self, not_move, move):
        # Pour chaque tour de boucle, move s'agrémente, a partir de 15 l'image change, et se remet normal au bout de 45 tour 
        self.move += 1
        if (self.move >= 0 and self.move <= 15) or self.move >= 45 : 
            self.player.character_image = pygame.image.load(not_move)
        else : 
            self.player.character_image = pygame.image.load(move)
        if self.move == 60 :
            self.move = 0 


        
        