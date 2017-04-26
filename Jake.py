#Legend of the Dragon
#Jake Routh
#4/25/16

from tkinter import *


class Directions(object):
    def __init__(self,options,commands):
        self.options = options
        self.commands = commands
        self.widgets = []
        
    def add(self,widget):
        self.widgets.append(widget)
        
    


class Game(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.parent.title("Legend of the Dragon")
        self.grid()
        options = 'hi hello butts whatever'.split()
        self.createCounter = 0
        commands=[self.hi,self.hello,self.butts,self.whatever]
        self.directions = Directions(options,commands)
        self.createwidgets(self.directions)
        
    def createwidgets(self,menu):
        row = 1
        for i in menu.options:
            btn = Button(self,text=i,command=menu.commands[row-1])
            menu.add(btn)
            btn.grid(row=row,column=0,sticky=W)
            row += 1        
        
        '''Button(self,
               text = "go left",
               command = self.i
               ).grid(row = 6, column = 0, sticky = W)'''
        if self.createCounter == 0:
            self.story_txt = Text(self, width = 100, height = 10, wrap = WORD)
            self.story_txt.grid(row =0, column = 2057, columnspan = 1,rowspan=700,
                                sticky=S)
        self.createCounter += 1
        
    def hi(self):
        self.story_txt.insert(END,"Hi ")   
    def hello(self):
        self.story_txt.insert(END,"Hello ")   
    def butts(self):
        self.story_txt.insert(END,"Butts ")   
    def whatever(self):
        for i in self.directions.widgets:
            i.grid_forget()
        self.story_txt.delete(0.0,END)
        self.story_txt.insert(0.0,"I AM THE NEW THING!!!!!!!!")
        options = 'new thing'.split()
        commands = [self.hi,self.hello]
        self.directions = Directions(options,commands)
        self.createwidgets(self.directions)


def main():
   
    root = Tk()
    root.geometry("860x545+300+300")
    app = Game(root)
    root.mainloop()  


if __name__ == '__main__':
    main()