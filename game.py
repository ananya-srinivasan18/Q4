
OLD VERSION - WITHOUT UPDATES TO CODE




# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:16:01 2024

@author: asrinivasan26
"""

from tkinter import *
import random
import time

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Forest Adventures")
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
        self.bg = PhotoImage(file="background.gif")
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
        #self.testx = 0

    def mainloop(self):
        while 1:
            #while the game is running, if the sprite is also running, then trigger the functions
            if self.running:
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
        self.width = width
        self.height = height
        self.game = game
    #def update_position(self, x,y):
       # test.x = 0
        #self.coordinates = Coords(x,y, x+self.width, y+self.height)
       # self.sprites[7].update_position(self.testx,60)# Move a platform!
       # self.image = self. game.canvas.create_image(x, y, image=self.photo_image, anchor = 'nw') #print photo (of platform)
       

class StickFigureSprite(Sprite):
    def __init__(self, game):
        Sprite.__init__(self, game) #no additional parameters because there's only one sprite
        #loads three left images and three right images:
        self.images_left = [
            PhotoImage(file = 'l1.png'),
            PhotoImage(file = 'l2.png'),
            PhotoImage(file = 'output-onlinepngtools (3).png')
        ]
        self.images_right = [
            PhotoImage(file = 'r1 (1).gif'),
            PhotoImage(file = 'r2.png'),
            PhotoImage(file = 'r3.png')
        ]
        #loads left images
        self.image = game.canvas.create_image(200,470, image = self.images_left[0], anchor='nw')
        self.x = -2 #subtract 2 from the x coordinate: character moves left
        self.y = 0 #not changing y value so that character only moves left
        self.current_image = 0 #stores character's current position
        self.current_image_add = 1 #number we add to position (used to update the self.current_image)
        self.jump_count = 0
        self.last_time = time.time() #stores current time
        self.coordinates = Coords() #sets to object of coords class, no set coordinates since it changes
        #BINDING THE KEYS:
        game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        game.canvas.bind_all('<space>', self.jump)
        game.canvas.bind_all('<KeyPress-Up>', self.jump) #added by me
   
    def turn_left(self, evt): #when the left arrow key is pressed (see above: key binding):
        #NOTE: evt isn't really important but python expects that parameter to  be there so if it's not it'll come out as error
        #evt means event, which is like "what occured to trigger this". However, we only call on the function when the certain /
        #key is pressed so it doesn't really matter.
        if self.y == 0:
            self.x = -2
   
    def turn_right(self, evt): #when the right arrow key is pressed (see above: key binding):
        if self.y == 0:
            self.x = 2
   
    def jump(self, evt):
        if self.y == 0: #character can only jump if it's not already jumping
            self.y = -4 #moves char vertically UP the screen
            self.jump_count = 0
   
    def animate(self):
        if self.x != 0 and self.y == 0: #is char moving but not jumping? if so, animate. otherwise there's no need (since he's standing still)
        #if char not moving, the rest of this def won't occur.
            if time.time() - self.last_time > 0.1: #is the amount of time since the animate function was last called enough to continue animating?
                self.last_time = time.time() #resets time to add next image
                self.current_image += self.current_image_add #adds variables
                if self.current_image >= 2:
                    self.current_image_add = -1 #so it goes from image 0 to image 1 to image 2 then back to image 1 etc
                if self.current_image <= 0: #so it goes from image 2 to image 1 to image 0 then back to image 1
                    self.current_image_add = 1
        if self.x < 0: #if x is less than 0, char is moving left
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, image = self.images_left[2])#if y isn't 0, it's jumping- so use image of char jumping(long stride)
            else:
                self.game.canvas.itemconfig(self.image, image = self.images_left[self.current_image])#not jumping(y=0)displays index of variable(next line)
                # current image's position
        elif self.x > 0: #same as code for left
                if self.y != 0:
                    self.game.canvas.itemconfig(self.image, image = self.images_right[2])
                else:
                    self.game.canvas.itemconfig(self.image, image = self.images_right[self.current_image])
               
    def coords(self): #returns coordinates of char since it's always moving around
        xy = self.game.canvas.coords(self.image)  #stores coordinates
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + 27 #27 px wide
        self.coordinates.y2 = xy[1] + 30 #30 px tall
        return self.coordinates
   
# ***** IMPORTANT: if x > 0 , char moving right. If x < 0, char moving left. If y > 0, char falling. If y < 0, char moving up (jumping)

    def move(self):
        self.animate()
        if self.y < 0: #negative y value = going up = jumping
            self.jump_count += 1
            if self.jump_count > 20:
                self.y = 4 #so that the char starts falling again
        if self.y > 0: #positive y value = going down = character is falling
            self.jump_count -= 1 #need to count back after counting to 20
        co = self.coords()
        left = True
        right = True
        top = True
        bottom = True
        falling = True
        #indicators to check whether char is hitting smth or falling (above)
        if self.y > 0 and co.y2 >= self.game.canvas_height: #make sure that although it's falling it doesn't hit bottom otherwise it would vanish offscreen
            self.y = 0 #sets y to 0 to stop char from falling when hits bottom
            bottom = False
        elif self.y < 0  and co.y1 <= 0:
            self.y = 0
            top = False #top = false means char has hit the top
        #check if hitting left/right of canvas
        if self.x > 0 and co.x2 >= self.game.canvas_width: #hitting right?
            self.x = 0
            right = False
        elif self.x < 0 and co.x1 <= 0: #hitting left?
            self.x = 0
            left = False
        #check if hitting other sprite
        for sprite in self.game.sprites: #for each sprite:
            if sprite == self: #if sprite is same as me (meaning we don't have to check for collisions; sprite only hit himself):
                continue#move onto next sprite
            sprite_co = sprite.coords() #gets coordinates of sprite and storing it
            if top and self.y < 0 and collided_top(co, sprite_co): #if char hasn't hit top (top = True) and figure is still jumping (y<0) and top of
            # / char has collided with sprite:
                self.y = -self.y #sprite has to fall down
                top = False #once char has hit the top no need to check for collisions with sprite again
            if bottom and self.y > 0 and collided_bottom(self.y, co, sprite_co): #if char is falling (y>0) and char is touching bottom:
                self.y = sprite_co.y1 - co.y2 #how much char should drop to meet platform and make sure it doesn't stop above or below
                if self.y < 0:
                    self.y = 0 #make sure calculation isn't a negative number, otherwise it would disappear; set y = 0 if that's true
                bottom = False
                top = False #no longer need to check if stick figure has collided top or bottom
            if bottom and falling and self.y == 0 and co.y2 < self.game.canvas_height and collided_bottom (1, co, sprite_co):
                falling = False #if all of these are true, char is NOT falling so set falling to false
            if left and self.x < 0 and collided_left(co, sprite_co): #Should we be looking for collisions? and is char moving left? and did the char
            # / collide with another sprite?
                self.x = 0 #char stops running
                left = False #stop checking for collisions on left
               # if self.endgame:
                    #self.game.running = False
            if right and self.x > 0 and collided_right(co, sprite_co): #same thing as left
                self.x = 0
                right = False
                
                    # reset position of character
                   
        ### JED EDIT
        # Check specifically for collision with door
        door = self.game.sprites[10]
        door_x = door.coordinates.x1
        door_y = door.coordinates.y1
        door_distance_squared = (door_x-self.coordinates.x1)*(door_x-self.coordinates.x1) + (door_y-self.coordinates.y1)*(door_y-self.coordinates.y1)
        #print(door_distance)
        if door_distance_squared < 400:
            # If this is true, we reached the door
            self.endgame = True
            print("You won!")
            self.coordinates.x1 = 198
            self.coordinates.y1 = 390
           
            self.game.canvas.move(self.image, 120, 360)
            
            self.game.canvas.move(self.game.sprites[0].image, 100, -20)
            self.game.sprites[0].coordinates.x1 = 100
            self.game.sprites[0].coordinates.y1 = 460
            self.game.running = True
           
            #self.move(self.coordinates.x1, self.coordinates.y1)
           
                   
        if falling and bottom and self.y == 0 and co.y2 < self.game.canvas_height: #if falling and bottom are both true, then we've looped through /
        # evey sprite on the liste without colliding at bottom. Final check: is bottom less than canvas height (above the ground)? That means he needs  /
        # to start falling since he's standing in midair AND the previous things already establish he's not touching a platform sprite
            self.y = 4 #starts falling
        self.game.canvas.move(self.image, self.x, self.y)
class DoorSprite(Sprite):
    def __init__(self,game,photo_image,x,y,width,height):
        Sprite.__init__(self,game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image = self.photo_image, anchor = 'nw')
        self.coordinates = Coords(x, y, x + (width/2), y + height) #sets x and y positions and calculates x2 and y2 positions. it's also width/2 since
        # / we want char to stop running in FRONT of the door (when it hits x2, which will be at half of the door's width)
        self.endgame = True #when stickman reaches door, game ends
       
       

   
           

g = Game()
#calling on the image of the platform and positioning them
platform1 = PlatformSprite(g, PhotoImage(file = 'P1_FINAL-removebg-preview.gif'), 0, 480, 100, 10)
platform2 = PlatformSprite(g, PhotoImage(file = 'P1_FINAL-removebg-preview.gif'), 150, 440, 100, 10)
platform3 = PlatformSprite(g, PhotoImage(file = 'P1_FINAL-removebg-preview.gif'), 300, 400, 100, 10)
platform4 = PlatformSprite(g, PhotoImage(file = 'P1_FINAL-removebg-preview.gif'), 300, 160, 100, 10)
platform5 = PlatformSprite(g, PhotoImage(file = 'P2_FINAL-removebg-preview.gif'), 175, 350, 66, 10)
platform6 = PlatformSprite(g, PhotoImage(file = 'P2_FINAL-removebg-preview.gif'), 50, 300, 66, 10)
platform7 = PlatformSprite(g, PhotoImage(file = 'P2_FINAL-removebg-preview.gif'), 170, 120, 66, 10)
platform8 = PlatformSprite(g, PhotoImage(file = 'P2_FINAL-removebg-preview.gif'), 45, 60, 66, 10)   # 45, 60, 66, 10
platform9 = PlatformSprite(g, PhotoImage(file = 'P3_FINAL-removebg-preview.gif'), 170, 250, 32, 10)
platform10 = PlatformSprite(g, PhotoImage(file = 'P3_FINAL-removebg-preview.gif'), 230, 200, 32, 10)
#putting them in Sprites category
g.sprites.append(platform1)  # 0
g.sprites.append(platform2)  # 1
g.sprites.append(platform3)  # 2
g.sprites.append(platform4)  # 3
g.sprites.append(platform5)  # 4
g.sprites.append(platform6)  # 5
g.sprites.append(platform7)  # 6
g.sprites.append(platform8)  # 7
g.sprites.append(platform9)  # 8
g.sprites.append(platform10) # 9
#g.sprites[7].x = 200
door = DoorSprite(g, PhotoImage(file = 'Doorclosed-removebg-preview.gif'), 45, 30, 40, 35)
g.sprites.append(door)
sf = StickFigureSprite(g)
g.sprites.append(sf)
g.mainloop()

if self.endgame:
    platform2.x = 200
