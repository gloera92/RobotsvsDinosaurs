from Herd import Herd


class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 120
        self.power_level = 100
        self.weapon = weapon
        self.attack_power = 40

    def robot_attack(self):
        if Herd(self.dino_army[0])

    def robot_damage_taken(self, health, attack_power):
        self.health = health - attack_power
        return self
