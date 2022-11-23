import matplotlib.pyplot as plt

def generate_graph(fitnesses, GENERATIONS):
    
    generations = list(range(0, GENERATIONS))
    for i in range(0, GENERATIONS):
        generations[i] = i + 1
    plt.plot(generations, fitnesses, color='blue')
    plt.xlabel("Generations")
    plt.ylabel("Fitnesses")
    plt.title(f"Relation graph between generations and fitnesses in {GENERATIONS} generations")
    plt.grid(True)
    plt.savefig("graph.png")
    # plt.show()
