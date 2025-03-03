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

   
       
player = Warrior()
player.display_stats()
player.display_equipment()

