# Tournament of Fighters
# File Manager


import csv as csvReader
import weapon
import armor


def load_text(file):
    list = []
    with open(file, 'r') as names_list:
      for line in names_list:   
          list.append(line.strip("\n"))
    return list
    
    
    
def load_weapons(file):
    weapons = {}
    with open(file, newline='') as csvfile:
        reader = csvReader.DictReader(csvfile)
        for row in reader:
            #print("Weapon:" + row['Weapon'] + " Damage:" + row['Base Damage'] + " STR:" + row['STR Scaling'] + " DEX:" + row['DEX Scaling'] + " Weight: " + row['Weight'])
            weapons[row['Weapon']] = weapon.Weapon(row['Weapon'], row['Base Damage'], row['STR Scaling'], row['DEX Scaling'], row['Weight'])
            print(weapons[row['Weapon']])
    
    return weapons


def load_armors(file):
    armors = {}
    with open(file, newline='') as csvfile:
        reader = csvReader.DictReader(csvfile)
        for row in reader:
            armors[row['Armor']] = armor.Armor(row['Armor'], row['Defence'], row['Weight'])
            print(armors[row['Armor']])
    
    return armors