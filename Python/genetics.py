class Chromosomes():
    
    def __init__(self):
        self.raw_data = []
        self.genes = []
        self.fitness = 0
        self.health = 0

    def extract_genes(self):
        for wall in self.raw_data.walls:
            self.genes.append([wall.attack_points, wall.defense_points])

def represent_population(population):
    chromosomes = []
    for castle in population:
        chromosome = Chromosomes()
        chromosome.raw_data = castle
        chromosome.health = castle.health_points
        chromosome.extract_genes()
        chromosomes.append(chromosome)
    return chromosomes