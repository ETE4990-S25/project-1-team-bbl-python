import random
class Enemy:
    def __init__(self, name, hp, attack_power, defense, weakness, loot_item, drop_rate):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.weakness = weakness
        self.loot_item = loot_item
        self.drop_rate = drop_rate

    def take_damage(self, amount, attack_type):
        """Reduces HP based on incoming damage, factoring in weaknesses and defense."""
        if attack_type == self.weakness:
            amount *= 1.5  # Apply weakness multiplier

        reduced_damage = max(0, amount - self.defense)  # Subtract defense
        self.hp -= reduced_damage  # Reduce HP

        if self.hp < 0:
            self.hp = 0  # Prevent negative HP

        print(f"{self.name} takes {reduced_damage} damage! HP now: {self.hp}/{self.max_hp}")  # Debugging

        return reduced_damage  # Return the final damage applied

    def is_defeated(self):
        """Check if the enemy is defeated."""
        return self.hp <= 0

    def drop_loot(self):
        """Determines if the enemy drops its item based on drop rate"""
        import random
        if random.randint(1, 100) <= self.drop_rate:
            return self.loot_item
        return None
    
class Bandit(Enemy):
    def __init__(self):
        super().__init__(
            name="Bandit",
            hp=100,
            attack_power=15,
            defense=5,
            weakness="fire",
            loot_item="Dagger",
            drop_rate=20
        )
    
    def light_attack(self):
        return (12, "The Bandit slashes quickly with a dagger!")

    def heavy_attack(self):
        return (18, "The Bandit lunges forward and stabs with force!")

    def attack(self):
        """Randomly selects and performs an attack, returning a tuple (damage, message)."""
        return random.choice([self.light_attack(), self.heavy_attack()])
class Footman(Enemy):
    def __init__(self):
        super().__init__(
            name="Footman",
            hp=150,
            attack_power=15,
            defense=8,
            weakness="magic",
            loot_item="Spear",
            drop_rate=20
        )

    def light_attack(self):
        return (15, "The Footman thrusts his spear forward!")

    def heavy_attack(self):
        return (22, "The Footman delivers a powerful overhead stab!")

    def attack(self):
        """Randomly selects and performs an attack, returning (damage, message)."""
        return random.choice([self.light_attack(), self.heavy_attack()])
    
class Skeleton(Enemy):
    def __init__(self):
        super().__init__(
            name="Skeleton",
            hp=50,
            defense=3,
            weakness="blunt",
            attack_power=5,
            loot_item="Bone Shard",
            drop_rate=30
        )
    def light_attack(self):
        return (10, "The Skeleton swings its rusted sword, dealing 10 damage!")
    
    def heavy_attack(self):
        return (18, "The skeleton raises its sword and slashes downward, dealing 18 damage!")
    
    def attack(self):
        return random.choice([self.light_attack(), self.heavy_attack()])
    
class Soldier(Enemy):
    def __init__(self):
        super().__init__(
            name="Soldier",
            hp=200,
            attack_power=25,
            defense=10,
            weakness="lightning",
            loot_item="Short Sword",
            drop_rate=20
        )

    def light_attack(self):
        return (18, "The Soldier swings his short sword swiftly!")

    def heavy_attack(self):
        return (25, "The Soldier raises his sword and slams down with force!")

    def attack(self):
        """Randomly selects and performs an attack, returning (damage, message)."""
        return random.choice([self.light_attack(), self.heavy_attack()])

    
class Knight(Enemy):
    def __init__(self):
        super().__init__(
            name="Knight",
            hp=300,
            attack_power=30,
            defense=15,
            weakness="piercing",
            loot_item="Knight's Greatsword",
            drop_rate=20
        )
    
    def light_attack(self):
        return (22, "The Knight swings his greatsword in a sweeping arc!")

    def heavy_attack(self):
        return (45, "The Knight grips his sword tightly and delivers a crushing downward strike!")

    def attack(self):
        """Randomly selects and performs an attack, returning a tuple (damage, message)."""
        return random.choice([self.light_attack(), self.heavy_attack()])
    
# === Tree Sentinel (Boss) === #
class TreeSentinel(Enemy):
    def __init__(self):
        super().__init__(
            name="Tree Sentinel",
            hp=1000,
            attack_power=50,  # ✅ Added required attack_power
            defense=20,
            weakness=None,
            loot_item="Golden Halberd",  # ✅ Fixed loot_items -> loot_item
            drop_rate=100  # ✅ Guaranteed drop
        )

    def side_swing(self):
        return (30, "The Tree Sentinel swings its halberd in various directions!")

    def stab(self):
        return (35, "The Tree Sentinel thrusts its halberd forward with force!")

    def horse_bash(self):
        return (40, "The Tree Sentinel's steed suddenly throws itself towards the right, hitting with brute force!")

    def rearing_slam(self):
        return (45, "The Tree Sentinel rears up and slams its halberd into the ground, creating a shockwave!")

    def rearing_swing(self):
        return (38, "The Tree Sentinel rears up, then swings its halberd counterclockwise!")

    def hoof_attack(self):
        return (25, "The Tree Sentinel's horse rears up and slams down its hooves!")

    def charging_attack(self):
        return (50, "The Tree Sentinel charges forward and swings its halberd in a powerful arc!")

    def leap_attack(self):
        return (55, "The Tree Sentinel jumps forward, bringing its halberd down with force!")

    def twirling_swing(self):
        return (48, "The Tree Sentinel turns around, then delivers a far-reaching counterclockwise swing!")

    def attack(self):
        """Randomly selects and performs an attack."""
        return random.choice([
            self.side_swing(),
            self.stab(),
            self.horse_bash(),
            self.rearing_slam(),
            self.rearing_swing(),
            self.hoof_attack(),
            self.charging_attack(),
            self.leap_attack(),
            self.twirling_swing()
        ])
