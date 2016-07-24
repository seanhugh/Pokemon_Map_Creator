#!/usr/bin/env python
import Map
from objects import Tree, Water, Sign
'''this function loads saved maps from file and creates them on the screen'''
def create(map1, background):
    current_save = "map_" + str(background)
    map1.objects = []
    f = open('maps/%s.txt' %(current_save), 'r')
    temp = f.read()
    eval(temp)
