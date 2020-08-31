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
        self.address = self.cursor.fetchall()