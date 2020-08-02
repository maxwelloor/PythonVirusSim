import random

class Person:

    people = []
    infection_count = 0
    recoveries = 0
    death_count = 0
    
    def __init__(self, home):
        self.infected = False
        self.immune = False
        self.days_infected = 0
        self.mask_on = False
        self.in_building = None

        self.home = home
        self.location = self.home

        Person.people.append(self)

    def infect(self):
        if not self.infected and not self.immune:
            self.infected = True
            Person.infection_count += 1
            print('Person Infected.')

    def kill(self):
        print("Someone has died.")
        Person.death_count += 1
        Person.people.remove(self)

    def recover(self):
        print("Someone has recovered!")
        Person.recoveries += 1
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
                
