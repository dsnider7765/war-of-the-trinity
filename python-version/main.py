# Main
# David Snider with help from Cavanaugh Richards
# Started on 4/13/16

import pygame
from pytmx import load_pygame
import pyscroll
import random
from player import Player
from encounter import *
import map_objects as mo
from wott_base_lib import *
import xml.etree.ElementTree as ET

pygame.init()

#color = 0

pygame.mixer.init()
theMix = pygame.mixer.Channel(1)
songNumber = 1
theSong = pygame.mixer.Sound("WhoToJoin.ogg")
theMix.play(theSong,loops=-1,fade_ms=1500)
screenSize = [800,600]
screen = pygame.display.set_mode(screenSize)
 

pygame.display.set_caption("War of the Trinity")
 
clock = pygame.time.Clock()



tmxData = load_pygame("theMap.tmx")
mapData = pyscroll.TiledMapData(tmxData)
mapSprite = pyscroll.BufferedRenderer(mapData,screenSize)

group = pyscroll.PyscrollGroup(map_layer=mapSprite)
player = Player()
spriteList = pygame.sprite.Group()
creatureList = pygame.sprite.Group()
specialList = pygame.sprite.Group()
testCreatureList = [Creature(64,64)]
for i in range(0,99):
    x = random.randint(1,99)*32
    y = random.randint(1,99)*32
    testCreature = Creature(x,y)
    testCreatureList.append(testCreature)
scienceMan = ScienceMan(640,96,theSong)
mutantMan = MutantMan(1280,160,theSong)
magicMan = MagicMan(1856,224,theSong)

group.add(player)

group.add(scienceMan)
group.add(mutantMan)
group.add(magicMan)


spriteList.add(scienceMan)
spriteList.add(mutantMan)
spriteList.add(magicMan)



specialList.add(scienceMan)
specialList.add(mutantMan)
specialList.add(magicMan)

for testCreature in testCreatureList:
    group.add(testCreature)
    spriteList.add(testCreature)
    creatureList.add(testCreature)

tree = ET.parse('theMap.tmx')
root = tree.getroot()
for i in root[-1]:
    attributes = i.attrib
    for x in range(int(attributes['x']),int(attributes['x'])+\
                   int(attributes['width']),32):
        for y in range(int(attributes['y']),int(attributes['y'])+\
                       int(attributes['height']),32):
            obj = mo.MapObject(x,y,32,32)
            spriteList.add(obj)
            group.add(obj)


done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_speed(-32, 0)
                player.directionX = "L"
                
            elif event.key == pygame.K_RIGHT:
                player.change_speed(32, 0)
                player.directionX = "R"
                
            elif event.key == pygame.K_UP:
                player.change_speed(0, -32)
                player.directionY = "U"
                
            elif event.key == pygame.K_DOWN:
                player.change_speed(0, 32)
                player.directionY = "D"
                
            elif event.key == pygame.K_x:
                for creature in creatureList:
                    if creature.check_player_collide(player):
                        ef = EncounterFunctions()
                        ef.start_encounter(player,creature,Encounter)
                for creature in specialList:
                    if creature.check_player_collide(player,theMix):
                        theSong.fadeout(1000)
                        
            elif event.key == pygame.K_RETURN:
                if songNumber == 1:
                    songNumber = 0
                    pygame.mixer.fadeout(3500)
                    theSong = pygame.mixer.Sound("The Wasteland.ogg")
                    
                    theMix.play(theSong,loops=-1,fade_ms=2500)
                else:
                    songNumber = 1
                    pygame.mixer.fadeout(3500)
                    theSong = pygame.mixer.Sound("WhoToJoin.ogg")
                    
                    theMix.play(theSong,loops=-1,fade_ms=2500)                    
                    
                        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.change_speed(32, 0)
                
            elif event.key == pygame.K_RIGHT:
                player.change_speed(-32, 0)
                
            elif event.key == pygame.K_UP:
                player.change_speed(0, 32)
                
            elif event.key == pygame.K_DOWN:
                player.change_speed(0, -32)      
    
    for creature in testCreatureList:
        if creature.dead:
            creature.remove(group,spriteList,creatureList)
    group.center(player.rect.center)

    group.draw(screen)
    player.update(spriteList)
    
    # Cavanaugh attributed here a much needed feature...
    '''font = pygame.font.SysFont("Calibri", 100, False, False)
    text = font.render("Your game smells nice...", True, (color, color, color))
    screen.blit(text, [0, screenSize[1] // 2])
    if color is not 255:
        color += 1
    else:
        color = 0'''
    
 
    pygame.display.flip()
    
    clock.tick(12)
 
pygame.quit()
player.save()