# coding:utf-8

#import module
import pygame
import threading
import math


from play.map import Map

class Loading_bar(threading.Thread):

    """
        Premet d'afficher l'image de chargement et la barre de chargement
    """
    def __init__(self, screen, map) :
        # Initialiser le constructeur de la super class threading
        threading.Thread.__init__(self)
        self.screen = screen
        self.bar_loading = 0
        self.map = map
        self.rectangle = pygame.Rect(175, 615, 850, 50)

    def run(self) :
        pygame.mixer.music.load("images/musique/wait.mp3")
        pygame.mixer.music.play()
        while self.bar_loading < 850 :
            self.screen.blit(self.map, (0,0)) 
            pygame.draw.rect(self.screen, (0, 0, 0), [175, 650, 850, 10]) 
            pygame.draw.rect(self.screen, (255,255,255), [175, 650, self.bar_loading, 10]) 
            self.bar_loading += 1
            if self.bar_loading < 250 :
                self.print_advice("Dormez dans votre lit de camp pour sauvegarder votre progression")
            elif self.bar_loading > 250 and self.bar_loading < 500 :
                self.print_advice("Vous ne pouvez pas marcher dans l'eau, ni dans la lave")
            else :
                self.print_advice("Une grotte remplit de tresors est cachée dans le Desert")

            pygame.display.update()
        pygame.mixer.music.stop()

    def print_advice(self, message) :

        font = pygame.font.SysFont(None, 30)
        text = font.render(message, 1, (255,255,255))
        text_rect = text.get_rect()
        text_rect.x = math.ceil(self.screen.get_width() /2 - len(message) * 5.5)
        text_rect.y = 615
        self.screen.blit(text,text_rect)
    


class Loading_map(threading.Thread):

    """
    Premet de charger les map
    """
    def __init__(self, game) :
        # Initialiser le constructeur de la super class threading
        threading.Thread.__init__(self)
        # barre blanche
        self.game = game
        self.bar_loading = 0

    def run(self) :
        self.game.map_foret_sol = self.game.create_map("images/bg/Foret.tmx")
        Map("images/Bg/Foret_obstacle.tmx", self.game.player).obstacle(12800, 6400)
        self.game.map_foret_behind = self.game.create_map("images/bg/Foret_behind.tmx")

        self.game.map_montagne_sol = self.game.create_map("images/bg/Montagne.tmx")
        Map("images/Bg/Montagne_obstacle.tmx", self.game.player).obstacle(6400, 0)
        self.game.map_montagne_behind = self.game.create_map("images/bg/Montagne_behind.tmx")

        self.game.map_marecage_sol = self.game.create_map("images/bg/Marecage.tmx")
        self.game.map_marecage_behind = self.game.create_map("images/bg/Marecage_behind.tmx")

        self.game.map_cratere_sol = self.game.create_map("images/bg/Cratere.tmx")
        self.game.map_cratere_behind = self.game.create_map("images/bg/Cratere_behind.tmx")

        self.game.map_desert_sol = self.game.create_map("images/bg/Desert.tmx")
        Map("images/Bg/Desert_obstacle.tmx", self.game.player).obstacle(0, 6400)
        self.game.map_desert_behind = self.game.create_map("images/bg/Desert_behind.tmx")

def start_loading(screen, game, map_loading) :

    loading_bar = Loading_bar(screen, map_loading)
    loading_map = Loading_map(game)
    loading_bar.start()
    loading_map.start()
    loading_bar.join()
    loading_map.join()

