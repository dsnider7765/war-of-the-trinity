#encounter
#David Snider
#4/18/16
from tkinter import *
from combat  import*

'''This class is to handle the various encounters in War of the Trinity'''



class EncounterInfo(object):
    def __init__(self,options,commands):
        self.options = options
        self.commands = commands
        self.widgets = []
        
    def add(self,widget):
        self.widgets.append(widget)
        
        
class Encounter(Frame):
    def __init__(self,master,player,creature):
        """ Initialize Frame. """
        super(Encounter, self).__init__(master)  
        self.grid()
        self.master.minsize(400,400)
        
        #default encounter
        options = "Attack Diplomacy Run Sneak Trick Observe".split()
        commands = [self.attack,self.diplomacy,self.run,self.sneak,self.trick,
                    self.observe]
        self.encounterMenu = EncounterInfo(options,commands)
        
        #fight menu
        self.fight = Fight(player,creature,master)
        options = "Attack Skip".split()
        commands = [self.fight.attack,self.fight.skip]
        self.fightMenu = EncounterInfo(options,commands)
        
        self.player = player
        self.creature = creature
        
        
        self.create_widgets(self.encounterMenu)
    
    
    def create_widgets(self,menu):
        txt = '''              Choose what you would like to do              '''
        Label(self,text=txt,
              height=3).grid(row=0,column=0,columnspan=3,sticky=N)
        
        #create a temp row counter for loop
        row = 1
        for i in menu.options:
            btn = Button(self,text=i,command=menu.commands[row-1])
            menu.add(btn)
            btn.grid(row=row,column=0,sticky=W)
            row += 1
        
        self.textBox = Text(self,height=25,width=32,wrap=W)
        self.textBox.grid(row=1,column=3,rowspan=50,sticky=E)
        self.textBox.insert(0.0,self.creature.__repr__()+'\n \n'+\
                            self.creature.txt)
        if menu == self.fightMenu:
            self.fight.textBox = self.textBox
        
        
    def __repr__(self):
        return "Ecounter"
    

    
    def attack(self):
        for i in self.encounterMenu.widgets:
            i.grid_forget()
        self.create_widgets(self.fightMenu)
        
    def diplomacy(self):
        pass
    
    def run(self):
        pass
    
    def sneak(self):
        pass
    
    def trick(self):
        pass
    
    def observe(self):
        pass
        
    
class Fight:
    def __init__(self,player,creature,root):
        '''self.creature = creature
        self.player  = player'''
        self.combat = Combat(player,creature)
        self.textBox = None
        self.root = root
        
    def attack(self):
        done = False
        #print(self.combat.creature.stats.hp.value)
        self.combat.attack("PC")
        self.combat.attack("CP")
        #print(self.combat.creature.stats.hp.value)
        text = '{} \n \n{}'.format(self.combat.player.__repr__(),
                                   self.combat.creature.__repr__())
        if self.combat.creature.stats.hp.value >\
           -5:
           #self.combat.creature.stats.hp.minValue:
            txt = '''
{}

HP:{}
{}            '''.format(self.combat.player.name,
                         str(self.combat.player.stats.hp.value),
                         self.combat.creature.__repr__())
            self.textBox.delete(0.0,END)
            self.textBox.insert(0.0,txt)
            
        elif self.combat.creature.stats.hp.value <= -5:
            self.textBox.delete(0.0,END)
            self.textBox.insert(0.0,
                                '{} has died.'.format(self.combat.\
                                                      creature.name))
            done = True
            self.combat.creature.dead = True
        
        elif self.combat.player.stats.hp.value <= -5:
            self.textBox.delete(0.0,END)
            self.textBox.insert(0.0,
                                '{} has died.'.format(self.combat.\
                                                      player.name))
            done = True
            
        if done:
            self.root.destroy()
        
    def skip(self):
        pass
    
    def end(self):
        pass

#class

class EncounterFunctions(object):
    def __init__(self):
        self.root = Tk()
    
    def start_encounter(self,player,creature,classChoice):
        self.root.title(player.name+' vs '+\
                        creature.name)
        app = classChoice(self.root,player,creature)
        self.root.mainloop()


#TESTING    
if __name__ == "__main__":
    import wott_base_lib as wbl
    import player
    
    
    ef = EncounterFunctions()    
    
    ef.start_encounter(player.Player(),wbl.Creature(0,0),Encounter)