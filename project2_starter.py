# Base Game Object (Level 1)
class GameObject:

    def __init__(self, name: str):
        self.name = name

    def describe(self):
        return f"{self.name}"

 # Weapon (HAS-A relationship)
class Weapon:
    def __init__(self, name: str, damage_bonus: int):
        self.name = name
        self.damage_bonus = damage_bonus

    def describe(self):
        return f"{self.name} (+{self.damage_bonus} dmg)"

# Character Base (Level 2)
class Character(GameObject):
    #Base class for all character types.
    def __init__(self, name: str, health: int, strength: int, magic: int):
        super().__init__(name)
        self.health = health
        self.max_health = health
        self.strength = strength
        self.magic = magic

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount: int):
        #Reduce health but not below 0.
        if amount < 0:
            amount = 0
        new_health = self.health - amount
        if new_health < 0:
            new_health = 0
            self.health = new_health
            return self.health

    def display_stats(self):
        #Return a string describing basic stats.
        return (f"{self.name} - "
                f"Health: {self.health}/{self.max_health}, "
                f"Strength: {self.strength}, Magic: {self.magic}")

# Warrior Class (Level 3)
class Warrior(Character):
    def __init__(self, name: str):
        super().__init__(name, health=140, strength=15, magic=3)
        self.character_class = "Warrior"
        self.weapon = Weapon("Iron Sword", 10)

    def attack(self, target: Character):
        #Basic Warrior attack. Uses strength and weapon damage bonus to calculate damage.
        
        if not self.is_alive():
            return f"{self.name} cannot attack because they are down."
        if not target.is_alive():
            return f"{target.name} is already defeated."

        damage = self.strength + self.weapon.damage_bonus
        target.take_damage(damage)
        return (f"{self.name} slashes {target.name} with {self.weapon.name} "
                f"for {damage} damage.")

    def power_strike(self, target: Character):
        #Special ability: big hit that does more damage than normal attack.
        if not self.is_alive():
            return f"{self.name} cannot use Power Strike because they are down."
        if not target.is_alive():
            return f"{target.name} is already defeated."

        damage = self.strength * 2 + self.weapon.damage_bonus
        target.take_damage(damage)
        return (f"{self.name} uses Power Strike on {target.name} "
                f"for {damage} damage!")

    def use_special(self, target: Character):
        return self.power_strike(target)

    def display_stats(self):
        base = super().display_stats()
        return f"{base} [Class: {self.character_class}, Weapon: {self.weapon.name}]"

 # Mage Class (Level 3)
class Mage(Character):
    def __init__(self, name: str):
        # lower health, high magic
        super().__init__(name, health=80, strength=6, magic=18)
        self.character_class = "Mage"
        self.weapon = Weapon("Magic Staff", 8)
        self.max_mana = 50
        self.current_mana = 50

    def restore_mana(self, amount: int):
        self.current_mana += amount
        if self.current_mana > self.max_mana:
            self.current_mana = self.max_mana

    def attack(self, target: Character):
        #Basic Mage attack. Weaker than Fireball, uses some of magic plus weapon bonus.
        
        if not self.is_alive():
            return f"{self.name} cannot attack because they are down."
        if not target.is_alive():
            return f"{target.name} is already defeated."

        damage = (self.magic // 2) + self.weapon.damage_bonus
        target.take_damage(damage)
        return (f"{self.name} casts a bolt with {self.weapon.name} at "
                f"{target.name} for {damage} damage.")

    def fireball(self, target: Character):
        #Special ability: Fireball. Should do significant damage.
        if not self.is_alive():
            return f"{self.name} cannot cast Fireball because they are down."
        if not target.is_alive():
            return f"{target.name} is already defeated."

        damage = self.magic + self.weapon.damage_bonus
        target.take_damage(damage)
        return (f"{self.name} casts Fireball on {target.name} "
                f"for {damage} damage!")

    def use_special(self, target: Character):
        return self.fireball(target)

    def display_stats(self):
        base = super().display_stats()
        return (f"{base} [Class: {self.character_class}, "
                f"Weapon: {self.weapon.name}, "
                f"Mana: {self.current_mana}/{self.max_mana}]")

# Rogue Class (Level 3)
class Rogue(Character):
    def __init__(self, name: str):
        # medium health, good strength, some magic
        super().__init__(name, health=100, strength=12, magic=8)
        self.character_class = "Rogue"
        self.weapon = Weapon("Steel Dagger", 7)

    def attack(self, target: Character):
        #Basic Rogue attack. Quicker hits, decent damage (uses half weapon bonus).
        if not self.is_alive():
            return f"{self.name} cannot attack because they are down."
        if not target.is_alive():
            return f"{target.name} is already defeated."

        damage = self.strength + (self.weapon.damage_bonus // 2)
        target.take_damage(damage)
        return (f"{self.name} strikes from the shadows and hits "
                f"{target.name} for {damage} damage.")

    def sneak_attack(self, target: Character):
        #Special ability: high damage critical hit.
        if not self.is_alive():
            return f"{self.name} cannot use Sneak Attack because they are down."
        if not target.is_alive():
            return f"{target.name} is already defeated."

        damage = self.strength + self.magic + self.weapon.damage_bonus
        target.take_damage(damage)
        return (f"{self.name} uses Sneak Attack on {target.name} "
                f"for {damage} damage!")

    def use_special(self, target: Character):
        return self.sneak_attack(target)

    def display_stats(self):
        base = super().display_stats()
        return f"{base} [Class: {self.character_class}, Weapon: {self.weapon.name}]"



# Entry point of program
if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("====================================")

    w = Warrior("Ari")
    m = Mage("Daniel")
    r = Rogue("Will")

    dummy = Character("Training Dummy", 100, 5, 5)

    print(w.display_stats())
    print(m.display_stats())
    print(r.display_stats())

    print("\n--- Demo Attacks ---")
    print(w.attack(dummy))
    print(m.fireball(dummy))
    print(r.sneak_attack(dummy))
    print("Dummy health:", dummy.health)
