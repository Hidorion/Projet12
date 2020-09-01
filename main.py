# coding: utf-8

#import
import hashlib
import pygame
import math
from play.game import Game
from registration.requeteSQL import create_registration
from registration.registration import user_input
from getpass import getpass
from registration.connection import forget_psd



pygame.init()
pygame.display.set_caption("Projet 2")
screen = pygame.display.set_mode((800, 600))

background_forest = pygame.image.load("images/bg/desert.jpg")
clock = pygame.time.Clock()


game = Game(screen)

running = True

if __name__ == "__main__":

    while running :

        screen.blit(background_forest, (0,0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT :
                running = False

            elif event.type == pygame.KEYDOWN :
                game.pressed[event.key] = True

            elif event.type == pygame.KEYUP :
                game.pressed[event.key] = False

                
        # game.movement(screen, event.type)
        game.update(screen)
        # clock.tick(120)
        pygame.display.flip()