import pygame as pyg
import pytmx as pyx
import sys
from classfile import *

class Game:
    def __init__(self):
        pyg.init()
        self.screen = pyg.display.set_mode((WIDTH, HEIGHT))
        pyg.display.set_caption(TITLE)
        self.clock = pyg.time.Clock()
        self.load_data()
    
    def load_data(self):
        self.map = TiledMap('Alex/maptest/map_test.tmx')
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

    def draw(self):
        pyg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.camera = Camera(self.map.width, self.map.height)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        pyg.display.flip()

if __name__ == "__main__":
    pass




g = Game()
while True :
    g.draw()