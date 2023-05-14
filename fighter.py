# Tournament of Fighters
# Fighters

import weapon as weapons
import armor as armors
import random

fighters = []

class Fighter():
    
    def __init__(self, name, homeland, vit, agi, str, dex, wep, armor, history):
        # Base Stats
        self.name = name 
        self.homeland = homeland
        self.vitality = vit
        self.agility = agi
        self.strength = str
        self.dexterity = dex
        self.weapon = wep
        self.armor = armor 
        self.history = history
        # Calculate Speed
        self.speed = self.fighter_speed()
        # Generate HP
        self.hp = self.fighter_hp()
        
    def __repr__(self):
        return "{name} from {homeland}\nHP: {hp}\nEquipped with {wep} / {ar} AR and {arm}\nSpeed: {spd}\nVIT: {vit}\nAGI: {agi}\nSTR: {str}\nDEX: {dex}".format(
            name = self.name, 
            homeland = self.homeland,
            hp = self.hp,
            spd = self.speed,
            wep = self.weapon,
            ar =  self.fighter_calculate_attack_rating(),
            arm = self.armor,
            vit = self.vitality,
            agi = self.agility,
            str = self.strength,
            dex = self.dexterity
            )
        
    # Damage Calculations
    
    def fighter_calculate_attack_rating(self):
        return int(self.weapon.damage + (self.strength * self.weapon.str_scaling) + (self.dexterity * self.weapon.dex_scaling))
        
    def fighter_attack(self):
        return int(self.fighter_calculate_attack_rating() + random.randint(0, 5))
    
    def fighter_receive_damage(self, attack):
        return int(attack - int(attack * self.armor.defence))
    
    # Speed Calculations
        
    def fighter_encumbrance(self):
        return self.vitality - (self.weapon.weight + self.armor.weight)
    
    def fighter_speed(self):
        return self.agility - self.fighter_encumbrance()
    
    # Health Calculations
    
    def fighter_hp(self):
        if self.vitality <= 0:
            return 10
        if self.vitality <= 10:
            return self.vitality * 20
        else:
            return 200 + ((self.vitality - 10) * 15)
        
    
f1 = Fighter("Pekor", "Pekoland", 5, 7, 12, 8, weapons.weapons[0], armors.armors[0], list())
f2 = Fighter("Bumber", "Belangerijke", 12, 4, 6, 13, weapons.weapons[0], armors.armors[0], list())
fighters.append(f1)
fighters.append(f2)



for x in fighters:
    print(x)
    print(x.fighter_calculate_attack_rating())
    print(x.fighter_attack())
    print(x.fighter_receive_damage(23))
    
def generate_fighter():
    return Fighter("random", "fighter", random.randint(0, 99), random.randint(0, 99), random.randint(0, 99), random.randint(0, 99), weapons.weapons[0], armors.armors[0], list())



for x in range (3):
    print(generate_fighter())