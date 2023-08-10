import random

attributes = {
    'pattern': [
        'solid',
        'tabby',
        'tortoiseshell',
        'calico',
        'bicolor',
        'pointed',
        'colorpoint',
        'lynx_point',
        'smoke',
        'chinchilla'
    ],
    'mouth_shape': [
        "simple_smile",
        "wide_smile",
        "toothy_grin",
        "open_mouth",
        "laughing",
        "pouting",
        "scream_shout",
        "smirk",
        "tongue_sticking_out",
        "biting_lips",
        "drooling",
        "zigzag_mouth",
    ],
    'fur': [
        "smooth",
        "longhair",
        "shorthair",
        "medium_hair",
        "curly",
        "wirehair",
        "satin",
        "rex",
        "puffy_fluffy",
        "sparse",
        "ticked",
        "double_coat",
    ],
    'eye_shape': [
        "round",
        "almond",
        "upturned",
        "downturned",
        "cat_eye",
        "wide_set",
        "close_set",
        "big",
        "small",
        "hooded",
        "bedroom",
        "prominent",
    ],
    'base_color': [
        "black",
        "white",
        "brown",
        "gray",
        "ginger",
        "cream",
        "chocolate",
        "cinnamon",
        "blue",
        "lilac",
        "fawn",
        "red",
    ],
    'accent_color': [
        "tabby",
        "tortoiseshell",
        "calico",
        "point",
        "smoke",
        "silver",
        "golden",
        "chocolate",
        "cinnamon",
        "creamy",
        "blue",
        "lilac",
    ],
    'highlight_color': [
        "white",
        "cream",
        "silver",
        "golden",
        "copper",
        "chocolate",
        "cinnamon",
        "blue",
        "lilac",
        "fawn",
        "red",
        "apricot",
    ],
    'eye': [
        "amber",
        "blue",
        "copper",
        "gold",
        "green",
        "hazel",
        "orange",
        "yellow",
        "odd_eyes",
        "aquamarine",
        "emerald",
        "topaz",
    ]
}

def generate_random_cat():
    cat = {}
    for attribute, options in attributes.items():
        cat[attribute] = random.choice(options)
    return cat

def generate_population(population_size):
    population = []
    for _ in range(population_size):
        cat = generate_random_cat()
        population.append(cat)
    return population

def evaluate_fitness(cat):
    # Example fitness evaluation: Count the number of desired attributes
    desirable_attributes = ['round', 'blue', 'longhair']  # Example desirable attributes
    fitness = sum(attribute in cat.values() for attribute in desirable_attributes)
    return fitness

def selection(population, fitness_scores):
    # Example selection: Select individuals with higher fitness scores
    selected_population = []
    population_size = len(population)
    total_fitness = sum(fitness_scores)

    # Calculate selection probabilities based on fitness scores
    probabilities = [fitness / total_fitness for fitness in fitness_scores]

    # Perform roulette wheel selection
    for _ in range(population_size):
        selected_population.append(random.choices(population, probabilities)[0])

    return selected_population

def crossover(parent1, parent2):
    # Example crossover: Perform single-point crossover
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = {key: parent1[key] if i < crossover_point else parent2[key] for i, key in enumerate(parent1)}
    child2 = {key: parent2[key] if i < crossover_point else parent1[key] for i, key in enumerate(parent1)}
    return child1, child2

def mutation(cat, mutation_rate):
    # Example mutation: Randomly change an attribute with a given mutation rate
    mutated_cat = dict(cat)
    for attribute in attributes:
        if random.random() < mutation_rate:
            mutated_cat[attribute] = random.choice(attributes[attribute])
    return mutated_cat

def create_next_generation(population, mutation_rate):
    fitness_scores = [evaluate_fitness(cat) for cat in population]
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

def genetic_algorithm(population_size, mutation_rate, generations):
    population = generate_population(population_size)
    best_fitness = 0
    best_cat = None

    for generation in range(generations):
        fitness_scores = [evaluate_fitness(cat) for cat in population]
        max_fitness = max(fitness_scores)
        max_index = fitness_scores.index(max_fitness)
        best_cat = population[max_index]
        best_fitness = max_fitness

        population = create_next_generation(population, mutation_rate)

        print(f"Generation {generation+1}: Best Fitness = {best_fitness}")
        print(best_cat)
        print("-------------------------")

    print("Genetic Algorithm Complete!")
    print(f"Best Fitness: {best_fitness}")
    print("Best Cat:")
    print(best_cat)

# Example usage
population_size = 10
mutation_rate = 0.1
generations = 10

genetic_algorithm(population_size, mutation_rate, generations)