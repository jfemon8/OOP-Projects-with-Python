from person import Person
import uuid
from datetime import datetime

class User(Person):
    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address)
        self.account_type = account_type
        self.balance = 0
        self.loan_balance = 0
        self.loan_tocken = 0
        self.account_number = str(uuid.uuid4())[:8]
        self.transaction_history = []
        
    def deposite(self, bank, amount):
        if amount > 0:
            self.balance += amount
            bank.total_balance += amount
            self.transaction_history.append(f'Date: {datetime.now()}\tDeposite: {amount}')
            print(f'\nTaka {amount} has been deposited to your account. Current balance: {self.balance}.')
        else:
            print('\nDeposite amount must be greater than 0.')
            
    def withdraw(self, bank, amount):
        if amount <= self.balance and amount <= bank.total_balance and amount > 0:
            self.balance -= amount
            bank.total_balance -= amount
            self.transaction_history.append(f'Date: {datetime.now()}\tWithdraw: {amount}')
            print(f'\nTaka {amount} has been withdraw successfully. Current balance: {self.balance}.')
        elif amount > bank.total_balance or bank.isbankrupt:
            print('\nSorry!! The bank is bankrupt!')
        elif amount > self.balance:
            print('\nWithdrawal amount exceeded!')
        else:
            print('\nWithdrawal amount must be positive.')
            
    def check_balance(self):
        print(f'\nCurrent balance: {self.balance}\tLoan balance: {self.loan_balance}')
        
    def check_transaction_history(self):
        print('\n** Transaction History **')
        for history in self.transaction_history:
            print(history)
            
    def take_loan(self, bank, amount):
        if not bank.loan_feature:
            print('\nSorry! The loan feature is currently off!!')
        elif amount <= 0:
            print('\nAmount must be positive.')
        elif amount > bank.total_balance or bank.isbankrupt:
            print('\nSorry!! The bank is bankrupt and cannot approve loans!')
        elif self.loan_tocken >= 2:
            print('\nLoan limit exceeded!')
        else:
            self.balance += amount
            self.loan_balance += amount
            bank.total_balance -= amount
            bank.total_loan_balance += amount
            self.loan_tocken += 1
            self.transaction_history.append(f'Date: {datetime.now()}\tLoan Taken: {amount}')
            print(f'\nYour loan request has been approved. Current balance: {self.balance} and Loan balance: {self.loan_balance}')
            
    def transfer(self, amount, receiver):
        if amount <= 0:
            print('\nAmount must be positive.')
        elif amount > self.balance:
            print('\nInsufficient balance for transfer!')
        else:
            self.balance -= amount
            receiver.balance += amount
            self.transaction_history.append(f'Date: {datetime.now()}\tTransferred {amount} to {receiver.name}')
            receiver.transaction_history.append(f'Date: {datetime.now()}\tReceived {amount} from {self.name}')
            print(f'\nTaka {amount} has been transferred from {self.name} to {receiver.name} successfully.')
            
    