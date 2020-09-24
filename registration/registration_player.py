# coding: utf-8

#import
import hashlib
from getpass import getpass


from registration.requeteSQL import create_registration
from validate_email import validate_email

import pygame
#from connection import check_logs

def lenght_input(entry, mot, max = 16, min = 3) :
        while len(entry) >= max or len(entry) <= min :
            print(f"Choisissez un {mot} entre {min + 1} et {max} caractères")
            entry = input(f"{mot} : ").lower()
        return entry

def password(information):
    mdp = information[2]
    mdp2 = information[3] # On reprend le password en xxxx
    if mdp != mdp2:
        print("message(screen, ""Vos mots de passe ne correspondent pas"", x, y)")
        #password(information)
    # Encode the string in UTF-8 encoding, necessary for this to hash the pwd
    # mdp = mdp.encode()
    # # Allows you to encode the pwd
    # mdp_encrypte = hashlib.sha1(mdp).hexdigest()
    # return mdp_encrypte
    return mdp

def check_pseudo(information, screen, x, y):
    SQL = create_registration()
    pseudo = information[0]
    # put the nickname in tuple to compare it to the table
    # check if the pseudo is already taken
    SQL.read_connection_pseudo()
    if pseudo in SQL.pseudo :
        print("message(screen, ""Cette identifiant est déjà prit"", x, y)")
        information[0] = ''
        pseudo = (pseudo,)
    else :
        return pseudo 

def check_email(information, screen, x, y):
    
    email = information[1]
    # while validate_email(email) == False :
    #     #message(screen, "Saisissez une adresse valide", x, y)
    #     email = information[1]
    SQL.read_connection_e_mail()
    
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
    email = check_email(information, screen, x, y)
    pseudo = check_pseudo(information, screen, x, y)
    mdp_encrypte = password(information)

    # save registration
    SQL.new_connection(email, pseudo, mdp_encrypte)
    #message(screen, "Votre inscription a bien été enregistrée", x, y)


# def message(self, screen, #message, x, y):
        # font = pygame.font.SysFont(None, 20)
        # text = font.render(#message, 1, (255,255,255))
        # text_rect = text.get_rect()
        # text_rect.x = x
        # text_rect.y = y
        # screen.blit(text,text_rect)


