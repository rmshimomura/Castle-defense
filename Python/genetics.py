import random
import copy

class Chromosomes():
    
    def __init__(self):
        self.raw_data = []
        self.genes = []
        self.fitness = 0
        self.health = 0

    def extract_genes(self):
        for wall in self.raw_data.walls:
            self.genes.append([wall.attack_points, wall.defense_points])

def represented_population(population : list):
    chromosomes = []
    for castle in population:
        chromosome = Chromosomes()
        chromosome.raw_data = castle
        chromosome.health = castle.health_points
        chromosome.extract_genes()
        chromosomes.append(chromosome)
    return chromosomes

def tournament_selection(population : list):
    temp_population = copy.deepcopy(population)
    selected_chromosomes = []
    while True:
        
        if len(temp_population) == 0:
            break
        
        first_chromossome = random.choice(temp_population)
        second_chromossome = random.choice(temp_population)

        if len(temp_population) == 1:
            selected_chromosomes.append(first_chromossome)
            break

        while first_chromossome == second_chromossome:
            second_chromossome = random.choice(temp_population)

        if first_chromossome.fitness >= second_chromossome.fitness:
            selected_chromosomes.append(first_chromossome)

        else:
            selected_chromosomes.append(second_chromossome)        

        temp_population.remove(first_chromossome)
        temp_population.remove(second_chromossome)
    
    # Sort selected chromosomes by fitness
    selected_chromosomes.sort(key=lambda x: x.fitness, reverse=True)

    return selected_chromosomes
    
def redistribute_points(chromosome : Chromosomes, sum_points : int, MAX_VALUE : int, mode : int, MINIMUM_VALUE : int):

    difference = sum_points - MAX_VALUE

    if difference > 0:

        i = 0

        while difference > 0:

            if chromosome.genes[i][mode] - 1 >= MINIMUM_VALUE:
                chromosome.genes[i][mode] -= 1
                difference -= 1

            i += 1

            if i == len(chromosome.genes):
                i = 0
    
    elif difference < 0:

        for i in range(0, len(chromosome.genes)):

            while chromosome.genes[i][mode] < MINIMUM_VALUE:
                chromosome.genes[i][mode] += 1
                difference += 1
                if difference == 0:
                    break

        i = 0

        while difference < 0:

            chromosome.genes[i][mode] += 1
            difference += 1

            i += 1

            if i == len(chromosome.genes):
                i = 0

    return chromosome.genes

def check_sum_chromosome(chromosome : Chromosomes, MAXIMUM_ATK_VALUE : int, MAXIMUM_DEF_VALUE: int, MINIMUM_VALUE: int):

    sum_attack = sum([gene[0] for gene in chromosome.genes])
    sum_defense = sum([gene[1] for gene in chromosome.genes])

    if sum_attack != MAXIMUM_ATK_VALUE:

        chromosome.genes = redistribute_points(chromosome, sum_attack, MAXIMUM_ATK_VALUE, 0, MINIMUM_VALUE)

    if sum_defense != MAXIMUM_DEF_VALUE:

        chromosome.genes = redistribute_points(chromosome, sum_defense, MAXIMUM_DEF_VALUE, 1, MINIMUM_VALUE)

    return chromosome.genes

def crossover(population: list, TARGET_POPULATION_SIZE: int):

    original_size = len(population)

    while True:

        first_chromosome = population[random.randint(0, original_size - 1)]
        second_chromosome = population[random.randint(0, original_size - 1)]
        crossover_point = random.randint(0, len(first_chromosome.genes) - 1)

        first_new_chromosome = Chromosomes()
        second_new_chromosome = Chromosomes()

        first_new_chromosome.genes = copy.deepcopy(first_chromosome.genes[:crossover_point]) + copy.deepcopy(second_chromosome.genes[crossover_point:])
        second_new_chromosome.genes = copy.deepcopy(second_chromosome.genes[:crossover_point]) + copy.deepcopy(first_chromosome.genes[crossover_point:])

        first_new_chromosome.health = copy.deepcopy(first_chromosome.health)
        second_new_chromosome.health = copy.deepcopy(second_chromosome.health)

        first_new_chromosome.fitness = 0
        second_new_chromosome.fitness = 0

        if len(population) + 1 <= TARGET_POPULATION_SIZE:
            population.append(first_new_chromosome)
        if len(population) + 1 <= TARGET_POPULATION_SIZE:
            population.append(second_new_chromosome)

        if len(population) == TARGET_POPULATION_SIZE:
            break

    return population

def mutation(population : list, MAXIMUM_ATK_VALUE : int, MAXIMUM_DEF_VALUE : int, MUTATION_RATE : int, MINIMUM_VALUE : int):
    
    # Count the chromosomes whose fitness difference with the best chromosome is less than 30%
    count = 0
    # 100 , 84, 72, 71 < 70
    
    for chromosome in population:
        if chromosome.fitness >= population[0].fitness * 0.7:
            count += 1

    elite_size = count

    for i in range(elite_size, len(population), 1):
        for j in range(4):
            random_number = random.uniform(0, 1)
            if(random_number <= MUTATION_RATE):
                population[i].genes[j][0] = random.randint(MINIMUM_VALUE, MAXIMUM_ATK_VALUE)
                population[i].genes[j][1] = random.randint(MINIMUM_VALUE, MAXIMUM_DEF_VALUE)

    return population