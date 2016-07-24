#!/usr/bin/env python
#!/usr/bin/env python
'''
Coded by Sean Hughes 4/7/15
This is an adventure RPG creation game. Use the GUI and the Command Output to create, save and explore maps. Note that to go between the GUI and the
command output you have to click the command output. Click 'h' at any time to have the controls printed to the screen. Have fun!
'''
import pygame
from pygame.locals import Color, KEYUP, K_ESCAPE, K_RETURN
import spritesheet
from sprite_sheet_anim import SpriteStripAnim
import sys
from Display import Display
import Player
from Map import maps, background
from objects import Tree
from editor import editor_handler
from Text import text_box
#------------------------------------------
#pygame is initialized and the display is set up
pygame.init()
display = Display()
font = pygame.font.Font(None, 25)
# Set the title of the window
pygame.display.set_caption('Guessng Game 1-10')
#--------------------------------------
'''here I define the objects and functions'''
#calls map1.draw()
def draw_items():   
    map1.draw()
#moves the player based on key inputs
def handle_movement():
    global move_right, move_left, move_up, move_down
    if (player.current_x == player.xloc and player.current_y == player.yloc):
        if move_right == True:
            player.move(1,0)
        if move_up == True:
            player.move(0,-1)
        if move_down == True:
            player.move(0,1)
        if move_left == True:
            player.move(-1,0)

#----------------------------------
#the variables and classes are initialized
map1 = maps(display)
editor_handler1 = editor_handler(map1)
editor_handler1.current_editor.help()
text_box1 = text_box(display)
player = Player.Player(20,20, display, map1)
map1.horizontal_shift = -200
map1.vertical_shift = -200
done = False
clock = pygame.time.Clock()
move_up = False
move_down = False
move_left = False
move_right = False
moving = False
#-------------------------------------
''' MAIN LOOP '''
#this is where all of the action happens while the game is being played
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            #CODE FOR MAP CREATOR
            temp = pygame.mouse.get_pos()
            temp = [temp[0], temp[1]]
            temp[0] = (temp[0] - map1.horizontal_shift)/20
            temp[1] = (temp[1] - map1.vertical_shift)/20
            editor_handler1.current_editor.add(temp[0],temp[1])
        if event.type == pygame.KEYDOWN:
            if (player.current_x == player.xloc and player.current_y == player.yloc):
                if event.key == pygame.K_LEFT:
                    move_left = True
                if event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_UP:
                    move_up = True
                elif event.key == pygame.K_DOWN:
                    move_down = True
                if event.key == pygame.K_c:
                    if editor_handler1.current_editor.editor_type > 0:
                        editor_handler1.current_editor.editor_type -=1
                if event.key == pygame.K_v:
                    if editor_handler1.current_editor.editor_type < editor_handler1.current_editor.number_of_types - 1:
                        editor_handler1.current_editor.editor_type +=1
                if event.key == pygame.K_s:
                    #CODE FOR MAP CREATOR
                    editor_handler1.current_editor.finish()
                if event.key == pygame.K_g:
                    #CODE FOR MAP CREATOR
                    if editor_handler1.current_editor.group == True:
                        editor_handler1.current_editor.group = False
                        print 'group mode OFF'
                    else:
                        editor_handler1.current_editor.group = True
                        print 'group mode ON'
                if event.key == pygame.K_h:
                    #CODE FOR MAP CREATOR
                    editor_handler1.current_editor.help()
                if event.key == pygame.K_l:
                    #CODE FOR MAP CREATOR
                    editor_handler1.switch_editor()
                if event.key == pygame.K_SPACE:
                    player.interact()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_UP:
                move_up = False
            elif event.key == pygame.K_DOWN:
                move_down = False
    handle_movement()
    draw_items()
    #text_box1.draw()
    pygame.display.flip()
    clock.tick(60)

