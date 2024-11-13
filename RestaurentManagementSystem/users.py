from abc import ABC
from order import Order

class User(ABC):
    def __init__(self, name, email, phone, address):
        super().__init__()
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        
class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()
        
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
        
    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print(f"{item_name} quantity excceded!")
            else:
                self.cart.add_item(item, quantity)
                print("Item added successfully.")
        else:
            print("Item not found.")
            
    def view_cart(self):
        print("** View Cart **")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
        print(f"Total price: {self.cart.total_price}")
        
    def pay_bill(self, restaurent): 
        print(f"{self.cart.total_price} paid successfully. Thank you!")
        self.cart.clear(restaurent) 
    
class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary
        
class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        
    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)
        
    def view_employee(self, resturent):
        resturent.view_employee()
        
    def add_new_item(self, resturent, item):
        resturent.menu.add_item(item)
        
    def delete_item(self, restaurent, item_name):
        restaurent.menu.remove_item(item_name)
            
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
            

