# Tournament of Fighters
# Weapons


import filemanager as file_manager

# Scaling Table

scaling = {
    "S": 1.00,
    "A": 0.90,
    "B": 0.70,
    "C": 0.50,
    "D": 0.40,
    "E": 0.25,
    "X": 0.00
}


class Weapon():
    
    def __init__(self, name, dmg, str, dex, weight):
        self.name = name
        self.damage = dmg
        self.str_scaling = scaling.get(str)
        self.dex_scaling = scaling.get(dex)
        self.weight = weight
        
    
    def __repr__(self):
        return "{weapon}, {dmg} base damage".format(weapon=self.name, dmg=self.damage)
    
    
    
    

def create_weapon(name, damage, str_scaling, dex_scaling, weight):
    return {name: Weapon(name, damage, str_scaling, dex_scaling, weight)}



