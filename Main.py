#!/usr/bin/env python
import pygame
from pygame.locals import Color, KEYUP, K_ESCAPE, K_RETURN
import spritesheet
from sprite_sheet_anim import SpriteStripAnim
import sys
import Display
from Player import player
pygame.init()
display = Display()