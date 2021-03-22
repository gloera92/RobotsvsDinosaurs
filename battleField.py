from Fleet import Fleet
from Herd import Herd


class BattleField:

    def __init__(self):
        self.Fleet = Fleet()
        self.Herd = Herd()

    def run_battle(self):
        self.Fleet.robot_army[0].robot_attack(self.Herd.dino_army[0])
        self.Herd.dino_army[0].dino_damage_taken(200, 40)
