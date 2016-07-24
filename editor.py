#!/usr/bin/env python
'''
THIS IS THE EDITOR CLASS. It is modified by the child classes below it which change the specific type of object created. The editor handler class
on the bottom compiles all of the different child classes together in an easy-to-use format which allows the user to switch between
editor 'types' without changing any code.
controls:
mouse click - add/remove an object
c - lowers object type
v - increases object type
p - saves the current map
l - changes the object type
h - prints the help screen
g - toggles between a group or non group setting
'''
from objects import Tree, Water, Sign
class editor():
    edit = True
    map1 = 0
    editor_type = 0
    group = False
    def edit(self, x, y):
        if self.edit == True:
            print "yah"
    def finish(self):
        temp = "Map.create_background(%i, %i, %s, %i, %i, %i, %i, %i, map1)" % (self.map1.current_background.width, self.map1.current_background.height, str(self.map1.current_background.texture_grid), self.map1.current_background.index, self.map1.current_background.up, self.map1.current_background.right, self.map1.current_background.left, self.map1.current_background.down)
        temp += ", "
        #print self.map1.backgrounds[self.map1.current_background].texture_grid
        for i in self.map1.objects:
             temp += i.object_code()
             temp += ", "
        current_save = "map_" + str(self.map1.current_background.index)
        f = open('maps/%s.txt' %(current_save), 'w')
        f.write(temp)
        f.close()
        print current_save + ' saved'
    def check_for_object(self, x, y):
        for i in self.map1.objects:
            if i.xloc == x and i.yloc == y:
                self.map1.objects.remove(i)
                return True
        return False
    def help(self):
        print "mouse click - add/remove an object\
        c - lowers object type\
        v - increases object type\
        s - saves the current map\
        l - changes the object type\
        h - prints the help screen\
        g - toggles between a group or non-group setting"
#edits the texture
class texture_editor(editor):
    ID = "texture editor"
    help_text = "press c and v to toggle through different textures"
    number_of_types = 4
    def add(self, x, y):
        for i in self.map1.current_background.texture_grid:
            if x == i[1] and y == i[2]:
                i[0] = self.editor_type
#edits the tree objects
class tree_editor(editor):
    ID = "tree editor"
    help_text = "press c and v to toggle through different trees. Click an existing tree to remove it."
    number_of_types = 3
    def add(self, x, y):
        if self.group == False:
            if self.check_for_object(x,y) == False:
                Tree(self.editor_type,x,y,self.map1, self.map1.display)
        else:
            if self.check_for_object(x,y) == False:
                for i in range(5):
                    for j in range(5):
                        Tree(self.editor_type,x+i,y+j,self.map1, self.map1.display)
#edits the water objects
class water_editor(editor):
    ID = "Water editor"
    help_text = "press c and v to toggle through different water blocks"
    number_of_types = 9
    def add(self, x, y):
        y = y-1
        if self.check_for_object(x,y) == False:
            Water(self.editor_type,x ,y,self.map1, self.map1.display)
#edits the sign objects
class sign_editor(editor):
    ID = "Sign editor"
    help_text = "place a sign then write its text"
    number_of_types = 1
    def add(self, x, y):
        y = y-1
        if self.check_for_object(x,y) == False:
            Sign(self.editor_type,x ,y,self.map1, self.map1.display, None)
#handles all of the editors and allows for switching between them. Also handles the printing of the help screen.
class editor_handler(object):
    def __init__(self, map1):
        self.map1 = map1
        self.trees = tree_editor()
        self.water = water_editor()
        self.texture = texture_editor()
        self.sign = sign_editor()
        self.editors = [self.trees, self.water, self.texture, self.sign]
        self.current_editor = self.editors[0]
        self.current_editor.map1 = map1
        self.clicker = 0
    def switch_editor(self):
        self.clicker+=1
        if self.clicker < len(self.editors):
            pass
        else:
            self.clicker = 0
        self.current_editor = self.editors[self.clicker]
        self.current_editor.map1 = self.map1
        print self.current_editor.ID
        print self.current_editor.help_text


