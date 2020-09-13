# coding: utf-8

#import
import pygame
import math
import time
from play.map import Map
from play.player import Player
from champ_select.champ_select import Avatar


class Game:

    def __init__(self, screen) :
        
        # self.player = Player(screen)
        self.champ_select = Avatar(screen)
        # Permet de définir la dernière direction du personnage
        self.last_movement = "up"
        #Calcul le nombre de tour pour changer l'image du personnage
        self.move = 0
        self.pressed = {}
        # Si le champ_select est affiché
        self.validation_champ_select = False
        # Si un avatar est selectionné
        self.selected_champ = False
        # Index de l'avatar choisit
        self.avatar_choose = 0
        # Permet de print la map et le personnage
        self.play = True
        # Si la touche valider est pressé mais aucun avatar choisit
        self.not_select = False
        # Met la mini map en full screen
        self.full_screen_map = False
        self.player = Player(screen, 1, self)

        # Créer les deux surface
        self.map_sol = ""
        self.map_behind = ""
        
        self.counter_move = 0

        self.list_image_avatar_x = [self.champ_select.avatar1_image_rect.x, self.champ_select.avatar2_image_rect.x, 
        self.champ_select.avatar3_image_rect.x, self.champ_select.avatar4_image_rect.x, self.champ_select.avatar5_image_rect.x, 
        self.champ_select.avatar6_image_rect.x, self.champ_select.avatar7_image_rect.x, self.champ_select.avatar8_image_rect.x]

        self.list_image_avatar_y = [self.champ_select.avatar1_image_rect.y, self.champ_select.avatar2_image_rect.y, 
        self.champ_select.avatar3_image_rect.y, self.champ_select.avatar4_image_rect.y, self.champ_select.avatar5_image_rect.y, 
        self.champ_select.avatar6_image_rect.y, self.champ_select.avatar7_image_rect.y, self.champ_select.avatar8_image_rect.y]

        # self.list_avatar = ["avatar1", "avatar2", "avatar3", "avatar4", "avatar5", "avatar6", "avatar7", "avatar8"]

    def update(self, screen):

        # self.player.avatar = self.list_avatar[self.avatar_choose]
        if self.play and self.full_screen_map == False:
            self.counter_move += 1
            if self.counter_move % 2 == 0:
                self.movement(screen)
            screen.blit(self.map_sol, (self.player.map_x, self.player.map_y))
            screen.blit(self.player.image, (400, 400)) 
            screen.blit(self.map_behind, (self.player.map_x, self.player.map_y))
            # screen.blit(self.map.mini_map, self.map.mini_map_rect)

        # if self.full_screen_map :
        #     screen.blit(self.map.mini_map_full, self.map.mini_map_full_rect)
        #     # pygame.draw.rect(screen,(225, 0,0),(self.map.tm_rect.x, self.map.tm_rect.y, 10, 10))   

        # if self.validation_champ_select :
        #     screen.blit(self.champ_select.background_champ_select, (0,0))
        #     if self.not_select == True and self.selected_champ == False:
        #         self.message_champ_select(screen)
        #     if self.selected_champ :
        #         pygame.draw.rect(screen,(0,225,0),(self.list_image_avatar_x[self.avatar_choose], self.list_image_avatar_y[self.avatar_choose], self.champ_select.avatar1_image.get_width(), self.champ_select.avatar1_image.get_height()))
        #     self.champ_select.update(screen)

    def create_map(self, file, cant_walk):

        map = Map(file)
        map_img = map.make_map(cant_walk)
        map_rect = map_img.get_rect()
        return map_img



    def movement(self, screen) :
        # si telle touche est pressée, j'appelle la fonction pour déplacer la carte
        if self.pressed.get(pygame.K_RIGHT):# and self.map.tm_rect.x + self.player.velocity < self.map.tm.get_width():
            self.player.move_right(screen)
            self.last_movement = "right"

        elif self.pressed.get(pygame.K_LEFT) :# and self.map.tm_rect.x > - 3200 :
            self.player.move_left(screen)
            self.last_movement = "left"

        elif self.pressed.get(pygame.K_UP) : #and self.map.tm_rect.y > - 3200 :
            self.player.move_up(screen)
            self.last_movement = "up"

        elif self.pressed.get(pygame.K_DOWN): # and self.map.tm_rect.y + self.player.velocity < self.map.tm.get_height():
            self.player.move_down(screen)
            self.last_movement = "down"


        # Met dans la position arrêt le personnage
        if self.pressed.get(pygame.K_RIGHT) == False and self.last_movement == "right" :
            self.player.image = pygame.image.load(f"images/ressources/{self.player.avatar}/character_right.png")
            self.player.image = pygame.transform.scale(self.player.image, (math.ceil(screen.get_height() / 25), math.ceil(screen.get_width() / 20)))

        elif self.pressed.get(pygame.K_LEFT) == False and self.last_movement == "left" :
            self.player.image = pygame.image.load(f"images/ressources/{self.player.avatar}/character_left.png")
            self.player.image = pygame.transform.scale(self.player.image, (math.ceil(screen.get_height() / 25), math.ceil(screen.get_width() / 20)))

        elif self.pressed.get(pygame.K_UP) == False and self.last_movement == "up" :
            self.player.image = pygame.image.load(f"images/ressources/{self.player.avatar}/character_up.png")
            self.player.image = pygame.transform.scale(self.player.image, (math.ceil(screen.get_height() / 25), math.ceil(screen.get_width() / 20)))

        elif self.pressed.get(pygame.K_DOWN) == False and self.last_movement == "down" :
            self.player.image = pygame.image.load(f"images/ressources/{self.player.avatar}/character_down.png")
            self.player.image = pygame.transform.scale(self.player.image, (math.ceil(screen.get_height() / 25), math.ceil(screen.get_width() / 20)))


    # # Déplace la carte en fonction des touche pressé
    # def move_right(self, screen):
    #     self.player.rect.x += self.player.velocity
    #     self.change_image(f"images/ressources/{self.player.avatar}/character_right.png", f"images/ressources/{self.player.avatar}/character_right_move.png" )
    #     self.player.image = pygame.transform.scale(self.player.image, (math.ceil(screen.get_height() / 25), math.ceil(screen.get_width() / 20)))

    # def move_left(self, screen):
    #     self.player.rect.x -= self.player.velocity
    #     self.change_image(f"images/ressources/{self.player.avatar}/character_left.png", f"images/ressources/{self.player.avatar}/character_left_move.png" )
    #     self.player.image = pygame.transform.scale(self.player.image, (math.ceil(screen.get_height() / 25), math.ceil(screen.get_width() / 20)))

    # def move_up(self, screen):
    #     self.player.rect.y -= self.player.velocity
    #     self.change_image(f"images/ressources/{self.player.avatar}/character_up.png", f"images/ressources/{self.player.avatar}/character_up_move.png" )
    #     self.player.image = pygame.transform.scale(self.player.image, (math.ceil(screen.get_height() / 25), math.ceil(screen.get_width() / 20)))

    # def move_down(self, screen):
    #     self.player.rect.y += self.player.velocity
    #     self.change_image(f"images/ressources/{self.player.avatar}/character_down.png", f"images/ressources/{self.player.avatar}/character_down_move.png" )
    #     self.player.image = pygame.transform.scale(self.player.image, (math.ceil(screen.get_height() / 25), math.ceil(screen.get_width() / 20)))

    
    # def change_image(self, not_move, move):
    #     # Pour chaque tour de boucle, move s'agrémente, a partir de 15 l'image change, et se remet normal au bout de 45 tour 
    #     self.move += 1
    #     if (self.move >= 0 and self.move <= 15) or self.move >= 45 : 
    #         self.player.image = pygame.image.load(not_move)
    #     else : 
    #         self.player.image = pygame.image.load(move)
    #     if self.move == 60 :
    #         self.move = 0 

    def message_champ_select(self, screen):
        font = pygame.font.SysFont("Gabriola", math.ceil(screen.get_width() / 40 + screen.get_height() / 40))
        text = font.render("Selectionnez un avatar pour valider", 1, (255,255,255))
        text_rect = text.get_rect()
        text_rect.x = math.ceil(screen.get_width() /2 - math.ceil(screen.get_width() / 3.5))
        text_rect.y = math.ceil(screen.get_height()/2 - (math.ceil((screen.get_width() / 40 + screen.get_height() / 40) / 2)))
        screen.blit(text,text_rect)

        
        