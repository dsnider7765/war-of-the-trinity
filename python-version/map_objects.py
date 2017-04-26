#map_objects
#David Snider
#4/21/16


import pygame


class MapObject(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('map.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        

        
    
        