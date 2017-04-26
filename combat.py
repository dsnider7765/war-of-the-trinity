#combat
#David Snider
#4/22/16

import random

class Combat(object):
    def __init__(self,player,creature):
        self.player = player
        self.creature = creature
        
    def attack(self,order):
        #print(self.player.stats.strength.value)
        if order == "PC":
            self.calculate_attack_PC()
        elif order == "CP":
            self.calculate_attack_CP()
        else:
            print('Invalid Argument: "{}". Please input either "PC" or "CP"')
            
    def roll_dice(self,number=1,dNumber=20):
        '''number is for number of dice; dNumber is side number for dice'''
        out = 0
        for i in range(number):
            out += random.randint(1,dNumber)
        return out
    
    def calculate_attack_PC(self):
        self.creature.stats.hp.value = self.creature.stats.hp.value - \
        ((self.player.stats.strength.value + self.roll_dice(1,6)) * \
         self.player.element.check_advantage(self.creature.element))
        
    def calculate_attack_CP(self):
        self.player.stats.hp.value = self.player.stats.hp.value - \
        ((self.creature.stats.strength.value + self.roll_dice(1,6)) * \
         self.creature.element.check_advantage(self.player.element))        
        
