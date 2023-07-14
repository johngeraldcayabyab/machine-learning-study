import random
from datetime import datetime

import datetime;

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


def calculate_cooldown_index():
    cooldown_end_block = 0
    offsprings = 0
    elapsed_time_since_delivery = 0
    return (cooldown_end_block * offsprings) - elapsed_time_since_delivery


kitty_1 = {
    'genes': [random.randint(0, 1) for _ in range(256)],
    'birth_time': datetime.datetime.now().timestamp(),
    'cooldown_end_block': cooldown_speed['0,1'],
    'matron_id': 0,
    'sire_id': 0,
    'siring_with_id': 0,
    'cooldown_index': calculate_cooldown_index(),
    'generation': 1
}

kitty_2 = {
    'genes': [random.randint(0, 1) for _ in range(256)],
    'birth_time': datetime.datetime.now().timestamp(),
    'cooldown_end_block': cooldown_speed['0,1'],
    'matron_id': 0,
    'sire_id': 0,
    'siring_with_id': 0,
    'cooldown_index': calculate_cooldown_index(),
    'generation': 1
}

print(sum(kitty_1['genes']), sum(kitty_2['genes']))
