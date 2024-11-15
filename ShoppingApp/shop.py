from product import Products

class Shop:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.products = Products()
        
    