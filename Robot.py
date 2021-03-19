class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 120
        self.power_level = 100
        self.weapon = weapon
        self.attack_power = 40

    def Attack(self, dinoToAttack):

