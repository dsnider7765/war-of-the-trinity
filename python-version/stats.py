# stats
# Cavanaugh Richards and adapted by David Snider
# 4/18/16

'''
NOTE:
  It is only necessary to call the Stats() class found at the 
  end of this file. All other classes listed here are used for
  initializing attributes of Stats(). 
  
  When importing this file, feel free to simply use:
      from stats import Stats
'''

# Parent Class for all stats
class Stat():
    def __init__(self, value = 1, minValue = 0, maxValue = 0, growthRate = 0.0,
                 name = 'Unnamed Stat'):
        # The name of the stat
        self.name = name
        
        # The actual value of the stat
        self.value = value
        
        # The minimum and maximum values for the stat 
        # (varies per division and character)
        self.minValue = minValue
        self.maxValue = maxValue
        
        # The rate at which the stat grows upon levelling up
        self.growthRate = growthRate
        
        

# HP Stat (Hit Points)
class HP(Stat):
    def __init__(self):
        Stat.__init__(self,value=15,name='HP',maxValue=15,minValue= -5)
        

class Strength(Stat):
    def __init__(self):
        Stat.__init__(self,name='Strength')
        

class Dexterity(Stat):
    def __init__(self):
        Stat.__init__(self,name='Dexterity')
        

class Constitution(Stat):
    def __init__(self):
        Stat.__init__(self,name='Constitution')
        

class Intelligence(Stat):
    def __init__(self):
        Stat.__init__(self,name='Intelligence')
        

class Wisdom(Stat):
    def __init__(self):
        Stat.__init__(self,name='Wisdom')
        

class Charisma(Stat):
    def __init__(self):
        Stat.__init__(self,name='Charisma')
        

class Comeliness(Stat):
    def __init__(self):
        Stat.__init__(self,name='Comeliness')
        

class Sanity(Stat):
    def __init__(self):
        Stat.__init__(self,name='Sanity')
        

class ArmorClass(Stat):
    def __init__(self):
        Stat.__init__(self,name='AC')
        
class Level(Stat):
    def __init__(self):
        Stat.__init__(self,name='Level')
        
class EXP(Stat):
    def __init__(self):
        Stat.__init__(self,name='EXP',value=0,maxValue=100,growthRate=2.5)
        
class X(Stat):
    def __init__(self):
        Stat.__init__(self,name='X',value=0)
        
class Y(Stat):
    def __init__(self):
        Stat.__init__(self,name='Y',value=0)
        
        
# Initializes all child classes of Stat
class Stats():
    def __init__(self):
        self.hp = HP()
        self.strength = Strength()
        self.dexterity = Dexterity()
        self.constitution = Constitution()
        self.intelligence = Intelligence()
        self.wisdom = Wisdom()
        self.charisma = Charisma()
        self.comeliness = Comeliness()
        self.sanity = Sanity()
        self.armorClass = ArmorClass()
        self.level = Level()
        self.exp = EXP()
        self.x = X()
        self.y = Y()
        '''self.statList = [self.x,self.y,self.level,
                         self.hp,self.strength,
                         self.dexterity,self.constitution,
                         self.intelligence,self.wisdom,
                         self.charisma,self.comeliness,
                         self.sanity,self.armorClass]'''        
    
    def __str__(self):
        statList = self.create_list()
        string = ""
        for item in statList:
            string += item.name + ': ' + str(item.value) + ' '
        return string
    
    def create_list(self):
        statList = [self.x,self.y,self.level,self.exp,
                    self.hp,self.strength,
                    self.dexterity,self.constitution,
                    self.intelligence,self.wisdom,
                    self.charisma,self.comeliness,
                    self.sanity,self.armorClass]
        return statList
    
if __name__ == "__main__":
    stats = Stats()
    print(stats)