import random

class TimeManager:
    
    def __init__(self):
        self.time = 1
        self.day = 1

    # The code that runs when the day changes
    def day_change(self, people, virus, infection_count, death_count, recovery_count):
        self.time = 1

        for person in people:
            person.staying_home_today = False

        everyone_infected = True
        recoveries = recovery_count
        deaths = death_count
        current_infections = infection_count

        virus.roll_notice_chance(death_count, current_infections)

        for person in people:
            if person.infected:
                person.days_infected += 1
                if virus.roll_death_chance():
                    person.kill()
                    deaths += 1

        people[0].decide_stay_home(virus, people)

        print('New Day! Infection Count: ' + str(infection_count) + ', Death Count: ' + str(deaths) + ', Recovery Count: ' + str(recoveries))

        self.day += 1

    # The code that runs once a simulated hour (basically every loop)
    def time_change(self, people, virus, stores):

        if self.time >= 1 and self.time < 12:

            for p in people:
                if p.location != p.home:
                    p.location.occupants -= 1

                    if p.infected:
                        p.location.sick_people_here -= 1

                    p.location = p.home

                    if p.infected:
                        p.location.sick_people_here += 1

                    p.home.occupants += 1

            for person in people:
                if person.infected:
                    if person.location == person.home:
                        for p in people:
                            if p.home == person.location:
                                if virus.roll_spread_chance():
                                    p.infect()

        if self.time >= 12:
            for person in people:
                if person.location == person.home and not person.staying_home_today:
                    while True:
                        new_location = random.choice(stores)
                        if new_location.occupants >= new_location.limit:
                            continue
                        else:
                            new_location.occupants += 1
                            person.location.occupants -= 1
                            if person.infected:
                                person.location.sick_people_here -= 1
                                new_location.sick_people_here += 1
                            person.location = new_location
                            break
            
            for person in people:
                if person.infected:
                    location_to_check = person.location
                else:
                    continue

                for p in people:
                    if person == p:
                        continue
                    else:
                        if p.location == location_to_check:
                            if virus.roll_spread_chance():
                                p.infect()

        for person in people:
            if person.infected:
                if person.days_infected >= virus.recovery_time:
                    if virus.roll_recovery_chance():
                        person.recover()

        
        self.time += 1

