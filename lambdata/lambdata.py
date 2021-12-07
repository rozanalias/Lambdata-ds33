'''Buliding a class for item price'''


class ItemPrice:
    '''Original Price'''
    def __init__(self, original_price=0):
        self.price = original_price

    def sales_tax(self, estimated_sales_tax):
        '''return the tax amount addition to the original price'''
        self.price += estimated_sales_tax

    def saving(self, discount):
        '''return the item price after the disscount'''
        self.price = self.price - discount
        print('You saved', discount)

    def __repr__(self):
        '''item price'''
        return f"Original Price: ${self.price}"    