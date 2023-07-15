# class Kitty:
#     def __init__(
#             self,
#             genes: bytes,  # uint32
#             birth_time: bytes,  # uint64
#             cooldown_end_block: bytes,  # uint64
#             matron_id: bytes,  # uint32
#             sire_id: bytes,  # uint32
#             siring_with_id: bytes,  # uint32
#             cooldown_index: bytes,  # uint16
#             generation: bytes  # uint16
#     ):
#         # genetic code of the kitty
#         self.genes = genes
#         # The exact timestamp of the kitty’s birth.
#         self.birth_time = birth_time
#         # The minimum time that a kitty has to wait before it can breed again.
#         self.cooldown_end_block = cooldown_end_block
#         # The ID of the cat’s mother.
#         self.matron_id = matron_id
#         # The ID of the cat’s father.
#         self.sire_id = sire_id
#         # If the cat isn’t pregnant then this is set to 0. However, if pregnant then this is set to the Id of the father
#         self.siring_with_id = siring_with_id
#         # How much longer the cat has to wait before it can breed again.
#         self.cooldown_index = cooldown_index,
#         # The generation of the cat. The first kitties produced were generation 0.
#         self.generation = generation
#
#
# class KittyBreeding:
#     def breed_with(self, matron_id: bytes, sire_id=123):
