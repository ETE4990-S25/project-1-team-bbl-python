from weapon_data import weapons
from armor_data import armor
from talismans_data import talismans
from enemy_data import Bandit 
from enemy_data import Footman
from enemy_data import Knight
from enemy_data import Soldier
from enemy_data import TreeSentinel
from enemy_data import Skeleton
import os
import random
import time
import sys
import select

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

def open_inventory():
    """Allows the player to equip a talisman from their inventory."""
    os.system("cls" if os.name == "nt" else "clear")

    if not player_inventory["talismans"]:
        print("\nYour inventory is empty. You have no talismans to equip.")
        input("\nPress Enter to return to the Light of Grace...")
        return

    print("\nYour Inventory - Talismans:")
    for i, talisman in enumerate(player_inventory["talismans"], 1):
        print(f"{i}. {talisman} - {talismans[talisman]['effect']}")

    print("\n5. Unequip current talisman")
    print("6. Return to Light of Grace")

    choice = input("\nSelect a talisman to equip (1-5) or return: ").strip()

    if choice in ["1", "2", "3"] and int(choice) <= len(player_inventory["talismans"]):
        selected_talisman = player_inventory["talismans"][int(choice) - 1]
        player.equipped_talisman = selected_talisman
        print(f"\nYou have equipped the {selected_talisman}.")
        apply_talisman_effect()  # Apply the talisman's effect
        input("\nPress Enter to return to the Light of Grace...")

    elif choice == "5":
        player.equipped_talisman = None
        print("\nYou have unequipped your talisman.")
        input("\nPress Enter to return to the Light of Grace...")

    elif choice == "6":
        return  

    else:
        print("\nInvalid choice. Try again.")
        input("\nPress Enter to continue...")
        open_inventory()  

def dungeons():
    """Handles the randomized dungeon chest selection."""
    os.system("cls" if os.name == "nt" else "clear")
    print("\nYou enter the dimly lit dungeon, the air damp and heavy with mystery.")
    print("Before you, four ancient chests rest in the gloom, their contents unknown.")

    # Assign talismans to specific labels and randomize chest positions
    talisman_keys = list(talismans.keys())
    random.shuffle(talisman_keys)  # Shuffle the actual talismans

    chest_contents = ["trap"] + talisman_keys  # 1 trap + 3 randomized talismans
    random.shuffle(chest_contents)  # Shuffle their placement in the chests

    opened_chests = set()  # Track which chests have been opened

    while True:
        print("\nChests: [1] [2] [3] [4]")
        choice = input("\nChoose a chest to open (1-4) or type 'leave' to return: ").strip().lower()

        if choice == "leave":
            print("\nYou step away from the chests and return to the dungeon entrance.")
            input("\nPress Enter to continue...")
            leave_church()  # Return to area selection instead of quitting
            return  

        if choice not in ["1", "2", "3", "4"]:
            print("\nInvalid choice. Choose a chest between 1 and 4.")
            continue

        chest_number = int(choice) - 1

        if chest_number in opened_chests:
            print("\nYou've already opened this chest. Choose another.")
            continue

        opened_chests.add(chest_number)
        result = chest_contents[chest_number]

        if result == "trap":
            print("\nAs you lift the lid, a sudden burst of light engulfs you!")
            print("A powerful force pulls you away...")
            input("\nPress Enter to continue...")
            encounter_tree_sentinel()  # Triggers boss battle
            return
        
        else:
            talisman_key = result  # The shuffled talisman key
            print(f"\nYou open the chest and find the **{talisman_key}**!")
            print(f"\n{talismans[talisman_key]['description']}")
            player_inventory["talismans"].append(talisman_key)
            print("\nThe talisman has been added to your inventory.")

        if len(opened_chests) == 4:
            print("\nYou have opened all the chests. There's nothing left here.")
            input("\nPress Enter to return to the dungeon entrance...")
            leave_church()  # Return to area selection
            return


def tree_lined_oasis():
    """Handles entry into the Tree-Lined Oasis and sets up the encounter with the Tree Sentinel."""
    os.system("cls" if os.name == "nt" else "clear")
    
    print("\nYou step into the Tree-Lined Oasis.")
    print("The air is still, too peaceful. The only sound is the distant rustling of leaves.")
    print("Ahead, golden armor catches the light. A knight—silent, unmoving—watches.")
    print("No roar. No battle cry. Just quiet, suffocating tension.")
    print("The ground trembles beneath you, as if warning you to turn back.")
    
    print("\nA message lingers in your mind:")
    print("   'An impossible fight lies ahead. Do you continue?'")

    while True:
        print("\n[1] Face the Tree Sentinel.")
        print("[2] Return to the Site of Grace.")
        
        choice = input("\nWhat will you do? ").strip()

        if choice == "1":
            print("\nYou step forward. The Tree Sentinel lowers his halberd.")
            print("The silence breaks.")
            input("\nPress Enter to face him...")
            encounter_tree_sentinel()
            break
        
        elif choice == "2":
            print("\nYou hesitate, then turn back. Some battles are not meant to be fought yet.")
            input("\nPress Enter to return to the Site of Grace...")
            light_of_grace()
            break

        else:
            print("\nIndecision will not save you. Choose.")


def encounter_tree_sentinel():
    """Handles the battle against the Tree Sentinel, ensuring proper mechanics."""
    global player  
    os.system("cls" if os.name == "nt" else "clear")

    print("\nThe Tree Sentinel stands in your path, its golden armor gleaming under the sun.")
    print("Without hesitation, it prepares to strike.")

    input("\nPress Enter to face the Tree Sentinel...")

    tree_sentinel = TreeSentinel()

    while tree_sentinel.hp > 0 and player.hp > 0:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\nBoss: {tree_sentinel.name} | HP: [{tree_sentinel.hp}/{tree_sentinel.max_hp}]")
        print(f"Your HP: [{player.hp}/{player.max_hp}] | Stamina: [{player.stamina}/{player.max_stamina}]")

        print("\nActions: [1] Light Attack | [2] Heavy Attack | [3] Block | [4] Use Potion | [5] Flee")
        choice = input("\nSelect an action: ").strip()

        if choice == "1":
            damage, message = player.attack("light")
            print(f"\n{message}")  
            tree_sentinel.take_damage(damage, "light")

        elif choice == "2":
            damage, message = player.attack("heavy")
            print(f"\n{message}")  
            tree_sentinel.take_damage(damage, "heavy")

        elif choice == "3":  # Block
            print("\nYou raise your shield and brace for impact.")
            time.sleep(1)
            reduced_damage = player.block(tree_sentinel)
            print(f"\nYou blocked the attack and took {reduced_damage} damage.")
            input("\nPress Enter to continue...")
            continue  

        elif choice == "4":  # Use Potion
            if player.use_potion():
                print(f"\nYou now have {player.hp}/{player.max_hp} HP remaining.")
            else:
                print("\nNo potions left!")
            input("\nPress Enter to continue...")
            continue  

        elif choice == "5":  # **Flee Always Fails & Deals Full Damage**
            print("\nYou attempt to flee, but the Tree Sentinel charges forward—ESCAPE IS IMPOSSIBLE!")
            attack_damage, attack_message = tree_sentinel.attack()
            print(attack_message)
            player.hp -= attack_damage  # Full damage taken
            print(f"\nYou take {attack_damage} damage as punishment for trying to flee!")
            input("\nPress Enter to continue...")
            continue  

        # **Tree Sentinel's Turn (You Can Still Dodge Normally)**
        if tree_sentinel.hp > 0:
            print("\nThe Tree Sentinel prepares to strike!")
            attack_damage, attack_message = tree_sentinel.attack()
            print(attack_message)

            dodge_time = detect_dodge()
            damage_taken = evaluate_dodge(dodge_time, attack_damage)

            if damage_taken == 0:
                print("\nYou evade the attack with perfect timing!")
            else:
                print(f"\nThe Tree Sentinel's attack lands! You take {damage_taken} damage.")
                player.hp -= damage_taken

        # **FORCE PLAYER TO SITE OF GRACE ON DEATH**
        if player.hp <= 0:
            print("\nYou have been defeated... The world fades to black.")
            input("\nPress Enter to return to the Light of Grace...")
            light_of_grace()  # **FORCE player to Site of Grace**
            return  # **EXIT IMMEDIATELY after death**

        input("\nPress Enter to continue...")

    # **If Player Wins**
    if tree_sentinel.hp <= 0:
        print("\nThe Tree Sentinel collapses, its massive form crashing to the ground.")
        print("\nYou have defeated the Tree Sentinel!")
        print("\nYou gained 1000 runes!")
        player.runes += 1000

        loot = tree_sentinel.drop_loot()
        if loot:
            print(f"You found a {loot}!")

        print("\nThe overwhelming silence returns... You should return to the Light of Grace.")

        # **Post-Fight Decision Menu**
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
                leave_church()  
                return
            else:
                print("\nInvalid option. Try again.")


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

def encounter_enemy(enemy):
    """Handles the combat encounter after ambush, ensuring proper mechanics."""
    global player  

    os.system("cls" if os.name == "nt" else "clear")

    # Reset damage tracking
    player.successful_hits = 0  
    player.took_damage = False  

    while enemy.hp > 0 and player.hp > 0:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\nEnemy: {enemy.name} | HP: [{enemy.hp}/{enemy.max_hp}]")
        print(f"Your HP: [{player.hp}/{player.max_hp}] | Stamina: [{player.stamina}/{player.max_stamina}]")

        print("\nActions: [1] Light Attack | [2] Heavy Attack | [3] Block | [4] Use Potion | [5] Flee")
        action = input("\nSelect an action: ").strip()

        if action == "1":
            damage, message = player.attack("light")
            print(f"\n{message}")  
            enemy.take_damage(damage, "light")
            player.successful_hits += 1  

        elif action == "2":
            damage, message = player.attack("heavy")
            print(f"\n{message}")  
            enemy.take_damage(damage, "heavy")
            player.successful_hits += 1  

        elif action == "3":  # Block
            print("\nYou raise your shield and brace for impact.")
            time.sleep(1)  
            reduced_damage = player.block(enemy)
            print(f"\nYou blocked the attack and took {reduced_damage} damage.")
            input("\nPress Enter to continue...")
            continue  # Skips enemy attack turn

        elif action == "4":  # Use Potion
            if player.use_potion():
                print(f"\nYou now have {player.hp}/{player.max_hp} HP remaining.")
            else:
                print("\nNo potions left!")
            input("\nPress Enter to continue...")
            continue  

        elif action == "5":  # **Flee Always Fails & Deals Full Damage**
            print("\nYou attempt to flee, but the enemy lunges forward—ESCAPE IS IMPOSSIBLE!")
            attack_damage, attack_message = enemy.attack()
            print(attack_message)
            player.hp -= attack_damage  # Full damage taken
            print(f"\nYou take {attack_damage} damage as punishment for trying to flee!")
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
                print("\nYou evade the attack with perfect timing!")
            else:
                print(f"\nThe enemy's attack lands! You take {damage_taken} damage.")
                player.hp -= damage_taken

        # **If Player Dies, Force Them to the Site of Grace**
        if player.hp <= 0:
            print("\nYou have been defeated... The world fades to black.")
            input("\nPress Enter to return to the Light of Grace...")
            light_of_grace()  # **Forces a respawn instead of exiting**
            return  # **Ensures function does not continue**

        input("\nPress Enter to continue...")

    # **If Enemy is Defeated**
    if enemy.hp <= 0:
        print(f"\nThe {enemy.name} collapses. Enemy Slain.")
        print("\nYou gained 200 runes!")
        player.runes += 200

        loot = enemy.drop_loot()
        if loot:
            print(f"You found a {loot}!")
            player_inventory.setdefault("items", []).append(loot)  

        print("\nThe item has been added to your inventory.")

        # **Post-Fight Decision Menu**
        while True:
            print("\nWhat would you like to do?")
            print("[1] Return to the Site of Grace (Recommended)")
            print("[2] Continue Exploring")
            print("[3] Select a Different Area")
            print("[4] Go to the Church of Marika")

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
            elif choice == "4":
                print("\nYou return to the Church of Marika.")
                church_of_marika()
                return
            else:
                print("\nInvalid option. Try again.")

def light_of_grace():
    """Handles healing, upgrades, and inventory access."""
    os.system("cls" if os.name == "nt" else "clear")
    print("\nYou rest at the Light of Grace.")
    print("Your health, stamina, and FP are fully restored.")

    # Fully restore the player's stats
    player.hp = player.max_hp
    player.stamina = player.max_stamina
    player.fp = player.max_fp

    print("\n[All stats restored.]")

    while True:
        os.system("cls" if os.name == "nt" else "clear")  
        print("\nYou are at the Light of Grace. What would you like to do?")
        print("1. Upgrade Attributes (Cost: 100 Runes)")
        print("2. Open Inventory (Equip Weapons, Armor, Talismans, Use Potions)")
        print("3. Exit Light of Grace")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            upgrade_attributes()
        elif choice == "2":
            display_inventory() 
        elif choice == "3":
            print("\nYou step away from the Light of Grace, ready to continue your journey.")
            leave_church()  # Ensures the player is correctly sent to area selection
            return  # Properly exits the function
        else:
            print("\nInvalid option. Try again.")
            input("\nPress Enter to continue...")

  

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
        print("8. Arcane (Increases item discovery & resistances)")
        print("9. Return")

        choice = input("\nSelect an option: ").strip()

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
                    player.max_stamina = player.endurance * 10
                    print("\nYour Endurance has increased.")
                    print(f"New Endurance: {player.endurance} | New Max Stamina: {player.max_stamina}")

                elif choice == "3":
                    player.mind += 1
                    player.max_fp = player.mind * 10
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
                    print(f"New Intelligence: {player.intelligence}")

                elif choice == "7":
                    player.faith += 1
                    print("\nYour Faith has increased.")
                    print(f"New Faith: {player.faith}")

                elif choice == "8":
                    player.arcane += 1
                    print("\nYour Arcane has increased.")
                    print(f"New Arcane: {player.arcane}")

                print(f"\nRemaining Runes: {player.runes}")
                input("\nPress Enter to continue...")  

            else:
                print("\nNot enough runes.")
                input("\nPress Enter to continue...")  

        elif choice == "9":
            break  

        else:
            print("\nInvalid option. Try again.")
            input("\nPress Enter to continue...")  

def merchant_kale():
    """Handles interactions with Merchant Kale."""
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\nYou approach Merchant Kale.")
        print("\nWelcome, traveler! What would you like to buy?")
        print("\n1. Smithing Stone (+1) - 100 Runes")
        print("2. Smithing Stone (+2) - 100 Runes")
        print("3. Smithing Stone (+3) - 100 Runes")
        print("4. Smithing Stone (+4) - 100 Runes")
        print("5. Smithing Stone (+5) - 100 Runes")
        print("6. Exit Merchant Kale")

        choice = input("\nSelect an option: ").strip()

        if choice in ["1", "2", "3", "4", "5"]:
            stone_level = int(choice)  
            if player.runes >= 100:
                player.runes -= 100  
                player.smithing_stones[stone_level] += 1  
                print(f"\nYou purchased a Smithing Stone (+{stone_level}).")
                print(f"Remaining Runes: {player.runes}")
            else:
                print("\nNot enough runes.")
            input("\nPress Enter to continue...")

        elif choice == "6":
            os.system("cls" if os.name == "nt" else "clear")  
            break  

        else:
            print("\nInvalid option. Try again.")
            input("\nPress Enter to continue...")

def smithing_table():
    """Handles weapon upgrades."""
    os.system("cls" if os.name == "nt" else "clear")
    print("\nYou stand before the Smithing Table.")
    
    while True:
        print("\nYour weapon is currently at level +", player.weapon_level)
        print("1. Upgrade Weapon (+1) (Cost: 100 Runes)")
        print("2. Return to the Church")
        
        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            if player.runes >= 100 and player.weapon_level < 5:
                if player.smithing_stones[player.weapon_level + 1] > 0:
                    player.runes -= 100
                    player.smithing_stones[player.weapon_level + 1] -= 1
                    player.weapon_level += 1
                    print(f"\nYour weapon is now +{player.weapon_level}!")
                else:
                    print("\nYou don't have a Smithing Stone for this upgrade!")
            elif player.weapon_level >= 5:
                print("\nYour weapon is already at max level (+5)!")
            else:
                print("\nNot enough runes!")
        elif choice == "2":
            break
        else:
            print("\nInvalid option. Try again.")

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
            castle_ruins()  # calls the function
            return  # Ensure the function exits after choosing a location

        elif choice == "2":
            print("\nYou travel to the Tree-Lined Oasis...")
            input("\nPress Enter to continue...")
            os.system("cls" if os.name == "nt" else "clear")
            tree_lined_oasis()  # Assuming this function exists
            return  

        elif choice == "3":
            print("\nYou travel to the Dungeons...")
            input("\nPress Enter to continue...")
            os.system("cls" if os.name == "nt" else "clear")
            dungeons()  # Assuming this function exists
            return  

        else:
            print("\nInvalid option. Try again.")
            input("\nPress Enter to retry...")  # Small pause before retrying


def church_of_marika():
    """Church of Marika main navigation menu."""
    os.system("cls" if os.name == "nt" else "clear")

    print("\nYou arrive at the Church of Marika.")
    print("The Light of Grace glows softly, inviting you to rest.")
    print("Nearby, Merchant Kale watches you curiously, and a Smithing Table sits in the corner.")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Light of Grace (Heal & Upgrade)")
        print("2. Talk to Merchant Kale (Buy Smithing Stones)")
        print("3. Use the Smithing Table (Upgrade Weapons)")
        print("4. Leave the Church")
        
        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            light_of_grace()
        elif choice == "2":
            merchant_kale()
        elif choice == "3":
            smithing_table()
        elif choice == "4":
            leave_church()
            break  # Exit the menu and move forward
        else:
            print("\nInvalid option. Try again.")
def fade_in_text(text, delay=3):
    os.system("cls" if os.name == "nt" else "clear")
    full_text = ""
    for line in text:
        full_text += line +"\n"
        os.system("cls" if os.name == "nt" else "clear")
        print(full_text)
        time.sleep(delay)

def play_cutscene():
    cutscene_text = [
        "The Lands Between...",
        "Once ruled by the Elden Ring, the Golden Order is now no more.",
        "The shattered fragments of the ring are scattered, and the once bountiful Lands Between are now consumed by corruption.",
        "You, the Tarnished, are banished from the Grace of the Golden Order...",
        "And now you are called to rise once again."
    ]
    fade_in_text(cutscene_text)
    time.sleep(2)
    os.system("cls" if os.name =="nt" else "clear")
    
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
def clear_screen():
    os.system("cls" if os.name == "nt" else"clear")

#---Class Selection---#
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

        for key, value in class_choices.items():
            print(f"{key}. {value.__class__.__name__}")

        choice = input("\nEnter your choice: ").strip().upper()

        if choice in class_choices:
            selected_class = class_choices[choice]
            os.system("cls" if os.name == "nt" else "clear")
            selected_class.display_stats()
            selected_class.display_equipment()

            #Confirmation after showing attributes
            confirm = input("\nWould you like to choose this class? (Y/N): ").strip().upper()

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

def open_inventory():
    global player_inventory
    print("\n **Inventory**")
    print("====================")
    print(" Weapons:", player_inventory["weapons"] if player_inventory["weapons"] else "None")
    print(" Armor:", player_inventory["armor"] if player_inventory["armor"] else "None")
    print( "Talismans:", player_inventory["talismans"] if player_inventory["talismans"] else "None")
    print(" Potions:")
    for potion, qty in player_inventory["potions"].items():
        print(f"   -{potion}: {qty}")
    print("====================")
    input("\nPress Enter to close inventory...")
                

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

def encounter_skeleton():
    """Starts the battle sequence against the skeleton with a brief introduction."""
    os.system("cls" if os.name == "nt" else "clear")

    # Skeleton Intro Scene
    print("\nAs you step forward, the air grows cold...")
    time.sleep(1)
    print("\nA chilling presence looms nearby.")
    time.sleep(1)
    print("\nFrom the shadows, bones rattle, and a skeletal warrior emerges!")
    print("\nIts hollow eyes lock onto you as it raises a rusted blade.")
    input("\nPress [Enter] to prepare for battle...")

    # Clear screen before battle starts
    os.system("cls" if os.name == "nt" else "clear")

    skeleton = Skeleton()

    while skeleton.hp > 0 and player.hp > 0:
        os.system("cls" if os.name == "nt" else "clear")

        # Show updated stats
        player.display_bars()
        print(f"\nEnemy: {skeleton.name} | HP: [{skeleton.hp}/{skeleton.max_hp}]")

        print("\nActions: [1] Light Attack | [2] Heavy Attack | [3] Block | [4] Use Potion | [5] Flee | [6] Quit")
        action = input("\nSelect an action: ").strip()

        if action == "6":
            print("\nYou fled from battle.")
            return

        # Handle Attacks
        if action == "1":
            damage, message = player.attack("light")
            print(f"\n{message}")
            skeleton.take_damage(damage, "light")
            time.sleep(1)

        elif action == "2":
            damage, message = player.attack("heavy")
            print(f"\n{message}")
            skeleton.take_damage(damage, "heavy")
            time.sleep(1)

        if skeleton.hp <= 0:
            print("\nThe Skeleton collapses into a pile of bones. Enemy Slain.")
            player.runes += 100  
            print(f"\nYou gained 100 runes! Total Runes: {player.runes}")

            print("\nPress Enter to continue forward...")
            input()
            os.system("cls" if os.name == "nt" else "clear")
            church_of_marika()
            return

        # **Blocking**
        if action == "3":  
            print("\nYou raise your shield and brace for impact.")
            time.sleep(1)  

            reduced_damage = player.block(skeleton)  
            print(f"\nYou blocked the attack and took {reduced_damage} damage.")

            input("\nPress Enter to continue...")
            continue  # Skips the enemy's turn

        # **Using Potion**
        elif action == "4":
            if player.use_potion():
                print(f"\nYou now have {player.hp}/{player.max_hp} HP remaining.")
            else:
                print("\nNo potions left!")
            input("\nPress Enter to continue...")
            continue  

        # **Flee Attempt (Fails 50% of the Time)**
        elif action == "5":
            if random.random() < 0.5:
                print("\nYou successfully flee to the Light of Grace!")
                input("\nPress Enter to continue...")
                light_of_grace()
                return
            else:
                print("\nFailed to flee! The Skeleton slashes at you as you turn your back!")
                attack_damage, attack_message = skeleton.attack()
                print(attack_message)
                player.hp -= attack_damage
                input("\nPress Enter to continue...")
                continue  

        # **Skeleton's Turn (You Can Still Dodge Normally)**
        if skeleton.hp > 0:
            print("\nThe Skeleton prepares to strike!")
            attack_damage, attack_message = skeleton.attack()
            print(attack_message)

            # **Dodge Mechanic Still Works Here**
            dodge_time = detect_dodge()
            damage_taken = evaluate_dodge(dodge_time, attack_damage)

            if damage_taken == 0:
                print("\nYou evade the attack with perfect timing!")
            else:
                print(f"\nThe Skeleton's attack lands! You take {damage_taken} damage.")
                player.hp -= damage_taken

        time.sleep(1.5)

    # **Check if Player Won or Lost**
    if player.hp > 0:
        print("\nThe Skeleton collapses into a pile of bones. Enemy Slain.")
        print("\nPress Enter to continue forward...")
        player.runes += 100  
        print(f"\nYou gained 100 runes! Total Runes: {player.runes}")
        input()  
        os.system("cls" if os.name == "nt" else "clear")
        church_of_marika()
    else:
        print("\nYou died...")
        exit()


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
        




