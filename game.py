# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:11:47 2024

@author: asrinivasan26
"""

from tkinter import *
import random
import time

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Forest Run")
        #can't resize window:
        self.tk.resizable (0,0)
        #Sets window to be the topmost window:
        self.tk.wm_attributes("-topmost", 1)
        #Sets canvas dimensions:
        self.canvas = Canvas(self.tk, width = 500, height = 500, highlightthickness= 0)
        self.canvas.pack()
        self.tk.update()
        #sets canvas dimensions (variables)
        self.canvas_height = 500
        self.canvas_width = 500
        #uploads photo
        self.bg = PhotoImage(file="Untitled_Artwork (1) (1).gif")
        #syncs them
        w = self.bg.width()
        h = self.bg.height()
        #prints the image for every 5x5 square
        for x in range (0,5):
            for y in range (0,5):
                self.canvas.create_image(x*w, y*h, image=self.bg, anchor = 'nw')
        #sets the variables (useful later)
        self.sprites = []
        self.running = True

    def mainloop(self):
        while 1:
            #while the game is running, if the sprite is also running, then trigger the functions
            if self.running == True:
                for sprite in self.sprites:
                    sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)
#Sets the positions (x1,y1,x2,y2)
class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
#COLLISION DETECTION CODE:
#Are the sprites (sprites' starting and ending x coordinates) HORIZONTALLY crossing each other? (Are the two sprites overlapping/bumping horizontally)
def within_x(co1, co2):
        #To check if x1 of co1 is in between both of the coordinates of the second (co2)
        if co1.x1 > co2.x1 and co1.x1 < co2.x2:
            #returns true if they are bumping into each other (same for other stuff)
            return True
        #To check if the x2 coordinate of co1 is in between the x1 and x2 of co2
        elif co1.x2 > co2.x1 and co1.x2 < co2.x2:
            return True
        #To check if x1 of co2 is in between the x1 and x2 of co1
        elif co2.x1 > co1.x1 and co2.x1 < co1.x2:
            return True
        #To check if the x2 of co2 is in between the x1 and x2 of co1
        elif co2.x2 > co1.x1 and co2.x2 < co1.x2:
            return True
        else:
            #Saying that the two sets of coordinates (two sprites) do NOT cross each other
            return False
#Are the sprites (sprites' starting/ending y coordinates) VERTICALLY crossing each other? (Are the two sprites overlapping/bumping vertically)
def within_y(co1,co2):
        if co1.y1 > co2.y1 and co1.y1 < co2.y2:
            #returns true if they are bumping into each other (same for other stuff)
            return True
        #To check if the y2 coordinate of co1 is in between the y1 and y2 of co2
        elif co1.y2 > co2.y1 and co1.y2 < co2.y2:
            return True
        #To check if y1 of co2 is in between the y1 and y2 of co1
        elif co2.y1 > co1.y1 and co2.y1 < co1.y2:
            return True
        #To check if the y2 of co2 is in between the y1 and y2 of co1
        elif co2.y2 > co1.y1 and co2.y2 < co1.y2:
            return True
        else:
            #Saying that the two sets of coordinates (two sprites) do NOT cross each other
            return False
    #figure out what side the sprite hits
def collided_left(co1, co2): #does it hit on left side of first sprite (character)?
        if within_y(co1, co2):#this line checks if its within the y of the sprite, since if its way above/below it there's no point it's not touching
            if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:#checks if it's touching or overlapping with platform's right side (char's left)
                return True
        return False
def collided_right(co1, co2):
        if within_y(co1, co2):
            if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
                return True
        return False
def collided_top(co1, co2):
        if within_x(co1, co2): #only applicable if it's within x value that the platform is (no point if it's way left/right of platform and not touching)
            if co1.y1 <= co2.y2 and co1.y1 >= co2.y1: #if the char's top coordinate is below top of platform but above bottom (hitting platform)
                return True
        return False
def collided_bottom(y, co1, co2): #y: height of platform - STUDY THIS PART MORE *****************************
        if within_x(co1, co2):#only applicable if it's within x value that the platform is (no point if it's way left/right of platform and not touching)
            y_calc = co1.y2 + y  #add height of platform to bottom y coordinate of character to make sure that char is able to fall off platform instead
            #of standing in midair. So, we need to check below him to see if he's colliding with the platform or not
            if y_calc >= co2.y1 and y_calc <= co2.y2:
                return True
        return False

class Sprite:
    def __init__(self, game):#sprites will be able to access list of other sprites
        self.game = game #store game parameter as object (variable)
        self.endgame = False #used to indicate end of game (currently false because the game isn't over)
        self.coordinates = None 
    def move(self):
        pass
    def coords(self):
        return self.coordinates #returns object's coordinates
    #these loop back to the main function since all classes with parent Sprite have move and coords functions
class PlatformSprite(Sprite): #sets the platform sprite up to have access to all the function commands like game and endgame
    def __init__ (self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image #save photo as variable
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor = 'nw') #print photo (of platform)
        self.coordinates = Coords(x, y, x + width, y + height) #contains location of platform

class StickFigureSprite(Sprite):
    def __init__(self, game):
        Sprite.__init__(self, game) #no additional parameters because there's only one sprite
        #loads three left images and three right images:
        #** COME BACK TO THIS PART:            self.images_left = 

g = Game()
#calling on the image of the platform and positioning them
platform1 = PlatformSprite(g, PhotoImage(file = 'P1_FINAL-removebg-preview.gif'), 0, 480, 100, 10)
platform2 = PlatformSprite(g, PhotoImage(file = 'P1_FINAL-removebg-preview.gif'), 150, 440, 100, 10)
platform3 = PlatformSprite(g, PhotoImage(file = 'P1_FINAL-removebg-preview.gif'), 300, 400, 100, 10)
platform4 = PlatformSprite(g, PhotoImage(file = 'P1_FINAL-removebg-preview.gif'), 300, 160, 100, 10)
platform5 = PlatformSprite(g, PhotoImage(file = 'P2_FINAL-removebg-preview.gif'), 175, 350, 66, 10)
platform6 = PlatformSprite(g, PhotoImage(file = 'P2_FINAL-removebg-preview.gif'), 50, 300, 66, 10)
platform7 = PlatformSprite(g, PhotoImage(file = 'P2_FINAL-removebg-preview.gif'), 170, 120, 66, 10)
platform8 = PlatformSprite(g, PhotoImage(file = 'P2_FINAL-removebg-preview.gif'), 45, 60, 66, 10)
platform9 = PlatformSprite(g, PhotoImage(file = 'P3_FINAL-removebg-preview.gif'), 170, 250, 32, 10)
platform10 = PlatformSprite(g, PhotoImage(file = 'P3_FINAL-removebg-preview.gif'), 230, 200, 32, 10)
#putting them in Sprites category
g.sprites.append(platform1)
g.sprites.append(platform2)
g.sprites.append(platform3)
g.sprites.append(platform4)
g.sprites.append(platform5)
g.sprites.append(platform6)
g.sprites.append(platform7)
g.sprites.append(platform8)
g.sprites.append(platform9)
g.sprites.append(platform10)
g.mainloop()
