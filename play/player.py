# coding: utf-8

#import
import math
import pygame
from play.map import Map
from play.rect_character import Rect_character



class Player (pygame.sprite.Sprite) :

    def __init__(self, screen, index, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.avatar = f'avatar{index}'
        self.image = pygame.image.load(f"images/ressources/{self.avatar}/character_up.png")
        self.image = pygame.transform.scale(self.image, (32 , 32))
        self.rect = self.image.get_rect()
        self.rect.x = 8000
        self.rect.y = 9000
        # self.rect = pygame.Rect(self.rect.x, self.rect.y, 32, 32)

        self.map_x = 0
        self.map_y = 0
        
        self.group_obstacle = pygame.sprite.Group()

        self.health = 10
        self.velocity = 1
        self.move = 0

        self.rect_character = Rect_character(self.rect.x, self.rect.y)


        # self.map_foret = Map("images/bg/Foret_obstacle.tmx", self)
        # self.map_img_foret = self.map_foret.obstacle(self.game.map_foret_sol)

        # self.map_montagne = Map("images/bg/Montagne_obstacle.tmx", self)
        # self.map_img_montagne = self.map_montagne.make_map(True)


        self.group_player = pygame.sprite.Group()
        self.group_player.add(self)
        

        # Déplace la carte en fonction des touche pressé
    def move_right(self, screen):
        
        self.rect_character.rect.x += self.velocity
        self.rect.x += self.velocity
        self.change_image(f"images/ressources/{self.avatar}/character_right.png", f"images/ressources/{self.avatar}/character_right_move.png" )
        self.image = pygame.transform.scale(self.image, (32, 32 ))
        if pygame.sprite.spritecollideany(self.rect_character, self.group_obstacle):
            self.rect.x -= self.velocity
            self.rect_character.rect.x -= self.velocity
 

    def move_left(self, screen): 

        self.rect_character.rect.x -= self.velocity
        self.rect.x -= self.velocity
        self.change_image(f"images/ressources/{self.avatar}/character_left.png", f"images/ressources/{self.avatar}/character_left_move.png" )
        self.image = pygame.transform.scale(self.image, (32, 32 ))
        if pygame.sprite.spritecollideany(self.rect_character, self.group_obstacle):
            self.rect.x += self.velocity
            self.rect_character.rect.x += self.velocity

    def move_up(self, screen):

        self.rect_character.rect.y -= self.velocity
        self.rect.y -= self.velocity
        self.change_image(f"images/ressources/{self.avatar}/character_up.png", f"images/ressources/{self.avatar}/character_up_move.png" )
        self.image = pygame.transform.scale(self.image, (32, 32 ))
        if pygame.sprite.spritecollideany(self.rect_character, self.group_obstacle):
            self.rect.y += self.velocity
            self.rect_character.rect.y += self.velocity

    def move_down(self, screen):
        
        self.rect_character.rect.y += self.velocity
        self.rect.y += self.velocity
        self.change_image(f"images/ressources/{self.avatar}/character_down.png", f"images/ressources/{self.avatar}/character_down_move.png" )
        self.image = pygame.transform.scale(self.image, (32, 32 ))
        if pygame.sprite.spritecollideany(self.rect_character, self.group_obstacle):
            self.rect.y -= self.velocity
            self.rect_character.rect.y -= self.velocity

    def change_image(self, not_move, move):
        # Pour chaque tour de boucle, move s'agrémente, a partir de 15 l'image change, et se remet normal au bout de 45 tour 
        self.move += 1
        if (self.move >= 0 and self.move <= 15) or self.move >= 45 : 
            self.image = pygame.image.load(not_move)
        else : 
            self.image = pygame.image.load(move)
        if self.move == 60 :
            self.move = 0 