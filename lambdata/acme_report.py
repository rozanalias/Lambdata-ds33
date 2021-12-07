'''Class Report'''

from random import randint, choice, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    '''Generate and add random products.'''
    products = []
    for _ in range(num_products):
        names = choice(ADJECTIVES) + " " + choice(NOUNS)
        prices = randint(5, 100)
        weights = randint(5, 100)
        flammabilities = uniform(0.0, 2.5)

        product = Product(names, prices, weights, flammabilities)
        products.append(product)

    return products


def inventory_report(products):
    '''prints a nice summary for product list'''
    names = set()
    sum_prices = 0
    sum_weight = 0
    sum_flamm = 0
    # Loop over the products to calculate the report
    for product in products:
        names.add(product.name)
        sum_prices = sum_prices + product.price
        sum_weight = sum_weight + product.weight
        sum_flamm = sum_flamm + product.flammability
    # printing nice summary

    nunique = len(names)
    avg_price = sum_prices / len(products)
    avg_weight = sum_weight / len(products)
    avg_flamm = sum_flamm / len(products)
    print('Unique product names:', nunique)
    print('Average price: ', avg_price)
    print('Average weight: ', avg_weight)
    print('Average flammability:', avg_flamm)


if __name__ == '__main__':
    inventory_report(generate_products())
