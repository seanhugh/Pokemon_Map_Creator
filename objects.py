#!/usr/bin/env python
'''THIS IS THE OBJECT CLASS. All of the code for the different classes of objects is stored here.'''
import spritesheet
from sprite_sheet_anim import SpriteStripAnim
#class for tree objects trees. tree_type refers to image and size. Can be 0-2. the xloc and yloc are the locations on the map, and map1
#and display refer to the map and display it is printed on
class Tree(object):   
    def __init__(self, tree_type, xloc, yloc,map1, display):

        self.tree0 = SpriteStripAnim('images/trees.gif', (80,60,36,60), 1, (0,0,0), True, 1)
        self.tree0 = self.tree0.next()
        self.tree1 = SpriteStripAnim('images/trees.gif', (0,80,18,40), 1, (0,0,0), True, 1)
        self.tree1 = self.tree1.next()
        self.tree2 = SpriteStripAnim('images/trees.gif', (96,0,48,60), 1, (0,0,0), True, 1)
        self.tree2 = self.tree2.next()
        self.type = tree_type
        self.xloc = xloc
        self.yloc = yloc
        self.display = display
        self.map1=map1
        self.adjust_positionx = 0
        self.adjust_positiony = 0
        map1.objects.append(self)
        if tree_type == 0:
            self.image = self.tree0
            self.taken_squares = [[xloc,yloc+1], [xloc+1,yloc+1]]
            self.adjust_positionx = 3
            self.adjust_positiony = 7
        if tree_type == 1:
            self.image = self.tree1
            self.taken_squares = [[xloc,yloc]]
            self.adjust_positionx = 1
            self.adjust_positiony = 3
        elif tree_type == 2:
            self.image = self.tree2
            self.taken_squares = [[xloc +1 ,yloc +1], [xloc ,yloc +1]]
        
    def draw(self, x_shift, y_shift):
        x_shift = x_shift
        y_shift = y_shift
        self.display.paint(self.image, (self.xloc*20 + x_shift + self.adjust_positionx, self.yloc*20 + y_shift + self.adjust_positiony))
    def change_type(self):
        self.map1.objects.remove(self)
        if self.type == 2:
            self.type = 1
            self.image = self.tree1
            self.taken_squares = [[self.xloc,self.yloc]]
        if self.type == 1:
            self.type == 2
            self.image = self.tree2
            self.taken_squares = [[self.xloc +1 ,self.yloc +1], [self.xloc ,self.yloc +1]]
        self.map1.objects.append(self)
    def object_code(self):
        return "Tree(%i,%i,%i,map1, map1.display)" % (self.type ,self.xloc,self.yloc)
    def interact(self):
        print "im a tree"

#class for water objects Water. object_type refers to image and size. Can be 0-8. the xloc and yloc are the locations on the map, and map1
#and display refer to the map and display it is printed on
class Water(object):   
    def __init__(self, object_type, xloc, yloc,map1, display):

        self.type0 = SpriteStripAnim('images/pond.png', (0,0,20,20), 1, (0,0,0), True, 1)
        self.type0 = self.type0.next()
        self.type1 = SpriteStripAnim('images/pond.png', (20,0,20,20), 1, (0,0,0), True, 1)
        self.type1 = self.type1.next()
        self.type2 = SpriteStripAnim('images/pond.png', (40,0,20,20), 1, (0,0,0), True, 1)
        self.type2 = self.type2.next()
        self.type3 = SpriteStripAnim('images/pond.png', (60,0,20,20), 1, (0,0,0), True, 1)
        self.type3 = self.type3.next()
        self.type4 = SpriteStripAnim('images/pond.png', (80,0,20,20), 1, (0,0,0), True, 1)
        self.type4 = self.type4.next()
        self.type5 = SpriteStripAnim('images/pond.png', (100,0,20,20), 1, (0,0,0), True, 1)
        self.type5 = self.type5.next()
        self.type6 = SpriteStripAnim('images/pond.png', (120,0,20,20), 1, (0,0,0), True, 1)
        self.type6 = self.type6.next()
        self.type7 = SpriteStripAnim('images/pond.png', (140,0,20,20), 1, (0,0,0), True, 1)
        self.type7 = self.type7.next()
        self.type8 = SpriteStripAnim('images/pond.png', (160,0,20,20), 1, (0,0,0), True, 1)
        self.type8 = self.type8.next()
        self.type = object_type
        self.xloc = xloc
        self.yloc = yloc
        self.display = display
        self.map1=map1
        map1.objects.append(self)
        if self.type == 0:
            self.image = self.type0
            self.taken_squares = [[xloc,yloc]]
        if self.type == 1:
            self.image = self.type1
            self.taken_squares = [[xloc,yloc]]
        elif self.type == 2:
            self.image = self.type2
            self.taken_squares = [[xloc,yloc]]
        elif self.type == 3:
            self.image = self.type3
            self.taken_squares = [[xloc,yloc]]
        elif self.type == 4:
            self.image = self.type4
            self.taken_squares = [[xloc,yloc]]
        elif self.type == 5:
            self.image = self.type5
            self.taken_squares = [[xloc,yloc]]
        elif self.type == 6:
            self.image = self.type6
            self.taken_squares = [[xloc,yloc]]
        elif self.type == 7:
            self.image = self.type7
            self.taken_squares = [[xloc,yloc]]
        elif self.type == 8:
            self.image = self.type8
            self.taken_squares = [[xloc,yloc]] 
    def draw(self, x_shift, y_shift):
        x_shift = x_shift
        y_shift = y_shift
        self.display.paint(self.image, (self.xloc*20 + x_shift, self.yloc*20 + y_shift + 20))
    def change_type(self):
        self.map1.objects.remove(self)
        if self.type == 2:
            self.type = 1
            self.image = self.tree1
            self.taken_squares = [[self.xloc,self.yloc]]
        if self.type == 1:
            self.type == 2
            self.image = self.tree2
            self.taken_squares = [[self.xloc +1 ,self.yloc +1], [self.xloc ,self.yloc +1]]
        self.map1.objects.append(self)
    def object_code(self):
        return "Water(%i,%i,%i,map1, map1.display)" % (self.type ,self.xloc,self.yloc)
    def interact(self):
        print "would u like to swim doe?"
#class for text objects Text. object_type refers to image and size. Must be 0. the xloc and yloc are the locations on the map, and map1
#and display refer to the map and display it is printed on. Text refers to the sign text. It can be None, which will then prompt the user
#to fill in the text, or it can be a string, which will then be read when the user interacts with the sign.
class Sign(object):   
    def __init__(self, object_type, xloc, yloc,map1, display, text):
        self.object0 = SpriteStripAnim('images/parts.gif', (30,160,20,16), 1, (0,0,0), True, 1)
        self.object0 = self.object0.next()
        self.type = object_type
        self.xloc = xloc
        self.yloc = yloc
        self.display = display
        self.map1=map1
        self.adjust_positionx = 0
        self.adjust_positiony = 0
        self.text = text
        map1.objects.append(self)
        if object_type == 0:
            self.image = self.object0
            self.taken_squares = [[xloc,yloc]]
            self.adjust_positionx = 0
            self.adjust_positiony = 20
    def draw(self, x_shift, y_shift):
        x_shift = x_shift
        y_shift = y_shift
        self.display.paint(self.image, (self.xloc*20 + x_shift + self.adjust_positionx, self.yloc*20 + y_shift + self.adjust_positiony))
    '''def change_type(self):
        self.map1.objects.remove(self)
        if self.type == 2:
            self.type = 1
            self.image = self.tree1
            self.taken_squares = [[self.xloc,self.yloc]]
        if self.type == 1:
            self.type == 2
            self.image = self.tree2
            self.taken_squares = [[self.xloc +1 ,self.yloc +1], [self.xloc ,self.yloc +1]]
        self.map1.objects.append(self)'''
    def object_code(self):
        if self.text != None:
            text_temp = "'" + self.text + "'"
        temp = "Sign(%i,%i,%i,map1, map1.display, %s)" % (self.type ,self.xloc,self.yloc, text_temp)
        return temp 
    def interact(self):
        if self.text != None:
            print "The sign has writing on it......"
            print "it says " + "'" + self.text + "'"
        else:
            print "what would you like the sign to say?"
            self.text = raw_input()
            print "sign created!"
