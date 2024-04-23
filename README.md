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
        self.tk.resizable (0,0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width = 500, height = 500, highlightthickness= 0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 500
        self.canvas_width = 500
        self.bg = PhotoImage(file="background.gif")
        w = self.bg.width()
        h = self.bg.height()
        for x in range (0,5):
            for y in range (0,5):
                self.canvas.create_image(x*w, y*h, image=self.bg, anchor = 'nw')
        self.sprites = []
        self.running = True

game = Game()
