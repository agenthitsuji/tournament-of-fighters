# Tournament of Fighters
# Armors


class Armor():
    
    def __init__(self, name, defence, weight):
        self.name = name
        self.defence = defence
        self.weight = weight
        
    
    def __repr__(self):
        return "{armor}, {defence} DR".format(armor=self.name, defence=self.defence)
    
    


def create_armor(name, defence, weight):
    return {name: Armor(name, defence, weight)}
    
# Initializing Armors


