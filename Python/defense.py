import castle
import genetics

ATTACK_LIMIT = 100
DEFENSE_LIMIT = 100
MINIMUM_VALUE = 10

DIRECTIONS = ["N", "S", "E", "W"]

class Attack():

    def __init__(self, attack_points, defense_points):
        self.attack_points = attack_points
        self.defense_points = defense_points


if __name__ == "__main__":

    new_castle = castle.Castle(1000)

    new_castle.generate_walls(ATTACK_LIMIT, DEFENSE_LIMIT, DIRECTIONS, MINIMUM_VALUE)

    new_castle.print_info()