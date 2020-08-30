# coding: utf-8

#import
import psycopg2

class create_registration():

    def __init__(self):
        self.connexion = psycopg2.connect("dbname=Testprojet2 user=postgres password=group12")
        self.cursor = self.connexion.cursor()
        self.player = []

    def create_table (self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS registration ( 
            id SERIAL PRIMARY KEY,
            name TEXT, 
            password TEXT)""")
        self.connexion.commit()

    # save identification and password
    def new_registration(self, name, password):
        requete_sql = """INSERT INTO registration(name, password) VALUES (%s, %s) """
        self.cursor.execute(requete_sql, (name, password))
        self.connexion.commit()

    # take the names of the table
    def read_registration(self):
        requete_sql = """SELECT name FROM registration"""
        self.cursor.execute(requete_sql)
        self.player = self.cursor.fetchall()