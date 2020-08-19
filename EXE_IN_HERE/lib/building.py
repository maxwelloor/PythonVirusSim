import pygame

class Building:
    pygame.font.init()
    homes = []
    stores = []

    first = True
    black = (0, 0, 0)

    h_x = 0
    h_y = 20
    h_count = 0

    s_x = 0
    s_y = 0
    s_count = 0

    total_y = 0

    font = pygame.font.SysFont('arial', 16)
    store_img = pygame.image.load('sprites\\building.png')
    house_img = pygame.image.load('sprites\\house.png')
    infection_counter_img = pygame.image.load('sprites\\infection_symbol.png')
    death_counter_img = pygame.image.load('sprites\\death_symbol.png')
    sick_counter_img = pygame.image.load('sprites\\sick_counter.png')

    occupant_bar_store = []
    occupant_bar_house = []

    for x in range(1, 14):
        occupant_bar_store.append(pygame.image.load('sprites\\person_bar_store\\b' + str(x) + '.png'))

    for x in range(1, 6):
        occupant_bar_house.append(pygame.image.load('sprites\\person_bar_house\\b' + str(x) + '.png'))

    def __init__(self, type):
        self.type = type
        self.occupants = 0
        self.occupant_bar = []
        self.limit = 0
        self.infections_spread_here = 0
        self.sick_people_here = 0
        self.deaths_here = 0
        self.img = Building.store_img
        self.ic_img = Building.infection_counter_img
        self.dc_img = Building.death_counter_img
        self.sc_img = Building.sick_counter_img
        self.occupant_bar_house = Building.occupant_bar_house
        self.occupant_bar_store = Building.occupant_bar_store

        if self.type == 'house':
            self.limit = 4
            self.img = Building.house_img

            if Building.h_count >= 14:
                Building.h_count = 0
                Building.h_x = 0
                Building.h_y += 168
                Building.total_y += 168

            self.x = Building.h_x
            self.y = Building.h_y

            Building.h_x += 138
            Building.h_count += 1

        else:

            self.limit = 12
            self.img = Building.store_img

            if Building.first:
                Building.first = False
                Building.s_y = Building.h_y + 200
                Building.total_y += 200
            
            if Building.s_count >= 14:
                Building.s_count = 0
                Building.s_x = 0
                Building.s_y += 168
                Building.total_y += 168

            self.x = Building.s_x
            self.y = Building.s_y

            Building.s_x += 138
            Building.s_count += 1

    def render(self, display, offset):
        # The building image
        display.blit(self.img, (self.x, self.y + offset))
        
        # The occupant bar
        if self.type == 'store':
            display.blit(self.occupant_bar_store[self.occupants], (self.x + 3, self.y + 128 + offset))
        else:
            display.blit(self.occupant_bar_house[self.occupants], (self.x + 3, self.y + 128 + offset))

        # The infection counter
        display.blit(self.ic_img, (self.x, self.y + offset))

        # The sick person counter
        display.blit(self.sc_img, (self.x, self.y + offset + 20))
        display.blit(Building.font.render('x' + str(self.sick_people_here), 1, Building.black), (self.x + self.sc_img.get_width(), self.y + offset + 20))

        # the death counter
        if self.type == 'house':
            display.blit(self.dc_img, (self.x, self.y + offset + 40))
            display.blit(Building.font.render('x' + str(self.deaths_here), 1, Building.black), (self.x + self.dc_img.get_width(), self.y + offset + 40))

        i_count = Building.font.render('x' + str(self.infections_spread_here), 1, Building.black)
        display.blit(i_count, (self.x + Building.infection_counter_img.get_width(), self.y + offset))



    @classmethod
    def generate_buildings(cls, num_of_homes, num_of_stores):
        for x in range(0, num_of_homes):
            cls.homes.append(Building('house'))
            
        for x in range(0, num_of_stores):
            cls.stores.append(Building('store'))


    @classmethod
    def get_stores(cls):
        return cls.stores

    @classmethod
    def get_homes(cls):
        return cls.homes

