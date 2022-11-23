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

def represented_population(population):
    chromosomes = []
    for castle in population:
        chromosome = Chromosomes()
        chromosome.raw_data = castle
        chromosome.health = castle.health_points
        chromosome.extract_genes()
        chromosomes.append(chromosome)
    return chromosomes

def tournament_selection(population, tournament_size):
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
    
def redistribute_points(chromosome, sum_points, MAX_VALUE, mode, MINIMUM_VALUE):

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
                chromosome.gen[i][mode] += 1
                difference += 1

        i = 0

        while difference < 0:

            chromosome.genes[i][mode] += 1
            difference += 1

            i += 1

            if i == len(chromosome.genes):
                i = 0

def check_sum_chromosome(chromosome, MAXIMUM_ATK_VALUE, MAXIMUM_DEF_VALUE, MINIMUM_VALUE):

    sum_attack = sum([gene[0] for gene in chromosome.genes])
    sum_defense = sum([gene[1] for gene in chromosome.genes])

    if sum_attack != MAXIMUM_ATK_VALUE:

        redistribute_points(chromosome, sum_attack, MAXIMUM_ATK_VALUE, 0, MINIMUM_VALUE)

    if sum_defense != MAXIMUM_DEF_VALUE:

        redistribute_points(chromosome, sum_defense, MAXIMUM_DEF_VALUE, 1, MINIMUM_VALUE)

def crossover(population, MAXIMUM_ATK_VALUE, MAXIMUM_DEF_VALUE, MINIMUM_VALUE):

    for i in range(0, len(population), 2):
        if i + 1 < len(population):
            first_chromosome = population[i]
            second_chromosome = population[i + 1]
            crossover_point = random.randint(1, len(first_chromosome.genes) - 1)
            first_chromosome.genes[crossover_point:], second_chromosome.genes[crossover_point:] = second_chromosome.genes[crossover_point:], first_chromosome.genes[crossover_point:]

            check_sum_chromosome(first_chromosome, MAXIMUM_ATK_VALUE, MAXIMUM_DEF_VALUE, MINIMUM_VALUE)
            check_sum_chromosome(second_chromosome, MAXIMUM_ATK_VALUE, MAXIMUM_DEF_VALUE, MINIMUM_VALUE)

        else:
            break

def mutation(population, MAXIMUM_ATK_VALUE, MAXIMUM_DEF_VALUE, MUTATION_RATE, MINIMUM_VALUE):
    for i in range(0, len(population), 1):
        for j in range(0, 4, 1):
            random_number = random.uniform(0, 1)
            if(random_number <= MUTATION_RATE):
                population[i].genes[j][0] = random.randint(MINIMUM_VALUE, MAXIMUM_ATK_VALUE)
                population[i].genes[j][1] = random.randint(MINIMUM_VALUE, MAXIMUM_DEF_VALUE)
            check_sum_chromosome(population[i], MAXIMUM_ATK_VALUE, MAXIMUM_DEF_VALUE, MINIMUM_VALUE)