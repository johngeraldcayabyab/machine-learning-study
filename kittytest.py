class Kitty(id):
    id = id
    genes = 0000000  # The genetic code of the kitty.
    birthTime = 121212  # The exact timestamp of the kitty’s birth.
    cooldownEndBlock = 3123123  # The minimum time that a kitty has to wait before it can breed again.
    matronId: 1  # id of the cats mother
    sireId: 2  # id of the cats father
    siringWithId: 0  # If the cat isn’t pregnant then this is set to 0. However, if pregnant then this is set to the Id of the father
    cooldownIndex: 123123213  # How much longer the cat has to wait before it can breed again.
    generation: 10  # The generation of the cat. The first kitties produced were generation 0.




def breedWith(matronId: int, sireId: int):
    matron = Kitty(matronId)
    sire = Kitty(sireId)
    matron.siringWithId = sireId
