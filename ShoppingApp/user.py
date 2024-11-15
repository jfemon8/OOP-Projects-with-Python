from make_product import MakeProduct
from order import Order

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
class Seller(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        
    def add_product(self, shop, name, price, quantity):
        item = MakeProduct(name, price, quantity)
        shop.products.add_item(item)
        
    def delete_product(self, shop, product_name):
        shop.products.remove_item(product_name)
        
    def view_products(self, shop):
        shop.products.show_products()
        
class Buyer(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.cart = Order()
        
    def view_products(self, shop):
        shop.products.show_products()
        
    def add_to_cart(self, shop, item_name, quantity):
        item = shop.products.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print(f'{item_name} quantity excceded!')
            else:
                self.cart.add_item(item, quantity)
        else:
            print(f'{item_name} not found in the shop')
            
    def view_cart(self):
        print('*** Cart ***')
        print('Name\tPrice\tQuantity')
        for item, quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
        print(f'Total price: {self.cart.total_price}')
        
    def make_payment(self, shop):
        print(f'Taka {self.cart.total_price} is paid successfully. Thank you.')
        self.cart.clear(shop)
        
    def remove_item(self, shop, item_name):
        item = shop.products.find_item(item_name)
        if item:
            self.cart.remove_item(item)
        else:
            print(f'{item_name} not found in the shop')