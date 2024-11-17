from user import User
from person import Person

class Admin(Person):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        
    def create_account(self, name, email, address, account_type, bank):
        user = User(name, email, address, account_type)
        bank.users[name] = user
        print(f'\nAccount created successfully! Account Number: {user.account_number}.')
        
    def delete_account(self, bank, name):
        if name in bank.users:
            del bank.users[name]
            print('\nAccount delete successfully.')
        else:
            print('\nAccount does not exist.')
            
    def view_users(self, bank):
        print('\nName\tAccount Number\tBalance')
        for user in bank.users.values():
            print(f'{user.name}\t{user.account_number}\t{user.balance}')
            
    def total_loan_amount(self, bank):
        print(f'\nTotal loan amount of the {bank.name} is {bank.total_loan_balance}.')
        
    def total_available_balance(self, bank):
        print(f'\nTotal available balance of the {bank.name} is {bank.total_balance}.')
        
    def toggle_loan_feature(self, bank, status):
        bank.loan_feature = status
        print(f'\nLoan feature {'enabled' if status else 'disabled'}.')

    def toggle_isbankrupt(self, bank, status):
        bank.isbankrupt = status
        if status:
            print(f'\n{bank.name} is bankrupted.')
        else:
            print(f'\n{bank.name} is not crupted anymore.')
