from Robot import Robot
from Weapon import Weapon


class Fleet:
    def __init__(self):
        self.robot_army = [Robot("T-800", Weapon()), Robot("Bob", Weapon()), Robot("Stan", Weapon())]
