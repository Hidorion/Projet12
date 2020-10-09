
from os import name
import pygame
import psycopg2
#from registration.requeteSQL import create_registration
#from play.object import Object
#from play.map import Map

class Crafting():
    
    def __init__(self, player): #screen, player):
        self.player = player
        self.crafting_interface = pygame.image.load("images/Bg/crafting.png")
        self.crafting_interface = pygame.transform.scale(self.crafting_interface,( 960 , 576 ))
        self.crafting_interface_rect = self.crafting_interface.get_rect()
        # self.crafting_interface_rect.x = screen.get_width() / 10
        # self.crafting_interface_rect.y = screen.get_height() / 10
        self.list_object_craft = pygame.sprite.Group()
        connection_infos = "dbname=Team12Corp user=AP2006 password=AP2006p2 port=15002 host=ale-pyt-2006-pjt-p2-db.pythonrover.wilders.dev"
        self.connection = psycopg2.connect(connection_infos)
        self.cursor = self.connection.cursor()

    # def show_crafting(self,screen):
    #     sql = requeteSQL.create_registration()
    #     player = self.player
    #     result = sql.read_crafting(player)
    #     for obj in result :
    #         self.list_object_craft.add(Object(obj, 0, 0))
    #     screen.blit(self.crafting_interface, (self.crafting_interface_rect.x, self.crafting_interface_rect.y))
    #     x = 150
    #     y = 112
    #     counter = 0
    #     for obj in self.list_object_craft:
    #         obj.rect.x = x
    #         obj.rect.y = y
    #         screen.blit(obj.image, obj.rect)
    #         x += 95
    #         counter += 1
    #         if counter == 10:
    #             y += 75
    #             x = 149.5
    #             counter = 0
    #     for obj in self.list_object_craft:
    #         screen.blit(obj.image, obj.rect)

    def read_inventory(self, pseudo):
        requete_sql = f"""SELECT object.name, amount, action.name, category.name, inventaire.id_object
                        FROM inventaire
                        INNER JOIN player ON inventaire.id_player = player.id
                        INNER JOIN connection ON player.id_connection = connection.id
                        INNER JOIN object ON inventaire.id_object = object.id
                        INNER JOIN category ON object.id_category = category.id
                        INNER JOIN action ON object.id_action = action.id
                        WHERE (connection.pseudo = '{pseudo}' AND object.id_category = 7 )
                        ORDER BY inventaire.id_object, object.name """
        self.cursor.execute(requete_sql)
        return self.cursor.fetchall()
        #return requete_sql

    def read_recipe(self):
        requete_sql = f"""SELECT object.name, recipe_object.object_name , recipe_object.amount
                        FROM recipe
                        INNER JOIN object ON recipe.id_object = object.id
                        INNER JOIN recipe_object ON recipe_object.id_recipe = recipe.id
                        ORDER BY object.name"""
        self.cursor.execute(requete_sql)
        return self.cursor.fetchall()
if __name__ == "__main__":    
    GoClass = Crafting(2)
    result = GoClass.read_inventory("douze")
    resultrecipe = GoClass.read_recipe()
    print(resultrecipe)

