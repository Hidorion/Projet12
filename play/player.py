# coding: utf-8

#import
import math
import pygame

from play.map import Map
from play.rect_character import Rect_character



class Player (pygame.sprite.Sprite) :

<<<<<<< Updated upstream
    def __init__(self, screen, index, game):
=======
    def __init__(self, screen, game, avatar, x, y, stamina, food, hydratation):
>>>>>>> Stashed changes
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.avatar = f'avatar{index}'
        self.image = pygame.image.load(f"images/ressources/{self.avatar}/character_up.png")
        self.image = pygame.transform.scale(self.image, (32 , 32))
        self.rect = self.image.get_rect()
<<<<<<< Updated upstream
        self.rect.x = 8000
        self.rect.y = 9000
=======
        self.rect.x = x
        self.rect.y = y
        self.stamina = stamina
        self.food = food 
        self.hydratation = hydratation
>>>>>>> Stashed changes
        # self.rect = pygame.Rect(self.rect.x, self.rect.y, 32, 32)

        self.map_x = 0
        self.map_y = 0
        
        self.group_obstacle = ""

        self.health = 10
        self.velocity = 2
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

    def interface_player(self, screen):
        food = pygame.image.load("images/ressources/interface/food.png")
        stamina = pygame.image.load("images/ressources/interface/stamina.png")
        hydratation = pygame.image.load("images/ressources/interface/hydratation.png")
        support_map =pygame.image.load("images/ressources/interface/support_map.png")
        bag_image = pygame.image.load("images/ressources/interface/bag.png")
        bag_rect = bag_image.get_rect()
        
        # x, y, largeur, hauteur
        pygame.draw.rect(screen, (51, 51, 51), [0,  math.ceil(screen.get_height() - screen.get_height() / 6.54), 
        math.ceil(screen.get_width() / 1.38), math.ceil(screen.get_height() / 5.3)]) 
        screen.blit(food, (10, screen.get_height() - 105))
        screen.blit(stamina, (10, screen.get_height() - 67))
        screen.blit(hydratation, (10, screen.get_height() - 30))
        screen.blit(support_map, (995, 510))
        screen.blit(bag_image, (1060, 390))
        pygame.draw.rect(screen, (230,81,25), [food.get_height() + 20, screen.get_height() - 95, self.food * 8 ,8])
        pygame.draw.rect(screen, (239,184,41), [stamina.get_height() + 20, screen.get_height() - 57, self.stamina * 8 ,8])
        pygame.draw.rect(screen, (67,93,255), [hydratation.get_height() + 20, screen.get_height() - 20, self.hydratation * 8 ,8])
        pygame.draw.rect(screen, (179, 179, 179), [0,  (math.ceil(screen.get_height() - (screen.get_height() / 6.54 + screen.get_width() / 10))), 
        math.ceil(screen.get_width() / 10), math.ceil(screen.get_height() / 6)])


