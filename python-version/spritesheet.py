# Filename: spritesheet.py
# Author: Cavanaugh Richards
# Start Date: 04-17-2016

'''Edit by David Snider ---------------(ds)'''

'''

#--------------------CHANGELOG--------------------#
  v. 1.0 - RELEASE - (04-17-2016)
    - Initial build

#-------------------------------------------------#

'''

import pygame

class SpriteSheet():
    # Class Constructor
    def __init__(self, filename, colorKey):#------added colorKey (ds)
        # Load spritesheet from filename and convert to pygame Surface
        self.image = pygame.image.load(filename).convert()
        self.COLORKEY = colorKey
        
    # Private function which loads an invidual image from a spritesheet
    def _get_sprite(self, x, y, width, height):
        # Creates a blank image
        image = pygame.Surface([width, height]).convert()
        
        # Copies selected image from spritesheet onto blank image
        image.blit(self.image, (0, 0), (x, y, width, height))
        
        #-------------------- using new COLORKEY ----------(ds)
        # Set transparency color
        #image.set_colorkey((0, 0, 0))
        image.set_colorkey(self.COLORKEY)
        return image
    
    # Loads all images from a spritesheet using _get_sprite()
    def load_sheet(self, width, height):
        # List that will hold all of the images in the animation
        frames = []
        
        # Always go through the spritesheet starting from (0, 0)
        x = 0
        y = 0
        
        # Calculate rows and columns from image size and spritesheet size
        rows = self.image.get_height() // height
        columns = self.image.get_width() // width
        
        # For each image in the spritesheet...
        for i in range(rows):
            for i in range(columns):
                # Load an image
                image = self._get_sprite(x, y, width, height)
                
                # Append the image to animation frames
                frames.append(image)
    
                # Next column
                x += width
                
            # Next row
            y += height
            
        # Appends all of the images backwards to create a loop in the images
        # Without this the animation may not be fluent (depends on the spritesheet)
        for image in reversed(frames):
            frames.append(image)
            
    
        return frames