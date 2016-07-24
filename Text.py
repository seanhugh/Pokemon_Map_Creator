#!/usr/bin/env python
import pygame
class text_box(object):
    def __init__(self, display):
        self.display = display
        self.image = pygame.image.load("images/text.png")
    def draw(self):
        self.display.paint(self.image, (0,328))
        
    


