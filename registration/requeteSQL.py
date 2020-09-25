# coding: utf-8

#import
import psycopg2

class create_registration():

    def __init__(self):
        #self.connexion = psycopg2.connect("dbname=Projet12 user=postgres password=group12")
        self.connexion = psycopg2.connect("dbname=postgres user=postgres password=12")
        self.cursor = self.connexion.cursor()
        self.name = []
        self.email = []

    def create_table (self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS connection ( 
            id SERIAL PRIMARY KEY,
            pseudo TEXT, 
            password TEXT,
            e_mail TEXT)""")
        self.connexion.commit()

    # save identification and password
    def new_registration(self, e_mail, pseudo, password):
        requete_sql = """INSERT INTO connection(pseudo, password, e_mail) VALUES (%s, %s, %s) """
        self.cursor.execute(requete_sql, (pseudo, password, e_mail))
        self.connexion.commit()

    # take the names of the table
    def read_registration_name(self):
        requete_sql = """SELECT pseudo FROM connection"""
        self.cursor.execute(requete_sql)
        self.name = self.cursor.fetchall()

    def read_registration_email(self):
        requete_sql = """SELECT e_mail FROM connection"""
        self.cursor.execute(requete_sql)
        self.email = self.cursor.fetchall()

    def read_table_player(self, pseudo):
        requete_sql =f"""SELECT player.avatar, player.position_x, player.position_y FROM player 
                        INNER JOIN connection ON player.id_connection = connection.id
                        WHERE connection.pseudo = '{pseudo}'"""
        self.cursor.execute(requete_sql)
        result = self.cursor.fetchall()
        return result

    def create_player(self, information_player) :
        requele_sql ="""INSERT INTO player(id_connection, avatar, position_x, position_y, stamina, food, hydratation)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        self.cursor.execute(requele_sql, (information_player[0], information_player[1], information_player[2], 
        information_player[3], information_player[4], information_player[5], information_player[6]))
        self.connexion.commit()