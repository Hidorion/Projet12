# coding: utf-8

#import
import pygame
import math
import time
from play.map import Map
from play.player import Player
from champ_select.champ_select import Avatar
from play.camera import Camera
from play import Variables as var
from registration.requeteSQL import create_registration


class Game:

    def __init__(self, screen) :

        self.pseudo = ""
        # Permet de définir la dernière direction du personnage
        self.last_movement = "up"
        #Calcul le nombre de tour pour changer l'image du personnage
        self.move = 0

        # Instance
        self.sql = create_registration()
        self.champ_select = Avatar(screen)
        self.player = ""
        self.camera = Camera(6400, 6400)

        #Booleen

        self.pressed = {}
        # Si le champ_select est affiché
        self.validation_champ_select = False
        # Si un avatar est selectionné
        self.selected_champ = False
        # Permet de print la map et le personnage
        self.play = False
        # Si la touche valider est pressé mais aucun avatar choisit
        self.not_select = False
        # Met la mini map en full screen
        self.full_screen_map = False


        # Permet de blit ou non l'interface du player à chaque changement
        self.interface = True 

    
        # Index de l'avatar choisit
        self.avatar_choose = 0

        # Créer les surfaces des map
        self.map_foret_sol = ""
        self.map_foret_behind = ""

        self.map_montagne_sol = ""
        self.map_montagne_behind = ""

        self.map_marecage_sol = ""
        self.map_marecage_behind = ""

        self.map_cratere_sol = ""
        self.map_cratere_behind = ""

        self.map_desert_sol = ""
        self.map_desert_behind = ""

        self.group_obstacle = pygame.sprite.Group()
        
        self.counter_move = 0

        self.list_image_avatar_x = [self.champ_select.avatar1_image_rect.x, self.champ_select.avatar2_image_rect.x, 
        self.champ_select.avatar3_image_rect.x, self.champ_select.avatar4_image_rect.x, self.champ_select.avatar5_image_rect.x, 
        self.champ_select.avatar6_image_rect.x, self.champ_select.avatar7_image_rect.x, self.champ_select.avatar8_image_rect.x]

        self.list_image_avatar_y = [self.champ_select.avatar1_image_rect.y, self.champ_select.avatar2_image_rect.y, 
        self.champ_select.avatar3_image_rect.y, self.champ_select.avatar4_image_rect.y, self.champ_select.avatar5_image_rect.y, 
        self.champ_select.avatar6_image_rect.y, self.champ_select.avatar7_image_rect.y, self.champ_select.avatar8_image_rect.y]

        self.map_rect = ""
        # self.list_avatar = ["avatar1", "avatar2", "avatar3", "avatar4", "avatar5", "avatar6", "avatar7", "avatar8"]

    def update(self, screen):

        if self.play and self.full_screen_map == False:
        
            self.movement(screen)
            self.camera.update(self.player.rect)
            self.blit_map(screen, self.map_foret_sol, self.map_foret_behind, 12800, 6400)
            self.blit_map(screen, self.map_marecage_sol, self.map_marecage_behind, 6400, 12800)
            self.blit_map(screen, self.map_cratere_sol, self.map_cratere_behind, 6400, 6400)
            self.blit_map(screen, self.map_montagne_sol, self.map_montagne_behind, 6400, 0)
            self.blit_map(screen, self.map_desert_sol, self.map_desert_behind, 0, 6400)
            self.player.interface_player(screen)

        if self.validation_champ_select :
            screen.blit(self.champ_select.background_champ_select, (0,0))
            if self.not_select == True and self.selected_champ == False:
                self.message_champ_select(screen, "Selectionnez un avatar pour valider")
            if self.selected_champ :
                pygame.draw.rect(screen,(0,225,0),(self.list_image_avatar_x[self.avatar_choose], self.list_image_avatar_y[self.avatar_choose], self.champ_select.avatar1_image.get_width(), self.champ_select.avatar1_image.get_height()))
            self.champ_select.update(screen)



    def blit_map (self, screen, map, behind, x, y, ) :
        self.map_rect.x = x
        self.map_rect.y = y
        screen.blit(map, (self.camera.apply_rect(self.map_rect))) #(self.player.map_x, self.player.map_y),
        screen.blit(self.player.image, self.camera.apply(self.player.rect))
        screen.blit(behind, self.camera.apply_rect(self.map_rect))
        
        
    def create_map(self, file):

        map = Map(file, self.player)
        map_img = map.make_map()
        self.map_rect = map_img.get_rect()
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
            self.player.image = pygame.transform.scale(self.player.image, (32, 32))

        elif self.pressed.get(pygame.K_LEFT) == False and self.last_movement == "left" :
            self.player.image = pygame.image.load(f"images/ressources/{self.player.avatar}/character_left.png")
            self.player.image = pygame.transform.scale(self.player.image, (32, 32))

        elif self.pressed.get(pygame.K_UP) == False and self.last_movement == "up" :
            self.player.image = pygame.image.load(f"images/ressources/{self.player.avatar}/character_up.png")
            self.player.image = pygame.transform.scale(self.player.image, (32, 32))

        elif self.pressed.get(pygame.K_DOWN) == False and self.last_movement == "down" :
            self.player.image = pygame.image.load(f"images/ressources/{self.player.avatar}/character_down.png")
            self.player.image = pygame.transform.scale(self.player.image, (32, 32))

    def message_champ_select(self, screen, message):
        font = pygame.font.SysFont("Gabriola", math.ceil(screen.get_width() / 40 + screen.get_height() / 40))
        text = font.render(message, 1, (255,255,255))
        text_rect = text.get_rect()
        text_rect.x = math.ceil(screen.get_width() /2 - len(message) * 7)
        text_rect.y = math.ceil(screen.get_height()/2 )
        screen.blit(text,text_rect)

    def instance_player (self, screen):
        id_connection = self.sql.id_connection(self.pseudo)
        result = self.sql.read_table_player(self.pseudo)
        if result == [] :
            self.sql.create_player([id_connection[0], f'avatar{self.avatar_choose +1}', 9000, 9000, 100, 100, 100])
        result = self.sql.read_table_player(self.pseudo)
        print(result)
        self.player = Player(screen, self, result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5])
        self.player.group_obstacle = self.group_obstacle

    def update_player(self):
        id_connection = self.sql.id_connection(self.pseudo)
        self.sql.update_table_player(self.player.rect.x, self.player.rect.y, self.player.stamina, 
        self.player.food, self.player.hydratation, id_connection[0])
        