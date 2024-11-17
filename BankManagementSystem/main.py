from bank import Bank
from user import User
from admin import Admin

bank = Bank('Emon\'s Bank')

def admin_panel():
    name = input('\nEnter your name: ')
    email = input('Enter your email: ')
    address = input('Enter your address: ')
    
    admin = Admin(name=name, email=email, address=address)
    
    while True:
        print(f'\nHello, {admin.name}!')
        print('1. Create user account')
        print('2. Delete user account')
        print('3. View all users')
        print('4. View total available balance of the bank')
        print('5. View total loan amount of the bank')
        print('6. Change loan feature')
        print('7. Change bankrupt status')
        print('8. Exit')
        option = int(input('Please enter an option: '))
        
        if option==1:
            u_name = input('\nEnter user name: ')
            u_email = input('Enter user email: ')
            u_address = input('Enter user address: ')
            type = input('Enter account type: ')
            admin.create_account(u_name, u_email, u_address, type, bank)
        elif option==2:
            user_name = input('\nEnter user name: ')
            admin.delete_account(bank, user_name)
        elif option==3:
            admin.view_users(bank)
        elif option==4:
            admin.total_available_balance(bank)
        elif option==5:
            admin.total_loan_amount(bank)
        elif option==6:
            status_input = input('\nEnter loan feature status (True/False): ').strip().lower()
            status = None
            if status_input in ['true', '1', 'yes']:
                status = True
            elif status_input in ['false', '0', 'no']:
                status = False
            else:
                print('\nInvalid input! Keeping the previous loan feature status.')
                status = bank.loan_feature 
            admin.toggle_loan_feature(bank, status)
        elif option==7:
            status_input = input('\nEnter bankrupt status (True/False): ').strip().lower()
            status = None
            if status_input in ['true', '1', 'yes']:
                status = True
            elif status_input in ['false', '0', 'no']:
                status = False
            else:
                print('\nInvalid input! Keeping the bankrupt feature status.')
                status = bank.isbankrupt 
            admin.toggle_isbankrupt(bank, status)
        elif option==8:
            break
        else:
            print('\nInvalid option!')

def user_panel():
    name = input('\nEnter your name: ')
    email = input('Enter your email: ')
    address = input('Enter your address: ')
    type = input('Enter account type: ')
    
    user = User(name=name, email=email, address=address, account_type=type)
    bank.users[name] = user
    
    while True:
        print(f'\nHello, {user.name}!')
        print('1. Deposite balance')
        print('2. Withdraw balance')
        print('3. Check balance')
        print('4. View transaction history')
        print('5. Request for loan')
        print('6. Transfer balance')
        print('7. Exit')
        option = int(input('Please enter an option: '))
        
        if option==1:
            amount = int(input('\nPlease enter your deposite amount: '))
            user.deposite(bank, amount)
        elif option==2:
            amount = int(input('\nPlease enter your withdrawal amount: '))
            user.withdraw(bank, amount)
        elif option==3:
            user.check_balance()
        elif option==4:
            user.check_transaction_history()
        elif option==5:
            amount = int(input('\nPlease enter your desired loan amount: '))
            user.take_loan(bank, amount)
        elif option==6:
            r_name = input('\nPlease enter receiver name: ')
            amount = int(input('Please enter the amount you want to transfer: '))
            if r_name in bank.users:
                reciever = bank.users[r_name]
                user.transfer(amount, reciever)
            else:
                print('Reciever not found!')
        elif option==7:
            break
        else:
            print('\nInvalid option!')

print(f'\n*** Welcome to {bank.name} ***')
while True:
    print('\n1. Enter as a Admin')
    print('2. Enter as an User')
    print('3. Exit')
    op = int(input('Please enter an option: '))
    
    if op==1:
        admin_panel()
    elif op==2:
        user_panel()
    elif op==3:
        print(f'\nThank you for using {bank.name}.')
        break
    else:
        print('\nInvalid option!')
        
