
import os
import sys
import pygame
#import psycopg2
#from registration.requeteSQL import create_registration
#from play.object import Object
#from play.map import Map
import core.play.variables as var

pygame.init()
pygame.display.set_caption("New Horizon: Crafting")

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
        self.button_previous = pygame.image.load("assets/backgrounds/previous.png")
        self.button_previous_rect = self.button_previous.get_rect()
        self.button_previous_rect.x = 470
        self.button_previous_rect.y = 175
        self.button_craft = pygame.image.load("assets/pics/fabriquer.png")
        self.button_craft = pygame.transform.scale(self.button_craft,( 500 , 75 ))
        self.button_craft_rect = self.button_craft.get_rect()
        self.button_craft_rect.x = 355
        self.button_craft_rect.y = 515
        # This variable simulate the result of the list of recipes's sql request list_of_recipes(self)
        resultrecipelist = [("Hachette",),("Concococteur",),("Potion nutritive",)]
        # This variable simulate the result of the list of ingredients' sql request read_ingredients(self,list_of_recipe) and get_ingredients(self,list_of_recipe,recipe)
        resultingredientlist = [("Pierre","Bois","Liane"),("Coco","Bois","Eau"),("Concococteur", "Fleur Violette", "Banane")]
        self.list_of_recipe = [n[0] for n in resultrecipelist]
        self.list_of_ingredient = [n for n in resultingredientlist]
        # This variable simulate the sql request read_inventory(self, pseudo)
        resultinventory = [("Pierre","Bois","Liane","Pierre","Coco","Bois","Eau","Fleur Violette","Banane")] 
        self.inventory_list = [n for n in resultinventory[0]]
    

    def show_crafting(self,crafting) :

        """
            This method will "blit" the crafting interface
        """
        GoClass = Crafting()
        screen = GoClass.screen

        running = True

        counter = 0
        while crafting :
            screen.blit(GoClass.crafting_interface, (GoClass.crafting_interface_rect.x, GoClass.crafting_interface_rect.y))
            screen.blit(GoClass.button_next, GoClass.button_next_rect)
            screen.blit(GoClass.button_previous, GoClass.button_previous_rect)
            screen.blit(GoClass.button_craft, GoClass.button_craft_rect)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    Crafting.ExitGame(self)
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_k:
                        crafting = False


                        # Crafting.ExitGame(self)
                    
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # collisions on sign up text fields
                    
                    if GoClass.button_next_rect.collidepoint(event.pos):
                        counter = Crafting.counter_addition(counter)
                    if GoClass.button_previous_rect.collidepoint(event.pos):
                        counter = Crafting.counter_soustraction(counter)
                    if GoClass.button_craft_rect.collidepoint(event.pos):
                        Crafting.check_inventory(counter,GoClass.list_of_ingredient,GoClass.list_of_recipe,GoClass.inventory_list)
                        
            item, item_rect, ing_one, ing_one_rect, ing_two, ing_two_rect, ing_three, ing_three_rect = Crafting.print_object(screen,counter,GoClass.list_of_recipe,GoClass.list_of_ingredient)
            screen.blit(item, item_rect)
            screen.blit(ing_one, ing_one_rect)
            screen.blit(ing_two, ing_two_rect)
            screen.blit(ing_three, ing_three_rect)

            pygame.display.flip()

    def ExitGame(self):
        """
            Function that stops the game
        """
        pygame.quit()
        sys.exit()

    def print_object(screen, counter,list_of_recipe,list_of_ingredient):
        """
            This method will "blit" the recipe and their ingredients
        """
        item = pygame.image.load(f"assets/pics/items_pics/{list_of_recipe[counter]}.png")
        item = pygame.transform.scale(item,( 75 , 75 ))
        item_rect = item.get_rect()
        item_rect.x = 565
        item_rect.y = 150
        ing_one = pygame.image.load(f"assets/pics/items_pics/{list_of_ingredient[counter][0]}.png")
        ing_one = pygame.transform.scale(ing_one,( 75 , 75 ))
        ing_one_rect = ing_one.get_rect()
        ing_one_rect.x = 315
        ing_one_rect.y = 320
        ing_two = pygame.image.load(f"assets/pics/items_pics/{list_of_ingredient[counter][1]}.png")
        ing_two = pygame.transform.scale(ing_two,( 75 , 75 ))
        ing_two_rect = ing_two.get_rect()
        ing_two_rect.x = 565
        ing_two_rect.y = 320
        ing_three = pygame.image.load(f"assets/pics/items_pics/{list_of_ingredient[counter][2]}.png")
        ing_three = pygame.transform.scale(ing_three,( 75 , 75 ))
        ing_three_rect = ing_three.get_rect()
        ing_three_rect.x = 815
        ing_three_rect.y = 320
        return item, item_rect, ing_one, ing_one_rect, ing_two, ing_two_rect, ing_three, ing_three_rect

    def counter_addition(counter):
        """
            This method will allow the user to browse the recipe list
        """
        if counter < 2 :
            counter += 1
        else :
            counter = 0
        return counter
    
    def counter_soustraction(counter):
        """
            This method will allow the user to browse the recipe list
        """
        if counter > 0 :
            counter -= 1
        else :
            counter = 2
        return counter

    def check_inventory(counter,list_of_ingredient, list_of_recipe,inventory_list):
        """
            This method will check if the player can craft an object
        """
        
        if list_of_ingredient[counter][1] in inventory_list and list_of_ingredient[counter][0] in inventory_list and list_of_ingredient[counter][2] in inventory_list:
            print(f"Vous avez réussi à fabriquer 1x {list_of_recipe[counter]} ! ")
            inventory_list.append(list_of_recipe[counter])
        else :
            print("Vous regardez dans votre sac mais vous ne parvenez pas à rassembler tout les ingrédients nécessaires")
        
    


    """
        This is the SQL request in order to get a real 'resultrecipelist' and 'resultingredientlist' from the DB    
    """
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
    


# # resultrecipelist = GoClass.list_of_recipes()

# GoClass = Crafting()
# GoClass.show_crafting(GoClass.screen)
