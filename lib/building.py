
class Building:
    homes = []
    stores = []

    def __init__(self, type):
        self.type = type
        self.occupants = 0
        self.limit = 0
        if self.type == 'house':
            self.limit = 4
        else:
            self.limit = 8

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

