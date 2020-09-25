# coding: utf-8

#import
import psycopg2

class create_registration():

    def __init__(self):
        self.connexion = psycopg2.connect("dbname=Testprojet2 user=postgres password=group12")
        self.cursor = self.connexion.cursor()
        self.name = []
        self.address = []

    def create_table (self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS registration ( 
            id SERIAL PRIMARY KEY,
            address TEXT,
            name TEXT, 
            password TEXT)""")
        self.connexion.commit()

    # save identification and password
    def new_registration(self, address, name, password):
        requete_sql = """INSERT INTO registration(address, name, password) VALUES (%s, %s, %s) """
        self.cursor.execute(requete_sql, (address, name, password))
        self.connexion.commit()

    # take the names of the table
    def read_registration_name(self):
        requete_sql = """SELECT name FROM registration"""
        self.cursor.execute(requete_sql)
        self.name = self.cursor.fetchall()

    def read_registration_address(self):
        requete_sql = """SELECT address FROM registration"""
        self.cursor.execute(requete_sql)
<<<<<<< Updated upstream
        self.address = self.cursor.fetchall()
=======
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
        self.connexion.commit()

    def id_connection(self, pseudo):
        requete_sql = f""" SELECT id 
                          FROM "connection" 
                          WHERE connection.pseudo = '{pseudo}'"""
        self.cursor.execute(requete_sql, pseudo)
        result = self.cursor.fetchone()
        return result

    def update_table_player(self, position_x, position_y, stamina, food, hydratation, id_connection):
        requete_sql = f"""UPDATE player 
                          SET position_x = '{position_x}', position_y = '{position_y}', stamina = '{stamina}', food = '{food}', hydratation = '{hydratation}'
                          WHERE player.id_connection = '{id_connection}'"""
        self.cursor.execute(requete_sql)
        self.connexion.commit()
>>>>>>> Stashed changes
