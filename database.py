# Tournament of Fighters
# Database

import random

import filemanager as file_manager

import fighter as fighter_obj
import weapon as weapon_obj
import armor as armor_obj

name_db_name = 'DB/names.txt'
homeland_db_name = 'DB/homelands.txt'
armor_db_name = 'DB/armors.csv'
weapon_db_name = 'DB/weapons.csv'

class Database():
    
    def __init__(self):
        self.fighter_db = list()
        self.name_db = file_manager.load_text(name_db_name)
        self.homeland_db = file_manager.load_text(homeland_db_name)
        self.weapon_db = file_manager.load_weapons(weapon_db_name)
        self.armor_db = file_manager.load_armors(armor_db_name)


    def generate_random_fighter(self):
        return fighter_obj.Fighter(
            Database.get_random_db_item(self.name_db), 
            Database.get_random_db_item(self.homeland_db), 
            random.randint(0, 20), 
            random.randint(0, 20), 
            random.randint(0, 20), 
            random.randint(0, 20), 
            weapon_obj.weapons["Sword"], 
            armor_obj.armors["Chainmail"], 
            list()
            )
        
        
        
        

    def get_random_db_item(database):
        return database[random.randint(0, len(database) - 1)]

