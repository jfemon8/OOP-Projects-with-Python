from user import Seller, Buyer
from order import Order
from shop import Shop
from make_product import MakeProduct
from product import Products

my_shop = Shop("Emon's Shop", "Barishal")

def seller_menu():
    name = input('Enter your name: ')
    phone = input('Enter your phone number: ')
    address = input('Enter your address: ')
    age = int(input('Enter your age: '))
    
    seller = Seller(name=name, phone=phone, address=address, age=age)
    
    while True:
        print(f'\nHello {seller.name}!\n')
        print('1. Add new product')
        print('2. Remove existing product')
        print('3. View all products')
        print('4. Exit')
        option = int(input('Please enter an option: '))
        
        if option==1:
            product_name = input('Enter product name: ')
            price = int(input('Enter product price: '))
            quantity = int(input('Enter product qunatity: '))
            seller.add_product(my_shop, product_name, price, quantity)
        elif option==2:
            product_name = input('Enter product name: ')
            seller.delete_product(my_shop, product_name)
        elif option==3:
            seller.view_products(my_shop)
        elif option==4:
            break
        else:
            print('Invalid option!')
            
def buyer_menu():
    name = input('Enter your name: ')
    phone = input('Enter your phone number: ')
    address = input('Enter your address: ')
    email = input('Enter your email: ')
    
    buyer = Buyer(name=name, phone=phone, address=address, email=email)
    
    while True:
        print(f'\nHey {buyer.name}!\n')
        print('1. View all products')
        print('2. Add product to cart')
        print('3. View cart')
        print('4. Remove product from cart')
        print('5. Make payment')
        print('6. Exit')
        option = int(input('Please enter an option: '))
        
        if option==1:
            buyer.view_products(my_shop)
        elif option==2:
            product_name = input('Enter product name: ')
            quantity = int(input('Enter product qunatity: '))
            buyer.add_to_cart(my_shop, product_name, quantity)
        elif option==3:
            buyer.view_cart()
        elif option==4:
            product_name = input('Enter product name: ')
            buyer.remove_item(my_shop, product_name)
        elif option==5:
            buyer.make_payment(my_shop)
        elif option==6:
            break
        else:
            print('Invalid option!')
  
print(f'** Welcome to {my_shop.name} **')          
while True:
    print('\n1. Seller')
    print('2. Buyer')
    print('3. Exit')
    op = int(input('Please enter your choice: '))
    
    if op==1:
        seller_menu()
    elif op==2:
        buyer_menu()
    elif op==3:
        break
    else:
        print('Invalid choice!')
        
