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
            
            
            
            
            

        
        
        
            
            
            
