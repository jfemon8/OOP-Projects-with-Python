class Order:
    def __init__(self):
        self.items = {}
        
    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
            
    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
            print(f'{item.name} removed from the cart.')
        else:
            print(f'{item.name} is not found in the cart.')
            
    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    
    def clear(self, shop):
        for item, quantity in self.items.items():
            shop_item = shop.products.find_item(item.name)
            shop_item.quantity -= quantity
        self.items = {}