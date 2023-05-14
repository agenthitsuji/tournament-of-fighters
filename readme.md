# Tournament of Fighters

## OVERVIEW 

Tournament of Fighters is a text-based game written in Python 3. It simulates combat between fighters with a set of attributes and items. There is no player input, it is meant to be more of an experience. Combat system is mostly inspired by Dark Souls' systems.

## TECHNOLOGY 

+  **Python3** as a coding language of choice

## MAIN CONCEPTS

+ **FIGHTER** - one of the characters partaking in the tournament. All fighters have the following attributes:
	+  **VIT** - Vitality, which determines Fighter's health and ability to wear heavier armor
	+  **AGI** - Agility, which determines who goes first during the combat turn.
	+  **STR** - Strength, which determines attack bonus from STR-scaling weapons (see below for Scaling)
	+  **DEX** - Dexterity, which determines attack bonus from DEX-scaling weapons (see below for Scaling)
	+  **Name** and **Homeland** - strings generated or randomly picked by the game, defining Fighter's name and country of origin.
	* **ATTRIBUTE** - as listed above, attributes translate into Fighter's combat ability. Attributes are hard-capped at 99, there is no soft cap as of now.
	+ **FIGHTER LEVEL** - This is similar to Soul Level and online matchmaking. Fighter's attributes are added together to determine what their FL is.
	+ **HISTORY** - each Fighter has their highest placements and Honours (see below) stored in their history.

+ **WEAPON** - used by Fighter to deal damage. Each weapon has following attributes:
	+ **DAMAGE** - base damage, flat value.
	+ **SCALING** - each weapon gets rated from S to E for both STR and DEX damage. Then, weapon's scaling bonus is calculated by multiplying scaling bonus with Fighter's respective attribute.
	+ **WEIGHT** - each weapon has its weight, too much weight can lead to Encumbrance penalty thus lowering Fighter's speed.

+ **ARMOR** - a set of armor worn by Fighter, which helps to mitigate incoming damage. Each armor has following attributes:
	+ **DMG REDUCTION** - a percentage bonus which lowers incoming damage, f.e an armor with 20% reduction bonus would reduce a 10 damage attack to 8.
	+ **WEIGHT** - each armor has its weight, too much weight can lead to Encumbrance penalty thus lowering Fighter's speed.

+ **COMBAT** - Combat is a match between two Fighters, which ends when one of the contestants HP drops below 0, or when a turn limit is reached - whichever one comes first. Combat consists of the following phases:
	+ **PRESENTATION** - each Fighter's current status is displayed - attributes, equipment, etc.
	+ **SPEED TEST** - Fighters speeds are compared and turn order is decided, who goes first that is.
	+ **ATTACK PHASE** - each Fighter generates a value from their stats and damage is applied. 
	+ **RESULT PHASE** - once a victory condition is met, a winner is determined in the Result Phase.

+ **TOURNAMENT** - a set of Combat instances between a pool of selected Fighters to determine a final winner. 
	+ **RANK** - Tournament Rank is determined by amount of Fighters taking place in it, equal to number of rounds it takes to get to the final. A 4-Fighter tournament will have one round - thus a rank of 1.  A 64-Fighter Tournament has five rounds - a rank of 5.
	+ **LADDER** - all Combat instances are prearranged on a ladder. Winners of combat 1 and combat 2 meet in combat 3 etc.
	+ **HONOURS** - each Tournament has a set of Honours that can be awarded to Fighters. Honours are saved for future viewing. They come in four classes, names of which aren't determined yet. Each Honour has its description as well.
	+ **HALL OF FAME** - Fighters with one or more Honour are inducted into Hall of Fame. Each Fighter's honours are added together to calculate their Honour Points, the higher the value, the higher their position.

## THINGS WE NEED TO CODE

+ **FIGHTER**:
	+ ability to choose Name and Homeland from pre-determined list
	+ ability to input custom Name and Homeland 
	+ ability to assign values to attributes
	+ ability to assign Weapon and Armor
	+ ability to add entries to Fighter's history
	+ ability to scale stats up/down depending on required Fighter Level
	+ a register of Fighters, ability to import and export files
+ **WEAPON**:
	+ damage calculation: base + scaling + random bonus
+ **ARMOR**
	+ calculations for weight and encumbrance bonus
+ **COMBAT**:
	+ determining turn order
	+ damage application
	+ determining winner 
+ **TOURNAMENT**:
	+ generating ladder and assigning Fighters to it
	+ progressing the ladder until the final
	+ awarding Honours to Fighters
+ **HALL OF FAME**:
	+ calculating Honour Points and keeping the table in order

