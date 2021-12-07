'''Part 1 - Keeping it Classy'''

import random


class Product:
    '''parent class for acme Product Features'''
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.identifier = random.randint(1000000, 9999999)
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability

    # what is my product stealability status
    def stealability(self):
        '''return the product stealability status'''
        stealability = self.price / self.weight

        if stealability < 0.5:
            return 'Not so stealable...'
        if 0.5 <= stealability < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable'

    # Is my product going to explode ?
    def explode(self):
        '''return the product stealability status'''
        explode_status = self.flammability * self.weight

        if explode_status < 10:
            return '...fizzle.'
        if 10 <= explode_status < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'

# Creating boxing Gloves child class
# A Proper Inheritance'''


class BoxingGlove(Product):
    '''Create a child class'''
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        '''returing my product child class name'''
        return '...it\'s a glove.'

    def punch(self):
        '''returing my gloves punch status'''
        if self.weight < 5:
            return 'That tickles.'
        if 5 <= self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
