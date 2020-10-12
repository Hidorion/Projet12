# coding: utf-8

#import
import hashlib
import psycopg2
from getpass import getpass


from core.registration.sql_queries import create_registration
from validate_email import validate_email

import pygame
#from connection import check_logs



def lenght_input(entry, mot, max = 16, min = 3) : #Allows to control the lenght of text typed
        while len(entry) >= max or len(entry) <= min :
            print(f"Choisissez un {mot} entre {min + 1} et {max} caractères")
            entry = input(f"{mot} : ").lower()
        return entry



def password(information): #check if password matches

    mdp = information[2]
    mdp2 = information[3] # On reprend le password en xxxx
    if mdp != mdp2:
        print("message(screen, ""Vos mots de passe ne correspondent pas"", x, y)")
        mdp_encrypte = None
        return mdp_encrypte#password(information)
    # Encode the string in UTF-8 encoding, necessary for this to hash the pwd
    # mdp = mdp.encode()
    # # # Allows you to encode the pwd
    # mdp_encrypte = hashlib.sha1(mdp).hexdigest()
    return mdp
    #return mdp

def check_pseudo(information, screen, x, y): #Check if pseudo already exists
    SQL = create_registration()

    pseudo = (information[0],)
    pseudo = str(pseudo[0])
    print(pseudo)
    # put the nickname in tuple to compare it to the table
    # check if the pseudo is already taken
    SQL.read_registration_name()
    if not pseudo:
        print("message(screen, ""Votre pseudo ne doit pas être vide"", x, y)")
        pseudo = None
    if pseudo in SQL.name :
        print("message(screen, ""Cette identifiant est déjà prit"", x, y)")
        pseudo = None

        #pseudo = (pseudo,)
    return pseudo 

def check_email(information, screen, x, y):
    SQL = create_registration()
    email = (information[1],)
    email = str(email[0])
    if validate_email(email) != False:
        SQL.read_registration_email()
        if email in SQL.email :
            print("message(screen, ""Cette email est déjà utilisée"", x, y)")
            email = None
    else :
        print("message(screen, ""Saisissez une adresse valide"", x, y)")    
        email = None
        return email 
    # while validate_email(email) == False :
    #     #message(screen, "Saisissez une adresse valide", x, y)
    #     email = information[1]
    # SQL.read_registration_email()
    # if email in SQL.email :
    #     print("message(screen, ""Cette email est déjà utilisée"", x, y)")    
    # while email in SQL.email :
    #     # if yes, return to the start of the while
    #     #message(screen, "Cette email est déjà prit", x, y)
    #     email = information[1].lower()
    #     # while validate_email(email) == False :
    #     #     
    #     #     email = information[1]
    #     email = (email,)
    return email 



def sign_up(information, screen, x, y): #Inscription
    SQL = create_registration()
    email = check_email(information, screen, x, y)
    pseudo = check_pseudo(information, screen, x, y)
    mdp_encrypte = password(information)
    if pseudo != None and email != None and mdp_encrypte != None:
        # save registration
        SQL.new_registration(email, pseudo, mdp_encrypte)
        print(pseudo,email,mdp_encrypte)
        print('message(screen, "Votre inscription a bien été enregistrée", x, y)')
        return True


# def message(self, screen, #message, x, y):
        # font = pygame.font.SysFont(None, 20)
        # text = font.render(#message, 1, (255,255,255))
        # text_rect = text.get_rect()
        # text_rect.x = x
        # text_rect.y = y
        # screen.blit(text,text_rect)


