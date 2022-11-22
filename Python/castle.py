import random

def fixed_total(quantity, total, min):
    total -= min * quantity
    if total < 1:
        return
    cumulative_sum = [0, total] + [random.randint(0, total) for _ in range(quantity-1)]
    cumulative_sum.sort()
    return [cumulative_sum[i] - cumulative_sum[i-1] for i in range(1, len(cumulative_sum))]

class Wall():

    def __init__(self, attack_points, defense_points, side):
        self.attack_points = attack_points
        self.defense_points = defense_points
        self.side = side

class Castle():

    def __init__(self, health_points):
        self.health_points = health_points
        self.walls = []
        
    def generate_walls(self, ATTACK_LIMIT, DEFENSE_LIMIT, DIRECTIONS, MINIMUM_VALUE):

        attack_points = fixed_total(4, ATTACK_LIMIT, MINIMUM_VALUE)
        defense_points = fixed_total(4, DEFENSE_LIMIT, MINIMUM_VALUE)

        for i in range(4):
            self.walls.append(Wall(attack_points[i] + MINIMUM_VALUE, defense_points[i] + MINIMUM_VALUE, DIRECTIONS[i]))

    def print_info(self):
        print("Castle Health Points: ", self.health_points)
        for wall in self.walls:
            print("WALL " + wall.side + f" [{wall.attack_points} - {wall.defense_points}]")
        print("=====================================")

def generate_population(quantity, ATTACK_LIMIT, DEFENSE_LIMIT, DIRECTIONS, MINIMUM_VALUE, CASTLE_HEALTH):
    population = []
    for _ in range(quantity):
        new_castle = Castle(CASTLE_HEALTH)
        new_castle.generate_walls(ATTACK_LIMIT, DEFENSE_LIMIT, DIRECTIONS, MINIMUM_VALUE)
        population.append(new_castle)
    return population