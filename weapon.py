# Tournament of Fighters
# Weapons

# Scaling Table
scaling = {
    "S": 1.00,
    "A": 0.90,
    "B": 0.70,
    "C": 0.50,
    "D": 0.40,
    "E": 0.25
}

weapons = []

class Weapon():
    
    def __init__(self, name, dmg, str, dex, weight):
        self.name = name
        self.damage = dmg
        self.str_scaling = scaling.get(str)
        self.dex_scaling = scaling.get(dex)
        self.weight = weight
        
    
    def __repr__(self):
        return "{weapon}, {dmg} base damage".format(weapon=self.name, dmg=self.damage)
    
    

weapons.append(Weapon("Sword", 10, "C", "S", 5))
