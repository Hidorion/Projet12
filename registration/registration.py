# coding: utf-8

#import
from requeteSQL import create_registration
import hashlib
from getpass import getpass
from validate_email import validate_email
#from connection import check_logs

def lenght_input(entry, mot, max = 16, min = 3) :
        while len(entry) >= max or len(entry) <= min :
            print(f"Choisissez un {mot} entre {min + 1} et {max} caractères")
            entry = input(f"{mot} : ").lower()
        return entry

def password():
    mdp = getpass("Mot de passe : ")
    mdp = (lenght_input(mdp, "Mot de passe", 32, 7))
    user_passwordcheck = getpass("Vérification de mot de passe : ") # On reprend le password en xxxx
    if user_passwordcheck == mdp:
        pass
    else :
        password()
    # Encode the string in UTF-8 encoding, necessary for this to hash the mdp
    mdp = mdp.encode()
    # Allows you to encode the mdp
    mdp_encrypte = hashlib.sha1(mdp).hexdigest()
    return mdp_encrypte
    

def check_pseudo():
    SQL = create_registration()
    pseudo = input("Pseudonyme : ").lower()
    pseudo = (lenght_input(pseudo, "Pseudonyme"))
    # put the nickname in tuple to compare it to the table
    pseudo =(pseudo,)
    # check if the pseudo is already taken
    SQL.read_registration_name()
    while pseudo in SQL.name :
        # if yes, return to the start of the while
        print("Cette identifiant est déjà prit")
        pseudo = input("Pseudonyme ").lower()
        pseudo = (lenght_input(pseudo, "Pseudonyme"))
        pseudo = (pseudo,)
    return pseudo 

def check_address():
    SQL = create_registration()
    address = input("adress-email : ").lower()
    while validate_email(address) == False :
        print("Saisissez une adresse valide")
        address = input("adress-email : ").lower()
    address =(address,)
    SQL.read_registration_address()
    
    while address in SQL.address :
        # if yes, return to the start of the while
        print("Cette email est déjà prit")
        address = input("adresse-email :").lower()
        while validate_email(address) == False :
            print("Saisissez une adresse valide")
            address = input("adress-email : ").lower()
        address = (address,)
    return address 


def sign_in():
    SQL = create_registration()
    SQL.create_table()
    address = check_address()
    pseudo = check_pseudo()
    mdp_encrypte = password()

    # save registration
    SQL.new_registration(address, pseudo, mdp_encrypte)
    print("Votre inscription a bien été enregistrée")
    check_logs()


