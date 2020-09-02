import psycopg2
import hashlib
from getpass import getpass

def lenght_input(entry, mot, max = 16, min = 3) :
        while len(entry) >= max or len(entry) <= min :
            print(f"Choisissez un {mot} entre {min} et {max} caractères")
            entry = input(f"{mot} : ").lower()
        return entry

def forget_psd():
    user_name = (input("Nom d'utilisateur : "),) # On prend l'user
    user_mail = (input("Adresse e-mail : "),) # On prend le mail
    connexion = psycopg2.connect("dbname=Testprojet2 user=postgres password=group12")
    cursor = connexion.cursor()
    cursor.execute(f'SELECT * FROM registration WHERE name = %s AND address = %s', (user_name, user_mail))
    connexion.commit()
    result = cursor.fetchone()
    if result:
        get_new_pwd(user_name,user_mail)
    else : #A Sinon...
        print("Nom d'utilisateur ou adresse e-mail incorrect")
        forget_psd()



def get_new_pwd(name,address):
    """
        #A Si le user et le password sont bons
    """
    user_password = getpass("Votre nouveau mot de passe : ") # On prend le password en xxxx
    user_password = (lenght_input(user_password, "Mot de passe : ", 32, 8))
    user_passwordcheck = getpass("Vérification de mot de passe : ") # On reprend le password en xxxx
    if user_passwordcheck == user_password:
        pass
    else :
        print("Vous n'avez pas entré 2 fois le même mot de passe")
        get_new_pwd(name,address)
    user_password = user_password.encode() #On encode en UTF8
    user_password = (hashlib.sha1(user_password).hexdigest(),) #On le hash en hexa
    connexion = psycopg2.connect("dbname=Testprojet2 user=postgres password=group12")
    cursor = connexion.cursor()
    cursor.execute(f'UPDATE * FROM registration SET password = %s WHERE name = %s AND address = %s', (user_password, name, address))
    connexion.commit()
    

"""
    vérification mot de passe à revoir : Fait
    Gérer la longueur du mot de passe : Fait

"""