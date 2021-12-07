'''test my ItemPrice class '''

import pytest
from lambdata import ItemPrice

@pytest.fixture
def macbook_pro():
    '''return my macbook pro price'''
    return ItemPrice(2399)

def test_macbook_pro_price(macbook_pro):
    '''testing my macbook price to be 2399'''
    assert macbook_pro.price == 2399
    
def test_macbook_pro_disscount(macbook_pro):
    '''testing my macbook price with disccount 500 to be 1899'''
    macbook_pro.saving(500)
    assert macbook_pro.price == 1899

def test_macbook_pro_texas(macbook_pro):
    '''testing my macbook price with sales tax $168.62'''
    macbook_pro.sales_tax(168.62)
    assert macbook_pro.price == 2567.62
