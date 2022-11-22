import random

def fixed_total(quantity, total, min):
    total -= min * quantity
    if total < 1:
        return
    cumulative_sum = [0, total] + [random.randint(0, total) for _ in range(quantity-1)]
    cumulative_sum.sort()
    return [cumulative_sum[i] - cumulative_sum[i-1] for i in range(1, len(cumulative_sum))]

class Attack():

    def __init__(self, attack_points, defense_points, health_points):
        self.attack_points = attack_points
        self.defense_points = defense_points
        self.health_points = health_points
    
        
def generate_attacks(ATTACK_LIMIT, DEFENSE_LIMIT, MINIMUM_VALUE):
    attack_points = fixed_total(4, ATTACK_LIMIT, MINIMUM_VALUE)
    defense_points = fixed_total(4, DEFENSE_LIMIT, MINIMUM_VALUE)

    attacks = []

    for i in range(4):
        attacks.append(Attack(attack_points[i] + MINIMUM_VALUE, defense_points[i] + MINIMUM_VALUE, 100))

    return attacks