import pygame
import random

class Block(pygame.sprite.Sprite):
    
 
    def __init__(self, color=[0,0,0], width=32, height=32):
        
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
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
        
    def change_speed(self, x, y):
        """ Change the speed of the player"""
        self.changeX += x
        self.changeY += y
 
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.changeX
        self.rect.y += self.changeY
        if self.rect.x > 3168:
            self.rect.x = 3168
                
        if self.rect.x < 0:
            self.rect.x = 0
            
        if self.rect.y > 3168:
            self.rect.y = 3168
            
        if self.rect.y < 0:
            self.rect.y = 0
                   