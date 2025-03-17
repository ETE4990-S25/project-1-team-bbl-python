#weapon_data.py

weapons = {
    "Scimitar":{
        "base_damage": 45,
        "upgrade_scaling": 5,
        "requirements": {"Strength": 10, "Dexterity": 12},
        "weight": 4.5,
        "critical_muiltiplier": 1.2,
        "attack_speed": "fast",
        "special_effects": None
    },
    "Battle Axe": {
        "base_damage": 55,
        "upgrade_scaling": 6,
        "requirements": {"Strength": 16, "Dexterity": 9},
        "weight": 7.0,
        "critical_muiltiplier": 1.1,
        "attack_speed": "medium",
        "special_effects": None
    },

    "Astrologer's Staff": {
        "base_damage": 20,
        "upgrade_scaling": 4,
        "requirements": {"Intelligence": 16},
        "weight": 3.0,
        "critical_muiltiplier": 1.0,
        "attack_speed": "slow",
        "special_effects": "boosts sorcery spells"

    },

    "Short Sword": {
        "base_damage": 40,
        "upgrade_scaling": 4,
        "requirements": {"Strength": 8, "Dexterity": 10},
        "weight": 4.0,
        "critical_muiltiplier": 1.1,
        "attack_speed": "medium",
        "special_effects": "None"
    },

    "Short Spear": {
        "base_damage": 40,
        "upgrade_scaling": 4,
        "requirements": {"Strength": 11, "Dexterity": 10},
        "weight": 5.5,
        "critical_muiltiplier": 1.3,
        "attack_speed": "medium",
        "special_effects": "long reach"
    },
    "Finger Seal": {
        "base_damage": 15,
        "upgrade_scaling": 3,
        "requirements": {"Faith": 16},
        "weight": 2.5,
        "critical_muiltiplier": 1.0,
        "attack_speed": "slow",
        "special_effects": "boosts holy spells"

    },

    "Dagger": {
       "base_damage": 35,
        "upgrade_scaling": 4,
        "requirements": {"Strength": 8, "Dexterity": 12},
        "weight": 2.0,
        "critical_muiltiplier": 1.5,
        "attack_speed": "very fast",
        "special_effects": "high critical hits" 
    },

    "Knight's Greatsword": {
        "base_damage": 75,
        "upgrade_scaling": 9,
        "requirements": {"Strength": 18, "Dexterity": 12},
        "weight": 10,
        "critical_muiltiplier": 1.1,
        "attack_speed": "slow",
        "special_effects": "None"
    },

    "Spear": {
        "base_damage": 45,
        "upgrade_scaling": 5,
        "requirements": {"Strength": 12, "Dexterity": 14},
        "weight": 6.0,
        "critical_multiplier": 1.3,
        "attack_speed": "medium",
        "special_effects": "long reach"
    },

    "Golden Halberd": {
        "base_damage": 90,
        "upgrade_scaling": 10,
        "requirements": {"Strength": 20, "Dexterity": 14, "Faith":12},
        "weight": 13.0,
        "critical_multiplier": 1.1,
        "attack_speed": "slow",
        "special_effects": "slight holy damage"
    }
    
}