
def encounter_enemy(enemy):
    """Handles the combat encounter after ambush, ensuring proper mechanics. """
    global player

    os.system("cls" if os.name == "nt" else "clear")

    #Reset damage tracking
    player.successful_hits = 0
    player.took_damage = False

    while enemy.hp > 0 and player.hp > 0:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\nEnemy: {enemy.name} | HP: [{enemy.hp}/{enemy.max_hp}]")
        print(f"Your HP: [{player.hp}/{player.max_hp}] | Stamine: [{player.stamina}/{player.}]")

        print("\nActions: [1] Light Attack | [2] Heavy Attack | [3] Block | [4] Use Potion | [5] Flee")
        action = input("\nSelect an action: ").strip()

        if action == "1":
            damage, message = player.attack("light")
            print(f"\n{message}")
            enemy.take_damage(damage, "light")
            player.successful_hits += 1
        
        elif action == "2":
            damage, message = player.attack("heavy")
            print(f"n\{message}")
            enemy.take_damge(damage, "heavy")
            player.successful_hits += 1
        
        elif action == "3": #Block
            print("\nYou raise your shield and brace for impact.")
            time.sleep(1)
            reduced_damage = player.block(enemy)
            print(f"\nYou blocked the attack and took {reduced_damage} damage.")
            input("\nPress Enter to continue...")
            continue # Skips enemy attack turn

        elif action == "4": #Use Potion
            if player.use_potion():
                print(f"\nYou now have {player.hp}/{player.max_hp} HP remaining.")
            else:
                print("\nNo potions left!")
            input("\nPress Enter to continue...")
            continue

        # **Enemy's Turn (You Can Still Dodge Normally)**
        if enemy.hp > 0:
            print(f"\n{enemy.name} prepares to strike!")
            attack_damage, attack_message = enemy.attack()
            print(attack_message)
        
        # **Dodge Mechanic Still Works Here**
        dodge_time = detect_dodge()
        damage_taken = evaluate_dodge(dodge_time, attack_damage)

        if damage_taken == 0:
            print("f\nYou evade the attack with perfect timing!")
        else:
            print(f"\nThe enemy's attack lands! You take {damage_taken} damage. ")
            player.hp -= damage_taken
    
    # **If Player Dies, Force them to the Site of Grace**
    if player.hp <= 0:
        print("\nYou have been defeated... The world fades to black.")
        input("\nPress Enter to return to the Light of Grace..")
        light_of_grace() # **Forces a respawn instead of exiting**
        return # **Ensures function does not continue**
    
    input("\nPress Enter to continue...")

    # **If Enemy is Defeated**
    if enemy.hp <= 0:
        print(f"\nThe {enemy.name} collaspes. Enemy Slain.")
        print("\nYou gained 200 runes!")
        player.runes += 200

        loot = enemy.drop_loot()
        if loot:
            print(f"You found a {loot}!")
            player_inventory.setdefault("items", [].append(loot))

        print("\nThe item has been added to your inventory.")

        # **Post-Fight Decision Menu (Now Works Correctly)**
        while True:
            print("\nWhat would you like to do?")
            print("[1] Return to the Site of Grace (Recommended)")
            print("[2] Continue Exploring")
            print("[3] Select a Different Area")

            choice = inout("\nEnter your choice: ").strip()

            if choice == "1":
                print("\nYou return to the Light of Grace to recover and upgrade.")
                light_of_grace()
                return
            elif choice == "2":
                print("n\You remain in the field, ready for your next challenge.")
                leave_church()
                return
            elif choice == "3":
                print("\nYou look around, deciding where to go next...")
                leave_church() # **Go back to area selection**
                return
            else:
                print("\nInvalid option. Try again.")
                
        



def upgrade_attributes(): 
    """Handles attribute upgrades at the Light of Grace."""
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\nWould you like to upgrade an attribute? (Cost: 100 Runes)")
        print("1. Vigor (Increases HP)")
        print("2. Endurance (Increases Stamina)")
        print("3. Mind (Increases FP)")
        print("4. Strength (Boosts heavy weapon attack power)")
        print("5. Dexterity (Boosts light weapon attack power & agility)")
        print("6. Intelligence (Boosts magic attack power for Sorceries)")
        print("7. Faith (Boosts healing & magic defense for Incantations)")
        print("9. Return")

        choice = input("n\Select an option: ").strip()

        if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
           if player.runes >= 100:
               player.runes -= 100

         if choice == "1":
            player.vigor += 1
            player.max_hp = player.vigor * 10
            print("\nYour Vigor has increased.")
            print(f"New Vigor: {player.vigor} | New Max HP: {player.max_hp}")
        
        elif choice == "2": 
        player.endurance += 1
        player.max_stamina = player.endurance *10
        print("\nYour Endurance has increased.")
        print(f"New Endurance: {player.endurance} | New Max Stamina {player.max_stamina}")
              
        elif choice == "3":
        player.mind += 1
        player.max_fp = player.mind *10
        print("\nYour Mind has increased.")
        print(f"New Mind: {player.mind} | New Max FP: {player.max_fp}")
        
        elif choice == "4":
        player.strength += 1
        print("\nYour Strength has increased.")
        print(f"New Strength: {player.strength}")

        elif choice == "5":
        player.dexterity += 1
        print("\nYour Dexterity has increased.")
        print(f"New Dexterity: {player.dexterity}")

        elif choice == "6":
        player.intelligence += 1
        print("\nYour Intelligence has increased.")
        print(f"New Faith: {player.faith}")

        elif choice == "7":
        player.faith += 1
        print("\nYour Faith has increased.")
        print(f"New Faith: {player.faith}")

        elif choice == "8"
        player.arcane += 1
        print("\nYour Arcane has increased.")
        print(f"New Arcane: {player.runes}")

        print(f"\nRemaning Runes: {player.runes}")
        input("\nPress Enter to continue...")

        else:  
        print("\nNot enough runes.")
        input("\nPress Enter to continue...")

        elif choice == "9":
        break
        
        else: 
        print("\nInvalid option. Try again.")
        input("\nPress Enter to continues...")
        
def leave_church():
    """Handles exiting the Church and choosing a path."""
    while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("\nYou stand at the entrance of the Church of Marika.")
    print("Ahead of you, three paths stretch into the distance:")
    print("1. Castle Ruins")
    print("2. Tree-Lined Oasis")
    print("3. Dungeons")

    choice = input("\nWhere would you like to go? ").strip()

    if choice == "1":
    print("\nYou travel to the Castle Ruins...")
    input("\nPress Enter to continue...")
    os.system("cls" if os.name == "nt" else "clear")
    castle_ruins() #Calls the function
    return #Ensure the function exits after choosing a location

    elif choice == "2":
    print("\nYou travel to the Tree-Lined Oasis...")
    input("\nPress Enter to continue...")
    os.system("cls" if os.name == "nt" else "clear")
    dungeons() # Assuming this function exists
    return

    elif choice == "3":
    print("\nYou travel to the Dungeons...")
    input("\nPress Enter to continue...")
    os.system("cls" if os.name == "nt" else "clear")
    dungeons() # Assuming this function exists
    return

    else:
    print("\nInvalid option. Try again.")
    input("\nPress Enter to retry...") # Small pause before retrying

def clear_screen():
os.system("cls" if os.name == "nt" else "clear")

#--Class Selection---#
def choose_class():
    class_choices = {
        "A": Warrior(),
        "B": Hero(),
        "C": Astrologer(),
        "D": Prophet()
    }
    selected_class = None
    confirmation = False

    while not confirmation:
    os.system("cls" if os.name == "nt" else "clear")
    print("\n===================")
    print("\nChoose Your Class")
    print("\n===================")
    print("1. Select a class to view its attributes.")
    print("2. Choose another class to compare.")
    print("3. Confirm final class choice.")
    print("4. Press 'X' to exit.")
    print("\n===================")

    for key, value in class_choice.items():
        print(f"{key}. {value.__class__.__name__}")
    
    choice = input("\nEnter you choice: ").strip().upper()
    
    if choice in class_choices:
        selected_class = class_choices[choice]
        os.system("cls" if os.name == "nt" else "clear")
        selected_class.display_stats()
        elected_class.display_equipment()

        #confirmation after showing attributes
        confirm = input("\nWould you list to chooce this class? (Y/N): ").strip().upper()
        if confirm == "Y":
            os.system("cls" if os.name == "nt" else "clear")
            print(f"\nYou have locked in {selected_class.__class__.__name__} class. Your journey begins...\n")
            return selected_class
        elif confirm == "N":
            print("\nReturning to class selection...\n")
            time.sleep(3)
        else:
            print("\nInvalid input. Returning to class selection...\n")
        
        elif choice == "X":
        print("\nExiting game. Goodbye, Tarnished\n")
        return None
        else:
        print("\nInvalid choice. Please try again.")
    return class_choices[selected_class]

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

if __name__ == "__main__":
    play_cutscene()
    chosen_class = choose_class()

    if chosen_class:
        print(f"\nYou are now a {chosen_class.__class__.__name__}. Prepare to walk the path of the Elden Lord...\n")
        time.sleep(3)
        
        
        #add starting equipment to inventory
        player_inventory["weapons"].extend(chosen_class.weapons) #add weapons
        player_inventory["armor"].extend(chosen_class.armor.values())#add armor
        player_inventory["talisman"] = [] #will be empty starting off

        #equip starting gear
        equipped_items["weapon"] = chosen_class.weapons[0] if chosen_class.weapons else None
        equipped_items["armor"] = chosen_class.armor.copy() #equip all armor
        equipped_items["shield"] = chosen_class.shield if hasattr(chosen_class, "shield") else None

        player = Player("Tarnished", vigor=chosen_class.vigor, endurance=chosen_class.endurance, mind=chosen_class.mind,)

        wake_up_in_cave()
        print("\nPress Enter to move forward...")
        input()
        encounter_skeleton()
        
player_inventory = {
    "weapons": [],
    "armor": [],
    "talismans": [],
    "potions": {
        "Healing Potion": 3,
        "Mana Potion": 1
    },
    "items": []  #category to store loot drops
}

#Stored equipped items
equipped_items = {
    "weapon": None,
    "armor": None,
    "talisman": None,
}

def add_to_inventory(category, item_name, quantity=1):
    if category == "potions":
        if item_name in player_inventory["potions"]:
            player_inventory["potions"][item_name] += quantity
        else:
            player_inventory["potions"][item_name ] = quantity
    else:
        if item_name not in player_inventory[category]:
            player_inventory[category].append(item_name)
    print(f"{item_name} has been added to your {category} inventory")
        
              
         
