#!/usr/bin/env python
import pygame
import spritesheet
from sprite_sheet_anim import SpriteStripAnim
'''the player class has paramaters xloc, yloc, display, map1. display is the display which it is drawn on, and map1 is the map which
it is drawn on this class handles sprites, movement and more'''
class Player(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, display, map1):
        pygame.sprite.Sprite.__init__(self)
        #im using a grid based interface of places 1 - 20 for each map.
        self.xloc = xloc
        self.yloc = yloc
        self.current_x = xloc
        self.current_y = yloc
        self.counter = 0
        frames = 10
        self.down = SpriteStripAnim('images/sprite_sheet.png', (0,0,25,30), 3, (255,255,255), True, frames)
        self.left = SpriteStripAnim('images/sprite_sheet.png', (0,65,25,30), 3, (255,255,255), True, frames)
        self.up = SpriteStripAnim('images/sprite_sheet.png', (0,35,25,30), 3, (255,255,255), True, frames)
        self.right = SpriteStripAnim('images/sprite_sheet.png', (0,100,25,30), 3, (255,255,255), True, frames)
        self.image = self.down.next()
        self.display = display
        self.map1 = map1
        self.map1.player = self
    def move(self, x, y):
        background = self.map1.current_background
        if self.check_for_collision(self.xloc + x,self.yloc + y)==False:
            self.xloc += x
            self.yloc += y
        else:
            if x == 1:
                self.image = self.right.next()
            if x == -1:
                self.image = self.left.next()
            if y == -1:
                self.image = self.up.next()
            if y == 1:
                self.image = self.down.next()
        #this checks to see if you are moving off of the screen
        if self.xloc>background.width-1:
            self.map1.switch_right()
            self.xloc = 0
            self.current_x = -1
        elif self.xloc<0:
            self.map1.switch_left()
            self.xloc = self.map1.current_background.width - 1
            self.current_x = self.map1.current_background.width
        elif self.yloc<0:
            self.map1.switch_up()
            self.yloc = self.map1.current_background.height - 1
            self.current_y = self.map1.current_background.height
        elif self.yloc>background.height:
            self.map1.switch_down()
            self.yloc = 0
            self.current_y = -1
        #this readjusts the window to have the dude in it
        
    def draw(self):
        #if the player is not moving
        accounting_for_vertical_sprite = 10
        x_shift = self.map1.horizontal_shift
        y_shift = self.map1.vertical_shift + accounting_for_vertical_sprite
        if (self.current_x == self.xloc and self.current_y == self.yloc):
            self.display.paint(self.image, (self.current_x * 20 + x_shift, self.current_y * 20 + y_shift))
        else:
            self.counter += 1
            #right
            if self.current_x < self.xloc:
                self.display.paint(self.image, (self.current_x * 20 + self.counter + x_shift, self.current_y * 20 + y_shift))
                self.image = self.right.next()
            #left
            elif self.current_x > self.xloc:
                self.display.paint(self.image, (self.current_x * 20 - self.counter + x_shift, self.current_y * 20 + y_shift))
                self.image = self.left.next()
            #down
            elif self.current_y < self.yloc:
                self.display.paint(self.image, (self.current_x * 20 + x_shift, self.current_y * 20 + self.counter + y_shift))
                self.image = self.down.next()
            #up
            elif self.current_y > self.yloc:
                self.display.paint(self.image, (self.current_x * 20 + x_shift, self.current_y * 20 - self.counter + y_shift))
                self.image = self.up.next()
            self.map1.move_screen(self.xloc,self.yloc)
            if self.counter==20:
                self.counter=0
                self.current_x = self.xloc
                self.current_y = self.yloc
    def check_for_collision(self, x, y):
        return self.map1.is_taken(x,y)
    def interact(self):
        for i in self.map1.objects:
            for squares in i.taken_squares: 
                if squares[0] == self.xloc:
                    if squares[1] == self.yloc +1:
                        i.interact()
                    if squares[1] == self.yloc -1:
                        i.interact()
                if squares[1] == self.yloc:
                    if squares[0] == self.xloc +1:
                        i.interact()
                    if squares[0] == self.xloc -1:
                        i.interact()
        
    
