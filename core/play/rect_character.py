# coding : utf-8
import pygame

<<<<<<< HEAD:core/play/character_rect.py
class Character_rect():
=======
class Rect_character():
    """
        Créé un objet qui remplace le rect du player
    """
>>>>>>> origin/Laura:core/play/rect_character.py

    def __init__(self, x, y):
        self.image = pygame.Surface((28, 15))
        self.rect = self.image.get_rect()
        self.rect.x = x + 2
        self.rect.y = y + 15

