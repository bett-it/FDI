import pygame

class Box:
    # axes
    # 0 - - - - -> width
    # |
    # |
    # |
    # V
    # height
    def __init__(self, width=100, height=100):
        self.width = width
        self.height = height

    def draw(self,window):
        pygame.draw.rect(window,(100,100,100),(0,0,self.width,self.height))
