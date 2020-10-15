# coding:utf-8

#import module
import pygame
import threading
import math


from core.play.map import Map

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

    def run(self) :
        pygame.mixer.music.load("assets/music/wait.mp3")
        pygame.mixer.music.play()
        while self.bar_loading < 850 :
            self.screen.blit(self.map, (0,0)) 
            pygame.draw.rect(self.screen, (0, 0, 0), [175, 675, 850, 10]) 
            pygame.draw.rect(self.screen, (255,255,255), [175, 675, self.bar_loading, 10]) 
            self.bar_loading += 2
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
        text_rect.y = 645
        self.screen.blit(text,text_rect)
    


class Loading_map(threading.Thread):

    """
    Premet de charger les map
    """
    def __init__(self, game, screen) :
        # Initialiser le constructeur de la super class threading
        threading.Thread.__init__(self)
        # barre blanche
        self.game = game

    def run(self) :
        self.game.map_foret_sol = self.game.create_map("assets/backgrounds/Foret.tmx")
        self.game.map_foret_behind = self.game.create_map("assets/backgrounds/Foret_behind.tmx")

        # self.game.map_desert_sol = self.game.create_map("assets/backgrounds/Desert.tmx")
        # Map("assets/backgrounds/Desert_obstacle.tmx", self.game).obstacle(0, 6400)
        # self.game.map_desert_behind = self.game.create_map("assets/backgrounds/Desert_behind.tmx")      
        # 
class Loading_interaction(threading.Thread):

    """
    Premet de charger les map
    """
    def __init__(self, game, screen) :
        # Initialiser le constructeur de la super class threading
        threading.Thread.__init__(self)
        # barre blanche
        self.game = game

    def run(self) :
        Map("assets/backgrounds/Foret_obstacle.tmx", self.game).obstacle(12800, 0)
        Map("assets/backgrounds/Foret_interaction.tmx", self.game).interaction(12800, 0) 

def start_loading(screen, game, map_loading) :

    loading_bar = Loading_bar(screen, map_loading)
    loading_map = Loading_map(game, screen)
    loading_interaction = Loading_interaction(game,screen)
    loading_interaction.start()
    loading_bar.start()
    loading_map.start()
    loading_interaction.join()
    loading_bar.join()
    loading_map.join()


