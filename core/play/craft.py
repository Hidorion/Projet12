
import os
import sys
import pygame
#import psycopg2
#from registration.requeteSQL import create_registration
#from play.object import Object
#from play.map import Map
import variables as var


class Crafting():
    
    def __init__(self): #screen, player):
        # self.player = player
        self.screen = pygame.display.set_mode((var.x_screen, var.y_screen))
        self.crafting_interface = pygame.image.load("assets/backgrounds/crafting.png")
        self.crafting_interface = pygame.transform.scale(self.crafting_interface,( 960 , 576 ))
        self.crafting_interface_rect = self.crafting_interface.get_rect()
        self.crafting_interface_rect.x = self.screen.get_width() // 10
        self.crafting_interface_rect.y = self.screen.get_height() // 10
        self.button_next = pygame.image.load("assets/backgrounds/next.png")
        self.button_next_rect = self.button_next.get_rect()
        self.button_next_rect.x = 700
        self.button_next_rect.y = 175
        # self.list_object_craft = pygame.sprite.Group()
        # connection_infos = "dbname=Team12Corp user=AP2006 password=AP2006p2 port=15002 host=ale-pyt-2006-pjt-p2-db.pythonrover.wilders.dev"
        # self.connection = psycopg2.connect(connection_infos)
        # self.cursor = self.connection.cursor()

    def show_crafting(self,screen) :
        running = True
        while running is True :
            screen.blit(self.crafting_interface, (self.crafting_interface_rect.x, self.crafting_interface_rect.y))
            screen.blit(self.button_next, self.button_next_rect)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    Crafting.ExitGame()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        # Crafting.ExitGame()
                        running = False
                    return running
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # collisions on sign up text fields
                    if self.button_next_rect.collidepoint(event.pos):
                        Crafting.update()
            pygame.display.flip()
    
    def ExitGame():
        """
            Function that stops the game
        """
        pygame.quit()
        sys.exit()

    def update():
        # This variable simulate the result of the list of recipes's sql request
        resultrecipelist = [("Hache",),("Concococteur",),("Potion nutritive",)]
        resultingredientlist = [("Pierre","Bois","Liane"),("Coco","Bois","Eau"),("Champignon marron", "Fleur Violette", "Banane")]
        list_of_recipe = [n[0] for n in resultrecipelist]
        list_of_ingredient = [n for n in resultingredientlist]
        item = list_of_recipe[0]
        ing_one = list_of_ingredient[0][0]
        ing_two = list_of_ingredient[0][1]
        ing_three = list_of_ingredient[0][2]
        print(item , ing_one , ing_two , ing_three)
    
    # def read_inventory(self, pseudo): #Get, through the player inventory, to the ressources
    #     requete_sql = f"""
    #                 SELECT object.name, amount, action.name, category.name, inventaire.id_object
    #                 FROM inventaire
    #                 INNER JOIN player ON inventaire.id_player = player.id
    #                 INNER JOIN connection ON player.id_connection = connection.id
    #                 INNER JOIN object ON inventaire.id_object = object.id
    #                 INNER JOIN category ON object.id_category = category.id
    #                 INNER JOIN action ON object.id_action = action.id
    #                 WHERE (connection.pseudo = '{pseudo}' AND object.id_category = 7 )
    #                 ORDER BY inventaire.id_object, object.name """
    #     self.cursor.execute(requete_sql)
    #     return self.cursor.fetchall()
        
    # def get_object_name(self,list_of_recipe): #Get the object name via the recipe name
    #     requete_sql = f"""
    #                 SELECT object.name
    #                 FROM object
    #                 INNER JOIN recipe ON object.id = recipe.id_object
    #                 WHERE recipe_name = '{list_of_recipe}'
    #                 """
    #     self.cursor.execute(requete_sql)
    #     return self.cursor.fetchall()

    # def list_of_recipes(self): #Get the list of recipes
    #     sql_request = f"""SELECT recipe_name FROM recipe ORDER BY recipe.id"""
    #     self.cursor.execute(sql_request)
    #     return self.cursor.fetchall()

    # def read_ingredients (self,list_of_recipe): #Get the recipe's list of ingredients
    #     request = f"""
    #                 SELECT object.name
    #                 FROM recipe_object
    #                 INNER JOIN recipe ON recipe.id = recipe_object.id_recipe
    #                 INNER JOIN object ON object.id = recipe_object.id_object
    #                 WHERE recipe_name = '{list_of_recipe}'
    #                 """
    #     self.cursor.execute(request)
    #     return self.cursor.fetchall()

    # def get_ingredients (self,list_of_recipe,recipe): #Get the ingredients of a chosen recipe
    #     for recipe in range(len(list_of_recipe)):
    #         ingredient = list_of_recipe[recipe]
    #         list_of_ingredient = Crafting.read_ingredients(ingredient)
    #         return list_of_ingredient

    # def browse_interface (self):
    #     next = pygame.image.load("assets/backgrounds/next.png")
    #     previous = pygame.image.load("assets/backgrounds/previous.png")
    #     next_rect = next.get_rect()
    #     previous_rect = previous.get_rect()
    

GoClass = Crafting()
# # resultrecipelist = GoClass.list_of_recipes()
# This variable simulate the result of the list of recipes's sql request




GoClass.show_crafting(GoClass.screen)