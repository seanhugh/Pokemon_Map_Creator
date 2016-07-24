#!/usr/bin/env python
import pygame
#a display class which makes the GUI creation more simple
class Display:
    def __init__(self):
        self.WHITE    = ( 255, 255, 255)
        self.BLACK     = (  0,   0,   0)
        self.screen = pygame.display.set_mode([400, 400])
    def paint(self, image, (x,y)):
        self.screen.blit(image, (x, y))
    