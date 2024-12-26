'''

Course Project - RPG by Arish Bawani

'''

import random

# humanoid superclass
class Humanoid:
    def __init__(self, height, weight, hair_color, eye_color):
        self.height = height
        self.weight = weight                             # attributes
        self.hair_color = hair_color
        self.eye_color = eye_color
        print("\n**** Now randomly rolling stat attributes for your character ****")
        self.strength = random.randint(1, 18)
        self.dexterity = random.randint(1, 18)
        self.constitution = random.randint(1, 18)                         # random stats
        self.intelligence = random.randint(1, 18)
        self.wisdom = random.randint(1, 18)
        self.charisma = random.randint(1, 18)

    def display_stats(self):
        print("\nYour character's attributes are:")
        print(f"Height: {self.height}ft")
        print(f"Weight: {self.weight}lbs")
        print(f"Hair Color: {self.hair_color}")
        print(f"Eye Color: {self.eye_color}")
        print(f"Strength: {self.strength}")                                     # stats display
        print(f"Dexterity: {self.dexterity}")
        print(f"Constitution: {self.constitution}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Wisdom: {self.wisdom}")
        print(f"Charisma: {self.charisma}")

# human sublcass
class Human(Humanoid):
    def human_bonus(self, attribute):
        print("\nAs a Human, you may add +2 to any one attribute.")
        if attribute == "strength":
            self.strength += 2
        elif attribute == "dexterity":
            self.dexterity += 2
        elif attribute == "constitution":                               # human bonus
            self.constitution += 2
        elif attribute == "intelligence":
            self.intelligence += 2
        elif attribute == "wisdom":
            self.wisdom += 2
        elif attribute == "charisma":
            self.charisma += 2

# elf subclass 
class Elf(Humanoid):
    def elves_bonus(self):
        print("\nAs an Elf, you are 100% resistant to sleep.")
        self.dexterity += 2                                      # elf bonus
        self.charisma += 2

# dwarf subclass 
class Dwarf(Humanoid):
    def dwarves_bonus(self):
        print("\nAs a Dwarf, you have 20% resistance to magic.")
        self.strength += 2
        self.constitution += 2                                # dwarf bonus                                             
        self.charisma -= 2

# create character
def characterCreation():
    print("Welcome to Falls of Eternity! Choose your playable race:")
    print("1. Human")
    print("2. Elf")
    print("3. Dwarf")

    # user inputs  
    race = input("Which race have you chosen for your character (1, 2, or 3)? ")
    hair_color = input("Enter your character's hair color: ")
    eye_color = input("Enter your character's eye color: ")                               
    height = int(input("Enter your character's height (3-7ft): "))
    weight = int(input("Enter your character's weight (60-300lbs): "))

    # character creation based on input

    if race == "1":
        character = Human(height, weight, hair_color, eye_color)
        character.display_stats()
        attribute = input("\nEnter one attribute to add +2 (strength, dexterity, constitution, intelligence, wisdom, charisma): ").lower()
        character.human_bonus(attribute)
    elif race == "2":
        character = Elf(height, weight, hair_color, eye_color)
        character.display_stats()
        character.elves_bonus()            
    elif race == "3":
        character = Dwarf(height, weight, hair_color, eye_color)
        character.display_stats()
        character.dwarves_bonus()
    else:
        print("Invalid choice. Please restart the program.")
        return

    print("\nFinal character stats:")                              # final stats
    character.display_stats()

# main
def main():
    characterCreation()

# run main
if __name__ == "__main__":
    main()
