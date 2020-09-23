# coding: utf-8

#import
import psycopg2

class create_registration():

    def __init__(self):
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
        self.address = self.cursor.fetchall()