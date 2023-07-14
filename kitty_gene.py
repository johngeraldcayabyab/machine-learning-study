import random
import numpy as np
from datetime import datetime
import json

cooldown_speed = {
    '0,1': '1 minute',
    '2,3': '2 minutes',
    '4,5': '5 minutes',
    '6,7': '10 minutes',
    '8,9': '30 minutes',
    '10,11': '1 hour',
    '12,13': '2 hours',
    '14,15': '4 hours',
    '16,17': '8 hours',
    '18,19': '16 hours',
    '20,21': '24 hours',
    '22,23': '2 days',
    '24,25': '4 days',
    '26+': '1 week',
}

with open('attributes.json') as attributes_file:
    file_contents = attributes_file.read()

attributes = json.loads(file_contents)

gene_positions = {
    'p': 37.5,
    'h1': 9.4,
    'h2': 2.3,
    'h3': 0.8
}


def generate_initial_genes():
    genome = []
    for attribute, genes in attributes.items():
        choices = []
        for segment, gene in genes.items():
            choices.append(gene)
        genetic_code = np.array(random.choices(choices, k=4)).flatten()
        genome.append(genetic_code)
    return np.array(genome).flatten()


def calculate_cooldown_index():
    cooldown_end_block = 0
    offsprings = 0
    elapsed_time_since_delivery = 0
    return (cooldown_end_block * offsprings) - elapsed_time_since_delivery


def get_attribute(attribute, genes):
    phenotypes = []
    attribute_genes = attributes[attribute].items()
    # print(attribute_genes)

    for gene in genes:
        for attribute_gene, source_gene in attribute_genes:

            if np.array_equal(gene, source_gene):
                phenotypes.append(attribute_gene)

    return phenotypes


def attribute_breakdown(genome):
    attribute_chunked = [genome[i:i + 16] for i in range(0, len(genome), 16)]
    phenotypes = {}
    counter = 0
    for attribute, genes in attributes.items():
        chunked = [attribute_chunked[counter][i:i + 4] for i in range(0, len(attribute_chunked[counter]), 4)]
        phenotypes[attribute] = get_attribute(attribute, chunked)
        counter += 1
    return phenotypes


kitty_1 = {
    'genome': generate_initial_genes(),
    'birth_time': datetime.now().timestamp(),
    'cooldown_end_block': cooldown_speed['0,1'],
    'matron_id': 0,
    'sire_id': 0,
    'siring_with_id': 0,
    'cooldown_index': calculate_cooldown_index(),
    'generation': 1
}

kitty_2 = {
    'genome': generate_initial_genes(),
    'birth_time': datetime.now().timestamp(),
    'cooldown_end_block': cooldown_speed['0,1'],
    'matron_id': 0,
    'sire_id': 0,
    'siring_with_id': 0,
    'cooldown_index': calculate_cooldown_index(),
    'generation': 1
}

# print(attribute_breakdown(kitty_1['genome']))
print(attribute_breakdown(kitty_2['genome']))
