import random

class Person:

    people = []
    infection_count = 0
    current_infections = 0
    recoveries = 0
    death_count = 0
    
    def __init__(self, home, average_iq, iq_range):
        self.infected = False
        self.immune = False
        self.days_infected = 0
        self.mask_on = False
        self.staying_home_today = False

        # this sets the iq based on average iq and iq range
        iq_change = random.randint(iq_range * -1, iq_range)
        self.iq = average_iq + iq_change

        if self.iq > 100:
            self.iq = 100
        elif self.iq < 0:
            self.iq = 0

        print(self.iq)

        self.home = home
        self.location = self.home
        self.home.occupants += 1

        Person.people.append(self)

    def infect(self):
        if not self.infected and not self.immune:
            self.infected = True
            self.location.infections_spread_here += 1
            self.location.sick_people_here += 1
            Person.infection_count += 1
            Person.current_infections += 1
            print('Person Infected.')

    def kill(self):
        print("Someone has died.")
        Person.death_count += 1
        Person.current_infections -= 1
        self.location.occupants -= 1
        self.location.sick_people_here -= 1
        self.home.deaths_here += 1
        Person.people.remove(self)

    def recover(self):
        print("Someone has recovered!")
        Person.recoveries += 1
        Person.current_infections -= 1
        self.location.sick_people_here -= 1
        self.infected = False
        self.immune = True

    @classmethod
    def generate_people(cls, homes, starting_infections, average_iq, iq_range):

        av_iq = average_iq
        iq_rng = iq_range

        # Average IQ is a number from 1 to 100 that determines how smart people are.
        # IQ range is the range that someones IQ can change either in the positive or negative direction from the average IQ.

        for home in homes:
            for x in range(0, 4):
                new_person = Person(home, av_iq, iq_rng)

        for x in range(0, starting_infections):
            while True:
                temp = random.choice(Person.people)
                if temp.infected:
                    continue
                else:
                    temp.infect()
                    break

    def decide_stay_home(self, virus, people):

        for person in people:
            # 10% chance they stay home if they arent infected just because they feel like it but 40% chance if the virus has been spotted.
            if not person.infected:
                roll = random.randint(0, 100)

                # Person stays home no matter what if they have 80 iq or higher and the virus has been noticed
                if person.iq >= 80 and virus.noticed:
                    person.staying_home_today = True


                # 10% to stay home any time. 40% to stay home if the virus has been spotted
                if not virus.noticed:
                    if roll <= 10:
                        person.staying_home_today = True
                else:
                    if roll <= 40:
                        person.staying_home_today = True

            # The rolls for if they are infected
            else:
                roll = random.randint(0, 100 + person.iq)

                # Chance to stay home if they are infected and the virus has not been noticed.
                if not virus.noticed:
                    if roll >= 100:
                        person.staying_home_today = True
                # Chance to stay home if the person is infected and the virus is known
                else:
                    if roll >= 30:
                        person.staying_home_today = True




                
