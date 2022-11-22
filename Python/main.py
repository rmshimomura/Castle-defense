import castle
import genetics
import attack
import copy

ATTACK_LIMIT = 100
DEFENSE_LIMIT = 100
MINIMUM_VALUE = 10
CASTLE_HEALTH = 1000
POPULATION_SIZE = 100

DIRECTIONS = ["N", "S", "W", "E"]

def basic_info(represent_population, attackers):
    for chromosome in represent_population:
        print(chromosome.genes)

    for attacker in attackers:
        print(attacker.attack_points, attacker.defense_points, attacker.health_points)

def test_population(represent_population, attackers):
    # Make backup_attackers receive the same values as attackers to avoid changing the original list and make backup_attacks immutable
    backup_attackers = copy.deepcopy(attackers)
    
    basic_info(represent_population, attackers)

    castle_number = 1

    for chromosome in represent_population: # For each chromosome in the population

        print("CASTLE : ", castle_number)

        iteration = 0

        # Reset attackers to the original values on backup_attackers
        attackers = copy.deepcopy(backup_attackers)

        while True:

            total_castle_dmg_taken = 0

            total_attackers_dmg_taken = 0

            problem = False

            for i in range(4):

                if attackers[i].health_points <= 0:
                    continue

                castle_dmg_taken = attackers[i].attack_points - chromosome.genes[i][1] if attackers[i].attack_points > chromosome.genes[i][1] else 0
                attackers_dmg_taken = chromosome.genes[i][0] - attackers[i].defense_points if chromosome.genes[i][0] > attackers[i].defense_points else 0

                total_castle_dmg_taken += castle_dmg_taken
                total_attackers_dmg_taken += attackers_dmg_taken
                attackers[i].health_points -= attackers_dmg_taken

                if attackers[i].health_points <= 0:
                    print("Attacker on side " + DIRECTIONS[i] + " died")

            if total_castle_dmg_taken == 0 and total_attackers_dmg_taken == 0:
                chromosome.fitness = -1
                print(f"{chromosome.genes} had a problem with {[(attacker.attack_points, attacker.defense_points, attacker.health_points) for attacker in attackers]}, fitness: {chromosome.fitness}\n\n")
                break

            chromosome.health -= total_castle_dmg_taken

            if sum([attacker.health_points for attacker in attackers]) <= 0:
                
                print(f"Castle survived the attack!, fitness: {chromosome.health + iteration}\n\n")
                chromosome.fitness = chromosome.health + iteration
                break

            if chromosome.health <= 0:
                print(f"Castle destroyed, fitness: {iteration}\n\n")
                chromosome.fitness = iteration
                break
            
            iteration += 1

            # print(f"Iteration: {iteration}, Castle Health: {chromosome.health}, Attackers Health: {sum([attacker.health_points for attacker in attackers])}, total castle dmg taken: {total_castle_dmg_taken}")
        castle_number += 1

if __name__ == "__main__":

    population = castle.generate_population(POPULATION_SIZE, ATTACK_LIMIT, DEFENSE_LIMIT, DIRECTIONS, MINIMUM_VALUE, CASTLE_HEALTH)
    represent_population = genetics.represent_population(population)
    attackers = attack.generate_attacks(ATTACK_LIMIT + 100, DEFENSE_LIMIT, MINIMUM_VALUE)

    test_population(represent_population, attackers)