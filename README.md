# Traveling Salesman Problem using Genetic Algorithm

## Overview

This project implements a **Genetic Algorithm (GA)** to solve the **Traveling Salesman Problem (TSP)**. The TSP is a combinatorial optimization problem where the objective is to find the shortest possible route that visits a set of cities exactly once and returns to the starting city. The solution utilizes a GA to approximate the shortest route efficiently.

## Problem Statement

The Traveling Salesman Problem asks for the most efficient path (shortest route) that visits a set of cities once and returns to the starting point. Given the computational complexity (NP-hard), this project uses a genetic algorithm to provide a near-optimal solution.

The project includes:
- A custom **GA** for evolving solutions through selection, crossover, and mutation.
- Calculation of **Euclidean distances** between cities.
- Implementation of **Order Crossover (OX)** and **Swap Mutation**.
- Output of the **shortest path** and **total distance** for a given set of cities.

## Features

- **Genetic Algorithm (GA)** implementation with:
  - Population initialization
  - Fitness function based on total route distance
  - Selection of the best candidates
  - Crossover and mutation for generating new solutions
- Outputs the best route found and the corresponding distance.
- Customizable parameters: population size, number of generations, and mutation rate.

## Project Structure

- `genetic_algorithm_tsp.py`: The main Python script implementing the Genetic Algorithm for the TSP.

## Cities and Coordinates

The problem is defined over a grid of 1,000 x 1,000 miles with 10 cities, each having the following coordinates:

| City | X-coordinate | Y-coordinate |
|------|--------------|--------------|
| A    | 100          | 300          |
| B    | 200          | 130          |
| C    | 300          | 500          |
| D    | 500          | 390          |
| E    | 700          | 300          |
| F    | 900          | 600          |
| G    | 800          | 950          |
| H    | 600          | 560          |
| I    | 350          | 550          |
| J    | 270          | 350          |

## How It Works

### Genetic Algorithm (GA) Workflow:

1. **Population Initialization**: Generates random tours that start and end at city A.
2. **Fitness Evaluation**: Each route's total distance is calculated using Euclidean distance, and the fitness is the inverse of this distance (shorter routes have higher fitness).
3. **Selection**: The best routes are selected for breeding.
4. **Crossover**: New routes (children) are generated using the Order Crossover (OX) method.
5. **Mutation**: Random cities in the route are swapped to maintain diversity in the population.
6. **Termination**: The algorithm runs for a fixed number of generations or until convergence.

### Algorithm Parameters:
- Population size: 100
- Generations: 500
- Mutation rate: 0.1 (modifiable)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nikhil9066/Traveling_Salesman_Problem.git
   cd Traveling_Salesman_Problem```
   
2. Install required packages:
   ```bash
   pip install numpy matplotlib```

3. Run the script:
   ```bash
   python genetic_algorithm_tsp.py```

## Output Example
After running the algorithm, the output will display:
- The best route found
- The shortest distance (in miles)

Example:
Best route found: ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'C', 'J', 'A']
Best distance: 2627.47 miles

## Applications of TSP
The Traveling Salesman Problem is widely applicable in areas such as:
- Logistics: Optimizing delivery routes to minimize time and fuel consumption.
- Circuit board manufacturing: Minimizing the movement of drilling machines.
- X-ray crystallography: Optimizing the arrangement of crystal analysis.
- Vehicle routing: Finding the shortest path for vehicles to service customers.

## Customization
You can modify the following parameters in the genetic_algorithm_tsp.py file:

- Number of generations
- Population size
- Mutation rate

## References
This project is based on the academic work from CIS 561 - Artificial Intelligence, focusing on solving the Traveling Salesman Problem using Genetic Algorithms.