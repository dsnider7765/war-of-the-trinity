#wott_base_lib
#David Snider
#4/14/16
import pygame
import random
from stats import Stats
from elements import *
from tkinter import *
from create_character import *
'''This is the library of base modules for War of the Trinity'''


class Creature(pygame.sprite.Sprite):
    def __init__(self, x, y, song=None, color=[255,0,0], width=32, height=32,
                 name='Creature',txt="A creature aproaches. He doesn't \
look too happy to see you.", element=Non()):
        
 
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
        self.rect.x = x
        self.rect.y = y
        self.changeX = 0
        self.changeY = 0
        
        #player stats
        self.name = name
        self.txt = txt
        self.stats = Stats()
        self.element = element
        self.dead = False
        #print(self.stats)
        
        #for special ones*****
        self.song = song
        
    def __repr__(self):
        txt = '''
{}

HP: {}'''.format(self.name,self.stats.hp.value)
        return txt
    
    def check_player_collide(self,player):
        if self.rect.x == player.rect.x:
            if self.rect.y + 32 == player.rect.y:
                return True
            elif self.rect.y - 32 == player.rect.y:
                return True
            else:
                return False
        elif self.rect.y == player.rect.y:
            if self.rect.x + 32 == player.rect.x:
                return True
            elif self.rect.x - 32 == player.rect.x:
                return True
            else:
                return False
        else:
            pass
        

class ScienceMan(Creature):
    def check_player_collide(self,player,song):
        self.song = song
        if self.rect.x == player.rect.x:
            if self.rect.y + 32 == player.rect.y:
                root = Tk()
                app = SciCharacterCreation(root,player,self.song)
                root.mainloop()                
            elif self.rect.y - 32 == player.rect.y:
                root = Tk()
                app = SciCharacterCreation(root,player,self.song)
                root.mainloop()                
            else:
                return False
        elif self.rect.y == player.rect.y:
            if self.rect.x + 32 == player.rect.x:
                root = Tk()
                app = SciCharacterCreation(root,player,self.song)
                root.mainloop()                
            elif self.rect.x - 32 == player.rect.x:
                root = Tk()
                app = SciCharacterCreation(root,player,self.song)
                root.mainloop()                
            else:
                return False
        else:
            pass

class MutantMan(Creature):
    def check_player_collide(self,player,song):
        self.song = song
        if self.rect.x == player.rect.x:
            if self.rect.y + 32 == player.rect.y:
                root = Tk()
                app = MutCharacterCreation(root,player,self.song)
                root.mainloop()                
            elif self.rect.y - 32 == player.rect.y:
                root = Tk()
                app = MutCharacterCreation(root,player,self.song)
                root.mainloop()                
            else:
                return False
        elif self.rect.y == player.rect.y:
            if self.rect.x + 32 == player.rect.x:
                root = Tk()
                app = MutCharacterCreation(root,player,self.song)
                root.mainloop()                
            elif self.rect.x - 32 == player.rect.x:
                root = Tk()
                app = MutCharacterCreation(root,player,self.song)
                root.mainloop()                
            else:
                return False
        else:
            pass

class MagicMan(Creature):
    def check_player_collide(self,player,song):
        self.song = song
        if self.rect.x == player.rect.x:
            if self.rect.y + 32 == player.rect.y:
                root = Tk()
                app = MagCharacterCreation(root,player,self.song)
                root.mainloop()                
            elif self.rect.y - 32 == player.rect.y:
                root = Tk()
                app = MagCharacterCreation(root,player,self.song)
                root.mainloop()                
            else:
                return False
        elif self.rect.y == player.rect.y:
            if self.rect.x + 32 == player.rect.x:
                root = Tk()
                app = MagCharacterCreation(root,player,self.song)
                root.mainloop()                
            elif self.rect.x - 32 == player.rect.x:
                root = Tk()
                app = MagCharacterCreation(root,player,self.song)
                root.mainloop()                
            else:
                return False
        else:
            pass
        
class Loadout(object):
    def __init__(self,name='',statList=[],description='A choice of loadout'):
        self.name = name
        self.statList = statList
        self.description = description
        
    def get(self):
        out = [self.name,self.statList,self.description]
        return out

# Base class for containing all loadouts for a faction
class LoadList(object):
    def __init__(self,loadouts=[]):
        self.loadouts = loadouts
        
    def get(self):
        return self.loadouts
        

# _________________________SCIENCE LOADOUTS_______________________
class X10Cannon(Loadout):
    def __init__(self):
        super(X10Cannon,self).__init__(name='X-10: Cannon',
                                       statList=[25,5,1,3,3,1,0,0,5,17],
                                       description='The X-10: Cannon is a heavy\
-hitter loadout. The Institute will deck you out with all kinds of weapons. \
From rocket launchers to machine guns to lasers to, of course, a large arm-\
mounted cannon, the X-10 gets it all.')
        
        
class ZX12Observer(Loadout):
    def __init__(self):
        super(ZX12Observer,self).__init__(name='ZX-12: Observer',
                                          statList=[22,1,2,5,6,6,1,2,5,15],
                                          description="The ZX-12: Observer is \
a knowledge-based loadout. The Institute will replace your brain with a super \
computer with 200x the processing speed. You will be able to assess and analyze\
 any situation's threat level as well as almost anything else about a person or\
 creature you encounter. Using all the data you collect, you may even gain the \
ability to know exactly what to do for the exact outcome you so desire.")
        
    
class ModelY(Loadout):
    def __init__(self):
        super(ModelY,self).__init__(name='Model Y: Changer',
                                    statList=[22,2,2,4,3,2,4,4,2,16],
                                    description="The Model Y: Changer is a \
peculiar loadout. The Institute has designed a way to allow the body to change \
shape. The only problem: many people forget what their true form really is and \
often lose themselves in madness trying to rediscover it.")
        
        
class Model0(Loadout):
    def __init__(self):
        super(Model0,self).__init__(name='Model 0: Prototype',
                                    statList=[20,4,4,1,3,1,2,1,1,16],
                                    description="The Institute's first \
"+'"complete" '+"cyborg model. It is easily the most powerful model... at times\
. Other times... Well, let's just say it's not so great. Using this model, one\
 must depend on luck. Every ability is a big gamble. You could decimate your \
enemy with one blow... or lose an arm. Let fate decide.")
        
class SciLoadList(LoadList):
    def __init__(self):
        super(SciLoadList,self).__init__(loadouts=[X10Cannon(),ZX12Observer(),
                                                   ModelY(),Model0()])
        
        
#_______________________________MUTANT LOADOUTS_________________________
class Hulking(Loadout):
    def __init__(self):
        super(Hulking,self).__init__(name='Colossal/Hulking Body',
                                     statList=[28,5,2,5,1,2,2,4,5,13],
                                     description="Through the use of their \
mutagen, shackles, torture, and brute force, the Army of the Republic will \
force your body into a state where it will enlarge itself to survive, providing\
 great strength and superior size. This new form typically does not send many \
into madness, but some still cannot survive the process without losing sanity.")
        
class Stretched(Loadout):
    def __init__(self):
        super(Stretched,self).__init__(name='Long/Stretched Body',
                                       statList=[18,3,5,4,2,3,4,4,5,12],
                                       description="While exposing you to their\
 mutagen, the Army of the Republic places everything you need to survive out of\
 reach. This forces your body to stretch to adapt. Doing so grants you great \
dexterity and endurance. Looking more human than the rest, many find these \
stretched people to be much more aproachable than most other mutants.")
        
class Amorphous(Loadout):
    def __init__(self):
        super(Amorphous,self).__init__(name='Amorphous Body',
                                       statList=[15,5,6,6,3,4,5,6,3,11],
                                       description="No one really knows how the\
 Army does this one; none can recall what happens during their adaptation \
procedure. One thing for sure is, you will never be the same... literally. \
Once you've undergone the process, you will have the ability to change into \
whatever form you wish. Be a dog, a cat, a cyborg, a seer, even a rock if you \
so choose. Whatever you do morph into, you will gain the statistics of. \
Just don't forget your true form or you may lose yourself to insanity.")
        
class Lycanthropic(Loadout):
    def __init__(self):
        super(Lycanthropic,self).__init__(name='Lycanthropic Body',
                                          statList=[25,6,5,6,1,2,1,1,2,11],
                                          description="So you've seen the \
mutation chambers right? Those things are filled with the Army's mutagen. \
For this mutation, they shove you in one of those along with a soup of animal \
DNA. All of that will fuse into you leaving you in this semi-human state. \
Unlike the other mutation options, this one can easily send you spiraling \
into madness; turning you feral. While being feral does offer a strength bonus,\
 you will find it harder to get along with people than it already was.")
        
class MutLoadList(LoadList):
    def __init__(self):
        super(MutLoadList,self).__init__(loadouts=[Hulking(),Stretched(),
                                                      Amorphous(),
                                                      Lycanthropic()])
#___________________________MAGIC LOADOUTS_________________________
class Seer(Loadout):
    def __init__(self):
        super(Seer,self).__init__(name='Seer',
                                  statList=[15,2,3,7,4,5,2,2,3,10],
                                  description="This is the most common path \
chosen by those in the Arcane Legion. It gives the user the ability to see the \
future as well as into the minds of others. As one grows stronger in this path,\
 the user can learn to control the minds it enters. It does, however, have very\
 strange effects on the human body. It causes the user to lose the eyes on his \
head, and grow them on his hands. While this makes things strange physically, \
the user does not, in fact use them to see, but rather to channel his power. A \
seer uses his mind to see.")
        
class ArcaneSpirit(Loadout):
    def __init__(self):
        super(ArcaneSpirit,self).__init__(name='Arcane Spirit',
                                          statList=[17,1,5,7,4,4,1,1,4,17],
                                          description="This path is different \
from anything else. The magic used overtakes one's body so much that the user \
becomes an apparition--becomes magic itself. Able to pass like ghosts or \
cause fear like a wraith, an Arcane Spirit could be anywhere, and no one would \
know unless he wanted you to.")
        
class Kineticist(Loadout):
    def __init__(self):
        super(Kineticist,self).__init__(name='Kineticist',
                                        statList=[20,5,5,6,3,6,5,5,3,14],
                                        description="This path does not change \
the user's physical form, but it does cause some very strange happenings. The \
user's muscles lose the ability to hold anything more than the user's body. \
The strength is transferred into usable energy for the user's mind, granting \
telekinesis.")
        
class Radical(Loadout):
    def __init__(self):
        super(Radical,self).__init__(name='Radical',
                                     statList=[21,5,5,4,5,2,3,7,0,13],
                                     description="Haha. Haha. Boom. What \
is this thing you call sanity? We don't need no stinkin' sanity. What is pain? \
Sounds like fun. BRING ME PAIN!!!!")
        
class MagLoadList(LoadList):
    def __init__(self):
        super(MagLoadList,self).__init__(loadouts=[Seer(),ArcaneSpirit(),
                                                     Kineticist(),Radical()])