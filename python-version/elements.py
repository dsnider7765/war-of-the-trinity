#elements
#David Snider
#4/22/16

class Element(object):
    def __init__(self,value):
        self.value = value
        self.ELEMENTLIST = 'non fire water electric grass ice poison ground\
        rock dark light metal'.split()
        self.advantages = {}
        
    def _create_advantages(self,numlist):
        for i in range(len(self.ELEMENTLIST)):
            self.advantages[self.ELEMENTLIST[i]] = numlist[i]
    
    def check_advantage(self,element):
        return self.advantages[element.value]
    
    def __repr__(self):
        out = "{}:\n".format(self.value)
        
        theList = [Non(), Fire(), Water(), Electric(), Grass(), Ice(), Poison(),
                   Ground(), Rock(), Dark(), Light(), Metal()]
        
        for i in theList:
            if self.check_advantage(i) == 1:
                out += 'is neutral against {}\n'.format(i.value)
            elif self.check_advantage(i) > 1:
                out += 'is {} times stronger against {}\
                \n'.format(str(self.check_advantage(i)),i.value)
                
            elif self.check_advantage(i) < 1 and self.check_advantage(i) > 0:
                out += 'is {} times weaker against {}\
                \n'.format(str(self.check_advantage(i)),i.value)
                
            else:
                out += 'has no effect on {}\n'.format(i.value)
        
        return out
    
    
class Non(Element):
    def __init__(self):
        super(Non,self).__init__('non')
        numList = [1,1,1,1,1,1,1,1,1,1,1,1]
        self._create_advantages(numList)
        
class Fire(Element):
    def __init__(self):
        super(Fire,self).__init__('fire')
        numList = [1,1,0.45,1,2,1.5,1.1,0.3,0.3,1,1,1.1]
        self._create_advantages(numList)
        
class Water(Element):
    def __init__(self):
        super(Water,self).__init__('water')
        numList = [1,2,1,1,0.5,0.9,1,0.8,1.2,1,1,1.2]
        self._create_advantages(numList)
        
class Electric(Element):
    def __init__(self):
        super(Electric,self).__init__('electric')
        numList = [1,1,2,1,1,1.5,1,0,0,1,1,0.3]
        self._create_advantages(numList)
        
class Grass(Element):
    def __init__(self):
        super(Grass,self).__init__('grass')
        numList = [1,0.5,2,0.8,0.8,1.75,0.5,1.2,1.4,1,1,0.9]
        self._create_advantages(numList)
        
class Ice(Element):
    def __init__(self):
        super(Ice,self).__init__('ice')
        numList = [1,1.5,1.1,0.8,1.3,1,1.2,1,1.2,1,1,1.2]
        self._create_advantages(numList)
        
class Poison(Element):
    def __init__(self):
        super(Poison,self).__init__('poison')
        numList = [2,1,0.5,1,1.5,0.8,1,0,0,1,1,0]
        self._create_advantages(numList)
        
class Ground(Element):
    def __init__(self):
        super(Ground,self).__init__('ground')
        numList = [1,1.9,1.2,2,0.8,1,2,1,0.8,1,1,0.2]
        self._create_advantages(numList)
        
class Rock(Element):
    def __init__(self):
        super(Rock,self).__init__('rock')
        numList = [1,1.7,0.7,2,0.7,1,2,1.2,1,1,1,0.2]
        self._create_advantages(numList)
        
class Dark(Element):
    def __init__(self):
        super(Dark,self).__init__('dark')
        numList = [1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,0,1.5]
        self._create_advantages(numList)
        
class Light(Element):
    def __init__(self):
        super(Light,self).__init__('light')
        numList = [1,1,1,1,1,1,1,1,1,4,1,1]
        self._create_advantages(numList)
        
class Metal(Element):
    def __init__(self):
        super(Metal,self).__init__('metal')
        numList = [1,1,1,1.7,1,1,1.5,1.5,1.5,1,1,1]
        self._create_advantages(numList)
        
        
class Types(object):
    def __init__(self):
        self.non = Non()
        self.fire = Fire()
        self.water = Water()
        self.electric = Electric()
        self.grass = Grass()
        self.ice = Ice()
        self.poison = Poison()
        self.ground = Ground()
        self.rock = Rock()
        self.dark = Dark()
        self.light = Light()
        self.metal = Metal()
        self._create_xml()
        
    def __repr__(self):
        theList = [self.non, self.fire, self.water, self.electric, self.grass,
                   self.ice, self.poison, self.ground, self.rock, self.dark,
                   self.light, self.metal]
        out = ''
        for i in theList:
            out += str(i) + '\n'
        return out
    
    def _create_xml(self):
        theList = [self.non, self.fire, self.water, self.electric, self.grass,
                   self.ice, self.poison, self.ground, self.rock, self.dark,
                   self.light, self.metal] 
        import xml.etree.ElementTree as ET
        root = ET.Element("types")
        for i in range(len(theList)):
            ET.SubElement(root,str(theList[i].value)).text = str(theList[i])
                
        tree = ET.ElementTree(root)
        tree.write("types.xml")        


#TESTING
if __name__ == "__main__":
    types = Types()
    print(types)
    print(types.metal.check_advantage(types.fire))
    print(types.light.check_advantage(types.dark))
    print(types.non.check_advantage(types.non))