# coding: utf-8

#import
import psycopg2
import hashlib
from getpass import getpass

def forget_psd():
    user_name = (input("Nom d'utilisateur : ").lower(),) # On prend l'user
    user_mail = (input("Adresse e-mail : "),) # On prend le mail
    connexion = psycopg2.connect("dbname=Testprojet2 user=postgres password=group12")
    cursor = connexion.cursor()
    cursor.execute(f'SELECT * FROM registration WHERE name = %s AND address = %s', (user_name, user_mail))
    connexion.commit()
    result = cursor.fetchone()
    if result: #A Si le user et le password sont bons
        user_password = getpass("Mot de passe : ") # On prend le password en xxxx
        user_passwordcheck = getpass("Vérification de mot de passe : ") # On reprend le password en xxxx
        if user_passwordcheck == user_password:
            pass
        else :
            print("Vous n'avez entré 2 fois le même mot de passe")
            forget_psd()
        user_password = user_password.encode() #On encode en UTF8
        user_password = (hashlib.sha1(user_password).hexdigest(),) #On le hash en hexa
        connexion = psycopg2.connect("dbname=Testprojet2 user=postgres password=group12")
        cursor = connexion.cursor()
        cursor.execute(f'UPDATE registration SET password = %s WHERE name = %s AND address = %s', (user_password, user_name, user_mail))
        connexion.commit()
    else : #A Sinon...
        print("Nom d'utilisateur ou adresse e-mail incorrect")
        forget_psd()