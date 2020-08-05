import random

class Virus:

    def __init__(self, spread_chance, lethality, noticibility):

        # All these are chances out of 1000.
        self.spread_chance = spread_chance
        self.lethality = lethality
        self.noticibilty = noticibility
        self.noticed = False

    def roll_spread_chance(self):
        roll = random.randint(0, 1000)

        if roll <= self.spread_chance:
            return True
        else:
            return False

    def roll_death_chance(self):
        roll = random.randint(0, 1000)

        if roll <= self.lethality:
            return True
        else:
            return False

    def roll_notice_chance(self, current_deaths, current_infections):
        roll = random.randint(0, 1000)

        if roll <= self.noticibilty * (10 * current_deaths):
            self.notice()

    def notice(self):
        if not self.noticed:
            self.noticed = True
            print('The virus has been noticed!')


        

