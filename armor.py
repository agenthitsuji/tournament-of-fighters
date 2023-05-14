# Tournament of Fighters
# Armors

armors = []

class Armor():
    
    def __init__(self, name, defence, weight):
        self.name = name
        self.defence = defence
        self.weight = weight
        
    
    def __repr__(self):
        return "{armor}, {defence} DR".format(armor=self.name, defence=self.defence)
    
    


armors.append(Armor("Chainmail", 0.10, 10))