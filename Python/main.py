import castle
import genetics

ATTACK_LIMIT = 100
DEFENSE_LIMIT = 100
MINIMUM_VALUE = 10
CASTLE_HEALTH = 1000

DIRECTIONS = ["N", "S", "W", "E"]

class Attack():

    def __init__(self, attack_points, defense_points, health_points):
        self.attack_points = attack_points
        self.defense_points = defense_points
        self.health_points = health_points

def generate_population(quantity, ATTACK_LIMIT, DEFENSE_LIMIT, DIRECTIONS, MINIMUM_VALUE, CASTLE_HEALTH):
    population = []
    for _ in range(quantity):
        new_castle = castle.Castle(CASTLE_HEALTH)
        new_castle.generate_walls(ATTACK_LIMIT, DEFENSE_LIMIT, DIRECTIONS, MINIMUM_VALUE)
        population.append(new_castle)
    return population

if __name__ == "__main__":

    population = generate_population(10, ATTACK_LIMIT, DEFENSE_LIMIT, DIRECTIONS, MINIMUM_VALUE, CASTLE_HEALTH)
    represent_population = genetics.represent_population(population)
    attackers = [Attack(50, 50, 100) for _ in range(4)]

    for _castle in population:
        _castle.print_info()

    for chromosome in represent_population:
        print(chromosome.genes)


    for chromosome in represent_population: # For each chromosome in the population

        iteration = 0

        attackers = [Attack(50, 50, 100) for _ in range(4)]

        while True:

            total_castle_dmg_taken = 0

            for i in range(4):

                if attackers[i].health_points < 0:
                    continue

                castle_dmg_taken = attackers[i].attack_points - chromosome.genes[i][1] if attackers[i].attack_points > chromosome.genes[i][1] else 0
                attackers_dmg_taken = chromosome.genes[i][0] - attackers[i].defense_points if chromosome.genes[i][0] > attackers[i].defense_points else 0
                total_castle_dmg_taken += castle_dmg_taken
                attackers[i].health_points -= attackers_dmg_taken

            chromosome.health -= total_castle_dmg_taken

            if sum([attacker.health_points for attacker in attackers]) <= 0:
                
                print(f"Castle survived the attack!, fitness: {chromosome.health + iteration}")
                chromosome.fitness = chromosome.health + iteration
                break

            if chromosome.health <= 0:
                print(f"Castle destroyed, fitness: {iteration}")
                chromosome.fitness = iteration
                break
            
            iteration += 1

    # for chromosome in represent_population:

    #     print(chromosome.fitness)

    print("Done")


            
                

    