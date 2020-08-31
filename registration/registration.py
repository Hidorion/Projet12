# coding: utf-8

#import
from registration.requeteSQL import create_registration
import hashlib
from getpass import getpass


def lenght_input(entry, mot, max = 16, min = 3) :
        while len(entry) >= max or len(entry) <= min :
            print(f"Choisissez un {mot} entre {min} et {max} caractères")
            entry = input(f"{mot} : ").lower()
        return entry

def password():
    mdp = input("Mot de passe : ")
    mdp = (lenght_input(mdp, "Mot de passe", 32, 8))
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
    address = input("address-email : ").lower()
    # put the nickname in tuple to compare it to the table
    address =(address,)
    # check if the pseudo is already taken
    SQL.read_registration_address()
    while address in SQL.address :
        # if yes, return to the start of the while
        print("Cette email est déjà prit")
        address = input("addresse-email :").lower()
        # address = (address,)
    return address 


def user_input():
    SQL = create_registration()
    SQL.create_table()
    address = check_address()
    pseudo = check_pseudo()
    mdp_encrypte = password()

    # save registration
    SQL.new_registration(address, pseudo, mdp_encrypte)
    print("Votre inscription a bien été enregistrée")


