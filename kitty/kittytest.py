import random
import datetime

ct = datetime.datetime.now()

# genes = (uint256) The genetic code of the kitty.
# birth_time = (uint64) The exact timestamp of the kitty’s birth.
# cooldown_end_block = (uint64) The minimum time that a kitty has to wait before it can breed again.
# matron_id = (uint32) id of the cats mother
# sire_id = (uint32) id of the cats father
# siring_with_id = (uint32) If the cat isn’t pregnant then this is set to 0. However, if pregnant then this is set to the Id of the father
# cooldown_index = (uint16) How much longer the cat has to wait before it can breed again.
# generation = (uint16) The generation of the cat. The first kitties produced were generation 0.

kitty_1 = {
    'id': 1,
    'genes': [random.randint(0, 1) for _ in range(256)],
    'birth_time': ct.timestamp(),
    'cooldown_end_block': 123,
    'matron_id': 123,
    'sire_id': 123,
    'siring_with_id': 123,
    'cooldown_index': 123,
    'generation': 123,
}

cooldown_time_per_generation = {
    '0,1': '1 minute',
    '2,3': '2 minutes',
    '4,5': '5 minutes',
    '6,7': '10 minutes',
    '8,9': '30 minutes',
    '10,11': '1 hour',
    '12,13': '2 hours',
    '14,15': '1 hour',
    '16,17': '1 hour',
    '18,19': '1 minute',
    '20,21': '1 minute',
    '22,23': '1 minute',
    '24,25': '1 minute',
    '26+': '1 minute',
}


class Kitty:
    def __init__(self, id):
        self.id = id
        self.genes = 0000000  # (uint256) The genetic code of the kitty.
        self.birth_time = 121212  # (uint256) The exact timestamp of the kitty’s birth.
        self.cooldown_end_block = 3123123  # (uint256) The minimum time that a kitty has to wait before it can breed again.
        self.matron_id: 0  # (uint256) id of the cats mother
        self.sire_id: 0  # (uint256) id of the cats father
        self.siring_with_id: 0  # (uint256) If the cat isn’t pregnant then this is set to 0. However, if pregnant then this is set to the Id of the father
        self.cooldown_index: 0  # (uint256) How much longer the cat has to wait before it can breed again.
        self.generation: 0  # (uint256) The generation of the cat. The first kitties produced were generation 0.

# class FirstKitty(Kitty):
#     def __init__(self, id):
#         super().__init__(id)
#         self.id = id
#         self.genes = [random.randint(0, 1) for _ in range(256)]
#         self.birth_time = 121212
#         self.cooldown_end_block = 3123123
#         self.matron_id: 0
#         self.sire_id: 0
#         self.siring_with_id: 0
#         self.cooldown_index: 0
#         self.generation: 0

# def breed_with(matron_id: int, sire_id: int):
#     matron = Kitty(matron_id)
#     sire = Kitty(sire_id)
#     matron.siring_with_id = sire_id
