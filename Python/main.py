import castle
import genetics
import attack
import copy
import report

CASTLE_ATTACK_POINTS = 100
CASTLE_DEFENSE_POINTS = 100
MINIMUM_VALUE = 10
CASTLE_HEALTH = 1000
POPULATION_SIZE = 100
MUTATION_RATE = 0.15
GENERATIONS = 100

ATTACKERS_ATK_POINTS = CASTLE_ATTACK_POINTS + 100
ATTACKERS_DEF_POINTS = CASTLE_DEFENSE_POINTS + 100


DIRECTIONS = ["N", "S", "W", "E"]

def basic_info(represented_population, attackers):

    castle_number = 1

    print("CASTLES:\n\n")

    for chromosome in represented_population:
        
        print(f"Castle {castle_number} - {chromosome.genes}")
        castle_number += 1

    print("\nATTACKERS:\n")

    for attacker in attackers:
        print(attacker.attack_points, attacker.defense_points, attacker.health_points)\
    
    print("\n")

def test_population(represented_population, attackers):

    backup_attackers = copy.deepcopy(attackers)
    
    # basic_info(represented_population, attackers)

    castle_number = 1

    for chromosome in represented_population:

        chromosome.health = CASTLE_HEALTH

        iteration = 0
        attackers = copy.deepcopy(backup_attackers)

        while True:

            total_castle_dmg_taken = 0
            total_attackers_dmg_taken = 0

            for i in range(4):

                if attackers[i].health_points <= 0:
                    continue

                castle_dmg_taken = attackers[i].attack_points - chromosome.genes[i][1] if attackers[i].attack_points > chromosome.genes[i][1] else 0
                attackers_dmg_taken = chromosome.genes[i][0] - attackers[i].defense_points if chromosome.genes[i][0] > attackers[i].defense_points else 0

                total_castle_dmg_taken += castle_dmg_taken
                total_attackers_dmg_taken += attackers_dmg_taken
                attackers[i].health_points -= attackers_dmg_taken

            if total_castle_dmg_taken == 0 and total_attackers_dmg_taken == 0:
                chromosome.fitness = -1
                break

            chromosome.health -= total_castle_dmg_taken

            if sum([attacker.health_points for attacker in attackers]) <= 0:                
                chromosome.fitness = chromosome.health + iteration
                break

            if chromosome.health <= 0:
                chromosome.fitness = iteration
                break
            
            iteration += 1

        castle_number += 1 

if __name__ == "__main__":

    population = castle.generate_population(POPULATION_SIZE, CASTLE_ATTACK_POINTS, CASTLE_DEFENSE_POINTS, DIRECTIONS, MINIMUM_VALUE, CASTLE_HEALTH)
    represented_population = genetics.represented_population(population)
    attackers = attack.generate_attacks(ATTACKERS_ATK_POINTS, ATTACKERS_DEF_POINTS, MINIMUM_VALUE)
    fitnesses = []
    genes = []

    f = open("output_attacks.txt", "w")
    f.write("ATTACKERS:\n\n")
    for attacker in attackers:
        f.write(f"{attacker.attack_points} {attacker.defense_points} {attacker.health_points}\n")
    f.write("\n")

    
    for i in range(0, GENERATIONS):

        temp = []

        for chromosome in represented_population:

            chromosome.genes = genetics.check_sum_chromosome(chromosome, CASTLE_ATTACK_POINTS, CASTLE_DEFENSE_POINTS, MINIMUM_VALUE)
            chromosome.health = CASTLE_HEALTH
            chromosome.fitness = 0
            new_chromosome = genetics.Chromosomes()
            new_chromosome.genes = copy.deepcopy(chromosome.genes)
            new_chromosome.health = copy.deepcopy(chromosome.health)
            new_chromosome.fitness = copy.deepcopy(chromosome.fitness)
            temp.append(new_chromosome)

        represented_population = temp

        test_population(represented_population, attackers)

        for chromosome in represented_population:
            atk_sum = sum([gene[0] for gene in chromosome.genes])
            def_sum = sum([gene[1] for gene in chromosome.genes])
            if atk_sum != CASTLE_ATTACK_POINTS or def_sum != CASTLE_DEFENSE_POINTS:
                print(f"Chromosome: {chromosome.genes}, atk_sum: {atk_sum}, def_sum: {def_sum}, fitness: {chromosome.fitness}, health: {chromosome.health}")

        represented_population.sort(key=lambda x: x.fitness, reverse=True)

        best_generation_chromosome = max(represented_population, key=lambda chromosome: chromosome.fitness)

        fitnesses.append(best_generation_chromosome.fitness)

        genes.append(best_generation_chromosome.genes)

        tournament_selection = genetics.tournament_selection(represented_population)

        crossover = genetics.crossover(tournament_selection, POPULATION_SIZE)

        mutation = genetics.mutation(crossover, CASTLE_ATTACK_POINTS, CASTLE_DEFENSE_POINTS, MUTATION_RATE, MINIMUM_VALUE)

        represented_population = mutation

    f.write("CASTLES:\n\n")
    for i in range(GENERATIONS):
        f.write(f"{genes[i]} survived {fitnesses[i]} days\n")

    f.close()
    report.generate_graph(fitnesses, GENERATIONS)