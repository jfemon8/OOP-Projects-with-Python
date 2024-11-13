
class Order:
    def __init__(self):
        self.items = {}
        
    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
            
    def remove(self, item):
        if item in self.items:
            del self.items[item]
       
    @property     
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    
    def clear(self, restaurent):
        for item, quantity in self.items.items():
            menu_item = restaurent.menu.find_item(item.name)
            menu_item.quantity -= quantity
        self.items = {}
                
