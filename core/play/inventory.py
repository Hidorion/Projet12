#coding:utf-8
import pygame
import math
import random

from core.registration.player_registration import create_registration
from core.play.object import Object
from core.play.map import Map

class Inventory():

    def __init__(self, screen, player):
        self.player = player
        self.image = pygame.image.load("assets/pics/interface_pics/bag.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1060
        self.rect.y = 390
        
        # load le boutton pour trier l'inventaire
        self.button_tri_inventory = pygame.image.load("assets/pics/buttons_pics/button_tri_inventory.png")
        self.button_tri_inventory_rect = self.button_tri_inventory.get_rect()
        self.button_tri_inventory_rect.x = 990
        self.button_tri_inventory_rect.y = 555

        # Background de l'inventaire
        self.interface_inventory = pygame.image.load("assets/pics/backgrounds_pics/inventory.png")
        self.interface_inventory = pygame.transform.scale(self.interface_inventory,( 960 , 576 ))
        self.interface_inventory_rect = self.interface_inventory.get_rect()
        self.interface_inventory_rect.x = screen.get_width() / 10
        self.interface_inventory_rect.y = screen.get_height() / 10

        # Objet dans l'inventaire
        self.list_object_inventory = pygame.sprite.Group()
        
        # dernier objet utilisé
        self.last_obj = ""

    def print_inventory(self, screen) :
        """
            Affiche le background et les objets dans l'inventaire
        """
        screen.blit(self.interface_inventory, (self.interface_inventory_rect.x, self.interface_inventory_rect.y))
        x = 150
        y = 112
        counter = 0
        # Pour chaque objet dans l'inventaire 
        for obj in self.list_object_inventory:
            # Si l'objet a le nom "eau", modification de l'image
            if obj.name == "eau" and obj.quantity == 100:
                obj.image = pygame.transform.scale(pygame.image.load(f"assets/pics/items_pics/eau.png"), (50, 42))
            elif obj.name == "eau" and obj.quantity == 0: 
                obj.image = pygame.transform.scale(pygame.image.load(f"assets/pics/items_pics/eau_vide.png"), (50, 42))
            else : 
                obj.image = pygame.transform.scale(pygame.image.load(f"assets/pics/items_pics/{obj.name}.png"), (50, 42))
            obj.rect.x = x
            obj.rect.y = y
            screen.blit(obj.image, obj.rect)
            x += 95
            counter += 1
            # Dès que 10 objets sont affichés, j'augmente le Y pour passer à la ligne du dessous, et je remet le X au debut
            if counter == 10:
                y += 75
                x = 149.5
                counter = 0

        # Pour chaque objet dans l'inventaire
        for obj in self.list_object_inventory:
            screen.blit(obj.image, obj.rect)
        screen.blit(self.button_tri_inventory, self.button_tri_inventory_rect)
        

    def add_list_object(self, pseudo):
        """
            Récupère l'inventaire du Player dans la BDD et l'ajoute à l'inventaire du player
        """

        # Instancie les requete SQL 
        sql = create_registration()
        # Fonction qui renvoi de contenu de l'inventaire du player
        result = sql.read_inventory(pseudo)
        # Pour chaque objet dans l'inventaire de la BDD
        for obj in result :
            # Ajouter à l'inventaire du player
            self.list_object_inventory.add(Object(obj, 0, 0))

    def update_vital_sign(self, obj) :
        """ 
            improves the player's vital signs
        """ 
        self.player.stamina += obj.stamina
        self.player.stamina = 100 if self.player.stamina > 100 else self.player.stamina
        self.player.food += obj.food
        self.player.food = 100 if self.player.food > 100 else self.player.food
        self.player.hydratation += obj.hydratation
        self.player.hydratation = 100 if self.player.hydratation > 100 else self.player.hydratation

    def pick_up_object(self, game):
        """
            Collision avec les fruit, les delete et les add a l'inventaire
        """
        if len(self.list_object_inventory) < 69 :
            for obj in self.player.game.group_object :
                if self.player.character_rect.rect.colliderect(obj.rect) and self.player.game.pressed.get(pygame.K_q):
                    self.list_object_inventory.add(obj)
                    self.player.game.group_object.remove(obj)

    def delete_inventory(self, obj):
        """
            Supprime les objets de l'inventaire pour les ajouter aux objets sur la map
        """
        self.player.game.group_object.add(obj)
        obj.rect.x = self.player.character_rect.rect.x + random.randint(-30, 30)
        obj.rect.y = self.player.character_rect.rect.y + random.randint(-30, 30)
        self.list_object_inventory.remove(obj)

    def sort_inventory(self, pseudo):
        """
            Tri l'inventaire
        """
        sql = create_registration()
        # Fonction qui supprime tout l'inventaire du player dans la BDD
        sql.delete_table_inventory(self.player.id_player)
        # Pour chaque objet dans l'inventaire, je l'ajouet à la BDD
        for obj in self.list_object_inventory :
            #Fonction qui ajoute des objets à la BDD
            sql.add_inventory(self.player.id_player, obj.id_object, obj.quantity)
        # Vider l'inventaire du player
        self.list_object_inventory = pygame.sprite.Group()
        # Fonction qui récupère l'inventaire dans la BDD
        result = sql.read_inventory(pseudo)
        for obj in result :
            # Add dans l'inventaire du player
            self.list_object_inventory.add(Object(obj, 0, 0))

    def delete_add_wood(self, obj):
        """
            Detruit un arbre et ajoute le bois a l'inventaire
        """
        # Fonction qui met à jour les signes vitaux les signes vitaux suivant l'objet
        self.update_vital_sign(self.last_obj)
        # Instancier les requête SQl
        sql = create_registration()
        # Recupère les caractéristiques de l'objet
        result = sql.read_information_object(obj.object)
        # Si l'inventaire n'est pas full, ajoute l'objet à l'inventaire
        for loop in range(obj.quantity):
            if len(self.list_object_inventory) < 69 :
                self.list_object_inventory.add(Object(result[0], 0, 0))
        # Supprime l'objet de la map
        self.player.game.group_tree.remove(obj)

    def move_tree(self, obj):
        """
            Transforme l'arbre et déplace les fruits
        """
        #Enlève 1 pv à l'objet arbre
        obj.pv -= 1
        # Si le player est à gauche de l'arbre, l'arbre tomber a droite
        if self.player.character_rect.rect.x  > obj.rect.x + obj.image.get_width() / 2:
            obj.image = pygame.transform.rotate(obj.image, 15)
            obj.rect.x -= 23
            obj.rect.y -= 7
            # Déplace les fruit qui sont dans le rect de l'arbre
            for fruit in self.player.game.fruit_tree :
                if fruit.rect.colliderect(obj.rect) :
                    fruit.rect.x += -12
                    fruit.rect.y += 3

        else :
            # Si le player est à droite de l'arbre, l'arbre tomber à gauche
            obj.image = pygame.transform.rotate(obj.image, - 15)
            obj.rect.x += -3
            obj.rect.y += -5
            # Déplace les fruit qui sont dans le rect de l'arbre
            for fruit in self.player.game.fruit_tree :
                if fruit.rect.colliderect(obj.rect) :
                    fruit.rect.x += 10
                    fruit.rect.y += 5

    def drop_fruit(self, obj) :
        """
            Fait tomber les fruit au sol
        """
        # Enlève 1 pv à l'objet arbre
        obj.pv -= 1
        for fruit in self.player.game.fruit_tree :
            # Pour chaque fruit dans le rect de l'arbre
            if fruit.rect.colliderect(obj.rect) :
                # Supprimer l'objet de l'arbre et l'ajoute à la liste des objets aux sol
                fruit.rect.y = obj.rect.y + obj.image.get_height() / 1.3
                self.player.game.group_object.add(fruit)
                self.player.game.fruit_tree.remove(fruit)
    
    def interaction_tree(self, obj):
        """
            Définit quelle interaction choisir en fonction des pv de l'arbre
        """
        if obj.pv == 3:
            self.move_tree(obj)
        elif obj.pv == 2 :
            self.drop_fruit(obj)
        else : 
            self.delete_add_wood(obj)

    def first_break_stone(self, obj):
        """
            Change l'image de la pierre
        """
        #Enlève 1 pv à l'objet pierre
        obj.pv -= 1
        obj.image = pygame.image.load(f"assets/pics/environment_pics/{obj.name}2.png")
        # Instancie les requêtes SQL
        sql = create_registration()
        # récupère les informations de l'objet
        result = sql.read_information_object(obj.object)
        for loop in range(2):
            if len(self.list_object_inventory) < 69 :
                # Ajoute l'objet à l'inventaire si l'inventaire n'est pas full
                self.list_object_inventory.add(Object(result[0], 0, 0))
        # Fonction qui met à jour les signes vitaux les signes vitaux suivant l'objet
        self.update_vital_sign(self.last_obj)

    def seconde_break_stone(self, obj) :
        """
            Delete l'objet pierre
        """
        # Fonction qui met à jour les signes vitaux les signes vitaux suivant l'objet
        self.update_vital_sign(self.last_obj)
        # Instancie les requêtes SQL
        sql = create_registration()
        # Renvoi les caractéristiques de l'objet
        result = sql.read_information_object(obj.object)
        if len(self.list_object_inventory) < 69 :
            # Ajoute l'objet a l'inventaire si il est pas full
            self.list_object_inventory.add(Object(result[0], 0, 0))
        # Supprime l'objet pierre du groupe_stone
        self.player.game.group_stone.remove(obj)

    def interaction_stone(self, obj):
        """
            Défini la fonction à lancer en fonction des pv de l'objet
        """
        if obj.pv == 3 :
            self.first_break_stone(obj)
        elif obj.pv == 2 :
            self.seconde_break_stone(obj)

        
