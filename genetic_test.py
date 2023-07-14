import random


# Step 1: Define the problem
def fitness_function(x):
    return x ** 2


# Step 2: Initialize the population
def initialize_population(population_size, chromosome_length):
    population = []
    for _ in range(population_size):
        chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
        population.append(chromosome)
    return population


# Step 3: Evaluate the fitness
def evaluate_fitness(population):
    fitness_scores = []
    for chromosome in population:
        x = int(''.join(map(str, chromosome)), 2)  # Convert binary chromosome to decimal value
        fitness_scores.append(fitness_function(x))
    return fitness_scores


# Step 4: Selection
def selection(population, fitness_scores):
    selected_population = []
    total_fitness = sum(fitness_scores)
    probabilities = [fitness / total_fitness for fitness in fitness_scores]
    for _ in range(len(population)):
        selected_population.append(random.choices(population, probabilities)[0])
    return selected_population


# Step 5: Crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


# Step 6: Mutation
def mutation(chromosome, mutation_rate):
    mutated_chromosome = chromosome.copy()
    for i in range(len(mutated_chromosome)):
        if random.random() < mutation_rate:
            mutated_chromosome[i] = 1 - mutated_chromosome[i]  # Flip the bit
    return mutated_chromosome


# Step 7: Replace the population
def create_next_generation(population, mutation_rate):
    fitness_scores = evaluate_fitness(population)
    selected_population = selection(population, fitness_scores)
    next_generation = []
    for i in range(0, len(selected_population), 2):
        parent1 = selected_population[i]
        parent2 = selected_population[i + 1]
        child1, child2 = crossover(parent1, parent2)
        child1 = mutation(child1, mutation_rate)
        child2 = mutation(child2, mutation_rate)
        next_generation.extend([child1, child2])
    return next_generation


# Step 8: Termination
def genetic_algorithm(population_size, chromosome_length, mutation_rate, generations):
    population = initialize_population(population_size, chromosome_length)
    for _ in range(generations):
        population = create_next_generation(population, mutation_rate)
    fitness_scores = evaluate_fitness(population)
    best_individual = population[fitness_scores.index(max(fitness_scores))]
    x = int(''.join(map(str, best_individual)), 2)
    return x


# Run the genetic algorithm
population_size = 100
chromosome_length = 8
mutation_rate = 0.01
generations = 100

result = genetic_algorithm(population_size, chromosome_length, mutation_rate, generations)
print("Best solution:", result)
