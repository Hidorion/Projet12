# coding: utf-8

# Import Modules
import pygame
import math
import time

# Import class 
from core.play.map import Map
from core.play.player import Player
from core.avatar_selection.avatar_selection import Avatar
from core.play.camera import Camera
from core.registration.sql_queries import create_registration
from core.play.object import Object
from core.play import client
from core.play.craft import Crafting

# Import Variable
from core.play import variables as var


class Game:

    """
        class which groups together the other classes and starts the game
    """

    def __init__(self, screen) :

        self.pseudo = ""
        # Permet de définir la dernière direction du personnage
        self.last_movement = "up"

        # Instance
        self.sql = create_registration()
        self.champ_select = Avatar(screen)
        self.player = ""
        self.camera = Camera(6400, 6400)

        #Booleen

        self.pressed = {}
        self.not_pressed = {}
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
        # Permet d'ouvrir l'inventaire ou non
        self.inventory = False
        # Permet de blit ou non l'interface du player à chaque changement
        self.interface = True 
        # Permet de lance le chargement des map
        self.loading = True

    
        # Index de l'avatar choisit
        self.avatar_choose = 0
        # Compteur pour déplacer le player
        self.counter_move = 0

        # Créer les surfaces des map
        self.map_foret_sol = ""
        self.map_foret_behind = ""
        self.map_desert_sol = ""
        self.map_desert_behind = ""
        # Rect des map
        self.map_rect = ""

        # Groupe de sprite
        self.group_obstacle = pygame.sprite.Group() # Groupe d'obstacles (Tronc, pierre, arbre, eau)
        self.group_object = pygame.sprite.Group() # Groupe d'objet (fruit, bois, pierre)
        self.group_water = pygame.sprite.Group() # Groupe de zone d'eau pour remplir la gourde
        self.group_tree = pygame.sprite.Group() # Groupe d'arbre
        self.group_stone = pygame.sprite.Group() # Groupe de pierre
        self.fruit_tree = pygame.sprite.Group() # Groupe de fruit dans les arbres
        
        
        # Ok c'est moche, mais c'est la liste des rect.x des avatars
        self.list_image_avatar_x = [self.champ_select.avatar1_image_rect.x, self.champ_select.avatar2_image_rect.x, 
        self.champ_select.avatar3_image_rect.x, self.champ_select.avatar4_image_rect.x, self.champ_select.avatar5_image_rect.x, 
        self.champ_select.avatar6_image_rect.x, self.champ_select.avatar7_image_rect.x, self.champ_select.avatar8_image_rect.x]
        # Ok c'est moche, mais c'est la liste des rect.y des avatars
        self.list_image_avatar_y = [self.champ_select.avatar1_image_rect.y, self.champ_select.avatar2_image_rect.y, 
        self.champ_select.avatar3_image_rect.y, self.champ_select.avatar4_image_rect.y, self.champ_select.avatar5_image_rect.y, 
        self.champ_select.avatar6_image_rect.y, self.champ_select.avatar7_image_rect.y, self.champ_select.avatar8_image_rect.y]


    def update(self, screen):

        """
            Update the game and call the functions necessary for the game
        """
        # Fonction qui envoi au server les informations du player
        self.data_exchange([self.player.rect, var.last_move, self.pseudo])
        # Si le jeu est lancé
        if self.play :
            # Fonction qui déplace et gère les images du player
            self.movement(screen)
            # Fonction qui met à jour la caméra qui suit le player 
            self.camera.update(self.player.rect)
            # Fonction qui affiche qui map, le player, et les objets sur la map
            self.blit_map(screen, self.map_foret_sol, self.map_foret_behind, 6400, 0)
            self.blit_map(screen, self.map_desert_sol, self.map_desert_behind, 0, 0)
            for obj in self.group_tree :
                screen.blit(obj.image, (self.camera.apply_rect(obj.rect)))
            for obj in self.fruit_tree :
                image = pygame.transform.scale(obj.image,(18, 23))
                screen.blit(image, (self.camera.apply_rect(obj.rect)))
            # Fonction qui affiche l'interface du player, ses signes vitaux, sac a dos, mini map, objet selectionné
            self.player.interface_player(screen)
            # Fonction qui permet de rammasser les objets au sol et les mettre dans la liste d'inventaire
            self.player.inventory.pick_up_object(self)
            
        if self.inventory :
            # Fonction qui affiche l'interface du player
            self.player.interface_player(screen)
            # Fonction qui affiche le background de l'inventaire et les objet de l'inventaire du player
            self.player.inventory.print_inventory(screen)
        # Fonction qui gère les commandes clavier
        self.commandes(screen)

        # Si le champ select est open
        if self.validation_champ_select :
            # Afficher le background du champ select
            screen.blit(self.champ_select.background_champ_select, (0,0))
            # Si aucun avatar est selectionné et que l'utilisateur valide
            if self.not_select == True and self.selected_champ == False:
                # Affiche un message d'erreur
                self.message_champ_select(screen, "Selectionnez un avatar pour valider")
            if self.selected_champ :
                # Si l'utilisateur clic sur un avatar, un ecran vert s'afficher derrière l'avatar
                pygame.draw.rect(screen,(0,225,0),(self.list_image_avatar_x[self.avatar_choose], self.list_image_avatar_y[self.avatar_choose], self.champ_select.avatar1_image.get_width(), self.champ_select.avatar1_image.get_height()))
            # Fonction qui affiche tout les avatars
            self.champ_select.update(screen)
          


    def blit_map (self, screen, map, behind, x, y ) :

        """
            fatorization of map blits
        """
        # Definir le rect de la map
        self.map_rect.x = x
        self.map_rect.y = y
        screen.blit(map, (self.camera.apply_rect(self.map_rect)))
        # Pour chaque objet (fruit, bois pierre) dans la liste
        for obj in self.group_object:
            image = pygame.transform.scale(obj.image,(18, 23))
            screen.blit(image, (self.camera.apply_rect(obj.rect)))
        # pour chaque objet (pierre)
        for obj in self.group_stone:
            screen.blit(obj.image, (self.camera.apply_rect(obj.rect)))
        # Si le serveur est ouvert
        if var.server_open :
            # Afficher chaque player connecté au serveur
            for player in var.list_players :
                image = pygame.image.load(player[1][1])
                image = pygame.transform.scale(image, (32 , 32))
                screen.blit(image, (self.camera.apply_rect(player[1][0])))
        else :
            screen.blit(self.player.image, self.camera.apply(self.player.rect))
        screen.blit(behind, self.camera.apply_rect(self.map_rect))
        
        
    def create_map(self, file):

        """
            Create map with map.tmx
        """
        # Pour chaque map tiled, instancie le class MAP
        map = Map(file, self.player)
        # Fonction qui recupère les tuiles de la map tiled pour créer une surface
        map_img = map.make_map()
        self.map_rect = map_img.get_rect()
        return map_img



    def movement(self, screen) :

        """
            Call function function that need the keyboard
        """

        # si telle touche est pressée, j'appelle la fonction pour déplacer la carte
        if self.pressed.get(pygame.K_RIGHT) or self.pressed.get(pygame.K_d):
            self.player.move_right(screen)
            self.last_movement = "right"
            

        elif self.pressed.get(pygame.K_LEFT) or self.pressed.get(pygame.K_a):    
            self.player.move_left(screen)
            self.last_movement = "left"
            

        elif self.pressed.get(pygame.K_UP) or self.pressed.get(pygame.K_w):  
            self.player.move_up(screen)
            self.last_movement = "up"
            

        elif self.pressed.get(pygame.K_DOWN) or self.pressed.get(pygame.K_s):  
            self.player.move_down(screen)
            self.last_movement = "down"

        
        # for each direction, restart image player 
        list_key = [[pygame.K_RIGHT, "right"], [pygame.K_LEFT, "left"], [pygame.K_UP, "up"], [pygame.K_DOWN, "down"]]
        for key in list_key :
            # fonction qui met à jour l'image du player
            self.update_image(key[0], key[1])

    def commandes(self,screen):

        # if crafting is open, press k to close crafting
        if self.pressed.get(pygame.K_k) :
            crafting = True
            self.pressed[pygame.K_k] = Crafting.show_crafting(self,crafting)

        # if inventory is open, press i for close inventory
        if self.not_pressed.get(pygame.K_i) and self.inventory == False and self.play == True :
            self.inventory = True
            self.play = False
            self.not_pressed[pygame.K_i] = False
        # if inventory is close, press i for open inventory
        elif self.not_pressed.get(pygame.K_i) and self.inventory == True and self.play == False :
            self.inventory = False
            self.play = True
            self.not_pressed[pygame.K_i] = False

        # Si l'utilisateur appui sur U et qu'il a un objet selectionné
        if self.not_pressed.get(pygame.K_u) and self.player.inventory.last_obj != "":
            # Si le dernier objet selectionné est une hache
            if self.player.inventory.last_obj.name == "hachette" :
                # Pour chaque arbre dans le group d'arbre
                for obj in self.group_tree :
                    # Si le rect du player est sur le rect de l'arbre
                    if self.player.character_rect.rect.colliderect(obj.rect) :
                        # Fonction qui intéragis avec l'arbre suivant son nombre de pv
                        self.player.inventory.interaction_tree(obj)
                        self.not_pressed[pygame.K_u] = False
                self.not_pressed[pygame.K_u] = False

            # Si le dernier objet selectionné est une pioche
            elif self.player.inventory.last_obj.name == "pioche" :
                # Pour chaque pierre dans le groupe de pierre
                for obj in self.group_stone :
                    # Si le rect du player est sur le rect du rocher
                    if self.player.character_rect.rect.colliderect(obj.rect) :
                        # Fonction qui intéragis avec le rocher suivant son nombre de pv
                        self.player.inventory.interaction_stone(obj)
                        self.not_pressed[pygame.K_u] = False
                self.not_pressed[pygame.K_u] = False

            # Si le dernier objet selectionné est une gourde
            elif self.player.inventory.last_obj.name == "eau":
                # Si le rect du player est a coté de l'eau
                if pygame.sprite.spritecollideany(self.player.character_rect, self.group_water):
                    # Pour chaque objet dans l'inventaire
                    for obj in self.player.inventory.list_object_inventory :
                        # Si l'objet a pour nom "eau" ca quantité passe a 100
                        obj.quantity = 100 if obj.name == "eau" else 1
                        self.not_pressed[pygame.K_u] = False
                    self.not_pressed[pygame.K_u] = False
                    pygame.transform.scale(pygame.image.load(f"assets/pics/items_pics/eau.png"), (50, 42))
                else : 
                    # Si le player n'est pas a coté de l'eau, mettre a jour les signes vitaux du player avec la gourde
                    self.player.inventory.update_vital_sign(self.player.inventory.last_obj)
                    # Pour chaque objet de l'inventaire
                    for obj in self.player.inventory.list_object_inventory :
                        # La quantité de l'eau est à zéro si l'objet a le nom "eau"
                        obj.quantity = 0 if obj.name == "eau" else 1
                        self.player.inventory.last_obj.image = pygame.transform.scale(pygame.image.load(f"assets/pics/items_pics/eau_vide.png"), (50, 42))
                        self.not_pressed[pygame.K_u] = False
                    self.not_pressed[pygame.K_u] = False

        # Si aucun outil est selectionné
        elif self.pressed.get(pygame.K_u) and self.player.inventory.last_obj == "" :
            # fonction qui print un message
            self.message_champ_select(screen, "Vous n'avez pas d'outil selectionné")


        
    def update_image(self, key, direction) :

        """
            factorization restart image if sprite don't move 
        """
        # Si le player a une tel direction et qu'il est arrêté
        if self.pressed.get(key) == False and self.last_movement == direction :
            # L'image se met en position arrêt
            self.player.image = pygame.image.load(f"assets/avatars/{self.player.avatar}/character_{direction}.png")
            var.last_move = f"assets/avatars/{self.player.avatar}/character_{direction}.png"
            self.player.image = pygame.transform.scale(self.player.image, (32, 32))

    def message_champ_select(self, screen, message):

        """
            print message in interface pygame
        """

        font = pygame.font.SysFont("Gabriola", math.ceil(screen.get_width() / 40 + screen.get_height() / 40))
        text = font.render(message, 1, (255,255,255))
        text_rect = text.get_rect()
        text_rect.x = math.ceil(screen.get_width() /2 - len(message) * 7)
        text_rect.y = math.ceil(screen.get_height()/2 )
        screen.blit(text,text_rect)

    def instance_player (self, screen):
        """
            instance player 
        """
        # Je récupère l'id de connection du player
        id_connection = self.sql.id_connection(self.pseudo)
        # Je regarde si le player un champ dans la table player
        result = self.sql.read_table_player(self.pseudo)
        # Si il a pas de champ dans la table player j'en créé un
        create = False 
        if result == [] :
            self.sql.create_player([id_connection[0], f'avatar{self.avatar_choose +1}', 13000, 9000, 100, 100, 100])
            result = self.sql.read_table_player(self.pseudo)
            create = True
        # Je récupère les infromation de la class player
        id_player = self.sql.id_player(id_connection[0])
        # J'intancie la class player avec les informations récupérées de la BDD
        if create : 
            self.player = Player(screen, self, result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], id_player[0])
            self.player.rect.x = 1500
            self.player.rect.y = 2000
        else:
            self.player = Player(screen, self, result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], id_player[0])
    def update_player(self):
        """
            Save player information
        """
        # Je récupère l'id de connection du player
        id_connection = self.sql.id_connection(self.pseudo)
        # Je met à jour ses infromation dans la base de donnée
        self.sql.update_table_player(self.player.rect.x, self.player.rect.y, self.player.stamina, 
        self.player.food, self.player.hydratation, id_connection[0])
        # Pour mettre a jour son inventaire je supprime ce qui appartient a l'id player de la table inventaire
        self.sql.delete_table_inventory(self.player.id_player)
        # Pour chaque objet dans l'inventaire, je l'ajouet à la BDD
        for obj in self.player.inventory.list_object_inventory :
            self.sql.add_inventory(self.player.id_player, obj.id_object, obj.quantity)

    def data_exchange(self, data):
        # Si le serveur est ouvert
        if var.server_open :
            # Fonction qui envoi et récupère les informations du serveur
            client.execute_client(data)

        