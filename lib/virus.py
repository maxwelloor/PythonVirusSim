import random

class Virus:

    def __init__(self, spread_chance, lethality, noticibility):

        # All these are chances out of 100.
        self.spread_chance = spread_chance
        self.lethality = lethality
        self.noticibilty = noticibility

    def roll_spread_chance(self):
        roll = random.randint(0, 100)

        if roll < self.spread_chance:
            return True
        else:
            return False

    def roll_death_chance(self):
        roll = random.randint(0, 100)

        if roll < self.lethality:
            return True
        else:
            return False


        

