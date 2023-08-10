import random

# Length of the chromosome (genes) representing each cat's characteristics
chromosome_length = 10


# Fitness function: evaluate the health of a cat population
def fitness_function(chromosome):
    # Calculate the fitness value based on the characteristics of the cat population
    # This can be any function that represents the health of a population
    return sum(chromosome)


# def generatePopulations(num_populations=10, population_size=50):
#     populations = []
#     for _ in range(num_populations):
#         population = []
#         for _ in range(population_size):
#             chromosome = []
#             for _ in range(chromosome_length):
#                 chromosome.append(random.randint(0, 1))
#
#             population.append(chromosome)
#         populations.append(population)
#
#     print(populations)


populations = [
    [
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
        [0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 1, 1, 0],
        [0, 0, 1, 1, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 0, 1]
    ],
    [
        [0, 1, 1, 1, 0, 1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 0, 1, 1, 1, 1, 0]
    ],
    [
        [1, 0, 1, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 1, 0, 0, 1, 1, 1, 1, 1, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 0]
    ],
    [
        [1, 1, 1, 1, 0, 1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
        [1, 0, 0, 1, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
        [0, 1, 1, 0, 0, 0, 1, 1, 0, 0]
    ],
    [
        [1, 1, 0, 0, 1, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    ],
    [
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 1, 1, 0, 0, 1, 0, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 1]
    ],
    [
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
        [1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 1, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    ],
    [
        [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 0, 0]
    ],
    [
        [0, 1, 1, 0, 0, 1, 1, 1, 1, 1],
        [0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 0]
    ],
    [
        [1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 1, 0, 1, 0, 1, 1]
    ]
]


def evolve(populations, num_generations=100):
    # Main evolution loop
    for generation in range(num_generations):
        print(f"Generation {generation + 1}")

        # Evaluate fitness for each population
        fitness_values = []
        for population in populations:
            population_fitness = []

            for chromosome in population:
                population_fitness.append(fitness_function(chromosome))

            fitness_values.append(population_fitness)

        # Select parents for reproduction
        selected_parents = []
        for population_fitness in fitness_values:
            # Roulette wheel selection
            total_fitness = sum(population_fitness)
            probabilities = [fitness / total_fitness for fitness in population_fitness]
            parents = random.choices(populations, probabilities, k=2)
            selected_parents.append(parents)

        # Create offspring through crossover
        offspring = []
        for parents in selected_parents:
            parent1, parent2 = parents
            child1 = parent1[:chromosome_length // 2] + parent2[chromosome_length // 2:]
            child2 = parent2[:chromosome_length // 2] + parent1[chromosome_length // 2:]
            offspring.append(child1)
            offspring.append(child2)

        # Apply mutation to the offspring
        for child in offspring:
            for i in range(chromosome_length):
                if random.random() < 0.1:  # Mutation probability of 0.1
                    child[i] = 1 - child[i]  # Flip the bit

        # Replace the old populations with the new offspring
        populations = offspring


# Select the best population based on fitness
best_population = max(populations,
                      key=lambda population: max(fitness_function(chromosome) for chromosome in population))

# Select the best individual (cat) within the best population
best_individual = max(best_population, key=fitness_function)

# Print the characteristics of the best individual
print("Best individual:", best_individual)
