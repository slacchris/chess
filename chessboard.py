import pygame 
from pygame.locals import *

class Square(pygame.sprite.Sprite):
    def __init__(self, color):
        super(Square, self).__init__()

        self.color = color

        self.surface = pygame.Surface((25, 25))
        
        if self.color.lower() == "white":
            #255, 253, 208 are the values for a cream color
            self.surface.fill((255, 253, 208))
        elif self.color.lower() == "black":
            self.surface.fill(0,0,0)

