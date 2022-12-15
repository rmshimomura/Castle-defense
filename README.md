# Castle defense

This repository is dedicated to the development of a genetic algorithm to solve the castle defense problem.

## Problem description

- Let's say that we have a square castle with limited amount of health, defense points and attack points.

- The castle is surrounded by enemies on all sides, each with a certain amount of health, attack points and defense points too.

- Basically, the goal is to find the best distribuition of the castle's attack points and defense points to maximize the castle's survival time.

- Each iteration represents a day, and each day the enemies attack the castle and the castle attacks the enemies.

### Damage calculation

- Basically, the damage is calculated in the following way:

- Health points lost = Attack points of the attacker - Defense points of the defender (limit 0)

## Fitness function

There are 3 main possibilities to the fitness function (configuration after the chromosome is tested):

1. The castle is destroyed, so the fitness function is the amount of days the castle survived.

2. The castle successfully defended itself, so the fitness function is the amount of days the castle survived + the amount of remaining health of the castle.

3. The castle wasn't destroyed, neither the enemies, but the attack points of the castle on the particular side is not enough to finish the enemies, and the enemies on the particular side is not enough to finish the castle, so the fitness value is set to -1 (annomaly).

Visual representation of the problem:

<div align="center">
  <img display:inline-block src="https://user-images.githubusercontent.com/65873681/207940027-40b0e6b4-4099-4203-af79-aa9e4327ad67.png"/>
</div>

### Notes

- After an enemy is killed, the resources on that particular side are not redistributed, otherwise, we would be creating another chromosome.

## Chromosome representation

The chromosomes (castle walls configuration) are represented using list of lists in Python such as:
```
[[18,65],[18,29],[99,15],[15,41]]
```
The enemies, also are represented in the same way.

## Methodology

- The genetic algorithm is implemented using the following steps:

### Initialization
1. Define the castle resources (attack points and defense points, and health).
2. Set the minimun value of the resources (minimum value that each side must have).
3. Define the population size, the number of generations and the mutation rate.
4. Generate the initial population of castle configurations, and enemies.

### Algorithm
1. Check if the sum of resources doesn't exceed the maximum value of the resources. If so, adjust the values so that the sum is equal to the maximum value.
2. Calculate the fitness of each chromosome using the attack by iteration.
3. Select the best chromosomes to be the parents of the next generation using tournament selection with $n = 2$. So the population size will be cut in half.
4. Apply crossover to the parents to generate remaining children (the half that was removed in tournament selection).
5. Select an elite (the best chromosomes of the generation) to prevent them from suffering mutation.
6. Apply mutation to the children.

### Termination

1. Print the best chromosomes of the generations.
2. Generate a graph of the best fitness of each generation.
