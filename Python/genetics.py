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
        first_chromossome = random.choice(temp_population)
        second_chromossome = random.choice(temp_population)

        while first_chromossome == second_chromossome:
            second_chromossome = random.choice(temp_population)
        
        if first_chromossome.fitness >= second_chromossome.fitness:
            selected_chromosomes.append(first_chromossome)
        else:
            selected_chromosomes.append(second_chromossome)        

        temp_population.remove(first_chromossome)
        temp_population.remove(second_chromossome)

        if len(temp_population) == 0:
            break
        if len(temp_population) == 1:
            selected_chromosomes.append(first_chromossome)
            break
    
    # Sort selected chromosomes by fitness
    selected_chromosomes.sort(key=lambda x: x.fitness, reverse=True)
    return selected_chromosomes
    