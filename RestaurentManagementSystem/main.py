from food_item import FoodItem
from menu import Menu
from order import Order
from restaurent import Restaurent
from users import Admin, Employee, Customer

my_res = Restaurent("My Restaurent")

def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")
    
    customer = Customer(name=name, email=email, phone=phone, address=address)
    
    while True:
        print(f'Hello {customer.name}!')
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View cart")
        print("4. Pay bill")
        print("5. Exit")
        choice = int(input("Please enter an option: "))
        
        if choice == 1:
            customer.view_menu(my_res)
        elif choice == 2:
            item_name = input("Please enter the item name: ")
            item_quantity = int(input("Enter your desired quantity: "))
            customer.add_to_cart(my_res, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill(my_res)
        elif choice == 5:
            break
        else:
            print("Invalid input")
            
def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")
    
    admin = Admin(name=name, email=email, phone=phone, address=address)
    
    while True:
        print(f'Hello {admin.name}!')
        print("1. Add new item")
        print("2. Add new employee")
        print("3. View employee")
        print("4. View menu")
        print("5. Delete item")
        print("6. Exit")
        choice = int(input("Please enter an option: "))
        
        if choice == 1:
            item_name = input("Please enter the item name: ")
            item_price = int(input("Enter price: "))
            item_quantity = int(input("Enter quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(my_res, item)
        elif choice == 2:
            name = input("Enter employee name: ")
            email = input("Enter employee email: ")
            phone = input("Enter employee phone: ")
            address = input("Enter employee address: ")
            age = int(input("Enter employee age: "))
            designation = input("Enter employee designation: ")
            salary = int(input("Enter employee salary: "))
            employee = Employee(name, email, phone, address, age, designation, salary)
            admin.add_employee(my_res,employee)
        elif choice == 3:
            admin.view_employee(my_res)
        elif choice == 4:
            admin.view_menu(my_res)
        elif choice == 5:
            item_name = input("Enter item name: ")
            admin.delete_item(my_res, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid input")
         
print(f"Hey, welcome to {my_res.name}!!")   
while True:
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        admin_menu()
    elif choice == 2:
        customer_menu()
    elif choice == 3:
        break
    else:
        print("Invalid input.")


