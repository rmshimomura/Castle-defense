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
