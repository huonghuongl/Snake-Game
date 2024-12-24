import sys,time
import pygame 
from random import randint
from UI import *
WIDTH = 1600
HEIGHT = 900

COLOR = '#000000'

MOUSE_LEFT = 0
MOUSE_MIDDLE = 1
MOUSE_RIGHT = 2
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
running = True

BG_IMG = 'Little-Big-Snake-640.jpg'
THEME_IMG = 'theme.png'

class App:
    
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1500,755))
        pygame.display.set_caption("Menu")
        self.user_input = None
        self.mouse_input = None

        self.bg = pygame.transform.scale(pygame.image.load(BG_IMG).convert_alpha(), (WIDTH, HEIGHT))
        self.menu = Menu(self)

    def update(self):
        self.menu.update()

    def draw(self):
        self.surface.blit(self.bg, (0, 0))
        self.menu.draw()


    def run(self):

        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.menu.eventHandling(e)

            self.user_input = pygame.key.get_pressed()
            self.mouse_input = pygame.mouse.get_pressed()  # 0 - mouse left, 1 - mouse middle, 2 - mouse right

            self.update()
            self.draw()

            pygame.display.flip()


if __name__ == '__main__':
    app = App()
    app.run()