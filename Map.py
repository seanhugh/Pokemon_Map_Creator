#!/usr/bin/env python
import pygame
import spritesheet
from sprite_sheet_anim import SpriteStripAnim
import map_creator
#map is the class that handles all of the objects and backgrounds and presents them in a paintable format
class maps(object):
    def __init__(self, display):
        self.display = display
        map_creator.create(self, 0)
    backgrounds = []
    current_background = 0
    objects = []
    player = 0
    horizontal_shift = 0
    vertical_shift= 0
    def draw_background(self):
        self.current_background.draw(self.horizontal_shift,self.vertical_shift)
    def draw_objects(self):
        for i in self.objects:
            if i.yloc<self.player.yloc:
                i.draw(self.horizontal_shift, self.vertical_shift)
        self.player.draw()
        for i in self.objects:
            if i.yloc>=self.player.yloc:
                i.draw(self.horizontal_shift, self.vertical_shift)
        
    def switch_right(self):
        map_creator.create(self, self.current_background.right)
        self.horizontal_shift = 0
    def switch_left(self):
        map_creator.create(self, self.current_background.left)
        self.horizontal_shift = -self.current_background.width*20 + 20*20
    def switch_up(self):
        map_creator.create(self, self.current_background.up)
        self.vertical_shift = -self.current_background.height*20 + 20*20
    def switch_down(self):
        map_creator.create(self, self.current_background.down)
        self.vertical_shift = 0
        pass
    def is_taken(self, x, y):
        for i in self.objects:
            for j in i.taken_squares:
                if j[0] == x and j[1] == y:
                    return True
        return False
    def draw(self):
        self.draw_background()
        self.draw_objects()
    def move_screen(self, x, y):
        width = self.current_background.width
        height = self.current_background.height
        if x*20 > -self.horizontal_shift +15*20 and -self.horizontal_shift + 20*20 <= width*20:
            self.horizontal_shift -= 1
        if x*20 < -self.horizontal_shift +5*20  and self.horizontal_shift < 0:
            self.horizontal_shift += 1
        if y*20 > -self.vertical_shift +15*20 and -self.vertical_shift + 20*20 <= height*20:
            self.vertical_shift -= 1
        if y*20 < -self.vertical_shift +5*20 and self.vertical_shift < 0:
            self.vertical_shift += 1
        pass
    def adjust_shift(self, x,y):
        if x> 20:
            self.horizontal_shift = -(x - 20)
        if y>20:
            self.vertical_shift = -(y - 20)
        
    
'''background is the class that handles the texture, size and location of the background. Paramaters are width,
height, texture_grid, index, up, right, down, left, map1, display'''
class background(object):
    def __init__(self, width, height, texture_grid, index, up, right, down, left, map1, display):
        self.texture_grid=texture_grid
        self.index = index
        self.right = right
        self.left = left
        self.up = up
        self.down = down
        map1.current_background = self
        self.display = display
        self.texture0 = SpriteStripAnim('images/grass_textures.png', (5,5,25,25), 1, (255,255,255), True, 1)
        self.texture0 = self.texture0.next()
        self.texture1 = SpriteStripAnim('images/grass_textures.png', (70,5,25,25), 1, (255,255,255), True, 1)
        self.texture1 = self.texture1.next()
        self.texture2 = SpriteStripAnim('images/grass_textures.png', (135,5,25,25), 1, (255,255,255), True, 1)
        self.texture2 = self.texture2.next()
        self.texture3 = SpriteStripAnim('images/grass_textures.png', (200,5,25,25), 1, (255,255,255), True, 1)
        self.texture3 = self.texture3.next()
        self.width = width
        self.height = height
    def draw(self, x_shift, y_shift):
        x_shift = x_shift
        y_shift = y_shift
        for i in self.texture_grid:
            if i[0] == 0:
                self.display.paint(self.texture0, (i[1]*20 + x_shift, i[2]*20+y_shift))
            if i[0] == 1:
                self.display.paint(self.texture1, (i[1]*20+ x_shift, i[2]*20+y_shift))
            if i[0] == 2:
                self.display.paint(self.texture2, (i[1]*20+ x_shift, i[2]*20+y_shift))
            if i[0] == 3:
                self.display.paint(self.texture3, (i[1]*20+ x_shift, i[2]*20+y_shift))
#creates a background... if you use an int(which is on eof the 4 textures, it will fill the background with that... else you can create
# a 20x20 grid and fill in the textures for each as a list) Up right down and left determine which spot on the map it will swithc too if
# you leave the map
def create_background(width, height, layout, index, up, right, down, left, map1):
    if str(type(layout)) == "<type 'int'>":
        templist=[]
        for i in range(width):
            for j in range(height):
                templist.append([layout, i, j])
        background(width, height, templist, index, up, right, down, left, map1, map1.display)
    else:
        background(width, height, layout, index, up, right, down, left, map1, map1.display)

    