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

# Crossover: Order Crossover (OX)
def crossover(parent1, parent2):
    size = len(parent1)
    
    # Ensure size is sufficient
    if size <= 2:
        raise ValueError("Parent size must be greater than 2 for crossover.")
    
    # Sample start and end indices
    start, end = sorted(random.sample(range(1, size - 1), 2))  # Exclude 'A'
    
    # Create child with 'None' placeholders
    child = [None] * size
    child[0], child[-1] = 'A', 'A'  # Keep 'A' at both ends
    child[start:end+1] = parent1[start:end+1]  # Inherit a slice from parent1
    
    # Fill the remaining cities from parent2 in the order they appear
    parent2_cities = [city for city in parent2 if city not in child]
    
    # Replace 'None' values in the child with cities from parent2
    j = (end + 1) % size  # Start filling from the next index after 'end'
    for city in parent2_cities:
        while child[j] is not None:
            j = (j + 1) % size  # Move to the next index if already filled
        child[j] = city  # Fill in missing cities
        j = (j + 1) % size  # Move to the next index

    return child

# Mutation: Swap Mutation
def mutate(route, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(route) - 1), 2)  # Exclude 'A'
        route[i], route[j] = route[j], route[i]
    return route

# Genetic Algorithm
def genetic_algorithm(cities, pop_size=100, generations=500, mutation_rate=0.1):
    population = create_population(pop_size, cities)
    
    # Print the initial population
    print("\nInitial population:")
    for i, route in enumerate(population):
        print(f"Route {i+1}: {route}")
    
    for gen in range(generations):
        fitnesses = [fitness(route) for route in population]
        
        # Print fitness values for the generation
        print(f"\nGeneration {gen+1} fitness values:")
        for i, f in enumerate(fitnesses):
            print(f"Route {i+1}: Fitness = {f:.2f}")
        
        new_population = []
        for _ in range(pop_size):
            parent1 = selection(population, fitnesses)
            parent2 = selection(population, fitnesses)
            
            # Print selected parents
            print(f"Selected Parent 1: {parent1}")
            print(f"Selected Parent 2: {parent2}")
            
            child = crossover(parent1, parent2)
            print(f"Child after crossover: {child}")
            
            child = mutate(child, mutation_rate)
            print(f"Child after mutation: {child}")
            
            # Debugging: Ensure all cities are present in the child
            if None in child:
                print(f"Error in child: {child}")
            else:
                new_population.append(child)
        
        population = new_population
    
    # Print final population
    print("\nFinal population:")
    for i, route in enumerate(population):
        print(f"Route {i+1}: {route}")
    
    best_route = min(population, key=fitness)
    
    # Print best route and best fitness (distance)
    print(f"\nBest route found: {best_route}")
    print(f"Best distance: {fitness(best_route):.2f}")
    
    return best_route, fitness(best_route)


# Run the Genetic Algorithm
best_route, best_distance = genetic_algorithm(cities)
print("Best route:", best_route)
print("Best distance:", best_distance)
