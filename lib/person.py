import random

class Person:

    people = []
    infection_count = 0
    current_infections = 0
    recoveries = 0
    death_count = 0
    
    def __init__(self, home):
        self.infected = False
        self.immune = False
        self.days_infected = 0
        self.mask_on = False

        self.home = home
        self.location = self.home
        self.home.occupants += 1

        Person.people.append(self)

    def infect(self):
        if not self.infected and not self.immune:
            self.infected = True
            self.location.infections_spread_here += 1
            Person.infection_count += 1
            Person.current_infections += 1
            print('Person Infected.')

    def kill(self):
        print("Someone has died.")
        Person.death_count += 1
        Person.current_infections -= 1
        self.location.occupants -= 1
        self.home.deaths_here += 1
        Person.people.remove(self)

    def recover(self):
        print("Someone has recovered!")
        Person.recoveries += 1
        Person.current_infections -= 1
        self.infected = False
        self.immune = True

    @classmethod
    def generate_people(cls, homes, starting_infections):
        for home in homes:
            for x in range(0, 4):
                new_person = Person(home)

        for x in range(0, starting_infections):
            while True:
                temp = random.choice(Person.people)
                if temp.infected:
                    continue
                else:
                    temp.infect()
                    break
                
