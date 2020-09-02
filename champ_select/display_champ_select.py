# coding: utf-8

#import
import pygame
from champ_select.load_character import Avatar


screen = pygame.display.set_mode((800, 600))
avatar = Avatar(screen)

def champ_select(screen, background) :


    screen.blit(background, (0,0))

    # for event in pygame.event.get():

    #     # if event.type == pygame.QUIT :
    #     #     champ_select = False

    avatar.update(screen)
    pygame.display.flip()
            # elif event.type == pygame.KEYDOWN :
            #     game.pressed[event.key] = True

            # elif event.type == pygame.KEYUP :
            #     game.pressed[event.key] = False
