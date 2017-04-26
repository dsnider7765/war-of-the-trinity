#save_game
#David Snider with help from Cavanaugh Richards


#experiment
'''root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "field1", name="blah").text = "some value1"
ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

tree = ET.ElementTree(root)
tree.write("filename.xml")

thing = etree.parse('filename.xml')
thingRoot = thing.getroot()
print(len(thingRoot))
for child in thingRoot:
    print(child)

<Element 'doc' at 0x7fdba106d318>
for child in thingRoot:
    for thingy in child:
        print(thingy)

<Element 'field1' at 0x7fdba106d368>
<Element 'field2' at 0x7fdba106d3b8>
for child in thingRoot:
    for thingy in child:
        print(thingy.text)

some value1
some vlaue2'''

class SaveGame(object):
    
    def __init__(self,player):
        
        self.player = player
        
    def save(self):
        import xml.etree.ElementTree as ET
        theList = self.player.stats.create_list()
        root = ET.Element(self.player.name)
        root.text = self.player.name
        info = ET.SubElement(root, "info")
        for item in theList:
            ET.SubElement(info, item.name).text = str(item.value)
        
        #ET.SubElement(info, "playerX").text = str(self.player.stats.x.value)
        #ET.SubElement(info, "playerY").text = str(self.player.stats.y.value)
        
        
        tree = ET.ElementTree(root)
        tree.write("save_game.xml")
        
        '''TESTING FOR PARSING
        test = ET.parse('save_game.xml')
        testRoot = test.getroot()
        print(testRoot[0][0].text)'''
        
    def load(self):
        
        import xml.etree.ElementTree as ET
        out = []
        tree = ET.parse("save_game.xml")
        
        root = tree.getroot()
        
        for child in root:
            for element in child:
                out.append(int(element.text))
        return out
