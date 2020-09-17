import math
import pygame as pyg
from play import Variables as var

class Camera:
    def __init__(self, width, height):
        self.camera = pyg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def update(self, target):

        x =  -target.centerx  + int(var.x_screen // 2)
        y =  -target.centery + int(var.y_screen // 2)

        # limit scrolling to map size
        # x = min(0, x)  # left
        # y = min(0, y)  # top
        # x = max(-(self.width - var.x_screen), x)  # right
        # y = max(-(self.height - var.y_screen), y)  # bottom
        
        self.camera = pyg.Rect(x, y, self.width, self.height)