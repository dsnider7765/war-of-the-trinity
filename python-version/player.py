#player
#David Snider
#4/18/16

import pygame
import random
from stats import Stats
from spritesheet import *
import save_game as sg
from elements import *

class Player(pygame.sprite.Sprite):
    
 
    def __init__(self, color=[255,255,0], width=32, height=32, element=Non()):
        
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        '''self.spriteSheet = SpriteSheet('cyborg assassin(scaled).png'
                                       ,(0,255,255))
        self.frames = self.spriteSheet.load_sheet(32,32)
        
        self.image = self.frames[0]'''
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.changeX = 0
        self.changeY = 0
        
        self.directionX = "R"
        self.directionY = "D"
        
        #player stats
        self.name = 'Player'
        self.stats = Stats()
        self.element = element
        
        #save
        self.saveGame = sg.SaveGame(self)
        
        self.load()
        
        
    def change_speed(self, x, y):
        """ Change the speed of the player"""
        self.changeX += x
        self.changeY += y
 
    def check_collide_x(self,spriteList):
        for i in spriteList:
            if i.rect.y == self.rect.y:
                if self.directionX == "L":
                    if i.rect.x + 32 == self.rect.x:
                        return True
                    else:
                        out = False
                if self.directionX == "R":
                    if i.rect.x - 32 == self.rect.x:
                        return True
                    else:
                        out = False
            else:
                out = False
        return out
    
    def check_collide_y(self,spriteList):
            for i in spriteList:
                if i.rect.x == self.rect.x:
                    if self.directionY == "U":
                        if i.rect.y + 32 == self.rect.y:
                            return True
                        else:
                            out = False
                    if self.directionY == "D":
                        if i.rect.y - 32 == self.rect.y:
                            return True
                        else:
                            out = False
                else:
                    out = False
            return out 
        
    def update(self,spriteList):
        """ Find a new position for the player"""
        if not self.check_collide_x(spriteList):
            self.rect.x += self.changeX
        
        if not self.check_collide_y(spriteList):
            self.rect.y += self.changeY
            
        if self.rect.x > 3168:
            self.rect.x = 3168
                
        if self.rect.x < 0:
            self.rect.x = 0
            
        if self.rect.y > 3168:
            self.rect.y = 3168
            
        if self.rect.y < 0:
            self.rect.y = 0
        
        self.stats.x.value = self.rect.x
        self.stats.y.value = self.rect.y
        
    def save(self):
        self.saveGame.save()
        
    def load(self):
        load = self.saveGame.load()
        self.rect.x = int(load[0])
        self.rect.y = int(load[1])
        stats = self.stats
        stats.level.value = int(load[2])
        stats.exp.value = int(load[3])
        stats.hp.value = int(load[4])
        stats.strength.value = int(load[5])
        stats.dexterity.value = int(load[6])
        stats.constitution.value = int(load[7])
        stats.intelligence.value = int(load[8])
        stats.wisdom.value = int(load[9])
        stats.charisma.value = int(load[10])
        stats.comeliness.value = int(load[11])
        stats.sanity.value = int(load[12])
        stats.armorClass.value = int(load[13])