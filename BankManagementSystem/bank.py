class Bank:
    def __init__(self, name):
        self.name = name
        self.users = {}
        self.total_balance = 0
        self.total_loan_balance = 0
        self.loan_feature = True
        self.isbankrupt = False
    
