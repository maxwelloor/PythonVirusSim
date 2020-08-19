import random

class Virus:

    def __init__(self, spread_chance, mortality, noticibility, r_chance, r_time):

        # All these are chances out of 1000.
        self.spread_chance = spread_chance
        self.mortality = mortality
        self.noticibilty = noticibility
        self.recovery_chance = r_chance
        self.recovery_time = r_time
        self.noticed = False

    def roll_spread_chance(self):
        roll = random.randint(0, 1000)

        if roll <= self.spread_chance:
            return True
        else:
            return False

    def roll_death_chance(self):
        roll = random.randint(0, 1000)

        if roll <= self.mortality:
            return True
        else:
            return False

    def roll_notice_chance(self, current_deaths, current_infections):
        roll = random.randint(0, 1000)

        if roll <= self.noticibilty * current_deaths:
            self.notice()

    def roll_recovery_chance(self):
        roll = random.randint(0, 1000)

        if roll <= self.recovery_chance:
            return True
        else:
            return False

    def notice(self):
        if not self.noticed:
            self.noticed = True
            print('The virus has been noticed!')


        

