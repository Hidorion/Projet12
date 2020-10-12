# coding: utf-8

#import
import psycopg2
import random

###########################
##### connection infos #####
###########################
# connection_infos = "dbname=Projet12 user=postgres password=group12"

connection_infos = "dbname=Projet12 user=postgres password=douzetrentedeux"

class create_registration():

    def __init__(self):
        self.connection = psycopg2.connect(connection_infos)
        self.cursor = self.connection.cursor()
        self.name = []
        self.email = []

    def create_table (self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS connection ( 
            id SERIAL PRIMARY KEY,
            pseudo TEXT, 
            password TEXT,
            e_mail TEXT)""")
        self.connection.commit()

    # save identification and password
    def new_registration(self, e_mail, pseudo, password):
        requete_sql = """INSERT INTO connection(pseudo, password, e_mail) VALUES (%s, %s, %s) """
        self.cursor.execute(requete_sql, (pseudo, password, e_mail))
        self.connection.commit()

    # take the names of the table
    def read_registration_name(self):
        requete_sql = """SELECT pseudo FROM connection"""
        self.cursor.execute(requete_sql)
        self.name = self.cursor.fetchall()

    def read_registration_email(self):
        requete_sql = """SELECT e_mail FROM connection"""
        self.cursor.execute(requete_sql)
        self.address = self.cursor.fetchall()
        self.email = self.cursor.fetchall()

    def read_table_player(self, pseudo):
        requete_sql =f"""SELECT player.avatar, player.position_x, player.position_y, player.stamina, player.food, player.hydratation FROM player 
        INNER JOIN connection ON player.id_connection = connection.id
        WHERE connection.pseudo = '{pseudo}'"""
        self.cursor.execute(requete_sql)
        result = self.cursor.fetchall()
        return result

    def create_player(self, information_player) :
        requete_sql ="""INSERT INTO player(id_connection, avatar, position_x, position_y, stamina, food, hydratation)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        self.cursor.execute(requete_sql, (information_player[0], information_player[1], information_player[2], 
        information_player[3], information_player[4], information_player[5], information_player[6]))
        self.connection.commit()

    def id_connection(self, pseudo):
        requete_sql = f""" SELECT id 
                          FROM connection 
                          WHERE connection.pseudo = '{pseudo}'"""
        self.cursor.execute(requete_sql)
        result = self.cursor.fetchone()
        return result

    def id_player(self, id_connection):
        requete_sql = f""" SELECT id 
                          FROM player
                          WHERE id_connection = '{id_connection}'"""
        self.cursor.execute(requete_sql)
        result = self.cursor.fetchone()
        return result

    def update_table_player(self, position_x, position_y, stamina, food, hydratation, id_connection):
        requete_sql = f"""UPDATE player 
                          SET position_x = '{position_x}', position_y = '{position_y}', stamina = '{stamina}', food = '{food}', hydratation = '{hydratation}'
                          WHERE player.id_connection = '{id_connection}'"""
        self.cursor.execute(requete_sql)
        self.connection.commit()

    def read_inventory(self, pseudo):
        requete_sql = f"""SELECT object.name, amount, action.name, category.name, object.stamina, object.food, object.hydratation, inventaire.id_object
                        FROM inventaire
                        INNER JOIN player ON inventaire.id_player = player.id
                        INNER JOIN connection ON player.id_connection = connection.id
                        INNER JOIN object ON inventaire.id_object = object.id
                        INNER JOIN category ON object.id_category = category.id
                        INNER JOIN action ON object.id_action = action.id
                        WHERE connection.pseudo = '{pseudo}'
                        ORDER BY inventaire.id_object, object.name """
        self.cursor.execute(requete_sql)
        return self.cursor.fetchall()

    def read_information_object(self, name):
        requete_sql = f"""SELECT object.name, amount_min, amount_max , action.name, category.name, object.stamina, object.food, object.hydratation, object.id
                        FROM object
                        INNER JOIN category ON object.id_category = category.id
                        INNER JOIN action ON object.id_action = action.id
                        WHERE object.name = '{name}'"""
        self.cursor.execute(requete_sql)
        result = self.cursor.fetchall()

        # Calculer le nombre d'objet avec la valeur min et max de la table 
        min = result[0][1]
        max = result[0][2]
        # Calculer le random
        amount = random.randint(min, max)
        # Transformer la tuple en liste pour delete un element et mettre le nombre d'objet
        result = [x for element in result for x in element]
        del result[2]
        result[1] = amount
        # Transformer en tuple pour la return
        result = tuple(result)
        tuple_result = [result]
        return tuple_result


    def delete_table_inventory(self, id_player):
        requete_sql = f"""DELETE FROM inventaire
                        WHERE id_player = {id_player}"""
        self.cursor.execute(requete_sql)
        self.connection.commit()

    def add_inventory(self, id_player, id_object, amount):
        requete_sql = f"""INSERT INTO inventaire 
        VALUES ({id_player}, {id_object}, {amount})"""
        self.cursor.execute(requete_sql)
        self.connection.commit()

    def update_water(self, id_player, amount) :
        requete_sql = f"""UPDATE inventaire 
                          SET amount = '{amount}'
                          WHERE id_object = 17 and id_player = {id_player}"""
        self.cursor.execute(requete_sql)
        self.connection.commit()




sql = create_registration()
sql.update_water(1, 75)

