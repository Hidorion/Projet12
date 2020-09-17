import pygame as pyg

class Camera:
    def __init__(self, width, height):
        self.camera = pyg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(800 / 2)
        y = -target.rect.centery + int(800 / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - 800), x)  # right
        y = max(-(self.height - 800), y)  # bottom
        self.camera = pyg.Rect(x, y, self.width, self.height)