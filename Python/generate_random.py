import random 

LIMIT = 100

result = []

available_points = LIMIT


for i in range(4):

    if i == 3:

        result.append(available_points)

    else:

        random_points = random.randint(0, available_points)

        result.append(random_points)

        available_points -= random_points

print(result)
