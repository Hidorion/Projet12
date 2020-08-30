# coding: utf-8

#import
from registration.requeteSQL import create_registration
import hashlib
from getpass import getpass

def password():
    mdp = getpass("Mot de passe : ")
    # Encode the string in UTF-8 encoding, necessary for this to hash the mdp
    mdp = mdp.encode()
    # Allows you to encode the mdp
    mdp_encrypte = hashlib.sha1(mdp).hexdigest()
    return mdp_encrypte

def check_pseudo():
    SQL = create_registration()
    pseudo = input("Identifiant : ").lower()
    while len(pseudo) > 13 or len(pseudo) < 1 :
        print("Choisissez un pseudo entre 1 et 10 caractères")
        pseudo = input("Identifiant : ").lower()
    # put the nickname in tuple to compare it to the table
    pseudo =(pseudo,)
    # check if the pseudo is already taken
    SQL.read_registration()
    while pseudo in SQL.player :
        # if yes, return to the start of the while
        print("Cette identifiant est déjà prit")
        pseudo = input("Identifiant : ").lower()
        while len(pseudo) > 13 or len(pseudo) < 1 :
            print("Choisissez un pseudo entre 1 et 10 caractères")
            pseudo = input("Identifiant : ").lower()
        pseudo =(pseudo,)
    return pseudo 

def user_input():
    SQL = create_registration()
    SQL.create_table()
    pseudo = check_pseudo()
    mdp_encrypte = password()

    # save registration
    SQL.new_registration(pseudo, mdp_encrypte)
    print("Votre inscription a bien été enregistrée")

