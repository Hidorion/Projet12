# A. Here we create a fake db with fake infos to check when we log in if the user and password are both correct.

import psycopg2

def create_table():
    """
        Create the table in the database
    """
    connexion = psycopg2.connect("dbname=logs user=postgres password=12")
    cursor = connexion.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS user_infos (id SERIAL PRIMARY KEY, name TEXT, password TEXT, avatar TEXT)')
    connexion.commit()
    connexion.close()

def adding_data():
    """
        Adding fake data to the tables
    """
    connexion = psycopg2.connect("dbname=logs user=postgres password=12")
    cursor = connexion.cursor()
    cursor.execute("INSERT INTO user_infos (name, password, avatar) VALUES ( 'Paul', 'jaimemamaman', 'Rouge et noir')")
    cursor.execute("INSERT INTO user_infos (name, password, avatar) VALUES ( 'Hector', 'azerty', 'Blanc et bleu')")
    cursor.execute("INSERT INTO user_infos (name, password, avatar) VALUES ( 'Phil', 'tarzan', 'Blanc et bleu')")
    connexion.commit()


adding_data()