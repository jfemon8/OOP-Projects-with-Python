class Menu:
    def __init__(self):
        self.items = []
        
    def add_item(self, name):
        self.items.append(name)
        
    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
        
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f'{item_name} deleted successfully from the menu.')
        else:
            print(f'{item_name} not found in the menu.')
        
    def show_menu(self):
        print("*** Menu ***")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')
 
           