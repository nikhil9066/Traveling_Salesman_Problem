import numpy as np
import random

# Coordinates of the cities
cities = {
    'A': (100, 300), 'B': (200, 130), 'C': (300, 500), 'D': (500, 390),
    'E': (700, 300), 'F': (900, 600), 'G': (800, 950), 'H': (600, 560),
    'I': (350, 550), 'J': (270, 350)
}

import numpy as np
import random

# Coordinates of the cities
cities = {
    'A': (100, 300), 'B': (200, 130), 'C': (300, 500), 'D': (500, 390),
    'E': (700, 300), 'F': (900, 600), 'G': (800, 950), 'H': (600, 560),
    'I': (350, 550), 'J': (270, 350)
}

# Calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Fitness function: total distance of the route
def fitness(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += euclidean_distance(route[i], route[i + 1])
    # Return to starting city
    distance += euclidean_distance(route[-1], route[0])
    return distance

# Initialize a random population
def create_population(pop_size, cities):
    population = []
    for _ in range(pop_size):
        route = list(cities.keys())[1:]  # Exclude city A
        random.shuffle(route)
        route = ['A'] + route + ['A']  # Start and end at A
        population.append(route)
    return population

# Selection: Tournament selection
def selection(population, fitnesses, k=3):
    selected = random.sample(list(zip(population, fitnesses)), k)
    selected.sort(key=lambda x: x[1])  # Sort by fitness (distance)
    return selected[0][0]  # Return the best route