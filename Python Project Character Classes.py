class Warrior:
    def __init__(self):
        self.level = 8
        self.vigor = 11
        self.mind = 12
        self.endurance = 11
        self.strength = 10
        self.dexterity = 16
        self.intelligence = 10
        self.faith = 8
        self.arcane = 9
        self.weapons = ["Scimitar", "Scimitar"]
        self.shield = "Riveted Wooden Shield"
        self.armor = {
            "Head": "Blue Cowl",
            "Chest": "Blue Cloth Vest",
            "Hands": "Warrior Gauntlets",
            "Legs": "Warrior Greaves"
        }

    def display_title(self):
        print("=" * 30)
        print("    Warrior Class   ")
        print("=" * 30)

    def display_stats(self):
        self.display_title()
        stats = {
            "Level": self.level,
            "Vigor": self.vigor,
            "Mind": self.mind,
            "Endurance": self.endurance,
            "Strength": self.strength,
            "Dexterity": self.dexterity,
            "Intelligence": self.intelligence,
            "Faith": self.faith,
            "Arcane": self.arcane,
        }
        max_length = max(len(key) for key in stats.keys())

        print("+" + "-" * (max_length + 10) + "+")
        for stat, value in stats.items():
            print(f"| {stat.ljust(max_length)} : {str(value).rjust(4)} |")
        
        print("+" + "-" * (max_length + 10) + "+")

    def display_equipment(self):
        print("\nEquipped:")
        
        print("\nWeapons & Shield:")
        for weapon in self.weapons:
           print(f" - {weapon}")
        print(f" - {self.shield}")
    
        print("\nArmor:")
        for part, piece in self.armor.items():
            print(f" - {piece} ({part})")


class Hero:
    def __init__(self):
        self.level = 7
        self.vigor = 14
        self.mind = 9
        self.endurance = 12
        self.strength = 16
        self.dexterity = 9
        self.intelligence = 7
        self.faith = 8
        self.arcane = 11
        self.weapons = ["Battle Axe"]
        self.shield = "Large Leather Shield"
        self.armor = {
            "Head": "Champion Headband",
            "Chest": "Champion Pauldron",
            "Hands": "Champion Bracers",
            "Legs": "Champion Gaiters"
        }

    def display_title(self):
        print("=" * 30)
        print("    Hero Class   ")
        print("=" * 30)

    def display_stats(self):
        self.display_title()
        stats = {
            "Level": self.level,
            "Vigor": self.vigor,
            "Mind": self.mind,
            "Endurance": self.endurance,
            "Strength": self.strength,
            "Dexterity": self.dexterity,
            "Intelligence": self.intelligence,
            "Faith": self.faith,
            "Arcane": self.arcane,
        }
        max_length = max(len(key) for key in stats.keys())

        print("+" + "-" * (max_length + 10) + "+")
        for stat, value in stats.items():
            print(f"| {stat.ljust(max_length)} : {str(value).rjust(4)} |")
        
        print("+" + "-" * (max_length + 10) + "+")

    def display_equipment(self):
        print("\nEquipped:")
        
        print("\nWeapons & Shield:")
        for weapon in self.weapons:
           print(f" - {weapon}")
        print(f" - {self.shield}")
    
        print("\nArmor:")
        for part, piece in self.armor.items():
            print(f" - {piece} ({part})")

class Astrologer:
    def __init__(self):
        self.level = 6
        self.vigor = 9
        self.mind = 15
        self.endurance = 9
        self.strength = 8
        self.dexterity = 12
        self.intelligence = 16
        self.faith = 7
        self.arcane = 9
        self.weapons = ["Astrolger's Staff, Short Sword"]
        self.shield = "Scripture Wooden Shield"
        self.armor = {
            "Head": "Astrologer Hood",
            "Chest": "Astrologer Robe",
            "Hands": "Astrologer Gloves",
            "Legs": "Astrologer Trousers"
        }
    def display_title(self):
        print("=" * 30)
        print("    Astrologer Class    ")
        print("=" * 30)
    def display_stats(self):
        self.display_title()
        stats = {
            "Level": self.level,
            "Vigor": self.vigor,
            "Mind": self.mind,
            "Endurance": self.endurance,
            "Strength": self.strength,
            "Dexterity": self.dexterity,
            "Intelligence": self.intelligence,
            "Faith": self.faith,
            "Arcane": self.arcane,
        }
        max_length = max(len(key) for key in stats.keys())

        print("+" + "-" * (max_length +10) + "+")
        for stat, value in stats.items():
            print(f"| {stat.ljust(max_length)} : {str(value).rjust(4)} |")
        print("+" + "-" * (max_length +10) + "+")

    def display_equipment(self):
        print("\nEquipped:")
        print("\nWeapons & Shields:")
        for weapon in self.weapons:
            print(f" - {weapon}")
        print(f" = {self.shield}")

        print("\nArmor:")
        for part, piece in self.armor.items():
            print(f"-= {piece} ({part})")
class Prophet:
    def __init__(self):
        self.level = 7
        self.vigor = 10
        self.mind = 14
        self.endurance = 8
        self.strength = 11
        self.dexterity = 10
        self.intelligence = 7
        self.faith = 16
        self.arcane = 10
        self.weapons = ["Short Spear", "Finger Seal"]
        self.shield = "Rickety Wooden Shield"
        self.armor = {
            "Head": "Prophet Blindfold",
            "Chest": "Prophet Robe",
            "Legs": "Prophet Trousers"
        }
    def display_title(self):
        print("=" * 30)
        print("    Prophet Class    ")
        print("=" * 30) 
    def display_stats(self):
        self.display_title()
        stats = {
             "Level": self.level,
            "Vigor": self.vigor,
            "Mind": self.mind,
            "Endurance": self.endurance,
            "Strength": self.strength,
            "Dexterity": self.dexterity,
            "Intelligence": self.intelligence,
            "Faith": self.faith,
            "Arcane": self.arcane,
        }
        max_length = max(len(key) for key in stats.keys())

        print("+" + "-" * (max_length +10) + "+")
        for stat, value in stats.items():
            print(f"| {stat.ljust(max_length)} : {str(value).rjust(4)} |")
        print("+" + "-" * (max_length + 10) + "+")

    def display_equipment(self):
        print("\nEquipped:")
        print("\nWeapons & Shield:")
        for weapon in self.weapons:
            print(f" - {weapon}")
        print(f" - {self.shield}")

        print("\nArmor:")
        for part, piece in self.armor.items():
            print(f" - {piece} ({part})")
   
def choose_class():
    while True:
        print("\n=========================")
        print("\nChoose Your Class")
        print("\n=========================")
        print("A. Warrior")
        print("B. Hero")
        print("C. Astrologer")
        print("D. Prophet")
        print("x. Exit")

        choice = input("\nEnter your choice (A/B/C/D/X): ").strip().upper()

        if choice == "A":
            player = Warrior()
        elif choice =="B":
            player = Hero()
        elif choice =="C":
            player = Astrologer()
        elif choice =="D":
            player = Prophet()
        elif choice =="X":
            print("\nExiting game. Goodbye Champion!\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")
            continue

        player.display_stats()
        player.display_equipment()
        print("\n" + "=" * 30 + "\n")

if __name__ == "__main__":
    choose_class()



