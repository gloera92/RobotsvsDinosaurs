from Fleet import Fleet


class BattleField:

    def __init__(self):
        self.Fleet = Fleet()

    def run_battle(self):
        self.Fleet.robot_army[0].Attack()