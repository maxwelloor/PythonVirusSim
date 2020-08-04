import pygame

class Building:
    homes = []
    stores = []

    h_x = 0
    h_y = 20
    h_count = 0

    s_x = 0
    s_y = 540
    s_count = 0

    def __init__(self, type):
        self.type = type
        self.occupants = 0
        self.occupant_bar = []
        self.limit = 0
        self.img = pygame.image.load('sprites\\building.png')

        for x in range(1, 14):
            self.occupant_bar.append(pygame.image.load('sprites\\person_bar\\b' + str(x) + '.png'))

        if self.type == 'house':
            self.limit = 4

            if Building.s_count >= 14:
                Building.s_count = 0
                Building.s_x = 0
                Building.s_y += 158

            if Building.h_count >= 14:
                Building.h_count = 0
                Building.h_x = 0
                Building.h_y += 158

            self.x = Building.h_x
            self.y = Building.h_y

            Building.h_x += 138
            Building.h_count += 1

        else:
            self.limit = 12
            self.x = Building.s_x
            self.y = Building.s_y

            Building.s_x += 138
            Building.s_count += 1

    def render(self, display):
        display.blit(self.img, (self.x, self.y))
        
        display.blit(self.occupant_bar[self.occupants], (self.x + 3, self.y + 128))


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

