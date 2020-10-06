# coding: utf-8

#import
import psycopg2
import hashlib
from getpass import getpass

###########################
##### connection infos #####
###########################
# connection_infos = "dbname=Projet12 user=postgres password=group12"

connection_infos = "dbname=Projet12 user=postgres password=douzetrentedeux"


# def lenght_input(entry, mot, max = 16, min = 3) :
#         while len(entry) >= max or len(entry) <= min :
#             print(f"Choisissez un {mot} entre {min} et {max} caractères")
#             entry = input(f"{mot} : ").lower()
#         return entry
        
        
def forget_psd():
    user_name = (input("Nom d'utilisateur : ").lower(),) # On prend l'user
    user_mail = (input("Adresse e-mail : ").lower(),) # On prend le mail
    connection = psycopg2.connect(connection_infos)
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM connection WHERE pseudo = %s AND address = %s', (user_name, user_mail))
    connection.commit()
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
    user_password = (lenght_input(user_password, "Mot de passe : ", 32, 7))
    user_passwordcheck = getpass("Vérification de mot de passe : ") # On reprend le password en xxxx
    if user_passwordcheck == user_password:
        pass
    else :
        print("Vous n'avez pas entré 2 fois le même mot de passe")
        get_new_pwd(name,address)
    user_password = user_password.encode() #On encode en UTF8
    user_password = (hashlib.sha1(user_password).hexdigest(),) #On le hash en hexa
    connection = psycopg2.connect(connection_infos)
    cursor = connection.cursor()
    cursor.execute(f'UPDATE connection SET password = %s WHERE pseudo = %s AND address = %s', (user_password, name, address))
    connection.commit()
    
    
"""
    vérification mot de passe à revoir : Fait
    Gérer la longueur du mot de passe : Fait

"""

def check_logs(inputs_tuple):
    user_name = inputs_tuple[0] #(input("Nom d'utilisateur : "),) # On prend l'user
    user_password = inputs_tuple[1] #getpass("Mot de passe : ") # On prend le password en xxxx
    #user_password = user_password.encode() #On encode en UTF8
    #user_password = (hashlib.sha1(user_password).hexdigest(),) #On le hash en hexa
    connection = psycopg2.connect(connection_infos)
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM connection WHERE pseudo = %s AND password = %s', (user_name, user_password))
    connection.commit()
    result = cursor.fetchone()
    if result: #A Si le user et le password sont bons
        return True
        print("ok")
    else : #A Sinon..."é&"
        return False



