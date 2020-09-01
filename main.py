# coding: utf-8

#import
import hashlib
import pygame
from registration.requeteSQL import create_registration
from registration.registration import user_input
from getpass import getpass
from registration.connection import forget_psd


pygame.init()
pygame.display.set_caption("Projet 2")
screen = pygame.display.set_mode(1080, 720)

background = pygame.image.load("background/desert.jpg")


if __name__ == "__main__":