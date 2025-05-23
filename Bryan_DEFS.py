def display_inventory():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n========== Player Inventory ===========\n")

        # Weapons
        print(" Weapons:")
        if player_inventory["weapons"]:
            for i, weapon in enumerate(player_inventory["weapons"], 1):
                print(f"  {i}.  {weapon}")
        else:
            print("   (No weapons available)")

        # Armor
        print("\n Armor:")
        if player_inventory["armor"]:
            for i, armor in enumerate(player_inventory["armor"], 1):
                print(f"  {i}. {armor}")
        else:
            print("  (No armor available)")

        # Talismans
        print("\n Talismans:")
        if player_inventory["talismans"]:
            for i, talisman in enumerate(player_inventory["talismans"], 1):
                print(f"  {i}. {talisman}")
        else:
            print("  (No talismans available)")

        # Potions
        print("\n Potions:")
        if player_inventory["potions"]:
            for i, (potion, quantity) in enumerate(player_inventory["potions"].items(), 1):
                print(f"  {i}. {potion} - {quantity} left")
        else:
            print("  (No potions available)")

        print("\n========= Equipped Items ==========")
        for category, item in equipped_items.items():
            print(f"{category.capitalize()}: {item if item else '(None)'}")

        # Select an option
        print("\n(1) Equip Weapon")
        print("(2) Equip Armor")
        print("(3) Equip Talisman")
        print("(4) Use Potion")
        print("(5) Exit Inventory")

        def equip_item(category):
            if not player_inventory[category]:
                print("\nYou have no items in this category.")
                time.sleep(2)
                return
            os.system("cls" if os.name == "nt" else "clear")
            print(f"\nSelect a {category[:-1]} to equip:\n")

            for i, item in enumerate(player_inventory[category], 1):
                print(f"  {i}.  {item}")

            choice = input("\nEnter the number of the item to equip: ").strip()

            if choice.isdigit():
                choice = int(choice) - 1
                if 0 <= choice < len(player_inventory[category]):
                    equipped_items[category[:-1]] = player_inventory[category][choice]
                    print(f"\nYou have equipped {player_inventory[category][choice]}.")
                else:
                    print("\nInvalid Choice.")
            else:
                print("\nInvalid input.")
            time.sleep(2)

        def use_potion():
            if not player_inventory["potions"]:
                print("\nYou have no potions left.")
                time.sleep(2)
                return
            os.system("cls" if os.name == "nt" else "clear")
            print("\nSelect a potion to use:\n")

            potions_list = list(player_inventory["potions"].items())
            for i, (potion, quantity) in enumerate(potions_list, 1):
                print(f"  {i}. {potion} - {quantity} left")

            choice = input("\nEnter the number of the potion to use: ").strip()

            if choice.isdigit():
                choice = int(choice) - 1
                if 0 <= choice < len(potions_list):
                    potion_name = potions_list[choice][0]
                    player_inventory["potions"][potion_name] -= 1

                    if player_inventory["potions"][potion_name] == 0:
                        del player_inventory["potions"][potion_name]
                    print(f"\nYou use {potion_name}.")
                else:
                    print("\nInvalid choice.")
            else:
                print("\nInvalid input.")

            time.sleep(2)

        choice = input("\nSelect an option: ").strip()
        if choice == "1":
            equip_item("weapons")
        elif choice == "2":
            equip_item("armor")
        elif choice == "3":
            equip_item("talismans") 
        elif choice == "4":
            use_potion()
        elif choice == "5":
            break
        else:
            print("\nInvalid choice, try again.")
            time.sleep(1)
            
            
def apply_talisman_effect():
    """Applies the equipped talisman's effect to the player."""
    if player.equipped_talisman:
        effect = talismans[player.equipped_talisman]["effect"]
        
        if "Stamina Recovery" in effect:
            player.stamina_regen_rate = 10  
        elif "Damage to Charged Attacks" in effect:
            player.attack_bonus = 1.15  
        elif "Restores HP" in effect:
            player.hp_regen = 1  
            
            
def castle_ruins():
    """Handles entry into Castle Ruins and triggers an ambush."""
    os.system("cls" if os.name == "nt" else "clear")
    print("\nYou step into the Castle Ruins.")
    print("There is an uneasy feeling in the air...")
    input("\nPress Enter to continue...")

    # Enemy pool for Castle Ruins (all non-boss enemies)
    enemy_pool = [Soldier(), Bandit(), Footman(), Knight()]
    enemy = random.choice(enemy_pool)  # Random enemy selection

    # Show a brief message before the ambush
    os.system("cls" if os.name == "nt" else "clear")
    print(f"\nAs you proceed, {enemy.name} ambushes you!")
    input("\nPress Enter to fight...")

    # Transition to combat
    encounter_enemy(enemy)

    # **If Player Dies in Battle, Return to Site of Grace**
    if player.hp <= 0:
        print("\nYour vision fades to black... You have been defeated.")
        input("\nPress Enter to return to the Light of Grace...")
        light_of_grace()  # **Send player back**
        return  # **Exit function to prevent further execution**

    # If the player wins, reward runes and drop loot
    if enemy.is_defeated():
        print(f"\nThe {enemy.name} collapses. Enemy Slain.")
        player.runes += 200  # Earn 200 runes
        print("\nYou gained 200 runes!")

        # Check for loot drop
        loot = enemy.drop_loot()
        if loot:
            print(f"You found a {loot}!")

        print("\nA voice in your mind whispers: 'Return to the Light of Grace to grow stronger...'")
        
        while True:
            print("\nWhat would you like to do?")
            print("[1] Return to the Site of Grace (Recommended)")
            print("[2] Continue Exploring")
            print("[3] Select a Different Area")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                print("\nYou return to the Light of Grace to recover and upgrade.")
                light_of_grace()  
                return
            elif choice == "2":
                print("\nYou remain in the field, ready for your next challenge.")
                leave_church()  
                return
            elif choice == "3":
                print("\nYou look around, deciding where to go next...")
                leave_church()  # **Go back to area selection**
                return
            else:
                print("\nInvalid option. Try again.")  
            #testing_updates 
            #test4
                     
            

def wake_up_in_cave():
    cave_text = [
        "Darkness surrounds you...",
        "A faint flickering light barely illuminates the damp walls of the cave.",
        "The air is cold, and the distant echoes of dripping water fill the silence."
        "You push yourself up from the ground, your body aching from a long slumber.",
        "Your journey begins here..."
    ]

    fade_in_text(cave_text, delay=2)
    input("\nPress Enter to stand up...")
    os.system("cls" if os.name == "nt" else "clear")

    print("You push yourself up, shaking off the numbness. The path ahead is uncertain, but you have no choice but to move forward.")

    print(" Before moving on, you must check your inventory")
    print(" **Press 'I' to open your inventory.**")
    

    while True:
        choice = input("\n> ").strip().upper()
        if choice == "I":
            display_inventory()
            break
        else:
            print("Invalid choice. Press I to check your inventory")

def evaluate_dodge(dodge_time, attack_damage):
    """Determines the outcome of the dodge based on reaction timing."""
    if dodge_time is None:
        damage_taken = attack_damage
        result = f"You failed to dodge! You take {damage_taken} damage."
    elif 0.00 <= dodge_time <= 0.50:        
        damage_taken = attack_damage // 2
        result = "Early Dodge! You take {damage_taken} damage."
    elif 0.51 <= dodge_time <= 1.00:
        damage_taken = 0
        result = f"Perfect Dodge! No damage taken."
    elif 1.01 <= dodge_time <= 1.50:
        damage_taken = attack_damage
        result = f"Late Dodge! You take {damage_taken} damage."
    else:
        damage_taken = attack_damage
        result = "You failed to react in time! Full damage taken."

    print(result)
    return damage_taken        
        
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
            

def fade_in_text(text, delay=3):
    os.system("cls" if os.name == "nt" else "clear")
    full_text = ""
    for line in text:
        full_text += line +"\n"
        os.system("cls" if os.name == "nt" else "clear")
        print(full_text)
        time.sleep(delay)            
            

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

class Player:
    def __init__(self, name="Tarnished", vigor=10, endurance=10, mind=10, strength=10, dexterity=10, intelligence=10, faith=10, arcane=10):
        self.name = name
        self.vigor = vigor  # Determines HP
        self.endurance = endurance  # Determines Stamina
        self.mind = mind  # Determines FP
        self.strength = strength  # Affects heavy weapons
        self.dexterity = dexterity  # Affects light weapons
        self.intelligence = intelligence  # Affects magic attack (Sorceries)
        self.faith = faith  # Affects healing & magic defense (Incantations)
        self.arcane = arcane  # Affects item discovery & resistances

        self.hp = self.vigor * 10
        self.stamina = self.endurance * 10
        self.fp = self.mind * 10

        self.max_hp = self.hp
        self.max_stamina = self.stamina
        self.max_fp = self.fp

        self.runes = 0  # Currency for upgrades
        self.weapon_level = 0  # Weapons start at +0
        self.smithing_stones = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}  # Tracks Smithing Stones
        self.fled_successfully = False
        
        # Stamina Regeneration Variables
        self.stamina_regen_time = 3  # Time before stamina regenerates
        self.stamina_regen_rate = 5  # Amount restored per tick
        self.last_action_time = time.time()
        self.inventory = {  
            "health_potion": 3,  
            "fp_potion": 1  
        }
        self.successful_hits = 0  # Tracks consecutive successful hits
        self.took_damage = False  # Resets when taking damage

        # Blocking Mechanic
        self.is_blocking = False  

    def block(self, enemy):
        """Reduces incoming damage and regenerates stamina when blocking."""
        print("\nYou raise your shield and brace for impact.")

        block_multiplier = 0.3  # Blocks 70% of incoming damage
        stamina_regen = 10  # Amount of stamina restored

        attack_damage, attack_message = enemy.attack()
        print(f"\n{attack_message}")  

        reduced_damage = int(attack_damage * block_multiplier)
        self.hp -= reduced_damage  
        self.stamina = min(self.stamina + stamina_regen, self.max_stamina)

        print(f"\nYou blocked the attack! You took {reduced_damage} damage.")
        print(f"Blocking restored some stamina (+{stamina_regen} Stamina).")
        print(f"Stamina: {self.stamina}/{self.max_stamina}")
    
        input("\nPress Enter to continue...")  # Wait for player input before moving forward
        return reduced_damage


    def reduce_stamina(self, amount):
        """Reduces stamina when performing actions."""
        if self.stamina >= amount:
            self.stamina -= amount
            self.last_action_time = time.time()
            return True  # Successful stamina reduction
        else:
            print("\nNot enough stamina!")
            return False  # Attack fails

    def regenerate_stamina(self):
        """Regenerates stamina if no action has been taken for 3 seconds."""
        if time.time() - self.last_action_time >= self.stamina_regen_time:
            self.stamina = min(self.stamina + self.stamina_regen_rate, self.max_stamina)

    def display_bars(self):
        """Displays player's stats."""
        print(f"HP: [{self.hp}/{self.max_hp}]")
        print(f"Stamina: [{self.stamina}/{self.max_stamina}]")
        print(f"FP: [{self.fp}/{self.max_fp}]")

    def attack(self, attack_type):
        """Performs an attack, consuming stamina based on type, and returns damage and a message."""
        base_damage = 0
        stamina_cost = 0

        if attack_type == "light":
            base_damage = 15
            stamina_cost = 10
            attack_message = "You performed a Light Attack"

        elif attack_type == "heavy":
            base_damage = 50
            stamina_cost = 20
            attack_message = "You performed a Heavy Attack"

        else:
            return 0, "Invalid attack type."

    # Check stamina before attacking
        if self.stamina < stamina_cost:
            return 0, "Not enough stamina to attack."

    # Reduce stamina
        self.reduce_stamina(stamina_cost)

    # **CRITICAL HIT CHECK** - 4th attack is a critical hit
        if self.successful_hits == 3 and not self.took_damage:
            crit_damage = base_damage * 2  # Critical hits deal double damage
            self.successful_hits = 0  # Reset counter after critical hit
            return crit_damage, "**CRITICAL HIT!** " + attack_message

    # Otherwise, apply normal damage
        self.successful_hits += 1
        return base_damage, attack_message

    def equip_weapon(self, weapon_name):
        """Equips a new weapon from the weapons dictionary."""
        if weapon_name in weapons:
            self.weapon = weapons[weapon_name]
            print(f"\n[DEBUG] Equipped Weapon: {self.weapon}")  # Debugging statement
        else:
            print("\nInvalid weapon name.")

    def equip_armor(self, armor_name):
        """Equips new armor from the armor dictionary."""
        if armor_name in armor:
            self.armor = armor[armor_name]
            print(f"\n[DEBUG] Equipped Armor: {self.armor}")  # Debugging statement
        else:
            print("\nInvalid armor name.")
    
    def display_equipped(self):
        """Displays currently equipped weapon and armor."""
        weapon_name = self.weapon["name"] if self.weapon else "None"
        armor_name = self.armor["name"] if self.armor else "None"

        print("\n--- Player Equipment ---")
        print(f"Weapon: {weapon_name}")
        print(f"Armor: {armor_name}")
    

    def use_potion(self):
        """Uses a health potion if available."""
        if self.inventory["health_potion"] > 0:
            self.inventory["health_potion"] -= 1
            self.hp = min(self.hp + self.max_hp, self.max_hp)  
            print("\nYou drink a health potion and feel reinvigorated!")
            return True
        else:
            print("\nYou're out of health potions!")
            return False
    def take_damage(self, amount):
        """Reduces HP and resets successful attack streak if hit."""
        self.hp = max(0, self.hp - amount)
        self.took_damage = True  # Player was hit, reset critical hit counter
        self.successful_hits = 0  # Reset streak

        print(f"\n{self.name} takes {amount} damage! HP now: [{self.hp}/{self.max_hp}]")

    # Check if player is dead
        if self.hp == 0:
            print("\nYou have fallen in battle...")
            exit()  # Ends the game when HP reaches 0

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
        
def detect_dodge():
    """Waits for the player to press Enter within the dodge window and records reaction time."""
    start_time = time.time()
    dodge_window = 1.5

    print("\nPress [Enter] to dodge!")

    while time.time() - start_time < dodge_window:
        elapsed_time = time.time() - start_time
        remaining_time = max(0, dodge_window - elapsed_time)

        print(f"\r{remaining_time:.2f} seconds left! Press [Enter] to dodge!  ", end="", flush=True)

        if sys.platform == "win32":
            import msvcrt
            if msvcrt.kbhit():
                key = msvcrt.getch().decode("utf-8")
                if key == "\r":
                    return elapsed_time
        else:
            i, o, e = select.select([sys.stdin], [], [], 0.1)
            if i:
                key = sys.stdin.read(1)
                if key == "\n":
                    return elapsed_time

    print("\nYou failed to dodge in time!")
    return None

def evaluate_dodge(dodge_time, attack_damage):
    """Determines the outcome of the dodge based on reaction timing."""
    if dodge_time is None:
        damage_taken = attack_damage
        result = f"You failed to dodge! You take {damage_taken} damage."
    elif 0.00 <= dodge_time <= 0.50:        
        damage_taken = attack_damage // 2
        result = "Early Dodge! You take {damage_taken} damage."
    elif 0.51 <= dodge_time <= 1.00:
        damage_taken = 0
        result = f"Perfect Dodge! No damage taken."
    elif 1.01 <= dodge_time <= 1.50:
        damage_taken = attack_damage
        result = f"Late Dodge! You take {damage_taken} damage."
    else:
        damage_taken = attack_damage
        result = "You failed to react in time! Full damage taken."

    print(result)
    return damage_taken