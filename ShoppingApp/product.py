class Products:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        
    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f'{item_name} is removed from the shop successfully.')
        else:
            print(f'{item_name} is not found in the shop')
            
    def show_products(self):
        print('*** Products ***')
        print('Name\tPrice\tQuantity')
        for item in self.items:
            if item.quantity > 0:
                print(f'{item.name}\t{item.price}\t{item.quantity}')
