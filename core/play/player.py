# coding: utf-8

#import
import math
import pygame

from core.play.map import Map
from core.play.character_rect import Character_rect
from core.play.inventory import Inventory
from core.play import variables as var



class Player (pygame.sprite.Sprite) :

    def __init__(self, screen, game, avatar, x, y, stamina, food, hydratation, id_player):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.avatar = avatar
        self.image = pygame.image.load(f"assets/avatars/{self.avatar}/character_up.png")
        self.image = pygame.transform.scale(self.image, (32 , 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.id_player = id_player
        self.stamina = stamina
        self.food = food 
        self.hydratation = hydratation
        

        self.game.group_obstacle = ""

        self.health = 10
        self.velocity = 3
        self.move = 0

        self.character_rect = Character_rect(self.rect.x, self.rect.y)

        self.inventory = Inventory(screen, self)

        self.group_player = pygame.sprite.Group()
        self.group_player.add(self)
        var.last_move = f"assets/avatars/{self.avatar}/character_down.png"

        # Déplace la carte en fonction des touche pressé
    def move_right(self, screen):
        
        self.character_rect.rect.x += self.velocity
        self.rect.x += self.velocity
        self.change_image(f"assets/avatars/{self.avatar}/character_right.png", f"assets/avatars/{self.avatar}/character_right_move.png" )
        self.image = pygame.transform.scale(self.image, (32, 32 ))
        if pygame.sprite.spritecollideany(self.character_rect, self.game.group_obstacle):
            self.rect.x -= self.velocity
            self.character_rect.rect.x -= self.velocity
 

    def move_left(self, screen): 

        self.character_rect.rect.x -= self.velocity
        self.rect.x -= self.velocity
        self.change_image(f"assets/avatars/{self.avatar}/character_left.png", f"assets/avatars/{self.avatar}/character_left_move.png" )
        self.image = pygame.transform.scale(self.image, (32, 32 ))
        if pygame.sprite.spritecollideany(self.character_rect, self.game.group_obstacle):
            self.rect.x += self.velocity
            self.character_rect.rect.x += self.velocity

    def move_up(self, screen):

        self.character_rect.rect.y -= self.velocity
        self.rect.y -= self.velocity
        self.change_image(f"assets/avatars/{self.avatar}/character_up.png", f"assets/avatars/{self.avatar}/character_up_move.png" )
        self.image = pygame.transform.scale(self.image, (32, 32 ))
        if pygame.sprite.spritecollideany(self.character_rect, self.game.group_obstacle):
            self.rect.y += self.velocity
            self.character_rect.rect.y += self.velocity

    def move_down(self, screen):
        
        self.character_rect.rect.y += self.velocity
        self.rect.y += self.velocity
        self.change_image(f"assets/avatars/{self.avatar}/character_down.png", f"assets/avatars/{self.avatar}/character_down_move.png" )
        self.image = pygame.transform.scale(self.image, (32, 32 ))
        if pygame.sprite.spritecollideany(self.character_rect, self.game.group_obstacle):
            self.rect.y -= self.velocity
            self.character_rect.rect.y -= self.velocity


    def change_image(self, not_move, move):
        # Pour chaque tour de boucle, move s'agrémente, a partir de 15 l'image change, et se remet normal au bout de 45 tour 
        self.move += 1
        if (self.move >= 0 and self.move <= 15) or self.move >= 45 : 
            self.image = pygame.image.load(not_move)
            var.last_move = not_move

        else : 
            self.image = pygame.image.load(move)
            var.last_move = move
        if self.move == 60 :
            self.move = 0 



    def interface_player(self, screen):
        food = pygame.image.load("assets/pics/interface_pics/food.png")
        stamina = pygame.image.load("assets/pics/interface_pics/stamina.png")
        hydratation = pygame.image.load("assets/pics/interface_pics/hydratation.png")
        support_map =pygame.image.load("assets/pics/interface_pics/support_map.png")
        
        # x, y, largeur, hauteur
        # Dessiner le rectangle noir derrière les barres de vie
        pygame.draw.rect(screen, (51, 51, 51), [0,  math.ceil(screen.get_height() - screen.get_height() / 6.54), 
        math.ceil(screen.get_width() / 1.38), math.ceil(screen.get_height() / 5.3)]) 
        screen.blit(food, (10, screen.get_height() - 105))
        screen.blit(stamina, (10, screen.get_height() - 67))
        screen.blit(hydratation, (10, screen.get_height() - 30))
        # blit le dessous de la map
        screen.blit(support_map, (995, 510))
        #Dessiner le sac de l'inventaire
        screen.blit(self.inventory.image, self.inventory.rect)
        # dessiner les trois barres de vies
        pygame.draw.rect(screen, (230,81,25), [food.get_height() + 20, screen.get_height() - 95, self.food * 8 ,8])
        pygame.draw.rect(screen, (239,184,41), [stamina.get_height() + 20, screen.get_height() - 57, self.stamina * 8 ,8])
        pygame.draw.rect(screen, (67,93,255), [hydratation.get_height() + 20, screen.get_height() - 20, self.hydratation * 8 ,8])
        # dessiner le carré pour afficher l'outil
        pygame.draw.rect(screen, (179, 179, 179), [0,  (math.ceil(screen.get_height() - (screen.get_height() / 6.54 + screen.get_width() / 10))), 
        math.ceil(screen.get_width() / 10), math.ceil(screen.get_height() / 6)])
        if self.inventory.last_obj != "" :
            if self.inventory.last_obj.name == "eau" and self.inventory.last_obj.quantity == 0 :
                self.inventory.last_obj.image = pygame.image.load(f"assets/pics/items_pics/eau_vide.png")
            elif self.inventory.last_obj.name == "eau" and self.inventory.last_obj.quantity == 100 :
                self.inventory.last_obj.image = pygame.image.load(f"assets/pics/items_pics/eau.png")
            self.inventory.last_obj.image = pygame.transform.scale(self.inventory.last_obj.image, (math.ceil(screen.get_width() / 10), math.ceil(screen.get_height() / 6)))
            screen.blit(self.inventory.last_obj.image, (0, (math.ceil(screen.get_height() - (screen.get_height() / 6.54 + screen.get_width() / 10)))))