'''Measure twice, Test once'''

from acme import Product
from acme_report import generate_products


def test_default_product_price():
    """Test default product price being 10."""
    prod = Product('Test Product')
    assert prod.price == 10


def test_default_product():
    """Test default product weight being 20."""
    prod = Product('Test Product')
    assert prod.weight == 20


def test_stealability_and_explode_of_product():
    '''testing product's stealability and explode
    with weight 20 and price 40'''
    prod_toy = Product('Toy', price=40, weight=20)
    assert prod_toy.stealability() == 'Very stealable'
    assert prod_toy.explode() == '...boom!'


def test_default_num_products():
    '''testing if my list length is 30'''
    assert len(generate_products()) == 30
