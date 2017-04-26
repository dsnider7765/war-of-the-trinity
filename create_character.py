#create_character
#David Snider
#4/25/16

'''Different ways to create your character based on which faction chosen'''


from tkinter import *
from save_game import *
import wott_base_lib as wbl
import pygame


class CharacterCreation(Frame):
    def __init__(self,root,player,loadList,song):
        super(CharacterCreation, self).__init__(root)  
        self.grid()
        root.title("Class Selection")
        self.master.minsize(400,400)
        self.loadList = loadList.get()
        self.player = player
        self.choice = IntVar()
        self.entryBoxList = []
        self.song = song
        for i in range(0,10):
            self.entryBoxList.append(Entry(self,width=6,state="readonly",
                                           font=("Times", 15, "bold")))  
        self.create_widgets()
        
    def create_widgets(self):
        #+3
        #10
        #statList = self.loadList
        playerStatList = self.player.stats.create_list()
        for i in range(1,11):
            Label(self,text=playerStatList[i+3].name,
                  font=("Times", 15, "bold")).grid(row=i,column=0,
                                                           sticky=W)
            self.entryBoxList[i-1].grid(row=i,column=1,sticky=W)
            #self.entryBoxList[i-1].insert(0, str(statList[i-1].get()[1]))
        for i in range(0,4):
            Radiobutton(self,text=self.loadList[i].name,variable=self.choice,
                        value=i,
                        command=self.handle_choice,
                        font=("Times", 15, "bold")).grid(row=i+1,column=2,sticky=W)
        Button(self,text="Submit",command=self.submit,
               font=("Times", 15, "bold")).grid(row=11,column=0,
                                                            sticky=W)
        self.textBox = Text(self,width=50,height=10,wrap=WORD,state=DISABLED,
                            font=("URW Chancery L", 25, "bold italic"))
        self.textBox.grid(row=1,rowspan=10,column=3,sticky=W)
    
    def handle_choice(self):
        #gets the stat list from the chosen loadout
        statList = self.loadList[self.choice.get()].get()[1]
        for i in range(0,10):
            self.entryBoxList[i].config(state=NORMAL)
            self.entryBoxList[i].delete(0,END)
            self.entryBoxList[i].insert(0,str(statList[i]))
            self.entryBoxList[i].config(state="readonly")
        description = self.loadList[self.choice.get()].get()[2]
        self.textBox.config(state=NORMAL)
        self.textBox.delete(0.0,END)
        self.textBox.insert(0.0,description)
        self.textBox.config(state=DISABLED)
            
    def submit(self):
        playerStatList = self.player.stats.create_list()
        for i in range(0,10):
            playerStatList[i+4].value = int(self.entryBoxList[i].get())
        self.player.save()
        self.master.destroy()
        
            
                                        
        
        
class SciCharacterCreation(CharacterCreation):
    def __init__(self,root,player,song):
        super(SciCharacterCreation,self).__init__(root,player,wbl.SciLoadList(),
                                                  song)
        
    def submit(self):
        super(SciCharacterCreation,self).submit()
        self.song.fadeout(2500)
        song = pygame.mixer.Sound("Institute of Science.ogg")
        #self.song = pygame.mixer.Sound("Institute of Science.ogg")
        self.song.play(song,loops=-1,fade_ms=2500)
        
class MutCharacterCreation(CharacterCreation):
    def __init__(self,root,player,song):
        super(MutCharacterCreation,self).__init__(root,player,wbl.MutLoadList(),
                                                  song)
        
    def submit(self):
        super(MutCharacterCreation,self).submit()
        self.song.fadeout(2500)
        #self.song = pygame.mixer.Sound("Army of the Republic.ogg")
        song = pygame.mixer.Sound("Army of the Republic.ogg")
        self.song.play(song,loops=-1,fade_ms=2500)
        
class MagCharacterCreation(CharacterCreation):
    def __init__(self,root,player,song):
        super(MagCharacterCreation,self).__init__(root,player,wbl.MagLoadList(),
                                                  song)
        
    def submit(self):
        super(MagCharacterCreation,self).submit()
        self.song.fadeout(2500)
        #self.song = pygame.mixer.Sound("Magic.ogg")
        song = pygame.mixer.Sound("Magic.ogg")
        self.song.play(song,loops=-1,fade_ms=2500)

        






#TESTING
if __name__ == "__main__":
    from player import *
    player = Player()
    root = Tk()
    app = MagCharacterCreation(root,player)
    root.mainloop()  
    root = Tk()
    app = SciCharacterCreation(root,player)
    root.mainloop()
    root = Tk()
    app = MutCharacterCreation(root,player)
    root.mainloop()