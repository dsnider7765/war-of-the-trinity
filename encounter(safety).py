#encounter
#David Snider
#4/18/16
from tkinter import *
'''This class is to handle the various encounters in War of the Trinity'''

class Encounter(Frame):
    def __init__(self,master,creature):
        """ Initialize Frame. """
        super(Encounter, self).__init__(master)  
        self.grid()
        self.master.minsize(400,400)
        
        self.options = "Attack Diplomacy Run Sneak Trick Observe".split()
        self.commandOptions = [self.attack,self.diplomacy,self.run,self.sneak,
                               self.trick,self.observe]
        #self.choice = StringVar()
        self.encountered = creature
        
        self.create_widgets()
    
    
    def create_widgets(self):
        #create a temp row counter for loop
        row = 0
        for i in self.options:
            Button(self,text=i,command=self.commandOptions[row]).grid(row=row,
                                                                      column=0,
                                                                      sticky=W)
            row += 1
        
        
    def __repr__(self):
        return "Ecounter"
    
    '''def choose(self):
        print(self.choice.get())'''
    
    def attack(self):
        self.master.destroy()
        ef = EncounterFunctions()
        ef.start_encounter(self.encountered,Fight)
        
    
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
        
    
class Fight(Encounter):
    def __init__(self,master,creature):
        """ Initialize Frame. """
        super(Encounter, self).__init__(master)  
        self.grid()
        self.master.minsize(400,400)
        
        
        self.options = "Attack Skip".split()
        self.commandOptions = [self.attack,self.skip]
        #self.choice = StringVar()
        self.encountered = creature
        
        self.create_widgets()
        
    def __repr__(self):
        return "Fight"
    
    def attack(self):
        pass
    def skip(self):
        pass


class EncounterFunctions(object):
    def __init__(self):
        self.root = Tk()
    
    def start_encounter(self,creature,classChoice):
        self.root.title(classChoice.__repr__(classChoice))
        app = classChoice(self.root,creature)
        self.root.mainloop()
        
    def close_encounter(self):
        self.root.destroy()
    


#TESTING    
if __name__ == "__main__":
    
    
    ef = EncounterFunctions()    
    
    ef.start_encounter('',Encounter)