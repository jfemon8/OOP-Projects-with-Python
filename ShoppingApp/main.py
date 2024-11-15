from user import Seller, Buyer
from order import Order
from shop import Shop
from make_product import MakeProduct
from product import Products

my_shop = Shop("Emon's Shop", "Barishal")

def signin_menu():
    while True:
        print('\n1. Signin as a seller')
        print('2. Signin as a buyer')
        print('3. Back to main menu')
        n = int(input('Enter an option: '))
        
        if n==1:
            name = input('Enter your username: ')
            password = input('Enter your password: ')
            flag = False
            for seller in my_shop.sellers:
                if seller.username==name and seller.password==password:
                    seller_menu(seller)
                    flag = True
                    break
            if flag==False:
                print('Wrong username or password!')
        elif n==2:
            name = input('Enter your username: ')
            password = input('Enter your password: ')
            flag = False
            for buyer in my_shop.buyers:
                if buyer.username==name and buyer.password==password:
                    buyer_menu(buyer)
                    flag = True
                    break
            if flag==False:
                print('Wrong username or password!')
        elif n==3:
            break
        else:
            print('Invalid input!')

def seller_signup():
    name = input('\nEnter your username: ')
    password = input('Enter your password: ')
    
    seller = Seller(username=name, password=password)
    my_shop.sellers.append(seller)
    
    while True:
        print('\n1. Create another seller account')
        print('2. Back to main menu')
        n = int(input('Enter an option: '))
        if n==1:
            seller_signup()
        elif n==2:
            break
        else:
            print('Invalid input!')

def buyer_signup():
    name = input('\nEnter your username: ')
    password = input('Enter your password: ')
    
    buyer = Buyer(username=name, password=password)
    my_shop.buyers.append(buyer)
    
    while True:
        print('\n1. Create another buyer account')
        print('2. Back to main menu')
        n = int(input('Enter an option: '))
        if n==1:
            buyer_signup()
        elif n==2:
            break
        else:
            print('Invalid input!')

def seller_menu(seller):
    while True:
        print(f'\nHello {seller.username}!\n')
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
            
def buyer_menu(buyer):
    while True:
        print(f'\nHey {buyer.username}!\n')
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
    print('\n1. Sign up as a customer')
    print('2. Sign up as a seller')
    print('3. Sign in')
    print('4. Exit')
    op = int(input('Please enter your choice: '))
    
    if op==1:
        buyer_signup()
    elif op==2:
        seller_signup()
    elif op==3:
        signin_menu()
    elif op==4:
        break
    else:
        print('Invalid choice!')
        
