# this page refers to the basic character design, including key attributes,
# health points, strength, and mana
class basic_character:
    def __init__(self, strength, dexterity, knowledge, health, mana, character_name):
        self.strength = int(strength)
        self.dexterity = int(dexterity)
        self.knowledge = int(knowledge)
        self.health = int(health)
        self.mana = int(mana)
        self.character_name = character_name