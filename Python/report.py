import matplotlib.pyplot as plt

def generate_graph(fitnesses, GENERATIONS):
    # make a list values that goes from 1 to 50 with the values that goes 1 to 50
    generations = list(range(0, GENERATIONS))
    for i in range(0, GENERATIONS):
        generations[i] = i + 1
    plt.bar(generations, fitnesses, color ='red')
    plt.xlabel("Generations")
    plt.ylabel("Fitnesses")
    plt.title(f"Relation graph between generations and fitnesses in {GENERATIONS} generations")
    plt.show()