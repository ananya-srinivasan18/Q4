# Q4
Quarter 4 Project

#GAME

#Week 1:
- pg 235

#Week 2:
- Get up to page 250 (background mechanics)

#Week 3:
- 258 (animate char)

#Week 4:
- 272

#Week 5:
- 282

#Week 6+7:
- Final touches, adding more levels if time

CODE

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

#Are the sprites (sprites' starting and ending coordinates) crossing each other? (Are the two sprites overlapping or bumping into each other)
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

            
g = Game()
g.mainloop()
