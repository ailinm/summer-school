import pygame
import random
import snake

from pygame.locals import *

class GameException(Exception):
    pass

class Settings(object):
    def __init__(self):
        self.resolution = ( 800, 600)
        self.background = (255, 228, 225)
        self.title = "Snake" 

class Game(object):

    def __init__(self, settings = Settings()):
        pygame.init()
        self.loadSettings(settings)
        self.clock = pygame.time.Clock()
        self.snakeParts = [snake.SnakePart(400,300, self.background)]
        self.gameObjects = [self.snakeParts[0]]
        self.sprites = pygame.sprite.RenderPlain(self.gameObjects)

        self.move_timer = 0

    def loadSettings(self, settings):
        self.screen = pygame.display.set_mode(settings.resolution)
        pygame.display.set_caption(settings.title)
        pygame.mouse.set_visible(False)

        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill(settings.background)

    def run(self):
        isRunning = True
        while True:
            try:
                self.tick()
                if not isRunning:
                    return
            except GameException:
                return

    def tick(self):
        self.clock.tick(60)
        moved = False
        for event in pygame.event.get():
            if event.type == QUIT:
                raise GameException
            elif event.type == KEYDOWN:
                if event.key == 273:
                    self.snakeParts[0].moveTo(1)
                    moved = True
                if event.key == 274:
                    self.snakeParts[0].moveTo(2)
                    moved = True
                if event.key == 276:
                    self.snakeParts[0].moveTo(3)
                    moved = True
                if event.key == 275:
                    self.snakeParts[0].moveTo(4)
                    moved = True
        if not moved:
            self.move_timer = self.move_timer+1
            if self.move_timer == 10:
                self.snakeParts[0].moveTo(self.snakeParts[0].lastDirection)
                self.move_timer = 0
        else:
            self.move_timer = 0
        
        
        self.sprites.update()
        self.screen.blit(self.background,(0,0))
        self.sprites.draw(self.screen)
        pygame.display.flip()
